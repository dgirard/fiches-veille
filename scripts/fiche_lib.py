#!/usr/bin/env python3
"""fiche_lib.py — parsing partagé des fiches de veille (stdlib uniquement).

Source unique de vérité pour :
- le skip d'un bloc YAML frontmatter en tête (`skip_frontmatter`) ;
- un parseur frontmatter minimal (`parse_frontmatter`) — grammaire fermée,
  toute construction hors grammaire lève `FrontmatterError` en nommant la ligne ;
- l'extraction de la ligne `## Veille` utilisée comme alias (`extract_veille`) ;
- le parsing des tableaux markdown du GrapheDeConnaissance (`parse_markdown_table`) ;
- l'accès structuré à une fiche (`parse_fiche` → `Fiche`).

Consommé par `lint_fiches.py` (gate Bronze), `build_knowledge_base.py` (Silver),
`build_index.py` (index + catalogue) et `migrate_editorial_frontmatter.py`.

Contrat de non-régression : `skip_frontmatter`, `extract_veille` et
`parse_markdown_table` reproduisent à l'octet le comportement historique des
implémentations dupliquées qu'ils remplacent (tests `scripts/tests/`).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


# ─── Frontmatter ─────────────────────────────────────────────────────────────


class FrontmatterError(ValueError):
    """Frontmatter hors de la grammaire minimale supportée."""


def skip_frontmatter(lines: list[str]) -> list[str]:
    """Ignore un bloc YAML frontmatter en tête (`---` … `---`).

    Comportement historique (à ne pas régresser) : si la première ligne est
    `---`, on saute jusqu'au `---` fermant ; sinon on renvoie les lignes telles
    quelles. Un frontmatter non fermé n'est PAS skippé (start reste au début).
    """
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[i + 1:]
    return lines


def _scalar(raw: str) -> object:
    """Convertit une valeur scalaire : quotes retirées, booléens reconnus."""
    s = raw.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        return s[1:-1]
    if s == "true":
        return True
    if s == "false":
        return False
    return s


def parse_frontmatter(lines: list[str]) -> tuple[dict, list[str]]:
    """Parse un frontmatter minimal en tête ; retourne (frontmatter, reste).

    Grammaire supportée (fermée) :
    - `cle: valeur`           → scalaire (quotes simples/doubles englobantes
                                 retirées ; `true`/`false` → booléens) ;
    - `cle: [a, b, c]`        → liste flow ;
    - `cle:` puis lignes      → liste bloc :
        `  - item`                `themes:\n  - a\n  - b`

    Toute autre construction (map imbriquée, `|`/`>` multiligne, tag, ancre)
    lève `FrontmatterError` en nommant le numéro de ligne (1-indexé dans le
    bloc frontmatter). Une fiche sans frontmatter renvoie ({}, lines).
    Un frontmatter ouvert mais non fermé lève `FrontmatterError`.
    """
    if not lines or lines[0].strip() != "---":
        return {}, lines

    close = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            close = i
            break
    if close is None:
        raise FrontmatterError("frontmatter ouvert (`---`) jamais fermé")

    body = lines[1:close]
    fm: dict = {}
    i = 0
    while i < len(body):
        raw = body[i]
        line = raw.rstrip("\n")
        lineno = i + 2  # 1 = `---` d'ouverture ; corps commence à 2
        if not line.strip():
            i += 1
            continue
        if line[:1] in (" ", "\t"):
            raise FrontmatterError(
                f"ligne {lineno} : indentation inattendue « {line.strip()} » "
                f"(seules les listes bloc `  - item` sous une clé sont permises)"
            )
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if not m:
            raise FrontmatterError(
                f"ligne {lineno} : « {line.strip()} » n'est pas une clé `cle: valeur`"
            )
        key, val = m.group(1), m.group(2).strip()
        if val == "":
            # Liste bloc : lignes suivantes « - item » (indentées ou non).
            items: list[str] = []
            j = i + 1
            while j < len(body):
                nxt = body[j].rstrip("\n")
                if not nxt.strip():
                    j += 1
                    continue
                mm = re.match(r"^\s*-\s+(.*)$", nxt)
                if not mm:
                    break
                items.append(_scalar(mm.group(1)))
                j += 1
            fm[key] = items
            i = j
            continue
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            fm[key] = [_scalar(x) for x in inner.split(",") if x.strip()] if inner else []
        elif val.startswith(("|", ">")):
            raise FrontmatterError(
                f"ligne {lineno} : scalaire multiligne (`{val[0]}`) non supporté"
            )
        else:
            fm[key] = _scalar(val)
        i += 1

    return fm, lines[close + 1:]


# ─── Sections & tables ───────────────────────────────────────────────────────


def parse_markdown_table(lines: list[str]) -> list[dict]:
    """Parse un tableau Markdown → liste de dicts (en-tête → cellule).

    Comportement historique repris de `build_knowledge_base.parse_markdown_table`
    (à ne pas régresser).
    """
    rows = []
    headers = None
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        cells = [c for c in cells if c != "" or cells.index(c) not in (0, len(cells) - 1)]
        while cells and cells[0] == "":
            cells.pop(0)
        while cells and cells[-1] == "":
            cells.pop()
        if not cells:
            continue
        if all(set(c.strip()) <= set("-: ") for c in cells):
            continue
        if headers is None:
            headers = cells
        else:
            if len(cells) >= len(headers):
                row = {headers[i]: cells[i] for i in range(len(headers))}
            else:
                row = {h: (cells[i] if i < len(cells) else "") for i, h in enumerate(headers)}
            rows.append(row)
    return rows


def split_sections(body_lines: list[str]) -> dict[str, str]:
    """Découpe le corps (frontmatter déjà retiré) en sections `## Nom`.

    Retourne {nom_section: texte} ; le texte exclut la ligne d'en-tête et est
    délimité par la prochaine `## `. L'ordre d'insertion suit l'ordre du fichier.
    """
    sections: dict[str, str] = {}
    current = None
    buf: list[str] = []
    for line in body_lines:
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m and not line.startswith("###"):
            if current is not None:
                sections[current] = "\n".join(buf).strip("\n")
            current = m.group(1).strip()
            buf = []
        elif current is not None:
            buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf).strip("\n")
    return sections


def _first_content_line(text: str) -> str:
    """Première ligne non vide et non-`#` d'un bloc de section."""
    for line in text.splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            return s
    return ""


