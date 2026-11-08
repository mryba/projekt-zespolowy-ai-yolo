"""Poziom 2 (później): rozpoznanie, co to za obiekt (śrubka, puszka, butelka).

Uruchamiane tylko dla obiektów wykrytych na poziomie 1. Wynik to gruba kategoria
(np. metal, plastik, butelka) albo „do rozpoznania". W projekcie jako mały eksperyment
na grubych kategoriach, nie jako pełne rozpoznawanie 22 klas.
"""
from __future__ import annotations

UNRECOGNIZED = "do rozpoznania"


def classify_object(image_path: str, box: tuple[float, float, float, float]) -> str:
    """TODO: zwróć nazwę klasy lub UNRECOGNIZED."""
    raise NotImplementedError("TODO: rozpoznanie obiektu (poziom 2)")
