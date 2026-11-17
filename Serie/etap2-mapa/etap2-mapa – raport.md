# Etap 2 – nowa mapa Lublina (strona [mapa], 15.11.2026)

Gałąź `mapa-osm`. Nowa mapa jest domyślna w zakładce „Mapa miasta”; przycisk „Stara mapa” wraca do mapy z kratką.

## Co weszło
- **Adresy i współrzędne** (`dane/mapa/budynki.yaml`): `geo` dla 31 samodzielnych budynków i obu zespołów,
  `adres` dla 30 z nich. Źródło: OSM (Nominatim, Overpass).
- **Dane terenu** (`narzedzia/mapa/pobierz_osm.py` → `panel_gracza/static/mapa/lublin.json`, 340 kB): 27 dzielnic,
  woda, rzeki, zieleń, drogi w czterech klasach, ulice osiedlowe, kolej; położenia 38 lokali, 13 punktów
  orientacyjnych i „serc” trzech stref bez dzielnic. Współrzędne w metrach od placu Litewskiego.
- **Silnik** (`panel_gracza/static/mapa/`): `widok.js` (kółko, przeciąganie, dwa palce, dwuklik, klawisze, płynne
  dojście), `lublin.js` (rysunek, znaczniki, pasek skrótów, warstwy), `ikony.js`, `mapa.css`.
- **Poziomy szczegółów**: miasto (strefy, główne drogi, małe znaki) → dzielnica (drogi zbiorcze, ikony, nazwy
  głównych ulic) → ulica (ulice osiedlowe, podpisy wszystkich znaków).
- **Wejście do budynku**: `lukrum.otworzWnetrze(id)`; dla zespołu id zespołu.
- **Wygląd**: kolory i kroje tylko z `motywy/zmienne.css`; stan lokalu rozróżnia ramka i znak (★ ✓), nie sam kolor.

## Sprawy na granicy z [mechaniki] (propozycje do WSPOLPRACA.md – nie wpisane, czekają na zgodę autora)
1. **Zastępcze otwieranie okien.** Nikt jeszcze nie słucha `lukrum:wnetrze`, więc mapa sama otwiera dotychczasową
   zakładkę albo okno (zespół: lista firm). Wnętrze wyłącza to, ustawiając w swoim słuchaczu
   `e.detail.obsluzone = true`. Propozycja: dopisać to pole do umowy.
2. **Położenia lokali.** `Lokal` w `schematy.py` nie ma `geo`, więc 38 położeń leży w `lublin.json` (klucz `lokale`).
   Propozycja: pole `geo` w `lokale.yaml`, wtedy mapa czyta je z danych gry. Dwa lokale nad Zalewem
   (`zemborzyce_1`, `zemborzyce_3`) mają położenie wpisane z ręki – ul. Żeglarska wypada w OSM poza miastem.
3. **Strefy bez dzielnic** (pytanie autora z 14.11): nieaktualne – każda strefa jest teraz jedną dzielnicą
   (zob. „Poprawki kolegi z 15.11 wieczorem”).
4. **`miejsce` sklepów sieciowych** poprawione na prawdziwe położenia z OSM (Makro – Chemiczna, Eurocash –
   Łęczyńska, Selgros – Jana Pawła II, Auchan – Witosa, Biedronka – Nałęczowska, Lidl – Romantyczna, Stokrotka –
   Braci Wieniawskich, Rożen – Turystyczna, stolarnia – Krochmalna). `strefa` bez zmian. Do sprawdzenia przez autora:
   Auchan (w Zygmuntowskich nie ma żadnego), błonia pod Zamkiem (współrzędne z ręki), Lidl (dzielnica niesprawdzona).
5. **Zmienne wyglądu.** `zmienne.css` i `dostepnosc.css` mapa wczytuje w warstwie kaskady `lukrum`, żeby nie zmieniać
   kolorów dotychczasowego panelu; mapa nie używa `--ramka`, bo tę nazwę ma też `motywy/grafik.css`.
   W palecie wysokiej widoczności `dostepnosc.css` pogrubia ramki także w starym panelu.
6. **Opisy budynków** w `budynki.yaml` kończą się odsyłaczami dla twórców („(dane/mapa/banki.yaml)”). Mapa je wycina
   przy wyświetlaniu; lepiej usunąć je z danych.

## Pionki i punkty charakterystyczne (15.11 wieczorem)
- Znaczniki to ilustrowane pionki na podstawkach (`ikony.js: zeton`), 45 rysunków: osobne dla banku, kamienicy,
  biurowca, urzędu, sanepidu, poczty, hurtowni, dyskontu, piekarni, zakładów mięsnych, sklepów, parku, szklarni,
  żaglówki na Zalewie, lokalu i działki oraz dla każdego zabytku.
