"""Eksperyment: wpływ progu pewności na liczbę poprawnych i błędnych wykryć.

Zapisuje wyniki w jednym, wspólnym formacie, żeby dało się porównać YOLO z innymi
metodami na tym samym podziale testowym.
"""
from __future__ import annotations


def sweep_confidence(model, test_images, thresholds: list[float], cfg: dict):
    """TODO: dla każdego progu policz TP/FP/FN i metryki; zwróć tabelę (pandas)."""
    raise NotImplementedError("TODO: przemiatanie progu pewności")


def plot_precision_recall(results_table, out_path: str) -> None:
    """TODO: krzywa precision/recall (i próg pewności) do sprawozdania."""
    raise NotImplementedError("TODO: wykres")
