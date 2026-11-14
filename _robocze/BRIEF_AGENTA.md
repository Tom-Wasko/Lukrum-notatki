# Wspólne zasady dla agentów LUKRUM

- **Projekt.** LUKRUM to przeglądarkowa symulacja biznesowa (Django) o kebabach w Lublinie, dla licealistów. Powstaje
  z gry Levas autora, ale **nie może mieć żadnych śladów gry REVAS** (wzmianek, nazw, artefaktów).
  Repo: `C:\Users\PC\Pulpit\Levas\lukrum\lukrum_gra` (kod w `gra/`). Plan: `C:\Users\PC\Pulpit\Levas\lukrum\notatki\PLAN_PRZEBUDOWY.md` (repo Lukrum-notatki; przeczytaj też `WSPOLPRACA.md` obok).
- **Nazwa LUKRUM.** W tekstach pisz „LUKRUM”, w identyfikatorach `lukrum`. W liczbie pojedynczej się nie odmienia,
  jak „liceum”: „w LUKRUM”, „gra LUKRUM”. Rodzaj nijaki: „LUKRUM liczy”, „LUKRUM powstało”. Często naturalniej jest napisać „gra”.
- **Tylko swoje pliki.** Ruszaj wyłącznie pliki wymienione w zadaniu, bo równolegle pracują inni agenci. Gdy trzeba
  zmienić cudzy plik, opisz to w raporcie, nie zmieniaj. **Nie commituj i nie pushuj**, robi to koordynator.
- **Python:** `PY = C:/Users/PC/Pulpit/Levas/lukrum/lukrum_gra/gra/.venv/Scripts/python`, uruchamiany z `lukrum_gra/gra`.
  - w trakcie: testy dotkniętych plików, `PY -m pytest -q -p no:cacheprovider testy/<plik>`;
  - na koniec: raz pełny `PY -X utf8 -m pytest -q -p no:cacheprovider`, `PY -m ruff check .`,
    przy zmianach yaml także `PY -X utf8 -m silnik.dane sprawdz`;
  - składnia JS: `cp plik.js "$TEMP/t.mjs" && node --check "$TEMP/t.mjs"`.
  - Test `testy/pieniadze/test_kasyno.py::test_mistrz_gry_nie_widzi_klubu` bywa niestabilny w pełnym przebiegu
    (osobno przechodzi). Koordynator to sprawdza, Ty tylko zgłoś, jeśli zachowuje się inaczej.
- **Zasady kodu.** Po polsku, styl i gęstość komentarzy jak obok. W silniku żadnych liczb gry, liczby siedzą w `dane/*.yaml`.
  Parametr w `zalozenia.yaml` ma postać `{wartosc, pewnosc: potwierdzone|skalibrowane|zalozenie, zrodlo}`.
  Testy mechanik czytają `testy/dane_zamrozone/`, a liczb tam nie zmieniaj, chyba że zadanie mówi inaczej. Testów nie
  osłabiaj. Teksty dla gracza pisz neutralnie płciowo, formami bezosobowymi.
- **Oszczędzaj tokeny.** Szukaj grepem i czytaj fragmenty, nie całe duże pliki. Najwyżej 2 zrzuty ekranu. Nie czytaj
  folderów `Levas/levas_gra`, `Levas/_archiwum` ani `Levas/notatki`, chyba że zadanie każe.
- **Zrzuty** (gdy zadanie ich wymaga):
  - serwer z `lukrum_gra/gra`: `PY -X utf8 manage.py graj --port <PORT> --bez-przegladarki` (w tle);
  - grę testową zakładasz `PY -X utf8 manage.py gra_pokazowa` (sprawdź `--help`);
  - zrzut: `CDP_PORT=<CDP> python C:/Users/PC/Pulpit/Levas/lukrum/_robocze/narzedzia/cdp.py URL out.png ["js"...]`.
  Na koniec zatrzymaj serwer. Nie dodawaj do gita `db.sqlite3`, `lokalne.json` ani `zapisy/`.
- **Raport.** Zapisz `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\etap1\<twoja-nazwa>.md`: co zmienione (pliki), które
  testy zmieniłeś i dlaczego, wątpliwości do autora. Odpowiedź końcowa to 5–10 linijek streszczenia.
