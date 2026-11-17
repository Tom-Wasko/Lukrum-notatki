# Dziennik lidera

Decyzje szefa dzień po dniu i stan prac lidera. Obowiązujące decyzje, tematami: [[Decyzje]] (tam wygrywają przy
rozbieżności). Role: **szef** (autor), **lider** (Claude Opus, główna sesja), **agenci** (podagenci), **majster**
(kolega od mapy), **kapitan** (nauczyciel, opiekun projektu). Zob. [[Sprawozdanie – zespół agentów]], protokół lidera:
`warsztat/LIDER.md`.

## Pytania do szefa
Wszystkie pytania, także z bieżącej pracy lidera, są w jednym miejscu: [[Do decyzji]] (nowe z nocy Fable: §8; gałąź
`fable` w repo notatek i repo `warsztat` na GitHubie: §7). Tu ich nie powtarzamy.

## Stan prac
*(aktualizuje lider; po przerwaniu albo w nowej sesji zacznij stąd, zob. `warsztat/LIDER.md` §8 i `_robocze/porzadki/STAN.md`)*

### 17.11 – porządki, krok 13 (odchudzenie notatek)
- Zrobione: kroki 1–8 porządków, 4d (kody dawnych serii w danych zastąpione realiami, nowy pomiar dekoru), 13A (Serie,
  Analizy, Funkcje) i 13B (notatki główne, dziennik, `Do decyzji` z pytaniami z nocy Fable). Szczegóły i dowody:
  `_robocze/porzadki/STAN.md`, raporty w `_robocze/porzadki/raporty/`.
- Dalej: recenzent (4e + 9: próbka 30 `zrodlo`, kontrola odsyłaczy) → poprawki → scalenie `porzadki` do `main` w obu
  repo i push (bez pytania, zob. Decyzje) → usunięcie `_robocze/krytyka-wyniki/` po Fable → `plan.md` i `STAN.md` do
  `notatki/Serie/porzadki/` → krok 11 (`METODA.md`, regulamin ZwzT a AI).
- Wyniki nocy Fable (projekt wnętrz, zeszyt wujka, dziury w ekonomii): `_robocze/fable-wnetrza|fable-zeszyt|fable-dziury/`
  (po porządkach do `Serie/fable`); pytania w [[Do decyzji]], §8. Prompt do okna Fable z `/loop 15m`:
  `_robocze/fable-wnetrza/prompt-okno-fable.md`.
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
- **Fable (do 17.11 8:00):** kolejno projekt wnętrz, treść zeszytu wujka, dziury w ekonomii (raporty w `_robocze/fable-*/`).
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
