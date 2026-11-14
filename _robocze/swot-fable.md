# LUKRUM – analiza strategiczna (SWOT, TOWS, ocena planu) – 14.11.2026

Niczego nie zmieniałem w repozytoriach ani w notatkach. Ścieżki bez przedrostka liczę od `Pulpit\Levas\lukrum\`.
„Raport szkolny” to `Levas\_archiwum\reserch\reports\Symulacje biznesowe dla młodzieży.md` (6.11.2026).

## 1. Streszczenie

LUKRUM ma dziś mocny silnik i słabe wszystko, co stoi między silnikiem a klasą. Silnik liczy grę 5 firm na 8 tygodni w 3,3 s, jest powtarzalny, ma kilkaset testów i narzędzia szkolne, których konkurencja nie ma: zakrywanie funkcji, zegar rundy, refleksje drużyn, eksport wyników. Żaden człowiek poza autorem jeszcze w tę grę nie zagrał: cały balans pochodzi z botów, a „gra testowa” jest odkładana od Levasa. Plan odsuwa ją jeszcze dalej, bo przed lekcjami (etap 4) stawia nową mapę, wnętrza wszystkich budynków, drugi tor mechanik, dekorowanie lokalu, dźwięk i telefon. Tymczasem konkurs „Zwolnieni z Teorii” nagradza przeprowadzone zajęcia i liczbę odbiorców, a nie jakość aplikacji, i ma termin końcowy 31.03.2027. Gałąź główna jest w najgorszym stanie prawnym (liczby i katalogi wspólne z REVAS), a poprawiający to PR #2 czeka i blokuje trzy inne wątki. Mapa, czyli nowa nawigacja całej gry, leży na ścieżce krytycznej, a po stronie kolegi nie ma jeszcze żadnej gałęzi ani odpowiedzi w `WSPOLPRACA.md`. Najważniejsze na teraz: scalić poprawiony PR #2, wyciąć zakres do „wersji na pierwszą lekcję” i jak najszybciej posadzić przy grze prawdziwych ludzi ze stoperem.

## 2. SWOT

### Mocne strony

| # | Co | Uzasadnienie i źródło |
|---|---|---|
| S1 | Wspólny rynek klasy na mapie prawdziwego miasta | Raport szkolny: najpopularniejsze licealne symulacje (Virtual Business, GoVenture) nie mają wspólnego rynku, a konkurs REVAS gra na niezależnych rynkach. Na liście materiałów MEN do „biznesu i zarządzania” nie ma darmowej polskiej gry wieloosobowej na mapie miasta |
| S2 | Silnik oddzielony od strony, powtarzalny, szybki | `lukrum_gra/dokumentacja/STACK.md`: silnik nie importuje Django, jedno źródło losowości, zapis gry jako decyzje. Mój pomiar na `main`: `balans.symuluj 8 sredni 7` = 3,3 s. Dzięki temu wymiana interfejsu nie rusza mechanik |
| S3 | Liczby gry w danych, z polem `zrodlo` | `gra/dane/*.yaml`, test `test_w_kodzie_silnika_nie_ma_liczb_gry`. Balans i wersję „pod lekcję” zmienia się bez programowania |
| S4 | Gotowe narzędzia dla nauczyciela | `gra/dane/funkcje.yaml`: 18 funkcji do zakrycia lub wyłączenia i zestawy „Pierwsza gra”, „Pełna gra”, „Krótka lekcja”. `gra/gry/harmonogram.py`: terminy i automatyczne zamykanie rund. `gra/gry/models.py`: `Runda.refleksje`. Panel `/mg/`: ranking i wyniki do CSV, konta drużyn |
| S5 | Treść prawdziwa i lokalna | `gra/dane/podatki_2026.yaml`, KPiR, VAT, ZUS, płaca minimalna 4 806 zł, pensje z ofert z Lublina (`_robocze/mechaniki-a-raport/raport.md`, część 4). Podstawa „biznesu i zarządzania” wymaga, by metoda „odzwierciedlała rzeczywistość społeczno-gospodarczą” (raport szkolny) |
| S6 | Notatki funkcji od razu w formie dla nauczyciela | `notatki/Funkcje/*.md`: każda ma „Dla ucznia”, „Czego uczy”, pytanie do omówienia i zadanie dla drużyn. To półprodukt scenariuszy lekcji |
| S7 | Proces z agentami, który sam siebie sprawdza | Briefy, raporty do plików, pomiary botami przed decyzją (`notatki/PLAN_PRZEBUDOWY.md`, rozdz. 9 i 11). Niezależny przegląd znalazł 12 błędów przy 598 zielonych testach (`_robocze/przeglad-a-fable.md`), a symulowany pozew wskazał źródło ryzyka (`_robocze/pozew-revas-fable.md`) |
| S8 | Tempo | Levas: 427 commitów od 25.10 do 13.11.2026. LUKRUM w dwa dni: etap 1, tor A (PR #2), dane i silnik wnętrz z 62 testami (`_robocze/wnetrza-silnik-raport.md`) |
| S9 | Jasne zasady współpracy na papierze | `notatki/WSPOLPRACA.md`: granica mapa ↔ wnętrza, gałęzie, PR przeglądany przez drugą stronę, wspólna tablica pytań |
| S10 | Lektury jako drugi przedmiot | Banki i biura z „Lalki”, „Potopu”, „Procesu”; bywalcy mówią cytatami (`notatki/Funkcje/Banki z lektur.md`, `_robocze/wnetrza-dane/gra/dane/wnetrza/bywalcy.yaml`). Daje to argument dla polonisty i temat do promocji |

### Słabe strony

| # | Co | Uzasadnienie i źródło |
|---|---|---|
| W1 | Nikt jeszcze nie grał | Balans i trudność znamy tylko z botów. „Po grze testowej” wraca jako odroczenie w `notatki/Do decyzji.md` (progi punktów, Wielkie otwarcie) i w `levas_gra/dokumentacja/POSTEP.md`, wiersz 131. Nie wiemy, ile minut trwa runda człowieka |
| W2 | Mechaniki toru A uczą błędów | `_robocze/przeglad-a-fable.md`: oceny lokali spadają do 1,6★ przez pomyłki, debet bez zgody był tańszy niż za zgodą, firma bezczynna dostaje 353 pkt, okres próbny i zlecenie niezgodne z Kodeksem pracy. Poprawki są w toku: w `_robocze/mechaniki-a` leży 14 zmienionych, niezapisanych plików (m.in. `opinie.pomylki` 10 → 2,5, stopy debetu ≤ 15%) |
| W3 | `main` w najgorszym stanie prawnym | `_robocze/pozew-revas-fable.md`, Z1 i Z3: 45 stałych i pełne katalogi wspólne z odtworzeniem REVAS; w PR #2 zostało 22 stałych i trzy tabele. Opisy źródeł przerobiono tak, że liczba została, a źródło znikło |
| W4 | Interfejs do wyrzucenia | `notatki/PLAN_PRZEBUDOWY.md`, rozdz. 10: obecny panel to „rusztowanie, nikomu go nie pokazujemy”. To ok. 11 tys. linii JS w `gra/panel_gracza/static/`. Nowe mechaniki nie mają jeszcze żadnego ekranu w nowym wyglądzie; raport toru A kończy się zdaniem „panel nadal rusztowanie” |
| W5 | Opisy rozjechały się z grą | `gra/INSTRUKCJA.md` (534 linie) mówi o 40 000 zł, odprawach i kredycie odnawialnym; dwie zakładki czytają nieistniejące pole `reklamacje` (przegląd, znalezisko 10). `README.md` podaje etap 1½ jako „do zrobienia”. Plan (rozdz. 2 i 7), `WSPOLPRACA.md` (zasada 7) i `LUKRUM.md` mówią „bez prawdziwych logo”, a decyzja z 14.11 w `Do decyzji.md` mówi, że logotypy zostają |
| W6 | Kolejka decyzji u jednej osoby | `notatki/Do decyzji.md` ma 28 otwartych pól, do tego 10 pytań z przeglądu toru A i 5 z raportu wnętrz. Autor „nie wymyśla wzorów, wybiera z propozycji”, więc każda mechanika czeka na niego |
| W7 | Współpraca działa tylko w jedną stronę | `git ls-remote`: w repo są gałęzie `main`, `mechaniki-a`, `wnetrza-dane`, żadnej `mapa-…`. Dwa pytania do `[mapa]` z 13.11 w `WSPOLPRACA.md` są bez odpowiedzi, trzy propozycje granicy z 14.11 niepotwierdzone. Termin prototypu mapy to 16.11 |
| W8 | PR #2 jako korek | Od scalenia PR #2 zależą: skutki propozycji klientów w `runda.py` (`wnetrza-silnik-raport.md`), dopiski `geo` w `budynki.yaml` dla mapy (`WSPOLPRACA.md`) i zdarzenia z lektur w `parki.yaml` (`Plan na 14.11.md`, pkt 2b) |
| W9 | Serwer to laptop autora | `gra/hostuj.bat`: serwer deweloperski Django i tymczasowy tunel Cloudflare, baza SQLite. Dawny hosting strony nie uruchamia Pythona (pamięć projektu, `strona-levas-ftp`). Gra działa tylko wtedy, gdy autor ma włączony komputer |
| W10 | Brak RODO, dostępności i telefonu | W repo nie ma polityki prywatności ani wzoru umowy powierzenia (grep: zero trafień poza `LOGOWANIE_MICROSOFT.md`). W panelu są 23 atrybuty `aria-label` na całość. Telefon „odłożony świadomie” (pamięć `poprawki4`), a plan obiecuje „komputery i telefony” |
| W11 | Testy nie łapią błędów sensu | 598 zielonych testów nie wykryło żadnego z 12 znalezisk przeglądu. Brakuje testów typu „dobra firma ma ocenę ≥ 2,5★”, „firma bezczynna < 150 pkt” |
| W12 | Kasyno ukryte przed nauczycielem | `gra/lukrum/settings.py:144`: domyślnie włączone. `notatki/Funkcje/Kasyno Pod Złotym Koziołkiem.md`: klub nie trafia do przeglądu mistrza gry ani do eksportu |

### Szanse

| # | Co | Uzasadnienie i źródło |
|---|---|---|
| O1 | Podstawa programowa wprost wymienia symulacje | Warunki realizacji „biznesu i zarządzania”: „symulacje biznesowe” (pkt 5) i „elementy grywalizacji” (pkt 10); dział VI obejmuje konkurencję, finansowanie, prognozę przychodów i kosztów (raport szkolny, [zpe.gov.pl](https://zpe.gov.pl/podstawa-programowa/szkola-ponadpodstawowa/biznes-i-zarzadzanie)) |
| O2 | Szkoła może wprowadzić grę sama | Innowacja pedagogiczna nie wymaga zgłoszenia do kuratorium; przy darmowej grze nie trzeba zgody organu prowadzącego (raport szkolny). Wystarczy jeden nauczyciel |
| O3 | Luka na rynku | Darmowa rundowa symulacja firmy prowadzona przez nauczyciela (JA Titan) zniknęła z oferty FMP (raport szkolny). Wyszukiwanie z 14.11 zwraca dla szkół głównie grę giełdową SIGG Fundacji GPW i webinary; ceny REVAS dla szkół nie są publiczne |
| O4 | Miasto ma gotowy program | „Przedsiębiorcza Młodzież” UM Lublin i UMCS: ok. 200 uczniów z 9 szkół w 2026 r., nabór prawdopodobnie w styczniu 2027. Mikrogranty „Miejski Aktywator Młodzieżowy” dla grup nieformalnych 13–26 lat (raport szkolny; naboru na 2027 nie znalazłem) |
| O5 | Patronat kuratora na wydarzenie | Kuratoria ogłaszają i obejmują patronatem turnieje z datą, nie produkty. Lubelskie ma regulamin patronatu z 13.09.2024 (raport szkolny) |
| O6 | Dowód skuteczności, którego nikt nie ma | Raport szkolny nie znalazł polskiej ewaluacji szkolnej symulacji z grupą porównawczą. Test przed i po grze byłby mocnym argumentem dla kuratorium i grantodawców |
| O7 | „Zwolnieni z Teorii” jako rama i termin | Etap realizacji wymaga partnera, co naturalnie prowadzi do listu szkoły i rozmowy z urzędem (raport szkolny) |
| O8 | Lublin Europejską Stolicą Kultury 2029 | Miasto prowadzi programy wspierające ESK ([lublin.eu](https://lublin.eu/en/what-to-see-do/european-capital-of-culture-2029/supportive-programs)). Gra o Lublinie z lekturami pasuje do Wydziału Kultury, który prowadzi też „Przedsiębiorczą Młodzież” |

### Zagrożenia

| # | Co | Uzasadnienie i źródło |
|---|---|---|
| T1 | Spór z REVAS albo wstyd przy weryfikacji | `_robocze/pozew-revas-fable.md`: najmocniejszy zarzut to sposób zdobycia danych (folder `revas_26`), a w konkursie i w urzędzie zwykle podpisuje się oświadczenie o oryginalności. Autor startuje w konkursie REVAS, a KUL używa symulacji REVAS, więc środowisko jest małe |
| T2 | Logotypy prawdziwych firm | Decyzja autora z 14.11: zostają. Skutek do przyjęcia: sieci handlowe wysyłają wezwania rutynowo (pozew, Z4), a urząd lub kuratorium mogą odmówić firmowania gry z cudzymi znakami |
| T3 | Projekt nie dotrze do klasy przed 31.03.2027 | Terminy „Zwolnionych z Teorii” z raportu szkolnego: projekt i zespół do 16.11.2026, formularze 1.12, realizacja do 31.03.2027 (daty do potwierdzenia na platformie). Plan stawia lekcje na końcu |
| T4 | Jedna godzina tygodniowo i 45 minut | „Biznes i zarządzanie” w zakresie podstawowym to 2 godziny w całym liceum, czyli ok. 60 lekcji (raport szkolny). Nauka zasad symulacji trwa 4–6 okresów decyzyjnych (tamże) |
| T5 | Zmiana podstaw programowych | Nowe podstawy w klasach I szkół ponadpodstawowych od września 2027; „biznes i zarządzanie” jest wśród przedmiotów w opracowaniu, wymiaru godzin nie znalazłem ([gov.pl](https://www.gov.pl/web/nauka/zmiany-w-podstawie-programowej-ksztalcenia-ogolnego), prezentacja IBE). Plan mówi o „lekcjach WOS”, a WOS w zakresie podstawowym jest zastępowany edukacją obywatelską (z pamięci, do potwierdzenia) |
| T6 | Telefony i sieć w szkole | Statuty szkół trzeba dostosować do ustawy o telefonach do 31.12.2026; w liceum decyduje statut. Szkolne Wi-Fi bywa słabe (raport szkolny, NIK) |
| T7 | RODO i dostępność | Gdy szkoła każe uczniom używać gry, staje się administratorem, a autor podmiotem przetwarzającym (art. 28 RODO). Szkoły obowiązuje WCAG 2.1 AA (raport szkolny). Logowanie Microsoft przekazuje imię, nazwisko i adres ucznia |
| T8 | Czas i siły licealistów | Projekt na Złotego Wilka to 4–10 godzin tygodniowo przez 4–6 miesięcy (raport szkolny). Dochodzą szkoła, konkurs REVAS i matura. Projekt stoi na jednej osobie |
| T9 | Utrzymanie po projekcie | Podatki, płaca minimalna i stopy trzeba aktualizować co rok (`gra/dane/podatki_2026.yaml`, `stopa_referencyjna_nbp` w `banki.yaml`). Bez autora i jego agentów nikt tego nie zrobi; nie ma też serwera ani opiekuna |
| T10 | Spadkobiercy autorów chronionych | Gombrowicz do 2039, Lem do 2076, Herbert do 2068 (pozew, Z9). Ryzyko rośnie, gdy postać dostaje własne kwestie i rysunek |

## 3. Strategie z macierzy TOWS

### S–O: mocne strony do szans

1. **Sprzedawać wspólny rynek i Lublin, nie grafikę (S1, S5 → O1, O3, O4).** Jednostronicowy opis dla nauczyciela i urzędu: klasa gra na jednym rynku, z polskimi podatkami, na mapie swojego miasta. To jest różnica wobec REVAS i gier giełdowych.
2. **Zrobić z notatek funkcji scenariusze (S6 → O1, O2).** Każda notatka ma już pytanie i zadanie. Brakuje tylko przypisania do punktów podstawy i ułożenia w lekcje. To praca na dni, nie tygodnie.
3. **Użyć zestawu „Krótka lekcja” i zegara jako trybu lekcyjnego (S4 → O2, O7).** Plan odkłada „presety” na później, a one już są w `funkcje.yaml`. Wystarczy je sprawdzić z ludźmi.
4. **Wbudować test przed i po (S2, S3 → O6).** Silnik i panel mistrza gry mają już refleksje i eksport CSV; dziesięć pytań przed pierwszą i po ostatniej rundzie da dowód dla kuratorium i grantu.
5. **Zaproponować miastu turniej, nie program (S1, S10 → O4, O5, O8).** Jedno wydarzenie z datą w „Przedsiębiorczej Młodzieży” da i patronat, i odbiorców do konkursu.

### W–O: słabości naprawiane szansami

1. **Gra próbna jako źródło decyzji (W1, W6 → O2).** Połowa otwartych pól w `Do decyzji.md` czeka „na grę testową”. Jedna gra z czterema osobami zamknie je szybciej niż kolejne pomiary botów.
2. **Jedna szkoła i jeden nauczyciel jako pilotaż (W9, W10 → O2).** Dla jednej klasy wystarczy mały serwer i konta na pseudonimach. Pełne RODO i dostępność są potrzebne przed drugą szkołą, nie przed pierwszą lekcją.
3. **Mikrogrant na serwer i domenę (W9 → O4).** Koszt jest mały, a grant daje też partnera wymaganego w konkursie.
4. **Zamówić u kolegi najpierw rzecz najmniejszą (W7 → O7).** Prototyp na 16.11 zdefiniować jako: mapa z kilkoma budynkami, kliknięcie woła `otworzWnetrze(id)`. Bez danych z OpenStreetMap w pierwszym kroku.

### S–T: mocne strony przeciw zagrożeniom

1. **Policzyć liczby od nowa własnymi botami (S2, S3, S7 → T1).** Narzędzia pomiarowe są. Każdą stałą wspólną z REVAS zastąpić wynikiem pomiaru z datą i nazwą pliku; martwe usunąć. Tak radzi pozew (część 2, Z1 i Z3) i część tego jest już w niezapisanych zmianach na `mechaniki-a`.
2. **Przełącznik „ikony ogólne” (S3 → T2).** Decyzja o logotypach zostaje, ale ogólne ikony `KOSZYK`, `WOZEK`, `PALETA` już są w `ikony_marek.js`. Jedno ustawienie serwera pozwoli pokazać urzędowi wersję bez cudzych znaków, bez zmiany gry dla klasy.
3. **Skrócić grę danymi, nie kodem (S3, S4 → T4).** Wariant 6–8 rund z zakrytymi funkcjami i księgowością w biurze mieści się w rytmie jednej godziny tygodniowo.
4. **Powtarzalny silnik jako podstawa utrzymania (S2 → T9).** Jeden plik „co zmienić 1 stycznia” (podatki, płaca minimalna, stopa NBP) i polecenie `silnik.dane sprawdz` pozwolą zaktualizować grę komuś innemu niż autor.

### W–T: obrona

1. **Nie pokazywać `main` nikomu przed scaleniem poprawionego PR #2 (W3 → T1).** Dotyczy też oświadczeń konkursowych.
2. **Zamrozić zakres do pierwszej lekcji (W4, W6 → T3, T8).** Wszystko, co nie jest potrzebne do rozegrania 3–4 rund w klasie, przesunąć za pierwszą lekcję.
3. **Kasyno domyślnie wyłączone albo widoczne dla nauczyciela (W12 → T2, T7).** Hazard ukryty przed mistrzem gry może zamknąć drogę przez kuratorium. Jako świadomie włączany temat lekcji o wartości oczekiwanej jest atutem.
4. **Ograniczyć nawiązania do autorów chronionych (W5 → T10).** Jedna aluzja na autora, bez własnych kwestii postaci; reszta z domeny publicznej, której jest dość.
5. **Rozmowa z prawnikiem o folderze `revas_26` (W3 → T1).** Bez niej nie da się ocenić najmocniejszego zarzutu. Folderu nie kasować na własną rękę (pozew, część 4).

## 4. Ocena planu

### Co jest za duże albo zbędne przed pierwszą lekcją

- **Wnętrza we wszystkich budynkach** (`notatki/Wygląd.md`: bank, hurtownia, biuro, urzędy). Do lekcji wystarczy kebab i ekrany podstawy gry. Lista podstawy jest w nagłówku `funkcje.yaml`: pulpit, mapa, wyniki, wybór lokalu, mój lokal, kuchnia, zespół, sprzęt, finanse i bank, biuro, lista błędów, wysyłanie decyzji.
- **Tor B** (`PLAN_PRZEBUDOWY.md`, rozdz. 11). Gwiazdki gości i nastrój zespołu zastąpią wzory, które tor A właśnie skalibrował, więc balans trzeba będzie mierzyć drugi raz. Fabuła z wujkiem zastępuje harmonogram odblokowań, a zakrywanie funkcji robi to samo już dziś.
- **Dekorowanie lokalu, dźwięk, pora dnia zgodna z zegarem, kilka wnętrz w trzech stanach, dwie palety w dwóch trybach** (`Wygląd.md`, decyzje 13–14.11). Każdy ekran trzeba wtedy narysować i sprawdzić cztery razy. Na lekcję wystarczy jedna paleta, jasna i ciemna.
- **Telefon równolegle z komputerem.** Raport szkolny zaleca jedno urządzenie na drużynę i komputer; statuty mogą zakazać telefonów. Telefon może poczekać.
- **Cel „zero śladów Revasa w historii gita”.** Według pozwu (część 3) to pogarsza pozycję autora. Lepszy cel: zero zapożyczonej treści i zapis, skąd jest każda liczba.
- **Kolejne branże „w danych”, giełda, handel, Harpagon, easter eggi.** Nie szkodzą, ale każda nowa mechanika to notatka, opis w instrukcji, test i pytanie do autora.

### Czego w planie brakuje

- **Lekcja 45 minut.** Plan ma jedno otwarte zdanie („ok. 4 tygodnie gry, ale się tym nie sugeruj”). Nie ma pomiaru, ile trwa runda człowieka, ani podziału lekcji. Raport szkolny proponuje 5–8 minut wstępu, 20–25 decyzji, 10–12 omówienia. Etap 3 planuje pomiar „czy mapa nie spowalnia”, ale nie ma punktu odniesienia.
- **Wdrożenie nauczyciela.** Brak przewodnika prowadzącego, krótkiego szkolenia i „pierwszych 10 minut” mistrza gry. Konkurs REVAS wymaga od opiekuna 4 godzin szkolenia; LUKRUM powinno wymagać mniej.
- **Ocenianie.** Raport szkolny: ocena nie powinna zależeć od miejsca w rankingu. Plan nie mówi, co nauczyciel wpisuje do dziennika. Refleksje i CSV są, brakuje karty pracy i testu.
- **Tabela „mechanika a punkt podstawy programowej”.** Bez niej nie ma innowacji pedagogicznej ani rozmowy z kuratorium. Plan mówi „WOS”, a oparciem jest „biznes i zarządzanie”.
- **Serwer i koszty.** Nigdzie nie zapisano, gdzie gra stoi podczas lekcji, kto płaci i kto reaguje, gdy padnie. Mały serwer w UE to rząd kilkudziesięciu złotych miesięcznie (mój szacunek, cenników nie sprawdzałem).
- **RODO uczniów.** Brak polityki prywatności, wzoru umowy powierzenia i zasady „konta na pseudonimach”. Refleksje to wolny tekst uczniów w bazie. Fonty i tunel idą przez serwery firm z USA.
- **Dostępność.** Brak kontroli kontrastu palet PRL, obsługi klawiaturą i tekstów zastępczych mapy. Mapa i wnętrza rysowane w SVG to najtrudniejszy przypadek.
- **Plan awaryjny lekcji.** Co robi nauczyciel, gdy sieć padnie albo drużyna nie wyśle decyzji. Automatyczne zamknięcie rundy jest; brakuje opisu.
- **Kryterium „gotowe do klasy”.** Etapy kończą się przeglądem autora, żaden nie kończy się grą z ludźmi.
- **Utrzymanie.** Kto po maturze aktualizuje podatki i odpowiada nauczycielom.

### Gdzie projekt najpewniej utknie

1. **Między etapem 2 a 3.** Stary panel jest zakazany do pokazywania, nowy powstaje w dwóch rękach (mapa u kolegi, wnętrza u autora), a granica między nimi jest nieuzgodniona. Jeśli mapa się opóźni, nie ma czego pokazać klasie, mimo działającego silnika.
2. **W kolejce decyzji autora.** Ponad 40 otwartych pytań przy jednej osobie decydującej i agentach, którzy produkują nowe pytania szybciej, niż autor odpowiada.
3. **W pętli przebudowy.** Levas → LUKRUM, zakładki → mapa, tor A → tor B, wzory → gwiazdki. Każda pętla jest uzasadniona, ale żadna nie przybliża pierwszej lekcji. Bez twardej daty gry w klasie następna pętla też się znajdzie.
4. **Na PR #2.** Dopóki nie jest scalony, stoją skutki propozycji klientów, dane mapy i zdarzenia z lektur, a `main` zostaje w stanie, którego nie wolno pokazać.

## 5. Priorytety

Kroki 1–8 trzeba zrobić przed pierwszą lekcją testową w szkole. Kroki 9–10 można zacząć równolegle, ale lekcja na nie nie czeka.

| # | Krok | Po co | Wysiłek | Kto |
|---|---|---|---|---|
| 1 | Założyć projekt i zespół w „Zwolnionych z Teorii”, potwierdzić daty na platformie, opisać projekt jako problem („licealiści nie umieją policzyć kosztów i podatków małej firmy”), wpisać datę pierwszej lekcji | Termin 16.11. Data lekcji zatrzymuje pętlę przebudowy | mały | autor osobiście |
| 2 | Jedna sesja decyzji: 10 pytań z `przeglad-a-fable.md`, 8 zaczepek WOS i pola z `Do decyzji.md`. Przy okazji ujednolicić zapis o logotypach w planie, `WSPOLPRACA.md` i `LUKRUM.md` | Odblokowuje krok 3 i usuwa sprzeczne instrukcje dla agentów obu stron | mały | autor osobiście |
| 3 | Dokończyć poprawki PR #2 (znaleziska 1–9 i 11), dodać brakujące testy sensu, wymienić resztę katalogów i stałych wspólnych z REVAS (pozew, Z1 i Z3), scalić | `main` przestaje być stanem, którego nie wolno pokazać; rusza mapa, wnętrza i zdarzenia | średni | `[mechaniki]`, scala autor |
| 4 | Rozmowa autora z kolegą: przyjąć trzy propozycje granicy z `WSPOLPRACA.md`, ustalić najmniejszy prototyp (kilka budynków i `otworzWnetrze`), pierwsza gałąź `mapa-…` w repo choćby surowa | Mapa jest na ścieżce krytycznej, a dziś nie widać żadnej pracy drugiej strony | mały | autor osobiście i `[mapa]` |
| 5 | Spisać „wersję na pierwszą lekcję”: zestaw „Krótka lekcja”, 6–8 rund, lista ekranów podstawy; resztę (tor B, dekorowanie, dźwięk, pora dnia, inne wnętrza, telefon) przenieść za lekcję | Zakres, który da się skończyć w kilka tygodni | mały | autor osobiście, spisuje `[mechaniki]` |
| 6 | Gra próbna z 4–6 osobami na obecnym panelu, 45 minut ze stoperem, bez publiczności (to nie jest „pokazywanie” gry) | Pierwsze dane o czasie rundy, zrozumiałości i balansie od ludzi; zamyka pola „po grze testowej” | mały | autor osobiście |
| 7 | Nowy wygląd tylko dla wersji z kroku 5: wnętrze kebaba z ekranami podstawy, podpięte do mapy; opisy i krótka instrukcja ucznia (1 strona) zgodne z nowymi mechanikami | Wersja, którą wolno pokazać klasie | duży | `[mechaniki]` wnętrza, `[mapa]` mapa i pasek |
| 8 | Pakiet nauczyciela w wersji zerowej: scenariusz jednej lekcji i cyklu 3–4 lekcji, tabela mechanik i punktów podstawy „biznesu i zarządzania”, karta pracy, test 10 pytań przed i po, zasady oceniania; do tego serwer z adresem https w UE, konta na pseudonimach, kasyno wyłączone albo widoczne dla nauczyciela | Bez tego nauczyciel nie poprowadzi lekcji, a szkoła nie zgłosi innowacji | średni | `[mechaniki]` szkic z notatek funkcji, autor z nauczycielem |
| 9 | Prawnik albo opiekun prawny: regulamin platformy REVAS, los folderu `revas_26`, treść oświadczeń konkursowych; przełącznik „ikony ogólne” dla wersji pokazywanej urzędom | Najmocniejszy zarzut pozwu leży poza grą i agent go nie naprawi | mały (rozmowa), mały (przełącznik) | autor osobiście; przełącznik `[mechaniki]` |
| 10 | Po pierwszej lekcji: zgłoszenie do „Przedsiębiorczej Młodzieży” (nabór prawdopodobnie w styczniu), wniosek o mikrogrant, polityka prywatności i wzór umowy powierzenia, przegląd dostępności | Druga szkoła, partner do konkursu, pieniądze na serwer | średni | autor osobiście, dokumenty `[mechaniki]` |

## 6. Pomysły warte rozważenia

1. **Test przed i po w samej grze.** Dziesięć pytań o pojęcia (marża, VAT, koszt zatrudnienia) przed pierwszą i po ostatniej rundzie, wynik w eksporcie nauczyciela. Uzasadnienie: jedyny twardy dowód uczenia się, którego nie zbiera prawie nikt w branży (raport szkolny).
2. **Role w drużynie przypięte do miejsc we wnętrzu.** Szef, finanse przy biurku, menu przy ladzie, kadry na zapleczu. Uzasadnienie: każdy uczeń ma zadanie, a nauczyciel może ocenić osobę, nie tylko drużynę.
3. **Raport „lucrum cessans” po rundzie.** Ile zysku uciekło przez kolejkę, brak dań i pomyłki, policzone z danych, które silnik już ma. Uzasadnienie: uczy kosztu alternatywnego i tłumaczy nazwę gry jednym ekranem.
4. **Prognoza przed rundą.** Drużyna wpisuje przewidywany przychód i zysk, a po rundzie widzi różnicę; trafność daje kilka punktów. Uzasadnienie: podstawa programowa wymaga prognozy przychodów i kosztów, a porównanie planu z wynikiem jest gotowym tematem omówienia.
5. **Widok na projektor z trzema pytaniami do omówienia.** Po rundzie gra sama wybiera z danych klasy trzy obserwacje („dwie drużyny podniosły ceny i straciły gości”). Uzasadnienie: badania mówią, że uczenie dzieje się w omówieniu, a nauczyciel bez przygotowania dostaje gotowy materiał.

## 7. Czego nie sprawdziłem

- Gry w przeglądarce ani podglądów wyglądu jako obrazu; z `_robocze/wyglad/*.html` przeczytałem tylko nagłówki i reguły `@media`.
- Pełnego pytestu; liczby testów biorę z raportów. Uruchomiłem tylko jedną grę botów na `main`.
- Pracy kolegi: wiem tylko, że w repo nie ma gałęzi `mapa-…` i odpowiedzi w `WSPOLPRACA.md`. Mógł pracować lokalnie.
- Folderu `revas_26` i pliku `_robocze/etap1/podobienstwa.md` (opieram się na raporcie pozwu).
- Pięciu plików `research_notes` z researchu szkolnego; czytałem tylko raport końcowy.
- Regulaminu i terminów „Zwolnionych z Teorii” 2026/27: wyszukiwanie nic nie zwróciło, daty pochodzą z raportu z 6.11 i były tam oznaczone jako niepotwierdzone.
- Naboru na 2027 do miejskich grantów i do „Przedsiębiorczej Młodzieży”: brak ogłoszeń w wynikach.
- Wymiaru godzin „biznesu i zarządzania” po reformie 2027 i statusu WOS w zakresie podstawowym: piszę z pamięci.
- Cennika REVAS dla szkół średnich i mechaniki „Kawiarenek” Fundacji GPW.
- Kosztów serwera (szacunek) i zachowania gry przy 10 drużynach jednocześnie.
- Szczegółów 14 niezapisanych plików na `mechaniki-a`: widziałem tylko różnice w `banki.yaml` i `klienci.yaml`.
- Statutu szkoły autora w sprawie telefonów i tego, czy nauczyciel-opiekun uczy „biznesu i zarządzania”.
