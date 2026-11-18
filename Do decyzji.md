# Do decyzji

Jedyne miejsce na sprawy otwarte i pytania do szefa. Po decyzji wpis znika stąd i trafia do [[Decyzje]] albo notatki
tematu. „Domyślnie” oznacza stan, który jest dziś w grze. Wpisy o tym samym temacie scalamy, nie dublujemy.
Dziennik lidera ([[Dziennik lidera]]) odsyła tutaj, nie ma własnej listy pytań.

## 1. Przed pokazaniem gry w szkole (prawo)
Uzasadnienia i propozycje tekstów: przegląd prawny nocy 16.11 (to ćwiczenie, nie porada prawna), w archiwum:
`archiwum/notatki-wycofane/Analizy/Noc Fable 15-16.11/przegląd prawny.md`. Część poprawek tekstów z przeglądu jest już
w grze (zlecenie i debet jako uproszczenia, urlop 20/26 dni, art. 36 KP, hipoteka i zastaw, rodzaj neutralny); poniżej
to, czego raport nocy ([[fable – raport]]) nie potwierdza.
- [ ] **„Nocna 13” a niepełnoletni:** (a) zostaje, opisana w instrukcji mistrza gry, z wyłącznikiem w kreatorze;
  (b) domyślnie wyłączona; (c) usunięta. Domyślnie: zostaje, bez zachęty do ukrywania jej przed mistrzem gry, ze
  zdaniem o 18 latach; wyłącznik to zmienna `LUKRUM_KASYNO=0`. Do zrobienia przy (a): informacja dla nauczyciela
  w rozdziale „Dla mistrza gry” w `INSTRUKCJA.md` (dziś brak wzmianki), klub poza zestawami „Krótka lekcja” i „Pierwsza
  gra”, wyłącznik w panelu MG (dziś tylko w ustawieniach serwera).
- [ ] **Znaki prawdziwych marek** (`LOGA` w `ikony_marek.js`): (a) zostają, (b) zwykłe ikony rodzaju sklepu,
  (c) fikcyjne nazwy. Domyślnie: (a), zgodnie z decyzją z 14.11 ([[Decyzje]], „Marki i prawo”).
- [ ] **Opisy porównujące ceny prawdziwych sieci** („trochę drożej”, „drożej niż w hurtowni”, abonament):
  (a) zostają, (b) opisy neutralne. Domyślnie: (a). Dotyczy też opinii o Stokrotce, Auchan i Eurocash oraz reklamy
  porównawczej i dóbr osobistych (art. 23–24 k.c.).
- [ ] **Zlecenie bez składek pracodawcy:** (a) uproszczenie z dopiskiem w instrukcji, (b) składki jak w prawie.
  Domyślnie: (a).
- [ ] **Przejęcie debetu przez nowy bank:** (a) uproszczenie z dopiskiem, (b) spłata debetu przed zmianą banku.
  Domyślnie: (a).
- [ ] **Józio i bank „Solaris”** (autorzy jeszcze chronieni): (a) zostają jako aluzje, (b) Józio tylko z imienia,
  (c) zamiana. Domyślnie: (a). Zob. też §8c: projekt wnętrz proponuje, by znikł właśnie Solaris (5 banków).
- [ ] **Prawdziwe numery domów** przy lichwiarzu, detektywie i lombardzie: (a) zostają, (b) sama ulica. Domyślnie: (a).
- [ ] **Paleta „Pewex”** (nazwa marki): (a) zostaje, (b) nazwa opisowa. Domyślnie: (a).
- [ ] **Giełda „prawdziwe notowania S&P 500”** (opis giełdy w `budynki.yaml`, giełda w budowie): skąd dane i na jakiej
  licencji; nazwa S&P 500 jest znakiem. Opcje: kursy spółek fikcyjnych albo dane z jawnej licencji; w instrukcji dopisek
  „symulacja, nie porada inwestycyjna”. Domyślnie: kursy fikcyjne.
- [ ] **Imiona i nazwiska, które mogą być prawdziwe:** „Jakub Klimek-Ślęzak” (`biura.yaml`, J.K.Ś.), „Zenon Lupa”
  (`budynki.yaml`), nazwa „e-Księgi24.pl”; niesprawdzone w sieci. Sprawdzić wyszukiwarką, przy trafieniu zmienić.
