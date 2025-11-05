#!/usr/bin/env python3
"""
Script pour extraire les URLs des fiches et créer une liste à traiter
"""
import os
import re
from pathlib import Path

def extract_urls_from_fiches():
    """Extrait les URLs et identifiants de toutes les fiches"""
    fiches_dir = Path("fiches")
    urls_data = []

    for fiche_file in fiches_dir.rglob("*.md"):
        with open(fiche_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extraire l'identifiant (première ligne avec #)
        id_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if not id_match:
            continue
        identifiant = id_match.group(1).strip()

        # Extraire l'URL
        url_match = re.search(r'^## URL\s*\n(.+)$', content, re.MULTILINE)
        if not url_match:
            continue
        url = url_match.group(1).strip()

        # Ignorer yahoo.com comme demandé
        if 'yahoo.com' in url:
            print(f"Skipping {identifiant}: yahoo.com excluded")
            continue

        urls_data.append({
            'identifiant': identifiant,
            'url': url,
            'fiche_path': str(fiche_file)
        })

    return urls_data

if __name__ == "__main__":
    urls = extract_urls_from_fiches()
    print(f"Trouvé {len(urls)} URLs à télécharger")

    # Sauvegarder la liste
    with open('urls_to_fetch.txt', 'w', encoding='utf-8') as f:
        for item in urls:
            f.write(f"{item['identifiant']}|{item['url']}\n")

    print("Liste sauvegardée dans urls_to_fetch.txt")
