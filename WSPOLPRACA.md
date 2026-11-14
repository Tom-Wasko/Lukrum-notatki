# WSPOLPRACA – mapa ↔ mechaniki i wnętrza

Wspólna tablica dla ludzi i agentów obu stron. **Każdy agent czyta ten plik przed pracą nad LUKRUM.**
Dopisuj się z datą i podpisem strony: `[mapa]` albo `[mechaniki]`.

## Kto co robi

| Strona | Ludzie | Działka | Gałęzie w `Tom-Wasko/Lukrum` |
|---|---|---|---|
| `[mapa]` | kolega autora + jego agenci | dane mapy (OSM), silnik mapy, zoom, budynki-ikony na mapie, pasek skrótów, telefon na mapie | `mapa-…` |
| `[mechaniki]` | autor (Tom-Wasko) + Claude | silnik gry, dane, balans, **wnętrza budynków**, klienci przy ladzie, teksty dla graczy | `mechaniki-…`, `wnetrza-…` |

## Zasady

1. **Przed pracą:** `git pull` w `Lukrum-notatki`, a w `Lukrum` `git fetch` i przegląd nowych gałęzi i PR.
2. **Do `main` tylko przez pull request.** Przegląda go druga strona. Nie wysyłamy prosto do `main`.
3. **Nie ruszamy cudzych plików** bez wpisu w „Pytania” i zgody. Granica jest w tabeli poniżej. Jeśli zmiana musi
   przejść przez granicę, najpierw dopisujemy ją do „Umów na granicy”.
4. **Notatki i decyzje lądują w tym repozytorium:**
   - plan: [[PLAN_PRZEBUDOWY]];
   - wygląd: [[Wygląd]];
   - funkcje: `Funkcje/`;
   - sprawy otwarte: [[Do decyzji]].
5. Commity w imieniu autora tylko jako Tom-Wasko, bez dopisków o asystentach AI. Kolega podpisuje się swoim kontem.
6. Wygląd: **jasny i ciemny tryb zawsze razem**. Styl to ilustrowana plansza + czytelność apki + nutka PRL ([[Wygląd]]).
7. Nic z gry Revas. Prawdziwe marki tylko z zastrzeżeniem i z naszymi ikonami ([[PLAN_PRZEBUDOWY]], rozdz. 7).

