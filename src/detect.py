"""Poziom 1 (priorytet): wykrycie anomalii, czyli obcego obiektu na pasie.

Wynik dla zdjęcia: lista detekcji (ramka, pewność). Położenie = identyfikator zdjęcia i ramka
w pikselach. Przeliczenie na metry i pozycja na pasie są poza zakresem (różna wysokość lotu,
brak metadanych w plikach).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Detection:
    image: str
    x1: float
    y1: float
    x2: float
    y2: float
    confidence: float


def load_model(model_name: str):
    """TODO: załaduj YOLO (Ultralytics), wagi wstępnie wytrenowane."""
    raise NotImplementedError("TODO: ładowanie modelu")


def train(model, data_yaml: str, cfg: dict):
    """TODO: douczanie na jednej klasie „obiekt_obcy" (transfer learning)."""
    raise NotImplementedError("TODO: trening")


def detect_image(model, image_path: str, conf: float, imgsz: int) -> list[Detection]:
    """TODO: inferencja na jednym zdjęciu."""
    raise NotImplementedError("TODO: detekcja")


def save_detections(detections: list[Detection], csv_path: str, images_dir: str) -> None:
    """TODO: zapis do CSV oraz obrazów z narysowanymi ramkami."""
    raise NotImplementedError("TODO: zapis wyników")
