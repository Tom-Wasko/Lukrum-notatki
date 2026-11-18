# Decyzje

Jedyne źródło obowiązujących decyzji szefa (autora), tematami. Data w nawiasie to dzień decyzji. Gdy nowa decyzja zmienia
starą, stara zostaje z adnotacją „(zmienione dd.mm)”, żeby nic nie zginęło. Sprawy otwarte: [[Do decyzji]]. Wygląd ma
własną notatkę: [[Wygląd]]. Dzień po dniu decyzje zapisuje [[Dziennik lidera]], a lider po każdej serii przenosi tu to,
co obowiązuje.

## Projekt
- Nazwa **LUKRUM**. W tekstach się nie odmienia („w LUKRUM”), rodzaj nijaki. (13.11)
- Gra jest własna: **nic z innych gier biznesowych**, ani nazw, ani mechanik, ani wzmianek. Liczby i wzory mają
  własne uzasadnienie w polu `zrodlo` (prawo, rynek Lublina, pomiar botami, decyzja autora). (13.11)
- Na start tylko kebab, ale branża (menu, składniki, sprzęt, klienci) siedzi w danych. (13.11)
- Nazwy ogólne w kodzie (`usluga`, `zasob`, `prowadzacy`) zostają. (13.11)
- Repozytoria prywatne. Commity tylko jako Tom-Wasko, bez dopisków o asystentach AI. README zawsze aktualny. (13.11)
- **Bez terminu.** Do gry trafia tylko to, co przejdzie testy. (16.11)
- **Terminy zewnętrzne** (słowa szefa 16.11): ZwzT założone, trzeba jeszcze wszystko powypełniać; wkrótce rozmowy
  z kuratorium i urzędem; nadzieja na spotkanie z „grubymi rybami” w przyszłym roku; do maja 2027 LUKRUM na testach
  w jakiejś szkole. „Gotowe 17.11 16:00” jest nieaktualne. (16.11)
- **Jawność AI:** plik `METODA.md` w repo gry („Jak powstał LUKRUM”), rozmowa szefa z kapitanem i sprawdzenie
  regulaminu ZwzT pod kątem AI. Commity bez zmian. (16.11)
- Agenci autora mogą zmieniać kod mapy bez ograniczeń. (16.11)

## Sposób pracy i repozytoria
- **Scalanie** (zmienione 17.11; wcześniej 16.11: „scalenia po akceptacji autora, pull request tylko przy zmianach
  w plikach majstra”): zmiany majstra z `origin/maciex` lider scala do `main` **od razu** po `git fetch`, bez pytania
  („scalaj wszystko od majstra od razu”), po sprawdzeniu składni JS i testów mapy. Własne serie scalamy po akceptacji
  szefa. Pull request tylko gdy zmiana dotyka plików drugiej strony. Majstrowi zostaje wpis w dzienniku [[WSPOLPRACA]].
- **Push bez pytania** („nie musisz mieć mojej zgody na push”, 17.11; zmienia „push po zgodzie” z 16.11), nadal bez
  `--force`. Pytać o nowe repo na GitHubie i o usuwanie zdalnych gałęzi. (17.11)
- Sesje startują z folderu `Pulpit\lukrum` (po przeprowadzce 17.11; wcześniej: z folderu projektu na dysku, 16.11),
  bo wtedy działają `CLAUDE.md` i własne definicje agentów.
- **Układ folderu `lukrum/`:** `gra/` = repo gry (spłaszczone, tylko gra), `notatki/` = repo notatek (plan, decyzje,
  `Funkcje/`, `Serie/`, `Analizy/`, `Zespół/`; sejf Obsidiana wspólny z majstrem), `warsztat/` = **osobne repo git bez
  związku z LUKRUM** (sposób pracy, szablony, definicje agentów, narzędzia), `archiwum/` bez gita, `_robocze/`
  tymczasowe. Raporty agentów i plany serii: `notatki/Serie/<seria>/`. Historia repo notatek zostaje. (16.11)
- Pozew, SWOT i porównania (dokumenty ze starą nazwą) idą do `archiwum/prawne/`, w notatkach tylko wnioski bez nazw
  ([[Pozew i SWOT – wnioski]]). `testy/dane_zamrozone/` bez zmian. (17.11)
- Stare kody serii i martwe odsyłacze w danych i kodzie: wyczyścić od razu przy porządkach (źródła na realia),
  słownik kodów do `archiwum/`. (16.11)
