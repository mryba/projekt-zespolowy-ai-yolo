# Dane (poza gitem)

Katalog `data/` jest ignorowany przez git. Struktura docelowa:

- `raw/` — zdjęcia do pracy (kopie lub dowiązania z `materialy-pasa/`)
- `labels/` — etykiety w formacie YOLO: jeden plik `.txt` na zdjęcie, wiersz `0 x_center y_center width height` (współrzędne znormalizowane 0–1, klasa `0` = obiekt obcy)
- `splits/` — listy `train.txt`, `val.txt`, `test.txt`

Materiały nie mają adnotacji (ramek) i żadne nie zostaną udostępnione, więc etykiety przygotowujemy samodzielnie przed treningiem. Do ustalenia: które zbiory adnotujemy w pierwszej kolejności (zdjęcia z drona, ground truth) i w jakim narzędziu.
Podział robimy **po obiekcie/scenie (FOD_xx)**, nie po pojedynczym zdjęciu.
