# Symulowany pozew REVAS przeciw LUKRUM (przegląd ryzyka, 14.11.2026)

To ćwiczenie, a nie porada prawna. Najpierw piszę jak pełnomocnik powoda i biegły informatyk, potem zmieniam stronę.
Niczego nie zmieniałem w repozytoriach. Z `revas_26` są tu tylko krótkie cytaty dowodowe.

**Co porównałem**
- `main` = `lukrum/lukrum_gra/gra` (4 commity, 13.11).
- `PR #2` = `lukrum/_robocze/mechaniki-a/gra` (tor A, czeka na scalenie).
- `wnętrza` = `lukrum/_robocze/wnetrza-dane/gra/dane/wnetrza`.
- `remake` = `_archiwum/revas_26/revas_gra` (odtworzenie REVAS przez autora).
- `oryginał` = `_archiwum/revas_26/materialy` (strony, podręczniki i dane zgrane z prawdziwej gry REVAS).

**Najważniejsze ustalenia**
1. Nazwa „Revas” zniknęła z obu wersji LUKRUM (grep: 0 trafień). Liczby zostały: w `main` prawie wszystkie, w PR #2 mniej więcej połowa.
2. Z kodem i tekstami oryginalnej gry REVAS LUKRUM nie ma nic wspólnego: 0 wspólnych linii z jej JS/CSS, 0 wspólnych ścieżek ikon SVG, jedno wspólne zdanie z podręcznika.
3. Najgroźniejszy nie jest sam LUKRUM, tylko to, skąd wzięły się liczby: folder `revas_26/materialy` zawiera ok. 9 100 stron HTML, 961 arkuszy i podręczniki 20 symulacji, zgrane skryptami z konta instruktora.
4. Opisy źródeł w danych przerobiono tak, że liczby zostały, a nazwa źródła znikła. W sporze wygląda to na zacieranie śladów i jest gorsze niż jawne „wzorowane na”.
5. Osobny, niezależny od REVAS kłopot: uproszczone logotypy prawdziwych firm są dalej w grze, wbrew planowi.

