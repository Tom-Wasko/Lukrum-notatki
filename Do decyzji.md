# Do decyzji

## Podobieństwa mechanik (etap 1, 13.11.2026)
Pełna lista z propozycjami: `../_robocze/etap1/podobienstwa.md`. Nazwy i teksty czyści etap 1. Czekają:
- [ ] wzory karty wyników i ich stałe (zadowolenie pracowników i klientów, rozwój firmy)
- [ ] stałe modelu popytu i reklamy
- [x] (14.11: ceny pod rozgrywkę, przeliczyć od zera – zob. niżej) liczby w katalogach (udogodnienia, wyposażenie, szkolenia, pakiety stanowisk, kandydaci)
- [ ] harmonogram odblokowania zakładek i limit dań
- [ ] kapitał startowy 40 000 zł
- [ ] nazwy w kodzie (usluga, zasob, prowadzacy)

## Wnętrza (13.11, gałąź `wnetrza-dane`) – rozstrzygnięte 13.11, zob. [[Wygląd]]
- [x] parki: zdarzenia zostają, pokazuje je mapa; dopisać zdarzenia z lektur
- [x] WOS: sprawdza Claude, zatwierdza autor
- [x] propozycje: wybór z prawdziwym skutkiem
- [x] ton bywalców: humor + cytaty z lektur

### Zaczepki WOS do zatwierdzenia (sprawdził Claude 14.11, `dymki.yaml`, commit c816a6e)
Zatwierdzenie = zmiana `sprawdzone: false` na `true` przy danej zaczepce (albo „zatwierdzam N” w rozmowie). Gra pokazuje tylko zatwierdzone.
- [x] 1. Paragon (Józio): kasa musi wydać paragon bez proszenia; e-paragon za zgodą klienta. **ustawa o VAT, art. 111 ust. 3a pkt 1** (wcześniej był zły punkt)
- [x] 2. Alergeny (Zagłoba): 14 alergenów z listy UE także przy jedzeniu bez opakowania. **rozp. (UE) 1169/2011, art. 44 ust. 1 lit. a, zał. II**. Usunięte „w menu albo na tablicy”, bo forma zależy od przepisów krajowych
- [x] 3. Cena z VAT (Rzecki): cena dla klienta zawsze brutto. **ustawa z 9.05.2014 o informowaniu o cenach, art. 3 ust. 1 pkt 1** (numer punktu do potwierdzenia w ISAP)
- [x] 4. Reklamacja (gość): 14 dni na odpowiedź, milczenie = przyjęcie. **ustawa o prawach konsumenta, art. 7a** (wcześniej „Kodeks cywilny”)
- [x] 5. Praca 16-latka (Józio): tylko lekkie prace, badanie lekarskie, w wakacje 7 h dziennie i 35 h tygodniowo, bez nadgodzin i nocy. **KP art. 200¹, 200², 201, 203**
- [x] 6. Monitoring (Judym): informacja 2 tygodnie przed uruchomieniem, cel, oznaczenie terenu. **KP art. 22², RODO art. 13**
- [x] 7. Płatność kartą (gość): obowiązek płatności bezgotówkowej od 2022, kasa połączona z terminalem od 2025. **Prawo przedsiębiorców, art. 19a** (wcześniej „obowiązek od 2025”, poprawione). Zakres do potwierdzenia
- [x] 8. „Na zeszyt” (Papkin): przerobione na odroczoną płatność. Ryzyko po stronie sprzedawcy, sprzedaż i tak na kasie. **KC art. 535, ustawa o VAT art. 111**. Najsłabiej udokumentowana; można ją też usunąć

### Cytaty z lektur do sprawdzenia (`cytat: true`, porównać z Wolnymi Lekturami)
- [x] (sprawdzone z Wolnymi Lekturami 14.11) Dulska: „Na to mamy cztery ściany i sufit, aby brudy swoje prać w domu”
- [x] (sprawdzone 14.11) Zagłoba: „Mości panowie! gdybym zaczął wszystko szczegółowie opowiadać, tedy i dziesięciu nocy by nie starczyło”
- [x] (sprawdzone 14.11) Zagłoba: „Zdechnę ja i pchły moje!”
- [x] (sprawdzone 14.11: „daj mi”, w oryginale „Krrokodyla”) Papkin: „Jeśli nie chcesz mojej zguby, krokodyla daj mi, luby” (w źródłach też „kup mi”)
- Rzecki: tylko aluzja do Napoleonów (`cytat: false`). Judym: cytat niepewny w brzmieniu, nie wstawiony

