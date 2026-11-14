# Grafiki LUKRUM (podgląd 4)

Własne płaskie grafiki SVG do wnętrz kebaba, sklepu meblowego i paska. Stan: **projekt do zatwierdzenia**.

## Jak używać

- **Kolory.** W plikach nie ma wpisanych kolorów. Ikony używają `currentColor`. Reszta używa zmiennych CSS:
  pięciu wspólnych (`--papier`, `--tusz`, `--akcent`, `--akcent-2`, `--ramka`) i pomocniczych `--g-*`
  (skóra, drewno, metal, ściana…). Wszystkie są w `zmienne.css` dla obu palet (Bar mleczny, Pewex) i obu motywów.
- **Wstawianie.** Zmienne CSS działają tylko wtedy, gdy SVG jest w dokumencie: wklej plik inline albo jako
  `<symbol>` i rysuj przez `<use href="#…">`. Przez `<img src>` grafika nie zobaczy zmiennych strony
  (ikony z `currentColor` też wymagają inline).
- **Fonty.** Napisy w grafikach (np. „ZAPLECZE”) biorą krój z `--font-szyld` albo `--font-gruby`.
- **Animacje.** Klasy do animowania w CSS strony: `.para` (para z rożna), `.neon` (świecące części),
  `.sekundnik` (zegar dworcowy), `.hak` (żuraw). Wyłącz je przy `prefers-reduced-motion`.
- **Miny obsługi.** `obsluga-kasjerka.svg` i `obsluga-kucharz.svg` mają trzy grupy `.mina-dobra`, `.mina-zwykla`,
  `.mina-zmeczona` (domyślnie widać zwykłą). Są też osobne pliki z jedną miną (`…-dobra.svg` itd.).
  Bywalcy i goście mają grupy `.mina-dobra`, `.mina-zwykla`, `.mina-zla`.
- **Składanie sceny.** Scena lokalu ma 1220×612: ściana 1220×380 na górze, podłoga 1220×232 pod nią, na to
  przezroczysta nakładka typu lokalu (`tla/typ-*.svg`), potem okno, sprzęt, dekor i postacie.
  Współrzędne z podglądu są w `podglad4.html` (funkcja `scenaLokalu`).
- **Lektury.** Nazwy plików bywalców to id z `bywalcy.yaml`. W interfejsie nie podpisujemy, z jakiej lektury
  jest postać. Postacie są własnymi interpretacjami, nie wzorują się na ekranizacjach.
- **Marki.** Nazwy sklepów w podglądzie są tekstem. Żadna grafika nie odtwarza cudzego logo.

## Zmiana grafik

Pliki powstają ze skryptów w `_narzedzia/` (`postacie.py`, `wnetrza.py`). Po zmianie uruchom
`python _narzedzia/zbuduj.py <dane.json>`: zapisze pliki SVG, ten spis i `../podglad4.html`.

## Spis

### `ikony/` – Ikony paska i interfejsu (24×24, kreska `currentColor`)

| Plik | Rozmiar | Opis |
|---|---|---|
| `ikony/dekor.svg` | 24×24 | Ikona: Dekor |
| `ikony/dymek.svg` | 24×24 | Ikona: Dymek |
| `ikony/finanse.svg` | 24×24 | Ikona: Finanse |
| `ikony/gwiazdka.svg` | 24×24 | Ikona: gwiazdka (zestaw, ocena) |
| `ikony/kuchnia.svg` | 24×24 | Ikona: Kuchnia |
| `ikony/lokal.svg` | 24×24 | Ikona: Lokal |
| `ikony/ludzie.svg` | 24×24 | Ikona: Ludzie |
| `ikony/mapa.svg` | 24×24 | Ikona: Mapa |
| `ikony/menu.svg` | 24×24 | Ikona: Menu i ceny |
| `ikony/punkt.svg` | 24×24 | Ikona: Miejsce do kliknięcia |
| `ikony/rozwin.svg` | 24×24 | Ikona: Rozwiń pasek |
| `ikony/sklep.svg` | 24×24 | Ikona: Sklep meblowy |
| `ikony/ustawienia.svg` | 24×24 | Ikona: Ustawienia |
| `ikony/wozek.svg` | 24×24 | Ikona: Wózek |
| `ikony/wroc.svg` | 24×24 | Ikona: Wróć |
| `ikony/zamknij.svg` | 24×24 | Ikona: Zamknij |

### `postacie/` – Postacie (pole 120×260, stopy na y=256, środek x=60)

