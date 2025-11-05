#!/usr/bin/env python3
"""
Script pour télécharger les URLs et convertir en markdown
"""
import os
import subprocess
import time
from pathlib import Path

def download_and_convert(identifiant, url, output_dir):
    """Télécharge une URL et la convertit en markdown"""
    output_file = output_dir / f"{identifiant}.md"

    # Skip si déjà téléchargé
    if output_file.exists():
        print(f"✓ Skip {identifiant} (already exists)")
        return True

    try:
        # Utiliser curl + lynx pour convertir HTML en text
        # -dump: convertit HTML en text, -nolist: sans liste de liens
        cmd = [
            'curl', '-sL', '-A',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            url
        ]

        result = subprocess.run(cmd, capture_output=True, timeout=30)

        if result.returncode != 0:
            print(f"✗ Error downloading {identifiant}: curl failed")
            return False

        html_content = result.stdout

        # Convertir avec lynx
        lynx_cmd = ['lynx', '-dump', '-stdin', '-nolist', '-assume_charset=UTF-8']
        lynx_result = subprocess.run(
            lynx_cmd,
            input=html_content,
            capture_output=True,
            timeout=10
        )

        if lynx_result.returncode != 0:
            # Fallback: sauvegarder le HTML brut
            with open(output_file, 'wb') as f:
                f.write(f"# {identifiant}\n\n".encode('utf-8'))
                f.write(f"**URL:** {url}\n\n".encode('utf-8'))
                f.write(html_content)
            print(f"⚠ Saved raw HTML for {identifiant}")
            return True

        # Sauvegarder le contenu markdown
        # Essayer de décoder avec différents encodages
        content = None
        for encoding in ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']:
            try:
                content = lynx_result.stdout.decode(encoding)
                break
            except:
                continue

        if content is None:
            # Dernier recours: ignorer les erreurs
            content = lynx_result.stdout.decode('utf-8', errors='ignore')

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# {identifiant}\n\n")
            f.write(f"**URL:** {url}\n\n")
            f.write("---\n\n")
            f.write(content)

        print(f"✓ Downloaded {identifiant}")
        return True

    except subprocess.TimeoutExpired:
        print(f"✗ Timeout for {identifiant}")
        return False
    except Exception as e:
        print(f"✗ Error {identifiant}: {e}")
        return False

def main():
    # Créer le répertoire raw-data s'il n'existe pas
    raw_data_dir = Path("raw-data")
    raw_data_dir.mkdir(exist_ok=True)

    # Lire la liste des URLs
    with open('urls_to_fetch.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print(f"Processing {len(lines)} URLs...")

    success = 0
    failed = 0

    for i, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue

        parts = line.split('|', 1)
        if len(parts) != 2:
            continue

        identifiant, url = parts

        print(f"[{i}/{len(lines)}] ", end='')

        if download_and_convert(identifiant, url, raw_data_dir):
            success += 1
        else:
            failed += 1

        # Petite pause pour ne pas surcharger les serveurs
        time.sleep(0.5)

    print(f"\n{'='*60}")
    print(f"Done! Success: {success}, Failed: {failed}")

if __name__ == "__main__":
    main()
