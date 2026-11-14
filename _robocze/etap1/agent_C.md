# Agent C – panel gracza (etap 1)

## Zmienione pliki (lukrum_gra/gra/)
- `panel_gracza/static/motyw.js`: usunięty motyw `stary` i `STARY_KLUCZ` ("revas-motyw"). Zapisany `stary` jest teraz nieznany, więc `znane()` daje domyślny `bok`.
- `zakladki/wspolne.js`: usunięte `staryWyglad`.
- Gałęzie starego wyglądu usunięte (zostały karty) w `banki.js` (kafelStary, zakładka Porównanie banków), `dostawcy.js` (kafelInfo, siatka kafli, tabela okna bazy), `finanse.js` (kartaBiura, kafelek „Samodzielnie”), `hr.js` (tabela kandydatów i szkoleń), `inwestycje.js` (stanowiska, udogodnienia), `marketing.js` (kanalStaryHtml, agencjaStaraHtml, siatka promocji), `ubezpieczenia.js` (tabelaPolis), `urzad.js` (tabela higieny), `zdarzenia.js`. Usunięte też nieużywane importy i zmienne po tych gałęziach.
- `styl.css`: usunięte `.zd-wynik-karta`, `.kafel .kg.kg-pelny` (też w `motywy/grafik.css`), `.logo-marki`; komentarze w linii 1 i 60 bez Revasa. `pulpit.css`: `.stopka`.
- Nazwa: wszystkie szablony (`panel_gracza`, `panel_mg`, `konta/_strona.html`) mają „LUKRUM” w logo i tytułach. Stopka w `gra.html` według brief-u, zastrzeżenie dodane w `start.html` i `jak_grac.html`. Teksty w `finanse.js` i `podatki.js` („Główna księgowa LUKRUM”, „Urząd skarbowy w LUKRUM”), komentarz w `ogolne.js` bez Revasa.
- `zakladki/ikony_marek.js`: usunięte `LOGA` i kafelki w barwach marek; `ikonaMarki()` rysuje tylko `WLASNE`. Nowe ogólne ikony branżowe: koszyk (Biedronka, Lidl, Stokrotka), wózek (Auchan), paleta (Makro, Selgros, Eurocash), bank z kolumnami (6 banków), dom (IKEA), młotek (OBI, Castorama, Jula, Leroy Merlin).
- Kasyno: hasło „koziol” działa globalnie (app.js, poza polami formularzy), bez blokady rundy w JS. Zmieniony toast na „Pod Złotym Koziołkiem…”. W JS i szablonach nie było tekstów „Złotym Kaflem”. Zakładka „Nocna 13” i adres zostają.
- Uwaga koordynatora o `otwarte: true` od rundy 1: sama obecność `v.kasyno` niczego nie pokazuje. Zakładka (`widoczna` w kasyno.js) wymaga `zaproszenie` albo hasła w localStorage albo wyników/decyzji. Poprawiłem `ogolne.js:182`: baner klubu na karcie wyników pokazywał się przy `otwarte`, teraz tylko gdy `zaproszenie` nie jest null.

## Test
- `testy/aplikacja/test_ikony_marek.py`: `_ikony()` czyta tylko `WLASNE` (każda marka z danych musi tam mieć ikonę). Dodany `test_bez_znakow_prawdziwych_firm`: brak `LOGA`, `logo-marki`, kolorów `fill="#`/`stroke="#` w ikonach. Nic nie osłabione.

## Sprawdzenie
- `node --check` wszystkich JS: OK. Testy `testy/aplikacja`: 80 przeszło. Pełny pytest i ruff uruchomione na końcu (wynik w odpowiedzi koordynatora).
- Zrzuty: `_robocze/etap1/zrzuty/C_dashboard_bok.png`, `C_banki_bok.png` (nowe ikony banków). Brak błędów JS w konsoli (przegląd 38 zakładek).
- Hasło „koziol” sprawdzone na koncie bez roli MG (MG klubu nie widzi, tak jest w API) w motywach bok, grafik i klasyczny: klub „Pod Złotym Koziołkiem” otwiera się z zakładki Bank. Rola MG konta „lokalny” przywrócona.

## Wątpliwości
- Zakładka nadal nazywa się „Nocna 13” (adres z danych). Do decyzji autora, czy zmienić na nazwę klubu.
- `formy.js` zawiera komentarz o „UF21” i „starym katalogu” (zgodność ze starymi zapisami), bez Revasa.
