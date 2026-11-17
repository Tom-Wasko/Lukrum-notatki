# LUKRUM – notatki

Notatki projektu LUKRUM: edukacyjnej symulacji biznesu (kebab na mapie Lublina) dla liceów, na lekcje WOS i konkurs
„Zwolnieni z Teorii”. To sejf Obsidiana i prywatne repozytorium `Tom-Wasko/Lukrum-notatki`, wspólne dla autora
i majstra (mapa). Kod gry jest w repozytorium `Tom-Wasko/Lukrum` (lokalnie `../gra`).

## Spis

| Notatka | Co w niej jest | Kto pisze |
|---|---|---|
| [[Plan]] | cel, etapy, role, folder projektu | lider |
| [[Postęp]] | zadania, kolejność prac i stan etapów (jedyna lista zadań projektu) | lider po każdej serii |
| [[Decyzje]] | obowiązujące decyzje autora, tematami | lider, po decyzji autora |
| [[Do decyzji]] | **tylko** sprawy otwarte i pytania do szefa, z wariantami | lider i agenci (gdy brief każe) |
| [[Wygląd]] | obowiązujący wygląd: styl, palety, kroje, wnętrza, pulpit | lider |
| [[Mapa]] | strefy, zespoły budynków, spis elementów mapy (odświeżany z danych gry) | obie strony |
| [[Nawiązania literackie]] | zasady i lista nawiązań; banki: [[Banki z lektur]] | lider |
| [[WSPOLPRACA]] | tablica mapa ↔ mechaniki: zasady, umowy na granicy, dziennik | obie strony, **czytać przed pracą** |
| `Funkcje/` | jedna notatka na funkcję gry wg szablonu `../warsztat/szablony/notatka-funkcji.md`; baza do instrukcji, planów zajęć i promocji | agenci, gdy brief każe |
| `Zespół/` | [[Dziennik lidera]] (decyzje szefa dzień po dniu i „Stan prac”; pytania są w [[Do decyzji]]) | lider |
| `Analizy/` | krytyki, sprawozdania i wnioski z datą, m.in. [[Sprawozdanie – zespół agentów]]; indeks [[Analizy]] | lider |
| `Serie/` | plany i raporty serii prac; indeks [[Serie]] | lider i agenci |
| [[Historia]] | kronika prac | lider, przy zamknięciu serii |

## Zasady tego repozytorium
1. **Jeden temat, jedna notatka.** Zanim założysz nową, sprawdź spis. Nie zakładamy notatek z datą w nazwie
   („Plan na…”, „Wnioski z…”): bieżące rzeczy idą do notatki tematu, a po zamknięciu jedna linia do [[Historia]].
2. **Stan obecny osobno od historii.** Notatka tematu mówi, jak jest teraz. Jak do tego doszło, mówi [[Historia]]
   i historia gita.
3. **Sprawa otwarta żyje tylko w [[Do decyzji]].** Po decyzji znika stamtąd i trafia do [[Decyzje]] albo notatki tematu.
4. **Bez plików roboczych.** Briefy, raporty agentów, pomiary i zrzuty nie należą do notatek. Raporty i plany serii mają tu jedno miejsce
   (wyjątek: folder `Serie/`, zob. [[Serie]]), rzeczy tymczasowe w `../_robocze/` u autora.
5. **Nic z innych gier biznesowych:** żadnych nazw, wzmianek ani porównań.
6. Przed pracą `git pull`. Commity w imieniu autora tylko jako Tom-Wasko, bez dopisków o asystentach AI.
7. Agenci zmieniają notatki tylko wtedy, gdy każe im to brief.

## Gdzie co jest poza notatkami
- Kod gry, instrukcja dla graczy i mistrza gry, dokumentacja techniczna: `../gra/`.
- Surowe materiały (briefy, logi, zrzuty, pliki z dawnych serii) leżą lokalnie w `../archiwum/`, poza gitem; spis w `../archiwum/LEGENDA.md` (tam też pliki wycofane z tych notatek: `archiwum/notatki-wycofane/`).
- Sposób pracy zespołu, szablony i definicje agentów: `../warsztat/` (osobne repozytorium szefa; majster ma własne narzędzia).
