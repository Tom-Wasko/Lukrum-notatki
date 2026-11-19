# Dziennik lidera

Decyzje szefa dzień po dniu i stan prac lidera. Obowiązujące decyzje, tematami: [[Decyzje]] (tam wygrywają przy
rozbieżności). Role: **szef** (autor), **lider** (Claude Opus, główna sesja), **agenci** (podagenci), **majster**
(kolega od mapy), **kapitan** (nauczyciel, opiekun projektu). Zob. [[Sprawozdanie – zespół agentów]], protokół lidera:
`warsztat/LIDER.md`.

## Pytania do szefa
Wszystkie pytania, także z bieżącej pracy lidera, są w jednym miejscu: [[Do decyzji]] (nowe z nocy Fable: §8; gałąź
`fable` w repo notatek i repo `warsztat` na GitHubie: §7). Tu ich nie powtarzamy.

## Stan prac
### 19.11 – stan (zacznij tutaj)
**Zrobione dziś:** krok 6 pulpitu (szablony kart w 4 stylach) sprawdzony i scalony z całą serią `pulpit` do `main` (46cd10c, 798 testów); poprawione nazwy (Biurowiec przy Zana, biuro rachunkowe w Kamienicy rachmistrzów); Park handlowy pod realnym adresem al. Kraśnicka 128; kebab odsyła sprzęt i wystrój do Parku, klientów do Pracowni Analiz, szkolenia do Akademii; kroki zeszytu otwierają teczkę we właściwym wnętrzu (8410066); prośba do majstra o żeton bazaru; sprzątnięte kopie robocze; seria `zeszyt`: treść zeszytu wujka w `dane/zeszyt.yaml` (48 zadań, 23 warunki, „gdzie kupić” z bieżących cen, wizyty zapisywane w grze), scalona do `main` (b990329, 817 testów); decyzje szefa o radiu (Decyzje.md); audyt decyzji szefa i seria `balans-katalogi` (wszystkie brakujące decyzje z 18.11: drobne mechaniki, tydzień 1, D2, higiena, klub w panelu MG, 5 banków) scalona do `main` (e926923, 823 testy, [[balans-katalogi – raport]]).
**Dalej:** lista wolnych nagrań do radia do akceptacji szefa; szyldy i cenniki wnętrz z danych; warianty `*_alt`; gra testowa (tydzień 23.11). Pytanie do szefa: prawdziwe marki banków na starej mapie (`mapa_budynki.js`).

### 18.11 noc – KONIEC DNIA: stan i plan na 19.11 (zacznij tutaj)
**Gałęzie gry (wszystkie wypchnięte na GitHub; `main` = porządki 17.11, bez pulpitu):** `pulpit-ui2` (fa646a6) = pulpit + 33 wnętrza z makiet Fable
+ Kamienica rachmistrzów i Park handlowy + biurowiec Zana z windą + edytor mapy i nowe pozycje żetonów + list „List z decyzjami” + nowy zeszyt, 783 testy.
Kopie robocze w `_robocze/pulpit-ui2`, `pulpit-ui`, `pulpit-mapa`, `pulpit-edytor`, `wnetrza-wdrozenie`, `pulpit-powloka` (po scaleniu usunąć: `git worktree remove`).
Serwer podglądu: `manage.py graj --port 8791` z `_robocze/pulpit-ui2` (gra testowa `Pulpit1b`).
**W toku (WIP-commit zrobiony 18.11 w nocy, niedokończony, niezweryfikowany testami):** agent Sonnet „krok 6” (jednolite szablony kart w 4 stylach, w `_robocze/pulpit-ui2`, BEZ commitu). Jeśli przerwany limitem: `git -C _robocze/pulpit-ui2 status`,
raport `_robocze/pulpit-styl-raport.md`; dokończ tym samym briefem (plan: `Serie/pulpit/pulpit – okna do wyboru stylu.md`, wzorce: `_robocze/szablony-kart/index.html`).
**Zrobione dziś (18.11):** panel postępu + rejestr agentów, prompty NotebookLM i wnioski z nich (`warsztat/LIDER.md` §11–12), pulpit kroki 1–5, wnętrza z makiet, edytor mapy,
alternatywy szablonu kart, METODA.md (szkic), start gry na Pythonie 3.12+, decyzje szefa (Decyzje.md), usunięta gałąź `fable`.
**Plan na 19.11 (kolejność szefa: 4, 2, 3 z pytaniami, 1):**
1. **Merge:** po zakończeniu kroku 6 i zielonych testach scal `pulpit-ui2` do `main` (decyzja szefa), push, wpis dla majstra w `WSPOLPRACA` (zmiany w `mapa/lublin.js`, `mapa/ikony.js`, `dane/mapa/*`); sprzątnij worktree; przegeneruj `INSTRUKCJA.pdf`.
2. **Reszta wnętrz (4):** teksty „Biurowiec przy Zana ▸ Biuro rachunkowe” (silnik/dane: `decyzje.py:716`, `biuro.py:422`, `wnioski.py:166`, `zalozenia.yaml`, `finanse.js`), „Dom reklamy” w README/INSTRUKCJA/`podglad_zetonow.html`,
   kroki zeszytu do ekranów kebaba jako teczka (`wejdzDoKroku`), sprzęt tylko w Parku (ekran „Stanowiska i sprzęt” nie z kebaba), szyldy z danych zamiast tekstu z makiet, żeton `bazar`, Park handlowy: wybierz realny adres (szef: „sam se go postaw”), wersje `*_alt`, 12 żetonów bez `geo` (banki, sprzęt, market, agencje).
