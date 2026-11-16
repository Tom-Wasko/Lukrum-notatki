# WSPOLPRACA – mapa ↔ mechaniki i wnętrza

Wspólna tablica dla ludzi i agentów obu stron. **Każdy agent, który pracuje na granicy mapy i wnętrz, czyta ten plik
przed pracą.** Dopisuj się z datą i podpisem strony: `[mapa]` albo `[mechaniki]`.

## Kto co robi

| Strona | Ludzie | Działka | Gałęzie w `Tom-Wasko/Lukrum` |
|---|---|---|---|
| `[mapa]` | majster + jego agenci | dane mapy (OSM), silnik mapy, przybliżanie, żetony budynków, pasek skrótów, telefon na mapie | `maciex`, `mapa-…` |
| `[mechaniki]` | autor (Tom-Wasko) + zespół agentów | silnik gry, dane, balans, **wnętrza budynków**, goście przy ladzie, teksty dla graczy | `<seria>`, `<seria>-<temat>` |

## Zasady
1. **Przed pracą:** `git pull` w `Lukrum-notatki`, a w `Lukrum` `git fetch` i przegląd nowych gałęzi.
2. **Scalanie do `main`:** strona `[mechaniki]` scala po akceptacji autora i zostawia wpis w Dzienniku niżej; zmiany z `maciex` scala do `main` od razu (od 17.11). Pull
   request jest potrzebny, gdy zmiana dotyka plików drugiej strony. Strona `[mapa]` wysyła swoje zmiany gałęzią
   albo pull requestem. (zmiana 16.11; wcześniej wszystko szło przez pull request)
3. **Cudze pliki:** zmianę przez granicę zapowiadamy wpisem w „Pytaniach” albo w Dzienniku. Od 16.11 agenci autora
   mogą zmieniać kod mapy, ale każdą taką zmianę odnotowują w Dzienniku, żeby majster wiedział, co się ruszyło.
4. **Gdzie są ustalenia:** plan [[Plan]], decyzje [[Decyzje]], wygląd [[Wygląd]], mapa [[Mapa]], funkcje `Funkcje/`,
   sprawy otwarte [[Do decyzji]].
5. Commity w imieniu autora tylko jako Tom-Wasko, bez dopisków o asystentach AI. Majster podpisuje się swoim kontem.
6. Wygląd: **jasny i ciemny tryb zawsze razem**, kolory tylko przez wspólne zmienne ([[Wygląd]]).
7. Nic z innych gier biznesowych. Prawdziwe marki tylko z zastrzeżeniem ([[Decyzje]], „Marki i prawo”).

## Wspólne pliki

| Co | Gdzie | Uwagi |
|---|---|---|
| Lista budynków: `id`, `nazwa`, `rodzaj`, `strefa`, `miejsce`, `adres`, `geo`, `wnetrze`, `zespol` | `dane/mapa/budynki.yaml` | `[mechaniki]` id i miejsca, `[mapa]` adres i geo |
| Zespoły budynków (`kamienica_bankowa`, `biurowiec_zana`) | lista `zespoly` w `budynki.yaml` | mapa rysuje tylko zespół; adres i geo w zespole |
| 10 stref gry z dzielnicami | `dane/mapa/strefy.yaml` | strefa to jednostka popytu |
| Lokale | `dane/mapa/lokale.yaml` | położenia lokali są dziś w `lublin.json` (do przeniesienia) |
| Schemat pól | `silnik/schematy.py` | po zmianie danych: `python -X utf8 -m silnik.dane sprawdz` w korzeniu repozytorium gry |
| Kolory i kroje: 3 palety × jasny/ciemny | `static/motywy/zmienne.css` | żadnych kolorów na sztywno |
| „Nie tylko kolor”, wysoka widoczność | `static/motywy/dostepnosc.css` | klasy `.znak-zysk`, `.znak-strata`, `.znak-uwaga`, wzory `--wzor-*` |
| Fonty lokalnie | `static/fonty/fonty.css` | Oswald, PT Sans, Alfa Slab One, Atkinson Hyperlegible |
| Wejście do budynku i wybór wyglądu | `static/lukrum.js` | zob. umowy niżej |
| Grafiki SVG | `static/grafiki/` + `README.md` | wspólna kreska dla ikon mapy i wnętrz |
| Dane terenu z OSM | `static/mapa/lublin.json`, skrypt `narzedzia/mapa/pobierz_osm.py` | strona `[mapa]` |

