# wnetrza-dane, część 2: raport (gałąź `wnetrza-dane`, 14.11)

Kopia robocza `wnetrza-dane`. Nic nie commitowane.

## 1. Zaczepki WOS
Wszystkie 8 w `dane/wnetrza/dymki.yaml`: `sprawdzone: true`, a do pola `sprawdzil` dopisane „; zatwierdził autor 14.11”
(schemat nie ma osobnych pól kto/kiedy). Poprawiony też komentarz nagłówkowy.

## 2. Cytaty (źródło: tekst .txt z wolnelektury.pl)
| Postać | Stary | Nowy | Źródło |
|---|---|---|---|
| Dulska | „…aby brudy swoje prać w domu”. | „Na to mamy cztery ściany i sufit, aby brudy swoje prać w domu i aby nikt o nich nie wiedział”. (dosłownie, akt I) | https://wolnelektury.pl/media/book/txt/moralnosc-pani-dulskiej.txt |
| Zagłoba 1 | „Mości panowie! gdybym zaczął…” | „Moi mości panowie! Gdybym zaczął wszystko szczegółowie opowiadać, tedy i dziesięciu nocy by nie starczyło”. (Ogniem i mieczem, t. I) | https://wolnelektury.pl/media/book/txt/ogniem-i-mieczem-tom-pierwszy.txt |
| Zagłoba 2 | „Zdechnę ja i pchły moje!” (źródło w danych: „Trylogia”) | brzmienie bez zmian, bo zgodne z tekstem; poprawione źródło: Ogniem i mieczem, t. II | https://wolnelektury.pl/media/book/txt/ogniem-i-mieczem-tom-drugi.txt |
| Papkin | „…krokodyla daj mi, luby” | „Jeśli nie chcesz mojej zguby, krrokodyla daj mi, luby!” (akt II, „daj mi”; „kup mi” w tekście nie występuje; „Krrokodyla” z podwójnym r tak jest w WL) | https://wolnelektury.pl/media/book/txt/zemsta.txt |

Pola `cytat_zrodlo` zaktualizowane (zawierają adres txt i „sprawdzone z Wolnymi Lekturami 14.11”).

## 3. Gracz nie wyłącza dymków
Usunięte: `?rodzaje=` i `us.filtr_gracza` (`silnik/wnetrza/ustawienia.py`), parametr `filtr_gracza` w `widok.dymki`/`widok.widok`,
pole `filtr_gracza` w odpowiedzi, obsługa w `api/wnetrza.py`. Panelu/JS filtra nie było (grep po `panel_gracza`). Ustawienia
mistrza gry (`wlaczone`, `wnetrza-ustawienia`) bez zmian. Testy: usunięty `test_filtr_gracza_to_tylko_widok`, w
`test_wnetrza_propozycje.py` asercje filtra zastąpione sprawdzeniem, że funkcji nie ma; nowy `test_gracz_nie_wylacza_dymkow`
(parametr `rodzaje` jest ignorowany, brak `filtr_gracza` w odpowiedzi).

## 4. Wskazówki skutków
Pole `wskazowka` (wymagane) przy każdej odpowiedzi propozycji: schemat `Odpowiedz` (`silnik/wnetrza/schematy.py`) odrzuca cyfry
i „%”; widok przekazuje je w `propozycja.odpowiedzi[].wskazowka` (liczb i szansy nadal nie ma). 10 wskazówek w yaml
(np. „Więcej gości i zysku, ale cięższa praca kuchni i ryzyko kontroli”). Testy: `test_kazda_odpowiedz_ma_wskazowke_bez_liczb`
(prawdziwe dane), `test_schemat_odrzuca_wskazowke_z_liczba`, asercja w teście API. Dane testowe uzupełnione o `wskazowka`.
Wątpliwość: przy odpowiedzi z `szansa` (kapela Papkina) wskazówka mówi „niepewny skutek”, co jest informacją o ryzyku bez liczb.

## 5. Plotki w tej samej rundzie
Konfiguracja kontekstu już brała `eventy_parku` bieżącej rundy, więc opóźnienie wynikało z losowania: plotka o parku wpadała
dopiero przy szczęśliwym losowaniu, nieraz rundę lub dwie po zdarzeniu na mapie. Teraz, gdy w rundzie jest zdarzenie w parku,
pierwszy dymek rundy (po wujku) jest plotką o parku (`silnik/wnetrza/dymki.py`). Wyłączone plotki (MG) nic nie wymuszają.
Test: `test_plotka_o_parku_w_tej_samej_rundzie_co_zdarzenie` (60 ziaren). Jeśli opóźnienie, które widział autor, było gdzie indziej
(np. w panelu), proszę o opis.

## 6. Zestaw ★★★
`dane/mapa/lokale.yaml`: nowy zestaw `profesjonalny` („Zestaw profesjonalny (★★★)”): układ jak `solidny` (kuchnia + kasa), cały sprzęt
w jakości 3 (ceny i utrzymanie z `sprzet.yaml`, więc brak nowych liczb; schemat zestawu nie ma pola `pewnosc`, dlatego adnotacja
„założenie” jest komentarzem w yaml). Lokal `centrum_1` (Krakowskie Przedmieście, od 6 firm) zmieniony z `solidny` na `profesjonalny`.
Czynsz bez zmian. Dostępność: sprzęt jakości 3 można też dokupić decyzją `sprzet_kup` w każdym lokalu, a zestaw ma jeden lokal.
`silnik/schematy.py` nie ruszany.
Pomiar `balans.symuluj 12 latwy,sredni,trudny 7,11,23`: `pomiary/wnetrza-przed.txt` i `wnetrza-po.txt` różnią się tylko czasem
wykonania, wyniki identyczne (w symulacjach centrum_1 nie jest brane, a zestaw ma wpływ tylko po jego kupnie/najmie).

## Poza zakresem, ale konieczne
`silnik/wnetrza/stan.py`: import `from ..wyniki import karta` nie działał po scaleniu z main (moduł nazywa się `punkty`):
poprawiony na `from ..wyniki import punkty as kw` (bez tego padały 2 pliki testów wnętrz przy zbieraniu).

## Notatki
Szkice w roboczym folderze etapu 2 (po wtopieniu w notatki funkcji usunięte): `Dymki przy ladzie.md` (nowa), `Zestawy wyposażenia gotowych lokali.md` (fragment do „Wyposażenie i udogodnienia”).

## Testy
`testy/wnetrza`: 94 przechodzą. Pełny pytest (z -x): wszystkie przechodzą (exit 0), `ruff check .` czysty, `silnik.dane sprawdz` w porządku.