- **Majster:** mapa „bez ograniczeń”, ale lider regularnie robi `git fetch` i sprawdza `origin/maciex`. (16.11)
- Panel kontrolny zespołu: tylko strona na claude.ai. Sposób pracy i panel: oba teraz, wbrew zaleceniu oceny. (16.11)
- Pytania do szefa bez limitu liczby (narzędzie mieści 4 naraz, więc idą rundami); szef czyta wszystko. Pytań
  sprawdzających rozumienie gry nie zadajemy. Koszt pracy (model, przybliżone zużycie) mierzymy w „Stan prac”. (16.11)
- Role: **szef**, **lider**, **agenci**, **majster** (mapa), **kapitan** (nauczyciel, opiekun). (16.11)

## Marki i prawo
- **Prawdziwe nazwy firm i miejsc zostają**, z zastrzeżeniem w grze, instrukcji i README. (13.11)
- **Uproszczone znaki prawdziwych marek zostają** (np. IKEA, Pewex), jako własne rysunki. (14.11; zmienia „bez logo”
  z 13.11)
- Prawdziwej firmie nie przypisujemy złych cech. Oszust, lichwiarz i truciciel to zawsze postacie wymyślone. Firmy
  o złych cechach (lichwiarz, oszust) są zawsze zmyślone. (13–14.11)
- Tekst zastrzeżenia (stopka gry, strona startowa, „Jak grać”):
  > LUKRUM to gra edukacyjna. Nazwy prawdziwych firm i miejsc służą tylko do oddania realiów Lublina. Oferty, ceny,
  > oprocentowania i zdarzenia w grze są fikcyjne. Gra nie jest związana z tymi firmami ani przez nie wspierana.
- Wersja dla ucznia: „W grze występują prawdziwe firmy z Lublina, żeby świat był znajomy. Ich oferty, ceny i zdarzenia
  są wymyślone.” Promocja: „Prawdziwy Lublin: znane miejsca, znane firmy, wymyślone interesy.” Czego uczy: znak
  towarowy, prawo autorskie, marka, konkurencja; pytanie na lekcję: dlaczego gra może użyć nazwy banku, ale nie jego
  prawdziwego logo? Gdzie w grze: banki, dostawcy, dyskonty, sklepy. Zrobione 13.11 (commity 26e4a8c, 895d423).
- **Podatki i przepisy są prawdziwe.** Ceny w katalogach mają służyć rozgrywce: każdy poziom ★ to wybór z kosztem
  („czy na pewno ★★★, skoro tyle droższe”). (14.11)
- Uproszczenia prawa są dozwolone, jeśli instrukcja mówi o nich wprost (dziś: zlecenie bez składek pracodawcy,
  przejęcie debetu przez nowy bank). Ostateczny wybór i reszta spraw prawnych: [[Do decyzji]], §1.

## Klub „Pod Złotym Koziołkiem”
- Zostaje ukryty. Ekran nazywa się „Nocna 13”. Hasło „koziol” otwiera go zawsze i każdemu, także mistrzowi gry. (13.11)
- W surowych danych jest zagadka „Rękopis znaleziony w JSON-ie”: hasło „saragossa” daje odznakę Szperacz
  ([[Kasyno Pod Złotym Koziołkiem]]). (13.11)
- Klub jest na mapie. Co z klubem w grze dla niepełnoletnich: [[Do decyzji]].

## Wynik i ranking
- Wynik tygodnia 0–1000 pkt w pięciu działach po 0–200 (finanse, goście, zespół, rozwój, bezpieczeństwo finansowe),
  według jawnych progów. Wyjątkowa gra może dać w dziale ponad 200. (13.11)
- Ranking to suma punktów z tygodni, późniejsze tygodnie ważą więcej. „Wielkie otwarcie” (tydzień 1) waży jak zwykły
  tydzień, 1,0. Progi tabeli punktów oceniamy po grze testowej. (13.11)
- Firma, która nic nie robi, dostaje 0–100 pkt. (14.11)
- Ranking i wyniki rundy pokazuje gazeta **„Kurier rankingowy”** w budynku Redakcji. Wejście do Redakcji pokazuje
  scenę redakcji z gazetą na biurku na pierwszym planie. (14.11, 16.11)

## Pieniądze
- Kapitał startowy **50 000 zł**. (13.11)
- **Debet** włącza się ręcznie i za darmo, płaci się za użycie. Liczy się saldo na koniec tygodnia. Bez zgody banku
  jest zawsze drożej, do tego alarm i blokada inwestycji. Stopy nie przekraczają odsetek maksymalnych. (13–14.11)
- Zmiana banku z otwartym debetem: najpierw spłata albo przejęcie przez nowy bank za opłatą. (14.11)
- **Banki: pierzeja, czyli rząd kamienic, i pięć banków zamiast sześciu**, żeby mieściły się w jednym kadrze; każdy
  ze specjalizacją, opłacalny dla innej strategii. Kolory marek zostają, ale mogą być inne niż dziś, dobrane do palet.
  Zmienia „sześć banków w jednej kamienicy” z 13–14.11. (16.11 noc) Stan danych: w `banki.yaml` i `budynki.yaml` jest
  jeszcze sześć banków (w danych jeszcze 6, decyzja: 5); który znika: [[Do decyzji]], §8c.
