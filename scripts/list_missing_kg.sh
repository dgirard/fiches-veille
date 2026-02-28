#!/bin/bash
# List fiches that have raw-data but no GrapheDeConnaissance section
for raw in raw-data/*.md; do
  base=$(basename "$raw")
  fiche=$(find fiches -name "$base" 2>/dev/null | head -1)
  if [ -n "$fiche" ]; then
    has_kg=$(grep -c "## GrapheDeConnaissance" "$fiche")
    if [ "$has_kg" -eq 0 ]; then
      month=$(echo "$fiche" | sed "s|fiches/\([0-9-]*\)/.*|\1|")
      echo "$month|$base"
    fi
  fi
done | sort -r