## Tor A (`mechaniki-a`, raport `_robocze/mechaniki-a-raport/raport.md`)
Rozstrzygnięte 13.11 wieczorem, do wprowadzenia 14.11:
- [x] „Wielkie otwarcie” waży jak zwykły tydzień (1,0). Progi tabeli punktów zostają, ocena po grze testowej
- [x] debet: włączenie za darmo, płaci się za użycie; bez zgody alarm i blokada (jak teraz)
- [x] Scrooge w tygodniu ze świętem: zamknięte, dokumenty przechodzą na następny tydzień z dopłatą (zamiast ryzyka 50%)
- [x] urlop 10% na umowie o pracę
- [x] zlecenie: zadowolenie −0,04 i kontrola PIP (14.11)
- [ ] czy biura mają mieć dodatkowe różnice

Wprowadzone 14.11, PR #2 (https://github.com/Tom-Wasko/Lukrum/pull/2, scala autor). Przegląd PR robi agent Fable (`_robocze/przeglad-a-fable.md`). Otwarte po wprowadzeniu:
- [x] (6 zł, 14.11) czy dopłata 3 zł za dokument przeniesiony po święcie wystarcza, żeby Scrooge nie był zawsze najlepszym biurem
- [x] (zostaje, 14.11) boty kupują tylko tyle wyposażenia, ile ma ich strategia, więc nowe pozycje mało na nie działają: zostawić czy dać im zakupy
- [x] „Gazeta Pana Cogito” i „Radio Tichy” zostają kanałami drukarni i Fali Koziołka (14.11); banki i giełda w jednej kamienicy, firmy przy Zana w jednym biurowcu (spis: „Mapa – elementy”)