## Start dla `[mapa]` (15.11 rano)
Wszystko poniżej jest w `main` repo gry (PR #3). Zacznij od `git pull`.

| Co | Gdzie | Co z tym robisz |
|---|---|---|
| Lista miejsc: 43 budynki z `id`, `nazwa`, `rodzaj`, `strefa`, `miejsce` (prawdziwe miejsce w Lublinie) | `gra/dane/mapa/budynki.yaml` | dopisujesz `adres` i `geo: {lat, lon}` z OSM; `miejsce` możesz poprawić, gdy OSM mówi inaczej |
| 10 stref gry z `dzielnice` (prawdziwe dzielnice Lublina) i `serce` (punkt, wokół którego rysujesz strefę, gdy lista dzielnic jest pusta) | `gra/dane/mapa/strefy.yaml` | sprawdzasz granice dzielnic; inne dzielnice to tło miasta (bez stref) |
| Schemat pól (`geo`, `adres`, `miejsce`, `wnetrze`, `dzielnice`, `serce`) | `gra/silnik/schematy.py` | po zmianie danych: `python -m silnik.dane sprawdz` (z folderu `gra/`) |
| Kolory i kroje: 3 palety × jasny/ciemny | `gra/panel_gracza/static/motywy/zmienne.css` | mapa bierze kolory **tylko** stąd (`var(--papier)` itd.), żadnych własnych kolorów na sztywno |
| „Nie tylko kolor” i dodatki wysokiej widoczności | `static/motywy/dostepnosc.css` | klasy `.znak-zysk`, `.znak-strata`, `.znak-uwaga`, wzory `--wzor-*` |
| Fonty lokalnie (Oswald, PT Sans, Alfa Slab One, Atkinson Hyperlegible) | `static/fonty/fonty.css` | podłączasz `fonty.css` w stronie mapy |
| Wejście do budynku i wybór wyglądu | `static/lukrum.js` (już w `gra.html` i `_pulpit.html`) | po kliknięciu budynku wołasz `lukrum.otworzWnetrze(id)`; na `lukrum:wyglad` przerysowujesz kolory |
| Grafiki SVG (ikony, postacie, wnętrza) | `static/grafiki/` + `README.md` | do wglądu, żeby ikony mapy miały tę samą kreskę |

Stara mapa z kratką (`mapa.js`, `mapa_uklad.js`, `uklad.pola` w `miasto.yaml`) działa dalej, dopóki nowa jej nie zastąpi.
Nowy budynek dziś musi mieć pole w kratce swojej strefy (np. `sanepid: [15, 7]`); po przejściu na OSM to wymaganie usuniemy.

## Granica: co mapa daje mechanikom i odwrotnie

| Sprawa | Kto | Stan |
|---|---|---|
| Lista miejsc (id, nazwa, strefa, miejsce, adres, geo) | `[mechaniki]` id i miejsca, `[mapa]` adres i geo | umowa 14.11 |
| Strefy = jednostki popytu, dzielnice tylko do rysowania | wspólnie | umowa 14.11 |
| Wejście do budynku `lukrum.otworzWnetrze(id)` i powrót `lukrum.wrocNaMape()` | `[mapa]` wywołuje, `[mechaniki]` rysują wnętrze | umowa 14.11 |
| Zdarzenia w parkach (`gra/dane/zdarzenia/parki.yaml`) pokazuje mapa w parkach; `[mechaniki]` dopisują nowe historie z lektur | `[mechaniki]` dane, `[mapa]` rysuje | ustalone przez autora 13.11 |
| Wspólne zmienne kolorów i fontów | jeden plik `zmienne.css` | umowa 14.11 |
| Paski: mapa ma swój, wnętrza swój | `[mapa]` / `[mechaniki]` | decyzja autora 14.11 |
| Ikony budynków na mapie a ich wnętrza (spójny styl) | `[mapa]` ikony, `[mechaniki]` wnętrza | do ustalenia |
| Lokale konkurencji i boty na mapie (dane z silnika) | `[mechaniki]` → API, `[mapa]` rysuje | do ustalenia |

## Umowy na granicy
<!-- Ustalone rzeczy przenosimy tutaj z „Pytań”. Format: data, strony, ustalenie. -->
- 13.11 `[mechaniki]`: miejsca z [[PLAN_PRZEBUDOWY]], rozdz. 6, to lista wyjściowa stref. Adresy sprawdza `[mapa]` na OSM.
- 14.11 autor: robimy tylko **10 stref** gry, a nie wszystkie dzielnice. Inne dzielnice to tło. Prawdziwe miejsca, ale bez
  tłoku na Starym Mieście i Krakowskim Przedmieściu. Sanepid: Śródmieście (ul. Karłowicza). Agencja reklamowa: biurowce
  przy Zana (Rury). Park handlowy na Węglinie: dwa sklepy obok siebie (meblowy z własnym wnętrzem i sprzęt kuchenny).
- 14.11 `[mechaniki]`, **lista miejsc**: rozszerzamy `gra/dane/mapa/budynki.yaml` (bez nowego pliku). Id zostają (`bank_1`, …).
  Pola: `miejsce` (opis prawdziwego miejsca), `adres` i `geo: {lat, lon}` (wpisuje `[mapa]` z OSM), `wnetrze` (id wnętrza,
  puste = budynek bez wnętrza; do tego czasu otwiera się stara zakładka z pola `zakladka`). Strefy w `strefy.yaml` mają
  `dzielnice` i `serce`.
- 14.11 `[mechaniki]`, **wejście do środka** (`static/lukrum.js`): mapa woła `lukrum.otworzWnetrze(id)` → zdarzenie
  `lukrum:wnetrze` `{id}`; wnętrze woła `lukrum.wrocNaMape()` → zdarzenie `lukrum:mapa`. Wnętrze rysuje się w tym samym
  oknie, bez długiej animacji (decyzja autora).
- 14.11 `[mechaniki]`, **wygląd** (`static/motywy/zmienne.css`): atrybuty na `<html>` `data-paleta` = `bar` (domyślna) |
  `pewex` | `wysoka` i `data-tryb` = `jasny` | `ciemny`. Ustawia je `lukrum.wyglad.ustaw({paleta, tryb})`, zapis w przeglądarce,
  zdarzenie `lukrum:wyglad`. Zmienne: `--papier`, `--tusz`, `--akcent`, `--akcent-2`, `--ramka`, `--zysk`, `--strata`,
  `--uwaga`, `--font-tekst`, `--font-szyld`, `--font-gruby` (Alfa Slab One), `--skala-tekstu`, `--ramka-grubosc`,
  `--ognisko`, `--tekstura` oraz `--g-*` dla grafik. Stan nigdy samym kolorem (▲ ▼ !, wzory). `data-motyw` zostaje
  dla starego wyboru układu panelu (bok, grafik), nie używać go w mapie. Zmiana nazw: najpierw wpis tutaj.

## Pytania
<!-- Format: - [ ] data [strona] → [do kogo]: pytanie. Odpowiedź wpisz pod spodem i odhacz. -->
- [x] 13.11 [mechaniki] → [mapa]: w jakim formacie dasz listę miejsc (YAML w `gra/dane/mapa/`?) i jak nazwiesz id?
  - 14.11: YAML, istniejący `budynki.yaml`, id bez zmian (umowa wyżej). Jeśli wolisz inaczej, dopisz tutaj.
- [x] 13.11 [mechaniki] → [mapa]: czy mapa ma swój plik CSS z kolorami, czy robimy jeden wspólny?
  - 14.11: jeden wspólny `zmienne.css` (umowa wyżej). Własny CSS mapy tak, ale kolory tylko przez zmienne.
- [ ] 14.11 [mechaniki] → [mapa]: czy `serce` stref bez dzielnic (Politechnika, Dworzec, Zygmuntowskie) wystarczy, czy wolisz własny obrys?

## Dziennik
<!-- Krótko: data, strona, co weszło (gałąź / PR). Najnowsze na górze. -->
- 14.11 [mechaniki]: PR #2 (tor A) scalony. PR #3 `wspolne-mapa` w main: pola miejsc i stref, sanepid, wspólne zmienne CSS z paletą wysokiej widoczności, fonty lokalnie, `lukrum.js`, grafiki z podglądu 4. Start dla [mapa] wyżej.
- 14.11 [mechaniki]: PR #2 poprawiony po przeglądzie (1d8b921): debet od salda końca tygodnia, pomyłki, punkty firmy bezczynnej, okres próbny, własne katalogi. `wnetrza-dane`: silnik dymków i propozycji (0779722).
- 14.11 [mechaniki]: podgląd 4 wnętrz (`_robocze/wyglad/podglad4.html`, grafiki SVG w `_robocze/wyglad/grafiki/`). **Do uzgodnienia z [mapa]:** do wspólnych zmiennych CSS dochodzą `--font-gruby` (gruby krój: szyld, nagłówki, ceny) i kolory grafik `--g-*` (skóra, drewno, metal). Propozycja: `grafiki/zmienne.css`.
- 14.11 [mechaniki]: PR #2 `mechaniki-a` (tor A): wynik 0–1000 pkt, pieniądze z debetem, biura rachunkowe, kadry wg KP, pomyłki w szczycie, nowe katalogi. Czeka na scalenie przez autora. Po scaleniu: `budynki.yaml` z `geo`/`adres` (propozycja wyżej).
- 14.11 [mechaniki]: `wnetrza-dane` – propozycje klientów ze skutkami, zaczepki WOS ze źródłami (czekają na zatwierdzenie autora), cytaty z lektur. Silnik wnętrz w toku. Propozycje granicy z mapą wyżej.
- 13.11 [mechaniki]: gałąź `wnetrza-dane` – dane bywalców i dymków przy ladzie (`gra/dane/wnetrza/`), bez silnika. Pauza do 14.11, plan w [[Plan na 14.11]].
- 13.11 [mechaniki]: założone repozytorium notatek, ten plik i [[Wygląd]]. Tor A nowych mechanik jest w toku na gałęzi `mechaniki-a`.
