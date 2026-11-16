# Dziennik lidera

Decyzje szefa, wybory lidera i pytania czekające na szefa. Najnowsze na górze w każdej sekcji.
Role: **szef** (autor), **lider** (Claude Opus, główna sesja), **agenci** (podagenci), **majster** (kolega od mapy),
**kapitan** (nauczyciel, opiekun projektu). Zob. [[Sprawozdanie – zespół agentów]].

## Pytania do szefa
- [ ] **(16.11) Gałąź `fable` w repo notatek na GitHubie.**
  - Jest już scalona do `main`. Usunięcie zablokował tryb auto.
  - Do usunięcia ręcznie albo za Twoją zgodą.

## Stan prac
*(aktualizuje lider; po przerwaniu albo w nowej sesji zacznij stąd – zob. LIDER.md §8)*

### 17.11 – nowy lider, pierwsze kroki
- Krok 1 (pamięć) i 2 (worktree: tylko `main` w obu repo, nic do naprawy) zrobione.
- Krok 3: `origin/maciex` scalony do `main` repo gry (`a0e123d`, żetony jako przedmioty), testy `swiat`+`aplikacja` 114 passed.
- Nie wypchnięte (czeka na zgodę szefa): repo gry `main` (+3: pliki zespołu i scalenie majstra), repo notatek `main` (+1).
- Krok 4: `_robocze/porzadki/plan.md` ma sekcję (0) „Zmiany po decyzjach 16.11 (noc)” i nowe pytania 9–11 w (h). Czeka na szefa.
- Nikt nie pracuje w tle.
- **Mapa drogowa (17.11, do potwierdzenia przez szefa):**
  1. Porządki (kroki 1–11 planu) ok. 7–9 h pracy, 2 okna limitu, 17–18.11.
  2. Warsztat i panel na claude.ai ok. 2–3 h, 18–19.11.
  3. Seria `pulpit`: teczka, portfel, ramki tylko po najechaniu, „Co tu zrobisz” ukryte; ok. 1 dzień.
  4. Seria `kebab-park`: sprzęt tylko w Parku, kebab odsyła; ok. 1 dzień.
  5. Seria `zeszyt`: zeszyt wujka i krój odręczny; ok. 1 dzień.
  6. Przygotowanie gry testowej ok. 0,5 dnia, a sama gra w tygodniu 23.11.
  7. Seria `budynki`: pierzeja 5 banków, giełda, Kamienica rachmistrzów, Dom reklamy, redakcja; ok. 2 dni.
  8. Seria `wnetrza`: osobne wnętrza dla każdego żetonu, PRL w holach; ok. 2–3 dni.
  9. Dalej: lekcje (etap 4), ZwzT, audyt i prawnik (etap 5), telefon, pilot w szkole do maja 2027.

### Przekazanie dla nowego lidera (16.11 wieczorem) – wykonane 17.11, zostaje jako historia
**Stan na 17.11.2026, noc (przed przeprowadzką):** agenci zakończeni, nic nie działa w tle, kopie robocze gita usunięte.
Szef odpowiedział na **wszystkie** pytania (ocena, plan porządków 1–8, krytyka wnętrz 1–16). Odpowiedzi są niżej
w „Decyzje szefa” (16.11, noc). Pliki zespołu są zacommitowane lokalnie w obu repo, ale **nie wypchnięte**: push za zgodą szefa.

Wyniki do wykorzystania (po porządkach przenieść do `analizy/`, a artefakty do `archiwum/`):
- `_robocze/porzadki/plan.md` + `szkice/`: plan porządków (Fable). **Uwaga:** decyzje 16.11 (noc) go zmieniają, bo
  dochodzą `analizy/` i `archiwum/`, jedno repo z korzeniem `lukrum/`, `Serie/` w notatkach i czyszczenie kodów serii od razu.
- `_robocze/krytyka-wyniki/`: krytyka wnętrz, makiety, zrzuty. Odpowiedzi na (e) są w Decyzjach.
- `_robocze/research-strategia/raport.md` i `_robocze/ocena-sposobu-pracy/ocena.md`.
- `_robocze/pamiec/`: **czysty pakiet pamięci** dla nowej ścieżki.

