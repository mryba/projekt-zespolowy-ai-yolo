"""Poziom 2 (mały eksperyment): rozpoznanie grubej kategorii obiektu (np. metal, plastik).

Uruchamiane tylko dla obiektów wykrytych na poziomie 1. Wynik to gruba kategoria
(np. metal, plastik, butelka) albo „do rozpoznania". Nie jest to pełne rozpoznawanie
22 klas.
"""
from __future__ import annotations

UNRECOGNIZED = "do rozpoznania"


def classify_object(image_path: str, box: tuple[float, float, float, float]) -> str:
    """TODO: zwróć kategorię lub UNRECOGNIZED."""
    raise NotImplementedError("TODO: rozpoznanie obiektu (poziom 2)")
