# Sprawozdanie: jak prowadzić zespół agentów (16.11.2026)

Dla szefa. Research zrobił agent Sonnet (18 wyszukiwań, źródła pobrane 16.11), wnioski i decyzje opisał lider.
Wynik: nowy `AGENTS.md`, protokół lidera `dokumentacja/zespol/LIDER.md` (repo gry) i definicje agentów w `lukrum/.claude/agents/`.

## Najważniejsze wnioski ze źródeł
1. **Agenci są drodzy.** Według Anthropic agent zużywa ok. 4 razy więcej tokenów niż zwykły czat, a system wieloagentowy
   ok. 15 razy więcej. Opłaca się przy pracach równoległych, długich wynikach (testy, przeszukiwanie) i świeżej recenzji.
   Przy zwykłym programowaniu, gdzie kroki zależą od siebie, często taniej jest zrobić to samemu. ([Anthropic, multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system), [Claude Code best practices](https://code.claude.com/docs/en/best-practices))
2. **Podagent nie widzi rozmowy lidera.** Zna tylko polecenie i plik `CLAUDE.md`. Wszystko, co lider już ustalił (pliki,
   fakty, decyzje), musi być w briefie, inaczej agent odkrywa to drugi raz za nasze tokeny. ([subagenci](https://code.claude.com/docs/en/sub-agents))
3. **Dobry brief:**
   - cel;
   - konkretne pliki;
   - granice („czego nie ruszać”);
   - kryterium ukończenia ze sprawdzalną komendą;
   - format raportu.

   Mgliste polecenia dawały u Anthropic zdublowaną pracę i luki. ([multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system))
4. **Model do zadania:**
   - Haiku do prostych, masowych rzeczy;
   - Sonnet do większości kodu;
   - Opus do trudnych decyzji.

   Układ „Opus lider + Sonnet wykonawcy” wypadł w teście Anthropic o 90% lepiej niż sam Opus. ([koszty Claude Code](https://code.claude.com/docs/en/costs))
5. **Równolegle 3–5 agentów**, przy kodzie najlepiej z rozłącznymi plikami albo w osobnych kopiach (worktree). ([Cognition: Don't build multi-agents](https://cognition.com/blog/dont-build-multi-agents))
6. **Plik zasad krótki** (poniżej 200 linii): tylko to, czego nie widać w kodzie, czyli komendy, pułapki i decyzje.
   Rzadkie procedury idą do osobnych plików czytanych na żądanie. ([best practices](https://code.claude.com/docs/en/best-practices), [agents.md](https://agents.md))
7. **Kontynuacja zamiast nowego agenta.** Poprawka wysłana do tego samego agenta korzysta z jego kontekstu i cache.
8. **Wyniki do plików, do lidera tylko streszczenie.** Długie logi i testy zawsze przycięte.
9. **Cache:** zmiana modelu w trakcie sesji i kompakcja unieważniają cache. Model wybieramy na początku sesji. ([prompt caching](https://code.claude.com/docs/en/prompt-caching))

Zastrzeżenie: liczby 4×, 15× i 90% pochodzą z badania Anthropic nad wyszukiwaniem informacji, nie nad programowaniem.

## Co znalazłem u nas
- **W projekcie nie było żadnego `CLAUDE.md`.** Claude Code wczytuje sam tylko `CLAUDE.md`, nie `AGENTS.md`. Dlatego
  agenci nie znali zasad, dopóki brief ich nie powtórzył, a każdy brief je powtarzał. Teraz `lukrum/CLAUDE.md` dołącza
  `AGENTS.md` automatycznie.
- Stary `AGENTS.md` był opisem dla każdego, bez zasad „jak wykonać zadanie”. Nowy mówi agentowi: brief to cały zakres,
  nie twórz własnych plików, oddaj dowód, raport w stałym formacie.
- Wspólne zasady wykonawcy siedzą teraz w definicjach agentów (`zwiadowca` Haiku, `wykonawca` Sonnet, `recenzent` Sonnet),
  więc lider nie musi ich wpisywać do każdego briefu.
- Noc Fable 15/16.11 pokazała, że swoboda bez listy plików wyjściowych daje bałagan (wiele raportów, planów i zrzutów
  w różnych miejscach). Nowe zasady: tylko wskazane pliki, robocze rzeczy w `_robocze/`.

## Nowy sposób pracy w skrócie
**szef** decyduje → **lider** pyta (maks. 4 pytania naraz, z rekomendacją), pisze plan i briefy → **agenci** wykonują
po jednym briefie → lider sprawdza dowody i diff, scala po akceptacji szefa → dokumentacja i dziennik.
Gdy szef jest niedostępny, lider zapisuje pytania w [[Dziennik lidera]] i idzie dalej tylko tam, gdzie da się to łatwo cofnąć.

Szczegóły (od 17.11): `warsztat/ZESPOL.md` i `gra/AGENTS.md` (dla każdego agenta), `warsztat/LIDER.md` (dla lidera).

## Do decyzji szefa
Pytania są w [[Dziennik lidera]] → „Pytania do szefa”.