| Plik | Rozmiar | Opis |
|---|---|---|
| `postacie/budowlaniec.svg` | 120×260 | Budowlaniec na działce |
| `postacie/bywalec-dulska.svg` | 120×260 | Bywalczyni: pani w płaszczu z futrzanym kołnierzem, torebka jak tarcza |
| `postacie/bywalec-jozio.svg` | 120×260 | Bywalec: licealista w za dużej bluzie, z telefonem |
| `postacie/bywalec-judym.svg` | 120×260 | Bywalec: młody lekarz w kurtce na fartuchu, ze stetoskopem |
| `postacie/bywalec-papkin.svg` | 120×260 | Bywalec: chudy elegant w za dużej skórzanej kurtce, z gitarą na plecach |
| `postacie/bywalec-rzecki.svg` | 120×260 | Bywalec: starszy pan w wytartym garniturze, z zeszytem pod pachą |
| `postacie/bywalec-zagloba.svg` | 120×260 | Bywalec: tęgi wąsacz w kamizelce wędkarskiej, z opaską na oku |
| `postacie/gosc-podrozny.svg` | 120×260 | Gość: podróżny z walizką (Dworzec) |
| `postacie/gosc-sasiadka.svg` | 120×260 | Gość: sąsiadka z siatką (osiedla) |
| `postacie/gosc-student.svg` | 120×260 | Gość: student w czapce, ze słuchawkami i plecakiem |
| `postacie/gosc-turystka.svg` | 120×260 | Gość: turystka z aparatem (Stare Miasto) |
| `postacie/obsluga-kasjerka.svg` | 120×260 | Obsługa: kasjerka, miny przełączane przez data-mina (dobra, zwykla, zmeczona) |
| `postacie/obsluga-kasjerka-dobra.svg` | 120×260 | Obsługa: kasjerka, mina „dobra” (plik z jedną miną) |
| `postacie/obsluga-kasjerka-zmeczona.svg` | 120×260 | Obsługa: kasjerka, mina „zmeczona” (plik z jedną miną) |
| `postacie/obsluga-kasjerka-zwykla.svg` | 120×260 | Obsługa: kasjerka, mina „zwykla” (plik z jedną miną) |
| `postacie/obsluga-kucharz.svg` | 120×260 | Obsługa: kucharz, miny przełączane przez data-mina (dobra, zwykla, zmeczona) |
| `postacie/obsluga-kucharz-dobra.svg` | 120×260 | Obsługa: kucharz, mina „dobra” (plik z jedną miną) |
| `postacie/obsluga-kucharz-zmeczona.svg` | 120×260 | Obsługa: kucharz, mina „zmeczona” (plik z jedną miną) |
| `postacie/obsluga-kucharz-zwykla.svg` | 120×260 | Obsługa: kucharz, mina „zwykla” (plik z jedną miną) |
| `postacie/sprzedawca.svg` | 120×260 | Sprzedawca w sklepie meblowym |
| `postacie/wujek.svg` | 120×260 | Wujek: kraciasta koszula, kamizelka, kaszkiet, zwinięta gazeta |

### `wnetrze/` – Elementy wnętrza kebaba (sprzęt w poziomach 1–3 = zestawy ★–★★★)

| Plik | Rozmiar | Opis |
|---|---|---|
| `wnetrze/drabina.svg` | 70×190 | Drabina malarska |
| `wnetrze/drzwi-zaplecze.svg` | 110×240 | Drzwi na zaplecze z tabliczką |
| `wnetrze/karton.svg` | 80×64 | Karton (lokal w urządzaniu) |
| `wnetrze/kasa-1.svg` | 110×64 | Kasa fiskalna, poziom 1 (zestaw ★) |
| `wnetrze/kasa-2.svg` | 110×64 | Kasa fiskalna, poziom 2 (zestaw ★★) |
| `wnetrze/kasa-3.svg` | 110×64 | Kasa fiskalna, poziom 3 (zestaw ★★★) |
| `wnetrze/lada-1.svg` | 450×160 | Lada (pole 450×160, blat na y=40), poziom 1 (zestaw ★) |
| `wnetrze/lada-2.svg` | 450×160 | Lada (pole 450×160, blat na y=40), poziom 2 (zestaw ★★) |
| `wnetrze/lada-3.svg` | 450×160 | Lada (pole 450×160, blat na y=40), poziom 3 (zestaw ★★★) |
| `wnetrze/okno-dworzec.svg` | 260×200 | Okno przemysłowe z widokiem na peron |
| `wnetrze/okno-kamienica.svg` | 260×200 | Okno kamienicy (łuk) z widokiem na Stare Miasto |
| `wnetrze/okno-pawilon.svg` | 260×200 | Witryna pawilonu z widokiem na bloki |
| `wnetrze/portret-wujka.svg` | 64×80 | Portret wujka w ramce (stały element lokalu) |
| `wnetrze/rozen-1.svg` | 120×200 | Rożen z parą (klasa .para), poziom 1 (zestaw ★) |
| `wnetrze/rozen-2.svg` | 120×200 | Rożen z parą (klasa .para), poziom 2 (zestaw ★★) |
| `wnetrze/rozen-3.svg` | 120×200 | Rożen z parą (klasa .para), poziom 3 (zestaw ★★★) |
| `wnetrze/tablica-1.svg` | 260×140 | Tablica menu bez napisów (ceny dopisuje gra), poziom 1 (zestaw ★) |
| `wnetrze/tablica-2.svg` | 260×140 | Tablica menu bez napisów (ceny dopisuje gra), poziom 2 (zestaw ★★) |
| `wnetrze/tablica-3.svg` | 260×140 | Tablica menu bez napisów (ceny dopisuje gra), poziom 3 (zestaw ★★★) |
| `wnetrze/wiadro.svg` | 44×46 | Wiadro z farbą |
| `wnetrze/zarowka.svg` | 34×96 | Goła żarówka na kablu (lokal w urządzaniu) |