- 11 nowych punktów Lublina poza danymi gry (`lublin.json: dodatkowe`, lista w `pobierz_osm.py: DODATKOWE`):
  Trybunał Koronny, Archikatedra, Brama Grodzka, Nowy Ratusz, Teatr im. Osterwy, Centrum Kultury, Muzeum Wsi
  Lubelskiej, Dworzec Lublin Główny, most Lutosławskiego, kościół na Czwartku, cmentarz przy Lipowej.
  Opisy są moje i **wymagają sprawdzenia przez autora** (daty i fakty pisałem z pamięci). Majdanka nie ma,
  zgodnie z decyzją z 8.11. Nowy Ratusz i Dworzec Główny mają współrzędne wpisane z ręki.

## Styl PRL i napisy (15.11, po uwagach kolegi)
- Znaczniki to tekturowe żetony: kwadratowe dla budynków, okrągłe dla lokali, parków i wody. Piktogram jest
  w płaskim druku w kilku kolorach palety, z grubym konturem i lekko przesuniętym kolorem. Punkty orientacyjne
  nie mają tektury, są narysowane tuszem wprost na planszy.
- Nazwy są na emaliowanych tabliczkach. Miejsce każdej wybiera `lublin.js: uloz`: pod, nad albo z boku żetonu,
  tak żeby nie zasłaniała żetonu, innej tabliczki, przycisków mapy ani nie wychodziła za ramkę. Ważniejsze
  wybierają pierwsze (Twój lokal, strefy, zespoły, budynki, lokale, punkty orientacyjne, nazwy dzielnic).
  Tabliczka, która się nie mieści, znika do czasu przybliżenia; po najechaniu pokazuje się zawsze.
- Progi poziomów: 0,09 i 0,3 px na metr.

## Poprawki kolegi z 15.11 wieczorem – **odwracają dwie decyzje autora z 14.11, do przeglądu**
1. **Strefa = jedna prawdziwa dzielnica** (`strefy.yaml: dzielnice`): Stare Miasto, Śródmieście (Centrum), Wieniawa
   (Miasteczko Akademickie), Rury (Politechnika), Czuby Północne (LSM i Czuby), Za Cukrownią (Zygmuntowskie),
   Dziesiąta (Dworzec), Czechów Południowy (Czechów i Kalinowszczyzna), Felin, Zemborzyce. Mapa podpisuje pole
   prawdziwą nazwą dzielnicy, a pod nią drobniej nazwą strefy z gry; nazwy stref w danych i zakładkach bez zmian.
   Pozostałe 17 dzielnic jest wyszarzone. Wycinane kształty trzech stref zniknęły ze skryptu i z `lublin.json`.
2. **Siedem lokali ma nowe adresy i nazwy** (`lokale.yaml`), żeby stały w dzielnicy swojej strefy; opisy bez zmian:
   - `dworzec_1` Kiosk przy Placu Dworcowym, pl. Dworcowy 1 → Kiosk za torami przy dworcu, ul. Nowy Świat 20
   - `dworzec_2` Lokal przy Dworcu Metropolitalnym, ul. Gazowa 4 → Lokal przy Wyścigowej, ul. Wyścigowa 31
   - `dworzec_3` Hala na Młyńskiej, ul. Młyńska 15 → Hala na Nowym Świecie, ul. Nowy Świat 34
   - `czechow_2` Pawilon na Paderewskiego, ul. Paderewskiego 2 → Pawilon na Lipińskiego, ul. Lipińskiego 3
   - `czechow_4` Budka na Kalinowszczyźnie, ul. Kalinowszczyzna 70 → Budka na Elsnera, ul. Elsnera 5
   - `felin_2` Pawilon na Witosa: ul. Witosa 12 → al. Witosa 30
   - `felin_3` Działka przy Mełgiewskiej, ul. Mełgiewska 80 → Działka przy Vetterów, ul. Vetterów 1
   Trzy lokale zostały w sąsiedniej kolorowej dzielnicy: `akademickie_4` (Głęboka 11, Śródmieście), `lsm_czuby_1`
   i `lsm_czuby_3` (Wileńska 3 i Filaretów 18, Rury). Dworzec w Dziesiątej to kompromis: sam dworzec stoi w Za Cukrownią.
3. **Budynki zbiorcze** (`budynki.yaml`): w biurowcu przy Zana są biura rachunkowe i trzy firmy od reklamy;
   ubezpieczyciel (ul. Hipoteczna 4) i parkiet maklerski (Krakowskie Przedmieście 59) są osobnymi budynkami. W kamienicy bankowej zostało sześć banków.
4. **Kolory**: strefy mają cztery odcienie bez zieleni; zielone są tylko parki, lasy i łąki.
5. **Oddalanie**: żetony bledną między 0,1 a 0,062 px/m; na pełnym oddaleniu widać nazwy dzielnic i własny lokal.
6. **Ikona lokalu**: sześć wariantów na stronie `/static/mapa/podglad_lokali.html` (`ikony.js: WARIANTY_LOKALU`);
   mapa rysuje `IKONA_LOKALU`: na ten moment wariant 3, rożen z mięsem.

## Czego nie ma
- wnętrz (strona mechanik), botów i billboardów na mapie, ruchu ulicznego i pory dnia ze starej mapy;
- rozsuwania znaków, które na widoku całego miasta nachodzą na siebie w Śródmieściu;
- testów automatycznych modułów JS (w repo nie ma narzędzia do testów przeglądarkowych).
