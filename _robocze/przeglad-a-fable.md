# Przegląd gałęzi `mechaniki-a` (PR #2) – 14.11.2026

Zakres: `git diff origin/main...HEAD` (103 pliki), silnik, dane, testy, pomiary. Kodu nie zmieniałem.
Skrypty sprawdzające leżą poza repo. „Potwierdzone” znaczy: sprawdzone skryptem na danych gry (`dane/`) albo testem.

## Streszczenie

PR nie nadaje się do scalenia w obecnym stanie, choć rdzeń (punkty, pakiety biur, wypowiedzenie według stażu) liczy poprawnie i nie znalazłem awarii.
Blokują dwie rzeczy: pomyłki w szczycie zbijają oceny lokali do ok. 1,6★ u najlepszego bota, a debet w domyślnym trybie karze za chwilowy minus w środku tygodnia, także gdy tydzień kończy się na plusie.
Trzecia sprawa to zachęta odwrotna do zamierzonej: debet bez zgody banku kosztuje w złotówkach kilka razy mniej niż debet za zgodą.
Gra uczy też kilku nieścisłości prawnych (okres próbny, odsetki ponad maksymalne, zlecenie bez wad), a instrukcja gracza i dwie zakładki panelu opisują stare mechaniki.
Trzy zmienione testy nie zostały osłabione w istotny sposób, ale najważniejsze nowe ścieżki (debet w środku tygodnia, wpływ pomyłek na opinie, święto w ostatniej rundzie) nie mają testów.

Pełny pytest na gałęzi: **598 testów zielonych** (4 min 47 s), więc żadne z poniższych znalezisk nie jest dziś łapane przez testy.

## Znaleziska (od najpoważniejszego)

### 1. Pomyłki w szczycie zbijają oceny lokali do 1,6★ (waga opinii nie została przeliczona)

- **Gdzie:** `gra/dane/mapa/klienci.yaml:130` (`opinie.pomylki: 10.0`), `gra/silnik/rynek/opinie.py:76`, `gra/silnik/kuchnia/operacje.py:195–209`, `gra/dane/zalozenia.yaml:435–443`.
- **Scenariusz:** waga 10,0 gwiazdki × udział pomyłek pochodzi z czasów reklamacji, gdy udział wynosił ok. 0,2–0,3%. Nowa mechanika daje 10–19% pomyłek. Gra 5 botów, poziom średni, ziarno 11, 10 rund: udział pomyłek – mediana 11%, maksimum 18,7% (45 firmo-tygodni). Bot zrównoważony w tygodniu 8: 247 pomyłek na 1 575 dań, powód „pomyłki” = −1,57★, ocena tygodnia 1,0★, ocena lokalu 1,76★, mnożnik popytu 0,80. Bot tani: −1,42★, ocena 1,57★, mnożnik 0,78.
- **Dlaczego tyle pomyłek:** dodatek „za szczyt” liczy popyt dnia ÷ godziny dnia, więc w dni szczytu jest pełny (+10 pp) nawet przy tygodniowym wykorzystaniu 30–80%. Do tego dochodzi zmęczenie (+6 pp) i brak szkoleń (+2 pp). Pomyłka karze trzy razy: składniki, opinie (popyt) i −40 × udział w zadowoleniu gości.
- **Pewność:** potwierdzone (skrypt, dwie gry botów).
- **Poprawka:** obniżyć `opinie.pomylki` do ok. 2–3 albo obniżyć `za_szczyt` i `za_zmeczenie`, tak żeby dobra firma miała 2–4% pomyłek. Dodać test: bot zrównoważony na średnim nie schodzi z oceną lokalu poniżej np. 2,5★ z powodu samych pomyłek.

### 2. Debet powstaje w środku tygodnia i nie jest spłacany w tym samym tygodniu

