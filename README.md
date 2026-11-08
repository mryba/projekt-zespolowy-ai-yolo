# Wykrywanie obiektów obcych na pasie startowym (YOLO)

Projekt realizowany w ramach przedmiotu „Projekt zespołowy” (V semestr informatyki, 2026/2027). Program analizuje zdjęcia nawierzchni pasa startowego i wskazuje na nich obiekty obce (FOD, *Foreign Object Debris*), czyli przedmioty, które nie powinny się tam znajdować. Do detekcji używamy modelu YOLO.

Autorzy: Marcin Ryba, Magdalena Hus.

## Cel

Pas startowy jest bezpieczny tylko wtedy, gdy nie leżą na nim obce przedmioty, takie jak śruby, puszki czy butelki. Docelowo wizja zakłada przelot drona wzdłuż pasa i automatyczną analizę zdjęć. Gdy system znajdzie obiekt, zgłasza alert z jego położeniem, aby można było go szybko usunąć.

Projekt rozwijamy w dwóch warstwach:

1. **Wykrycie obiektu obcego.** Odpowiada na pytanie, czy na zdjęciu jest obiekt obcy i w którym miejscu obrazu. To zakres bieżących prac.
2. **Rozpoznanie obiektu.** Określenie, co to za przedmiot. W tym projekcie w ograniczonej formie: eksperyment na grubych kategoriach (patrz Zakres). Pełne rozpoznawanie poszczególnych klas wymaga znacznie większego zbioru.

## Zakres

W zakresie projektu:

