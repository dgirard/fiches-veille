#!/usr/bin/env python3
"""
Consolide toutes les sections GrapheDeConnaissance des fiches de veille
en une Knowledge Base multi-fichiers Obsidian avec wikilinks.

Génère :
- knowledge-base.md : Dashboard léger
- kb/*.md : Pages entités individuelles + index
"""

import os
import re
import shutil
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path


# ─── Parsing & déduplication (inchangés) ─────────────────────────────────────


def normalize_name(name: str) -> str:
    """Normalise un nom d'entité pour la déduplication."""
    return name.strip().lower()


def parse_markdown_table(lines: list[str]) -> list[dict]:
    """Parse un tableau Markdown et retourne une liste de dicts."""
    rows = []
    headers = None
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        # Retirer les éléments vides au début et à la fin
        cells = [c for c in cells if c != "" or cells.index(c) not in (0, len(cells) - 1)]
        # Nettoyer les cellules vides aux extrémités dues au split
        while cells and cells[0] == "":
            cells.pop(0)
        while cells and cells[-1] == "":
            cells.pop()

        if not cells:
            continue
        # Détecter la ligne de séparateur (---|---)
        if all(set(c.strip()) <= set("-: ") for c in cells):
            continue
        if headers is None:
            headers = cells
        else:
            if len(cells) >= len(headers):
                row = {headers[i]: cells[i] for i in range(len(headers))}
            else:
                row = {}
                for i, h in enumerate(headers):
                    row[h] = cells[i] if i < len(cells) else ""
            rows.append(row)
    return rows


def extract_graphe_connaissance(filepath: str) -> tuple[list[dict], list[dict], str]:
    """Extrait les triples et entités d'une fiche. Retourne (triples, entités, fiche_id)."""
    fiche_id = Path(filepath).stem

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Trouver la section GrapheDeConnaissance
    gc_match = re.search(r"^## GrapheDeConnaissance\s*$", content, re.MULTILINE)
    if not gc_match:
        return [], [], fiche_id

    gc_content = content[gc_match.end():]

    # Extraire la section Triples
    triples_match = re.search(r"^### Triples\s*$", gc_content, re.MULTILINE)
    entites_match = re.search(r"^### Entités\s*$", gc_content, re.MULTILINE)

    triples = []
    entites = []

    if triples_match:
        # Le contenu des triples va de ### Triples jusqu'à ### Entités ou fin
        start = triples_match.end()
        end = entites_match.start() if entites_match else len(gc_content)
        triples_text = gc_content[start:end]
        triples = parse_markdown_table(triples_text.split("\n"))

    if entites_match:
        start = entites_match.end()
        # Chercher la prochaine section ## ou fin
        next_section = re.search(r"^## ", gc_content[start:], re.MULTILINE)
        end = start + next_section.start() if next_section else len(gc_content)
        entites_text = gc_content[start:end]
        entites = parse_markdown_table(entites_text.split("\n"))

    return triples, entites, fiche_id


def deduplicate_entities(all_entities: list[tuple[dict, str]]) -> list[dict]:
    """Déduplique les entités. all_entities = [(entity_dict, fiche_id), ...]"""
    # Grouper par (nom normalisé, type)
    groups = defaultdict(list)
    for entity, fiche_id in all_entities:
        name = entity.get("Entité", "").strip()
        etype = entity.get("Type", "").strip()
        key = (normalize_name(name), normalize_name(etype))
        groups[key].append((entity, fiche_id))

    deduplicated = []
    for key, items in sorted(groups.items()):
        # Choisir le nom le plus fréquent (forme originale)
        name_counts = defaultdict(int)
        type_counts = defaultdict(int)
        attributes = {}
        fiches = set()

        for entity, fiche_id in items:
            name = entity.get("Entité", "").strip()
            etype = entity.get("Type", "").strip()
            attr = entity.get("Attribut", "").strip()
            val = entity.get("Valeur", "").strip()
            name_counts[name] += 1
            type_counts[etype] += 1
            if attr and val:
                attributes[attr] = val
            fiches.add(fiche_id)

        # Nom le plus fréquent
        best_name = max(name_counts, key=name_counts.get)
        best_type = max(type_counts, key=type_counts.get)

        deduplicated.append({
            "name": best_name,
            "type": best_type,
            "attributes": attributes,
            "fiches": sorted(fiches),
            "occurrences": len(items),
        })

    return deduplicated


