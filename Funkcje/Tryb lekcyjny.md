# Tryb lekcyjny

- **Stan:** w grze (main, 16.11.2026); do sprawdzenia w klasie
- **Gdzie w grze:** kreator nowej gry (krok 3, „Sposób prowadzenia”), panel mistrza gry (wiersz „Sposób prowadzenia”), pulpit MG, panel i pulpit drużyny (plakietka z terminem)

## Dla ucznia (do instrukcji)
Gra może toczyć się „na żywo” albo w trybie lekcyjnym. W trybie lekcyjnym kilka pierwszych rund przechodzi się razem na lekcji, a kolejne rundy zamykają się same po terminie, więc decyzje można podejmować między lekcjami. Przy nazwie gry widać, do kiedy trzeba wysłać decyzje.

## Zasada działania
- Ustawienie siedzi w `konfiguracja["lekcje"] = {rundy_na_zywo, termin_dni}` (`gry/lekcje.py`); brak klucza oznacza grę na żywo, więc stare gry działają bez zmian. Wartości domyślne i zakresy: `settings.LUKRUM_TRYB_LEKCYJNY` (rundy na żywo 3, zakres 1–6; termin 7 dni, zakres 1–14). Nie ma ich w `dane/`, bo testy czytają zamrożoną kopię danych.
- Rundy do `rundy_na_zywo` nie mają terminu. Od następnej termin to moment otwarcia rundy (`termin_od`) plus `termin_dni`. Harmonogram tygodniowy (`gry/harmonogram.py`), jeśli jest ustawiony, ma pierwszeństwo. Pauza oznacza brak terminu. Zmiana trybu w trakcie gry liczy termin od teraz.
- Rundy po terminie zamyka komenda `manage.py zamykaj_rundy`, którą trzeba uruchamiać na serwerze z harmonogramu zadań. Bez niej widać tylko „Termin minął – zamknij rundę”. Rundy „na żywo” zamykają się też same, gdy wyślą wszystkie drużyny (jak dotąd).
- API: pole `lekcje` przy tworzeniu gry (400 przy złych wartościach), `{"lekcje": {...}|null}` w `POST /api/gry/<id>/prowadzenie`; `zakresy_lekcji` w widoku MG.
- Widoki: kreator (pola liczb ukryte dla „Na żywo”, podsumowanie w kroku 4), panel MG, karta gry na pulpicie MG („Na żywo: runda 2 z 3”, „Między lekcjami, termin …”), chip w panelu gracza („Na żywo, na lekcji” / „Do: <data>” / „Termin minął”) i pasek na pulpicie ucznia.
- Testy: `testy/aplikacja/test_prowadzenie.py` (zakresy, wyliczenie terminu, przebieg rund, zmiana w trakcie, stara gra bez pól, pierwszeństwo harmonogramu).

## Liczby i źródła
| Parametr | Wartość | Pewność | Plik | Źródło |
|---|---|---|---|---|
| rundy na żywo | 3 (1–6) | założenie | `lukrum/settings.py` (`LUKRUM_TRYB_LEKCYJNY`) | domyślnie jedna lekcja na start |
| termin kolejnej rundy | 7 dni (1–14) | założenie | tamże | tydzień szkolny |

## Czego uczy (do planu zajęć)
- pojęcia: planowanie w czasie, terminy i ich konsekwencje, praca zespołowa poza lekcją
- pytanie do omówienia: co zmienia się w decyzjach firmy, gdy ma tydzień na przemyślenie, a nie kilka minut?
- krótkie zadanie dla drużyn: ustalcie, kto i kiedy w drużynie wysyła decyzje przed terminem.

## Do promocji
„Lekcja to start, a gra toczy się dalej między lekcjami.”

## Nawiązanie literackie
Brak.

## Otwarte
Kto uruchamia `zamykaj_rundy` na serwerze i ile tygodni gry na cykl lekcji: [[Do decyzji]]. Wygląd nowych pól kreatora nie był sprawdzony na zrzucie.
