# Tryb lekcyjny w panelu mistrza gry (worktree fable-lekcje)

## Co było
- `Gra.termin_od` + `gry/harmonogram.py`: tygodniowy harmonogram zamykania rund, komenda `zamykaj_rundy` (cron) zamyka rundy po terminie;
  `hg.prowadzenie()` zasila panel MG, pulpit MG, panel i pulpit drużyny (chip "Zamknięcie: ...").
- Ustawienia gry: `konfiguracja` (jak `podpowiedzi`), zmiana przez `POST /api/gry/<id>/prowadzenie`.

## Dodane
- `gry/lekcje.py`: `zakresy()`, `popraw()`, `ustawienie()`, `termin()`, `opis()`. Zapis: `konfiguracja["lekcje"] = {rundy_na_zywo, termin_dni}`; brak klucza = na żywo (stare gry bez zmian).
- Wartości domyślne i zakresy (3 / 1-6, 7 / 1-14) w `settings.LUKRUM_TRYB_LEKCYJNY`. Najpierw wpisałem je do `dane/katalog.yaml`,
  ale testy czytają zamrożoną kopię danych (bez tych kluczy), więc cofnąłem – dane i schematy bez zmian.
- Zachowanie: rundy <= rundy_na_zywo bez terminu; od następnej termin = `termin_od` (moment otwarcia rundy) + N dni. Użyty istniejący mechanizm:
  `do_zamkniecia` już nie wyklucza gier bez harmonogramu, więc `zamykaj_rundy` zamyka też rundy lekcyjne po terminie.
  Harmonogram tygodniowy, jeśli ustawiony, ma pierwszeństwo. Pauza: brak terminu. Zmiana trybu w trakcie gry liczy termin od teraz.
- `hg.prowadzenie()` zwraca `lekcje` ({tryb, etap: na_zywo|miedzy, rundy_na_zywo, termin_dni, tekst}) i `termin_minal`.
- API: `lekcje` przy tworzeniu gry (400 przy złych wartościach), `{"lekcje": {...}|null}` w `/prowadzenie`; `zakresy_lekcji` w widoku MG.
- UI: kreator (krok 3, "Sposób prowadzenia", pola liczb ukryte dla "Na żywo", podsumowanie w kroku 4); panel MG: wiersz "Sposób prowadzenia" z linkiem "zmień" (okno), w opisie "Termin minął – zamknij rundę";
  karta gry na pulpicie MG ("Na żywo: runda 2 z 3", "Między lekcjami, termin ...", "Termin minął – zamknij rundę");
  panel gracza: chip "Na żywo, na lekcji" / "Do: <data>" / "Termin minął"; pulpit ucznia: analogiczny pasek.

## Pliki
gry/lekcje.py (nowy), gry/harmonogram.py, api/widoki.py, silnik/gra.py (tylko zapis `konf["lekcje"]` w `nowa`), lukrum/settings.py, panel_mg/widoki.py,
panel_mg/templates/panel_mg/lista.html, panel_mg/static/mg/{mg,pulpit}.js, panel_gracza/static/{app,pulpit_ucznia}.js, testy/aplikacja/test_prowadzenie.py.

## Testy
Dopisane w `test_prowadzenie.py`: zakresy i domyślne, wyliczenie terminu, kreator + przebieg rund (na żywo -> między lekcjami -> termin minął -> zamknięcie komendą),
zmiana w trakcie gry i pauza, stara gra bez pól, pierwszeństwo harmonogramu. `test_prowadzenie.py`, `test_panel_mg.py`, `test_api.py` zielone; `ruff check .` czysty; `node --check` 4 plików JS OK.
Nie uruchamiałem pełnego pytest ani przeglądarki (zrzutów nie ma).

## Czego nie ma / uwagi
- Rundy "na żywo" nadal zamykają się też same, gdy wyślą wszystkie drużyny (jak dziś) – nie zmieniałem tej mechaniki.
- Automatyczne zamykanie wymaga działającej komendy `zamykaj_rundy` na serwerze; bez niej widać tylko "termin minął".
- Zmieniony poza listą: `silnik/gra.py` (jedna linia zapisu opcji) i `lukrum/settings.py`.
- Wygląd nowych pól kreatora niesprawdzony na zrzucie (klasy `opcje-p`, `pole` istniejące).