def deduplicate_triples(all_triples: list[tuple[dict, str]]) -> list[dict]:
    """Déduplique les triples. all_triples = [(triple_dict, fiche_id), ...]"""
    groups = defaultdict(list)
    for triple, fiche_id in all_triples:
        sujet = normalize_name(triple.get("Sujet", ""))
        predicat = normalize_name(triple.get("Prédicat", ""))
        objet = normalize_name(triple.get("Objet", ""))
        key = (sujet, predicat, objet)
        groups[key].append((triple, fiche_id))

    deduplicated = []
    for key, items in sorted(groups.items()):
        # Meilleure confiance
        best_confidence = 0.0
        best_triple = items[0][0]
        fiches = set()
        sources = set()
        temporalites = set()

        for triple, fiche_id in items:
            try:
                conf = float(triple.get("Confiance", "0"))
            except ValueError:
                conf = 0.0
            if conf > best_confidence:
                best_confidence = conf
                best_triple = triple
            fiches.add(fiche_id)
            sources.add(triple.get("Source", "").strip())
            temporalites.add(triple.get("Temporalité", "").strip())

        # Temporalité : DYNAMIQUE > STATIQUE > ATEMPOREL si conflit
        if "DYNAMIQUE" in temporalites:
            temporalite = "DYNAMIQUE"
        elif "STATIQUE" in temporalites:
            temporalite = "STATIQUE"
        else:
            temporalite = "ATEMPOREL"

        deduplicated.append({
            "sujet": best_triple.get("Sujet", "").strip(),
            "type_sujet": best_triple.get("Type Sujet", "").strip(),
            "predicat": best_triple.get("Prédicat", "").strip(),
            "objet": best_triple.get("Objet", "").strip(),
            "type_objet": best_triple.get("Type Objet", "").strip(),
            "confiance": best_confidence,
            "temporalite": temporalite,
            "sources": sorted(sources),
            "fiches": sorted(fiches),
            "occurrences": len(items),
        })

    return deduplicated


# ─── Résolution noms / chemins ───────────────────────────────────────────────


def entity_to_filename(name: str) -> str:
    """Convertit un nom d'entité en nom de fichier. 'Claude Code' → 'Claude-Code'."""
    # Remplacer espaces et caractères spéciaux par des tirets
    filename = re.sub(r"[/\\:*?\"<>|]", "-", name)
    filename = re.sub(r"\s+", "-", filename)
    # Supprimer les tirets en double et en début/fin
    filename = re.sub(r"-+", "-", filename).strip("-")
    return filename


