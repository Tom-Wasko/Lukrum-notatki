# Recenzja porządków – kroki 4e i 9 (stan: 17.11.2026, tylko odczyt)

Repo: `gra` (main, HEAD 607aa1d), `notatki` (main). Sprawdzone: próbka `zrodlo` z `krok-4d.md` (porównanie `git show HEAD~1:` z obecnym tekstem, pełne wartości, bo raport 4d ma wiersze obcięte), kontrola (d), odsyłacze, tabela (c), stan gita.

## Wynik ogólny
Zmiany `zrodlo` są poprawne rzeczowo: żadna liczba, data ani podstawa prawna nie zginęła (art. 154 KP, art. 22d PIT, art. 21 ust. 1 pkt 148 PIT, art. 6 ust. 4 ustawy o SUS, Oswald/Proto/Sgroi 2015, ceny 2026 i zakresy płac zostały). Braków: 8 (żaden wysoki). `git status` czysty w obu repo, `.gitignore` ignoruje `db.sqlite3` (przez `*.sqlite3`), `lokalne.json`, `zapisy/`.

## 1. Próbka 30 zmienionych `zrodlo`
| # | Pole | Ocena |
|---|---|---|
| 1 | `dostawcy.yaml:zrodlo` | OK (zostały Auchan, 85%/132%, 1,5–2 zł) |
| 2 | `funkcje.yaml:autopilot.zrodlo` | OK |
| 3 | `kalendarz/kalendarz.yaml:zrodlo` | do poprawy (niski): nadal powołuje się na notatki „Prawidła świata” i „Menu i składniki”, których nie ma w `notatki/` |
| 4 | `kandydaci.yaml:zrodlo` | OK (pensje, pracuj.pl, płaca minimalna 4 806 zł) |
| 5 | `kandydaci.yaml:agencja.zrodlo` | OK (KP art. 36 zachowany) |
| 6 | `katalog.yaml:rundy.kalendarz.zrodlo` | do poprawy (niski): „użytkownik 27.10 (założenie autora)” – to była odpowiedź autora na pytanie, nie założenie; zmienia sens, plus słowo „użytkownik” |
| 7 | `katalog.yaml:rundy.harmonogram_lokali.zrodlo` | OK |
| 8 | `katalog.yaml:udogodnienia.zrodlo` | OK („UF9” → „Dodatkowe pozycje”, wszystkie ceny na miejscu) |
| 9 | `mapa/dekor.yaml:efekty.popyt.zrodlo` | OK (10,9 tyg., cel 8–12, data pomiaru; sekcja „Pomiar 17.11.2026” w `dekor.md` istnieje) |
| 10 | `mapa/klienci.yaml:zrodlo` | OK |
| 11 | `mapa/lokale.yaml:zrodlo` | OK (×1,5 z 40, 75% par, 18 rund zachowane) |
| 12 | `mapa/popyt.yaml:zrodlo` | OK (dwukrotne „kalibracja botami”, ale zrozumiałe; lista 10 mnożników stref jest) |
| 13 | `mapa/promocje.yaml:pamiec.zrodlo` | OK (niski: „kalibracja z 7.11.2026” jest ogólnikowa, bez wskazania pliku) |
| 14 | `mapa/reklama.yaml:zrodlo` | OK (4–10%, 10–30%, 0,265, 8 emisji) |
| 15 | `podatki_2026.yaml:zrodlo` | do poprawy (niski): nadal „Plan implementacji: „Przepisy i stawki z pamięci”” (nieistniejący dokument); „Ustalenia autora … i ustalenia autora o prawidłach świata” brzmi niezręcznie. Stawki prawne zachowane |
| 16 | `zalozenia.yaml:popyt.wspolczynniki_jakosci.zrodlo` | OK |
| 17 | `zalozenia.yaml:popyt.wyposazenie_nasycenie.zrodlo` | OK (430%, +31%, 7 tys., 420 zł, +17%) |
| 18 | `zalozenia.yaml:finanse.amortyzacja_niskocenna.zrodlo` | OK (art. 22d ust. 1 PIT, 10 000 zł, 20%) |
| 19 | `zalozenia.yaml:finanse.inwestor_ratunkowy.zrodlo` | OK (niski: tekst zaczyna się od nawiasu „(odpowiedź autora w planie optymalizacji balansu…”; plan nie istnieje w `notatki/`) |
| 20 | `zalozenia.yaml:magazyn.auto_dostawca.zrodlo` | OK (wszystkie procenty 5/6/7/10%; dwa pomiary 10.11 to teraz oba „pomiar botów”, ale rozróżnia je opis w nawiasie) |
| 21 | `zalozenia.yaml:pracownicy.odejscia.zrodlo` | OK |
| 22 | `zalozenia.yaml:pracownicy.przenosiny.zrodlo` | OK |
| 23 | `zalozenia.yaml:pracownicy.formy_zatrudnienia.zrodlo` | do poprawy (średni): został kod pomiaru „pomiar c4_urlop” (`zalozenia.yaml:570`) – nowy czytelnik nie wie, co to; zamienić na „pomiar botów z 14.11.2026” |
| 24 | `zalozenia.yaml:pracownicy.studenci.zrodlo` | OK (art. 21 ust. 1 pkt 148 PIT, art. 6 ust. 4 SUS, 1,0 / 19–39) |
| 25 | `zalozenia.yaml:pracownicy.oferta_pracy.zrodlo` | OK (niski: „Poprawki 3”, „przed poprawkami 3” – nazwa serii bez wyjaśnienia) |
| 26 | `zalozenia.yaml:pracownicy.szkolenia.zrodlo` | OK |
| 27 | `zalozenia.yaml:pracownicy.wydajnosc_z_zadowolenia.zrodlo` | OK (Oswald/Proto/Sgroi, ±5%, 12%) |
| 28 | `zalozenia.yaml:pracownicy.podkupywanie_botow.zrodlo` | OK (14%, ziarna 1 i 7) |
| 29 | `zalozenia.yaml:lista_bledow.scal_dania_od.zrodlo` | do poprawy (niski): „uwaga z próby gry (listopad 2026)” to nowa treść zamiast „analiza gracza [5]”; nie wiadomo, czy to prawda. Bezpieczniej: „uwaga z analizy gracza (listopad 2026)” albo „założenie autora” |
| 30 | `zdarzenia/falafel.yaml:zrodlo`, `urzad.yaml:zrodlo`, `parki.yaml:zrodlo`, `zasoby.yaml:zrodlo` | falafel OK (niski: „lista ufajniania” – żargon bez dokumentu); parki, zasoby OK; `urzad.yaml:14` do poprawy (średni): „do kalibracji w kroku 5” – zostało |

Dodatkowo (poza próbką): „w kroku 5” zostało też w `dane/zalozenia.yaml:431` i `dane/zdarzenia/magazyn.yaml:11` (te same słowa, kod serii bez znaczenia po porządkach).

## 2. Kontrola (d)
| Polecenie | Wynik |
|---|---|
| `git -C gra grep -i -E "revas\|levas\|\[inna gra\]\|\[poprzedni"` | 1 trafienie fałszywe: `silnik/wnetrza/stan.py:65` (`([poprzednie[u]…`, wzorzec łapie nawias listy). Śladu nazwy brak |
| `git -C notatki grep -i -E "revas\|levas"` | **1 BRAK:** `Zespół/Dziennik lidera.md:86` zawiera „REVAS” („`uzytkownik`: ZwzT zamiast REVAS”). Poprawka: „ZwzT zamiast poprzedniego konkursu” albo usunąć zdanie. Plik w trakcie edycji lidera, więc nie ruszałem |
| `git -C notatki ls-files \| grep -i -E "revas\|levas"` | 0 |
| `grep -r -i -l -E "revas\|levas" warsztat CLAUDE.md .claude` | 0 |

## 3. Martwe odsyłacze
| Plik:linia | Problem | Poprawka |
|---|---|---|
| `gra/dokumentacja/STACK.md:120` | „postęp w `dokumentacja/POSTEP.md`” – plik usunięty w kroku 4 | „postęp w `notatki/Postęp.md` (repozytorium notatek)” |
| `gra/silnik/ksiegowosc/urzad.py:1`, `silnik/kuchnia/menu.py:1`, `silnik/kuchnia/swiezosc.py:1` (`notatki/Menu i składniki.md`), `silnik/rynek/reklama.py:1`, `silnik/swiat/zdarzenia.py:1` | docstringi powołują się na notatki „Elementy mapy”, „Menu i składniki”, „Ustalenia gry”, „Prawidła świata”, „Zdarzenia i historie”, których nie ma (łącznie 11 plików w `silnik/` z formułą „notatka „…””, m.in. `limity.py`, `handel.py`, `promocje.py`, `awarie.py`, `magazyn.py`, `schematy.py:1357`) | zastąpić „założenia autora” albo `notatki/Mapa.md` / `Decyzje.md`; dług, nie blokada |
| `gra/dokumentacja/STACK.md:92` | `_robocze/pomiary/kalibracja/` nie istnieje (tworzy go skrypt `balans/warianty.py:58`) | OK, tylko dopisać „tworzony przy pomiarze” |

Skrypt odsyłaczy Obsidiana z (f): 0 „BRAK”. Ścieżki `gra/gra`, `lukrum_gra`, `raporty/`, `fable_noc`, `dokumentacja/zespol`: 0 trafień w `*.md`. W `testy/dane_zamrozone/` trafienia zostają celowo (zamrożone). `git -C gra ls-files | grep png` poza `static/`: 0 (jest tylko `INSTRUKCJA.pdf` w korzeniu, zgodnie z planem). Pozostałe „brakujące” ścieżki z mojego skryptu to nazwy pakietów w `OPIS_GRY.md`/`STACK.md` i adresy URL – fałszywe alarmy.

## 4. Tabela (c), 10 pozycji wyrywkowo
Sprawdzono grepem w plikach docelowych: nazwa LUKRUM/*lucrum cessans* (`Plan.md`), 17 decyzji (`Decyzje.md`), zastrzeżenie marek, zmiana decyzji o logo (`Decyzje.md` + `Historia.md`), 8 zaczepek WOS (`Funkcje/Dymki przy ladzie.md`), 4 cytaty (`Nawiązania literackie.md`), tabela 13 miejsc (`Mapa.md`), umowy na granicy (`WSPOLPRACA.md`), 18 tematów nocy (`Serie/fable/…`), pomiary katalogów i wystroju (`Analizy/…/pomiary/`). Wszystkie obecne – w tej części 0 braków. (Szczegółowe porównanie liczb w 5 notatkach funkcji nie wchodziło do tego zlecenia.)

## 5. Git
`git -C gra status` i `git -C notatki status`: czyste (0 zmian). `gra/.gitignore` zawiera `zapisy/`, `lokalne.json`, `*.sqlite3`; `git check-ignore` potwierdza dla `db.sqlite3`, `lokalne.json`, `zapisy/`. Pliki `db.sqlite3` i `lokalne.json` leżą w korzeniu repo, ale są ignorowane. 0 braków.

## Lista braków do poprawy
| Priorytet | Plik:linia | Problem | Poprawka |
|---|---|---|---|
| średni | `notatki/Zespół/Dziennik lidera.md:86` | „REVAS” – kontrola (d) ≠ 0 | przepisać zdanie bez nazwy |
| średni | `gra/dokumentacja/STACK.md:120` | martwy `dokumentacja/POSTEP.md` | odsyłacz do `notatki/Postęp.md` |
| średni | `gra/dane/zalozenia.yaml:570` | kod „c4_urlop” | „pomiar botów 14.11.2026” |
| średni | `gra/dane/zdarzenia/urzad.yaml:14`, `zdarzenia/magazyn.yaml:11`, `dane/zalozenia.yaml:431` | „w kroku 5” | usunąć „w kroku 5” |
| niski | `gra/dane/podatki_2026.yaml:12` | „Plan implementacji” (nieistniejący) i podwójne „ustalenia autora” | „z pamięci, do weryfikacji przed kalibracją”, bez nazwy planu |
| niski | `gra/dane/katalog.yaml` (`rundy.kalendarz.zrodlo`) | „użytkownik … (założenie autora)” zmienia sens | „odpowiedź autora 27.10” |
| niski | `gra/dane/zalozenia.yaml` (`lista_bledow.scal_dania_od.zrodlo`) | wymyślone „z próby gry” | „z analizy gracza” albo „założenie autora” |
| niski | 11 plików `silnik/…` (docstringi l. 1) | odsyłacze do nieistniejących notatek | zastąpić ogólnie; można osobną serią |