- **Giełda (biuro maklerskie „Byk i Koziołek”) to osobny budynek**, nie część banków; jest już na mapie majstra
  (`gielda`). (16.11 noc)

## Biura rachunkowe
- Cztery biura, pakiety S/M/L z limitem dokumentów i dopłatą. (13.11)
- Scrooge w tygodniu ze świętem jest zamknięty: dokumenty przechodzą na następny tydzień z dopłatą 6 zł (wcześniej 3 zł).
  (14.11)
- Asteroida 328 nie ma limitu dokumentów. (14.11)
- Zmiana biura kosztuje jednorazowo tydzień pakietu nowego biura. (14.11)
- U Józefa K. nie da się obejść opóźnienia zmiany pakietu. (14.11)
- Biura rachunkowe mają stać w osobnej kamienicy z szyldami jak banki, o nazwie **„Kamienica rachmistrzów”**.
  (16.11, nazwa 16.11 noc; do zrobienia)
- Księga KPiR zostaje w biurowcu przy Zana. (16.11 noc; wątpliwość wobec krytyki wnętrz: [[Do decyzji]], §8c pyt. 4)

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
  tygodni (pomiar 17.11: 10,9 tygodnia). Kupuje się raz i zostaje. (14.11)
- Sklep meblowy to osobne miejsce z własnym wnętrzem, wózkiem i kasą z paragonem. (14.11)
- Po budowie na działce stoi pawilon z własnym wnętrzem. (14.11)
- Stara reklama (tradycyjna i internetowa) jest usunięta. Zostaje model „agencja × kanał”. „Gazeta Pana Cogito”
  i „Radio Tichy” to kanały drukarni i Fali Koziołka, bez osobnych miejsc. (13–14.11)
- Agencje reklamowe mają stać w osobnym biurowcu z windą, o nazwie **„Dom reklamy”** (parter z portiernią i „Twoimi
  kampaniami”, piętra: drukarnia, radio, eventy, internet). **Budynek „drukarnia” na mapie znika.** Biurowiec przy
  Zana zostaje dla reszty firm i księgi. (16.11, nazwa i układ 16.11 noc; do zrobienia)

## Goście i dymki
- Cztery rodzaje dymków: opinie o cenie i smaku, plotki z miasta, propozycje i kłopoty, zaczepki WOS. (13.11)
- **Gracz nie wyłącza dymków.** Rodzaje włącza i wyłącza mistrz gry. (14.11)
- Propozycja gościa ma 2–3 odpowiedzi z prawdziwym skutkiem. Przed wyborem widać wskazówkę bez liczb i bez szansy.
  Najwyżej jedna propozycja na kilka rund. (13–14.11)
- Plotka o parku pojawia się w tej samej rundzie co zdarzenie na mapie. (14.11)
- Bywalcy mówią po swojemu, z humorem i prawdziwymi cytatami z lektur w domenie publicznej. (13.11)
- Zaczepki WOS sprawdza w źródłach lider, zatwierdza autor. Gra pokazuje tylko zatwierdzone. Osiem zatwierdzonych
  jest opisanych w [[Dymki przy ladzie]]. (13–14.11)
- Zdarzenia losowe zostają w parkach i pokazuje je mapa. Dopisujemy zdarzenia z lektur. (13.11)

## Mapa i miejsca
- Mapa własna, rysowana na prawdziwych granicach dzielnic z OpenStreetMap, z płynnym przybliżaniem. (13.11)
- **10 stref gry**, pozostałe dzielnice to tło. Prawdziwe miejsca, ale bez tłoku na Starym Mieście i Krakowskim
  Przedmieściu. (14.11)
- **Majdanka na mapie nie ma.** (8.11)
- Sanepid w Śródmieściu (ul. Karłowicza). Park handlowy na Węglinie to dwa sklepy obok siebie. (14.11)
- Kliknięcie budynku wchodzi do środka od razu, bez długiej animacji. (13.11)
- **Miasteczko, detektyw, hurtownie i sklepy mają własne żetony** (`detektyw`, `gielda`, `akademia`, `makro`, `selgros`,
  `auchan`, `biedronka`, `lidl`…) i **każdy własne wnętrze**: nie ma wspólnych hal ani holi (Selgros osobno od Lidla).
  (16.11 noc)
- Szczegóły i spis elementów: [[Mapa]].