def extract_fiche_veille(filepath: str) -> str:
    """Extrait la ligne ## Veille d'une fiche pour l'utiliser comme alias."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("## Veille"):
                    continue
                if line.startswith("## "):
                    break
                if line and not line.startswith("#"):
                    return line
    except (OSError, UnicodeDecodeError):
        pass
    return ""


def build_fiche_metadata(fiches_dir: Path) -> tuple[dict, dict]:
    """Construit les index fiche_id → chemin relatif et fiche_id → veille.

    Returns:
        (fiche_paths, fiche_veilles) :
            fiche_paths[fiche_id] = "fiches/YYYY-MM/fiche_id"
            fiche_veilles[fiche_id] = "Texte veille"
    """
    fiche_paths = {}
    fiche_veilles = {}
    for fiche_path in sorted(fiches_dir.rglob("*.md")):
        fiche_id = fiche_path.stem
        # Chemin relatif depuis la racine du projet (sans .md pour wikilink)
        rel = fiche_path.relative_to(fiches_dir.parent)
        fiche_paths[fiche_id] = str(rel).replace(".md", "")
        veille = extract_fiche_veille(str(fiche_path))
        if veille:
            fiche_veilles[fiche_id] = veille
    return fiche_paths, fiche_veilles


# ─── Classification entités majeures / mineures ─────────────────────────────


def classify_entities(entities: list[dict], triples: list[dict],
                      threshold: int = 3) -> tuple[set, set]:
    """Classifie les entités en majeures et mineures.

    Majeure = 3+ triples comme sujet OU 3+ fiches sources.
    Returns (major_names, minor_names) — ensembles de noms normalisés.
    """
    # Compter les triples comme sujet par entité normalisée
    subject_counts = defaultdict(int)
    for t in triples:
        subject_counts[normalize_name(t["sujet"])] += 1

    major = set()
    minor = set()
    for e in entities:
        nname = normalize_name(e["name"])
        subj_count = subject_counts.get(nname, 0)
        fiche_count = len(e["fiches"])
        if subj_count >= threshold or fiche_count >= threshold:
            major.add(nname)
        else:
            minor.add(nname)

    return major, minor


def compute_incoming_triples(triples: list[dict]) -> dict:
    """Calcule les triples entrants (comme objet) par entité normalisée."""
    incoming = defaultdict(list)
    for t in triples:
        incoming[normalize_name(t["objet"])].append(t)
    return incoming


# ─── Wikilinks ───────────────────────────────────────────────────────────────


def entity_wikilink(name: str, major_set: set, entity_filenames: dict) -> str:
    """Génère un wikilink vers une entité.

    entity_filenames: {nom_normalisé: filename} pour les majeures.
    """
    nname = normalize_name(name)
    if nname in major_set:
        filename = entity_filenames.get(nname, entity_to_filename(name))
        return f"[[kb/{filename}\\|{name}]]"
    else:
        anchor = entity_to_filename(name)
        return f"[[kb/_entites-mineures#{anchor}\\|{name}]]"


def fiche_wikilink(fiche_id: str, fiche_paths: dict, fiche_veilles: dict) -> str:
    """Génère un wikilink vers une fiche source."""
    path = fiche_paths.get(fiche_id, f"fiches/{fiche_id}")
    alias = fiche_veilles.get(fiche_id, fiche_id)
    return f"[[{path}\\|{alias}]]"


# ─── Génération multi-fichiers ───────────────────────────────────────────────


def generate_entity_page(entity: dict, subject_triples: list[dict],
                         object_triples: list[dict], major_set: set,
                         entity_filenames: dict, fiche_paths: dict,
                         fiche_veilles: dict) -> str:
    """Génère le contenu d'une page entité individuelle."""
    lines = []
    name = entity["name"]
    etype = entity["type"]
    total_relations = len(subject_triples) + len(object_triples)

    lines.append(f"# {name}")
    lines.append("")
    lines.append(f"> **Type** : {etype} | {total_relations} relations | {len(entity['fiches'])} fiches sources")
    lines.append("")

    # Attributs
    if entity["attributes"]:
        lines.append("## Attributs")
        lines.append("")
        for attr, val in sorted(entity["attributes"].items()):
            lines.append(f"- **{attr}** : {val}")
        lines.append("")

    # Relations comme sujet, groupées par prédicat
    if subject_triples:
        lines.append("## Relations (comme sujet)")
        lines.append("")

        # Grouper par prédicat
        by_predicat = defaultdict(list)
        for t in subject_triples:
            by_predicat[t["predicat"]].append(t)

        for pred in sorted(by_predicat.keys()):
            pred_triples = sorted(by_predicat[pred],
                                  key=lambda t: -t["confiance"])
            lines.append(f"### {pred}")
            lines.append("")
            for t in pred_triples:
                obj_link = entity_wikilink(t["objet"], major_set, entity_filenames)
                conf = f"{t['confiance']:.2f}"
                temp = t["temporalite"]
                line = f"- {obj_link} ({t['type_objet']}) — {conf}, {temp}"
                lines.append(line)
                # Fiches sources de ce triple
                for fid in t["fiches"]:
                    lines.append(f"  - {fiche_wikilink(fid, fiche_paths, fiche_veilles)}")
            lines.append("")

    # Relations comme objet (entrantes)
    if object_triples:
        lines.append("## Relations (comme objet)")
        lines.append("")
        for t in sorted(object_triples, key=lambda t: (-t["confiance"], t["predicat"])):
            subj_link = entity_wikilink(t["sujet"], major_set, entity_filenames)
            lines.append(f"- {subj_link} **{t['predicat']}** → {name} — {t['confiance']:.2f}")
        lines.append("")

    # Fiches sources
    if entity["fiches"]:
        lines.append("## Fiches sources")
        lines.append("")
        for fid in entity["fiches"]:
            lines.append(f"- {fiche_wikilink(fid, fiche_paths, fiche_veilles)}")
        lines.append("")

    return "\n".join(lines)


