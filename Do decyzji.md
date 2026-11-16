# Do decyzji

Tylko sprawy otwarte. Po decyzji wpis znika stąd i trafia do [[Decyzje]] albo notatki tematu. „Domyślnie” oznacza
stan, który jest dziś w grze. Pytania lidera z bieżącej pracy są w [[Dziennik lidera]].

## 1. Przed pokazaniem gry w szkole (z przeglądu prawnego 16.11)
Uzasadnienia i propozycje tekstów: [[przegląd prawny|przegląd prawny (Analizy)]].
- [ ] **„Nocna 13” a niepełnoletni:** (a) zostaje, opisana w instrukcji mistrza gry, z wyłącznikiem w kreatorze;
  (b) domyślnie wyłączona; (c) usunięta. Domyślnie: zostaje, bez zachęty do ukrywania jej przed mistrzem gry, ze
  zdaniem o 18 latach; wyłącznik to zmienna `LUKRUM_KASYNO=0`.
- [ ] **Znaki prawdziwych marek** (`LOGA` w `ikony_marek.js`): (a) zostają, (b) zwykłe ikony rodzaju sklepu,
  (c) fikcyjne nazwy. Domyślnie: (a), zgodnie z decyzją z 14.11.
- [ ] **Opisy porównujące ceny prawdziwych sieci** („trochę drożej”, „drożej niż w hurtowni”, abonament):
  (a) zostają, (b) opisy neutralne. Domyślnie: (a).
- [ ] **Zlecenie bez składek pracodawcy:** (a) uproszczenie z dopiskiem w instrukcji, (b) składki jak w prawie.
  Domyślnie: (a).
- [ ] **Przejęcie debetu przez nowy bank:** (a) uproszczenie z dopiskiem, (b) spłata debetu przed zmianą banku.
  Domyślnie: (a).
- [ ] **Józio i bank „Solaris”** (autorzy jeszcze chronieni): (a) zostają jako aluzje, (b) Józio tylko z imienia,
  (c) zamiana. Domyślnie: (a).
- [ ] **Prawdziwe numery domów** przy lichwiarzu, detektywie i lombardzie: (a) zostają, (b) sama ulica. Domyślnie: (a).
- [ ] **Paleta „Pewex”** (nazwa marki): (a) zostaje, (b) nazwa opisowa. Domyślnie: (a).
- [ ] Rozmowa z prawnikiem o materiałach porównawczych z etapu 1 i o regulaminie konkursu.

## 2. Zmiany z 15–16.11 do akceptacji
Zrobione bez pytania autora, są w `main`. Lista z uzasadnieniem: [[raport|raport nocy Fable (Analizy)]], rozdz. 2.
- [ ] nazwa sklepu „Meblościanka”
- [ ] tytuły ekranów (tabela `NAZWY` w `zakladki/index.js`) i treść listów wujka (`zakladki/wujek.js`)
- [ ] list od wujka tylko w tygodniach 1–4
- [ ] motyw „Grafik zmian” zdjęty z listy wyboru
- [ ] księga gości: piąty wymiar to „wnętrze”, a nie „czystość”
- [ ] wielkość efektu wystroju (+0,8% popytu i +0,07★ za dopasowaną grupę); w danych jest też rozbieżność zwrotu
  9,8 a 10,9 tygodnia do wyjaśnienia
- [ ] nowe ceny katalogów: strategia premium traci najwięcej, do oceny w grze testowej
- [ ] instrukcja gracza i mistrza gry do przeczytania
- [ ] klikalne miejsca we wnętrzu: czy są dość spokojne i czy pasują postacie (wejdzie w krytykę wnętrz)

## 3. Mapa (zmiany majstra z 15.11, które odwracają decyzje z 14.11)
Opis: [[etap2-mapa – raport]].
- [ ] **Strefa = jedna prawdziwa dzielnica** (wcześniej strefy z kilku dzielnic albo wycinane kształty): zostaje?
- [ ] **Siedem lokali ma nowe adresy i nazwy**, żeby stały w dzielnicy swojej strefy: zostaje?
- [ ] dopisać do umów na granicy pole `e.detail.obsluzone` (dziś działa bez wpisu)
- [ ] położenia lokali: pole `geo` w `lokale.yaml` zamiast w `lublin.json`
- [ ] do sprawdzenia przez autora: położenie Auchan, błoni pod Zamkiem i Lidla; opisy 11 punktów orientacyjnych
- [ ] ikona lokalu: sześć wariantów na `/static/mapa/podglad_lokali.html`, dziś wariant 3 (rożen z mięsem)
- [ ] ikony mapy a ikony paska wnętrz: jedna kreska?

## 4. Mechaniki i balans
- [ ] stałe modelu popytu i reklamy: przeliczyć od zera, martwe usunąć
- [ ] harmonogram odblokowań i limit dań: zmienić (kierunek z planu: odblokowania przez listy wujka, limit dań ze sprzętu)
- [ ] Asteroida 328 bez limitu dokumentów: pakiety M i L nie mają sensu (zawsze wygrywa S). Różnicować czy usunąć?
- [ ] czy biura rachunkowe mają mieć dodatkowe różnice
- [ ] progi tabeli punktów i częstość pomyłek: ocena po grze testowej

## 5. Lekcje i serwer
- [ ] kto uruchamia `manage.py zamykaj_rundy` na serwerze (bez tego tryb lekcyjny nie zamyka rund po terminie)
- [ ] ile tygodni gry na cykl lekcji (wstępnie ok. 4, „ale się tym nie sugeruj”; scenariusze zakładają ok. 12)
- [ ] gotowe zestawy funkcji pod lekcje

## 6. Wygląd
- [ ] układ na telefonie (wspólnie z majstrem)
- [ ] kiedy znika stary wybór układu panelu („bok”, „grafik”)
- [ ] kolejne nawiązania literackie (Zajdel, Winnetou, inne lektury)

## 7. Porządki
- [ ] gałąź `fable` w repozytorium notatek na GitHubie: scalona do `main`, do usunięcia