- **Gdzie:** `gra/silnik/runda.py:179` (`uruchom_debet` po decyzjach), `gra/silnik/ksiegowosc/finanse.py:157–167` (`do_splaty = debet − pobrany_w_miesiacu`), `gra/silnik/pieniadze/banki.py:483–492` (opłata), `runda.py:284`.
- **Scenariusz:** domyślny tryb `na_biezaco`. Firma kończy tydzień 6 z 6 156 zł i bez debetu, w tygodniu 7 wydaje na decyzje więcej, niż ma, a sprzedaż wszystko pokrywa. Gra 2 botów, kapitał 24 000 zł, poziom średni, ziarno 7, bot premium:
  - tydzień 7: koniec tygodnia **gotówka 16 728 zł i jednocześnie debet 5 082 zł**; opłata 50 zł i odsetki;
  - tydzień 8: debet spłacony dopiero na końcu, więc bank pobiera **drugą opłatę 50 zł** i drugie odsetki za ten sam chwilowy minus.
- **Skutek bez zgody na debet:** gra łatwa, ziarno 7, bot agresywny, tydzień 7: gotówka 20 017 zł, debet 10 601 zł, **alarm i blokada inwestycji**, mimo że saldo netto jest dodatnie. Wcześniej limit był automatyczny, więc ten sam mechanizm nikogo nie karał. Teraz każda drużyna, która w poniedziałek wyda więcej, niż ma, dostaje alarm.
- **Niezgodność z opisem:** notatka „Debet”, komentarze i tekst dla gracza mówią „saldo poniżej zera na koniec tygodnia”.
- **Pewność:** potwierdzone (skrypt, tryby `na_biezaco` i `jednoczesnie`).
- **Poprawka:** w `wyrownaj_gotowke` spłacać cały debet z gotówki na koniec tygodnia (bez wyjątku dla debetu z tego tygodnia), a opłatę i alarm liczyć od salda końcowego. Prościej: przyjąć `jednoczesnie` jako tryb domyślny.

### 3. Debet bez zgody jest tańszy niż debet za zgodą i nie ma limitu

- **Gdzie:** `gra/silnik/pieniadze/banki.py:483–492`, `gra/dane/mapa/banki.yaml:15, 33–91`.
- **Scenariusz:** debet 2 000 zł przez tydzień. Za zgodą: Kmicic 46,54 zł, Soplicowo 51,15 zł, Solaris 96,54 zł (opłata tygodniowa + odsetki). Bez zgody: 7,31 zł (same odsetki karne 19% ÷ 52). Przy 8 000 zł: 66–116 zł za zgodą, 29,23 zł bez zgody. W Oszczędnościach Rzeckiego nawet sama stopa za zgodą (20%) jest wyższa od karnej (19%).
- **Skutek:** jedyną karą za debet bez zgody jest alarm i blokada inwestycji. Bot agresywny na łatwym kończy z 23 851 zł debetu bez zgody i płaci za niego ok. 87 zł tygodniowo. W ostatniej rundzie blokada nie działa wcale. Uczeń, który policzy, wyłączy debet.
- **Pewność:** potwierdzone arytmetycznie na danych gry i w grze botów.
- **Poprawka:** przy debecie bez zgody pobierać opłatę co najmniej taką jak najwyższa opłata tygodniowa banków (albo opłatę za „niedozwolone saldo debetowe”), a stopę karną trzymać powyżej każdej stopy debetu. Rozważyć odrzucanie wydatków ponad saldo, gdy debet jest wyłączony.

### 4. Firma, która nic nie robi, dostaje 353 pkt – prawie tyle co słaba gra