def generate_minor_entities_page(minor_entities: list[dict], triples: list[dict],
                                 incoming: dict, major_set: set,
                                 entity_filenames: dict, fiche_paths: dict,
                                 fiche_veilles: dict) -> str:
    """Génère la page des entités mineures, groupées par type."""
    lines = []
    lines.append("# Entités mineures")
    lines.append("")
    lines.append(f"> {len(minor_entities)} entités avec moins de 3 triples/fiches")
    lines.append("")

    # Grouper par type
    by_type = defaultdict(list)
    for e in minor_entities:
        by_type[e["type"]].append(e)

    type_order = ["PERSONNE", "ORGANISATION", "TECHNOLOGIE", "CONCEPT",
                  "METHODOLOGIE", "EVENEMENT", "LIEU"]
    for t in sorted(by_type.keys()):
        if t not in type_order:
            type_order.append(t)

    # Index des triples par sujet (normalisé)
    triples_by_subj = defaultdict(list)
    for t in triples:
        triples_by_subj[normalize_name(t["sujet"])].append(t)

    for etype in type_order:
        if etype not in by_type:
            continue
        ents = sorted(by_type[etype], key=lambda e: e["name"])
        lines.append(f"## {etype} ({len(ents)})")
        lines.append("")

        for e in ents:
            anchor = entity_to_filename(e["name"])
            nname = normalize_name(e["name"])
            subj_triples = triples_by_subj.get(nname, [])
            obj_triples = incoming.get(nname, [])
            total_rel = len(subj_triples) + len(obj_triples)

            lines.append(f"### {e['name']} {{#{anchor}}}")
            lines.append("")
            lines.append(f"**Type** : {e['type']} | {total_rel} relations | {len(e['fiches'])} fiches")
            lines.append("")

            # Attributs
            if e["attributes"]:
                for attr, val in sorted(e["attributes"].items()):
                    lines.append(f"- **{attr}** : {val}")
                lines.append("")

            # Relations comme sujet (compact)
            if subj_triples:
                for t in sorted(subj_triples, key=lambda t: -t["confiance"]):
                    obj_link = entity_wikilink(t["objet"], major_set, entity_filenames)
                    lines.append(f"- **{t['predicat']}** → {obj_link} ({t['type_objet']}) — {t['confiance']:.2f}")
                lines.append("")

            # Relations comme objet (compact)
            if obj_triples:
                for t in sorted(obj_triples, key=lambda t: -t["confiance"]):
                    subj_link = entity_wikilink(t["sujet"], major_set, entity_filenames)
                    lines.append(f"- {subj_link} **{t['predicat']}** → {e['name']} — {t['confiance']:.2f}")
                lines.append("")

            # Fiches
            if e["fiches"]:
                lines.append("**Fiches** : " + ", ".join(
                    fiche_wikilink(fid, fiche_paths, fiche_veilles)
                    for fid in e["fiches"]
                ))
                lines.append("")

    return "\n".join(lines)


