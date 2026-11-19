# zeszyt – brief: treść zeszytu wujka w danych

**Seria:** zeszyt · **Gałąź:** `zeszyt-tresc` (od `main`) · **Kopia:** `_robocze/zeszyt-tresc` · **Agent:** wykonawca (Sonnet)
**Raport:** `notatki/Serie/zeszyt/zeszyt – raport treść.md` (szablon `warsztat/szablony/raport.md`)

## Cel
Zeszyt wujka (`panel_gracza/static/pulpit/zeszyt.js`) dziś bierze listy i kroki z kodu `zakladki/wujek.js` (LISTY, kroki,
BUDYNEK_KROKU, PUNKT_KROKU). Treść ma przejść do danych `dane/zeszyt.yaml` według gotowego szkicu, a odhaczanie zadań ma
liczyć gra.

## Materiał (czytaj tylko to)
- `archiwum/fable-17.11/fable-zeszyt/zeszyt-szkic.yaml` – struktura i treść: 23 warunki, 48 zadań w 18 tygodniach, zadania
  stałe, 9 stron „gdzie kupić” z szablonami liczb. `zeszyt.md` obok to uzasadnienia (czytaj tylko w razie wątpliwości).
- `archiwum/fable-17.11/fable-zeszyt/raport.md` – pytania Fable. Odpowiedzi szefa są niżej.

## Decyzje szefa (nie pytać ponownie)
1. **Odhaczanie zapisuje gra, nie przeglądarka.** Warunki `stan`, `decyzja` i `wyslane` liczy się z `v`. Warunek `wizyta`
   zapisuje serwer: pole JSON w `gry/models.py: Runda` (np. `zeszyt = {firma: [id miejsc]}`), migracja i mały endpoint
   w `api/` wołany przy wejściu do wnętrza (`swiat/swiat.js`). Do `v` trafia lista wizyt bieżącej rundy.
2. **Bez pojęć z WOS** przy zadaniach. Pole `pojecie` usuń z danych.
3. Wujek **poleca sklepy po nazwie** (zostaje tak, jak w szkicu).
4. Sprzęt jest tylko w Parku handlowym (`sprzet_gastro`), a sklep ze sprzętem nazywa się **„Konstruktorzy T&K”**.
   Stanowiska zostają w stolarni. Sprzęt i dostawcy będą odblokowani od tygodnia 1 (zrobi to inna seria). Zostaw
   `zastepstwo` z szkicu, bo zadziała, dopóki element jest zablokowany.
5. Żeton `biura` już nie istnieje, użyj `kamienica_rachmistrzow`. `dom_reklamy` to dziś `biurowiec_zana`. `bazar` nie ma
   jeszcze żetonu (prośba do majstra w `notatki/WSPOLPRACA.md`), więc zadanie z bazarem odsyła tylko do ekranu.

## Zakres
- `dane/zeszyt.yaml` z polami `{wartosc…}` tam, gdzie są liczby gry. Zarejestruj plik w `silnik/dane` tak, żeby
  `silnik.dane sprawdz` go walidował (pydantic).
- `api/prezentacja.py`: do `v` dołóż zeszyt bieżącego tygodnia (tydzień liczony jak w szkicu) i liczby do szablonów
  „gdzie kupić” (najtańsi dostawcy ze składników, ceny sprzętu, banki i biura z bieżących danych).
- JS: `WARUNKI` w jednym miejscu (np. `pulpit/zeszyt-warunki.js`). `zeszyt.js` i `wujek.js` czytają treść z `v`. Kartka
  wystająca z zamkniętego zeszytu pokazuje `kartka` następnego zadania. Plan tygodnia (`planTygodnia`, `listTygodnia`)
  i nawigacja kroków (`pulpit/nawigacja.js: WNETRZE_KROKU`) dalej działają.
- Testy: każda nazwa warunku z danych ma implementację w JS, każdy `zeton` jest w `dane/mapa/budynki.yaml` (wyjątek:
  `lokal`, `bazar`), każdy `element` jest w harmonogramie, każda `funkcja` w `dane/funkcje.yaml`, każdy `punkt` to istniejący
  ekran. Do tego test endpointu wizyt.
- Teksty dla gracza mają być neutralne płciowo (tryb rozkazujący, liczba mnoga, jak w szkicu).

## Poza zakresem
Wygląd zeszytu (CSS, animacje, okładka), radio, mechanika odblokowań, żeton bazaru, mapa majstra.

## Gotowe, gdy
`pytest` (całość) zielony poza znanym niestabilnym testem kasyna, `ruff check .` czysty, `silnik.dane sprawdz` OK, dla
zmienionych modułów `node --check` OK. Do tego jeden zrzut zeszytu otwartego na stronie tygodnia 1 w grze pokazowej
(`_robocze/zeszyt/`). Commit na gałęzi zrób jako Tom-Wasko, bez dopisków. Push i scalenie robi lider. README
i INSTRUKCJA.md popraw w części o zeszycie.