- **Gdzie:** `gra/silnik/wyniki/punkty.py:102–112` (zadowolenie gości bez gości), `punkty.py:155–156` i `gra/silnik/runda.py:584–588` (zespół i bezpieczeństwo bez działalności).
- **Scenariusz:** firma bez żadnej decyzji przez 12 tygodni (gra z 5 botami, poziom łatwy, ziarno 7): otwarcie 150 pkt, potem co tydzień 365 pkt: Finanse 34 (dochód ok. 0 → 20, marża 0 → 15), Goście 61 (zadowolenie 74/100 przy zerze gości), Zespół 40 (brak przepracowania przy zerze osób), Bezpieczeństwo 230 – najwyższe w całej grze. Wynik gry 352,7. W tej samej grze bot agresywny ma 380,6, bot tani 440,7, a w pojedynczych tygodniach bot tani schodzi do 345–364 pkt, czyli poniżej firmy bezczynnej.
- **Pewność:** potwierdzone.
- **Poprawka:** bez sprzedaży dawać 0 pkt za zadowolenie gości, bez zespołu 0 pkt za przepracowanie, a dział Bezpieczeństwo liczyć dopiero dla firmy z lokalem (albo mnożyć go przez udział obsłużonych). Dodać test „firma bezczynna < 150 pkt”.

### 5. Oprocentowanie debetu przekracza odsetki maksymalne (art. 359 § 2¹ KC)

- **Gdzie:** `gra/dane/mapa/banki.yaml:33` (Kmicic 17%), `:69` (Rzecki 20%), `:80` (Soplicowo 16%), `:91` (Solaris 17%).
- **Scenariusz:** plik sam przyjmuje stopę referencyjną NBP ok. 4%. Odsetki maksymalne kapitałowe to 2 × (4% + 3,5 pp) = 15%, a maksymalne za opóźnienie 2 × (4% + 5,5 pp) = 19% (tyle ma `stopa_karna`). Cztery banki mają debet droższy niż 15%, a Rzecki droższy nawet niż odsetki karne. Uczeń zobaczy „legalną” ofertę, której bank nie może dać.
- **Pewność:** prawdopodobne (zależy od aktualnej stopy NBP – nie sprawdzałem jej w źródle).
- **Poprawka:** obniżyć stopy debetu do najwyżej 15% i różnicować banki opłatą i limitem, albo dopisać w `zrodlo`, skąd wyższa stopa.

### 6. Okres próbny: 1 tydzień wypowiedzenia to nie jest reguła dla umowy na 3 miesiące (art. 34 KP)

- **Gdzie:** `gra/dane/kandydaci.yaml:174`, notatka „Kadry wg Kodeksu pracy” (wiersz 13), test `test_okres_wypowiedzenia_zalezy_od_stazu`.
- **Scenariusz:** gra traktuje pierwsze 12 tygodni jak okres próbny z wypowiedzeniem 1 tydzień. Art. 34 KP: 3 dni robocze przy okresie próbnym do 2 tygodni, 1 tydzień przy dłuższym niż 2 tygodnie, **2 tygodnie przy okresie próbnym 3 miesiące**. Gra opisuje właśnie umowę „do 3 miesięcy”, więc uczy złej liczby.
- **Pewność:** prawdopodobne (przepis znam, w ISAP nie sprawdzałem).
- **Poprawka:** dla stażu 0–12 tygodni dać 2 tygodnie albo opisać okres próbny jako „krótszy niż 3 miesiące”. Pozostałe progi (2 tygodnie, miesiąc, 3 miesiące) są zgodne z art. 36.

### 7. Umowa zlecenie jest w grze o ok. 34% tańsza za godzinę i prawie nic nie kosztuje