def generate_type_index(etype: str, entities: list[dict], major_set: set,
                        entity_filenames: dict) -> str:
    """Génère un index par type d'entité."""
    lines = []
    type_entities = [e for e in entities if e["type"] == etype]
    type_entities.sort(key=lambda e: e["name"])

    lines.append(f"# Index — {etype}")
    lines.append("")
    lines.append(f"> {len(type_entities)} entités de type {etype}")
    lines.append("")

    for e in type_entities:
        link = entity_wikilink(e["name"], major_set, entity_filenames)
        attrs_str = ""
        if e["attributes"]:
            first_attr = next(iter(e["attributes"].items()))
            attrs_str = f" — {first_attr[0]}: {first_attr[1]}"
        lines.append(f"- {link}{attrs_str} ({e['occurrences']} occ., {len(e['fiches'])} fiches)")

    lines.append("")
    return "\n".join(lines)


def generate_alpha_index(entities: list[dict], major_set: set,
                         entity_filenames: dict) -> str:
    """Génère un index alphabétique de toutes les entités."""
    lines = []
    lines.append("# Index alphabétique des entités")
    lines.append("")
    lines.append(f"> {len(entities)} entités")
    lines.append("")

    sorted_entities = sorted(entities, key=lambda e: e["name"].upper())

    current_letter = ""
    for e in sorted_entities:
        first = e["name"][0].upper() if e["name"] else "?"
        # Grouper les caractères non-alphabétiques
        if not first.isalpha():
            first = "#"
        if first != current_letter:
            current_letter = first
            lines.append(f"## {current_letter}")
            lines.append("")

        link = entity_wikilink(e["name"], major_set, entity_filenames)
        lines.append(f"- {link} ({e['type']}, {len(e['fiches'])} fiches)")

    lines.append("")
    return "\n".join(lines)