**Pierwsze kroki nowego lidera:**
1. **Pamięć:** skopiuj całą zawartość `_robocze/pamiec/` (z `MEMORY.md`) do swojego katalogu pamięci. Starej pamięci z poprzedniego folderu nie przenoś.
2. `git worktree list` w obu repo, w razie potrzeby `git worktree repair`. Zapytaj szefa o push plików zespołu.
3. `git fetch` w repo gry: nowe commity majstra na `origin/maciex` (17.11: m.in. „budynki jako przedmioty”).
4. Zaktualizuj `plan.md` porządków o decyzje 16.11 (noc) i pokaż szefowi zmiany. Potem porządki według planu
   (spłaszczenie, `analizy/`, `archiwum/`, `METODA.md`, czyszczenie kodów serii, ponowny pomiar zwrotu z wystroju).
5. Równolegle albo zaraz po: repo `warsztat/` i panel na claude.ai (decyzja: oba teraz).
6. Potem gra etapami: ważne1–3 i punkty krytyki według Decyzji 16.11 (noc).
7. Przypomnij szefowi o rozmowie z kapitanem o metodzie z AI i o grze testowej (może w tygodniu 23.11).

## Decyzje szefa
**17.11.2026 (nowy lider)**
- **Push bez pytania** („nie musisz mieć mojej zgody na push”); nadal bez `--force`. Nowe repo na GitHubie i usuwanie zdalnych gałęzi – pytać.
- Sesje startują z folderu `Pulpit\lukrum` (po przeprowadzce; wcześniejszy wpis o starym folderze nieaktualny).
- **Fable (ostatnie godziny do 17.11 8:00):** kolejno: 1) „projekt wnętrz” (makiety i specyfikacja do serii budynki i wnetrza, `_robocze/fable-wnetrza/`), 2) treść zeszytu wujka (`_robocze/fable-zeszyt/`), 3) dziury w ekonomii (`_robocze/fable-dziury/`, na własnej kopii `main`). Brief: `_robocze/fable-wnetrza/brief.md`, prompt startu z `/loop`: `prompt-startu.md`. Kolejność: najpierw porządki; Fable startuje na hasło szefa **„fable start”**, wtedy lider nie stawia nowych agentów, a działający kończą bieżący krok.
- **Porządki, pytania 9–11:** 9a – pozew, SWOT i podobieństwa do `archiwum/prawne/` (bez gita), w notatkach tylko streszczenie wniosków bez starej nazwy; 10a – `testy/dane_zamrozone/` bez zmian; 11b – analizy jako `notatki/Analizy/`, repo notatek zostaje w `notatki/` (zmienia wybór lidera z 16.11 o korzeniu w `lukrum/`).
- **Zmiany majstra scalamy do `main` od razu** („scalaj wszystko od majstra od razu”): po `git fetch` lider scala `origin/maciex` bez pytania, sprawdza składnię JS i testy mapy, a push zostaje za zgodą szefa.

**16.11.2026 (noc): przegląd oceny sposobu pracy, plan porządków (5–8), krytyka wnętrz (1–16)**

*Ocena (`analizy/` po porządkach, teraz `_robocze/ocena-sposobu-pracy/ocena.md`):*
- **Gra testowa:** jeszcze nie teraz, może w przyszłym tygodniu. Funkcji nie zamrażamy.
- **Terminy (słowa szefa):**
  - ZwzT jest założone, trzeba tam jeszcze wszystko powypełniać;
  - gra testowa może w przyszłym tygodniu;
  - wkrótce rozmowy z kuratorium i urzędem;
  - nadzieja na spotkanie z „grubymi rybami” w przyszłym roku;
  - do maja LUKRUM na testach w jakiejś szkole.

  „Gotowe 17.11 16:00” jest nieaktualne.