- **Gdzie:** `gra/dane/zalozenia.yaml:563` (urlop 10%), `:425` (`umowa_zlecenie: −0,02`), `gra/dane/podatki_2026.yaml` (`zus_pracodawcy_zlecenie: 0.0`, uproszczenie sprzed PR), `gra/dane/boty.yaml:169, 209`.
- **Scenariusz:** etat kosztuje 1,2048 × pensja za 0,9 godzin, czyli 1,339 za jednostkę pracy; zlecenie 1,0 za 1,0. Do tego niższa opłata kadrowa biura i brak wypowiedzenia. Jedyną wadą jest −0,02 w zadowoleniu (ok. 13 pkt składnika „Zadowolenie zespołu”) i odejście od razu. PR pogłębia starą różnicę (urlop 10%) i ustawia dwie strategie botów na zlecenie.
- **Czego to uczy:** że kucharza przy rożnie w stałych godzinach można legalnie i bez ryzyka zatrudnić na zleceniu. Naprawdę zlecenie ma składki jak etat (poza studentem do 26 lat), a praca w warunkach art. 22 § 1 KP jest stosunkiem pracy bez względu na nazwę umowy.
- **Pewność:** potwierdzone arytmetycznie; ocena dydaktyczna – moja.
- **Poprawka:** dodać ryzyko kontroli PIP przy zleceniu na stanowisku kuchni (mandat i przekształcenie w etat) albo przywrócić ZUS na zleceniu (jeden parametr) i zostawić zwolnienie tylko studentowi.

### 8. Scrooge: dopłata 3 zł to naprawdę ok. 6,30 zł, a mimo to biuro da się ograć

- **Gdzie:** `gra/silnik/ksiegowosc/biuro.py:158–178` (`nalicz`), `:70` (`limit_rundy`), `gra/dane/mapa/biura.yaml`.
- **a) Ukryta druga dopłata.** Limit pakietu jest miesięczny, ale silnik stosuje go co tydzień (28 dokumentów w pakiecie M). W zamkniętym tygodniu limit przepada, a tydzień później 61 dokumentów trafia na limit 28: 33 × 3,30 zł ponad limit + 29 × 3,00 zł za święto. Bot zrównoważony: 330,07 zł zamiast 123,74 zł. Opis dla gracza mówi tylko o 3 zł. Potwierdzone.
- **b) Święto w ostatniej rundzie.** Przeniesione dokumenty nigdy nie są rozliczone. Gra 11 rund (święto w rundzie 11): Scrooge znów najtańszy w 11 z 16 profili. Potwierdzone rachunkiem na `oplata()`.
- **c) Przeskok.** Zmiana biura jest darmowa i natychmiastowa, a kalendarz świąt jawny: Scrooge w zwykłe tygodnie i Józef K. w tygodniu ze świętem jest lepsze od każdego biura z osobna. Prawdopodobne (wynika z kodu, nie rozegrałem).
- **d) Asteroida 328 jest zawsze gorsza od J.K.Ś.** Oba mają OC i ryzyko 0, a J.K.Ś. jest tańsze w każdym z 16 profili; kadry „do 6 osób w cenie” zrównują ceny dopiero przy ok. 32 pracownikach. Potwierdzone.
- **e) Ryzyko błędu nic nie waży.** Mandat 200 zł × 4% = 8 zł na tydzień u Józefa K., 4 zł u Scrooge’a.
- **Poprawka:** limit liczyć miesięcznie albo przenosić niewykorzystany limit zamkniętego tygodnia; w ostatniej rundzie rozliczyć przeniesione dokumenty od razu; zmianę biura obłożyć opłatą albo tygodniem zwłoki; Asteroidzie dać cechę, której J.K.Ś. nie ma. Liczby do pytania o 3 zł są w sekcji „Balans”.

### 9. Opóźnienie zmiany pakietu u Józefa K. da się obejść

- **Gdzie:** `gra/silnik/ksiegowosc/biuro.py:118–125`.
- **Scenariusz:** runda 1: `{"biuro": "jozef_k", "pakiet": "M"}`. M jest pakietem domyślnym, więc funkcja wraca bez zapisania `pakiet_biura`. Runda 2: `{"pakiet": "S"}` wchodzi od razu jako „pierwszy wybór”. Dopiero trzecia zmiana czeka 2 rundy. Drugie obejście: jedna runda w innym biurze ze zmianą pakietu i powrót.
- **Pewność:** potwierdzone skryptem (po rundzie 2 `pakiet_biura == "S"`, `pakiet_nastepny is None`).
- **Poprawka:** przy wyborze biura zapisywać `pakiet_biura` wprost (także gdy równa się domyślnemu), a opóźnienie liczyć od wejścia do biura.

