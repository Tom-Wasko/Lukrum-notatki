# PIP, zmiana biura, przejęcie debetu: widok w panelu

## Co było
- PIP: silnik liczy i losuje, wynik trafia do `wyniki.pip` i do wniosków (wnioski.py). W hr.js nie było nic (ani ostrzeżenia, ani wyniku).
- Biuro: opłata liczona w silniku (`oplata_zmiany`), panel jej nie pokazywał.
- Debet: komunikat `debet_przy_zmianie` był w wynikach banku, ale JS go nie wyświetlał. Przed zmianą nic nie ostrzegało.

## Dodane (worktree fable-pip/gra)
- `api/prezentacja.py`: `_pip()` i `v["pip"]` (zasady z danych, osoby jak etat: tygodnie po tej rundzie, godziny, flaga `ryzyko`); `v["banki"]["przejecie_debetu"]` ({debet, gotowka, oplata} albo None).
- `silnik/ksiegowosc/biuro.py` (`widok`): `oferty[].oplata_zmiany` (per pakiet) oraz `ostatnie_biuro`. To jedyna zmiana w silniku, tylko pola widoku.
- `hr.js`: pigułka `znak-uwaga` przy osobie na kafelku obsady, pasek ostrzeżenia nad obsadą, tekst w profilu pracownika; w wynikach zespołu komunikat z karą (`znak-strata`) albo informacja, że kontroli nie było.
- `finanse.js` (biura): wiersz „Opłata za przejście do tego biura” na karcie każdego innego biura (po pierwszym wyborze) i komunikat z kwotą po wyborze. Pakiet jak w silniku: z decyzji tylko gdy wchodzi od razu.
- `banki.js`: na kartach innych banków (po „Zmień bank konta”) informacja o spłacie z gotówki albo przejęciu z opłatą; gdy limit banku < debet, ostrzeżenie `znak-strata` o debecie ponad limit. Komunikat silnika w wynikach banku.
- Test: `testy/aplikacja/test_widok_pip_biuro_debet.py` (5 testów). Przeszły też test_biuro, test_biuro_14_11, test_kontrola_pip, test_zmiana_banku_z_debetem. `ruff check .` czysto, `node --check` ok dla 3 plików JS.

## Wątpliwości
- Komunikat po wyborze banku jest tylko w ostrzeżeniu na karcie przed kliknięciem i w wynikach po przeliczeniu. Nie ma osobnego podglądu po kliknięciu.
- Pasek PIP nad obsadą pokazuje tekst pierwszej zagrożonej osoby (liczby tygodni mogą się różnić między osobami; szczegóły w profilu).
- „Mniej godzin” jako rada: gracz nie ma bezpośredniego suwaka godzin, realnie działa umowa o pracę.
- Pełnego pytest i zrzutów nie robiłem.
