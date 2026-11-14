# Agent D – lekkie poprawki po przeglądzie autora (etap 1)

Najpierw przeczytaj `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\BRIEF_AGENTA.md`. Kod jest w `lukrum_gra/gra`, repo ma commit `26e4a8c`,
więc `git diff` pokaże Twoje zmiany. Raport zapisz w `_robocze/etap1/agent_D.md`. Nie commituj.

## 1. Zakładka Księgowość w ogóle nie działa (najważniejsze)
Autor zgłasza, że grupa „Księgowość” (`index.js`: biuro, kpir, vat, podatki) nie działa. Prawdopodobnie zepsuło ją usunięcie gałęzi
`staryWyglad` (agent C, pliki `zakladki/finanse.js`, `urzad.js`, `formy.js`, `wspolne.js`…) albo zmiana tekstów w danych (agent B).
- Uruchom serwer (port 8792, CDP 9232) i grę `gra_pokazowa`. Otwórz każdą podzakładkę Księgowości (i dla pewności każdą inną
  zakładkę z menu) i zbierz błędy z konsoli JS. Najprościej skryptem przez CDP: przejdź po zakładkach i wypisz wyjątki.
- Porównaj z wersją sprzed zmian w `C:\Users\PC\Pulpit\Levas\levas_gra\gra` (tylko do odczytu, ten sam kod przed przemianowaniem).
- Napraw przyczynę. Na koniec ma nie być żadnego błędu JS na **żadnej** zakładce. W raporcie podaj listę sprawdzonych zakładek.

## 2. Przywróć uproszczone logo marek
Autor chce z powrotem uproszczone logo prawdziwych firm (obiekt `LOGA` w `zakladki/ikony_marek.js`, klasa CSS `.logo-marki`
i test `testy/aplikacja/test_ikony_marek.py`). Weź je z `levas_gra/gra` (te same pliki). Ikony ogólne dodane przez agenta C
w `WLASNE` mogą zostać jako zapas dla marek bez logo. Test ma wrócić do sprawdzania logo, a `test_bez_znakow_prawdziwych_firm`
usuń. Komentarz przy `LOGA` napisz neutralnie, np. „uproszczone znaki marek (nazwy prawdziwych firm – zastrzeżenie w stopce)”.

## 3. Kasyno: „Pod Złotym Koziołkiem nikt teraz nie otwiera”
Po wpisaniu „koziol” autor dostaje ten komunikat (`static/app.js:442`, gdy `S.v.kasyno?.otwarte` jest fałszywe). Ustal przyczynę
i opisz ją w raporcie. Podejrzenie: autor gra lokalnie (`start.bat`, konto `lokalny` = mistrz gry), a API celowo nie wysyła
mistrzowi gry danych kasyna (`api/widoki.py` ok. linii 100–105, test `test_mistrz_gry_nie_widzi_klubu`). Sprawdź też inne
możliwości (runda 1, brak lokalu, flaga gry). **Nie zmieniaj jeszcze zasady dla mistrza gry**, bo koordynator pyta autora.
Dostaniesz decyzję wiadomością. Jeśli przyczyna jest inna (błąd), napraw ją od razu.

## Sprawdzenie
`node --check` zmienionych JS, testy `testy/aplikacja/` i `testy/pieniadze/`, na koniec raz pełne pytest i ruff. Najwyżej 2 zrzuty
(Księgowość po naprawie, Banki z logo). Zatrzymaj serwer na koniec.
