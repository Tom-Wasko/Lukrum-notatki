# Krytyka wyglądu wnętrz LUKRUM (16.11.2026)

Recenzja świeżym okiem: jak zobaczy to licealista i nauczyciel. Kopia robocza `krytyka` (detached `main`), gra pokazowa
zatrzymana na tygodniu 6, okno 1400×900. Zrzuty: `archiwum/krytyka-16.11/zrzuty/` (nazwa pliku = paleta-tryb-miejsce), zrzuty makiet: `archiwum/krytyka-16.11/zrzuty/makiety/`.
Role: **szef** (autor), **majster** (kolega od mapy), **kapitan** (nauczyciel opiekun), lider (Claude Opus).

Stan pliku: komplet, części (a)–(f).

## (a) Werdykt ogólny

Gra ma **jedno prawdziwe wnętrze (kebab) i osiem poczekalni**. Kebab jest narysowany, żyje (goście, obsługa, ceny na
tablicy, szyld z nazwą drużyny) i od razu widać, o czym jest gra. Pozostałe miejsca to ten sam pusty korytarz z rzędem
identycznych drzwi albo okienek: różnią się tylko napisem na tabliczce. Licealista po trzecim takim ekranie przestanie
patrzeć na scenę i zacznie klikać kafelki „Co tu zrobisz” pod spodem, czyli scena stanie się ozdobnikiem, który trzeba
przewinąć.

Trzy rzeczy psują odbiór najbardziej:
1. **Scena nie jest miejscem decyzji.** Klik wyrzuca do zwykłej zakładki z formularzem i paskiem do 10 podzakładek
   (`bar-jasny-zespol-ekran.png`). Wnętrze jest więc tylko menu z obrazkiem. Decyzja szefa nr 2 trafia w sedno.
2. **Klikalne miejsca wyglądają jak siatka debugowania.** Przerywane ramki i kółka „+” na wszystkim, a nazwa punktu
   pojawia się dopiero po najechaniu myszą, czyli na tablecie i telefonie nigdy.
3. **PRL jest tylko w kebabie i w gazecie.** Hole i okienka nie mają lamperii, lastryko, paprotki, tablicy z literkami,
   numerków. To najtańsze miejsce na „nutkę PRL”, a jest puste.

Co jest dobre i warto zachować: postacie (spójny, sympatyczny styl), tablica menu z prawdziwymi cenami i plakietką
„BRAK”, „Kurier rankingowy” jako gazeta, „Księga gości” ze strzałkami ▲▼, zamknięte drzwi z kłódką i plakietką
„od tygodnia 7”, hala hurtowni z własnym tłem, wszystkie trzy palety działają bez błędów w konsoli.

## (b) Wnętrza po kolei

Priorytet: **W** wysoki, **Ś** średni, **N** niski.

### 1. Mój kebab
Zrzuty: `bar-jasny-kebab.png`, `bar-ciemny-kebab.png`, `pewex-jasny-kebab.png`, `wysoka-jasny-kebab.png`,
`wysoka-ciemny-kebab.png`, `bar-jasny-kebab-telefon.png`, `bar-jasny-kebab-karta.png`.

Działa: kompozycja (okno, szyld, tablica, lada, rożen, zaplecze), obsługa z imionami, goście z dymkami, karta WOS
„Jak to jest z prawem?” z podstawą prawną, zmiana wystroju według typu lokalu.

| # | Co źle | Dlaczego | Jak poprawić | Pr. |
|---|---|---|---|---|
| K1 | 12 przerywanych ramek z kółkiem „+” naraz (bar jasny). Ramki pracownika, kasy i lady nachodzą na siebie. | Wygląda jak tryb edycji, nie jak lokal. Nie wiadomo, co jest ważne. | Ramka tylko po najechaniu/fokusie. W spoczynku mała stała etykieta przy przedmiocie (makieta 02). Pracownika połączyć z zapleczem. | W |
| K2 | Nazwa punktu tylko po najechaniu. | Dotyk nie ma „najechania”; uczeń na tablecie widzi same plusy. | Etykiety stałe, krótkie („Menu i ceny”, „Zespół”). | W |
| K3 | Paleta wysoka (jasna i ciemna): grube pełne ramki zamykają postacie i sprzęt w czarnych/białych prostokątach. | Scena staje się nieczytelna właśnie dla tych, dla których jest ta paleta. Gość w ramce wygląda jak zaznaczony błąd. | W wysokiej nie rysować ramek w spoczynku, tylko etykiety z grubym obrysem; ramka po fokusie. | W |
| K4 | Telefon 400 px: scena ma ok. 350×175 px, punkty po 15–30 px. | Nie da się trafić palcem; scena jest tylko obrazkiem nad listą. | Na wąskim ekranie scena przewijana w poziomie (wysokość ok. 60% ekranu) albo sama lista z miniaturą. Do decyzji razem z „telefon – odłożone”. | Ś |
| K5 | Napis „MIEJSCE NA DODATKI” w ramce na ścianie. | Wygląda jak niedokończona grafika. | Pusty gwóźdź i jaśniejszy prostokąt po zdjętym obrazie; podpis dopiero w etykiecie. | Ś |
| K6 | Wujek stoi na drzwiach zaplecza i zasłania punkt „Zaplecze”. | Dwa cele w jednym miejscu, dymek wujka przykrywa drzwi. | Wujek przy oknie albo przy portrecie (lewa strona), drzwi wolne. | Ś |
| K7 | Lista „Co tu zrobisz”: 12 kafelków, z czego 4 (chłodnia, pokój socjalny, biurko, szuflada) nie istnieją na scenie. | Scena i lista opowiadają dwa różne lokale. Po decyzji „wnętrza dla wszystkich funkcji” to dziura. | Dorysować: chłodnię (drzwi obok zaplecza albo w oknie zaplecza), biurko z szufladą w rogu. Listę zostawić tylko jako spis dla czytników i telefonu. | W |
| K8 | Tablica: „KEBAB W TORTILLI…” ucięte, trzy czerwone „BRAK” zasłaniają pół tablicy. | Najważniejsza informacja lokalu jest w najmniejszym druku sceny. | Skrót nazw w danych („Tortilla”), „BRAK” jako przekreślenie kredą + ! na końcu wiersza. | Ś |
| K9 | Tryb ciemny: drzwi zaplecza świecą jaskrawym błękitem, opinie w Księdze gości są kremowe na ciemnym tle. | Dwa najjaśniejsze elementy ekranu to rzeczy nieważne. | Drzwi z `--g-metal2`/przyciemniony `--akcent-2`; karty opinii z `--g-karta`. | N |
| K10 | Saldo i tydzień są trzy razy: górny pasek, nagłówek sceny, „Kasa” na scenie. | Szum. | Zniknie z decyzją nr 1 (jeden HUD). | N |

