#!/usr/bin/env bash
# Запускает проверку структуры репозитория Team-incredibles-project.
# Аргументы передаются в scripts/check-structure.py, например --pending.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if command -v python3 >/dev/null 2>&1; then
  PYTHON=python3
elif command -v python >/dev/null 2>&1; then
  PYTHON=python
else
  echo "Нужен Python 3, чтобы запустить scripts/check-structure.py." >&2
  exit 1
fi

exec "$PYTHON" "$ROOT/scripts/check-structure.py" "$@"