- [ ] **Instytucje publiczne w roli fikcyjnych firm:** „Pracownia Analiz UMCS” (zamiana na „Pracownia Analiz przy
  uniwersytecie”, bez adresu rektoratu). Domyślnie: opisy neutralne, nazwy zostają.
- [ ] **Adresy e-mail w historii gita** (34 commity autora z prywatnym Gmailem, 1 commit drugiej osoby): przed
  upublicznieniem repo albo przepisać historię z adresem `noreply` GitHuba, albo opublikować świadomie.
- [ ] **Dopiski edukacyjne w instrukcji** (uproszczenia gry względem prawa): progi PIP (30 h, 4 tygodnie, 5%) to
  uproszczenie, inspektor ocenia sposób pracy (art. 22 § 1 KP) i dotyczy to też B2B; staż skrócony do 6 tygodni;
  ZUS co tydzień (naprawdę co miesiąc); „odsetki za opóźnienie”, nie „karne”; lichwa jest przestępstwem (art. 304 k.k.);
  zapłacone odsetki od zwykłego kredytu są kosztem (zdanie o odsetkach Harpagona to uproszczenie); rejestracja firmy
  w CEIDG, a lokal żywieniowy zgłasza się do PIS; daty roku szkolnego w `INSTRUKCJA.md:8` (2025/26 na 2026/27).
- [ ] **RODO i serwer:** w dokumentacji dla szkoły dopisać, że przy tunelu Cloudflare i logowaniu Microsoft ruch
  przechodzi przez podmioty trzecie (szkoła jest administratorem danych uczniów); loginy uczniów bez nazwisk.
- [ ] **Ekran „Nawiązania i źródła”** w grze (autor, tytuł, wydanie): zalecany przy Józiu i Solaris, jeszcze nie ma.
- [ ] **Drobne do sprawdzenia:** stopka z zastrzeżeniem w `jak_grac.html`, w panelu MG i na stronach logowania; PDF
  instrukcji zgodny z `.md` (wygenerowany 16.11, sprawdzić po kolejnych zmianach); OSM: zdanie o ODbL dla `lublin.json`
  w README i `User-Agent` skryptu OSM (`LUKRUM-pobierz-mape/1.0`); wpis o autorstwie grafik (`narzedzia/grafiki/`)
  w `grafiki/README.md`; dymki o 16-latku w wakacje (`dymki.yaml`, art. 200¹–203 KP a przepisy o młodocianych,
  art. 190 KP).
- [ ] **Rozmowa z prawnikiem** (lista z przeglądu i z [[Pozew i SWOT – wnioski]]): materiały porównawcze z etapu 1,
  regulamin i oświadczenia konkursowe ZwzT, zasady użycia prawdziwych marek, sankcje PIP (zmiany od 2026), hazard
  w grze szkolnej, publikacja historii gita.

## 2. Zmiany z 15–16.11 do akceptacji
Zrobione bez pytania autora, są w `main`. Lista z uzasadnieniem: [[fable – raport]], rozdz. 2.
- [ ] nazwa sklepu „Meblościanka”
- [ ] tytuły ekranów (tabela `NAZWY` w `zakladki/index.js`) i treść listów wujka (`zakladki/wujek.js`)
- [ ] list od wujka tylko w tygodniach 1–4 (zeszyt wujka na kolejne tygodnie: §8b)
- [ ] motyw „Grafik zmian” zdjęty z listy wyboru
- [ ] księga gości: piąty wymiar to „wnętrze”, a nie „czystość”
- [ ] wielkość efektu wystroju (+0,8% popytu i +0,07★ za dopasowaną grupę) i zwrot kompletu: w raporcie nocy było
  9,8 tygodnia, nowy pomiar z 17.11 (3 ziarna × 5 botów średnich, 24 rundy, `dekor.yaml`) daje **10,9**, w celu 8–12.
  Do potwierdzenia, że obowiązuje 10,9
- [ ] nowe ceny katalogów: strategia premium traci najwięcej, do oceny w grze testowej
- [ ] instrukcja gracza i mistrza gry do przeczytania
- [ ] klikalne miejsca we wnętrzu: czy są dość spokojne i czy pasują postacie (wejdzie w krytykę wnętrz)

