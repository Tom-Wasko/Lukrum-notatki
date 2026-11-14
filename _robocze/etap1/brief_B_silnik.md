# Agent B – czyszczenie silnika, danych i testów (etap 1)

Najpierw przeczytaj `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\BRIEF_AGENTA.md` (wspólne zasady). Raport zapisz
w `_robocze/etap1/agent_B.md`.

## Twoje pliki (w `lukrum_gra/gra/`)
Wszystko, z WYJĄTKIEM: `panel_gracza/static/**`, `panel_gracza/templates/**`, `panel_mg/templates/**`,
`konta/templates/**`, `testy/aplikacja/test_ikony_marek.py`, testów motywu (te ma agent C) oraz `INSTRUKCJA.md`,
`LOGOWANIE_MICROSOFT.md`, `*.bat` (koordynator). Czyli: `silnik/`, `dane/`, `api/`, `gry/`, `konta/*.py`,
`panel_gracza/*.py` i `panel_gracza/management/`, `panel_mg/*.py`, `balans/`, `lukrum/`, `manage.py`,
`pyproject.toml`, `testy/` (z `dane_zamrozone/`).

Lista trafień: `grep -rniE "revas|levas|fitness|siłowni|fruukulele|\bATH\b|\bApex\b|\bVela\b|dashboard r1|gra [ABC] online|[ABC]/[ABC]/[ABC] online"`
(najwięcej: `dane/zalozenia.yaml` 38, `dane/katalog.yaml` 11, te same w `testy/dane_zamrozone/`). Na koniec ten grep
w Twoich plikach ma dać **0**. Słowo „klub” sprawdź ręcznie (zostaje tylko w znaczeniu gry, np. klub sportowy w kalendarzu).

## Zadania
1. **Ślady innej gry.** Usuń każdą wzmiankę o REVAS i jego grach (nazwy drużyn ATH, Fruukulele, Apex, Vela, „gra A/B/C online”,
   „dashboard r1”, „klub fitness”, „jak w REVAS”) z komentarzy, docstringów i pól `zrodlo`.
   - `zrodlo` przepisz realiami, np. „założenie autora: …”, „skalibrowane pomiarami botów (balans/)”, przepis, GUS, cennik.
     Gdy `pewnosc: potwierdzone` opierała się tylko na tamtej grze, zmień ją na `skalibrowane` (liczba dopasowana
     pomiarami) albo `zalozenie`. **Wartości liczb zostają bez zmian.**
   - Komentarz w kodzie przepisz tak, żeby opisywał, co kod robi, bez odwołań do innych gier.
   - To samo w `testy/dane_zamrozone/` (tam też tylko teksty, liczby bez zmian).
2. **Martwy kod trybu „REVAS”** (np. `silnik/gra.py` ok. linii 41 i 56 oraz inne `tryb`/`legacy`, jeśli są). Usuń go, jeśli nic go
   nie używa (sprawdź grepem, także w testach i `api/`). Jeśli jest używany, zmień tylko nazwę na neutralną
   (np. `bez_mapy`) i opisz to w raporcie.
3. **Nazwa gry.** Zamień tekst „Levas” na „LUKRUM” (zasady odmiany są w BRIEF_AGENTA). Popraw opis w `pyproject.toml`
   i komentarz ruff o „kodzie przeniesionym” na neutralny („starszy kod”).
4. **Nazwy własne w katalogach** (`dane/katalog.yaml` i jego kopia w `dane_zamrozone`). Banki MBP Bank, Beauty Bank,
   Euro Biznes Bank, Gaz Bank, IT Bank, Brand Bank, biura rachunkowe Prefix, Plus, Seven, Rachmistrz, Krak, Petra, media
   Radio Fakty, Radio City, Głos Miasta, Newsy Miasta, narzędzie „Panorama Firm” – zmień je na **własne, wymyślone** nazwy
   z lubelskim smakiem. Mają to być nazwy fikcyjne, nie prawdziwe firmy: np. „Bank Pod Bramą”, „Kasa Bystrzyca”,
   „Biuro Rachunkowe Sumator”, „Radio Czechówka”, „Tygodnik Zalew”. Klucze (`id`) zmień tylko wtedy, gdy zawierają
   starą nazwę, i popraw wszystkie odwołania (dane, silnik, testy). Liczby zostają.
5. **Kasyno.** `dane/zdarzenia/kasyno.yaml` i kopia zamrożona:
   - `nazwa: Klub „Pod Złotym Kaflem”` zmień na `nazwa: „Pod Złotym Koziołkiem”` (w tekstach kasyna, gdzie pojawia się
     „Złotym Kaflem”, też na „Złotym Koziołkiem”);
   - `kod_od_rundy: 4` zmień na `1`, z komentarzem: hasło „koziol” otwiera drzwi zawsze, od pierwszej rundy;
   - popraw `testy/pieniadze/test_kasyno.py`: krotka `SLADY` ma „Złotym Kaflem”, zamień ją; test, który ustawia
     `kod_od_rundy = 2`, ma dalej sprawdzać to, co sprawdzał;
   - sprawdź w `silnik/pieniadze/kasyno.py` i `api/prezentacja.py`, czy coś jeszcze nie zamyka drzwi na hasło (np. stan
     funkcji, runda). Hasło ma działać zawsze, gdy gra ma kasyno. Kod JS z hasłem (`kasyno.js`) ma agent C, więc tylko
     opisz w raporcie, czego API od niego oczekuje.
6. Z pozostałymi podobieństwami (wzory, liczby, harmonogram) **nic nie rób**. To decyzje autora.

## Uwaga o testach
W pełnym przebiegu 6 testów pada zależnie od kolejności, a osobno przechodzą (to stan wyjściowy):
`test_kasyno::test_mistrz_gry_nie_widzi_klubu`, `test_harmonogram::test_api_prowadzenie`,
dwa w `test_zdarzenia` (`test_podglad_…`, `test_widok_api`) i dwa ERROR w `test_limity`. Gdy na koniec padają tylko
one, zgłoś to i nie naprawiaj. Gdy masz czas, znajdź przyczynę (AttributeError; prawdopodobnie stan współdzielony
między testami, np. pamięć gier w `gry/serwisy.py` albo ustawienia) i opisz ją w raporcie z propozycją poprawki.

## Dopiski
- Odwołania do `dokumentacja/WIEDZA_O_GRZE.md` (np. `silnik/ksiegowosc/finanse.py`, `silnik/kuchnia/operacje.py`) – tego pliku
  w LUKRUM nie ma. Zastąp je odwołaniem do `dokumentacja/OPIS_GRY.md` albo usuń, a zasadę opisz w komentarzu własnymi słowami.
- Agent C zmienia w szablonach nagłówek „Levas Kebab” na „LUKRUM”, a tytuły stron na „LUKRUM – …”. Jeśli jakiś test
  (`testy/aplikacja/*`) sprawdza stary tekst, popraw test pod nowy (test należy do Ciebie).