### 2. Kamienica bankowa
Zrzuty: `bar-jasny-kamienica_bankowa.png`, `bar-ciemny-kamienica_bankowa.png`, `wysoka-jasny-kamienica_bankowa.png`,
`bar-jasny-bank-ekran.png`.

Działa: nazwy banków z lektur i krótkie hasła („kredyt na start”, „lokaty”) dobrze uczą, że banki się różnią.

| # | Co źle | Dlaczego | Jak poprawić | Pr. |
|---|---|---|---|---|
| B1 | Siedem identycznych brązowych drzwi w rzędzie. | Banki konkurują ofertą, a wyglądają jak szafki w szatni. Zero tożsamości. | Fasada z szyldami (decyzja 3, makieta 04): każdy bank ma własny szyld, kolor markizy i znak. | W |
| B2 | Wszystkie drzwi prowadzą na ten sam ekran. Kliknięto „Kmicic”, a ekran zaczyna się od „Konto firmowe: Ziemia Obiecana”. | Gracz myśli, że kliknął źle. | Wnętrze jednego banku: lada, doradca, tylko oferta tego banku + „Twoje konto jest w…”. | W |
| B3 | „Oszczędności Rzeckiego” zmniejszone do ok. 9 px, żeby zmieścić się na tabliczce. | Nieczytelne, zwłaszcza na rzutniku w klasie. | Szyld dwuwierszowy albo skrót „Rzecki – oszczędności”. | Ś |
| B4 | Parkiet maklerski „Byk i Koziołek” to ósme takie same drzwi. | Giełda to inna czynność (prywatne pieniądze właściciela) i inny nastrój. | Osobne wejście: brama w podwórze albo suterena z tablicą kursów. | Ś |
| B5 | Jedna trzecia sceny to pusta podłoga, nikogo nie ma. | Martwo. | Portier, klient z teczką, zegar; po przejściu na fasadę problem znika. | N |
| B6 | Ekran banku ma fioletowe akcenty spoza palety (kolor marki banku wpisany na sztywno). | Łamie zasadę „kolory tylko ze zmiennych”; w palecie wysokiej fiolet na szarym ma słaby kontrast. | Marki rozróżniać znakiem i wzorem, kolor brać z `--akcent`/`--akcent-2`. | Ś |

### 3. Biurowiec przy Zana
Zrzuty: `bar-jasny-biurowiec_zana.png`, `bar-ciemny-biurowiec_zana.png`, `bar-jasny-biuro-ekran.png`, `bar-jasny-agencje-ekran.png`.

Działa: zamknięte drzwi „Lajk i Spółka” (kłódka + „od tygodnia 7” + przerywany kafelek) to wzorowe pokazanie stanu bez
samego koloru.

| # | Co źle | Dlaczego | Jak poprawić | Pr. |
|---|---|---|---|---|
| Z1 | Pięć jednakowych szklanych drzwi, za szybą nic. | Jak w kamienicy: brak tożsamości firm. | Po wyprowadzce biur i agencji (decyzje 4, 5) zostają ubezpieczenia + księga: zrobić jedno biuro z okienkiem agenta TUW i regałem z księgą. | W |
| Z2 | „Księga firmy (KPiR)” jest drzwiami do firmy. | To własna księga gracza, nie usługodawca. | Księga leży fizycznie: segregator na biurku w kebabie (K7) albo regał w kamienicy rachmistrzów „prowadzę sam”. | Ś |
| Z3 | Drzwi „Fala Koziołka” → ekran zatytułowany „Fala Koziołka – ulotki, radio i eventy”, podzakładka „Ulotki i radio”, a pierwsza firma to Drukarnia „Papier Przyjmie”. | Trzy nazwy na jedną rzecz. W środku są trzy różne firmy (drukarnia, radio, eventy) pod szyldem jednej. | Winda (decyzja 5): każda firma ma piętro i własną nazwę. | W |
| Z4 | Jedne drzwi „Biura rachunkowe”, a w środku cztery firmy (J.K.Ś., Józef K., Scrooge, Asteroida 328). | Wybór biura to porównanie czterech ofert; scena tego nie pokazuje. | Osobna kamienica z czterema szyldami (decyzja 4). | W |
| Z5 | Szary pas u góry sceny jako jedyny znak „biurowca”. | Nie czyta się jako nic. | Sufit kasetonowy ze świetlówkami, tablica informacyjna z literkami, wykładzina. | N |

### 4. Park handlowy
Zrzut: `bar-jasny-park_handlowy.png`.

| # | Co źle | Dlaczego | Jak poprawić | Pr. |
|---|---|---|---|---|
| P1 | Troje drzwi na środku pustej ściany; połowa sceny wolna. | Nie wygląda jak pasaż ani sklep. To najsłabsza scena w grze. | Trzy witryny sklepowe z towarem za szybą: rożen i frytownica, stolik z parasolem, meblościanka z kryształami. Witryna = punkt. | W |
| P2 | „Sprzęt gastronomiczny” to ten sam ekran co „Rożen” w kebabie. | Dwie drogi do tego samego formularza; po decyzji 2 kebab ma tylko odsyłać. | W kebabie: stan sprzętu + „kupisz w Parku handlowym”. Kupno tylko tutaj. | W |
| P3 | „Instalacje i wyposażenie” kontra „Meblościanka: wystrój” – granica niejasna (stoliki są w pierwszym, meble w drugim). | Gracz nie wie, gdzie kupić stolik. | Jedna nazwa na jedno: „Stoliki i ogródek” oraz „Wystrój”. Pytanie do szefa (e). | Ś |
| P4 | Brak sprzedawcy, brak cen. | Scena hali (hurtownie) ma sprzedawcę, pasaż nie. | Sprzedawca w fartuchu przy jednej z witryn, metki z ceną „od … zł”. | N |