### 10. Panel i instrukcja gracza opisują stare mechaniki

- **Gdzie i co:**
  - `gra/panel_gracza/static/zakladki/sprzedaz.js:26, 39, 44` oraz `konkurencja.js:28` czytają pole `reklamacje`, którego silnik już nie zwraca (jest `pomylki`): kolumna i kafelek „Pomyłki w szczycie” są puste;
  - `hr.js:311` – etykieta „reklamacje” przy skłonności do pomyłek, a `proc(…, 0)` zaokrągla 0,45% i 1,2% do „0%” i „1%”;
  - `gra/silnik/wyniki/wnioski.py:178` – „Firma korzysta z kredytu odnawialnego”;
  - `gra/INSTRUKCJA.md:12, 514` – kapitał 40 000 zł; `:143, 160` – „wynik działalności”, średnia od tygodnia 2; `:371` – „odprawę płacisz od razu”; `:420` – kredyt odnawialny;
  - `gra/dane/zalozenia.yaml:207` – martwy parametr `kredyt_odnawialny_automatyczny: true`;
  - `gra/dane/zalozenia.yaml:756` – `wnioski.dlaczego_min: 0.05` został ze skali starego wyniku; w punktach zdanie „wynik prawie się nie zmienił” praktycznie nigdy nie padnie.
- **Pewność:** potwierdzone (grep; pola `reklamacje` nie ma w żadnym wyniku silnika). Panelu w przeglądarce nie otwierałem.
- **Poprawka:** podmienić pola w JS, poprawić teksty, przepisać cztery akapity instrukcji, `dlaczego_min` ustawić na ok. 10 pkt.

### 11. Pensja za okres wypowiedzenia przy wyprowadzce: zła kolumna KPiR i brak ZUS

- **Gdzie:** `gra/silnik/nieruchomosci/przejecia.py:280–283`.
- **Scenariusz:** najemca traci lokal, pracownik na umowie o pracę nie ma dokąd przejść. Silnik księguje „Wynagrodzenie za okres wypowiedzenia…” w domyślnej kolumnie „pozostałe” i bez składek pracodawcy. Zwykłe zwolnienie daje pensję w kolumnie wynagrodzeń i ZUS do końca wypowiedzenia. W samodzielnej księgowości dokument dostanie typ „Faktura zakupu”.
- **Pewność:** prawdopodobne (z kodu; nie rozegrałem wyprowadzki).
- **Poprawka:** podać kolumnę `"wynagrodzenia"` i doliczyć `stawka_zus` jak w `runda.py:249–252`.

### 12. Drobniejsze

- **Pomyłka przy pustym magazynie nic nie kosztuje** (`operacje.py:214` i `_zuzyj`): sprzedaż jest ograniczona zapasem przed losowaniem pomyłek, a brakujące zużycie jest po cichu obcinane. Pomyłka nie zużywa też godzin kuchni. Prawdopodobne.
- **Zmiana banku z otwartym debetem** (`banki.py:271–280`): zgoda przechodzi do nowego banku bez decyzji, razem z długiem; można przeskoczyć do Solarisa dopiero wtedy, gdy potrzebny jest limit. Prawdopodobne.
- **Urlop 10% = 26 dni** (`zalozenia.yaml:563`): 26 dni przysługuje po 10 latach stażu z wliczoną szkołą, młodszym 20 dni (7,7%). Uproszczenie do przyjęcia, ale źródło powinno to mówić.
- **Płatność za debet nie występuje w realnych cennikach jako „opłata za tydzień na minusie”** – banki biorą prowizję za przyznanie limitu i odsetki. To konstrukcja gry; warto to napisać w opisie.
- **`konkurencja.py:91`**: pole `zadowolenie_klientow` niesie teraz skalę 0–100 zamiast mnożnika ok. 1,0.
- **Nowe pozycje wyposażenia** to tylko `procent` w mnożniku popytu: „Dostawa przez aplikację” nie daje dowozu, „Ogródek” nie zależy od pory roku, „BLIK” daje 85% za 40 zł miesięcznie przy cenie 0.

