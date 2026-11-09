#!/usr/bin/env bash
# Uruchamia notebook projektu (macOS, Linux):
# tworzy środowisko .venv, jeśli go brak, instaluje zależności i startuje Jupyter.
set -euo pipefail

cd "$(dirname "$0")/.."

if command -v python3 >/dev/null 2>&1; then
  PY=python3
elif command -v python >/dev/null 2>&1; then
  PY=python
else
  echo "Brak Pythona. Zainstaluj Python 3.9 lub nowszy." >&2
  exit 1
fi

if [ ! -d .venv ]; then
  echo "Tworzę środowisko wirtualne (.venv)..."
  "$PY" -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate

echo "Instaluję zależności (pierwsze uruchomienie może potrwać)..."
pip install -r requirements.txt

echo "Uruchamiam notebook..."
exec jupyter notebook notebooks/projekt_yolo.ipynb