### 5. Stare Miasto
Zrzuty: `bar-jasny-stare_miasto.png`, `pewex-jasny-stare_miasto.png`.

| # | Co źle | Dlaczego | Jak poprawić | Pr. |
|---|---|---|---|---|
| S1 | Te same drzwi co w banku, lekko różowa ściana z poziomymi kreskami ma udawać cegłę. | „Brama kamienicy przy Grodzkiej” z nagłówka nie istnieje na obrazku. | Sklepiona sień z brukiem i latarnią; drzwi różnej wielkości i kształtu po obu stronach, prześwit na podwórze. | W |
| S2 | Biuro nieruchomości, sala licytacji, notariusz i lichwiarz wyglądają tak samo. | To cztery różne nastroje; Harpagon powinien odstraszać. | Klucz: witryna z ogłoszeniami; licytacje: podwójne drzwi z młotkiem; notariusz: mosiężna tabliczka; kantor: krata w okienku, neon „POŻYCZKI”. | Ś |
| S3 | „Nocna 13” (gdy włączona) dostaje pełnoprawne piąte drzwi z tabliczką „bez szyldu”. | Tabliczka z napisem „bez szyldu” jest sprzecznością. | Drzwi do sutereny bez tabliczki, tylko wizjer i słabe światło; etykieta dopiero po najechaniu. | N |

### 6. Miasteczko akademickie
Zrzuty: `bar-jasny-miasteczko.png`, `pewex-ciemny-miasteczko.png`, `wysoka-jasny-miasteczko.png`.

Szef ma rację: to wygląda słabo. Konkretnie:

| # | Co źle | Dlaczego | Jak poprawić | Pr. |
|---|---|---|---|---|
| M1 | Scena jest identyczna z Urzędami (te same cztery okienka, lady, paprotki). | Gracz nie wie, gdzie jest. Nic nie mówi „uczelnia”. | Własna scena: hol akademika/uczelni (makieta 06). | W |
| M2 | „Tablica ogłoszeń” jest okienkiem z urzędnikiem. | Tablica ogłoszeń to tablica. Metafora się wali na pierwszym punkcie. | Prawdziwa tablica korkowa z kartkami i odrywanymi paskami; liczba kartek = liczba kandydatów. | W |
| M3 | Lady to cztery wielkie brązowe prostokąty: ok. 35% sceny bez żadnej treści. W Pewex ciemnym świecą jako najjaśniejsza plama. | Wzrok idzie na puste pudła. | Mniej mebla, więcej rekwizytu: stół z mapą stref (Pracownia Analiz), drzwi z lupą (Sokole Oko), kalendarz ścienny. | W |
| M4 | Postacie przycięte do popiersi w ogromnych szybach, tabliczka „OKIENKO 1” zasłania im tors. | Najlepszy zasób gry (postacie) pokazany najgorzej. | Postacie w całości, stojące przy swoich rekwizytach. | Ś |
| M5 | Cztery punkty to cztery różne instytucje (agencja pracy, pracownia badań, detektyw, kalendarz miasta) wciśnięte do jednej sali. | Detektyw od konkurencji „w okienku na uczelni” jest nielogiczny. | Detektyw jako drzwi z matową szybą w rogu albo osobny budynek (pytanie do szefa). | Ś |

### 7. Urzędy
Zrzuty: `bar-jasny-urzedy.png`, `wysoka-ciemny-urzedy.png`.

Działa: tu metafora okienek jest na miejscu. To jedyna scena, w której okienka powinny zostać.

| # | Co źle | Dlaczego | Jak poprawić | Pr. |
|---|---|---|---|---|
| U1 | Dwa okienka mają tę samą nazwę „Urząd skarbowy”. | Różni je drobny podpis. | „Skarbowy: VAT” i „Skarbowy: PIT”, albo jedno okienko z dwiema sprawami w okienku decyzji. | Ś |
| U2 | Brak PRL-u w miejscu, które się o niego prosi. | Zmarnowana okazja na humor i klimat. | Lamperia, tablica z wymiennymi literkami, automat z numerkami, kartka „Przerwa śniadaniowa 10:00–10:15”, pieczątki na ladzie. | Ś |
| U3 | Ratusz i Sanepid to dwa budynki na mapie, a jedna sala. | Adres w nagłówku ma dwie ulice. | Zostawić jedną salę („Centrum obsługi”), ale okienka pogrupować tabliczkami instytucji. | N |
| U4 | Ogromne lady, jak w M3. | Jak wyżej. | Niższa lada, na niej rekwizyty sprawy (teczka, pieczątka, wniosek). | Ś |

### 8. Kurier rankingowy (redakcja)
Zrzut: `bar-jasny-redakcja.png`.

Działa: pierwsza strona gazety to najlepszy pomysł wizualny poza kebabem. Tytuł, wydanie, kolumny, strzałki ▲▼ w tabeli.

| # | Co źle | Dlaczego | Jak poprawić | Pr. |
|---|---|---|---|---|
| R1 | Pod gazetą jest jeszcze scena z trzema okienkami, które powtarzają linki z gazety. | Ekran ma ok. 1500 px wysokości; scena jest poniżej zgięcia i nic nie dodaje. | Scena redakcji jako tło, gazeta leży na biurku na pierwszym planie; albo sama gazeta bez okienek. | W |
| R2 | Papkin z szablą jako urzędnik „Tabeli ligowej” w okienku. | Zabawne raz, ale to kopia sceny urzędu. | Redakcja: biurka z maszynami do pisania, tablica z tabelą ligową na ścianie, zecer przy kaszcie. | Ś |
| R3 | Kolumna „Wasz tydzień w liczbach” ma 12 wierszy drobnego tekstu. | Najważniejsze liczby tygodnia giną. | Trzy duże liczby (klienci, przychód, dochód), reszta w „Punkty tygodnia”. | Ś |

### 9. Hurtownie i dyskonty
Zrzuty: `bar-jasny-hurtownie.png`, `bar-ciemny-hurtownie.png`, `wysoka-ciemny-hurtownie.png`.

Działa: własne tło hali, regały z towarem, sprzedawca przy kasie, wózek. Druga najlepsza scena.