Ścieżki `static/…` liczą się od `panel_gracza/`.

## Granica: co mapa daje mechanikom i odwrotnie

| Sprawa | Kto | Stan |
|---|---|---|
| Lista miejsc (id, nazwa, strefa, miejsce, adres, geo) | `[mechaniki]` id i miejsca, `[mapa]` adres i geo | umowa 14.11, działa |
| Strefy = jednostki popytu | wspólnie | umowa 14.11; od 15.11 strefa = jedna dzielnica (czeka na akceptację autora) |
| Wejście do budynku i powrót | `[mapa]` wywołuje, `[mechaniki]` rysują wnętrze | działa od 16.11 |
| Zdarzenia w parkach (`dane/zdarzenia/parki.yaml`) | `[mechaniki]` dane, `[mapa]` rysuje | ustalone 13.11 |
| Wspólne zmienne kolorów i fontów | jeden plik `zmienne.css` | umowa 14.11, działa |
| Paski: mapa ma swój, wnętrza swój | `[mapa]` / `[mechaniki]` | decyzja autora 14.11; od 16.11 kierunek „mapa na cały ekran, ikony w rogach” ([[Wygląd]]) |
| Krok „teraz” z listu od wujka na mapie | `[mechaniki]` wstawiają regułę CSS, `[mapa]` trzyma `data-id` i `.lm-kafel` | działa od 16.11 |
| Ikony budynków na mapie a ich wnętrza (spójny styl) | `[mapa]` ikony, `[mechaniki]` wnętrza | do ustalenia |
| Lokale konkurencji i boty na mapie | `[mechaniki]` → API, `[mapa]` rysuje | do ustalenia |

## Umowy na granicy
<!-- Ustalone rzeczy przenosimy tutaj z „Pytań”. Format: data, strony, ustalenie. Zmiana nazw: najpierw wpis tutaj. -->
- **Lista miejsc** (14.11): rozszerzamy `dane/mapa/budynki.yaml`, bez nowego pliku. Id zostają (`bank_1`, …).
  Pola: `miejsce` (opis prawdziwego miejsca), `adres` i `geo: {lat, lon}` (wpisuje `[mapa]` z OSM), `wnetrze` (id
  wnętrza; puste = budynek bez wnętrza). `miejsce` wolno poprawić, gdy OSM mówi inaczej.
- **Wejście do środka** (14.11, `static/lukrum.js`): mapa woła `lukrum.otworzWnetrze(id)` → zdarzenie `lukrum:wnetrze`
  `{id}`; dla zespołu id zespołu. Wnętrze woła `lukrum.wrocNaMape()` → zdarzenie `lukrum:mapa`. Wnętrze rysuje się
  w tym samym oknie, bez długiej animacji.
- **Pole `obsluzone`** (w użyciu od 16.11, do formalnego potwierdzenia): słuchacz wnętrz ustawia
  `e.detail.obsluzone = true`. Gdy nikt tego nie zrobi, mapa otwiera zastępczo dotychczasowe okno.
- **Wygląd** (14.11, `static/motywy/zmienne.css`): atrybuty na `<html>` `data-paleta` = `bar` (domyślna) | `pewex` |
  `wysoka` i `data-tryb` = `jasny` | `ciemny`. Ustawia je `lukrum.wyglad.ustaw({paleta, tryb})`, zapis w przeglądarce,
  zdarzenie `lukrum:wyglad` (mapa przerysowuje kolory). Zmienne: `--papier`, `--tusz`, `--akcent`, `--akcent-2`,
  `--ramka`, `--zysk`, `--strata`, `--uwaga`, `--font-tekst`, `--font-szyld`, `--font-gruby`, `--skala-tekstu`,
  `--ramka-grubosc`, `--ognisko`, `--tekstura` oraz `--g-*` dla grafik. Stan nigdy samym kolorem (▲ ▼ !, wzory).
  `data-motyw` zostaje dla starego wyboru układu panelu, nie używać go w mapie.
- **Znacznik na mapie** (16.11): element znacznika ma `data-id` i w środku `.lm-kafel`. Korzysta z tego zaznaczenie
  kroku „teraz”. Nie zmieniać bez wpisu tutaj.