### `dekor/` – Dekor w stylach: podstawowy, prl, nowoczesny, studencki, rodzinny

| Plik | Rozmiar | Opis |
|---|---|---|
| `dekor/lampa-nowoczesny.svg` | 60×120 | Lampa wisząca, styl nowoczesny |
| `dekor/lampa-podstawowy.svg` | 60×120 | Lampa wisząca, styl podstawowy (bez dekoru) |
| `dekor/lampa-prl.svg` | 60×120 | Lampa wisząca, styl PRL |
| `dekor/lampa-rodzinny.svg` | 60×120 | Lampa wisząca, styl rodzinny |
| `dekor/lampa-studencki.svg` | 60×120 | Lampa wisząca, styl studencki |
| `dekor/meble-nowoczesny.svg` | 220×150 | Stolik z krzesłami, styl nowoczesny |
| `dekor/meble-podstawowy.svg` | 220×150 | Stolik z krzesłami, styl podstawowy (bez dekoru) |
| `dekor/meble-prl.svg` | 220×150 | Stolik z krzesłami, styl PRL |
| `dekor/meble-rodzinny.svg` | 220×150 | Stolik z krzesłami, styl rodzinny |
| `dekor/meble-studencki.svg` | 220×150 | Stolik z krzesłami, styl studencki |
| `dekor/plakat-nowoczesny.svg` | 64×96 | Dodatek: plakat, styl nowoczesny |
| `dekor/plakat-prl.svg` | 64×96 | Dodatek: plakat, styl PRL |
| `dekor/plakat-rodzinny.svg` | 64×96 | Dodatek: plakat, styl rodzinny |
| `dekor/plakat-studencki.svg` | 64×96 | Dodatek: plakat, styl studencki |
| `dekor/podloga-nowoczesny.svg` | 1220×232 | Podłoga, styl nowoczesny |
| `dekor/podloga-podstawowy.svg` | 1220×232 | Podłoga, styl podstawowy (bez dekoru) |
| `dekor/podloga-prl.svg` | 1220×232 | Podłoga, styl PRL |
| `dekor/podloga-rodzinny.svg` | 1220×232 | Podłoga, styl rodzinny |
| `dekor/podloga-studencki.svg` | 1220×232 | Podłoga, styl studencki |
| `dekor/roslina-nowoczesny.svg` | 64×112 | Dodatek: roślina, styl nowoczesny |
| `dekor/roslina-prl.svg` | 64×112 | Dodatek: roślina, styl PRL |
| `dekor/roslina-rodzinny.svg` | 64×112 | Dodatek: roślina, styl rodzinny |
| `dekor/roslina-studencki.svg` | 64×112 | Dodatek: roślina, styl studencki |
| `dekor/sciana-nowoczesny.svg` | 1220×380 | Ściana, styl nowoczesny |
| `dekor/sciana-podstawowy.svg` | 1220×380 | Ściana, styl podstawowy (bez dekoru) |
| `dekor/sciana-prl.svg` | 1220×380 | Ściana, styl PRL |
| `dekor/sciana-rodzinny.svg` | 1220×380 | Ściana, styl rodzinny |
| `dekor/sciana-studencki.svg` | 1220×380 | Ściana, styl studencki |
| `dekor/szyld-nowoczesny.svg` | 260×66 | Szyld bez napisu, styl nowoczesny (elementy z klasą .neon świecą) |
| `dekor/szyld-podstawowy.svg` | 260×66 | Szyld bez napisu, styl podstawowy (bez dekoru) (elementy z klasą .neon świecą) |
| `dekor/szyld-prl.svg` | 260×66 | Szyld bez napisu, styl PRL (elementy z klasą .neon świecą) |
| `dekor/szyld-rodzinny.svg` | 260×66 | Szyld bez napisu, styl rodzinny (elementy z klasą .neon świecą) |
| `dekor/szyld-studencki.svg` | 260×66 | Szyld bez napisu, styl studencki (elementy z klasą .neon świecą) |
| `dekor/zdjecie-nowoczesny.svg` | 100×76 | Dodatek: obraz z Lublinem, styl nowoczesny |
| `dekor/zdjecie-prl.svg` | 100×76 | Dodatek: obraz z Lublinem, styl PRL |
| `dekor/zdjecie-rodzinny.svg` | 100×76 | Dodatek: obraz z Lublinem, styl rodzinny |
| `dekor/zdjecie-studencki.svg` | 100×76 | Dodatek: obraz z Lublinem, styl studencki |