| # | Co źle | Dlaczego | Jak poprawić | Pr. |
|---|---|---|---|---|
| H1 | Podpisy pod regałami („dostawcy, jakość, dzień dostawy”) leżą dokładnie na przerywanej linii podłogi. | Tekst wygląda na przekreślony/podkreślony, we wszystkich paletach. | Podpis na tabliczce z tłem albo przesunięty o 20 px. Poprawka na 5 minut. | W |
| H2 | „Rampa” to regał z towarem. | Rampa to brama z ciężarówką. | Brama rolowana z tyłem ciężarówki po prawej. | Ś |
| H3 | Sprzedawca i kasa nie są klikalne, choć wyglądają na najważniejsze. | Gracz kliknie właśnie tam. | Kasa = „Zamówienia tego tygodnia” (podsumowanie koszyka). | Ś |
| H4 | Jedna hala dla dziewięciu budynków mapy (Makro, Selgros, Lidl, piekarnia…). | Na mapie to różni dostawcy, w środku anonimowy regał. | Jeden regał na dostawcę z jego szyldem nad regałem (w okienku: oferta tylko tego dostawcy). | Ś |
| H5 | Paleta wysoka ciemna: snopy światła jako szare trójkąty na czarnym tle. | Wyglądają jak błąd renderowania. | W palecie wysokiej wyłączyć snopy. | N |

### 10. Miejsca bez wnętrza (Bazar, Plan tygodnia, akademia, drukarnia, poczta)
Klik w budynek otwiera zwykły ekran, bez sceny. Po decyzji 2 każde potrzebuje wnętrza. Propozycje w (d), punkt 2.

## (c) Problemy wspólne

**Spójność**
- C1. Trzy szablony (hol, okienka, hala) na osiem miejsc: cztery hole różnią się kolorem drzwi, trzy sale okienek niczym.
  Każde miejsce powinno mieć jeden rekwizyt, po którym się je poznaje z miniatury. **W**
- C2. Ta sama lampa i ta sama paprotka w każdej scenie, w tych samych miejscach. **N**
- C3. Jeden cel ma kilka wejść i nazw (sprzęt: „Rożen” i „Sprzęt gastronomiczny”; klienci: „Okno” w kebabie
  i „Pracownia Analiz”; agencje: trzy nazwy). Zasada: jedna rzecz, jedno miejsce, jedna nazwa. **W**
- C4. Ekrany decyzji mają inny język wizualny niż sceny: zaokrąglone karty, kolory marek spoza palety, małe szare
  przyciski. Po przeniesieniu do okienek ta różnica będzie widoczna w jednym kadrze. **Ś**

**Czytelność**
- C5. Klikalność pokazana ramką przerywaną + „+” (patrz K1), nazwa tylko po najechaniu (K2). **W**
- C6. Scena ma stały format 1220×612 i zajmuje ok. 60% szerokości okna; reszta to pasek boczny, górny i nagłówek. **W**
  (rozwiązuje decyzja 1)
- C7. Napisy na tabliczkach 12–15 jednostek sceny, czyli ok. 11–13 px na laptopie; na rzutniku w klasie nieczytelne. **Ś**
- C8. Lista „Co tu zrobisz” powtarza scenę 1:1. Zostawić jako tekstowy spis (czytniki, telefon), zwinięty domyślnie. **Ś**

**PRL**
- C9. Poza kebabem (kaloryfer, portret, szyld) i gazetą nie ma go wcale. Tani zestaw rekwizytów do wspólnego użycia:
  lamperia olejna, lastryko, tablica z literkami, numerki, paprotka na kwietniku, zegar, kartka „Zaraz wracam”,
  neon, saturator, boazeria. **Ś**

**Dostępność**
- C10. Paleta wysoka: ramki punktów zasłaniają scenę (K3). **W**
- C11. Cele dotykowe na telefonie poniżej 24 px (K4). **Ś**
- C12. `okno()`: zamknięcie to `<span>✕</span>`, nie przycisk; brak `role="dialog"` i pułapki fokusu. Przed
  przeniesieniem wszystkich decyzji do okienek trzeba to naprawić. **W**
- C13. Postać z dymkiem pokazuje treść tylko po najechaniu/fokusie; na dotyku dymka WOS nie da się przeczytać bez
  kliknięcia. **Ś**
- C14. Stan bez samego koloru: dobrze w Księdze gości (▲▼), na drzwiach (kłódka, „!”). Źle: „BRAK” na tablicy to sam
  czerwony prostokąt z tekstem (tekst ratuje), czerwone nazwy wierszy „Cena”, „Obsługa” w Księdze. **N**

**Kolory**
- C15. Kolory na sztywno poza `zmienne.css`: `styl.css` (41 wartości hex), `zakladki/ikony_marek.js` (21),
  `zaslona` okna ma `rgba(20,15,10,.5)`, nagłówek okna `var(--pom)` ze starego motywu. Okienka nad sceną muszą brać
  kolory wyłącznie ze zmiennych palety. **Ś**

**Tekst**
- C16. Nagłówki ekranów decyzji są długie i wielkimi literami („KAMIENICA BANKOWA – KONTO, KREDYTY I LOKATY”), łamią
  się na dwa wiersze. W okienku: krótki tytuł + okruszek. **N**
- C17. Etykiety punktów mieszają wzory: „Tablica: menu i ceny”, „Biura rachunkowe”, „Fala Koziołka”. Wzór dla sceny:
  rzeczownik czynności, najwyżej 3 słowa („Menu i ceny”); nazwa firmy tylko na jej szyldzie. **N**

## (d) Propozycje projektowe do decyzji szefa 1–6

Makiety: `archiwum/krytyka-16.11/makiety/index.html` (spis). Każda makieta ma u góry przełącznik wariantu, palety i trybu; parametry działają
też w adresie (`?w=A&paleta=pewex&tryb=ciemny`). Rysunki w makietach są własne i uproszczone: pokazują układ, nie
docelową kreskę (w grze: postacie i symbole z `grafiki/zestaw.svg`). Liczby w makietach są przykładowe.

Wspólna zasada dla wszystkich wnętrz („estrada”): scena na cały ekran, u góry jedna belka (◂ Mapa, nazwa miejsca,
tydzień, kasa, „Wyślij decyzje”), etykiety punktów widoczne stale, ramka dopiero po najechaniu albo fokusie.

