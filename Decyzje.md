# Decyzje

Obowiązujące decyzje autora, tematami. Data w nawiasie to dzień decyzji. Gdy nowa decyzja zmienia starą, stara stąd
znika (zostaje w historii gita i w [[Historia]]). Sprawy otwarte: [[Do decyzji]]. Wygląd ma własną notatkę: [[Wygląd]].
Dzień po dniu decyzje zapisuje [[Dziennik lidera]], a lider po każdej serii przenosi tu to, co obowiązuje.

## Projekt
- Nazwa **LUKRUM**. W tekstach się nie odmienia („w LUKRUM”), rodzaj nijaki. (13.11)
- Gra jest własna: **nic z innych gier biznesowych**, ani nazw, ani mechanik, ani wzmianek. Liczby i wzory mają
  własne uzasadnienie w polu `zrodlo` (prawo, rynek Lublina, pomiar botami, decyzja autora). (13.11)
- Na start tylko kebab, ale branża (menu, składniki, sprzęt, klienci) siedzi w danych. (13.11)
- Nazwy ogólne w kodzie (`usluga`, `zasob`, `prowadzacy`) zostają. (13.11)
- Repozytoria prywatne. Commity tylko jako Tom-Wasko, bez dopisków o asystentach AI. README zawsze aktualny. (13.11)
- **Bez terminu.** Do gry trafia tylko to, co przejdzie testy. (16.11)
- Scalenia do `main` po akceptacji autora. Majstrowi zostaje wpis w dzienniku [[WSPOLPRACA]]. Pull request tylko przy
  zmianach w jego plikach. (16.11)
- Agenci autora mogą zmieniać kod mapy bez ograniczeń. (16.11)
- Sesje startują z folderu `lukrum`, bo wtedy działają `CLAUDE.md` i własne definicje agentów. (16.11)

## Marki i prawo
- **Prawdziwe nazwy firm i miejsc zostają**, z zastrzeżeniem w grze, instrukcji i README. (13.11)
- **Uproszczone znaki prawdziwych marek zostają** (np. IKEA, Pewex), jako własne rysunki. (14.11; zmienia „bez logo” z 13.11)
- Prawdziwej firmie nie przypisujemy złych cech. Oszust, lichwiarz i truciciel to zawsze postacie wymyślone. (13.11)
- Tekst zastrzeżenia:
  > LUKRUM to gra edukacyjna. Nazwy prawdziwych firm i miejsc służą tylko do oddania realiów Lublina. Oferty, ceny,
  > oprocentowania i zdarzenia w grze są fikcyjne. Gra nie jest związana z tymi firmami ani przez nie wspierana.
- **Podatki i przepisy są prawdziwe.** Ceny w katalogach mają służyć rozgrywce: każdy poziom ★ to wybór z kosztem
  („czy na pewno ★★★, skoro tyle droższe”). (14.11)
- Uproszczenia prawa są dozwolone, jeśli instrukcja mówi o nich wprost (dziś: zlecenie bez składek pracodawcy,
  przejęcie debetu przez nowy bank). Ostateczny wybór: [[Do decyzji]].

## Klub „Pod Złotym Koziołkiem”
- Zostaje ukryty. Ekran nazywa się „Nocna 13”. Hasło „koziol” otwiera go zawsze i każdemu, także mistrzowi gry. (13.11)
- W surowych danych jest zagadka „Rękopis znaleziony w JSON-ie”: hasło „saragossa” daje odznakę Szperacz. (13.11)
- Co z klubem w grze dla niepełnoletnich: [[Do decyzji]].

## Wynik i ranking
- Wynik tygodnia 0–1000 pkt w pięciu działach po 0–200 (finanse, goście, zespół, rozwój, bezpieczeństwo finansowe),
  według jawnych progów. Wyjątkowa gra może dać w dziale ponad 200. (13.11)
- Ranking to suma punktów z tygodni, późniejsze tygodnie ważą więcej. „Wielkie otwarcie” (tydzień 1) waży jak zwykły
  tydzień, 1,0. Progi tabeli punktów oceniamy po grze testowej. (13.11)
- Firma, która nic nie robi, dostaje 0–100 pkt. (14.11)
- Ranking i wyniki rundy pokazuje gazeta **„Kurier rankingowy”** w budynku Redakcji. (14.11, 16.11)

## Pieniądze
- Kapitał startowy **50 000 zł**. (13.11)
- **Debet** włącza się ręcznie i za darmo, płaci się za użycie. Liczy się saldo na koniec tygodnia. Bez zgody banku
  jest zawsze drożej, do tego alarm i blokada inwestycji. Stopy nie przekraczają odsetek maksymalnych. (13–14.11)
- Zmiana banku z otwartym debetem: najpierw spłata albo przejęcie przez nowy bank za opłatą. (14.11)
- Sześć banków ze specjalizacjami, każdy opłacalny dla innej strategii. Banki i biuro maklerskie są w jednej
  kamienicy. (13–14.11)

## Biura rachunkowe
- Cztery biura, pakiety S/M/L z limitem dokumentów i dopłatą. (13.11)
- Scrooge w tygodniu ze świętem jest zamknięty: dokumenty przechodzą na następny tydzień z dopłatą 6 zł. (14.11)
- Asteroida 328 nie ma limitu dokumentów. (14.11)
- Zmiana biura kosztuje jednorazowo tydzień pakietu nowego biura. (14.11)
- U Józefa K. nie da się obejść opóźnienia zmiany pakietu. (14.11)
- Biura rachunkowe mają stać **w osobnej kamienicy z szyldami**, jak banki. (16.11, do zrobienia)

