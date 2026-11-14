# Agent D – poprawki po przeglądzie autora

## 1. Księgowość
Przyczyna: agent C przy usuwaniu gałęzi `staryWyglad` skasował w `zakladki/finanse.js` także funkcję `wyborNiskocennych`
(wybór „zakupy tańsze niż próg: w koszty / amortyzuję”), a `biuro` dalej ją wywoływało (linia ~292) → ReferenceError
przy rysowaniu decyzji zakładki Biuro rachunkowe (grupa Księgowość nie otwierała się w trakcie gry). Wcześniejsze przejście
po zakładkach w grze zakończonej tego nie pokazało (po końcu gry nie ma widoku decyzji), dlatego sprawdzałem w grze w toku
(tydzień 7).
Naprawa: przywrócona `wyborNiskocennych` z `levas_gra` (tylko ta funkcja; teksty bez zmian, brak wzmianek Levasu).
Porównałem też definicje JS stare/nowe: poza tą funkcją nic nie jest usunięte, a nadal używane.
Sprawdzone zakładki (hash, tryb decyzje i wyniki, gra w toku, 0 wyjątków JS i 0 błędów konsoli): wszystkie 53 klucze z `ZAKLADKI`
i menu, w tym biuro, kpir, vat, podatki, raport, bank, harpagon, urzad, sanepid, lokale, licytacje, przejecia, mapa, klienci,
konkurencja, kalendarz, lokal_przeglad, lokal_menu, zaop_*, wnetrze_*, hr_rozwoj, zespol, rynek_pracy, promocje, agencje,
internet, handel, ubezpieczenia, czas_wlasciciela, gielda, lista_bledow, wyslij, dashboard, kasyno, wlasciciel i in.
Uwaga: zakładki ukryte/zakryte (np. kasyno, wlasciciel, przewozy) w bieżącej konfiguracji przekierowują na dashboard.

## 2. Logo marek
`zakladki/ikony_marek.js`: wrócił `LOGA` (z levas_gra) i gałąź `logo-marki` w `ikonaMarki` (LOGA ma pierwszeństwo, WLASNE z
ogólnymi ikonami zostało jako zapas); komentarze neutralne („uproszczone znaki marek (nazwy prawdziwych firm – zastrzeżenie
w stopce)”). `styl.css`: wróciła reguła `.agencja-znak > .logo-marki`. `testy/aplikacja/test_ikony_marek.py` = wersja z levas_gra
(`_ikony` czyta WLASNE i LOGA); `test_bez_znakow_prawdziwych_firm` usunięty. Zrzut: `D_banki.png`.
Do ustalenia (poza moimi plikami): „zastrzeżenie w stopce” – sprawdzić, czy stopka je zawiera.

## 3. Kasyno – przyczyna i decyzja autora
Przyczyna komunikatu „nikt teraz nie otwiera”: lokalne konto `lokalny` jest mistrzem gry, a `api/widoki.py::_bez_klubu`
ukrywało klub (`kas.ukryj`) każdemu MG, więc `S.v.kasyno` było puste. Dane (`kod_od_rundy: 1`) i rundy były w porządku.
Wdrożona decyzja koordynatora: `_bez_klubu` zależy już tylko od `LUKRUM_KASYNO`; `_dla` przy wyłączonym klubie zostawia portfel.
MG widzi klub w widoku firmy (także podglądy rund) i przy zapisie decyzji. Przegląd MG, eksport, CSV i ranking nadal bez klubu.
Test `test_mistrz_gry_nie_widzi_klubu` → `test_mistrz_gry_widzi_klub` (MG widzi klub i portfel w widoku, zestawienia czyste).
Zakładka „Nocna 13” bez zmian. Zaktualizowany opis w `dane/zdarzenia/kasyno.yaml`.

## 4. Szperacz (dodatek)
- `dane/zdarzenia/kasyno.yaml`: `kasyno.rekopis_znaleziony_w_jsonie` (tekst dokładnie jak w poleceniu); `silnik/schematy.py::Klub`:
  pole opcjonalne; `silnik/pieniadze/kasyno.py::widok`: pole `kasyno.rekopis_znaleziony_w_jsonie` w odpowiedzi API.
- `static/app.js`: wpisanie „saragossa” na dowolnej zakładce (poza polami) → toast „Szperacz! Znalazłeś rękopis…”, zapis
  `lukrum-szperacz` w localStorage (kasyno.js: `HASLO_SZPERACZ`, `jestSzperaczem`, `zapamietajSzperacza`), mała ikonka
  (`odznaka-szperacz`, title „Szperacz”) obok nazwy drużyny w nagłówku; po odświeżeniu odznaka zostaje. Brak wpływu na wyniki,
  w zwykłym interfejsie bez wzmianki. Zweryfikowane skryptem CDP.
- Test: `test_rekopis_w_surowych_danych_od_pierwszej_rundy` (dane z żywego pliku, bo testy używają zamrożonej kopii bez pola;
  widok ucznia w rundzie 1 zawiera pole z „koziol” i „saragossa”).
  Uwaga: pole pojawia się, gdy klub jest dla firmy dostępny (tu `kod_od_rundy: 1`), czyli w grze od rundy 1.

## Testy
Zmienione: `test_kasyno.py` (odwrócony test MG, nowy test pola), `test_ikony_marek.py` (powrót do logo).
Wyniki: testy/aplikacja + testy/pieniadze 122 passed (przed dodatkiem Szperacza); test_kasyno 9 passed; `silnik.dane sprawdz` OK.
Pełny pytest i ruff: patrz niżej.
Uwaga środowiskowa: dysk C: był zapełniony (0 MB wolnego) – zrzuty początkowo nie zapisywały się; cdp.py zostawia profile Chrome
`tmp*` w %TEMP% (setki MB każdy; stare z 8–13.11 leżą tam do skasowania przez autora).