### Decyzja 1. Mapa na cały ekran, ikony w rogach, lista wujka
Makieta: `archiwum/krytyka-16.11/makiety/01-mapa-pelny-ekran.html` (klik w pozycję listy przesuwa i przybliża mapę, budynek pulsuje).
Zrzuty: `archiwum/krytyka-16.11/zrzuty/makiety/01-A-jasny.png`, `01-A-ciemny-pokaz.png`, `01-C-pewex.png`.

Układ rogów (wspólny dla wariantów):
- lewy górny: **Tydzień 6 z 18** (z paskiem postępu sezonu) i **Kasa**;
- prawy górny: **?** (Jak grać), **⚙** (wygląd, ustawienia), **konto** (inicjały drużyny);
- prawy dolny: **Wyślij decyzje** (jedyny duży, kolorowy przycisk na ekranie; plakietka „! 4 do poprawy” zastępuje
  osobną „Listę błędów”), nad nim + − ⌂ mapy;
- lewy dolny: **lista wujka**.

Lista wujka: kartka w kratkę z marginesem, pismo odręczne, pinezka. Każda pozycja ma dwa wiersze: *co* („Towar na cały
tydzień!”) i *gdzie* („➜ Hurtownie, Mełgiewska”). Zrobione = ☑ + przekreślenie, bieżące = podkreślenie, czyli stan bez
samego koloru. Na dole dopisek „PS.” na miejsce dzisiejszego listu wujka. W palecie wysokiej pismo odręczne zamienia
się na zwykły krój pochylony.

| Wariant | Opis | Za | Przeciw |
|---|---|---|---|
| **A. Kartka w rogu** (rekomendacja) | Kartka przypięta w lewym dolnym rogu, zwijana przyciskiem ▾ do paska z wariantu C. | Zawsze widać plan tygodnia; najbardziej „wujkowa”. | Zasłania południowy zachód mapy (ok. 25% szerokości na laptopie). |
| B. Zeszyt z boku | Wysuwany z prawej krawędzi, ucho „Lista wujka · 3 z 7”. | Mieści długą listę. | Zasłania wschód (hurtownie, Felin), koliduje z ikonami konta. |
| C. Tylko następny krok | Pasek na dole: wujek + jedno zdanie + „Pokaż”. | Prawie nic nie zasłania; jedyny sensowny na telefonie. | Nie widać całości planu. |

Rekomendacja: **A domyślnie, C jako stan zwinięty i jako widok na wąskim ekranie.** Dane listy już są
(`zakladki/wujek.js: kroki()` zwraca miejsce, czynność i stan), trzeba dodać id budynku do każdego kroku.
Do uzgodnienia z majstrem: funkcja mapy „pokaż budynek” (przesuń, przybliż, pulsuj), np. `lukrum.pokazNaMapie(id)`.

### Decyzja 2. Wnętrza dla wszystkich funkcji, decyzje w okienku nad sceną
Makiety: `archiwum/krytyka-16.11/makiety/02-okienko-decyzji.html`, `archiwum/krytyka-16.11/makiety/03-idz-gdzie-indziej.html`.
Zrzuty: `archiwum/krytyka-16.11/zrzuty/makiety/02-A-jasny.png`, `02-B-ciemny.png`, `02-C-wysoka.png`, `03-A-jasny.png`,
`03-B-pewex-ciemny.png`, `03-C-jasny.png`.

**Okienko decyzji**

| Wariant | Opis | Za | Przeciw |
|---|---|---|---|
| **A. Teczka na środku** (rekomendacja) | Okno do 940 px nad przyciemnioną sceną. Nagłówek: okruszek „Mój kebab ▸ drzwi na zaplecze” + tytuł + ✕. Pod nim zakładki okienka. Stopka: „✓ Zapisano w decyzjach roboczych”, „Gotowe”. | Jedno okno na wszystko, mieści tabele; to rozbudowa istniejącego `okno()`. Na telefonie pełny ekran. | Zasłania scenę na czas decyzji. |
| B. Szuflada z boku | Panel 540 px z prawej, scena obok żyje. | Widać skutek decyzji na scenie. | Za wąska na bank, KPiR, grafik; poniżej 1100 px i tak pełny ekran. |
| C. Dymek przy przedmiocie | Mały dymek z 1–3 polami (cena dania). „Całe menu…” otwiera teczkę. | Najszybszy, bardzo „growy”. | Tylko dla prostych decyzji. |

Rekomendacja: **A jako standard, C później dla 2–3 najczęstszych decyzji (ceny, promocja).** Treść okienka to dzisiejsze
ekrany zakładek renderowane do okna zamiast do `#karta`; pasek podzakładek znika, w okienku zostają najwyżej 3–4
zakładki tego punktu sceny. Wymagania dostępności: `role="dialog"`, fokus w oknie, Esc, powrót fokusu na punkt, ✕ jako
`<button>`.

**Komunikat „to załatwisz gdzie indziej”**

| Wariant | Opis | Za | Przeciw |
|---|---|---|---|
| **A. Mówi ktoś z obsługi** (rekomendacja) | Dymek postaci: „Stoliki? Tego u nas się nie kupi. Meble są w Meblościance w Parku handlowym.” + stan („Teraz w sali: 4 stoliki”) + „Pokaż na mapie ➜”. | Znana forma (dymki gości), uczy miasta. | Potrzebna postać w scenie; bez obsady mówi wujek z portretu. |
| B. Metka na przedmiocie | Metka sklepowa przy stoliku ze stanem i odsyłaczem. | Ładny rekwizyt, stan widać stale. | Mały tekst, przy krawędzi sceny się nie mieści. |
| C. Drogowskaz na dole | Stały pasek u dołu ekranu. | Przewidywalne miejsce, dobre dla czytników i telefonu. | Mniej klimatu. |

Rekomendacja: **A, a na wąskim ekranie C.** Zawsze trzy rzeczy: co tu jest teraz, gdzie to kupić, przycisk „Pokaż na
mapie” (ten sam mechanizm co lista wujka). Punkt „tylko do oglądania” ma strzałkę na etykiecie („Sala ➜ Meblościanka”).

**Brakujące wnętrza (bez pustych okien wyboru)**