def generate_dashboard(entities: list[dict], triples: list[dict],
                       major_set: set, entity_filenames: dict,
                       num_fiches: int, total_raw_triples: int,
                       total_raw_entities: int,
                       entities_by_type: dict) -> str:
    """Génère le dashboard léger knowledge-base.md."""
    lines = []
    today = date.today().isoformat()

    lines.append("# Knowledge Base — Veille Technologique")
    lines.append("")
    lines.append(f"> {num_fiches} fiches | {len(entities)} entités | {len(triples)} triples | Généré le {today}")
    lines.append("")

    # Navigation
    lines.append("## Navigation")
    lines.append("")
    lines.append("- [[kb/_index-entites\\|Index alphabétique]]")

    type_order = ["PERSONNE", "ORGANISATION", "TECHNOLOGIE", "CONCEPT",
                  "METHODOLOGIE", "EVENEMENT", "LIEU"]
    for t in sorted(entities_by_type.keys()):
        if t not in type_order:
            type_order.append(t)

    for etype in type_order:
        if etype not in entities_by_type:
            continue
        count = len(entities_by_type[etype])
        lines.append(f"- [[kb/_index-type-{etype}\\|{etype}]] ({count})")
    lines.append(f"- [[kb/_entites-mineures\\|Entités mineures]] ({len(entities) - len(major_set)})")
    lines.append("")

    # Entités les plus connectées
    lines.append("## Entités les plus connectées")
    lines.append("")
    lines.append("| Entité | Type | Relations | Fiches |")
    lines.append("|--------|------|-----------|--------|")

    # Calculer le nombre total de relations (sujet + objet) par entité
    relation_counts = defaultdict(int)
    for t in triples:
        relation_counts[normalize_name(t["sujet"])] += 1
        relation_counts[normalize_name(t["objet"])] += 1

    # Construire le lookup nom normalisé → entité
    entity_lookup = {}
    for e in entities:
        entity_lookup[normalize_name(e["name"])] = e

    top_entities = sorted(relation_counts.items(), key=lambda x: -x[1])[:20]
    for nname, rel_count in top_entities:
        e = entity_lookup.get(nname)
        if not e:
            continue
        link = entity_wikilink(e["name"], major_set, entity_filenames)
        lines.append(f"| {link} | {e['type']} | {rel_count} | {len(e['fiches'])} |")
    lines.append("")

    # Statistiques
    lines.append("## Statistiques")
    lines.append("")

    # Prédicats les plus fréquents
    lines.append("### Prédicats les plus fréquents")
    lines.append("")
    predicat_counts = defaultdict(int)
    for t in triples:
        predicat_counts[t["predicat"]] += 1
    for pred, count in sorted(predicat_counts.items(), key=lambda x: -x[1])[:15]:
        lines.append(f"- **{pred}** : {count}")
    lines.append("")

    # Distribution par type
    lines.append("### Distribution par type")
    lines.append("")
    for etype in type_order:
        if etype not in entities_by_type:
            continue
        count = len(entities_by_type[etype])
        pct = count / len(entities) * 100 if entities else 0
        lines.append(f"- **{etype}** : {count} ({pct:.1f}%)")
    lines.append("")

    # Déduplication
    lines.append("### Déduplication")
    lines.append("")
    lines.append(f"- **Triples** : {total_raw_triples} → {len(triples)} ({total_raw_triples - len(triples)} doublons)")
    lines.append(f"- **Entités** : {total_raw_entities} → {len(entities)} ({total_raw_entities - len(entities)} doublons)")
    lines.append("")

    return "\n".join(lines)


# ─── I/O ─────────────────────────────────────────────────────────────────────


def write_output_files(base_dir: Path, files: dict[str, str]):
    """Écrit les fichiers générés et nettoie les fichiers obsolètes dans kb/."""
    kb_dir = base_dir / "kb"
    kb_dir.mkdir(exist_ok=True)

    # Fichiers attendus dans kb/
    expected_kb_files = set()

    for rel_path, content in files.items():
        filepath = base_dir / rel_path
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        if rel_path.startswith("kb/"):
            expected_kb_files.add(filepath.name)

    # Nettoyer les fichiers obsolètes dans kb/
    for existing in kb_dir.iterdir():
        if existing.is_file() and existing.suffix == ".md":
            if existing.name not in expected_kb_files:
                print(f"  Suppression fichier obsolète : {existing}")
                existing.unlink()


# ─── Main ────────────────────────────────────────────────────────────────────