- **Zdarzenia w parkach** (13.11): dane w `dane/zdarzenia/parki.yaml`, pokazuje je mapa w parkach.
- **Zespoły budynków** (14.11): na mapie jeden budynek, w środku hol z szyldami. Zob. [[Mapa]], rozdz. 2.

## Pytania
<!-- Format: - [ ] data [strona] → [do kogo]: pytanie. Odpowiedź wpisz pod spodem i odhacz. Odhaczone po miesiącu usuwamy. -->
- [ ] 16.11 [mapa] → [mechaniki]: pole `geo` w `lokale.yaml` zamiast położeń w `lublin.json`? (propozycja z raportu mapy)
- [ ] 16.11 [mapa] → [mechaniki]: odsyłacze dla twórców w opisach `budynki.yaml` usunąć z danych? Dziś mapa je wycina.
- [ ] 16.11 [mechaniki] → [mapa]: biura rachunkowe i agencje reklamowe dostaną osobne budynki (decyzja autora 16.11).
  Gdzie je postawić na mapie?

## Dziennik
<!-- Krótko: data, strona, co weszło (gałąź / PR / commit). Najnowsze na górze. Wpisy starsze niż miesiąc przenosimy do [[Historia]]. -->
- 17.11 [mechaniki]: **repo gry spłaszczone** (na gałęzi `porzadki`, do `main` po recenzji): wszystko z `gra/` jest teraz
  w korzeniu repo (`silnik/`, `dane/`, `panel_gracza/`, `testy/`, `manage.py`…), `.venv` w korzeniu. Po scaleniu do
  `main` majster: `git pull`, usunąć stare `gra/.venv`, założyć nowe (`start.bat` robi to sam). Ścieżki w
  `narzedzia/mapa/pobierz_osm.py` poprawione (bez członu `gra`). Gałąź `maciex` scalamy do `main` od razu po każdym
  `git fetch`, bez czekania. Notatki: nowe pliki `Plan`, `Decyzje`, `Postęp`, `Mapa`, `Historia`, `Serie/`, `Analizy/`;
  usunięte `LUKRUM.md`, `PLAN_PRZEBUDOWY.md`, `Mapa – elementy.md` (treść w `Mapa.md`).
- 16.11 [mechaniki]: `main` gry = 08268aa: gałąź `fable` (wnętrza, palety, list od wujka i reszta) scalona z mapą
  z `maciex`. Scalone gałęzie zdalne usunięte, `maciex` została.
- 16.11 [mechaniki]: na mapie budynek z bieżącego kroku Planu tygodnia ma obwódkę i plakietkę „teraz”. Zrobione po
  stronie mechanik (`zakladki/wujek.js` wstawia regułę CSS dla `.lm-znak[data-id="…"] .lm-kafel`), bez zmian
  w `static/mapa/*`.
- 16.11 [mechaniki]: słuchacz `lukrum:wnetrze` ustawia `e.detail.obsluzone = true` (`app.js`), więc kliknięcie
  budynku otwiera wnętrze. Sprawdzone automatem: wszystkie 75 znaczników coś otwiera. Jedyna zmiana
  w `dane/mapa/budynki.yaml`: pole `opis` budynku `biura` (cztery obecne biura), bez ruszania `adres` i `geo`.
- 15.11 [mapa]: nowa mapa z OSM: granice dzielnic, żetony, tabliczki, trzy poziomy szczegółów, strefa = jedna
  dzielnica, siedem lokali z nowymi adresami. Raport: [[etap2-mapa – raport]].
- 14.11 [mechaniki]: PR #5 (00fef41): biura, zmiana banku z debetem, kontrola PIP, kadry, pomyłki; silnik dymków
  i propozycji, zestaw ★★★.
- 14.11 [mechaniki]: PR #4 (ddb885c): zespoły budynków (kamienica bankowa, biurowiec przy Zana).
- 14.11 [mechaniki]: PR #3 (0d62000): pola miejsc i stref, sanepid, wspólne zmienne z paletą wysokiej widoczności,
  fonty lokalnie, `lukrum.js`, grafiki wnętrz.
- 14.11 [mechaniki]: PR #2 (9df787f): tor A: wynik 0–1000 pkt, debet, biura rachunkowe, kadry, pomyłki, katalogi.
- 13.11 [mechaniki]: założone repozytorium notatek i ta tablica.