### Sprawdzone i poprawne

- Tabele progów: każdy dział ma 200 pkt bez „ponad”; interpolacja i „ponad” liczą dobrze.
- Wagi tygodni: gra 1, 2, 3 i 12 rund – bez dzielenia przez zero (`[1,0]`, `[1,0; 1,0]`, `[1,0; 1,0; 2,0]`, 1,0…2,0).
- Składniki przy pomyłce liczą się drugi raz i tylko raz (`obsluzeni + pomylki`).
- Opłata za debet i odsetki idą do KPiR bez VAT (usługa zwolniona), opłaty biura z VAT 23%.
- Płaca minimalna 4 806 zł, brak odprawy w firmie poniżej 20 osób, progi art. 36 – zgodne.
- Święta tydzień po tygodniu (rundy 17–19) kumulują dokumenty – wynika z kodu (`+=`), nie rozgrywałem tak długiej gry.

## Testy

- **Pełny pytest:** 598 passed, 287 s (`python -X utf8 -m pytest -q -p no:cacheprovider` z `gra/`). Ruff i `silnik.dane sprawdz` – nie uruchamiałem.
- `test_zuzycie_zasobow_na_klienta`: zmiana uzasadniona, ale test przestał sprawdzać stałą liczbę (400 porcji). Nie wykryje za dużej liczby pomyłek. Warto dodać wariant z wyzerowanymi dodatkami (dokładnie 400) i wariant z szansą = `maks`.
- `test_zamowienia_ponad_saldo`: filtr po poziomie jest w porządku. Druga asercja nie pilnuje już, że w zakładce Dostawy nie ma innych błędów – drobne osłabienie.
- `test_bot_z_dwoma_lokalami…`: 6 → 7 rund nie osłabia testu, ale jest kruche; lepiej grać do chwili, gdy bot ma 2 lokale.
- Usunięte razem z kartą: test `wskaznik_zadluzenia` ma odpowiednik (`test_udzial_kapitalu`).
- **Brak testów dla:**
  - debetu w grze (tryb `na_biezaco`: opłata, spłata, alarm przy dodatnim saldzie) – są tylko testy na ręcznie ustawionej firmie;
  - porównania kosztu debetu za zgodą i bez zgody;
  - wpływu pomyłek na opinie i górnej granicy udziału pomyłek (`test_pomylki` sprawdza tylko „≥ 0” i „kiedyś > 0”);
  - święta w ostatniej rundzie i zmiany biura z przeniesionymi dokumentami;
  - obejścia opóźnienia u Józefa K.;
  - wyniku firmy bezczynnej i firmy bez pracowników;
  - pensji za wypowiedzenie przy wyprowadzce;
  - wypowiedzenia po 13 i 26 tygodniach w rozegranej grze (jest tylko wywołanie funkcji).

## Balans