- **Jawność AI:** plik `METODA.md` w repo gry („Jak powstał LUKRUM”) + rozmowa szefa z kapitanem + sprawdzenie regulaminu ZwzT pod kątem AI. Commity bez zmian.
- **Warsztat (osobne repo) i panel na claude.ai: oba teraz**, wbrew zaleceniu oceny.
- **Spłaszczenie i pełne porządki:** tak, wbrew zaleceniu oceny.
- **Czytanie:** bez limitów, szef czyta wszystko.
- **Pytania sprawdzające rozumienie gry:** nie („nie obchodzi mnie to”).
- **Pamięć:** czysta. Do nowej pamięci tylko LUKRUM, zasady z `strategia-poprawek` i `agenci-sonnet` wchłonięte do LIDER.md, `uzytkownik`: ZwzT zamiast REVAS.
- **Majster:** mapa „bez ograniczeń” zostaje, ale **lider regularnie sprawdza, czy majster coś wypchnął** (`git fetch`, `origin/maciex`) i ściąga przed pracą.
- **Koszt:** mierzymy (model, przybliżone zużycie, czy weszło do gry) w „Stan prac”. Bez limitu prac „o procesie”.

*Układ `lukrum/` (zmienia wcześniejsze):*
- `notatki/` (pliki projektu) i **`analizy/`** (oceny, research, krytyki, sprawozdania, symulowany pozew, SWOT, raporty z nocy) to **jedno repo** `Lukrum-notatki`.
- **Raporty agentów i plany serii: `notatki/Serie/<seria>/`.**
- **`archiwum/` bez gita**: wszystkie artefakty (podglądy wyglądu 1–4, makiety, stare zrzuty, wyniki nocy).
- Zrzuty z nocy Fable 15/16.11 trafiają do `analizy/` jako ilustracja raportu.
- Zwrot z wystroju (9,8 czy 10,9 tyg.): zmierzyć ponownie przy porządkach i wpisać wynik z datą.
- Stare kody serii (ok. 420) i martwe odsyłacze w danych i kodzie: **wyczyścić od razu przy porządkach** (źródła na realia), a słownik starych kodów do `archiwum/`.

*Wnętrza i pulpit:*
1. **Zeszyt wujka** (wariant B):
   - w środku lista zadań i rozpisane, gdzie co najlepiej kupić;
   - animacja przewracania stron;
   - zamknięty nie znika, tylko wystaje z brzegu ekranu, a na wystającej kartce widać następny krok (C).
2. **Okienko decyzji:** teczka na środku (A), dymki później do cen i promocji.
3. **Sprzęt tylko w Parku handlowym.** Kebab pokazuje stan sprzętu i odsyła, a zeszyt ma ten krok w tygodniu 1.
4. **Kebab:**
   - na miejscu: menu i ceny, promocje, zespół i grafik, wyniki, magazyn, czas i portfel właściciela;
   - odsyła: sprzęt, stoliki i wystrój → Park, zatrudnianie → Miasteczko, szkolenia → Akademia, klienci → Pracownia Analiz.

   **Portfel:** zawsze z boku (mapa i wnętrza), w zastępstwie ikony „kasa”. Pokazuje skrót: gotówkę i stan kebaba. Pełne wyniki rundy zostają w Redakcji.
5. **Banki: pierzeja (B)**, czyli rząd kamienic. **5 banków zamiast 6**, żeby mieściły się w jednym kadrze. Kolory marek zostają, bo szef je lubi, ale mogą być inne niż dziś, dobrane do palet.
6. **Giełda: osobny budynek**, który jest już na mapie majstra (`gielda`).
7. Nazwy: **„Kamienica rachmistrzów”** (biura rachunkowe), **„Dom reklamy”** (agencje, biurowiec z windą).
8. **Dom reklamy:** parter z portiernią i „Twoimi kampaniami”, piętra: drukarnia, radio, eventy, internet. **Budynek „drukarnia” na mapie znika.**
9. **KPiR zostaje w biurowcu przy Zana.**
10. **Miasteczko, detektyw, hurtownie:** na nowej mapie majstra miejsca mają **własne żetony** (`detektyw`, `gielda`, `akademia`, `makro`, `selgros`, `auchan`, `biedronka`, `lidl`…). **Każde ma mieć własne wnętrze**, czyli nie ma wspólnych hal ani holi. Selgros jest osobno od Lidla.
11. **Redakcja:** scena redakcji, gazeta na biurku na pierwszym planie.
12. Hurtownie i sklepy: osobne wnętrza (pkt 10). „Gdzie co najlepiej kupić” jest w zeszycie wujka.
13. Kolory: zob. pkt 5.
14. **Odręczny krój pisma dla wujka:** tak, licencja OFL, polskie znaki. Agent proponuje 2–3, szef wybiera na zrzucie.
15. **Lista „Co tu zrobisz”** znika z widoku. Zostaje ukryta dla czytników ekranu i jako zastępstwo na wąskim ekranie.
16. **Na razie tylko komputer**, telefon później.

