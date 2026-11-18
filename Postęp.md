# LUKRUM – postęp prac

Jedyna lista zadań projektu. Pisze lider po każdej serii. Stan na 17.11.2026, `main` gry `da8d532` (ostatni pełny
przebieg: 740 testów przechodzi). Repo gry jest spłaszczone (kod w korzeniu, bez `gra/` w ścieżkach).
Cel i etapy: [[Plan]]. Decyzje: [[Decyzje]]. Sprawy otwarte: [[Do decyzji]]. Historia zamkniętych serii: [[Serie]].

## Teraz (kolejność ustalona przez autora 16.11, mapa drogowa lidera z 17.11)
1. [x] Sposób pracy zespołu: `AGENTS.md`, `warsztat/`, definicje agentów (do przeglądu autora)
2. [x] Porządki w całym folderze projektu (seria `porzadki`, zrobione 17.11): spłaszczenie repo gry, kody serii, odchudzenie
   notatek do 41 plików, recenzja ([[porzadki – recenzja]]), scalenie do `main`. Zostaje `METODA.md` (jawność AI,
   [[Do decyzji]] §5): research regulaminu ZwzT w toku, szkic pisze lider
3. [ ] Warsztat i panel zespołu na claude.ai
4. [ ] Gra etapami, bez terminu.
   - [ ] `balans-katalogi`: poprawki drobnych mechanik (decyzja 18.11): Asteroida 328, kasa/lada/tablica menu, szkolenia, lodówka, szafy
   - [ ] D1–D2 i higiena z przeglądu dziur: cena bota 1,05, okienko sanepidu, przycisk blokady klubu w panelu MG, sprzęt i dostawcy od tygodnia 1 Do gry trafia tylko to, co przejdzie testy. Kolejne serie:
   - [ ] `pulpit`: mapa na cały ekran, w rogach małe ikony (runda, portfel, „Wyślij decyzje”, lista wujka, ⚙, konto,
     „Jak grać”); teczka na środku okienka decyzji; „Co tu zrobisz” ukryte; wyniki rundy w budynku Redakcji
   - [ ] `kebab-park`: sprzęt kupowany tylko w Parku handlowym, kebab pokazuje stan i odsyła
   - [ ] `zeszyt`: zeszyt wujka (lista zadań, gdzie co kupić, animacja stron, wystaje z brzegu) i odręczny krój
   - [ ] przygotowanie gry testowej i sama gra (może w tygodniu 23.11)
   - [ ] `budynki`: pierzeja 5 banków, giełda osobno, Kamienica rachmistrzów, Dom reklamy, redakcja
   - [ ] `wnetrza`: osobne wnętrze dla każdego żetonu, PRL w holach; krytyka wnętrz i poprawki wybrane przez autora
   - [ ] lista wujka: kliknięcie pozycji przesuwa i przybliża mapę do budynku, a ten pulsuje
   - [ ] dalej: lekcje (etap 4), ZwzT, audyt i prawnik (etap 5), telefon, pilot w szkole do maja 2027

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
- [ ] dźwięk: lekkie dźwięki domyślnie włączone (dzwonek nad drzwiami, skwierczenie, gwar, stempel w urzędzie), łatwe
  wyciszenie, mistrz gry może wyciszyć całą klasę
- [ ] pora dnia zgodna z prawdziwą godziną także we wnętrzu (za oknem rano jasno, wieczorem ciemno; niezależna od trybu
  jasny/ciemny; na mapie już jest)
- [ ] wizyty wujka przy ladzie w ważnych momentach
- [ ] wnętrza dla każdego żetonu mapy według projektu Fable 17.11 (makiety w `archiwum/fable-17.11/fable-wnetrza/`; pytania: [[Do decyzji]] §8c)

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
  ([[Tryb lekcyjny]]; wygląd nowych pól kreatora niesprawdzony na zrzucie)
- [x] projekt pięciu scenariuszy: `dokumentacja/SCENARIUSZE_LEKCJI.md` w repozytorium gry
- [x] dane wnętrz (silnik): nic otwartego poza tym, że wskaźniki skutków (np. `wyposazenie`, `tlok`) czekają na
  podpięcie skutków w danych
- [ ] lekcja 45 minut ze zmierzonym czasem rundy
- [ ] przewodnik nauczyciela i zasady oceniania
- [ ] tabela „mechanika a podstawa programowa” (WOS, biznes i zarządzanie); przegląd nauczyciela, próba w klasie
- [ ] gotowe zestawy odsłoniętych funkcji pod lekcje
- [ ] gra testowa z 4–6 osobami ze stoperem, potem z klasą (termin: [[Do decyzji]] §5)
- [ ] serwer dla szkoły (dziś laptop autora i tunel), osoba od `zamykaj_rundy`, dane osobowe uczniów (RODO):
  [[Do decyzji]] §1 i §5
- [ ] zgłoszenie do konkursu z datą lekcji (31.03.2027, niepotwierdzone)

## Etap 5 – audyt i publikacja
- [ ] niezależny przegląd całości (kod, dane, teksty, zrzuty)
- [ ] decyzje po przeglądzie prawnym z 16.11 (lista: [[Do decyzji]], §1; przegląd w `archiwum/notatki-wycofane/Analizy/Noc Fable 15-16.11/`)
- [ ] sprawdzenie nazwy w UPRP i znaków towarowych (zwłaszcza gdy LUKRUM wyjdzie poza szkoły), publikacja za zgodą autora
- [ ] dług prawny (poprawki tekstów, informacja o klubie w instrukcji MG, stopki, PDF zgodny z `.md`): lista w [[Do decyzji]], §1
- [ ] sekcja „Prawo”: pozew i SWOT są tylko we wnioskach ([[Pozew i SWOT – wnioski]]; priorytety zostają tam, nie w [[Plan]]).
  Lista kontrolna kolejnego przeglądu: stałe wspólne z dawnym projektem ≥ 3 miejsca po przecinku → 0, brak nazw z dawnej
  gry w danych, panelu, instrukcji i PDF, `ikony_marek.js` bez prawdziwych logo, tabela nawiązań literackich, wykaz grafik
  i fontów

## Dług w dokumentacji i kodzie
- [ ] `OPIS_GRY.md` opisuje jeszcze układ z zakładkami i kapitał 40 000 zł: przepisać pod obecną grę
- [ ] `STACK.md`: liczba testów, motywy, nowe moduły frontu (`swiat/`, `mapa/`)
- [x] kody dawnych serii w danych i komentarzach kodu wyczyszczone (krok 4d, 17.11; słownik w `archiwum/kody-serii.md`)
- [ ] martwe odsyłacze do dokumentów, których w repo nie ma: sprawdzić w recenzji porządków (krok 9)
- [ ] `test_kasyno.py::test_mistrz_gry_nie_widzi_klubu` bywa niestabilny w pełnym przebiegu