| Miejsce | Propozycja sceny | Punkty |
|---|---|---|
| Kebab: zaplecze | Chłodnia jako drugie drzwi (z termometrem), biurko z szufladą w rogu sali, segregator = księga firmy. | chłodnia, czas właściciela, portfel, (księga) |
| Bazar | Stragany pod parasolami, każdy stragan to oferta innej drużyny, tablica „Kupię / Sprzedam”. | oferty, moje ogłoszenia, licytacje |
| Poczta | Okienko nadawcze, waga, skrzynka: „Wyślij decyzje” jako list z pieczątką. | wyślij, potwierdzenie nadania |
| Akademia | Sala wykładowa z tablicą i rzutnikiem. | szkolenia, lekcje |
| Drukarnia | Wchodzi do Domu reklamy (1. piętro), osobny budynek na mapie zbędny albo prowadzi do windy. | ulotki, plakaty |
| Plan tygodnia | Znika jako ekran: zastępuje go lista wujka na mapie. | – |
| Parkiet | Podwórze kamienicy bankowej: tablica kursów z ▲▼, makler. | akcje, obligacje |

### Decyzja 3. Kamienica bankowa: fasada z szyldami, potem wnętrze banku
Makieta: `archiwum/krytyka-16.11/makiety/04-kamienica-bankowa.html`. Zrzuty: `archiwum/krytyka-16.11/zrzuty/makiety/04-A-jasny.png`, `04-B-ciemny.png`,
`04-C-wysoka-ciemny.png`, `04-W-pewex.png`.

| Wariant | Opis | Za | Przeciw |
|---|---|---|---|
| **A. Jedna kamienica** (rekomendacja) | Trzy banki na parterze (witryna, markiza, szyld), trzy na piętrze (szyld nad balkonem), brama w podwórze = parkiet „Byk i Koziołek”. | Jeden budynek jak na mapie; wszystkie banki w kadrze; szyldy szerokie. | Trzeba pilnować, żeby parter nie wyglądał na „ważniejszy”. |
| B. Pierzeja | Sześć wąskich kamieniczek, każda inna. | Najładniejsze, lubelskie. | Wąskie szyldy (długie nazwy ciasno), brak miejsca na bramę parkietu. |
| C. Fasada + spis | A plus mosiężny spis przy bramie z jedną liczbą na bank. | Porównanie bez wchodzenia; klawiatura, telefon. | Zasłania część fasady (zwijany). |

Rekomendacja: **A + spis z C jako zwijany dodatek.** Każdy szyld ma inny kształt, kolor z palety i monogram, więc banki
rozróżnia się nie tylko kolorem. Chorągiewka „TU MASZ KONTO” pokazuje bank drużyny.

Wnętrze banku (wariant W makiety): jeden szablon dla sześciu banków. Tablica „Oprocentowanie” z liczbami tego banku,
dwa okienka (Kasa = konto i debet, Doradca = kredyty i leasing), sejf = lokaty. Na dole plakietka „Twoje konto jest
w banku…”. Punkty otwierają okienka z decyzji 2. Powrót: „◂ Kamienica”.

### Decyzja 4. Biura rachunkowe w osobnej kamienicy
Makieta: `archiwum/krytyka-16.11/makiety/05-kamienica-rachmistrzow.html`. Zrzuty: `archiwum/krytyka-16.11/zrzuty/makiety/05-B-jasny.png`, `05-W-ciemny.png`.

| Wariant | Opis | Za | Przeciw |
|---|---|---|---|
| **A. Kamienica z szyldami** (rekomendacja) | Ta sama funkcja rysująca co banki: dwa biura na parterze, dwa na piętrze, brama „Prowadzę sam” (KPiR i VAT samodzielnie). | Jeden wzór „szyld = firma”, mało nowego kodu. | Podobna do bankowej: trzeba ją odróżnić (inny dach, kolor muru, napis na attyce). |
| B. A + spis lokatorów | Drewniany spis z ceną od… i ryzykiem błędu przy każdym biurze. | Wybór biura to porównanie dwóch liczb. | Zasłania część fasady. |
| C. Klatka schodowa | Przekrój klatki: drzwi biur na półpiętrach (bez makiety). | Inny kadr niż bank. | Więcej rysowania, gorsza czytelność szyldów. |

Rekomendacja: **A ze spisem z B.** „Księga firmy (KPiR)” przestaje być drzwiami w biurowcu: staje się bramą
„Prowadzę sam” tutaj oraz segregatorem na biurku w kebabie. Nazwa „Kamienica rachmistrzów” i adres są propozycją.

### Decyzja 5. Agencje reklamowe w osobnym biurowcu z windą
Makieta: `archiwum/krytyka-16.11/makiety/06-biurowiec-winda.html` (w wariancie A winda jeździ po kliknięciu guzika albo piętra).
Zrzuty: `archiwum/krytyka-16.11/zrzuty/makiety/06-A-jasny.png`, `06-A-wysoka-ciemny.png`, `06-B-pewex.png`, `06-C-ciemny.png`.

Piętra (propozycja, nazwy firm z danych gry): **P** portiernia = „Twoje kampanie” (co trwa, co wygasa),
**1** Drukarnia „Papier Przyjmie” (ulotki, plakaty, gazeta), **2** Radio „Fala Koziołka” (spot, billboard),
**3** „Kozi Gród Events” (degustacje, eventy), **4** „Lajk i Spółka” (internet, od tygodnia 7). Nazwa robocza budynku:
„Dom reklamy”.

| Wariant | Opis | Za | Przeciw |
|---|---|---|---|
| **A. Przekrój z windą** (rekomendacja) | Budynek w przekroju: szyb windy z lewej, na każdym piętrze pokój firmy z szyldem i rekwizytem, z prawej kaseta z guzikami i wyświetlaczem. Klik w guzik albo piętro: kabina jedzie, piętro się podświetla, „Wysiądź: …” otwiera okienko decyzji. | Wszystkie firmy widać naraz, zamknięte piętro też; winda jest zabawką, nie przeszkodą. | Pokoje są niskie (104 jednostki), więc rekwizyty muszą być proste. |
| B. Wnętrze kabiny | Boazeria, lustro, wyświetlacz, kaseta; po wyborze drzwi otwierają się na piętrze firmy. | Najwięcej klimatu. | Firm nie widać przed wyborem; dwa kliknięcia więcej na każdą wizytę. |
| C. Hol z tablicą | Tablica informacyjna z literkami, drzwi windy, portier. Wybór z tablicy. | Najtańszy, mocno PRL. | Winda jest tylko dekoracją, czyli nie spełnia „wybierasz piętro i idziesz”. |