## 3. Mapa (zmiany majstra z 15.11, które odwracają decyzje z 14.11)
Opis: [[etap2-mapa – raport]].
- [ ] **Strefa = jedna prawdziwa dzielnica** (wcześniej strefy z kilku dzielnic albo wycinane kształty): zostaje?
- [ ] **Siedem lokali ma nowe adresy i nazwy**, żeby stały w dzielnicy swojej strefy: zostaje?
- [ ] dopisać do umów na granicy pole `e.detail.obsluzone` (dziś działa bez wpisu; [[WSPOLPRACA]])
- [ ] położenia lokali: pole `geo` w `lokale.yaml` zamiast w `lublin.json`; odsyłacze dla twórców usunąć z opisów
  `budynki.yaml` (mapa dziś je wycina)
- [ ] do sprawdzenia przez autora: położenie Auchan, błoni pod Zamkiem i Lidla; opisy 11 punktów orientacyjnych
  (pisane z pamięci)
- [ ] [mechaniki] → [mapa]: gdzie na mapie postawić **Kamienicę rachmistrzów** (biura rachunkowe) i **Dom reklamy**
  (agencje reklamowe)? Decyzja o samych budynkach: [[Decyzje]]
- [ ] ikona lokalu: sześć wariantów na `/static/mapa/podglad_lokali.html`, dziś wariant 3 (rożen z mięsem)
- [ ] ikony mapy a ikony paska wnętrz: jedna kreska?

## 4. Mechaniki i balans
- [ ] stałe modelu popytu i reklamy: przeliczyć od zera, martwe usunąć
- [ ] harmonogram odblokowań i limit dań: zmienić (kierunek z planu: odblokowania przez listy wujka, limit dań ze sprzętu)
- [ ] Asteroida 328 bez limitu dokumentów: pakiety M i L nie mają sensu (zawsze wygrywa S). Różnicować czy usunąć?
- [ ] czy biura rachunkowe mają mieć dodatkowe różnice
- [ ] progi tabeli punktów i częstość pomyłek: ocena po grze testowej
- [ ] **Kasa fiskalna, lada, tablica menu:** jakość ★ nie ma efektu na sprzedaż (tylko zadowolenie kasjera +0,02 za
  gwiazdkę), więc ★★★ nigdy się nie zwraca. Dodać efekt w silniku (np. tempo obsługi kasy) czy zostawić jako komfort?
- [ ] **Firmy szkoleniowe:** ocena firmy (`zadowoleni_klienci`) nie ma efektu mechanicznego, więc zawsze wygrywa
  najtańsza (HACCP w Pięć Minut). Dylemat będzie prawdziwy, gdy ocena da np. większy procent oczekujących.
- [ ] **Szafa chłodnicza i zamrażarka ★★★:** gwiazdki to tylko pojemność, opłaca się przy stałym nadmiarze towaru
  ponad ok. 500 l; dla botów (premium) to czysty koszt.
- [ ] **Lodówka na napoje ★★★:** zwrot ok. 18 tygodni, powyżej zakresu 10–14; zaakceptować albo obniżyć cenę do ok. 3 000.
- [ ] **Bot agresywny** jest bliski bankructwa na poziomie łatwym już przed zmianą cen (balans botów, nie katalogów).
- [ ] Zwroty dopłat ★★★ liczone z założonej marży na sztukę, a nie z pomiaru; przy mniejszym ruchu wydłużą się.
- [ ] **Opłata za zmianę biura:** A→samodzielnie→A jest dziś bez opłaty (gra pamięta ostatnie biuro); jeśli ma być
  płatne, zmienić regułę w `oplata_zmiany`. Obejście przez dwa płatne przeskoki (pakiet w biurze bez opóźnienia)
  zostawione.
- [ ] **Kontrola PIP:** liczą się zlecenie i zlecenie ze studentem w pełnym wymiarze; B2B i staż pominięte; po karze
  licznik się nie zeruje (kontrola co tydzień z szansą 5%); boty „tani” i „agresywny” tracą 10–40 pkt przez karę PIP
  i puste magazyny (nie rozdzielone).
