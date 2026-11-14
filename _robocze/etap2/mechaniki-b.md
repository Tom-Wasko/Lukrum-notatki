# Zadanie: mechaniki-b (Tor A, decyzje autora 14.11)

Najpierw przeczytaj `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\BRIEF_AGENTA.md` (zasady wspólne). WYJĄTEK od briefu:
pracujesz w worktree `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\mechaniki-b` (gałąź mechaniki-b, kod w `gra/`), a nie w lukrum_gra.
Python: `C:/Users/PC/Pulpit/Levas/lukrum/lukrum_gra/gra/.venv/Scripts/python`, uruchamiany z `mechaniki-b/gra`.
Kontekst usterek: `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\przeglad-a-fable.md` (punkty 7, 8, 9, 11 i „pusty magazyn”).
Nie commituj. Raport: `_robocze/etap2/mechaniki-b-raport.md`. Liczby gry tylko w yaml (`{wartosc, pewnosc, zrodlo}`, źródło: „decyzja autora 14.11”).

## Do zrobienia
1. **Scrooge.** Dopłata za dokument przeniesiony po święcie: 6 zł zamiast 3 zł (`dane/mapa/biura.yaml`). Dokumenty
   przeniesione z ostatniej rundy gry mają być rozliczone w ostatniej rundzie (teraz przepadają, `silnik/ksiegowosc/biuro.py` `nalicz`).
2. **Asteroida 328: bez limitu dokumentów.** Jej pakiety nie mają dopłat za dokumenty ponad limit (to jej przewaga nad J.K.Ś.).
3. **Opłata za zmianę biura:** jednorazowo równowartość tygodnia pakietu NOWEGO biura (koszt usług obcych, z dokumentem
   do KPiR jak inne opłaty biura). Pierwszy wybór biura na starcie bez opłaty. Powrót do poprzedniego biura też płatny.
4. **Józef K.: obejście opóźnienia zmiany pakietu.** (a) w rundzie 1 jawny wybór pakietu równego domyślnemu ma się zapisać
   (`pakiet_biura`), (b) wyjście do innego biura i powrót nie może skasować opóźnienia. Testy na oba obejścia.
5. **Zmiana banku z otwartym debetem.** Gdy gotówka wystarcza, debet jest najpierw spłacany ze starego banku.
   Gdy nie wystarcza, nowy bank przejmuje debet za jednorazową opłatą (procent kwoty, w `banki.yaml`, założenie:
   2% kwoty, minimum jak najmniejsza opłata banku). Komunikat dla gracza neutralny płciowo. Testy.
6. **Umowa zlecenie: ryzyko kontroli PIP i niższe zadowolenie.** Gdy zleceniobiorca pracuje jak etatowiec (pełen
   wymiar w stałym grafiku, np. ≥ 30 h/tydz. przez 4 tygodnie z rzędu; próg w yaml), co tydzień jest szansa kontroli PIP
   (założenie 5%/tydzień); kontrola = kara (założenie 2000 zł, art. 281 KP mówi o 1000–30 000 zł) + wpis do zdarzeń.
   Zadowolenie zleceniobiorcy: z −0,02 na −0,04 (`zalozenia.yaml`). Losowanie przez `silnik/losowosc.py` (powtarzalne ziarno).
   Sprawdź, czy istnieją kontrole (sanepid itd.) i użyj tego samego mechanizmu.
7. **Pensja za okres wypowiedzenia przy wyprowadzce** (`silnik/nieruchomosci/przejecia.py:280–283`): do kolumny
   wynagrodzeń KPiR i z ZUS pracodawcy, jak zwykła pensja (użyj tej samej funkcji co lista płac).
8. **Pomyłka przy pustym magazynie** (`silnik/kuchnia/operacje.py` ok. 214, `_zuzyj`): pomyłka ma kosztować (zmarnowany
   składnik albo strata porcji/zadowolenia, jak pomyłka przy pełnym). Wybierz najprostsze spójne rozwiązanie, opisz w raporcie.

Nie zmieniaj: częstości pomyłek (5,2% / 2,8% zostają), botów (nie kupują nowego sprzętu – zostaje), plików wnętrz (`silnik/wnetrza*`, `dane/wnetrza/`).

## Pomiary (zmiany balansu)
Przed zmianami i po nich: `PY -X utf8 -m balans.symuluj 12 latwy,sredni,trudny 7,11,23` (z `gra/`), wyniki do
`_robocze/etap2/pomiary/przed.txt` i `po.txt`; jeśli `balans.pomiar_punktow` istnieje, też przed/po. Krótko porównaj w raporcie.

## Notatki funkcji
Dla każdej zmienionej funkcji szkic notatki do `_robocze/etap2/notatki/<Nazwa funkcji>.md` w formacie jak
`C:\Users\PC\Pulpit\Levas\lukrum\notatki\Funkcje\Wysoka widoczność.md` (stan, gdzie w grze, dla ucznia, zasada działania,
liczby i źródła). Jeśli w `notatki/Funkcje/` jest już notatka tej funkcji (np. biura, banki, kadry), napisz w szkicu tylko
nowy fragment i nazwę pliku do uzupełnienia. Repo notatek nie ruszaj.