- Wykrywanie [obiektu obcego](docs/slownik.md#fod-obiekt-obcy) na zdjęciu pasa startowego modelem [YOLO](docs/slownik.md#yolo), z jedną klasą „obiekt obcy”.
- Eksperyment rozpoznawania na grubych kategoriach (poziom 2): kilka szerokich kategorii materiału lub typu przedmiotu zamiast pojedynczych klas, na wycinkach wykrytych obiektów. Eksperyment jest mały i dobrany do obecnego zbioru danych, a jego wyniki mają charakter orientacyjny.
- Podstawową jednostką analizy jest pojedynczy obraz: zdjęcie albo klatka wyodrębniona z nagrania.
- Wynik detekcji: ramka wokół obiektu, pewność, zapis do CSV oraz obrazy z naniesionymi ramkami.
- Położenie obiektu: identyfikator zdjęcia i ramka w pikselach.
- Podział danych na poziomie obiektu lub nagrania, jeden ustalony zbiór testowy, dobór progów na zbiorze walidacyjnym.
- Ewaluacja (poziom obrazu i lokalizacja) oraz eksperyment z [progiem pewności](docs/slownik.md#próg-pewności).
- Szkielet alertu: schemat informacji przekazywanej po wykryciu obiektu.
- Dokumentacja: opis metody, eksperymentu i dziennik prac.

## Poza zakresem

Rzeczy, które świadomie pomijamy w tym projekcie, a które zostają jako możliwy dalszy rozwój:

- Pełne rozpoznawanie poszczególnych klas obiektów (np. śruba, puszka, butelka, 22 osobne klasy). Przy 1–3 zdjęciach na obiekt i podziale po obiekcie zbiór jest na to za mały.
- Analiza strumienia wideo w czasie rzeczywistym oraz agregacja wyników w czasie.
- Przeliczanie położenia na metry. Wysokość lotu bywa różna (np. 15, 20 lub 25 m), a w plikach nie ma metadanych.
- Pozycja obiektu na pasie (początek i koniec pasa, odległość).
- Sterowanie dronem, w tym powrót w miejsce wykrycia i zdjęcia z innej płaszczyzny.
- Raport z lotu z listą obiektów rozpoznanych i oczekujących na rozpoznanie.
- Implementacja innych metod niż YOLO.

## Metoda

- **Model:** mały model YOLO (Ultralytics), wstępnie wytrenowany i douczany na jednej klasie „obiekt obcy”. Zbiór jest niewielki, dlatego korzystamy z [transfer learningu](docs/slownik.md#transfer-learning) zamiast uczyć sieć od zera.
- **Podział danych:** na zbiory treningowy, walidacyjny i testowy dzielimy po obiekcie (`FOD_xx`), a nie po pojedynczym zdjęciu. Dzięki temu ten sam obiekt nie trafia jednocześnie do treningu i testu. Klatki z tego samego nagrania również nie są dzielone między zbiory, także po [augmentacji](docs/slownik.md#augmentacja).
- **Eksperyment:** badamy wpływ progu pewności detekcji na liczbę poprawnych i błędnych wykryć. Punktem odniesienia jest ten sam model bez douczania.
- **Ewaluacja:** decyzja na poziomie obrazu ([TP, FP, TN, FN](docs/slownik.md#tp-fp-tn-fn), [precision](docs/slownik.md#precision), [recall](docs/slownik.md#recall), [F1](docs/slownik.md#f1)) oraz lokalizacja obiektu ([IoU](docs/slownik.md#iou)). Progi dobieramy na zbiorze walidacyjnym, a nie na teście. Szczególną wagę ma recall, bo przeoczony obiekt jest groźniejszy niż fałszywy alarm.

Czy YOLO będzie na końcu najlepszym wyborem, pokażą wyniki. Wymagania przedmiotu zakładają jeden ustalony zbiór testowy oraz uzgodnione zasady organizacji danych i zapisu wyników, aby rezultaty różnych metod można było porównać.

## Dane

Materiały pochodzą z trzech źródeł (katalog `materialy-pasa/`, poza repozytorium):

- **Zdjęcia z drona** (`Karty obiektów FOD/FOD_xx/raw_graphics/`): widok z góry, wysokość lotu podana na karcie, 3840×2160. Dla każdej sceny jest wersja bez obiektu (`clean`), z obiektem (`4k`) i klatka ze strumienia 720p (`stream`). Kadry pochodzą z różnych miejsc pasa. Karty z grafikami mają obiekty FOD_01–07, karta FOD_20 nie zawiera grafik.
- **Zdjęcia obiektów na pasie** (ground truth): 33 zdjęcia z telefonów, z bliska.
- **Zdjęcia obiektów z miarką**: 22 zdjęcia z aparatu wraz z opisem i wymiarami obiektów (`lista_fod.docx`).

Obiektów jest 22 (`FOD_01`–`FOD_22`). Zdjęcia nie zawierają adnotacji (ramek), a w plikach z drona nie ma metadanych o pozycji ani wysokości. Wymagania przedmiotu przewidują, że dane referencyjne i adnotacje mogą zostać udostępnione, co należy potwierdzić u prowadzącego. Format danych roboczych opisuje [data/README.md](data/README.md).

## Status

Szkielet projektu: struktura, konfiguracja i notebook z opisem sekcji. Funkcje w `src/` są na razie szkicami (`TODO`), trening i wyniki jeszcze nie powstały.

## Uruchomienie

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks/projekt_yolo.ipynb
```

Sprawdzenie bez przeglądarki:

```bash
jupyter nbconvert --to notebook --execute notebooks/projekt_yolo.ipynb --output-dir /tmp
```

## Struktura repozytorium

| Ścieżka | Zawartość |
|---|---|
| `config.yaml` | parametry: ścieżki, model, progi, podział danych |
| `requirements.txt` | zależności |
| `notebooks/projekt_yolo.ipynb` | notebook z całym przebiegiem (9 sekcji) |
| `src/` | kod: `data`, `detect`, `classify`, `report`, `evaluate`, `experiment`, `config` |
| `data/`, `results/` | dane i wyniki, poza gitem |
| `docs/` | dokumentacja projektu (poniżej) |

## Dokumentacja

- [docs/dziennik.md](docs/dziennik.md): przebieg prac krok po kroku, z uzasadnieniem decyzji.
- [docs/slownik.md](docs/slownik.md): słownik pojęć z formalnymi definicjami i bibliografią.
- [docs/metoda_i_eksperyment.md](docs/metoda_i_eksperyment.md): zarys metody i eksperymentu.