- [ ] **Widok debetu i biura w panelu:** po wyborze banku komunikat jest tylko na karcie przed kliknięciem i w wynikach
  po przeliczeniu; pasek PIP pokazuje tekst pierwszej zagrożonej osoby; „mniej godzin” jako rada, choć nie ma suwaka
  godzin (realnie działa umowa o pracę).

## 5. Lekcje, serwer i termin
- [ ] kto uruchamia `manage.py zamykaj_rundy` na serwerze (bez tego tryb lekcyjny nie zamyka rund po terminie; rundy
  „na żywo” zamykają się też same, gdy wyślą wszystkie drużyny). Serwer to dziś laptop autora i tunel
- [ ] ile tygodni gry na cykl lekcji (wstępnie ok. 4, „ale się tym nie sugeruj”; scenariusze zakładają ok. 12)
- [ ] gotowe zestawy funkcji pod lekcje
- [ ] jedna strona „Cel i termin” uzgodniona z kapitanem: co i kiedy ocenia ZwzT, data pierwszej lekcji, lista ekranów
  „wersji na pierwszą lekcję” (dziś trzy sprzeczne terminy; termin zgłoszenia do konkursu 31.03.2027 niepotwierdzony)
- [ ] **Jawność AI:** `METODA.md` w repo gry i sprawdzenie regulaminu ZwzT pod kątem AI (krok 11 porządków) oraz rozmowa
  szefa z kapitanem. Stan 18.11: szkic `gra/METODA.md` jest; regulaminu 2026/27 nie udało się pobrać (strona organizatora blokuje boty),
  szef lub kapitan wkleja tekst z platformy, wnioski i pytania: [[Regulamin ZwzT a AI]]
- [ ] **Gra testowa z ludźmi** w 7–10 dni na obecnym `main` (kapitan + 4–8 uczniów, zestaw „Pierwsza gra”, 2–3 rundy,
  stoper, kartka „co było niejasne”). Szef 16.11: „może w przyszłym tygodniu, funkcji nie zamrażamy”. Z oceny sposobu
  pracy: do tego czasu bez nowych funkcji (szef tego nie przyjął)
- [ ] z oceny sposobu pracy 16.11 do przyjęcia lub odrzucenia przez szefa: budżet czytania (najwyżej 1 strona „do
  decyzji” i 8 pytań dziennie; szef: „czytam wszystko, bez limitów”); ustalenia z majstrem twarzą w twarz (kto rusza
  mapę, raporty, podpisy commitów prawdziwym nazwiskiem); licznik kosztu w „Stan prac”
  ([[Dziennik lidera]], zob. też [[Sprawozdanie – zespół agentów]])
- [ ] wygląd nowych pól kreatora trybu lekcyjnego (klasy `opcje-p`, `pole`) niesprawdzony na zrzucie
  ([[Tryb lekcyjny]])
- [ ] przełącznik „ikony ogólne” na pokaz dla urzędów (propozycja)

## 6. Wygląd
- [ ] układ na telefonie (wspólnie z majstrem; na razie tylko komputer)
- [ ] kiedy znika stary wybór układu panelu („bok”, „grafik”)
- [ ] kolejne nawiązania literackie (Zajdel, Winnetou, inne lektury)

## 7. Porządki i repozytoria
- [ ] dług w kodzie i dokumentacji: lista w [[Postęp]], „Dług w dokumentacji i kodzie”

## 8. Pytania po nocy Fable z 17.11
Trzy raporty Fable czekają na szefa. Pełne pytania, makiety i skrypty są w `archiwum/fable-17.11/fable-*/` (po przeniesieniu:
`Serie/fable`).

### 8a. Dziury w ekonomii (`archiwum/fable-17.11/fable-dziury/raport.md`, tabela w `dziury.md`)
Wzorzec: bot `zrownowazony` grający jako człowiek, 12 tygodni, 3 ziarna; za dziurę uznana różnica o tym samym znaku
na wszystkich ziarnach (szum pojedynczej gry ok. ±15 pkt). Jedna drużyna sama gry nie złamie.
- [ ] **D3–D5 (kosmetyka):** lokata obniża punkty; pożyczka w ostatnim tygodniu pompuje gotówkę; zdarzenia opłaca się
  ignorować. Poprawiać po grze testowej czy teraz?