**16.11.2026 (pytania z planu porządków)**
- **Spłaszczenie repo gry:** lider ściąga najnowszy `maciex` i robi po swojemu („majster da sobie radę”), a majster dostaje wpis w WSPOLPRACA.
- **Pozew, SWOT, podobieństwa** (dokumenty ze starą nazwą) idą poza `lukrum/`, ostatecznie do `archiwum/prawne/` (decyzja 9a).
- **Historia repo notatek zostaje**, bez nowego repo. Stara nazwa jest w treści plików 6 commitów z 13–14.11
  (`PLAN_PRZEBUDOWY.md`, `WSPOLPRACA.md`, `Do decyzji.md`, `Wnioski Fable 14.11.md`, `_robocze/…`). Po porządkach bieżące pliki są czyste.
- **Raporty agentów i plany serii:** `notatki/Serie/<seria>/` (plan.md + `<temat>.md` + indeks).

**16.11.2026 (20:30)**
- `warsztat/` to **osobne repo git, bez związku z LUKRUM** (zmienia wcześniejsze „bez gita”).
- Panel kontrolny: **tylko strona na claude.ai** (zmienia wcześniejsze „oba warianty”).
- Plan B na wyczerpanie limitu: zapisany w LIDER.md §8.
- Research o strategii pracy szefa z AI, a po pracy Fable ocena tego sposobu pracy.

**16.11.2026 (wieczór, uwagi do plików zespołu)**
- Role: kolega od mapy to **majster**, nauczyciel opiekun projektu to **kapitan**.
- Pytania do szefa **bez limitu liczby**. Narzędzie mieści 4 naraz, więc idą rundami.
- **Układ `lukrum/`:**
  - `gra/` = repo `Lukrum`, tylko gra; obecne `lukrum_gra/` po zmianie nazwy, a `lukrum_gra/gra/` idzie na wierzch repo (spłaszczenie);
  - `notatki/` = repo `Lukrum-notatki`, wszystko o projekcie, w tym raporty, plany serii i dziennik;
  - `warsztat/` = **zwykły folder bez gita**: ogólny sposób pracy zespołu, szablony, definicje agentów, narzędzia i panel. To szablon na kolejne projekty.
- **Panel kontrolny** (projekt poboczny): **oba warianty**, czyli lokalny generator HTML w warsztacie i strona na claude.ai z bazą stanu.
- Szef przenosi `lukrum/` do nowego folderu (`Pulpitukrum`) **17.11 ok. 6:00**, po pracy agentów nocnych, i w nowym folderze startuje nowego lidera.
- Porządki bez ograniczeń: „możesz zmieniać wszystko, jeśli wyjdzie lepiej”.

**16.11.2026**
- Sesje startują z folderu projektu (od 17.11 `Pulpit\lukrum`), bo wtedy działają `CLAUDE.md` i własni agenci.
- Scalenia do `main` po akceptacji szefa, a koledze zostaje wpis w dzienniku WSPOLPRACA. PR tylko przy zmianach w jego plikach.
- Fable jest dostępny tylko do 17.11 8:00 (darmowy okres), potem poza zespołem.
- Szef czyta pliki zespołu przed commitem. Porządki ruszają po jego uwagach.
- Noc 16/17.11: dwa agenty Fable równolegle, oba tylko czytają:
  - plan porządków + szkice scalonych plików → `_robocze/porzadki/`;
  - krytyka wnętrz ze zrzutami i makietami → `_robocze/krytyka-wyniki/`, praca w kopii `_robocze/krytyka`.

  Rano szef wybiera.