Każdy zarzut ma oznaczenie, czego dotyczy: **[main]**, **[PR #2]**, **[plan]**, **[poza grą]**.

---

## Część 1. „Pozew”

### Z1. Przejęcie zestawów danych gry (katalogi) — [main] mocno, [PR #2] częściowo

**Podstawa.** Art. 1 i art. 3 pr. aut. (zbiór o twórczym doborze i układzie; wartości wymyślone przez twórcę gry to nie „fakty”), ustawa o ochronie baz danych z 27.07.2001 (art. 6 i 8 – pobranie istotnej części), art. 3 ust. 1 u.z.n.k. (pasożytnicze korzystanie z cudzego nakładu).

**Dowody.**

| LUKRUM | Odpowiednik w remake'u | Co jest wspólne |
|---|---|---|
| [main] i [PR #2] `dane/katalog.yaml:104–148` | `dane/katalog.json` → `udogodnienia.pozycje` | 9 z 9 pozycji z tymi samymi liczbami i rundami, 8 z tymi samymi nazwami. Np. „Automat z kawą fair trade” 95 / 2500 / 200 i „Kuchenka mikrofalowa” z ceną 202 i utrzymaniem 5 |
| [PR #2] `dane/katalog.yaml:231–262`, [main] `:216–` | `katalog.json` → `wyposazenie.pozycje` | 6 z 6 pozycji z tymi samymi liczbami (95/200/20, 90/0/1500, 80/0/100, 75/2000/200, 60/2500/0, 30/2300/10) i rundami 4/4/4/5/5/5; trzy nazwy dosłowne („Darmowe WiFi”…) |
| [main] i [PR #2] `dane/katalog.yaml:309–313` | `katalog.json` → `szkolenia.firmy` | trzy firmy szkoleniowe z ocenami 90 / 83 / 80 |
| [main] `dane/katalog.yaml:83–88` | `katalog.json` → `stanowiska.pakiety` | 1000 / 1800 / 2200 / 3000 / 4000 |
| [main] `dane/katalog.yaml:250–347` | `katalog.json` → `media_tradycyjne` | 12 mediów: te same zasięgi, ceny (TV 30 000 / 25 000 / 20 000) i progi zniżek, nazwy zmienione |
| [main] `dane/katalog.yaml:374–413` | `katalog.json` → `narzedzia_internetowe` | 9 narzędzi z tymi samymi kosztami (np. 3500 / 250) |
| [main] `dane/katalog.yaml:416–459` | `katalog.json` → `banki` | 6 banków z tymi samymi stawkami (kredyt odnawialny 0,07 / 0,06 / 0,05 / 0,12 / 0,12 / 0,10), nazwy zmienione |
| [main] `dane/katalog.yaml:464–489` | `katalog.json` → `biura_rachunkowe` | 6 biur: 1,2 / 1,2 / 1,1 / 1,3 / 1,0 / 1,5 za dokument |
| [main] `dane/kandydaci.yaml:124–165` | `dane/kandydaci.json` | widełki pensji 4785–4950 / …–5170 / 5280–…, odprawa jako część pensji, krok 5 |

W PR #2 pakiety stanowisk, banki, biura, media i kandydaci są już własne (np. `katalog.yaml:83` „własny cennik LUKRUM”). Zostały: udogodnienia, pierwsze 6 pozycji wyposażenia i oceny firm szkoleniowych.

**Siła.** [main]: **mocny** co do faktów (kilka pełnych tabel, nietypowe wartości jak 202 zł wykluczają przypadek), **średni** co do prawa (ochrona zbioru wymaga twórczego doboru; przy bazach sui generis nakład na *wymyślenie* danych się nie liczy – wyrok TSUE C-203/02 BHB). [PR #2]: **średni**, bo zostały trzy tabele.

**Żądania.** Zaniechanie i usunięcie danych z gry, odszkodowanie w wysokości dwukrotności stosownego wynagrodzenia (art. 79 pr. aut.), wydanie korzyści, publikacja oświadczenia.

### Z2. Sposób pozyskania danych: masowe zgranie gry z konta instruktora — [poza grą], ale obciąża całość

**Podstawa.** Odpowiedzialność umowna za naruszenie regulaminu lub licencji platformy (art. 471 k.c.; TSUE C-30/14 Ryanair – umowa może zakazać pobierania nawet z bazy niechronionej), art. 8 ust. 2 ustawy o ochronie baz danych (powtarzające się, systematyczne pobieranie), art. 11 u.z.n.k. (tajemnica przedsiębiorstwa: ukryte parametry modelu), ewentualnie RODO (dane innych drużyn i szkół). Jeżeli konto nie należało do autora albo użyto go poza zakresem zgody, pełnomocnik powoda dopisałby art. 267 k.k.

**Dowody.**
- `_archiwum/revas_26/materialy/revas_online/README.md:1–3`: „dane zgrane z REVAS online (konto instruktora)… skryptami”.
- `_archiwum/revas_26/narzedzia/revas_online/` – 9 skryptów (`gra_instruktor.py`, `stare_gry.py`, `zestawienie.py`…).
- Zawartość `materialy/`: ok. 9 100 plików HTML, 961 xlsx, 287 csv, 114 pdf; podręcznik „Klub fitness” i podręczniki 19 innych symulacji; 9 archiwalnych gier „Biuro podróży” z lat 2018–2020 (cudze drużyny); panel instruktora z danymi wszystkich firm.
- `revas_gra/kalibracja/*.py` i `dane_zrodlowe/*.json` – dopasowanie wzorów do tych danych.

**Siła.** **Mocny** co do faktów. Co do prawa zależy od regulaminu platformy, którego nie udało mi się znaleźć (zob. część 4). To zarzut, który w procesie robi największe wrażenie, bo pokazuje zamiar i skalę.

**Żądania.** Zaniechanie korzystania z danych, ich zwrot lub zniszczenie, odszkodowanie, zakaz wykorzystania wyników kalibracji.

### Z3. Ukryty model gry odtworzony ze stałymi „co do czwartego miejsca” — [main] cały, [PR #2] część popytu

**Podstawa.** Art. 11 i art. 3 u.z.n.k. Prawo autorskie tylko pomocniczo: wzór i zasada gry nie są chronione (art. 1 ust. 2¹ pr. aut.; TSUE C-406/10 SAS Institute – funkcjonalność programu nie jest chroniona).

**Dowody.**

| LUKRUM | Remake | Stałe |
|---|---|---|
| [main] i [PR #2] `dane/zalozenia.yaml:8, 14, 20, 26` | `zalozenia.json:5–8` | 1,096 / 1,0035 / 0,247 / 1,498 |
| [main] i [PR #2] `zalozenia.yaml:35, 47–48, 54` | `zalozenia.json:9–11` | 0,654; wagi 0 / 0,407 / 0,593; 0,073 |
| [main] i [PR #2] `zalozenia.yaml:82–91` | `zalozenia.json:14` | 10 korekt miesięcy (0,972 … 0,796) |
| [main] `zalozenia.yaml:114, 119–122, 127, 132, 146` | `zalozenia.json:21–27` | reklama: 2,2166; 0,011492…0,053354; 0,1898; 2,7561; 0,3971 |
| [main] `zalozenia.yaml:293–298, 309–314, 329–334` | `zalozenia.json:58–60` | karta wyników: 0,8486 / 0,1768 / 0,193 / 0,105 / 0,2282; 0,9464 / 0,3162 / 0,0163 / 0,0115; 0,5353 / 0,1062 / 0,3389 / 1,192 / 0,031 |

Mój skrypt znalazł w `main` 45 wspólnych stałych o co najmniej trzech miejscach po przecinku, w PR #2 – 22. W PR #2 karta wyników i stara reklama są już usunięte (wynik 0–1000 pkt, model „agencja × kanał”).

Dodatkowy dowód złej wiary: w PR #2 `zalozenia.yaml:10–12` źródło brzmi „panel 361 obserwacji (3 firmy z botami, 11 miesięcy)… błąd 5,4%, walidacja 6,3%”, a w remake'u `zalozenia.json:5` – „panel 361 obserwacji – gra ATH luty–grudzień (3 firmy z botami)… błąd 5,4%, walidacja 6,3%”. Opis przerobiono tak, że udaje własne pomiary.

W PR #2 część tych stałych jest martwa: kod czyta tylko `wagi_jakosci`, `wspolczynniki_jakosci`, `wyposazenie_na_procent_klientow` (`silnik/kuchnia/jakosc.py:21, 32`) i `elastycznosc_ceny` z modelu strefowego (`silnik/rynek/popyt.py:158`). Reszta leży w pliku jako dowód bez funkcji.

**Siła.** **Średni.** Stałe to własne oszacowania autora z obserwacji gry, a nie parametry wykradzione z kodu REVAS – to osłabia zarzut tajemnicy. Wzmacnia go Z2 (pozyskanie mogło naruszać umowę, a wtedy wyjątek z art. 11 ust. 3 u.z.n.k. nie działa) i przerobione opisy źródeł.

**Żądania.** Zakaz używania modelu, usunięcie stałych, odszkodowanie.

### Z4. Uproszczone logotypy i nazwy prawdziwych firm — [main], [PR #2], [plan]; powodem nie jest REVAS

**Podstawa.** Art. 296 ust. 2 pkt 3 p.w.p. i art. 9 ust. 2 lit. c rozp. 2017/1001 (znaki renomowane – nie wymaga ryzyka pomyłki), art. 1 pr. aut. (logo jako utwór, przeróbka = opracowanie), art. 43 w zw. z art. 23–24 k.c. (dobre imię osoby prawnej, gdy gra przypisuje firmie wymyślone ceny i zdarzenia).

**Dowody.**
- [main] `panel_gracza/static/zakladki/ikony_marek.js:106–149`: słownik `LOGA` – Biedronka (biedronka w barwach sieci), Lidl, Stokrotka, Auchan, Makro, Selgros, Eurocash, IKEA, OBI, Castorama, Jula, Leroy Merlin oraz banki PKO BP, Pekao, ING, mBank, Santander, Crédit Agricole.
- [PR #2] `ikony_marek.js:105–135`: `LOGA` dalej zawiera 12 sieci handlowych (banki usunięte).
- [PR #2] `panel_gracza/static/zakladki/mapa_budynki.js:339–340`: szyldy na mapie „PKO BP”, „PEKAO”, „ING”, „mBank”, „SANTANDER” w barwach firmowych, choć banki w danych mają już nazwy z lektur.
- [main] `dane/mapa/banki.yaml:22–85`: prawdziwe banki z wymyślonymi ofertami, np. przy Crédit Agricole „za to wyższe oprocentowanie”.
- Dane: Auchan i Biedronka jako dostawcy z cenami (`dane/dostawcy.yaml:12, 34, 121`), IKEA i Leroy Merlin jako sklepy (`dane/katalog.yaml:236–299`), pracuj.pl (`dane/kandydaci.yaml:152`), TikTok i Mapy Google (`dane/mapa/reklama.yaml:198–228`), BLIK, ZAiKS/STOART, Motor Lublin z terminarzem meczów (`dane/kalendarz/kalendarz.yaml:246–458`), UMCS i KUL na szyldach.
- Sprzeczność w dokumentach: plan (`PLAN_PRZEBUDOWY.md`, rozdz. 7) mówi „bez prawdziwych logo”, a notatka `Funkcje/Logo i zastrzeżenie marek.md` opisuje „uproszczone znaki marek” jako gotową funkcję.

**Siła.** **Średni**, a po publikacji realny: właściciele tych znaków mają działy prawne i wysyłają wezwania rutynowo. Samo użycie nazwy w tekście jest słabym zarzutem. Rysunek nawiązujący do logo w barwach firmy jest zarzutem dużo mocniejszym. Zastrzeżenie w stopce nie znosi naruszenia.

**Żądania.** Usunięcie znaków, oświadczenie, przy znakach renomowanych odszkodowanie.

### Z5. Układ gry: harmonogram odblokowań, nazwy ekranów, klucze — [main], [PR #2]

**Podstawa.** Art. 13 u.z.n.k. (naśladownictwo gotowego produktu), art. 3 u.z.n.k., pomocniczo art. 1 pr. aut. (struktura i kolejność jako element twórczy).

**Dowody.**
- `dane/katalog.yaml:14–34` w obu wersjach ↔ `katalog.json` → `rundy.odblokowanie`: ta sama kolejność i te same klucze (`finanse_bank`, `finanse_biuro`, `inwestycje_sprzet`, `hr_udogodnienia`, `karta_skumulowana`…), runda po rundzie od 1 do 7. Jedyna różnica: `hr_zatrudnienie` w rundzie 1 zamiast 2.
- `dane/katalog.yaml:61–68`: 3 pozycje oferty w rundzie 1, potem +3 na rundę od rundy 3 – jak w remake'u.
- `panel_gracza/static/zakladki/index.js:105, 125, 126`: „karta wyników”, „Lista błędów”, „Wyślij decyzje”; w `INSTRUKCJA.md` 21 wystąpień tych nazw i „Dashboard”; rozdz. 3 „Cel gry – karta wyników”, rozdz. 14 „Kiedy co się odblokowuje”.
- Zestaw plików zakładek `oferta.js, inwestycje.js, hr.js, dostawcy.js, marketing.js, sprzedaz.js, finanse.js, ogolne.js, wspolne.js` jak w remake'u.

**Siła.** **Słaby do średniego.** Pojedyncze nazwy są ogólne. Identyczny siedmiostopniowy harmonogram z tymi samymi kluczami jest najtrudniejszy do wytłumaczenia przypadkiem. Obecny panel ma i tak zniknąć (mapa zamiast zakładek).

### Z6. Kod: LUKRUM jako opracowanie remake'u — [main], [PR #2]

**Podstawa.** Art. 2 i art. 74 pr. aut. (opracowanie cudzego programu).

**Dowody.** 1 445 z 4 286 znaczących linii remake'u występuje dosłownie w PR #2. Najwięcej: `silnik/gra.py` 87%, `silnik/kuchnia/operacje.py` 62%, `silnik/decyzje.py` 54%, `panel_gracza/static/styl.css` 85%, `motywy/grafik.css` 94%, `zakladki/ikony.js` 94%, `zakladki/finanse.js` 66%.

**Siła.** **Słaby** – i to dobra wiadomość. Remake napisał autor LUKRUM, więc kopiuje sam siebie. Z frontem oryginału (basic.js, main.js, menu.js, suppliers.js, basic.css, style.css – 599 linii) LUKRUM nie ma ani jednej wspólnej linii, a z 41 ścieżkami ikon SVG oryginału żadnej wspólnej. Zarzut ożyłby tylko, gdyby remake zawierał przepisany kod REVAS, czego nie widać. Kodu serwera REVAS nikt z nas nie widział.

### Z7. Teksty — [main], [PR #2]

**Podstawa.** Art. 1 pr. aut.

**Dowody.** Wspólne ciągi 6 słów między LUKRUM a 25 podręcznikami REVAS: jeden. `panel_gracza/static/zakladki/ogolne.js:398` „Wróć do podejmowania decyzji w bieżącej rundzie” ↔ `materialy/revas_online/instrukcje/klub_fitness/25_klub_fitness.txt`. Do tego nazwy pozycji z Z1.

**Siła.** **Słaby.** Instrukcja LUKRUM jest napisana samodzielnie.

### Z8. Znak i renoma „REVAS” — [poza grą]

**Podstawa.** Art. 296 p.w.p., art. 10 u.z.n.k.

**Dowody.** W LUKRUM brak. Ryzyko jest w otoczeniu: repozytorium Levas (`github.com/…/Levas`, 427 commitów, 50 plików ze słowem „revas”) i strona Levasa, jeśli są lub były publiczne; materiały promocyjne lub zgłoszenia konkursowe, które opisywałyby grę jako „jak REVAS” albo „lepszy REVAS”.

**Siła.** **Słaby**, o ile nazwa nie pojawi się w promocji. Nie potwierdziłem rejestracji znaku (część 4).

### Z9. Postacie i cytaty z lektur — [PR #2], [wnętrza], [plan]; powodami byliby spadkobiercy

**Podstawa.** Art. 1, 16, 29 i 34 pr. aut.; znaki towarowe związane z utworami.

**Stan praw (autor, rok śmierci, ochrona majątkowa do końca roku):**

| Bezpieczne (domena publiczna) | Chronione |
|---|---|
| Prus 1912, Sienkiewicz 1916, Zapolska 1921, Żeromski 1925, Reymont 1925, Fredro 1876, Mickiewicz 1855, Potocki 1815, Molier, Dickens 1870, Kafka 1924, May 1912, Saint-Exupéry 1944 (w Polsce wolny od 2015; polskie przekłady chronione) | Gombrowicz 1969 → 2039, Lem 2006 → 2076, Zbigniew Herbert 1998 → 2068, Frank Herbert 1986 → 2056, Singer 1991 → 2061, Zajdel 1985 → 2055 |

**Dowody.**
- [wnętrza] `dymki.yaml:128, 134, 140, 146`: cytaty z Zapolskiej, Sienkiewicza i Fredry – bezpieczne, jeśli zgodne z wydaniem z domeny publicznej.
- [wnętrza] `bywalcy.yaml:66–69`, `dymki.yaml:75`: Józio i „przyprawić gębę” (Gombrowicz).
- [PR #2] `dane/mapa/banki.yaml:92–95` bank „Solaris” z opisem nawiązania do Lema; `dane/mapa/reklama.yaml:73–85` „Gazeta Pana Cogito” z pastiszem („Rożen jako imperatyw moralny”); `reklama.yaml:110` „Radio Tichy”; `dane/mapa/biura.yaml:66–67` „Asteroida 328”.
- [plan] `PLAN_PRZEBUDOWY.md`, rozdz. 8: „Kto kontroluje przyprawę, kontroluje rynek” (Diuna), sepulki, „Konstruktorzy T&K”, inspektor Pimko, „upupianie” kucharza.

**Siła.** **Słaby.** Imię postaci, tytuł i pojedyncze słowo zwykle nie są utworem. Ryzyko rośnie, gdy postać chronionego autora dostaje własne kwestie i rysunek (to już nowy utwór z cudzą postacią) albo gdy nawiązań z jednego autora jest dużo. Spadkobiercy Lema i Gombrowicza aktywnie zarządzają prawami.

### Z10. Regulamin konkursu — [plan]

Regulamin konkursu REVAS dla szkół (MBIZ 2025), który udało się odczytać, nie zawiera postanowień o prawach do platformy, zakazie kopiowania ani o skryptach. Zarzut z regulaminu konkursu jest więc **słaby**. Groźniejsze są oświadczenia, które autor sam złoży: w „Zwolnionych z Teorii”, w urzędzie miasta i kuratorium zwykle podpisuje się, że projekt jest oryginalny i nie narusza praw osób trzecich. Przy stanie z `main` takie oświadczenie byłoby ryzykowne.

---

## Część 2. Obrona i naprawa

| Zarzut | Najmocniejszy kontrargument | Konkretna zmiana | Priorytet |
|---|---|---|---|
| **Z1** katalogi | Pojedyncze ceny i procenty to parametry gry, nie utwór. Dane „wymyślone” nie dają ochrony sui generis (C-203/02). Autor nie jest przedsiębiorcą, więc u.z.n.k. stosuje się wątpliwie | **Scalić PR #2**, a przed scaleniem dokończyć: `dane/katalog.yaml:104–148` – wymienić 9 starych udogodnień na własne (albo zostawić tylko pozycje UF9 z własnymi opisami); `:231–262` – nowe liczby i nazwy dla pierwszych 6 pozycji wyposażenia; `:309–313` – oceny firm szkoleniowych inne niż 90/83/80. Te same zmiany w `testy/dane_zamrozone/`. Każdą nową liczbę uzasadnić w polu `zrodlo` prawdziwym źródłem (cennik, pomiar botów z datą i plikiem) | **1 – przed pokazaniem komukolwiek** |
| **Z2** zgranie danych | Art. 75 ust. 2 pkt 2 pr. aut. i C-406/10: legalny użytkownik może obserwować i badać działanie programu, a umowa nie może tego wyłączyć. Dane nie zostały rozpowszechnione | Nie przenosić niczego z `revas_26` do LUKRUM (już obowiązuje). Nie publikować i nie udostępniać `revas_26` nikomu, także koledze od mapy. Ustalić, czyje było konto instruktora i na jakich warunkach. O tym, co zrobić z samym folderem (zachować, zwrócić, usunąć dane osobowe), powinien zdecydować prawnik – nie kasować na własną rękę po tym przeglądzie | **1** |
| **Z3** stałe modelu | To własne oszacowania statystyczne z obserwacji, obarczone błędem 5–6%, a nie parametry REVAS. Wzór nie jest chroniony | W `dane/zalozenia.yaml` usunąć martwe pola: `elastycznosc_wzgledem_rynku`, `wykladnik_liczby_firm`, `mnoznik_bazowy`, `korekta_miesiaca`, `recepcja_1gw_mnoznik`, `utrata_klientow`, `postac_ceny` (najpierw grep w `silnik/`, `balans/`, `schematy.py`). Używane `wagi_jakosci` (0,407 / 0,593), `wspolczynniki_jakosci` „2”: 0,654 i `wyposazenie_na_procent_klientow` 0,073 wyznaczyć od nowa pomiarem botów LUKRUM i zapisać wynik pomiaru. Pola `zrodlo` z „panelem 361 obserwacji” usunąć razem z liczbami – nie przerabiać opisu przy zostawionej liczbie | **1** |
| **Z4** marki | Użycie nazwy w celu opisowym, niekomercyjnie, w edukacji; brak działania „w obrocie” (art. 296 p.w.p.); rysunki własne | Usunąć cały słownik `LOGA` z `ikony_marek.js` i dać ogólne ikony branżowe (`KOSZYK`, `WOZEK`, `PALETA` już są w pliku). Usunąć szyldy banków z `mapa_budynki.js:339–340`. Najbezpieczniej zastąpić sieci handlowe i sklepy nazwami fikcyjnymi („dyskont”, „hurtownia przy Mełgiewskiej”, „market budowlany na Węglinie”); jeśli nazwy zostają – tylko czcionką gry, bez barw firmowych, bez cen przypisanych jako „oferta firmy X” i bez negatywnych zdarzeń. Poprawić notatkę `Funkcje/Logo i zastrzeżenie marek.md`, żeby zgadzała się z planem. Dopasować `testy/aplikacja/test_ikony_marek.py` | **1** (logotypy), **2** (nazwy) |
| **Z5** układ | Kolejność „najpierw oferta i bank, potem sprzedaż, potem marketing” wynika z dydaktyki; nazwy są opisowe; panel jest tymczasowy | Tor B z planu (listy wujka zamiast harmonogramu) usuwa zarzut – do tego czasu w `dane/katalog.yaml:14–34` zmienić klucze na własne i przestawić kolejność, a `:61–68` zamienić na limit dań wynikający ze sprzętu. Zmienić etykiety w `zakladki/index.js:105, 125, 126`, `ogolne.js`, `app.js` i w `INSTRUKCJA.md` (np. „Wynik tygodnia”, „Sprawdź plan”, „Zamknij tydzień”, „Pulpit”). `ogolne.js:398` – inne zdanie na przycisku | **2** |
| **Z6** kod | Autor kopiował własny kod; brak dostępu do kodu REVAS; zero wspólnych linii z frontem oryginału | Nic nie trzeba zmieniać. Zachować dowody autorstwa remake'u (część 3) | **3** |
| **Z7** teksty | Jedno zdanie użytkowe | Zmiana przycisku jak w Z5 | **3** |
| **Z8** znak REVAS | Brak użycia w LUKRUM | Nie używać nazwy w promocji, zgłoszeniach i README. Sprawdzić, czy repozytorium i strona Levasa są niepubliczne | **2** |
| **Z9** lektury | Imiona, tytuły i pojedyncze słowa nie są utworami; krótki cytat z podaniem autora mieści się w art. 29 | Autorów chronionych zostawić jako aluzję jednowyrazową albo zamienić: „Solaris” → nazwa z domeny publicznej, „Gazeta Pana Cogito” i „Radio Tichy” → np. tytuły z Prusa lub Kraszewskiego, hasło z Diuny usunąć, Józio bez własnych kwestii „z Gombrowicza”. Cytaty z domeny publicznej sprawdzić z Wolnymi Lekturami (lista w `Do decyzji.md`) | **2** |
| **Z10** oświadczenia | – | Nie składać oświadczeń o oryginalności, dopóki priorytet 1 nie jest zamknięty w `main` | **1** |

Uwaga do `main`: gałąź główna jest dziś w najgorszym stanie (45 stałych, pełne katalogi, logotypy banków). Jeśli ktokolwiek ma zobaczyć grę przed scaleniem PR #2, pokazywać tylko wersję z PR #2 po poprawkach z tabeli.

---

## Część 3. Ryzyka w planie

Oceniam planowane rzeczy tak, jakby były już w grze.

| Planowana rzecz (źródło) | Ryzyko | Jak je ominąć już w projekcie |
|---|---|---|
| „Zero śladów Revasa… w kodzie i historii gita”, nowe repo bez historii (`PLAN_PRZEBUDOWY.md`, rozdz. 1–2, 5) | **Zaostrza Z1–Z3.** Usuwanie nazw przy zostawionych liczbach i odcięcie historii w sporze wygląda na ukrywanie pochodzenia. Sam plan jest dokumentem, który to opisuje | Zmienić cel z „zero śladów” na „zero zapożyczonej treści”. Każdą liczbę zastąpić własną i mieć dla niej zapis, skąd jest. Historię Levasa zachować prywatnie |
| Paleta o nazwie „Pewex” (`Wygląd.md`, decyzje 14.11; `_robocze/wyglad/podglad3.html`) | „Pewex” jest dziś używaną marką handlową i najpewniej zarejestrowanym znakiem | Nazwać paletę opisowo: „Dewizowa”, „Bursztyn”, „Neon”. „Bar mleczny” jest nazwą rodzajową i może zostać |
| Dekorowanie lokalu w „sklepie meblowym” z wejściem do środka | Jeśli sklepem będzie IKEA (dziś `katalog.yaml:226`: „IKEA (meble)”), dochodzi przedstawienie wnętrza i barw sieci – to więcej niż wzmianka o nazwie | Sklep fikcyjny z własnym wyglądem. Nazwy mebli własne, bez stylizacji na szwedzkie |
| „Nie podpisujemy, z jakiej lektury są postacie” | Przy autorach chronionych brak podania autora i źródła odbiera obronę z prawa cytatu (art. 34 pr. aut.) i narusza prawo do autorstwa | W scenie można nie podpisywać, ale gra musi mieć ekran „Nawiązania i źródła” (autor, tytuł, wydanie). Dla zadania „znajdź 10 nawiązań” wystarczy odsłaniać go po grze |
| Bywalcy rysowani jako postacie (`bywalcy.yaml`, pole `wyglad`; „grafiki może zrobić Fable”) | Rysunek podobny do aktora z ekranizacji (Rzecki, Zagłoba, Papkin) narusza wizerunek i prawa do filmu. Grafika z generatora może nie mieć ochrony i może przypominać cudzą | W briefie dla rysownika: wygląd tylko z opisu w książce i z pola `wyglad`, bez kadrów z filmów. Zapisać, kto i czym wykonał każdą grafikę |
| Józio, Pimko, „gęba”, „upupianie” (rozdz. 8 i 11, tor B) | Gombrowicz chroniony do końca 2039. Kilka nawiązań naraz plus własne kwestie postaci to już korzystanie z postaci, nie aluzja | Najwyżej jedno słowo-aluzja w całej grze albo postać z domeny publicznej w tej roli (np. profesor z „Syzyfowych prac”) |
| Lem: Solaris, sepulki, Trurl i Klapaucjusz, Tichy; Herbert: Pan Cogito; Diuna; Zajdel; Singer | Autorzy chronieni; im więcej nawiązań do jednego autora, tym łatwiej o zarzut. „Dune” i „Solaris” są też znakami towarowymi innych podmiotów | Limit: jeden autor chroniony = jedna aluzja bez cytatu i bez pastiszu. Nazw firm w grze z nich nie tworzyć |
| Inspiracja „Good Pizza, Great Pizza” (`Wygląd.md`) | Sam pomysł klienta z dymkiem przy ladzie jest wolny. Ryzyko pojawi się przy podobnym kadrze, stylu postaci i układzie dymków | Nie pokazywać rysownikom zrzutów tej gry. Nie wymieniać jej w promocji. Własny kadr: właściciel z boku (już zaplanowane) |
| Mapa z OpenStreetMap (etap 2) | Licencja ODbL: brak podpisu albo nieudostępnienie przetworzonej bazy przy publikacji | Podpis „© autorzy OpenStreetMap” na mapie i w README (jest w planie). Zdecydować, czy `dzielnice.yaml` będzie publikowany na ODbL |
| Prawdziwe adresy urzędów, sanepid z „inspektorem Pimko”, prawdziwe uczelnie na szyldach | Negatywne zdarzenia przypisane prawdziwej instytucji; nazwiska prawdziwych osób | Instytucje publiczne mogą zostać z nazwy rodzajowej („Sanepid”, „Urząd skarbowy”). Żadnych prawdziwych nazwisk. UMCS i KUL – bez herbów i barw, najlepiej „uniwersytet” |
| Opinie gości w gwiazdkach widoczne na mapie, „wizytówka w Mapach Google”, TikTok (tor B, `reklama.yaml:198–228`) | Wygląd wzorowany na konkretnym serwisie | Własny wygląd opinii, kanały nazwane rodzajowo („filmiki w sieci”, „wizytówka na mapie”) |
| Fonty Oswald, PT Sans, Alfa Slab One, Rubik Mono One z Google Fonts | Licencja OFL pozwala na użycie. Ładowanie z serwerów Google w szkole przekazuje adresy IP uczniów (RODO) | Pliki fontów trzymać w repo razem z plikiem licencji |
| Dźwięki (dzwonek, skwierczenie, gwar) | Efekty z internetu bez licencji | Tylko źródła z licencją CC0 albo własne nagrania; lista w repo |
| Kasyno ukryte przed mistrzem gry (`Funkcje/Kasyno…`) | Nie dotyczy REVAS. Gra dla niepełnoletnich z hazardem ukrytym przed nauczycielem może zamknąć drogę przez kuratorium i urząd miasta | Domyślnie wyłączone, nauczyciel włącza świadomie i widzi w przeglądzie |
| Nowe katalogi, wynik 0–1000 pkt, debet, kadry wg KP, pomyłki w szczycie, fabuła z wujkiem, popyt z mapy (rozdz. 11) | **Zmniejszają ryzyko.** To własne mechaniki | Robić dalej. Przy każdej zapisać źródło liczb w notatce funkcji |
| Decyzja „nazwy w kodzie (usluga, zasob, prowadzacy) zostają” | Słaby ślad pochodzenia z klubu fitness, widoczny tylko w kodzie | Może zostać, dopóki repo jest prywatne. Przed upublicznieniem zmienić |

---

## Część 4. Jak pomóc sobie w razie sporu

1. **Zachować historię.** Repozytorium Levas (427 commitów) i remake pokazują, że kod pisał autor. Nie kasować, nie przepisywać historii, trzymać prywatnie.
2. **Dziennik pochodzenia liczb.** Dla każdej tabeli i stałej: data, skąd wartość (cennik z adresem i datą, przepis, pomiar botów z nazwą pliku w `balans/`), kto zdecydował. Notatki w `Funkcje/` już to częściowo robią – dopisać pole „Źródło liczb”.
3. **Pomiary balansu od zera.** Zachować surowe wyniki botów LUKRUM, na których oparto nowe wartości, żeby dało się pokazać, że model powstał z własnych danych.
4. **Stan przed i po.** Zapisać wynik skryptu porównującego stałe (dziś 45 w `main`, 22 w PR #2) przy każdym etapie – do zera.
5. **Grafiki i dźwięki.** Lista: plik, autor albo narzędzie, data, licencja.
6. **Cytaty.** Przy każdym: autor, tytuł, wydanie, adres w Wolnych Lekturach.
7. **Dostęp do REVAS.** Zebrać, na jakiej podstawie autor miał konto (zgłoszenie do konkursu, zgoda nauczyciela) i co wtedy akceptował.
8. **Nie niszczyć dowodów.** Gdy spór jest przewidywalny, kasowanie materiałów szkodzi bardziej niż one same. Wyjątek to dane osobowe – tu decyzję zostawić prawnikowi.

---

## Część 5. Czego nie sprawdziłem i gdzie potrzebny prawnik

- **Regulamin i licencja platformy REVAS** (konto instruktora, zakaz automatycznego pobierania). Nie znalazłem go w sieci. Od niego zależy siła Z2 i Z3. To pierwsze pytanie do prawnika.
- **Znak „REVAS”** w UPRP i EUIPO – wyszukiwarka nic nie zwróciła, rejestrów nie przeszukałem bezpośrednio. To samo dla „Pewex”, „LUKRUM” i „Pan Cogito”.
- **Regulaminy „Zwolnionych z Teorii”**, urzędu miasta i kuratorium – nie czytałem.
- **Oryginał REVAS.** Porównywałem z remakiem autora i ze zgranymi stronami. Kodu serwera i prawdziwych parametrów REVAS nie znam, więc nie wiem, jak blisko prawdy są stałe z Z3.
- **Czy repozytoria i strona Levasa są publiczne** – nie sprawdzałem, żeby nie wysyłać nazw autora na zewnątrz.
- **Pełnego porównania `main` z remakiem linia po linii** dla kodu nie robiłem (tylko PR #2); dane porównałem w obu.
- **Nazwy fikcyjnych firm i lokali w grze** (np. „e-Księgi24.pl”, „Lublin Jedzie”, „Kebabowa Królowa”, „J.K.Ś.”, nazwy kebabów botów) – nie sprawdziłem, czy nie istnieją naprawdę.
- **Podglądów 1 i 2** (`podglady.html`, `podglady2.html`) nie oglądałem jako obrazu, tylko przeszukałem tekst.
- **Prawnik jest potrzebny do:** oceny Z2 (umowa, RODO, ewentualnie karne), decyzji o losie folderu `revas_26`, treści oświadczeń konkursowych, zasad użycia prawdziwych marek oraz statusu autora jako „przedsiębiorcy” w rozumieniu u.z.n.k.

Źródła zewnętrzne: regulamin MBIZ 2025 (`cdn.revas.pl/wp-content/uploads/2025/08/Regulamin-Konkursu-MBIZ-2025-2.pdf`), regulamin AMM 2026 (`revas.pl/wp-content/uploads/2026/02/Regulamin_AMM2026.pdf`). Orzeczenia TSUE przytaczam z pamięci – sygnatury do potwierdzenia przez prawnika.

---

## Lista kontrolna na następny przegląd

**Dane i wzory**
- [ ] Skrypt wspólnych stałych (≥ 3 miejsca po przecinku) między `gra/` a `revas_gra`: wynik 0 poza przypadkowymi (0,005; 0,004).
- [ ] `dane/katalog.yaml`: brak „Automat z kawą fair trade”, ceny 202, zestawu 95/200/20…30/2300/10, ocen 90/83/80, pakietów 1000/1800/2200/3000/4000.
- [ ] `dane/zalozenia.yaml`: brak 1,096 / 1,0035 / 0,247 / 1,498 / 0,407 / 0,593 / 0,654 / 0,073 i korekt miesięcy; brak frazy „panel 361 obserwacji”.
- [ ] `testy/dane_zamrozone/` zgodne z nowymi danymi.
- [ ] `rundy.odblokowanie` i limit dań: inna kolejność i klucze albo zastąpione listami wujka.
- [ ] Każda tabela ma w `zrodlo` prawdziwe, sprawdzalne źródło.
- [ ] Stan `main` = stan po PR #2 (nie zostały stare pliki).

**Interfejs i teksty**
- [ ] Brak „Karta wyników”, „Lista błędów”, „Wyślij decyzje”, „Dashboard” w panelu i w `INSTRUKCJA.md` (także w PDF).
- [ ] Zdanie z `ogolne.js:398` zmienione.
- [ ] Ponowne porównanie 6-wyrazowych ciągów z podręcznikami REVAS: 0.
- [ ] Zrzuty nowego wyglądu obok zrzutów REVAS: inny układ, kolory, nawigacja.

**Marki**
- [ ] `ikony_marek.js`: brak słownika `LOGA`; `mapa_budynki.js`: brak szyldów banków i barw firmowych.
- [ ] Lista wszystkich prawdziwych nazw w `dane/`, panelu, instrukcji i grafikach wnętrz; przy każdej decyzja „zostaje / fikcyjna”.
- [ ] Sklep meblowy i paleta „Pewex”: nazwy i wygląd.
- [ ] Fikcyjne nazwy firm sprawdzone w wyszukiwarce i KRS.

**Lektury i grafika**
- [ ] Tabela nawiązań: autor, rok śmierci, rodzaj (cytat / imię / aluzja), źródło tekstu.
- [ ] Autorzy chronieni: najwyżej jedna aluzja na autora, bez cytatów, bez własnych kwestii postaci.
- [ ] Ekran „Nawiązania i źródła” istnieje.
- [ ] Grafiki bywalców: brak podobieństwa do aktorów z ekranizacji; wykaz pochodzenia grafik, fontów (pliki lokalne + licencje) i dźwięków.
- [ ] Podpis OpenStreetMap na mapie.

**Otoczenie**
- [ ] Grep `revas|levas|fitness` w repo, w opisach PR, w README i w materiałach promocyjnych.
- [ ] Repo i strona Levasa niepubliczne; `revas_26` nieudostępniany.
- [ ] Regulamin platformy REVAS zdobyty i przeczytany przez prawnika.
- [ ] Regulaminy konkursów, do których idzie LUKRUM, sprawdzone pod kątem oświadczeń.
- [ ] Kasyno: domyślnie wyłączone i widoczne dla nauczyciela.
