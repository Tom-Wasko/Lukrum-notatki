# zeszyt – raport: treść zeszytu wujka w danych (19.11)

Brief: [[zeszyt – brief treść]]. Wykonawca: Sonnet (166 tys. tokenów, 28 min). Dokończenie (pełne testy, commit, raport): lider.

## Co weszło
- `dane/zeszyt.yaml` – 18 stron tygodni (48 zadań), zadania stałe, słownik 23 warunków, 9 stron „gdzie kupić” z szablonami
  liczb; bez pojęć z WOS; żetony poprawione (`kamienica_rachmistrzow`, `biurowiec_zana`), sklep ze sprzętem „Konstruktorzy T&K”.
  Walidacja w `silnik.dane sprawdz` (schemat w `silnik/schematy.py`).
- `api/zeszyt.py` – zeszyt bieżącego tygodnia i liczby „gdzie kupić” (najtańsi dostawcy, sprzęt, banki, biura) do `v.zeszyt`.
- Wizyty zapisuje gra: `Runda.zeszyt` (migracja 0008), `POST /api/gry/<id>/zeszyt/<firma>/wizyta` (`api/wizyty.py`),
  wołany przy wejściu do wnętrza (`swiat/swiat.js`). MG oglądający drużynę i gra zakończona – bez zapisu.
- `pulpit/zeszyt-warunki.js` – wszystkie warunki w jednym miejscu; `zeszyt.js` i `wujek.js` czytają treść z `v`.
- Testy `testy/aplikacja/test_zeszyt.py` (19): kompletność warunków, żetony, elementy harmonogramu, funkcje, ekrany, endpoint.

## Decyzje wykonawcy
`kampania_trwa: internet` = `stan.internet` albo kampania agencji internetowej; `danie_specjalne` z `v.zeszyt.specjalne`;
zadanie bazaru otwiera scenę `bazar` (wizyta); pole „gdzie” = nazwa budynku z mapy; ceny w formacie „zł / opakowanie”.

## Do zrobienia później
- Zrzut zeszytu na tygodniu 1 nie powstał (kopia bez migracji i konta) – szef obejrzy w grze.
- Wygląd tabeli sprzętu na stronie „Gdzie co kupić” (CSS poza zakresem).
- Żeton bazaru czeka na majstra (`WSPOLPRACA.md`, 19.11).
