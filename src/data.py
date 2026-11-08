"""Dane: indeks zdjęć, metadane i podział train/val/test.

Jednostką podziału jest obiekt/scena (FOD_xx), nie pojedyncze zdjęcie. To samo
zdjęcie ujęte dwa razy nie może trafić do różnych zbiorów (przeciek danych).
"""
from __future__ import annotations

import re
from pathlib import Path

# FOD_01_GT_20260824_114626.jpg  /  FOD_01_DSC02171.JPG
FILENAME_RE = re.compile(r"^(?P<object_id>FOD_\d+)_(?P<rest>.+)\.(jpg|jpeg)$", re.IGNORECASE)


def parse_filename(name: str) -> dict | None:
    """Wyciąga id obiektu (FOD_xx) z nazwy pliku. None, gdy nazwa nie pasuje."""
    m = FILENAME_RE.match(name)
    if not m:
        return None
    return {"object_id": m.group("object_id"), "file": name}


def build_index(images_dir: str | Path):
    """TODO: zwróć tabelę (pandas) zdjęć: plik, object_id, typ (GT / z miarką), rozmiar."""
    raise NotImplementedError("TODO: indeks zdjęć")


def split_by_object(index, ratios: dict, seed: int):
    """TODO: podział train/val/test po object_id (bez przecieku między zbiorami)."""
    raise NotImplementedError("TODO: podział po obiekcie")