3. **Zeszyt wujka (2):** podpiąć treść z `archiwum/fable-17.11/fable-zeszyt/` (48 zadań, odhaczanie w grze, „gdzie kupić” z cen: rozszerzyć widok `v`), samouczek.
4. **Radio (3):** najpierw pytania do szefa (stacje: jazz, klasyczna, polska z PRL, „Lalka”, szum; prowadzący i wtrącenia o grze; nawiązanie do radia z gier postapokaliptycznych własnymi środkami), potem szukanie WYŁĄCZNIE nagrań z domeny publicznej / wolnych licencji (Internet Archive, Musopen, Wolne Lektury; adres źródła + licencja przy każdym; **bez syntezatora**; pliki do gry dopiero po akceptacji listy przez szefa).
5. **Mechanika i gra testowa (1):** seria `balans-katalogi` (Asteroida 328, kasa/lada, szkolenia, lodówka, szafy), cena bota 1,05, potwierdzenie higieny, blokada klubu przez MG, sprzęt i dostawcy od tygodnia 1, `zeszyt-szkic.yaml` do danych; potem termin gry testowej z kapitanem.
6. **Panel postępu i artefakty:** narzędzia claude.ai przestały działać po zmianie konta; po restarcie Claude Code poproś szefa o link i odśwież panel (`warsztat/panel/README.md`); opublikuj edytor mapy (`_robocze/edytor-mapy/index.html`) i szablony (`_robocze/szablony-kart/index.html`) lub zostaw jako pliki lokalne.
7. **Niezałatwione:** regulamin ZwzT (wklejony tekst), rozmowa z kapitanem o AI, repo `warsztat` zostaje lokalne, adresy tymczasowe (biurowiec Zana, kamienica ustawiona przez szefa), 6 notatek NotebookLM do ponowienia po wgraniu plików z `_robocze/notebooklm/`.
**Koszt dnia (tokeny agentów, tys.):** pulpit ok. 1 100, wnętrza 308, edytor 104, szablony 133, porządki ok. 1 400 (17.11); rejestr: `Zespół/Rejestr agentów.md`.

### 18.11 – decyzje szefa, pulpit, panel postępu
- Zrobione: porządki (kroki 1–13, scalone do `main`), decyzje szefa z pytań w okienku zapisane w [[Decyzje]] (ekonomia po dziurach,
  tydzień 1, banki 6→5 bez Solarisa, zeszyt wujka, giełda u majstra, prawo bez zmian, mechaniki poprawiamy teraz), start gry na Pythonie 3.12+
  (`start.bat`, `start.sh`), `METODA.md` (szkic), regulamin ZwzT sprawdzony częściowo, panel postępu na claude.ai (`warsztat/panel/`).
- W toku: seria `pulpit`, krok 1 „powłoka” (agent Sonnet, kopia `_robocze/pulpit-powloka`, plan [[pulpit – plan]]).
- Dalej: `zeszyt`, `balans-katalogi` i poprawki dziur, `budynki`, `wnetrza`; szef: nawigacja i interfejs (pasek, układ paneli).
- Czeka na szefa: pionowy napis LUKRUM i dodatkowe ikony paska, układ paneli we wnętrzach (szkic nie rozstrzyga), termin gry testowej.

*(aktualizuje lider; po przerwaniu albo w nowej sesji zacznij stąd, zob. `warsztat/LIDER.md` §8 i `_robocze/porzadki/STAN.md`)*

### 17.11 – porządki, krok 13 (odchudzenie notatek)
- Zrobione: kroki 1–8 porządków, 4d (kody dawnych serii w danych zastąpione realiami, nowy pomiar dekoru), 13A (Serie,
  Analizy, Funkcje) i 13B (notatki główne, dziennik, `Do decyzji` z pytaniami z nocy Fable). Szczegóły i dowody:
  `_robocze/porzadki/STAN.md`, raporty w `_robocze/porzadki/raporty/`.
