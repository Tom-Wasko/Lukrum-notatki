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

## Granica: co mapa daje mechanikom i odwrotnie

| Sprawa | Kto | Stan |
|---|---|---|
| Lista miejsc na mapie (id, nazwa, dzielnica, współrzędne, rodzaj budynku) | `[mapa]` → plik danych, który czytają mechaniki | propozycja 14.11 niżej |
| Dzielnice jako jednostki popytu (id dzielnicy w danych gry) | wspólnie | do ustalenia |
| Wejście do budynku: mapa wywołuje `otworzWnetrze(idMiejsca)`, a wnętrze ma przycisk „Wróć na mapę” | `[mapa]` wywołuje, `[mechaniki]` rysuje wnętrze | propozycja 14.11 niżej |
| Zdarzenia w parkach (`gra/dane/zdarzenia/parki.yaml`) pokazuje mapa w parkach; `[mechaniki]` dopisują nowe historie z lektur | `[mechaniki]` dane, `[mapa]` rysuje | ustalone przez autora 13.11 |
| Wspólne zmienne kolorów i fontów (jasny/ciemny) | wspólnie, jeden plik CSS | propozycja 14.11 niżej |
| Ikony budynków na mapie a ich wnętrza (spójny styl) | `[mapa]` ikony, `[mechaniki]` wnętrza | do ustalenia |
| Lokale konkurencji i boty na mapie (dane z silnika) | `[mechaniki]` → API, `[mapa]` rysuje | do ustalenia |

### Propozycje `[mechaniki]` z 14.11 (do przyjęcia albo zmiany przez `[mapa]`)
1. **Lista miejsc**: rozszerzamy istniejący `gra/dane/mapa/budynki.yaml`, zamiast zakładać nowy plik. Każde miejsce ma już
   `id`, `nazwa`, `rodzaj`, `strefa`, `opis`. `[mapa]` dopisuje `geo: {lat, lon}` i `adres` (z OSM). Pole `zakladka`
   zastąpi później `wnetrze` (id wnętrza, `null` = budynek bez wnętrza). Id zostają jak teraz (`bank_1`, …). Dzielnica
   to dzisiejsza `strefa`, czyli jednostka popytu. Uwaga: plik jest zmieniany na `mechaniki-a`, dlatego dopiski robimy
   po scaleniu tego PR.
2. **Wejście do środka**: mapa wywołuje `window.lukrum.otworzWnetrze(idMiejsca)`. Wnętrze rysuje się w tym samym oknie,
   bez długiej animacji (decyzja autora), i ma przycisk „Wróć na mapę”, który wywołuje `window.lukrum.wrocNaMape()`.
   Dane wnętrza kebaba poda API `GET /api/wnetrza/…` (gałąź `wnetrza-dane`, w toku).
3. **CSS**: jeden wspólny plik zmiennych `gra/panel_gracza/static/motywy/zmienne.css` (`:root` = jasny,
   `[data-motyw="ciemny"]` = ciemny). Nazwy: `--papier`, `--tusz`, `--akcent`, `--akcent-2`, `--ramka`, `--font-tekst`,
   `--font-szyld`. Mapa i wnętrza biorą kolory tylko stąd. Paletę i kroje wybiera autor przy podglądzie 3.

## Umowy na granicy
<!-- Ustalone rzeczy przenosimy tutaj z „Pytań”. Format: data, strony, ustalenie. -->
- 13.11 `[mechaniki]`: miejsca z [[PLAN_PRZEBUDOWY]], rozdz. 6, to lista wyjściowa stref. Adresy sprawdza `[mapa]` na OSM.

## Pytania
<!-- Format: - [ ] data [strona] → [do kogo]: pytanie. Odpowiedź wpisz pod spodem i odhacz. -->
- [ ] 13.11 [mechaniki] → [mapa]: w jakim formacie dasz listę miejsc (YAML w `gra/dane/mapa/`?) i jak nazwiesz id?
- [ ] 13.11 [mechaniki] → [mapa]: czy mapa ma swój plik CSS z kolorami, czy robimy jeden wspólny?

## Dziennik
<!-- Krótko: data, strona, co weszło (gałąź / PR). Najnowsze na górze. -->
- 14.11 [mechaniki]: `wnetrza-dane` – propozycje klientów ze skutkami, zaczepki WOS ze źródłami (czekają na zatwierdzenie autora), cytaty z lektur. Silnik wnętrz w toku. Propozycje granicy z mapą wyżej.
- 13.11 [mechaniki]: gałąź `wnetrza-dane` – dane bywalców i dymków przy ladzie (`gra/dane/wnetrza/`), bez silnika. Pauza do 14.11, plan w [[Plan na 14.11]].
- 13.11 [mechaniki]: założone repozytorium notatek, ten plik i [[Wygląd]]. Tor A nowych mechanik jest w toku na gałęzi `mechaniki-a`.