### `tla/` – Tła: typy lokali, widoki stref, lokal surowy, działka, hala sklepu

| Plik | Rozmiar | Opis |
|---|---|---|
| `tla/dzialka-teren.svg` | 1220×612 | Działka: niebo, bloki w tle, ziemia, ogrodzenie |
| `tla/sklep-hala.svg` | 1220×612 | Hala sklepu meblowego (kratownice, lampy, alejka) |
| `tla/stan-surowy-podloga.svg` | 1220×232 | Lokal niewyposażony: wylewka z folią malarską |
| `tla/stan-surowy-sciana.svg` | 1220×380 | Lokal niewyposażony: surowy tynk z łatami, kable |
| `tla/typ-dworzec.svg` | 1220×612 | Typ lokalu: przy dworcu (stalowa belka, zegar dworcowy, tablica „Perony”) |
| `tla/typ-kamienica.svg` | 1220×612 | Typ lokalu: kamienica na Starym Mieście (sklepienie, filar, odkryta cegła) |
| `tla/typ-pawilon.svg` | 1220×612 | Typ lokalu: pawilon osiedlowy (sufit kasetonowy, świetlówki, kaloryfer) |
| `tla/widok-dworzec.svg` | 240×190 | Widok strefy za oknem i w tle działki (dworzec) |
| `tla/widok-lsm.svg` | 240×190 | Widok strefy za oknem i w tle działki (lsm) |
| `tla/widok-stare-miasto.svg` | 240×190 | Widok strefy za oknem i w tle działki (stare-miasto) |

### `stany/` – Stany lokalu: etapy budowy i plac budowy

| Plik | Rozmiar | Opis |
|---|---|---|
| `stany/betoniarka.svg` | 110×110 | Betoniarka |
| `stany/budowa-etap1.svg` | 560×320 | Budowa lokalu, etap 1: fundamenty (podstawa na y=320) |
| `stany/budowa-etap2.svg` | 560×320 | Budowa lokalu, etap 2: ściany i rusztowanie (podstawa na y=320) |
| `stany/budowa-etap3.svg` | 560×320 | Budowa lokalu, etap 3: dach (podstawa na y=320) |
| `stany/budowa-etap4.svg` | 560×320 | Budowa lokalu, etap 4: wykończenie, przed otwarciem (podstawa na y=320) |
| `stany/projekt.svg` | 130×100 | Stół z projektem lokalu |
| `stany/tablica-budowy.svg` | 150×130 | Tablica informacyjna budowy |
| `stany/zuraw.svg` | 220×420 | Żuraw budowlany (grupa .hak lekko się kołysze) |

### `sklep/` – Sklep meblowy

| Plik | Rozmiar | Opis |
|---|---|---|
| `sklep/kasa.svg` | 170×170 | Kasa sklepowa z taśmą |
| `sklep/paczka.svg` | 60×44 | Paczka z zakupem (w wózku) |
| `sklep/puszka.svg` | 34×40 | Puszka farby (kolor etykiety: currentColor) |
| `sklep/regal.svg` | 230×300 | Regał sklepowy z tabliczką działu (napis i towar dokłada gra) |
| `sklep/wozek.svg` | 150×130 | Wózek sklepowy |
