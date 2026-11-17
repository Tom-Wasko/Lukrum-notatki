# Raporty serii

Każda seria prac ma folder `Serie/<seria>/`: `<seria> – plan.md` (punkty, agenci, pliki), raporty agentów `<seria> – <temat>.md` w formacie
z szablonu raportu (`warsztat/szablony/`) i, gdy zmienia się balans, wyniki pomiarów (tabele `.md` idą po zamknięciu serii do `archiwum/notatki-wycofane/`, w notatkach zostaje tylko wynik w tej tabeli).
Po zamknięciu serii lider dopisuje tutaj jeden wiersz. Nazwy plików są unikalne w całym sejfie, żeby działały odsyłacze Obsidiana. Surowe logi, makiety i zrzuty leżą w `archiwum/` (poza gitem).

## Zamknięte serie

| Seria | Kiedy | Co weszło do `main` | Scalenie | Szczegóły |
|---|---|---|---|---|
| `etap1` | 13.11.2026 | Gra pod nazwą LUKRUM: nowe repozytorium, pakiet `lukrum`, nowa dokumentacja, źródła założeń opisane realiami, zastrzeżenie marek, klub „Pod Złotym Koziołkiem” | 26e4a8c, 895d423 | – |
| `mechaniki-a` (tor A) | 13–14.11 | Wynik 0–1000 pkt, kapitał 50 000 zł, debet, banki ze specjalizacjami, biura S/M/L, kadry wg Kodeksu pracy, pomyłki w szczycie, nowe katalogi | PR #2, 9df787f | wyniki pomiarów niżej |
| `wspolne-mapa` | 14.11 | Pola miejsc i stref (`adres`, `geo`, `miejsce`, `wnetrze`), sanepid, wspólne zmienne wyglądu z paletą wysokiej widoczności, fonty lokalnie, `lukrum.js`, grafiki wnętrz | PR #3, 0d62000 | – |
| `zespoly` | 14.11 | Zespoły budynków: kamienica bankowa, biurowiec przy Zana | PR #4, ddb885c | – |
| `mechaniki-b` + `wnetrza-dane` | 14.11 | Poprawki toru A po przeglądzie (opłata za zmianę biura, zmiana banku z debetem, kontrola PIP, pomyłka przy pustym magazynie); silnik dymków i propozycji gości, zestaw sprzętu ★★★ | PR #5, 00fef41 | – |
| `etap2-mapa` | 15–16.11 | Mapa Lublina z OpenStreetMap: silnik z przybliżaniem, żetony, zespoły, pasek skrótów, pora dnia (strona `[mapa]`) | gałąź `maciex`, 96b3ad6, a0e123d | [[etap2-mapa – raport]] |
| `fable` | 15–16.11 | Miejsca z wnętrzami, palety w całym panelu, list od wujka, sklep meblowy i wystrój lokalu, „Kurier rankingowy”, księga gości, podium, tryb lekcyjny, nowa instrukcja, ceny katalogów od zera, przegląd prawny | 4afdd60, 9ee8192 | [[fable – raport]]; przegląd prawny i pomiary w `archiwum/notatki-wycofane/Analizy/Noc Fable 15-16.11/` |
| `porzadki` | 16–17.11 | Nowy układ `lukrum/` (`gra/`, `notatki/`, `warsztat/`, `archiwum/`), spłaszczenie repo gry, kody serii zastąpione realiami w danych (740 testów), odchudzenie notatek do 41 plików. Plan i stan: [[porzadki – plan]], [[porzadki – stan]], recenzja: [[porzadki – recenzja]]. |
| `fable-wnetrza` | 16–17.11 | Noc Fable: projekt 34 wnętrz (makiety, specyfikacje), treść zeszytu wujka, dziury w ekonomii (zmowa na giełdzie handlu). Wyniki: `archiwum/fable-17.11/`, pytania w [[Do decyzji]] §8. |

## Wyniki pomiarów, na które powołują się dane gry

**Tor A, wynik w punktach** (surowe tabele: `archiwum/notatki-wycofane/Serie/mechaniki-a/pomiary/` i `…/mechaniki-b/pomiary/`) (12 rund, ziarna 7, 11, 23, po przeglądzie 14.11): strategia zrównoważona i naśladowca są
najlepsze, agresywna najsłabsza na każdym poziomie botów. Firma bezczynna dostaje 0–100 pkt. Dobrze obsadzona firma
myli się w ok. 2–4% porcji, przeciążona w ok. 10%.

**Ceny katalogów od zera** (15.11, `archiwum/notatki-wycofane/Analizy/Noc Fable 15-16.11/pomiary/katalogi.md`): składniki ★ = 85%,
★★★ = 132% ceny ★★. Średnia gotówka botów na poziomie łatwym −3,6%. Najwięcej traci strategia premium.

**Wystrój lokalu** (16.11, `archiwum/notatki-wycofane/Analizy/Noc Fable 15-16.11/pomiary/dekor.md`): komplet za 8 300 zł zwraca się średnio
w 10,9 tygodnia przy pełnej konwersji popytu (cel 8–12). W symulacji botów przyrost gotówki to średnio 112 zł na tydzień.

## Nazwy serii
`<seria>` to krótkie słowo bez dat (`porzadki`, `pulpit`, `wnetrza-2`). Gałąź serii nazywa się tak samo, gałęzie
tematów `<seria>-<temat>`.
