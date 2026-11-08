# Dziennik projektu

Cel: po zakończeniu projektu ten plik ma być **nauką i zrozumieniem** dla całego zespołu, jak to działa i dlaczego tak zrobiliśmy. Prowadzimy go na bieżąco przy każdym kroku, nowe wpisy na górze.

Format wpisu: **co zrobiliśmy** · **dlaczego tak** (alternatywy) · **jak to działa** · **gdzie w kodzie** · **co zrozumieć przed następnym krokiem**.

## Spis
- [Wpisy](#wpisy)
- [Po co jest każdy plik](#po-co-jest-każdy-plik)
- [Słownik pojęć](#słownik-pojęć)

## Wpisy

### 2026-11-09 · Krok 8: rozpoznawanie klas jako mały eksperyment na grubych kategoriach
- **Co:** rozpoznawanie klasy obiektu (poziom 2) wchodzi do zakresu w ograniczonej formie: eksperyment na kilku grubych kategoriach.
- **Dlaczego tak:** mamy 22 obiekty po 1–3 zdjęcia. Przy podziale po obiekcie osobne klasy dla każdego obiektu nie mają przykładów w treningu, więc pełne rozpoznawanie byłoby niewiarygodne. Kilka kategorii (metal, plastik, butelka, guma, folia i tkanina, drewno i kamień) daje po kilka obiektów na kategorię. Alternatywy: dopasowanie do wzorców (działa tylko dla znanych obiektów), pełne 22 klasy (za mało danych).
- **Jak to działa:** po wykryciu obiektu poziom 1 wycina fragment obrazu, a poziom 2 przypisuje mu kategorię albo „do rozpoznania”.
- **Gdzie:** `src/classify.py`, `config.yaml` (`classify.*`), `docs/metoda_i_eksperyment.md`.
- **Zrozum:** to eksperyment o charakterze orientacyjnym, a nie gotowy rozpoznawacz. Priorytetem pozostaje poziom 1.

### 2026-11-09 · Krok 7: decyzja o położeniu obiektu
- **Co:** położenie obiektu to **identyfikator zdjęcia i ramka w pikselach**. Nie przeliczamy na metry i nie wyznaczamy pozycji na pasie.
- **Dlaczego tak:** wysokość lotu bywa różna (np. 15, 20 lub 25 m), a w plikach z drona nie ma metadanych (GPS, wysokość). Przeliczenie pikseli na metry dałoby fałszywą dokładność. Alternatywy: położenie w metrach od środka kadru (wymaga znanej wysokości i parametrów kamery), pozycja na pasie (wymaga logów lotu lub rozpoznawania oznaczeń pasa). Obie odłożone.
- **Jak to działa:** alert niesie `image` (które zdjęcie) i `box` (gdzie na nim). Pole `runway_position_m` w `src/report.py` zostaje puste i jest zapowiedzią przyszłego rozszerzenia.
- **Gdzie:** `src/report.py`, `README.md` (Zakres i Poza zakresem).
- **Zrozum:** „gdzie” ma dwa poziomy: gdzie na zdjęciu (mamy) i gdzie na pasie (nie mamy, bo brakuje danych o locie).

### 2026-11-09 · Krok 6: korekta danych i lektura wymagań prowadzącego
- **Co:** poprawiliśmy opis danych po obejrzeniu wszystkich źródeł i przeczytaniu wymagań prowadzącego (`Projekt_zespolowy.pdf`).
- **Odkrycia:** zdjęcia z drona są w kartach obiektów (`Karty obiektów FOD/FOD_xx/raw_graphics/`: `clean`, `4k`, `stream`). Obiektów jest 22, a nie 8. Wcześniejszy zapis, że zdjęcia nie pochodzą z drona, był błędny.
- **Z wymagań:** adnotacje mogą zostać udostępnione (do potwierdzenia); klatki z nagrań są dopuszczalne, a analiza w czasie rzeczywistym nie jest wymagana; obowiązuje jeden ustalony zbiór testowy i uzgodnione zasady zapisu wyników, aby można było porównać rezultaty; progi dobieramy na zbiorze walidacyjnym.
- **Otwarte (z wymagań):** „należy uzgodnić sposób postępowania z obiektami nienależącymi do danych treningowych”.
- **Zrozum:** przed opisem danych trzeba przejrzeć wszystkie foldery, a nie tylko pierwszy z brzegu.

### 2026-11-08 · Krok 5: plan eksperymentu i ewaluacji
- **Co:** zaplanowaliśmy jeden eksperyment: wpływ progu pewności na liczbę poprawnych i błędnych wykryć, oraz porównanie YOLO bez douczania z YOLO douczonym.
- **Dlaczego tak:** to najprostszy eksperyment, który pokazuje kompromis między „nie przeoczyć" a „nie alarmować bez powodu". Dla bezpieczeństwa pasa ważniejszy jest recall.
- **Jak to działa:** model dla każdego obiektu podaje ramkę i pewność (0–1). Próg pewności mówi „zgłaszam tylko, jeśli pewność jest co najmniej taka". Niski próg: więcej trafień, ale i więcej fałszywych alarmów. Wysoki próg: odwrotnie. Przemiatamy kilka progów i patrzymy na TP, FP, FN. Detekcję uznajemy za trafioną, gdy IoU (nakładanie się ramki przewidzianej i prawdziwej) przekracza próg.
- **Gdzie:** `src/evaluate.py`, `src/experiment.py`, `config.yaml` (`experiment.conf_sweep`, `detect.iou_threshold`).
- **Zrozum przed następnym krokiem:** czym są TP, FP, TN, FN, precision, recall, F1 i IoU (słowniczek niżej). Wynik ma być w CSV w jednym formacie, żeby porównać z innymi metodami.

### 2026-11-08 · Krok 4: dlaczego dzielimy po obiekcie
- **Co:** zdecydowaliśmy, że podział na train/val/test robimy po obiekcie/scenie (FOD_xx), nie po zdjęciu.
- **Dlaczego tak:** ten sam obiekt jest sfotografowany kilka razy (np. dwa znaczniki czasu, zdjęcie z miarką). Gdyby jedno zdjęcie trafiło do treningu, a drugie do testu, model „widziałby odpowiedź" i wynik byłby zawyżony. To **przeciek danych**.
- **Jak to działa:** nazwa pliku zawiera id obiektu (`FOD_01_...`). Grupujemy po tym id i losujemy całe grupy do zbiorów.
- **Gdzie:** `src/data.py` (`parse_filename`, `split_by_object`), `config.yaml` (`data.split_unit`, `data.split_ratio`, `seed`).
- **Zrozum:** augmentacje (obrót, jasność) też robimy tylko na zbiorze treningowym, z tego samego powodu.

### 2026-11-08 · Krok 3: struktura repozytorium
- **Co:** zbudowaliśmy szkielet: notebook, moduły `src/`, `config.yaml`, README, dokumentację. Funkcje to `TODO`, notebook uruchamia się bez błędów.
- **Dlaczego tak:** prowadzący chce zobaczyć podstawę przed konkretami. Notebook jest narracją, logika siedzi w `src/`, parametry w `config.yaml`. Alternatywa (jeden duży notebook) jest prostsza, ale gorzej się rozwija i trudniej pokazać, że znamy cały kod.
- **Jak to działa:** notebook wczytuje konfigurację i wywołuje funkcje z `src/`. Zmiana eksperymentu to zmiana `config.yaml`, nie kodu.
- **Gdzie:** całe repo, opis plików niżej.
- **Zrozum:** dwa poziomy w kodzie: `detect.py` (poziom 1) i `classify.py` (poziom 2, później), a `report.py` opisuje alert.

### 2026-11-08 · Krok 2: dwa poziomy (anomalia, potem rozpoznanie)
- **Co:** przyjęliśmy wizję dwóch poziomów: poziom 1 to wykrycie obcego obiektu i alert, poziom 2 to rozpoznanie co to jest.
- **Dlaczego tak:** pierwszy próg sukcesu to wiedza, że na pasie jest coś obcego i gdzie. Dzięki temu ekipa może je usunąć przed kolejnym startem. Rozpoznanie klasy wymaga zbioru z klasami i jest następnym krokiem.
- **Jak to działa:** poziom 1 zwraca ramkę i pewność. Poziom 2 dla wykrytych obiektów podaje klasę albo „do rozpoznania". Alert ma status: wykryty / rozpoznany / do rozpoznania.
- **Gdzie:** `src/detect.py`, `src/classify.py`, `src/report.py`.
- **Zrozum / założenie:** zdjęcia pasa pochodzą z drona (widok z góry), a zdjęcia samych przedmiotów z telefonu lub aparatu. W plikach nie ma pozycji wzdłuż pasa ani wysokości lotu, więc położenie to identyfikator zdjęcia i ramka w pikselach (patrz Krok 7). **Poza zakresem:** dron wraca w miejsce wykrycia i fotografuje z innej płaszczyzny.

### 2026-11-08 · Krok 1: wybór tematu YOLO i strategia
- **Co:** Marcin Ryba wybiera temat „wykrywanie obiektów za pomocą YOLO". W projekcie uczestniczy też Magdalena Hus.
- **Dlaczego tak:** YOLO dobrze lokalizuje obiekty i jest szybki. Z siedmiu tematów od prowadzącego to jedyny typowo „detekcyjny". Ryzyko: potrzebuje etykiet (ramek) i słabo radzi sobie z obiektami, których nie widział, a zdjęć jest niewiele: kilkadziesiąt zdjęć z bliska oraz zestawy z drona dla kilku obiektów.
- **Jak to działa (YOLO):** „You Only Look Once". Sieć neuronowa patrzy na obraz raz i od razu zwraca ramki z pewnością. **Transfer learning:** bierzemy model już wytrenowany na dużym zbiorze i douczamy na naszej jednej klasie, bo mamy mało zdjęć.
- **Gdzie:** `config.yaml` (`detect.model`, `detect.class_names`).
- **Czy YOLO będzie optymalne:** nie wiemy. Metody anomaly detection (autoenkoder, PaDiM, PatchCore, FastFlow) uczą się z obrazów „normalnych" bez etykiet i mogą lepiej radzić sobie z nieznanymi obiektami, ale gorzej lokalizują. Rekomendację da dopiero porównanie na tym samym teście.

## Po co jest każdy plik

- `README.md` — jedna strona: cel, jak pracujemy z YOLO, instalacja, struktura.
- `requirements.txt` — lista bibliotek, żeby każdy zainstalował to samo. `ultralytics` (YOLO), `opencv-python` (obrazy i rysowanie ramek), `numpy` (tablice), `pandas` (tabele i CSV), `pyyaml` (wczytanie konfiguracji), `matplotlib` (wykresy), `scikit-learn` (metryki pomocnicze), `jupyter` i `nbconvert` (notebook i jego uruchamianie z terminala).
- `config.yaml` — wszystkie parametry: `seed` (powtarzalność), `paths` (ścieżki), `data.split_*` (podział), `detect.*` (model, rozdzielczość `imgsz`, próg pewności `conf_threshold`, próg `iou_threshold`), `classify.*` (poziom 2, wyłączony), `experiment.conf_sweep` (progi do przemiatania), `alert.min_confidence`.
- `.gitignore` — czego nie wrzucamy do gita: dane, wyniki, wagi modeli, materiały prowadzącego.
- `notebooks/projekt_yolo.ipynb` — narracja w 9 sekcjach.
- `src/config.py` — wczytanie `config.yaml`.
- `src/data.py` — indeks zdjęć, id obiektu z nazwy pliku, podział po obiekcie.
- `src/detect.py` — poziom 1: model, trening, detekcja, zapis wyników.
- `src/classify.py` — poziom 2: rozpoznanie klasy (później).
- `src/report.py` — alert i raport (wykryty / rozpoznany / do rozpoznania).
- `src/evaluate.py` — IoU i metryki.
- `src/experiment.py` — przemiatanie progu pewności i wykresy.
- `data/README.md` — format danych i etykiet.
- `docs/slownik.md` — słownik pojęć z definicjami i bibliografią. `docs/metoda_i_eksperyment.md` — zarys pod sprawozdanie.

## Słownik pojęć

Formalne definicje pojęć (YOLO, IoU, precision, recall, przeciek danych i inne) z bibliografią: [slownik.md](slownik.md).