- [ ] **D6:** 150 pkt „Zaopatrzenie” w tygodniu otwarcia jest nie do zdobycia; odblokować dostawców w tygodniu 1
  (pasuje do zeszytu wujka, §8b)?
- [ ] pomiar szumu (ta sama strategia w dwóch firmach różni się o ±16 pkt) wziąć pod uwagę przy ocenianiu drużyn na lekcji

### 8b. Zeszyt wujka (`archiwum/fable-17.11/fable-zeszyt/raport.md`, treść w `zeszyt.md` i `zeszyt-szkic.yaml`)
Szkic: 48 zadań w 18 tygodniach, 23 warunki odhaczania, rozdział „gdzie co najlepiej kupić” z cenami z `dostawcy.yaml`.
- [ ] **Bazar** nie ma żetonu, a zadanie tygodnia 6 do niego prowadzi (zob. §8c, pyt. 7)
- [ ] **Odhaczanie „wizytą”** jest po stronie przeglądarki (inny komputer = nieodhaczone). Wystarczy, czy zapisywać w grze?
- [ ] **Pojęcie z WOS** przy zadaniu: pokazywać graczom (małym drukiem) czy tylko mistrzowi gry? Przyjęte: tylko mistrz gry
- [ ] **Wujek poleca konkretne sklepy po nazwie** (Biedronka, Lidl…). Zgodne z decyzją o prawdziwych markach, ale to już
  rekomendacja, nie tło: zostaje?
- [ ] zadania tygodni 12–17 są przeglądowe (po jednym), bo harmonogram nie odblokowuje już nic po tygodniu 11. Wystarczy?

### 8c. Projekt wnętrz (`archiwum/fable-17.11/fable-wnetrza/raport.md`, `projekt.md`, makiety w `makiety/`)
Makiety scen dla każdego żetonu mapy i warianty alternatywne. Fable zaproponował: Solaris znika (6 → 5 banków), boczek
zamiast układu pływającego, Kamienica rachmistrzów jako klatka schodowa, Dom reklamy z numerami pięter przy szybie windy.
- [ ] **1. Który bank znika (6 → 5)?** Decyzja szefa 16.11: 5 banków w pierzei. Propozycja Fable: **Solaris** (ryzyko
  praw autorskich, Lem; najmniej „lubelski”). To zmienia ekonomię (znika debet 40 000 zł) i wymaga zmiany `banki.yaml`;
  w danych jest jeszcze 6, decyzja: 5. Co z dużym debetem: do Soplicowa, do Kmicica, czy znika? Jak wygląda rząd
  z Solarisem: makieta `pierzeja_alt`
- [ ] **5. Urzędy skarbowe** (VAT, PIT) w ratuszu przy Szeligowskiego: zgoda? Sanepid osobno ma własny żeton i wnętrze
- [ ] **6. „Wyślij decyzje”:** przycisk w boczku wysyła od razu, czy prowadzi na Pocztę (okienko nadawcze)?
- [ ] **7. Bazar:** nie ma żetonu na mapie. Dodać (gdzie?), czy handel zostaje bez wnętrza?
- [ ] **8. Parki:** siedem żetonów, jeden wzór sceny z jednym obiektem w tle. Wystarczy, czy parki zostają samą informacją
  na mapie?
- [ ] **9. Giełda:** w silniku nie ma jeszcze decyzji giełdy (budynek `gielda` jest). Scena jest gotowa „na zapas”;
  czy żeton ma być czynny przed mechaniką?
- [ ] **10. Nazwa sklepu ze sprzętem:** zostaje „Hurtownia sprzętu gastronomicznego”, czy „Konstruktorzy T&K” z planu
  nawiązań?
- [ ] **12. Dozorczyni w Kamienicy rachmistrzów** stoi jako postać Dulskiej (zastępstwo): zostawić jako nawiązanie
  (kamieniczniczka) czy nowa postać?
- [ ] przed wdrożeniem: etykiety w kilku makietach nachodzą na rysunek, w palecie wysokiej napisy na szyldach się
  zmniejszają, byk i koziołek na giełdzie wymagają prawdziwych symboli z generatora grafik (zob. raport)
