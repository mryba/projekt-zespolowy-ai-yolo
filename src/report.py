"""Schemat alertu: co przekazujemy dalej po wykryciu obiektu obcego na zdjęciu.

Położenie to identyfikator zdjęcia i ramka w pikselach. Status mówi, na jakim etapie
jest obiekt: wykryty (poziom 1), rozpoznany do kategorii albo „do rozpoznania"
(poziom 2, mały eksperyment).
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    DETECTED = "wykryty"
    RECOGNIZED = "rozpoznany"
    UNRECOGNIZED = "do rozpoznania"


@dataclass
class Alert:
    image: str                                # identyfikator zdjęcia
    box: tuple[float, float, float, float]    # x1, y1, x2, y2 w pikselach obrazu
    confidence: float
    status: Status = Status.DETECTED
    label: str | None = None                  # kategoria po rozpoznaniu (poziom 2)
