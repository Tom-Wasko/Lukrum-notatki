# Plan LUKRUM

Cel, etapy i podział ról. Zadania, kolejność prac i stan są w notatce [[Postęp]].
Decyzje: [[Decyzje]]. Sprawy otwarte: [[Do decyzji]]. Jak do tego doszliśmy: [[Historia]].

## 1. Cel
LUKRUM to symulacja biznesowa dla liceów razem z programem i planem zajęć, dzięki którym nauczyciel WOS poprowadzi
kilka lekcji o prowadzeniu firmy. Projekt idzie na konkurs „Zwolnieni z Teorii” oraz przez Urząd Miasta Lublin
i kuratorium (tym zajmuje się autor).

Wymagania:
1. **Gra własna od początku do końca.** Mechaniki, liczby, nazwy i wygląd są nasze i opisane realiami: prawo, rynek,
   Lublin. Nic z innych gier biznesowych.
2. **Nazwa LUKRUM.** Od łac. *lucrum*, czyli zysk, a „Lu” to ukryty Lublin. Na lekcję WOS jest bonus:
   *lucrum cessans* (utracone korzyści, art. 361 § 2 k.c.).
3. **Gra na mapie Lublina** z płynnym przybliżaniem: miasto, dzielnica, budynek i jego wnętrze. Miejsca na mapie
   zastępują zakładki i menu.
4. **Nawiązania literackie** rozsiane po grze ([[Nawiązania literackie]]).
5. **Komputery i telefony.** Trzy palety, w tym wysoka widoczność ([[Wygląd]]).

## 2. Etapy

| Etap | Co | Stan w skrócie (szczegóły tylko w [[Postęp]]) |
|---|---|---|
| 1 | Gra pod nową nazwą, czyste repozytorium, nowa dokumentacja | zrobione 13.11 |
| 1½ | Wygląd: styl, palety, kroje, grafiki wnętrz | ustalone i wdrożone 14–16.11, przegląd autora |
| 2 | Mapa Lublina z OpenStreetMap, wejście do budynków | zrobione 15–16.11, poprawki w toku |
| 3 | Wszystkie miejsca z własnymi wnętrzami, nawiązania, boty na mapie | w toku: pełne wnętrze ma kebab |
| 4 | Lekcje: scenariusze, zestawy funkcji, gra testowa w klasie | projekt scenariuszy i tryb lekcyjny gotowe |
| 5 | Audyt i publikacja | do zrobienia |

**Mechaniki** idą obok etapów (tor A zrobiony, z toru B część). Stan i lista zadań: [[Postęp]].

**Teraz** i kolejne serie: [[Postęp]], „Teraz”. **Czego brakuje** (lekcja 45 minut, przewodnik nauczyciela, podstawa
programowa, serwer, RODO, gra próbna, zgłoszenie do konkursu, nazwa w UPRP) ma właścicieli: zadania w [[Postęp]]
(etapy 4 i 5), pytania w [[Do decyzji]] (§1 i §5). Priorytety z analizy SWOT: [[Pozew i SWOT – wnioski]].

## 3. Kto co robi
- **Mapa** (dane z OpenStreetMap, silnik mapy, żetony, pasek skrótów): majster ze swoimi agentami.
- **Mechaniki i wnętrza** (silnik gry, dane, balans, ekrany w budynkach, teksty): autor z zespołem agentów.
- Tablica wymiany między stronami: [[WSPOLPRACA]].
- **Kapitan:** nauczyciel, opiekun projektu.
- Role i zasady zespołu (szef, lider, agenci): `../warsztat/ZESPOL.md`, [[Dziennik lidera]].

## 4. Folder projektu
```
lukrum/                 folder główny u autora, poza gitem
  CLAUDE.md, .claude/   start sesji; definicje agentów instalowane z warsztatu
  gra/                  repozytorium Tom-Wasko/Lukrum: tylko gra (kod, instrukcja, dokumentacja techniczna)
  notatki/              to repozytorium: plan, decyzje, Funkcje/, Serie/ (raporty serii), Analizy/ (krytyki, sprawozdania), Zespół/
  archiwum/             surowe materiały, tylko lokalnie, poza gitem (spis w LEGENDA.md)
  warsztat/             osobne repozytorium: sposób pracy zespołu, szablony, definicje agentów, narzędzia
  _robocze/             kopie robocze agentów; nic trwałego
```
