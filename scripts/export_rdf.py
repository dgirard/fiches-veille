#!/usr/bin/env python3
"""export_rdf.py — exporte les triples du GrapheDeConnaissance en Turtle (stdlib).

Produit l'ABox du corpus, à charger avec l'ontologie formelle
`docs/reference/ontologie-kg.ttl` (TBox) dans un raisonneur OWL pour vérifier
que les triples respectent les domaines, portées et disjonctions de types.

    python3 scripts/export_rdf.py                    # → gold/rdf/corpus.ttl
    python3 scripts/export_rdf.py -o /tmp/corpus.ttl

Vérification avec open-ontologies (binaire externe, non requis par le pipeline) :

    open-ontologies batch --no-connect --data-dir <dir> <fichier>
    # fichier : load docs/reference/ontologie-kg.ttl
    #           load gold/rdf/corpus.ttl
    #           reason --profile owl-rl     (puis owl-dl)

Choix de modélisation :
- une entité = un individu par (nom, type), comme la dédup de la KB : les
  homonymes de types différents (`Cursor` ORGANISATION / TECHNOLOGIE) restent
  distincts, conformément à `ontologie-kg.md` ;
- un objet épistémique (AFFIRMATION / MESURE / CITATION) = un individu propre à
  la fiche, jamais partagé ;
- confiance, temporalité et source ne sont pas exportées (le contrôle porte
  sur les types).
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fiche_lib import parse_fiche, parse_markdown_table  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

CLASSES = {
    "PERSONNE": "Personne", "ORGANISATION": "Organisation",
    "TECHNOLOGIE": "Technologie", "CONCEPT": "Concept",
    "METHODOLOGIE": "Methodologie", "EVENEMENT": "Evenement", "LIEU": "Lieu",
    "DOCUMENT": "Document", "AFFIRMATION": "Affirmation", "MESURE": "Mesure",
    "CITATION": "Citation",
}
EPISTEMIQUES = {"AFFIRMATION", "MESURE", "CITATION"}

PREFIXES = """@prefix v: <https://veille.example/onto#> .
@prefix e: <https://veille.example/e/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
"""


def _slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")[:60] or "x"


def _hash(s: str, n: int) -> str:
    return hashlib.md5(s.encode("utf-8")).hexdigest()[:n]


def node_iri(nom: str, typ: str, fiche_id: str) -> str:
    if typ in EPISTEMIQUES:
        return f"e:{_slug(fiche_id)}_{_hash(nom, 8)}"
    return f"e:{typ}__{_slug(nom)}_{_hash(nom.lower(), 6)}"


def predicate_iri(predicat: str) -> str:
    """`s_oppose_à` → `v:s_oppose_a` (IRI ASCII, cf. ontologie-kg.ttl)."""
    return "v:" + predicat.replace("à", "a").replace("é", "e").replace("ê", "e")


def _literal(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def triples_of(path: Path) -> list[dict]:
    kg = parse_fiche(path).sections.get("GrapheDeConnaissance", "")
    bloc = kg.split("### Triples", 1)
    if len(bloc) < 2:
        return []
    return parse_markdown_table(bloc[1].split("### Entités", 1)[0].splitlines())


def export(root: Path) -> tuple[str, int, int]:
    out = [PREFIXES]
    seen: set[str] = set()
    n = 0
    for path in sorted(root.glob("fiches/*/*.md")):
        for row in triples_of(path):
            ts, to = row.get("Type Sujet", ""), row.get("Type Objet", "")
            if ts not in CLASSES or to not in CLASSES:
                continue
            s_iri = node_iri(row["Sujet"], ts, path.stem)
            o_iri = node_iri(row["Objet"], to, path.stem)
            for iri, nom, typ in ((s_iri, row["Sujet"], ts), (o_iri, row["Objet"], to)):
                if iri not in seen:
                    seen.add(iri)
                    out.append(f"{iri} a v:{CLASSES[typ]} ; rdfs:label {_literal(nom)} .")
            out.append(f"{s_iri} {predicate_iri(row['Prédicat'])} {o_iri} .")
            n += 1
    return "\n".join(out) + "\n", n, len(seen)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("-o", "--output", default=str(ROOT / "gold" / "rdf" / "corpus.ttl"))
    args = ap.parse_args()
    ttl, n, nodes = export(ROOT)
    dest = Path(args.output)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(ttl, encoding="utf-8")
    print(f"✓ {n} triples, {nodes} nœuds → {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