- Dalej: recenzent (4e + 9: próbka 30 `zrodlo`, kontrola odsyłaczy) → poprawki → scalenie `porzadki` do `main` w obu
  repo i push (bez pytania, zob. Decyzje) → usunięcie `_robocze/krytyka-wyniki/` po Fable → `plan.md` i `STAN.md` do
  `notatki/Serie/porzadki/` → krok 11 (`METODA.md`, regulamin ZwzT a AI).
- Wyniki nocy Fable (projekt wnętrz, zeszyt wujka, dziury w ekonomii): `archiwum/fable-17.11/fable-wnetrza|fable-zeszyt|fable-dziury/`
  (po porządkach do `Serie/fable`); pytania w [[Do decyzji]], §8. Prompt do okna Fable z `/loop 15m`:
  `archiwum/fable-17.11/fable-wnetrza/prompt-okno-fable.md`.
- Zmiany majstra: `origin/maciex` scalony do `main` gry 17.11 (żetony jako przedmioty); każdą następną serię zaczynamy od
  `git fetch`.
- Nikt nie pracuje w tle poza bieżącym krokiem. Mapa drogowa serii (kolejność prac po porządkach): [[Postęp]], „Teraz”.

## Decyzje szefa
**17.11.2026 (nowy lider)**
- **Push bez pytania** („nie musisz mieć mojej zgody na push”); nadal bez `--force`. Nowe repo na GitHubie i usuwanie
  zdalnych gałęzi: pytać.
- Sesje startują z folderu `Pulpit\lukrum`.
- **Zmiany majstra scalamy do `main` od razu** („scalaj wszystko od majstra od razu”): po `git fetch` lider scala
  `origin/maciex`, sprawdza składnię JS i testy mapy, a push idzie bez pytania.
- **Fable (do 17.11 8:00):** kolejno projekt wnętrz, treść zeszytu wujka, dziury w ekonomii (raporty w `archiwum/fable-17.11/fable-*/`).
  Start na hasło „fable start”; wtedy lider nie stawia nowych agentów.
- **Porządki, pytania 9–11:** pozew, SWOT i podobieństwa do `archiwum/prawne/` (bez gita), w notatkach tylko wnioski bez
  starej nazwy; `testy/dane_zamrozone/` bez zmian; analizy jako `notatki/Analizy/` (repo notatek zostaje w `notatki/`).

**16.11.2026 (noc i wieczór)**
Odpowiedzi szefa na ocenę sposobu pracy, plan porządków i krytykę wnętrz 1–16 (zeszyt wujka, teczka, sprzęt w Parku, kebab
na miejscu i odsyłacze, portfel, 5 banków w pierzei, giełda osobno, Kamienica rachmistrzów, Dom reklamy, własne wnętrza
dla żetonów, redakcja, krój odręczny, „Co tu zrobisz”, tylko komputer), układ folderów, terminy, jawność AI i pozostałe
są w [[Decyzje]] (sekcje „Projekt”, „Sposób pracy i repozytoria”, „Pieniądze”, „Biura rachunkowe”, „Katalogi i wystrój”,
„Mapa i miejsca”, „Pulpit i wnętrza”, „Lekcje”) i w [[Wygląd]]. Zadania z tych decyzji: [[Postęp]]. Treść krytyki:
[[Krytyka wnętrz 16.11]]; wnioski z oceny sposobu pracy: [[Sprawozdanie – zespół agentów]] i [[Do decyzji]], §5.

**16.11.2026 (dzień)**
- Nazwy robocze: autor to **szef**, główna sesja to **lider**. Kolega od mapy to **majster**, nauczyciel to **kapitan**.
- Szef czyta pliki zespołu przed commitem. Fable dostępny do 17.11 8:00. Noc 16/17.11: dwa agenty Fable tylko czytały
  (plan porządków, krytyka wnętrz); rano szef wybrał.
- Kolejność: sposób pracy zespołu, porządek w `lukrum/`, gra etapami; bez terminu; krytykę wnętrz robi świeży recenzent.
- Git: lokalny `main` gry (71 commitów: Fable + maciex) wypchnięty, 740 testów; scalone gałęzie zdalne usunięte.
- Biura i agencje w osobnych budynkach, pulpit z mapą na cały ekran i lista wujka: [[Decyzje]].

## Wybory lidera
Poziom myślenia agentów, limit równoległych agentów i zasady rozdzielania pracy: `warsztat/LIDER.md` (§2 i §4). Agenci
nie tworzą własnych podagentów. Przerwanych agentów wznawiamy przez `SendMessage`, nie od nowa. `AGENTS.md` repo gry to
krótki przewodnik dla każdego agenta; protokół lidera jest osobno w `warsztat/`, bo agenci go nie potrzebują.
Własne definicje agentów leżą w `warsztat/` i są instalowane do `.claude/agents/` skryptem `zainstaluj.ps1`.
