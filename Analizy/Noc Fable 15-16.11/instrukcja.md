# Raport: instrukcja (gałąź fable-instrukcja)

## Zmienione pliki
- `gra/INSTRUKCJA.md` – przepisana od zera (538 linii, było 534): pierwsze 10 minut, runda, wynik 0–1000, miejsca w mieście
  (tabela), funkcje zakryte/wyłączone, klienci (pomyłki w szczycie, dymki), menu i ceny, dostawcy, ludzie i Kodeks pracy
  (formy, urlop 10%, wypowiedzenia, kontrola PIP), pieniądze (6 banków, debet, przejęcie debetu, Harpagon, biura rachunkowe
  z opłatą za zmianę), marketing, zdarzenia i rozwój, odblokowania, rady, część „Dla mistrza gry” (zakładanie gry, funkcje,
  zamykanie rundy, podgląd drużyn, tryb lekcyjny, PIP i spory, ranking). Tylko składnia obsługiwana przez `instrukcja.py`.
- `gra/panel_gracza/templates/panel_gracza/jak_grac.html` – bez Google Fonts; dołączone fonty.css, zmienne.css,
  dostepnosc.css i lukrum.js; kolory i fonty na zmiennych palety. `statyczne` dostarcza context processor
  (`lukrum.statyczne.kontekst`), więc widoki.py bez zmian.

## Potwierdzone w danych/kodzie
Kapitał 50 000 zł; 18 rund; PIP: 30 h, 4 tygodnie z rzędu, szansa 5%, kara 2 000 zł (zlecenie; student poniżej progu);
opłata za zmianę biura = 1 tydzień pakietu nowego biura, pierwszy wybór bez opłaty; przejęcie debetu 2% kwoty, min. 40 zł;
limity debetu 5 000–40 000 zł; Scrooge 6 zł za dokument; zmiana z licytacji: lokale od tyg. 1 (dane: `licytacje_od_rundy: 1`),
przejęcia od tyg. 4 (stara instrukcja podawała licytacje od 4 – poprawiono wg danych).

## Nie potwierdzone / pominięte
- Bez liczb: ceny pakietów biur (nie czytane w całości), czas wypowiedzenia „2 tygodnie / miesiąc / 3 miesiące” podany
  ogólnie wg notatki Kadry.
- Ranking „od rundy 3” i próg „kółko i z rysunkami” – przepisane ze starej wersji lub pominięte; nie sprawdzano w kodzie ekranów.
- Kasyno – pominięte celowo (notatka: „celowo nie opisujemy”).
- Układ menu u góry/z boku w ⚙ – wg briefu, nie sprawdzano w kodzie.
- Panel MG: „dymki wyłączane przez MG” (notatka) usunięte z instrukcji, bo nie ma tego w `panel_mg`.
- W części dla MG nie ma osobnego widoku kontroli PIP – opisano, że drużyna widzi ją we wnioskach, a MG przez „Strona firmy”.

## Wątpliwości
- Nazwy przycisków MG wzięte z `mg.js` (np. „Zamknij rundę N”, „Wstrzymaj grę”, „Cofnij rundę”, „Strona firmy”).
- Tryb lekcyjny opisany jako zalecenie organizacyjne (nie ma przełącznika) – zgodnie z decyzją 14.11 w „Do decyzji”.
- Test `test_instrukcja_jak_grac_bez_logowania` przechodzi; pełnego pytestu nie uruchamiano. PDF nie generowano.