- Nazwy robocze: autor to **szef**, główna sesja Claude to **lider**.
- Kolejność:
  1. sposób pracy zespołu (research + AGENTS.md), który szef chce najpierw dopracować;
  2. porządek w całym `lukrum/`;
  3. gra etapami.
- **Bez terminu.** Do gry trafia tylko to, co przejdzie testy.
- **Krytyka wnętrz:** robi ją świeży recenzent (zrzuty, oba tryby), lider streszcza, szef wybiera poprawki. Punkty szefa 1–6 idą od razu.
- **Biura:**
  - biura rachunkowe w osobnej kamienicy z szyldami (jak banki);
  - agencje reklamowe w osobnym biurowcu z windą;
  - biurowiec przy Zana zostaje dla reszty firm.
- **Git:**
  - wypchnąć lokalny `main` repo gry (71 commitów: Fable + maciex) – zrobione, 740 testów przechodzi;
  - usunąć scalone gałęzie zdalne (bez `maciex`) – zrobione.
- **Mapa:** agenci lidera mogą zmieniać kod mapy bez ograniczeń.
- **Notatki:** pełna przebudowa. Scalić i przepisać w czysty układ, a stare raporty Fable streścić i usunąć (historia zostaje w gicie).
- **Pulpit:**
  - mapa na cały ekran;
  - w rogach małe ikony: runda, kasa, „Wyślij decyzje”, lista wujka, ⚙, konto, „Jak grać”;
  - wyniki rundy w budynku Redakcji.
- **Lista wujka:** klik w pozycję przesuwa i przybliża mapę do budynku, a ten pulsuje. Wejście robi gracz sam.

## Wybory lidera
**16.11.2026 (noc)**
- Jedno repo na `notatki/` i `analizy/`: korzeniem repo `Lukrum-notatki` będzie `lukrum/`, a `.gitignore` przepuszcza tylko
  `notatki/`, `analizy/` i siebie. `gra/` (osobne repo), `warsztat/` (osobne repo), `archiwum/`, `_robocze/`, `CLAUDE.md`
  i `.claude/` są pominięte. Majster otwiera `notatki/` jako sejf Obsidiana. Do potwierdzenia przez szefa przy przeglądzie planu.

**16.11.2026 (wieczór)**
- Poziom myślenia agentów (`effort`): zwiadowca `low`, wykonawca `medium`, recenzent `high`, Opus i Fable `high`. Opis w LIDER.md §2.
- Równolegle domyślnie do 5 agentów, w tym do 3 piszących kod (powody w LIDER.md §4: wspólny limit subskrypcji, pełny pytest obciąża komputer, scalanie).
- Agenci nie tworzą własnych podagentów (ograniczenie Claude Code). Rozdziela tylko lider.
- Przerwanych agentów Fable wznowiono przez SendMessage (zachowali przeczytany kontekst), a nie od nowa. Plan porządków dostał nowe decyzje o układzie.

**16.11.2026**
- `AGENTS.md` (repo gry) przepisany na krótki przewodnik dla każdego agenta.
- Protokół lidera osobno w `dokumentacja/zespol/LIDER.md`, bo agenci go nie potrzebują, a każda linia AGENTS.md kosztuje przy każdym starcie.
- Dodany `lukrum/CLAUDE.md`, który dołącza `AGENTS.md`. Wcześniej nie było żadnego `CLAUDE.md`, więc agenci nie dostawali zasad automatycznie.
- Własne definicje agentów w `lukrum/.claude/agents/`, poza repo:
  - kolega ma własny zestaw narzędzi;
  - pliki są małe;
  - w razie potrzeby można je przenieść do repo.
- Raporty agentów w `raporty/<seria>/` (repo gry). Dziennik lidera i sprawozdania w `notatki/Zespół/`, bo czyta je szef.
- Repo notatek: `main` przewinięty do gałęzi `fable` (fast-forward, 4 commity notatek z nocy Fable) i wypchnięty.