Rekomendacja: **A.** Zamknięte piętro: guzik z przerywaną obwódką, kartka „od tygodnia 7”, zgaszone światło; klik nie
rusza windy, portier mówi, kiedy otworzą. Przy systemowym „ogranicz ruch” kabina przeskakuje bez animacji.
W Biurowcu przy Zana zostają ubezpieczenia: zamiast holu z drzwiami jedno biuro TUW „Pod Koziołkiem” z agentem
(szablon wnętrza firmy z makiet 04/05: tablica z polisami, okienko, szafa pancerna na polisy).

### Decyzja 6. Miasteczko akademickie
Makieta: `archiwum/krytyka-16.11/makiety/07-miasteczko-akademickie.html`. Zrzuty: `archiwum/krytyka-16.11/zrzuty/makiety/07-A-jasny.png`, `07-A-wysoka.png`,
`07-B-ciemny.png`.

| Wariant | Opis | Za | Przeciw |
|---|---|---|---|
| **A. Hol uczelni** (rekomendacja) | Tablica korkowa z kartkami (rynek pracy), stół z mapą stref i tablica z wykresem (Pracownia Analiz), kalendarz-zdzierak (wydarzenia), drzwi z matową szybą „Sokole Oko” (konkurencja). | Każda sprawa ma własny rekwizyt; stan widać na scenie (liczba kartek, kartka kalendarza); postacie w całości. | Trzeba narysować cztery nowe rekwizyty. |
| B. Dziedziniec kampusu | Akademik z tablicą, instytut, słup ogłoszeniowy, budka detektywa. | Tłumaczy, czemu detektyw jest „przy uczelni”; ładny kadr. | Widok z zewnątrz, czyli drugi po mapie; małe punkty. |
| C. Poprawione okienka (bez makiety) | Niższe lady, postacie w całości, rekwizyt sprawy zamiast tabliczki „Okienko 1”. | Najmniej pracy. | „Tablica ogłoszeń” dalej jest urzędnikiem; scena dalej jak Urzędy. |

Rekomendacja: **A.** Okienka zostają wyłącznie w Urzędach, gdzie pasują (z lamperią, numerkami i tablicą z literkami).

## (e) Pytania do szefa (z rekomendacją)

1. **Lista wujka: kartka w rogu (A), zeszyt (B) czy sam następny krok (C)?** Rekomendacja: A, zwijana do C.
2. **Okienko decyzji: teczka na środku (A) czy szuflada (B)?** Rekomendacja: A; dymki (C) później dla cen i promocji.
3. **Czy z kebaba dalej da się kupić sprzęt („Rożen”), czy tylko w Parku handlowym?** Rekomendacja: tylko w Parku;
   w kebabie stan sprzętu i odsyłacz. Uwaga: w tygodniu 1 gracz musi wtedy przejść przez mapę, więc lista wujka musi
   mieć ten krok.
4. **Co jest „u siebie” w kebabie, a co odsyła?** Rekomendacja: u siebie menu i ceny, promocje, zespół i grafik,
   wyniki, magazyn, czas i portfel właściciela; odsyła: sprzęt, stoliki i wystrój (Park handlowy), zatrudnianie
   (Miasteczko), szkolenia (Akademia), klienci w okolicy (Pracownia Analiz).
5. **Fasada banków: jedna kamienica (A) czy pierzeja (B)?** Rekomendacja: A + zwijany spis.
6. **Parkiet „Byk i Koziołek”: w podwórzu kamienicy bankowej czy osobny budynek?** Rekomendacja: podwórze.
7. **Nazwy nowych budynków:** „Kamienica rachmistrzów” i „Dom reklamy” pasują? Gdzie stoją na mapie (do ustalenia
   z majstrem)?
8. **Podział pięter w Domu reklamy** (drukarnia, radio, eventy, internet + portiernia z „Twoimi kampaniami”): zgoda?
   Czy budynek „drukarnia” na mapie znika, czy prowadzi do windy na 1. piętro?
9. **Księga firmy (KPiR):** brama „Prowadzę sam” u rachmistrzów + segregator w kebabie zamiast drzwi w biurowcu?
   Rekomendacja: tak.
10. **Miasteczko: hol (A) czy dziedziniec (B)? Detektyw zostaje w miasteczku czy dostaje własny budynek?**
    Rekomendacja: A, detektyw zostaje jako drzwi w kącie.
11. **Redakcja:** sama gazeta bez sceny z okienkami, czy scena redakcji z gazetą na biurku? Rekomendacja: scena
    redakcji jako tło, gazeta na pierwszym planie (jeden kadr zamiast dwóch pod sobą).
12. **Hurtownie:** jeden regał na dostawcę z prawdziwym szyldem (Makro, Selgros…), czy jedna anonimowa hala?
    Rekomendacja: regał na dostawcę, bo prawdziwe marki zostają (decyzja z 8.11).
13. **Kolory marek** (fiolet banku itd.) w okienkach: zastąpić znakiem i kolorami palety? Rekomendacja: tak.
14. **Pismo odręczne wujka** wymaga nowego kroju w `fonty/` (licencja OFL, polskie znaki). Zgoda na dodanie?
    W makiecie użyty krój systemowy zastępczo.
15. **Lista „Co tu zrobisz” pod sceną:** usunąć z widoku (zostaje dla czytników i telefonu)? Rekomendacja: tak.
16. **Telefon:** nadal odłożony? Jeśli tak, na wąskim ekranie zostaje lista zamiast sceny i nie projektujemy teraz
    dotyku.

## (f) Proponowany podział na zadania dla agentów Sonnet

Pliki rozłączne w obrębie fali. Ścieżki względem `panel_gracza/static/`. Plik `swiat/sceny.js` trzeba najpierw
rozbić (fala 0), bo inaczej wszyscy agenci scen pracowaliby w jednym pliku.

