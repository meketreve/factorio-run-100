#!/usr/bin/env bash
# Troca o perfil de mods do Factorio. Uso: perfil.sh vanilla | modded
set -euo pipefail
M="$HOME/.factorio/mods"
case "${1:-}" in
  vanilla) cp "$M/mod-list.vanilla.json"        "$M/mod-list.json"; echo "→ VANILLA (só base + DLC). Conquistas da Steam ativas." ;;
  modded)  cp "$M/mod-list.modded-backup.json"  "$M/mod-list.json"; echo "→ MODDED (88 mods). Conquistas da Steam desativadas." ;;
  *) echo "uso: $0 vanilla|modded"; exit 1 ;;
esac
grep -c '"enabled": true' "$M/mod-list.json" | xargs echo "mods habilitados:"
