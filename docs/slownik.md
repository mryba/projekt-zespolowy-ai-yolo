# Słownik pojęć

Formalne definicje pojęć używanych w projekcie, w porządku alfabetycznym. Każde hasło ma trzy części: **definicja**, **w projekcie** (jak pojęcie jest użyte u nas) i **źródło**. Pełne opisy bibliograficzne są na końcu. Hasła oznaczone „do uzupełnienia o źródło” mają definicję roboczą bez potwierdzonego cytowania.

Spis: [Adnotacja](#adnotacja) · [Augmentacja](#augmentacja) · [Detekcja obiektów](#detekcja-obiektów) · [F1](#f1) · [FOD (obiekt obcy)](#fod-obiekt-obcy) · [Ground truth](#ground-truth) · [IoU](#iou) · [Nadir](#nadir) · [Precision](#precision) · [Próg pewności](#próg-pewności) · [Przeciek danych](#przeciek-danych) · [Recall](#recall) · [TP, FP, TN, FN](#tp-fp-tn-fn) · [Transfer learning](#transfer-learning) · [YOLO](#yolo) · [Zbiory treningowy, walidacyjny i testowy](#zbiory-treningowy-walidacyjny-i-testowy)

## Adnotacja

**Definicja.** Informacja opisująca zawartość obrazu, przygotowana przez człowieka lub narzędzie: dla detekcji obiektów jest to zwykle klasa obiektu oraz ramka ograniczająca (prostokąt w układzie pikseli obrazu).

**W projekcie.** Adnotacja to prostokąt wokół obiektu obcego na zdjęciu. Format YOLO zapisuje ją jako wiersz `klasa x_środka y_środka szerokość wysokość`, ze współrzędnymi znormalizowanymi do przedziału 0–1 (opis w `data/README.md`). Wymagania przedmiotu dopuszczają, że adnotacje zostaną udostępnione, co wymaga potwierdzenia.

**Źródło.** Wymagania przedmiotu „Projekt zespołowy” (`Projekt_zespolowy.pdf`). Do uzupełnienia o źródło naukowe.

## Augmentacja

**Definicja.** Sztuczne powiększanie zbioru uczącego przez modyfikowanie istniejących obrazów (np. zmiana jasności, kontrastu, szumu, rozmycia, niewielkie przekształcenia geometryczne), z odpowiednią aktualizacją adnotacji po zmianach geometrycznych.

**W projekcie.** Augmentujemy wyłącznie zbiór treningowy. Wersje tej samej klatki i klatki sąsiednie nie mogą trafić do zbioru walidacyjnego ani testowego (patrz [przeciek danych](#przeciek-danych)).

**Źródło.** Wymagania przedmiotu (`Projekt_zespolowy.pdf`, temat 7 i zasada dotycząca zbioru testowego). Do uzupełnienia o źródło naukowe.

## Detekcja obiektów

**Definicja.** Zadanie widzenia komputerowego polegające na ustaleniu, jakie obiekty znajdują się na obrazie i gdzie: dla każdego wykrytego obiektu wynikiem jest ramka ograniczająca, klasa i wartość pewności.

**W projekcie.** Mamy jedną klasę, „obiekt obcy”. Detekcja jest pierwszym poziomem systemu. Drugi poziom, rozpoznanie klasy przedmiotu, jest poza zakresem.

**Źródło.** Redmon i in. (2016), gdzie detekcję ujęto jako pojedynczy problem regresji ramek i prawdopodobieństw klas.

## F1

**Definicja.** Średnia harmoniczna [precision](#precision) i [recall](#recall):

`F1 = 2 · precision · recall / (precision + recall)`

**W projekcie.** Raportujemy F1 obok precision i recall, ale priorytetem jest recall, bo przeoczony obiekt jest groźniejszy niż fałszywy alarm.

**Źródło.** Powers (2011), który zwraca uwagę, że precision, recall i F-measure są miarami obciążonymi i nie powinny być stosowane bez zrozumienia tych obciążeń.

## FOD (obiekt obcy)

**Definicja.** *Foreign Object Debris*: każdy obiekt, żywy lub nie, znajdujący się w nieodpowiednim miejscu na terenie lotniska, który może zranić personel lub uszkodzić statek powietrzny.

**W projekcie.** FOD to przedmiot leżący na pasie startowym, np. śruba, butelka, kamień, kawałek folii. Zbiór zawiera 22 obiekty (`FOD_01`–`FOD_22`). Klasa detekcji nazywa się „obiekt obcy”.

**Źródło.** FAA, program FOD oraz Advisory Circular 150/5210-24 (od 2024-02-08 zastąpiony przez 150/5210-24A). Sformułowanie sprawdzono na stronie programu FAA, tekstu wersji 24A nie otwarto.

## Ground truth

**Definicja.** Prawda odniesienia: dane uznane za wzorcowe, z którymi porównuje się wyniki metody (adnotacje, wskazanie obecności obiektu).

**W projekcie.** Zdjęcia z folderu „obiektów na pasie (ground truth)” pokazują obiekt w miejscu położenia. Adnotacje ramek, gdy będą dostępne, pełnią rolę prawdy odniesienia dla oceny lokalizacji.

**Źródło.** Do uzupełnienia o źródło. Użycie terminu zgodne z nazwą folderu z materiałami prowadzącego.

## IoU

**Definicja.** *Intersection over Union*: stosunek pola części wspólnej ramki przewidzianej i ramki prawdziwej do pola ich sumy:

`IoU = |A ∩ B| / |A ∪ B|`

Wartość 1 oznacza idealne nałożenie, 0 brak części wspólnej.

**W projekcie.** IoU służy do oceny lokalizacji: detekcję uznajemy za trafioną, gdy IoU względem adnotacji przekracza przyjęty próg (`detect.iou_threshold` w `config.yaml`). Wartości 0,50 i 0,75 są w praktyce częstymi progami.

**Źródło.** Everingham i in. (2010), kryterium nakładania ramek w benchmarku PASCAL VOC (szczegół sekcji do weryfikacji w pełnym tekście). Zastosowanie IoU do rozstrzygania TP/FP: dokumentacja Ultralytics.

## Nadir

**Definicja.** Kierunek pionowo w dół. Zdjęcie nadirowe to ujęcie wykonane z kamerą skierowaną prostopadle do powierzchni.

**W projekcie.** Zdjęcia z drona w kartach obiektów są wykonane w trybie nadir (widok z góry).

**Źródło.** Do uzupełnienia o źródło. Opis zgodny z oznaczeniem „NADIR” na kartach obiektów.

## Precision

**Definicja.** Odsetek zgłoszonych detekcji, które są poprawne:

`precision = TP / (TP + FP)`

**W projekcie.** Mówi, jak często alarm okazuje się prawdziwy. Niska precision oznacza wiele fałszywych alarmów.

**Źródło.** Powers (2011).

## Próg pewności

**Definicja.** Minimalna wartość pewności (*confidence*) detekcji, od której wykrycie jest uwzględniane w wyniku. Model przypisuje każdej ramce wartość z przedziału 0–1; ramki poniżej progu są odrzucane.

**W projekcie.** Próg pewności jest głównym parametrem eksperymentu: sprawdzamy, jak jego zmiana wpływa na liczbę poprawnych i błędnych wykryć (`experiment.conf_sweep` w `config.yaml`). Niski próg zwiększa recall i liczbę fałszywych alarmów, wysoki działa odwrotnie. Wartość dobieramy na zbiorze walidacyjnym.

**Źródło.** Dokumentacja Ultralytics (parametr `conf`, współpraca z metodą NMS); wymagania przedmiotu (temat 5, eksperyment).

## Przeciek danych

**Definicja.** *Data leakage*: wprowadzenie do procesu uczenia informacji o zmiennej docelowej, która nie powinna być legalnie dostępna modelowi. Zawyża oszacowanie jakości.

**W projekcie.** Typowy przykład: dwa zdjęcia tego samego obiektu lub sąsiednie klatki tego samego nagrania w treningu i teście. Dlatego dzielimy dane po obiekcie lub nagraniu, a nie po pojedynczym zdjęciu.

**Źródło.** Kaufman i in. (2012).

## Recall

**Definicja.** Odsetek prawdziwych obiektów, które zostały wykryte:

`recall = TP / (TP + FN)`

**W projekcie.** Najważniejsza miara bezpieczeństwa: pokazuje, ile obiektów obcych system przeoczył. Wysoki recall oznacza, że rzadko pomija obiekt.

**Źródło.** Powers (2011).

## TP, FP, TN, FN

**Definicja.** Cztery możliwe wyniki decyzji „czy jest obiekt?” względem prawdy odniesienia:

- **TP** (*true positive*): obiekt jest i został wykryty.
- **FP** (*false positive*): obiektu nie ma, a system zgłosił alarm.
- **TN** (*true negative*): obiektu nie ma i nie zgłoszono alarmu.
- **FN** (*false negative*): obiekt jest, ale system go nie wykrył.

**W projekcie.** Raportujemy je na poziomie obrazu („pas czysty” albo „wykryto obiekt”), a przy ocenie lokalizacji także względem ramek (z użyciem [IoU](#iou)).

**Źródło.** Powers (2011); wymagania przedmiotu (zasady oceny wyników).

## Transfer learning

**Definicja.** Uczenie transferowe: wykorzystanie wiedzy zdobytej w jednym zadaniu lub dziedzinie (źródłowej) do poprawy uczenia w innym zadaniu lub dziedzinie (docelowej).

**W projekcie.** Używamy modelu YOLO wstępnie wytrenowanego na dużym zbiorze i douczamy go na jednej klasie „obiekt obcy”. Przy niewielkim zbiorze zdjęć jest to rozsądniejsze niż uczenie sieci od zera.

**Źródło.** Pan i Yang (2010).

## YOLO

**Definicja.** *You Only Look Once*: rodzina modeli detekcji obiektów, w której pojedyncza sieć neuronowa przewiduje ramki i prawdopodobieństwa klas bezpośrednio z całego obrazu w jednym przebiegu. Pierwsza wersja działała w tempie 45 klatek na sekundę, a lżejszy wariant 155.

**W projekcie.** Korzystamy z implementacji Ultralytics i małego modelu wstępnie wytrenowanego (`detect.model` w `config.yaml`). Model douczamy na jednej klasie „obiekt obcy”.

**Źródło.** Redmon i in. (2016); dokumentacja Ultralytics.

## Zbiory treningowy, walidacyjny i testowy

**Definicja.** Trzy rozłączne części danych: treningowy służy do uczenia, walidacyjny do doboru parametrów i progów, testowy do końcowej oceny. Zbiór testowy pozostaje niezmieniony, a wyniki na nim nie służą do strojenia.

**W projekcie.** Stosujemy jeden ustalony zbiór testowy. Podział robimy na poziomie obiektu (`FOD_xx`) lub nagrania, żeby uniknąć [przecieku danych](#przeciek-danych). Progi dobieramy na zbiorze walidacyjnym.

**Źródło.** Wymagania przedmiotu (`Projekt_zespolowy.pdf`, wymagania wspólne i zasady oceny wyników).

---

## Bibliografia

- Everingham, M., Van Gool, L., Williams, C. K. I., Winn, J., Zisserman, A. (2010). *The Pascal Visual Object Classes (VOC) Challenge*. International Journal of Computer Vision, 88, 303–338. DOI: 10.1007/s11263-009-0275-4.
- FAA. *Foreign Object Debris Program*. <https://www.faa.gov/airports/airport_safety/fod>. Advisory Circular 150/5210-24 *Airport Foreign Object Debris (FOD) Management* (wycofany 2024-02-08, zastąpiony przez 150/5210-24A).
- Kaufman, S., Rosset, S., Perlich, C., Stitelman, O. (2012). *Leakage in Data Mining: Formulation, Detection, and Avoidance*. ACM Transactions on Knowledge Discovery from Data, 6(4), art. 15. DOI: 10.1145/2382577.2382579.
- Pan, S. J., Yang, Q. (2010). *A Survey on Transfer Learning*. IEEE Transactions on Knowledge and Data Engineering, 22(10), 1345–1359. DOI: 10.1109/TKDE.2009.191.
- Powers, D. M. W. (2011). *Evaluation: From Precision, Recall and F-Measure to ROC, Informedness, Markedness and Correlation*. Journal of Machine Learning Technologies, 2(1), 37–63. arXiv:2010.16061 (nazwa czasopisma bywa podawana różnie w różnych bazach).
- Redmon, J., Divvala, S., Girshick, R., Farhadi, A. (2016). *You Only Look Once: Unified, Real-Time Object Detection*. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), s. 779–788. DOI: 10.1109/CVPR.2016.91. <https://openaccess.thecvf.com/content_cvpr_2016/html/Redmon_You_Only_Look_CVPR_2016_paper.html>
- Ultralytics. *YOLO Performance Metrics*. <https://docs.ultralytics.com/guides/yolo-performance-metrics>
- Wymagania przedmiotu „Projekt zespołowy”: dokument `Projekt_zespolowy.pdf` (materiał prowadzącego).