## Pulpit – nawigacja i układ ekranu (18.11.2026, szkic szefa `archiwum/szkice-szefa/pulpit-nawigacja-18.11.jpg`)
- **Mapa na cały ekran.** Lewy górny róg: ⚙ ustawienia nad pionowym paskiem ikon (na szkicu m.in. koszyk) z logiem „Ł”;
  pod paskiem napis „Tydzień N” to **tylko informacja o rundzie** (nic się nie rozwija).
- **Ikony paska:** ⚙ ustawienia, „Wyślij decyzje”, konto i „Jak grać”, koszyk (zakupy). Pomysł lidera na dalsze: do ustalenia.
- **Zeszyt wujka** wystaje z krawędzi ekranu, na kartce widać następny krok („kup mięso”). Najechanie wysuwa listę zadań,
  kliknięcie otwiera cały zeszyt. W środku **rzeczy podzielone na osobne strony i animacja przewracania stron**; w zeszycie
  jest też krótki samouczek (tutorial).
- **Portfel** to plik banknotów przy dolnej krawędzi; wygląda naturalnie. Najechanie pokazuje saldo i debet, kliknięcie
  otwiera okno finansów (konto, płynność, zobowiązania).
- **Wnętrza:** układ ekranu (boczek czy pływające panele) – według szkicu panele wystają z krawędzi jak na mapie; szczegóły
  przy serii `pulpit`.
- **KPiR:** księga zostaje w **biurowcu przy Zana** (potwierdzone 18.11, bez segregatora w kebabie).
- **Gałąź `fable`** w repo notatek usunięta z GitHuba (18.11). **Repo `warsztat` zostaje lokalne** („na razie nie”).

## Pulpit i wnętrza (16.11, do zrobienia)
Wygląd tych elementów: [[Wygląd]]. Kolejność prac: [[Postęp]].
- **Pulpit:** mapa na cały ekran. W rogach małe ikony: runda, kasa, „Wyślij decyzje”, lista wujka, ⚙, konto, „Jak
  grać”. Wyniki rundy ogląda się w budynku Redakcji. Na razie tylko komputer, telefon później. (16.11, 16.11 noc)
- **Portfel** zawsze z boku (mapa i wnętrza), w zastępstwie ikony „kasa”: skrót gotówki i stanu kebaba. Pełne wyniki
  rundy zostają w Redakcji. (16.11 noc)
- **Lista wujka:** kliknięcie pozycji przesuwa i przybliża mapę do budynku, a ten pulsuje. Wejście robi gracz. (16.11)
- **Zeszyt wujka** (wariant B): w środku lista zadań i rozpisane, gdzie co najlepiej kupić; animacja przewracania
  stron; zamknięty nie znika, tylko wystaje z brzegu ekranu, a na wystającej kartce widać następny krok. Odręczny krój
  pisma wujka: tak, licencja OFL, polskie znaki; agent proponuje 2–3, szef wybiera na zrzucie. (16.11 noc)
- **Okienko decyzji:** teczka na środku, dymki do cen i promocji później. (16.11 noc)
- **Sprzęt kupuje się tylko w Parku handlowym.** Kebab pokazuje stan sprzętu i odsyła; zeszyt ma ten krok w tygodniu 1
  (wykonalność: [[Do decyzji]], §8b). (16.11 noc)
- **Kebab: na miejscu** menu i ceny, promocje, zespół i grafik, wyniki, magazyn, czas i portfel właściciela;
  **odsyła:** sprzęt, stoliki i wystrój → Park, zatrudnianie → Miasteczko, szkolenia → Akademia, klienci → Pracownia
  Analiz. (16.11 noc)
- Lista „Co tu zrobisz” znika z widoku; zostaje ukryta dla czytników ekranu i jako zastępstwo na wąskim ekranie.
  (16.11 noc)
- Nazwy ekranów w duchu mapy, ale bez zgadywania: „Kurier rankingowy”, „Notes błędów księgowej”, „Nadaj decyzje na
  poczcie”. (14.11)
- Krytykę wnętrz robi świeży recenzent (zrzuty, oba tryby); lider streszcza, szef wybiera poprawki. (16.11) Odpowiedzi
  szefa na krytykę 16.11 noc są w pozycjach powyżej i w [[Krytyka wnętrz 16.11]].

## Lekcje
- Tryb mieszany: pierwsze 2–3 rundy na żywo na lekcji, dalej między lekcjami, rundę zamyka mistrz gry albo termin. (14.11)
- Zakrywanie funkcji zostaje ręczne. Gotowe zestawy pod lekcje później. (13.11)
- Gra testowa z ludźmi: nie od razu, może w tygodniu 23.11; funkcji nie zamrażamy. (16.11 noc; zmienia „bez gry
  próbnej przed nowym wyglądem” z 14.11)
