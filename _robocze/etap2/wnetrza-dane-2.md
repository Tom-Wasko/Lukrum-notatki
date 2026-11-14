# Zadanie: wnetrza-dane, część 2 (decyzje autora 14.11)

Najpierw przeczytaj `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\BRIEF_AGENTA.md` (zasady wspólne). WYJĄTEK od briefu:
pracujesz w worktree `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\wnetrza-dane` (gałąź wnetrza-dane, już scalona z main;
kod w `gra/`). Python: `C:/Users/PC/Pulpit/Levas/lukrum/lukrum_gra/gra/.venv/Scripts/python`, z `wnetrza-dane/gra`.
Co jest na gałęzi: `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\wnetrza-silnik-raport.md` (przeczytaj najpierw).
Nie commituj. Raport: `_robocze/etap2/wnetrza-dane-2-raport.md`. Równolegle inny agent zmienia biura, banki, kadry,
kuchnię i nieruchomości w innym worktree: nie ruszaj tych plików.

## Do zrobienia
1. **Zaczepki WOS zatwierdzone.** Autor zatwierdził wszystkie 8 (paragon, alergeny, cena z VAT, reklamacja, praca
   16-latka, monitoring, płatność kartą, „na zeszyt”): w `dymki.yaml` `sprawdzone: true` (i kto/kiedy, jeśli schemat ma takie pole: „autor 14.11”).
2. **4 cytaty z lektur do sprawdzenia** w Wolnych Lekturach (wolnelektury.pl, wersja tekstowa .txt utworu): Dulska,
   dwa Zagłoby, Papkin („daj”/„kup”). Znajdź je w `dane/` grepem (pole `cytat`). Każdy porównaj dosłownie z tekstem lektury;
   popraw do brzmienia oryginału (z interpunkcją) albo, gdy cytatu w tekście nie ma, zamień na prawdziwy krótki cytat
   tej postaci pasujący do sytuacji. W raporcie: stary, nowy, link do źródła.
3. **Gracz nie wyłącza dymków.** Usuń własny filtr gracza (`?rodzaje=` w widoku wnętrz, `filtr_gracza` w odpowiedzi,
   ewentualne UI i testy filtra gracza). Ustawienie mistrza gry (`wlaczone`) zostaje bez zmian.
4. **Propozycje: wskazówka skutków bez liczb.** Przed wyborem odpowiedzi gracz widzi przy każdej opcji krótką wskazówkę
   kierunku skutków (np. „więcej gości, mniej zysku na porcji”, „ryzyko złej opinii”) bez liczb i bez szansy powodzenia.
   Wskazówki w danych (pole przy opcji w yaml propozycji, schemat pydantic), test, że każda opcja ma wskazówkę i że nie ma w niej cyfr ani „%”.
5. **Plotki w tej samej rundzie co zdarzenie** na mapie (parki): teraz plotka przychodzi z opóźnieniem – przestaw na tę
   samą rundę. Test.
6. **Zestaw ★★★ w danych.** Wszystkie jakości mają 1–3 gwiazdki. W `dane/mapa/lokale.yaml` `zestawy` są ★ (podstawowy) i ★★
   (solidny, podwójny): dodaj zestaw ★★★ (np. `profesjonalny`, nazwa „Zestaw profesjonalny (★★★)”), z parametrami
   wyprowadzonymi z istniejących (lepszy niż solidny, droższy; liczby `pewnosc: zalozenie`). Sprawdź, gdzie zestaw jest
   używany (zakup/wymiana wyposażenia, lokale `zestaw:`) i czy ★★★ jest osiągalny w grze (np. ulepszenie wyposażenia);
   jeśli nie ma ścieżki, dopisz najprostszą spójną (albo opisz w raporcie, jeśli wymaga to plików drugiego agenta).
   Grafiki sprzętu w poziomie 3 już są (`panel_gracza/static/grafiki/wnetrze/`).

## Pomiary
Punkt 6 to balans: przed i po `PY -X utf8 -m balans.symuluj 12 latwy,sredni,trudny 7,11,23` (z `gra/`), wyniki do
`_robocze/etap2/pomiary/wnetrza-przed.txt` i `wnetrza-po.txt`, krótko porównaj w raporcie.

## Notatki funkcji
Szkice do `_robocze/etap2/notatki/<Nazwa funkcji>.md` w formacie jak `C:\Users\PC\Pulpit\Levas\lukrum\notatki\Funkcje\Wysoka widoczność.md`.
Jeśli notatka funkcji już jest w `notatki/Funkcje/`, napisz tylko nowy fragment i nazwę pliku. Repo notatek nie ruszaj.