- **Agresywny bot „bankrutuje” na łatwym – sens gry, nie błąd, ale z zastrzeżeniem.** Tak samo było przed PR (2 750 zł gotówki, wynik −0,91), więc to nie regres. Przyczyna jest jednak inna, niż sugeruje raport: bot łatwy nigdy nie włącza debetu, więc od tygodnia 7 ma stały alarm i 10–26 tys. zł debetu bez zgody. To nie jest bankructwo – firma gra dalej i płaci ok. 90 zł tygodniowo (znalezisko 3). Lekcja „agresja bez finansowania kończy się źle” działa dopiero wtedy, gdy debet bez zgody naprawdę boli.
- **Czy 3 zł wystarcza na Scrooge’a.** Rachunek na `oplata()` dla 16 profili (15–60 dokumentów, 2–6 etatów albo 3 zlecenia), koszt łączny z oczekiwanym mandatem:
  - 12 rund, święta w rundach 9 i 11: Scrooge **nie wygrywa w żadnym profilu**; najtańszy jest Józef K. (11 profili) albo J.K.Ś. (5). Przy 30 dokumentach i 2 etatach: Józef K. 1 786 zł, Scrooge 1 898 zł, J.K.Ś. 2 043 zł, Asteroida 2 907 zł;
  - 12 rund bez świąt (albo gra do 8 rund): Scrooge wygrywa w 13 z 16 profili (1 533 zł wobec 1 786 zł);
  - 11 rund, święto w ostatniej: Scrooge wygrywa w 11 z 16.
  - Wniosek: sama dopłata 3 zł nie wystarczyłaby – działa dopiero razem z ukrytą dopłatą ponad limit (razem ok. 180–310 zł za jedno święto). Wynik zależy więc od kalendarza, a nie od decyzji gracza, i znika przy przeskoku między biurami. Różnice to 100–250 zł na 12 tygodni, czyli poniżej 0,3% kosztów firmy: wybór biura praktycznie nie wpływa na wynik.
- **Pomyłki** są największym powodem niskich ocen lokali; mnożnik popytu z opinii u dwóch sprawdzonych botów to 0,78–0,80 (znalezisko 1), więc pomiary z `d14_punkty.md` są zaniżone względem tego, co wyjdzie po poprawce wagi.
- **Wielkie otwarcie:** boty mają 553–695 pkt niezależnie od poziomu; człowiek łatwo zrobi 1 000 (lokal, 6 dań, 3 osoby, 800 zł towaru, 25 tys. zł w kasie). Przy wadze 1,0 to ok. +25 pkt wyniku gry przewagi nad botem – do oceny po grze testowej.

## Pytania do autora

1. Debet: czy opłata ma dotyczyć salda na koniec tygodnia (jak w notatce), czy każdego chwilowego minusa? Od tego zależy poprawka znaleziska 2.
2. Debet bez zgody: dopłata, wyższa stopa czy odrzucanie wydatków ponad saldo?
3. Ile pomyłek ma mieć dobra firma – 2–4% czy obecne 10–15%? I czy pomyłka ma karać w opiniach tak mocno jak kolejka?
4. Zlecenie: zostaje uproszczenie „bez ZUS i bez ryzyka”, czy dodać kontrolę PIP?
5. Okres próbny: 2 tygodnie (umowa na 3 miesiące) czy inny opis?
6. Stopy debetu ponad 15%: obniżyć czy zostawić jako świadome uproszczenie?
7. Scrooge: czy limit pakietu ma przepadać w zamkniętym tygodniu (dziś tak), i czy zmiana biura ma być darmowa?
8. Asteroida 328: jaką przewagę ma mieć nad J.K.Ś.?
9. Firma bezczynna: ile punktów powinna mieć?
10. Kto aktualizuje `INSTRUKCJA.md` – ten PR czy osobne zadanie?

## Czego nie sprawdziłem

- Panelu w przeglądarce (tylko kod JS grepem) i panelu mistrza gry.
- Pliku `Revas` – zgodnie z zakazem.
- Aktualnej stopy NBP i brzmienia art. 34 KP w ISAP – oparłem się na wiedzy własnej.
- Cen rynkowych w katalogach (wyposażenie, szkolenia, pensje z ofert) – nie weryfikowałem źródeł.
- Przejęć zastawu, leasingu, Harpagona i inwestora ratunkowego w połączeniu z debetem.
- Samodzielnej księgowości z nowymi dokumentami (opłata za debet, dokumenty przeniesione).
- Gier dłuższych niż 12 rund, poziomu „niemożliwy” i botów „człowiek”.
- Zamrożonych danych testów poza porównaniem z opisem w raporcie agenta.
- Pomiary własne to pojedyncze gry (ziarna 7 i 11), a nie serie; liczby pokazują mechanizm, nie średnie.