def main():
    fiches_dir = Path(__file__).parent.parent / "fiches"
    base_dir = Path(__file__).parent.parent

    print(f"Scanning fiches in {fiches_dir}...")

    # 1. Parse toutes les fiches (inchangé)
    all_triples = []
    all_entities = []
    num_fiches = 0

    for fiche_path in sorted(fiches_dir.rglob("*.md")):
        triples, entites, fiche_id = extract_graphe_connaissance(str(fiche_path))
        if triples or entites:
            num_fiches += 1
            for t in triples:
                all_triples.append((t, fiche_id))
            for e in entites:
                all_entities.append((e, fiche_id))

    total_raw_triples = len(all_triples)
    total_raw_entities = len(all_entities)

    print(f"Fiches avec GrapheDeConnaissance: {num_fiches}")
    print(f"Triples bruts: {total_raw_triples}")
    print(f"Entités brutes: {total_raw_entities}")

    # 2. Déduplique entités et triples (inchangé)
    print("Déduplication des entités...")
    unique_entities = deduplicate_entities(all_entities)

    print("Déduplication des triples...")
    unique_triples = deduplicate_triples(all_triples)

    print(f"Entités uniques: {len(unique_entities)}")
    print(f"Triples uniques: {len(unique_triples)}")

    # 3. Extrait les métadonnées fiches (Veille + chemin)
    print("Extraction métadonnées fiches...")
    fiche_paths, fiche_veilles = build_fiche_metadata(fiches_dir)

    # 4. Classifie entités (majeure/mineure)
    print("Classification entités...")
    major_set, minor_set = classify_entities(unique_entities, unique_triples)
    major_entities = [e for e in unique_entities if normalize_name(e["name"]) in major_set]
    minor_entities = [e for e in unique_entities if normalize_name(e["name"]) in minor_set]
    print(f"  Majeures: {len(major_entities)}, Mineures: {len(minor_entities)}")

    # 5. Calcule les triples entrants par objet
    incoming = compute_incoming_triples(unique_triples)

    # Index des triples par sujet (normalisé)
    triples_by_subj = defaultdict(list)
    for t in unique_triples:
        triples_by_subj[normalize_name(t["sujet"])].append(t)

    # Construire le mapping nom normalisé → filename pour les entités majeures
    entity_filenames = {}
    for e in major_entities:
        nname = normalize_name(e["name"])
        entity_filenames[nname] = entity_to_filename(e["name"])

    # Entités par type (pour indexes)
    entities_by_type = defaultdict(list)
    for e in unique_entities:
        entities_by_type[e["type"]].append(e)

    # 6. Génération de tous les fichiers
    print("Génération des fichiers...")
    files = {}

    # Dashboard
    files["knowledge-base.md"] = generate_dashboard(
        unique_entities, unique_triples, major_set, entity_filenames,
        num_fiches, total_raw_triples, total_raw_entities, entities_by_type
    )

    # Pages entités majeures
    for e in major_entities:
        nname = normalize_name(e["name"])
        filename = entity_filenames[nname]
        subj_triples = triples_by_subj.get(nname, [])
        obj_triples = incoming.get(nname, [])
        files[f"kb/{filename}.md"] = generate_entity_page(
            e, subj_triples, obj_triples, major_set, entity_filenames,
            fiche_paths, fiche_veilles
        )

    # Index par type
    type_order = ["PERSONNE", "ORGANISATION", "TECHNOLOGIE", "CONCEPT",
                  "METHODOLOGIE", "EVENEMENT", "LIEU"]
    for t in sorted(entities_by_type.keys()):
        if t not in type_order:
            type_order.append(t)

    for etype in type_order:
        if etype not in entities_by_type:
            continue
        files[f"kb/_index-type-{etype}.md"] = generate_type_index(
            etype, unique_entities, major_set, entity_filenames
        )

    # Index alphabétique
    files["kb/_index-entites.md"] = generate_alpha_index(
        unique_entities, major_set, entity_filenames
    )

    # Entités mineures
    files["kb/_entites-mineures.md"] = generate_minor_entities_page(
        minor_entities, unique_triples, incoming, major_set, entity_filenames,
        fiche_paths, fiche_veilles
    )

    # 7. Écriture + nettoyage
    print(f"Écriture de {len(files)} fichiers...")
    write_output_files(base_dir, files)

    # Stats finales
    kb_files = [f for f in files if f.startswith("kb/")]
    entity_pages = [f for f in kb_files if not f.startswith("kb/_")]
    dashboard_lines = files["knowledge-base.md"].count("\n") + 1

    print(f"\nRésultat :")
    print(f"  knowledge-base.md : {dashboard_lines} lignes")
    print(f"  kb/ : {len(kb_files)} fichiers ({len(entity_pages)} pages entités + {len(kb_files) - len(entity_pages)} index)")
    print(f"  Entités majeures : {len(major_entities)}")
    print(f"  Entités mineures : {len(minor_entities)}")


if __name__ == "__main__":
    main()
