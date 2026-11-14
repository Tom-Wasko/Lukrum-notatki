# Agent C – panel gracza: stary wygląd, logo marek, nazwa (etap 1)

Najpierw przeczytaj `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\BRIEF_AGENTA.md` (wspólne zasady). Raport zapisz
w `_robocze/etap1/agent_C.md`. Równolegle agent B czyści silnik, dane, API i testy (poza Twoimi), więc nie ruszaj
tamtych plików.

## Twoje pliki (w `lukrum_gra/gra/`)
`panel_gracza/static/**` (bez `vendor/`), `panel_gracza/templates/**`, `panel_mg/templates/**`, `panel_mg/static/**`
(jeśli jest), `konta/templates/**` i test `testy/aplikacja/test_ikony_marek.py`.

## Zadania
1. **Usuń „Stary wygląd (tabele)”.** Chodzi o motyw `stary` w `panel_gracza/static/motyw.js` i wszystkie gałęzie
   `staryWyglad` (i podobne) w `app.js` oraz `zakladki/*.js`: banki (8), inwestycje (5), marketing (7), dostawcy,
   finanse, formy, hr, lokal_wybor, ubezpieczenia, urzad, wspolne, zdarzenia, a do tego reguły CSS tylko dla tego
   motywu i opcję w szablonach.
   - Zostaje gałąź **nowa** (karty). Znika kod rysujący stare tabele i wszystko, co potem nie ma użycia.
   - Gracz, który miał zapisany motyw `stary` (localStorage `lukrum-motyw`), ma dostać domyślny `bok`. `znane()` już to
     robi, sprawdź tylko.
   - Usuń dawny klucz `STARY_KLUCZ = "revas-motyw"` i jego odczyt.
   - Pozostałe motywy (bok, klasyczny, grafik) i obecny wygląd mają działać **bez zmian**.
2. **Nazwa.** We wszystkich szablonach „Levas Kebab” zmień na „LUKRUM” (logo w nagłówku: `<div>LUKRUM</div>` zamiast
   `Levas <br>Kebab`, tytuły „LUKRUM – …”).
   - Stopka w `panel_gracza/templates/panel_gracza/gra.html:22` ma dostać tekst: „LUKRUM – gra edukacyjna. Nazwy
     prawdziwych firm i miejsc oddają realia Lublina, a oferty, ceny i zdarzenia w grze są fikcyjne. Gra nie jest
     związana z tymi firmami.” Odwołanie do WIEDZA_O_GRZE ma zniknąć.
   - To samo zastrzeżenie, krótko, dodaj na stronie startowej (`start.html`) i na `jak_grac.html` w stopce.
   - Teksty w JS: „Levasu”/„w Levasie” (`finanse.js:48`, `podatki.js:83`) zamień na LUKRUM według zasad odmiany
     (LUKRUM się nie odmienia, np. „Główna księgowa LUKRUM”, „Urząd skarbowy w LUKRUM”, czasem lepiej „w grze”).
   - Usuń wzmiankę o Revasie w `styl.css:1` i `:60` oraz w `zakladki/ogolne.js:344`; komentarz ma opisywać, co robi kod.
   - Końcowy grep `-iE "revas|levas|fitness"` w Twoich plikach ma dać **0**.
3. **Prawdziwe logo marek.** W `zakladki/ikony_marek.js` obiekt `LOGA` (od linii ok. 80) rysuje uproszczone, ale
   rozpoznawalne znaki prawdziwych firm (Biedronka, Lidl, banki, IKEA…). Logo są chronione, a nazwy zostają.
   - Usuń `LOGA` całkiem.
   - Dla każdej z tych firm daj w `WLASNE` **własną, ogólną ikonę branżową** w stylu istniejących `WLASNE` (24×24,
     kreska `currentColor`). Ma nie przypominać znaku firmy: bez jej barw, kształtu znaku i liter. Dyskont/market ma
     koszyk, hurtownia magazyn/paletę, bank budynek z kolumnami, sklep z wyposażeniem dom/narzędzie, market budowlany
     młotek. Ikony mogą się powtarzać w obrębie branży.
   - Pozostaw działanie `ikonaMarki()` i przedrostka „Konto firmowe: ”.
   - Popraw test `test_ikony_marek.py`, żeby pilnował nowej zasady (żadnych `LOGA`, każda marka z danych ma ikonę
     `WLASNE`). Nie osłabiaj go poza tym.
   - CSS `.logo-marki` usuń, jeśli przestanie być używane.
4. **Kasyno – hasło zawsze.** Agent B ustawia w danych `kod_od_rundy: 1` i nazwę „Pod Złotym Koziołkiem”. Sprawdź
   `zakladki/kasyno.js` (`HASLO = "koziol"`) i miejsce, gdzie łapane jest wpisywanie hasła. Wpisanie „koziol” ma
   **zawsze** otworzyć kasyno: na każdej zakładce, w każdej rundzie, w każdym motywie, także gdy fokus nie jest w polu
   (o ile gra ma kasyno – sprawdź, co przychodzi z API). Jeśli JS ma własną blokadę rundy, usuń ją. Teksty „Złotym Kaflem”
   w JS i szablonach zmień na „Złotym Koziołkiem”.

## Sprawdzenie
- `node --check` każdego zmienionego pliku JS (patrz BRIEF_AGENTA).
- Testy `testy/aplikacja/` (to Twoje pole widzenia: panel, szablony), a na koniec pełne pytest raz.
- **Najwyżej 2 zrzuty:** Dashboard w motywie `bok` oraz Banki albo Dostawcy (widać nowe ikony marek), na grze z
  `gra_pokazowa`. Zrzuty zapisz w `_robocze/etap1/zrzuty/`. Sprawdź w konsoli, czy nie ma błędów JS.
