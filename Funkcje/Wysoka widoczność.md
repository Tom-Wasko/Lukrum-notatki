# Wysoka widoczność

- **Stan:** w grze (część wspólna 14.11, PR #3 `wspolne-mapa`: zmienne, fonty, znaki; przełącznik w menu ⚙ działa od 16.11.2026)
- **Gdzie w grze:** ustawienia wyglądu (⚙), obok palet Bar mleczny i Pewex; działa na mapie i we wnętrzach

## Dla ucznia (do instrukcji)
Jeśli słabiej widzisz albo nie rozróżniasz niektórych kolorów, włącz w ustawieniach paletę „Wysoka widoczność”.
Gra ma wtedy mocny kontrast, większe litery, grube ramki i bardzo czytelny krój pisma. Jest wersja jasna i ciemna.
W każdej palecie zysk ma znak ▲, a strata ▼, więc nie musisz rozpoznawać ich po kolorze.

## Zasada działania
- Plik `gra/panel_gracza/static/motywy/zmienne.css`, atrybut `data-paleta="wysoka"` i `data-tryb="jasny|ciemny"` na `<html>`.
  Ustawia go `lukrum.wyglad.ustaw({paleta: "wysoka", tryb})` z `static/lukrum.js`, a przeglądarka zapamiętuje wybór.
- Jasna: białe tło, czarny tekst, ciemnoniebieski akcent. Ciemna: czarne tło, biały tekst, żółty akcent.
  Kontrast wszystkich kolorów tekstu do tła jest co najmniej 7:1 (WCAG 2.2, poziom AAA). Sprawdzone skryptem 14.11:
  najsłabszy kolor ma 8,2:1 (jasna) i 9,4:1 (ciemna).
- `--skala-tekstu: 1.25` (litery o 25% większe), `--ramka-grubosc: 3px`, fokus 4 px, przyciski co najmniej 44 px wysokości,
  podkreślone odnośniki, krój Atkinson Hyperlegible (Braille Institute, licencja OFL) zamiast Oswalda i Alfa Slab One,
  bez tekstur papieru.
- **We wszystkich paletach** (`static/motywy/dostepnosc.css`): klasy `.znak-zysk` ▲, `.znak-strata` ▼, `.znak-uwaga` !,
  `.znak-ok` ✓, `.znak-brak` ✕ oraz wzory `--wzor-strata` i `--wzor-uwaga` do wykresów. Stan nigdy nie jest samym kolorem.
- Przy okazji poprawiony jasny Pewex: akcent `#d4601b` miał 3,1:1, teraz `#a84a0e` ma 4,7:1 (AA).
- `prefers-reduced-motion`: animacje grafik (`.para`, `.neon`, `.sekundnik`, `.hak`) wyłącza `dostepnosc.css`.

## Czego uczy (do planu zajęć)
- pojęcie z WOS / przedsiębiorczości: dostępność cyfrowa; ustawa z 4.04.2019 o dostępności cyfrowej stron i aplikacji
  podmiotów publicznych, Europejski akt o dostępności (od 28.06.2025 obejmuje też część usług firm)
- pytanie do omówienia na lekcji: czy twój kebab jest dostępny dla wszystkich klientów (próg, menu, kasa, strona)?
- krótkie zadanie dla drużyn: włączcie na chwilę wysoką widoczność i znajdźcie w grze jedną rzecz, którą rozpoznaje się
  tylko po kolorze. Zgłoście ją autorowi.

## Do promocji
LUKRUM da się czytać także przy słabszym wzroku i daltonizmie: jeden przełącznik i gra ma kontrast AAA.

## Nawiązanie literackie
Brak (funkcja ma być prosta i bez żartów).
