# LUKRUM – postęp prac

Zadania i stan etapów. Pisze lider. Stan na 17.11.2026, `main` 08268aa (740 testów przechodzi).
Cel i etapy: [[Plan]]. Decyzje: [[Decyzje]]. Sprawy otwarte: [[Do decyzji]].
Historia zamkniętych serii: [[Serie]].

## Teraz (kolejność ustalona przez autora 16.11)
1. [x] Sposób pracy zespołu: `AGENTS.md`, `warsztat/`, definicje agentów (do przeglądu autora)
2. [ ] Porządki w całym folderze projektu (seria `porzadki`)
3. [ ] Gra etapami, bez terminu. Do gry trafia tylko to, co przejdzie testy:
   - [ ] krytyka wnętrz (świeży recenzent, zrzuty w obu trybach) i poprawki wybrane przez autora
   - [ ] pulpit: mapa na cały ekran, w rogach małe ikony (runda, kasa, „Wyślij decyzje”, lista wujka, ⚙, konto,
     „Jak grać”); wyniki rundy w budynku Redakcji
   - [ ] lista wujka: kliknięcie pozycji przesuwa i przybliża mapę do budynku, a ten pulsuje
   - [ ] biura rachunkowe w osobnej kamienicy z szyldami, agencje reklamowe w osobnym biurowcu z windą, biurowiec
     przy Zana dla reszty firm

## Etap 1 – gra pod nową nazwą (zrobione 13.11.2026)
- [x] nowe repozytorium, pakiet Django `lukrum`, nowa dokumentacja
- [x] źródła założeń opisane realiami (prawo, rynek, Lublin)
- [x] prawdziwe marki z zastrzeżeniem, klub „Pod Złotym Koziołkiem”, instrukcja i PDF

## Etap 1½ – wygląd (zrobione 14–16.11.2026, do przeglądu autora)
- [x] trzy palety × jasny/ciemny we wspólnych zmiennych (`motywy/zmienne.css`), fonty lokalnie
- [x] grafiki SVG wnętrz i postaci (`static/grafiki/`, generator `narzedzia/grafiki/`)
- [x] cały panel, lista gier, panel mistrza gry i logowanie w paletach; wybór w menu ⚙
- [ ] przegląd rzadkich ekranów w trybie ciemnym i w wysokiej widoczności (obejrzane tylko główne)
- [ ] telefon: sprawdzone kilka ekranów, brak pełnego przeglądu

## Etap 2 – mapa Lublina (zrobione 15–16.11.2026, poprawki w toku)
- [x] dane z OpenStreetMap: dzielnice, woda, zieleń, drogi, kolej (`narzedzia/mapa/pobierz_osm.py`)
- [x] silnik mapy z płynnym przybliżaniem, żetony budynków, zespoły budynków, pasek skrótów, pora dnia
- [x] kliknięcie budynku otwiera wnętrze; wszystkie 75 znaczników coś otwiera
- [x] krok „teraz” z listu od wujka zaznaczony na mapie i we wnętrzu
- [ ] położenia lokali w danych gry (`lokale.yaml: geo`) zamiast w `lublin.json`
- [ ] odsyłacze dla twórców usunąć z opisów w `budynki.yaml` (dziś mapa wycina je przy rysowaniu)
- [ ] opisy 11 punktów orientacyjnych sprawdzić w źródłach (pisane z pamięci)
- [ ] boty i billboardy na mapie; przycisk „Stara mapa” do zdjęcia po teście z klasą
- [ ] wybór ikony lokalu (sześć wariantów na `/static/mapa/podglad_lokali.html`), potem usunąć stronę podglądu

## Etap 3 – wszystkie miejsca z wnętrzami (w toku)
- [x] miejsca zamiast działów menu; wnętrze kebaba z klikalnymi punktami, bywalcami i dymkami
- [x] sklep meblowy „Meblościanka” (wystrój lokalu), księga gości, „Kurier rankingowy”, podium na koniec gry
- [x] przełącznik rodzajów dymków w panelu mistrza gry
- [ ] wnętrza poza kebabem są schematyczne (drzwi, okienka); pawilon na działce korzysta ze sceny budowy
- [ ] strona startowa pokazuje „Nowe w tej rundzie” starymi nazwami („Zakładki”, „HR”)
- [ ] kolejne nawiązania literackie, zdarzenia z lektur w parkach

## Mechaniki
Tor A (zrobione, PR #2 i #5, 14.11.2026):
- [x] wynik 0–1000 pkt z pięciu działów, ranking jako suma ważona tygodni, „Wielkie otwarcie”
- [x] kapitał 50 000 zł, debet z opłatą liczony na koniec tygodnia, banki ze specjalizacjami
- [x] biura rachunkowe w pakietach S/M/L, opłata za zmianę biura
- [x] kadry według Kodeksu pracy, kontrola PIP przy zleceniu „jak etat”
- [x] pomyłki w szczycie, nowe katalogi, ceny przeliczone od zera (★ / ★★ / ★★★ jako wybór z kosztem)
- [x] panel pokazuje PIP, opłatę za zmianę biura i przejęcie debetu

Tor B:
- [x] opinie gości w pięciu wymiarach (księga gości; bez nowej mechaniki, pokazuje to, co silnik już liczył)
- [x] list od wujka w tygodniach 1–4 i na koniec gry
- [x] wystrój lokalu dopasowany do gości okolicy (nowa mechanika, wyłącznik w `dane/mapa/dekor.yaml`)
- [ ] nastrój zespołu widoczny na twarzach, wydarzenia dla filii, popyt z mapy
- [ ] harmonogram odblokowań prowadzony listami wujka zamiast numerów rund
- [ ] przepisanie opisów w grze pod nowe mechaniki
- [ ] gra testowa z ludźmi: balans jest dotąd tylko z botów

## Etap 4 – lekcje
- [x] tryb lekcyjny (pierwsze rundy na żywo, potem terminy); wymaga uruchamiania `manage.py zamykaj_rundy` na serwerze
- [x] projekt pięciu scenariuszy: `dokumentacja/SCENARIUSZE_LEKCJI.md` w repozytorium gry
- [ ] odwołania do podstawy programowej, przegląd nauczyciela, próba w klasie
- [ ] gotowe zestawy odsłoniętych funkcji pod lekcje

## Etap 5 – audyt i publikacja
- [ ] niezależny przegląd całości (kod, dane, teksty, zrzuty)
- [ ] decyzje po przeglądzie prawnym z 16.11 ([[przegląd prawny|przegląd prawny (Analizy)]]; lista w notatkach, `Do decyzji.md`)
- [ ] sprawdzenie nazwy i znaków towarowych, publikacja za zgodą autora

## Dług w dokumentacji i kodzie
- [ ] `OPIS_GRY.md` opisuje jeszcze układ z zakładkami i kapitał 40 000 zł: przepisać pod obecną grę
- [ ] `STACK.md`: liczba testów, motywy, nowe moduły frontu (`swiat/`, `mapa/`)
- [ ] w danych i komentarzach kodu są odsyłacze do dokumentów, których w repo nie ma (ok. 25 miejsc), oraz kody dawnych
  serii: osobna seria porządków w kodzie
- [ ] `test_kasyno.py::test_mistrz_gry_nie_widzi_klubu` bywa niestabilny w pełnym przebiegu