Poprawki po przeglądzie Fable wprowadzone 14.11 (commit 1d8b921, PR #2). Otwarte po nich:
- [x] zlecenie: ryzyko kontroli PIP, gdy zleceniobiorca pracuje jak etatowiec, i mniej zadowolenia (14.11)
- [x] zmiana biura rachunkowego: jednorazowa opłata (14.11)
- [x] Scrooge: dopłata 6 zł za dokument przeniesiony po święcie (14.11, mechaniki-b)
- [x] Asteroida 328: bez limitu dokumentów (14.11, mechaniki-b)
- [ ] Asteroida bez limitu: pakiety M i L nie mają już sensu (zawsze wygrywa S). Czym je różnić albo usunąć?
- [x] Józef K.: obejścia zamknięte (14.11, mechaniki-b)
- [x] pensja za okres wypowiedzenia: kolumna wynagrodzeń i ZUS pracodawcy (14.11, mechaniki-b)
- [x] pomyłka przy pustym magazynie kosztuje klienta (14.11, mechaniki-b)
- [ ] panel i instrukcja nie pokazują jeszcze kontroli PIP, opłaty za zmianę biura ani przejęcia debetu
- [x] zmiana banku z otwartym debetem: najpierw spłata albo przejęcie przez nowy bank za opłatą (14.11)
- [x] pomyłki: zostaje 5,2% / 2,8%, ocena po teście gotowego LUKRUM (14.11)

## Symulowany pozew REVAS (Fable 14.11, `_robocze/pozew-revas-fable.md`)
- [x] nazwy własne i logotypy prawdziwych firm zostają (np. IKEA, Pewex), decyzja autora 14.11
- [x] katalogi: ceny mają zmuszać do myślenia („czy na pewno ★★★ zamiast ★, skoro tyle droższe”), czyli priorytet ma rozgrywka, a nie odwzorowanie rynku; podatki i przepisy zostają prawdziwe (14.11). Do zrobienia: przeliczyć katalogi od zera tak, żeby każdy poziom był wyborem z kosztem
- [ ] stałe modelu wspólne z REVAS (main 45, PR #2 22) przeliczyć od zera, martwe usunąć
- [x] nazwy ekranów w duchu mapy, ale bez zgadywania: np. „Kurier rankingowy” (zamiast Karty wyników), „Notes błędów księgowej” (Lista błędów), „Nadaj decyzje na poczcie” (Wyślij decyzje) (14.11)
- [ ] harmonogram odblokowań zmienić
- [ ] folder `revas_26` i regulamin platformy: rozmowa z prawnikiem

## Podgląd 4 (Fable 14.11, `_robocze/wyglad/podglad4.html`)
- [x] gruby krój: **Alfa Slab One** (14.11)
- [x] (zostaje, 14.11) style dekoru i grupy: PRL → turyści, imprezowicze; nowoczesny → biurowi, podróżni; studencki → studenci, uczniowie, imprezowicze; rodzinny → rodziny, uczniowie
- [x] sklep meblowy: wózek i kasa z paragonem; sklep jest osobną „strefą” (miejscem na mapie z własnym wnętrzem), jak lokal czy bank (14.11)
- [x] wszystkie jakości w grze mają 1, 2 albo 3 gwiazdki, więc zestaw ★★★ wchodzi do danych (14.11)
- [x] działka po budowie: pawilon z własnym wnętrzem (14.11)
- [x] ceny dekoru 900–3 200 zł i próg 40% zostają jako założenie, z pomiarem zwrotu (ok. 8–12 tygodni) (14.11)
- [ ] czy klikalne miejsca są dość spokojne i czy pasują postacie

## Wnętrza i testy (decyzje 14.11)
- [x] propozycje klientów: przed wyborem wskazówka skutków bez liczb i bez szansy
- [x] plotki o parkach w tej samej rundzie co zdarzenie na mapie
- [x] gracz nie wyłącza dymków (filtr gracza był tylko do testów); zostaje ustawienie mistrza gry
- [x] bez gry próbnej przed nowym wyglądem (były testy na Levasie); następny test z kolegami w gotowym LUKRUM

## Inne
- [x] położenie sanepidu i agencji reklamowej na mapie: sanepid w Śródmieściu (ul. Karłowicza), agencja w biurowcach przy Zana (Rury); park handlowy na Węglinie to dwa sklepy obok siebie (14.11)
- [x] lekcje: mieszane – pierwsze 2–3 rundy na żywo na lekcji, dalej między lekcjami (np. 2 w tygodniu, zamyka MG) (14.11)

## Po nocy Fable (16.11) – szczegóły w `_robocze/fable/pozew-2.md` i `ZMIANY.md`
- [ ] „Nocna 13” w grze dla niepełnoletnich: (a) zostaje, ale opisana w instrukcji mistrza gry z wyłącznikiem w kreatorze; (b) domyślnie wyłączona; (c) usunięta. Domyślnie przyjęte: zostaje, usunięta zachęta do ukrywania jej przed mistrzem gry, dopisane zdanie o 18 latach.
- [ ] znaki prawdziwych marek (`LOGA` w `ikony_marek.js`: sieci sklepów, banki): (a) zostają (decyzja 8.11: prawdziwe marki zostają), (b) zwykłe ikony rodzaju sklepu, (c) fikcyjne nazwy. Domyślnie: bez zmian.
- [ ] opisy porównujące ceny prawdziwych sieci (Stokrotka „trochę drożej”, Auchan „drożej niż w hurtowni”, abonament przypisany Auchan): (a) zostają, (b) opisy neutralne (propozycje tekstów w pozew-2.md, M1). Domyślnie: bez zmian.
- [ ] zlecenie bez składek pracodawcy: (a) uproszczenie z dopiskiem w instrukcji (zrobione), (b) składki jak w prawie (`podatki_2026.yaml`). Domyślnie: (a).
- [ ] przejęcie debetu przez nowy bank: (a) zostaje jako uproszczenie z dopiskiem (zrobione), (b) spłata debetu przed zmianą banku. Domyślnie: (a).
- [ ] Józio (Gombrowicz, prawa do 2039) i bank „Solaris” (Lem): (a) zostają jako aluzje, (b) Józio tylko z imienia bez cytatów, (c) zamiana. Domyślnie: bez zmian.
- [ ] prawdziwe numery domów z OSM przy lichwiarzu, detektywie i lombardzie: (a) zostają, (b) sama ulica. Domyślnie: bez zmian (pole mapy kolegi).
- [ ] paleta „Pewex” (nazwa marki): (a) zostaje, (b) nazwa opisowa. Domyślnie: bez zmian.
- [ ] nazwy z nocy do akceptacji: sklep „Meblościanka”, tytuły ekranów (tabela `NAZWY` w `zakladki/index.js`), listy wujka (`zakladki/wujek.js`).
- [ ] tryb lekcyjny: zamykanie rund po terminie wymaga uruchamiania `manage.py zamykaj_rundy` na serwerze (harmonogram zadań). Kto to ustawia?
- [ ] dymki: instrukcja nie opisuje wyłączania dymków przez mistrza gry, bo w panelu MG nie ma takiego przełącznika (decyzja 14.11 mówi, że ma zostać ustawienie MG) – do dorobienia.
