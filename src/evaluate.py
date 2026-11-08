"""Ewaluacja: decyzja na poziomie obrazu oraz lokalizacja obiektu.

Poziom obrazu: TP, FP, TN, FN, precision, recall, F1.
Lokalizacja: IoU ramki przewidzianej i prawdziwej.
Priorytet: wysoki recall (nie przeoczyć obiektu), nawet kosztem fałszywych alarmów.
"""
from __future__ import annotations


def iou(box_a: tuple[float, float, float, float], box_b: tuple[float, float, float, float]) -> float:
    """Intersection over Union dwóch ramek (x1, y1, x2, y2)."""
    ax1, ay1, ax2, ay2 = box_a
    bx1, by1, bx2, by2 = box_b
    iw = max(0.0, min(ax2, bx2) - max(ax1, bx1))
    ih = max(0.0, min(ay2, by2) - max(ay1, by1))
    inter = iw * ih
    union = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - inter
    return inter / union if union > 0 else 0.0


def image_level_metrics(predictions, ground_truth) -> dict:
    """TODO: TP/FP/TN/FN, precision, recall, F1 dla decyzji „jest obiekt / nie ma"."""
    raise NotImplementedError("TODO: metryki na poziomie obrazu")


def localization_metrics(predictions, ground_truth, iou_threshold: float) -> dict:
    """TODO: dopasowanie ramek po IoU i metryki lokalizacji."""
    raise NotImplementedError("TODO: metryki lokalizacji")
