"""Schemat alertu/raportu: co przekazujemy dalej po wykryciu obiektu obcego.

Cel alertu: ktoś może wysłać ekipę w to miejsce i usunąć obiekt, żeby następny
samolot mógł bezpiecznie wystartować. Statusy: wykryty / rozpoznany / do rozpoznania.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Status(str, Enum):
    DETECTED = "wykryty"
    RECOGNIZED = "rozpoznany"
    UNRECOGNIZED = "do rozpoznania"


@dataclass
class Alert:
    image: str
    box: tuple[float, float, float, float]  # x1, y1, x2, y2 w pikselach obrazu
    confidence: float
    status: Status = Status.DETECTED
    label: str | None = None                # klasa po rozpoznaniu (poziom 2)
    runway_position_m: float | None = None  # poza zakresem: pozycja na pasie (wymaga logów lotu), na razie puste


@dataclass
class FlightReport:
    alerts: list[Alert] = field(default_factory=list)

    @property
    def runway_clear(self) -> bool:
        """Pierwszy próg sukcesu: na pasie nie ma potencjalnie obcych elementów."""
        return len(self.alerts) == 0