**Fala 0 (jeden agent, przed resztą)**
| Zadanie | Pliki | Zakres |
|---|---|---|
| S0. Rozbicie scen | `swiat/sceny.js` → `swiat/sceny/wspolne.js` (cegiełki: `u`, `napis`, `hot`, `osobaSvg`, lampa, paprotka, lamperia, lastryko), `sceny/kebab.js`, `sceny/hol.js`, `sceny/okienka.js`, `sceny/hala.js`; `sceny.js` tylko reeksportuje | Bez zmiany wyglądu; testy `testy/swiat/` bez zmian. |

**Fala 1 (równolegle, fundament)**
| Zadanie | Pliki | Zakres |
|---|---|---|
| F1. Okienko decyzji | `zakladki/wspolne.js` (tylko `okno`, `zamknijOkno`, `odswiezOkno`), nowy `motywy/okienko.css` | Teczka z makiety 02-A: okruszek, zakładki, stopka zapisu, `role="dialog"`, Esc, fokus, ✕ jako przycisk, kolory tylko ze zmiennych. |
| F2. Punkty sceny | `swiat/sceny/wspolne.js` (tylko `hot`), `swiat/swiat.css` (sekcja `.hot`, `.podpis`, `.stan`) | Etykieta stała, ramka po najechaniu/fokusie, wariant dla palety wysokiej (K1–K3, C5, C10). |
| F3. Wnętrze na cały ekran | `swiat/swiat.js` (`naglowek`, `miejsce.decyzje`, `lista`), `swiat/swiat.css` (sekcje `.sw`, `.sw-gora`, `.sw-lista`) | Belka + scena na całą szerokość; lista „Co tu zrobisz” tylko dla czytników. Zależy od decyzji 1. |
| F4. Mapa: rogi i lista wujka | nowy `swiat/hud.js`, nowy `motywy/hud.css`, `zakladki/wujek.js` (dodać id budynku do kroków) | Ikony w rogach, kartka wujka (makieta 01-A/C). Funkcję „pokaż budynek” robi majster w `mapa/lublin.js`; uzgodnić nazwę w WSPOLPRACA.md. |
| F5. Szybka poprawka hurtowni | `swiat/sceny/hala.js` | H1 (podpis na linii podłogi), H5. Można scalić od razu. |

**Fala 2 (po F1–F3; sklejenie)**
| Zadanie | Pliki | Zakres |
|---|---|---|
| G1. Punkt → okienko albo odsyłacz | `swiat/swiat.js` (akcja `sw-hot`, nowe `otworzOkienko`, `odeslij`), `swiat/miejsca.js` (pola `okienko`, `odsyla: {miejsce, tekst}`) | Klik otwiera ekran zakładki w okienku F1 zamiast `c.idz`; punkty z `odsyla` pokazują dymek z makiety 03-A. Jeden agent, bo to serce zmiany. |

**Fala 3 (równolegle, po jednej scenie na agenta; każdy dotyka tylko swojego pliku sceny)**
| Zadanie | Pliki | Zakres |
|---|---|---|
| W1. Kebab | `swiat/sceny/kebab.js`, `narzedzia/grafiki/` (nowe symbole) | K5–K8: chłodnia, biurko z szufladą, wujek z lewej, tablica menu. |
| W2. Fasada z szyldami | nowy `swiat/sceny/fasada.js` | Wspólna funkcja dla banków i rachmistrzów (makiety 04-A, 05-A) + zwijany spis. |
| W3. Wnętrze firmy | nowy `swiat/sceny/firma.js` | Szablon: tablica z ofertą, okienka, rekwizyt (bank, biuro, TUW). Makiety 04-W, 05-W. |
| W4. Dom reklamy z windą | nowy `swiat/sceny/winda.js` | Makieta 06-A, animacja kabiny, zamknięte piętro. |
| W5. Miasteczko akademickie | nowy `swiat/sceny/uczelnia.js` | Makieta 07-A. |
| W6. Urzędy w stylu PRL | `swiat/sceny/okienka.js` | U1, U2, U4: niższe lady, lamperia, numerki, tablica z literkami. |
| W7. Park handlowy: witryny | nowy `swiat/sceny/pasaz.js` | P1, P4. |
| W8. Stare Miasto: sień | `swiat/sceny/hol.js` (styl `brama`) | S1–S3. |
| W9. Redakcja | `swiat/kurier.js`, nowy `swiat/sceny/redakcja.js` | R1–R3. |
| W10. Hurtownie | `swiat/sceny/hala.js` (po F5) | H2–H4: rampa, kasa, regał na dostawcę. |
| W11. Bazar, poczta, akademia | nowe `swiat/sceny/bazar.js`, `poczta.js`, `akademia.js` | Brakujące wnętrza z tabeli w decyzji 2. |

**Fala 4 (jeden agent, na końcu)**
| Zadanie | Pliki | Zakres |
|---|---|---|
| Z1. Podpięcie miejsc | `swiat/miejsca.js`, `swiat/swiat.js` (`scenaMiejsca`), `dane/mapa/budynki.yaml`, `dane/funkcje.yaml` | Nowe miejsca (rachmistrze, dom reklamy, pojedyncze banki), przeniesienie punktów, nowe budynki mapy (z majstrem). |
| Z2. Kolory i zrzuty | `styl.css`, `zakladki/ikony_marek.js` | C15: kolory na sztywno w treści okienek; przegląd 3 palet × 2 tryby. |

Kolejność minimalna, gdyby szef chciał szybki efekt: F5 → F2 → F1 → G1 → W2+W3 (banki) → W5 (miasteczko).

## Ograniczenia tej recenzji
- Oglądano grę pokazową w tygodniu 6 w oknie 1400×900 oraz kebab i kamienicę przy 400 px. Nie sprawdzano stanów
  „lokal w budowie”, „bez lokalu”, wielu lokali ani kasyna (funkcja niewidoczna w tej grze).
- Widoczności fokusu klawiatury nie udało się potwierdzić na zrzucie (`bar-jasny-kebab-fokus.png` nie pokazuje
  obwódki, bo fokus ustawiony skryptem nie włącza `:focus-visible`). Do sprawdzenia ręcznie klawiszem Tab.
- Makiety to rysunki poglądowe z prostych kształtów. Nazwy „Kamienica rachmistrzów”, „Dom reklamy”, hasła na szyldach
  biur i adresy są propozycjami recenzenta, a liczby są przykładowe.