## Ludzie
- Kadry według Kodeksu pracy: okres wypowiedzenia zamiast odprawy, umowa o pracę albo zlecenie. (13.11)
- Urlop to 10% czasu na umowie o pracę. (13.11)
- Zlecenie: zadowolenie −0,04 i ryzyko kontroli PIP, gdy zleceniobiorca pracuje jak etatowiec. (14.11)
- Pensja za okres wypowiedzenia idzie do wynagrodzeń, z ZUS pracodawcy. (14.11)
- **Pomyłki w szczycie** zamiast reklamacji: częstości 5,2% i 2,8% zostają, ocena po teście gotowej gry. Pomyłka
  przy pustym magazynie kosztuje klienta. (14.11)
- Boty kupują tylko tyle wyposażenia, ile ma ich strategia. (14.11)

## Katalogi i wystrój
- Wszystkie jakości w grze mają 1, 2 albo 3 gwiazdki. Zestaw sprzętu ★★★ jest w danych. (14.11)
- **Wystrój lokalu:** PRL → turyści, imprezowicze; nowoczesny → biurowi, podróżni; studencki → studenci, uczniowie,
  imprezowicze; rodzinny → rodziny, uczniowie. Ceny 900–3 200 zł i próg 40% to założenie z celem zwrotu w 8–12
  tygodni. Kupuje się raz i zostaje. (14.11)
- Sklep meblowy to osobne miejsce z własnym wnętrzem, wózkiem i kasą z paragonem. (14.11)
- Po budowie na działce stoi pawilon z własnym wnętrzem. (14.11)
- Stara reklama (tradycyjna i internetowa) jest usunięta. Zostaje model „agencja × kanał”. „Gazeta Pana Cogito”
  i „Radio Tichy” to kanały drukarni i Fali Koziołka, bez osobnych miejsc. (13–14.11)
- Agencje reklamowe mają stać **w osobnym biurowcu z windą**. Biurowiec przy Zana zostaje dla reszty firm. (16.11, do zrobienia)

## Goście i dymki
- Cztery rodzaje dymków: opinie o cenie i smaku, plotki z miasta, propozycje i kłopoty, zaczepki WOS. (13.11)
- **Gracz nie wyłącza dymków.** Rodzaje włącza i wyłącza mistrz gry. (14.11)
- Propozycja gościa ma 2–3 odpowiedzi z prawdziwym skutkiem. Przed wyborem widać wskazówkę bez liczb i bez szansy.
  Najwyżej jedna propozycja na kilka rund. (13–14.11)
- Plotka o parku pojawia się w tej samej rundzie co zdarzenie na mapie. (14.11)
- Bywalcy mówią po swojemu, z humorem i prawdziwymi cytatami z lektur w domenie publicznej. (13.11)
- Zaczepki WOS sprawdza w źródłach lider, zatwierdza autor. Gra pokazuje tylko zatwierdzone. Osiem zatwierdzonych
  jest opisanych w `Funkcje/Dymki przy ladzie`. (13–14.11)
- Zdarzenia losowe zostają w parkach i pokazuje je mapa. Dopisujemy zdarzenia z lektur. (13.11)

## Mapa i miejsca
- Mapa własna, rysowana na prawdziwych granicach dzielnic z OpenStreetMap, z płynnym przybliżaniem. (13.11)
- **10 stref gry**, pozostałe dzielnice to tło. Prawdziwe miejsca, ale bez tłoku na Starym Mieście i Krakowskim
  Przedmieściu. (14.11)
- Sanepid w Śródmieściu (ul. Karłowicza). Park handlowy na Węglinie to dwa sklepy obok siebie. (14.11)
- Kliknięcie budynku wchodzi do środka od razu, bez długiej animacji. (13.11)
- Szczegóły i spis elementów: [[Mapa]].

## Pulpit (16.11, do zrobienia)
- Mapa na cały ekran. W rogach małe ikony: runda, kasa, „Wyślij decyzje”, lista wujka, ⚙, konto, „Jak grać”.
- Wyniki rundy ogląda się w budynku Redakcji.
- Lista wujka: kliknięcie pozycji przesuwa i przybliża mapę do budynku, a ten pulsuje. Wejście robi gracz.
- Nazwy ekranów w duchu mapy, ale bez zgadywania: „Kurier rankingowy”, „Notes błędów księgowej”, „Nadaj decyzje na
  poczcie”. (14.11)

## Lekcje
- Tryb mieszany: pierwsze 2–3 rundy na żywo na lekcji, dalej między lekcjami, rundę zamyka mistrz gry albo termin. (14.11)
- Zakrywanie funkcji zostaje ręczne. Gotowe zestawy pod lekcje później. (13.11)
- Bez gry próbnej przed nowym wyglądem. Następny test z kolegami w gotowym LUKRUM. (14.11)

## Wnętrza: sposób przeglądu (16.11)
- Krytykę wnętrz robi świeży recenzent (zrzuty, oba tryby). Lider streszcza, autor wybiera poprawki.
