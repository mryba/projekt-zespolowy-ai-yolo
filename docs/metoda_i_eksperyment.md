# Metoda i eksperyment (zarys pod sprawozdanie)

## Cel
Wykryć obcy obiekt na zdjęciu pasa startowego i wskazać jego położenie: zdjęcie i ramka w pikselach (poziom 1). Rozpoznawanie grubych kategorii to poziom 2, mały eksperyment (patrz niżej).

## Dane
Trzy źródła: zdjęcia z drona (karty obiektów: `clean`, `4k`, `stream`, widok z góry, wysokość podana na karcie), 33 zdjęcia obiektów na pasie z telefonów (ground truth) oraz 22 zdjęcia z miarką z aparatu z opisem i wymiarami. Obiektów jest 22. Brak adnotacji w materiałach roboczych. Podział po obiekcie/scenie lub nagraniu.

## Metoda
YOLO (Ultralytics), mały model wstępnie wytrenowany, douczony na jednej klasie „obiekt obcy". Punkt odniesienia: ten sam model bez douczania.

## Eksperyment
Wpływ progu pewności na TP, FP, FN, precision, recall, F1. Lokalizacja: IoU. Priorytet: recall.

## Eksperyment dodatkowy: rozpoznawanie na grubych kategoriach (poziom 2)
Zamiast 22 osobnych klas stosujemy kilka szerokich kategorii, aby każda miała kilka przykładów. Eksperyment jest mały i orientacyjny. Wejściem są wycinki wykrytych obiektów, wyjściem kategoria albo „do rozpoznania”.

Robocze przypisanie obiektów do kategorii (do potwierdzenia):

| Kategoria | Obiekty |
|---|---|
| metal | FOD-05, 08, 11, 12 |
| plastik | FOD-01, 10, 15, 16, 21 |
| butelka | FOD-19, 20 |
| guma | FOD-02, 06 |
| folia i tkanina | FOD-13, 14, 17, 22 |
| drewno, karton, kamień, beton | FOD-03, 04, 07, 09, 18 |

Podział po obiekcie, jak w poziomie 1. Ograniczenie: dla obiektów spoza tych kategorii model nie ma właściwej odpowiedzi, dlatego wynik musi dopuszczać „do rozpoznania”. Jest to punkt do uzgodnienia z prowadzącym.

## Wyniki
_Brak (szkielet)._

## Ograniczenia
Mało zdjęć, brak adnotacji (przygotowujemy je samodzielnie, co ogranicza liczbę i jakość etykiet), zróżnicowana wysokość lotu i brak metadanych w plikach z drona, dlatego położenie to zdjęcie i ramka w pikselach, bez przeliczenia na metry i bez pozycji na pasie. Otwarte: postępowanie z obiektami spoza danych treningowych.

## Wnioski
_Do uzupełnienia po eksperymencie._