# ─── Extraction Veille (compat historique) ──────────────────────────────────


def extract_veille(filepath: str) -> str:
    """Extrait la ligne `## Veille` d'une fiche pour l'utiliser comme alias.

    Reproduit `build_knowledge_base.extract_fiche_veille` à l'identique :
    skip du frontmatter, puis première ligne non-`#` après l'en-tête `## Veille`.
    Erreurs de lecture → chaîne vide.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        start_idx = 0
        if lines and lines[0].strip() == "---":
            for i in range(1, len(lines)):
                if lines[i].strip() == "---":
                    start_idx = i + 1
                    break
        for line in lines[start_idx:]:
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


# ─── Accès structuré à une fiche ─────────────────────────────────────────────


@dataclass
class Fiche:
    """Représentation parsée d'une fiche. Champs dérivés des 10 sections."""
    id: str
    path: Path
    frontmatter: dict = field(default_factory=dict)
    sections: dict[str, str] = field(default_factory=dict)

    @property
    def titre(self) -> str:
        return _first_content_line(self.sections.get("Titre Article", ""))

    @property
    def date(self) -> str:
        return _first_content_line(self.sections.get("Date", ""))

    @property
    def auteurs(self) -> str:
        return _first_content_line(self.sections.get("Authors", ""))

    @property
    def source(self) -> str:
        """Source déclarée en frontmatter (chaîne vide si absente)."""
        return str(self.frontmatter.get("source", "") or "")

    @property
    def themes(self) -> list[str]:
        t = self.frontmatter.get("themes", [])
        return [str(x) for x in t] if isinstance(t, list) else [str(t)]

    @property
    def veille(self) -> str:
        return extract_veille(str(self.path))

    @property
    def keywords(self) -> str:
        return _first_content_line(self.sections.get("Keywords", ""))

    @property
    def has_kg(self) -> bool:
        return "GrapheDeConnaissance" in self.sections

    @property
    def is_skill(self) -> bool:
        return str(self.frontmatter.get("fiche_type", "")) == "skill"

    @property
    def is_promotion(self) -> bool:
        return bool(self.frontmatter.get("cabinet_promotion_candidate", False))


def parse_fiche(path: str | Path) -> Fiche:
    """Parse une fiche sur disque en objet `Fiche`.

    Lève `FrontmatterError` si le frontmatter est hors grammaire.
    """
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    fm, body = parse_frontmatter(lines)
    return Fiche(
        id=path.stem,
        path=path,
        frontmatter=fm,
        sections=split_sections(body),
    )
