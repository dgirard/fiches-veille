#!/usr/bin/env python3
import os
import glob

# Lire les slugs depuis urls_to_fetch.txt
slugs_to_check = []
with open('scripts/urls_to_fetch.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if '|' in line:
            slug = line.split('|')[0]
            if slug:
                slugs_to_check.append(slug)

# Obtenir tous les fichiers de fiches existants
existing_files = []
for md_file in glob.glob('fiches/**/*.md', recursive=True):
    basename = os.path.basename(md_file)
    # Retirer l'extension .md
    basename = basename.replace('.md', '')
    existing_files.append(basename)

# Trouver les fiches manquantes
missing = []
for slug in slugs_to_check:
    if slug not in existing_files:
        missing.append(slug)

if missing:
    print(f"Il y a {len(missing)} fiche(s) manquante(s):")
    for m in missing:
        print(f"  - {m}")
else:
    print("Toutes les fiches existent déjà!")
