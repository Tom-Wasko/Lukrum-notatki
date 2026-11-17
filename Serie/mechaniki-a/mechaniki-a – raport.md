# Raport agenta M – nowe mechaniki, tor A (gałąź `mechaniki-a`)

Worktree: kopia robocza `mechaniki-a` (gałąź `mechaniki-a`, katalog `gra/`; worktree był
założony o poziom wyżej, przeniosłem go `git worktree move`). Pomiary: `pomiary/` (tabele przeniesione do `archiwum/notatki-wycofane/Serie/mechaniki-a/pomiary/`; pliki `.txt` w `archiwum/mechaniki-a-surowe/`, a wszystkie odwołania `pomiary/…` w tym raporcie czytaj względem tego folderu). Narzędzia: `balans.symuluj`
(wynik w pkt) i nowy `balans.pomiar_punktow` (tabela strategii × poziom, działy, bankructwa).

## Pomiar bazowy (przed zmianami, main 895d423)
`python -X utf8 -m balans.symuluj 12 latwy,sredni,trudny 7,11,23` (pełny zapis: `pomiary/baza_symuluj.txt`).
Pełny pytest: wszystkie zielone, ok. 4,3 min.

| poziom | strategia | gotówka zł (śr. 3 ziarna) | wynik działalności (stary iloczyn, śr.) |
|---|---|---|---|
| łatwy | zrównoważony | 64 200 | 0,42 |
| łatwy | tani | 35 700 | −0,00 |
| łatwy | premium | 41 900 | 0,27 |
| łatwy | agresywny | 2 750 | −0,91 |
| łatwy | naśladowca | 46 400 | 0,18 |
| średni | zrównoważony | 90 800 | 0,78 |
| średni | tani | 76 800 | 0,48 |
| średni | premium | 56 400 | 0,52 |
| średni | agresywny | 40 400 | 0,06 |
| średni | naśladowca | 83 100 | 0,72 |
| trudny | zrównoważony | 111 000 | 1,27 |
| trudny | tani | 99 000 | 0,95 |
| trudny | premium | 66 300 | 0,74 |
| trudny | agresywny | 58 900 | 0,49 |
| trudny | naśladowca | 106 000 | 1,26 |

Wniosek bazowy: strategia zrównoważona (i naśladowca) najlepsze, agresywna najsłabsza, gotówka bliska zera tylko u agresywnej
na poziomie łatwym.

## Część 1. Wynik 0–1000 pkt (commit 388b89e)

**Co zmieniono.** Iloczyn pięciu wskaźników i wszystkie stałe regresji (0,9464 / 0,8486 / 0,5353 itd.) usunięte.
Nowy moduł `silnik/wyniki/punkty.py` (stary `karta.py` skasowany), dane w `dane/zalozenia.yaml` sekcja `wynik`:
- pięć działów (finanse, goście, zespół, rozwój, bezpieczeństwo finansowe), każdy sumuje 3–4 składniki z **tabelą progów**
  `[ [miara, punkty], … ]` (interpolacja liniowa; „ponad” – za każde `za` jednostek `pkt` punktów, najwyżej `maks`, więc dział
  może przekroczyć 200: np. udogodnienia/socjal, lokale, dochód). Max bez „ponad” = 200 w każdym dziale (pilnuje test);
- zadowolenie gości (0–100) i zespołu to proste własne wzory punktowe (`wynik.goscie`, `zadowolenie_osoby`), liczby okrągłe;
- tydzień 1 = „Wielkie otwarcie”: 1000 pkt za przygotowanie (lokal 250, menu 200, ekipa 250, zaopatrzenie 150, rezerwa 150);
- ranking = suma ważona punktów tygodni, waga rośnie liniowo od 1,0 (tydz. 2) do 2,0 (ostatni), otwarcie 0,5; „wynik gry” =
  suma ważona ÷ suma wag (skala 0–1000, widok `karta_skumulowana`, `ranking`, panel MG);
- zadowolenie osoby (odejścia, tempo pracy): własny wzór `zadowolenie_osoby.wspolczynniki` (stała 1,0, płaca 0,30, sprzęt 0,02,
  szkolenie 0,05+0,04, zlecenie −0,02, przepracowanie −0,5 ponad 85%); progi odejść przesunięte o +0,05 (0,92 / 1,0 / 0,95);
- panel (rusztowanie): karta wyników pokazuje 5 działów, tabelę progów (`v.tabela_punktow`), składniki własnej karty i
  ranking w punktach; „dlaczego wynik się zmienił” liczy z działów; mapa publiczna `rynek.karta` ma tylko punkty;
- usunięte: `kebab()` i `karta_kebab`, `rozwoj_poprzedni`, `szczyt_majatku`, `poprzednio_*`, `utracona_poprzednio` w modelu firmy.

**Testy.** Skasowane `test_karta.py`, `test_karta_finanse.py` (wzory 5 wskaźników); nowy `test_punkty.py` (progi, „ponad”,
dział > 200, gości, otwarcie, ranking z wagami, mandaty/Harpagon w dochodzie, majątek z wagą). Poprawione liczby w
`test_zadowolenie`, `test_kal_ludzie` (przesunięcie skali zadowolenia o 0,05), `test_wnioski`, `test_panel_mg`
(ranking od tygodnia 1), `test_lista_bledow`, `test_mechaniki`. Kopia zamrożona: tylko sekcje `wynik` i `zadowolenie_osoby`
w `testy/dane_zamrozone/zalozenia.yaml` (stara `karta_wynikow` usunięta); reszta zamrożonych danych bez zmian, bo
silnik nadal czyta ich stary kształt tam, gdzie nowa mechanika jej nie ruszyła.

**Pomiar po części 1** (`pomiary/c1_punkty.md`, 12 rund, ziarna 7/11/23; gotówka prawie jak przed, bo zmiana nie dotyka gry):

| poziom | zrównoważony | tani | premium | agresywny | naśladowca |
|---|---|---|---|---|---|
| łatwy | 612 | 437 | 576 | 391 | 559 |
| średni | 699 | 601 | 649 | 572 | 675 |
| trudny | 749 | 671 | 675 | 654 | 725 |

Kryteria: zrównoważona najlepsza na każdym poziomie, agresywna najsłabsza, rozrzut ok. 360–810 pkt (słaba gra 400–600,
dobry bot ok. 750). Do 1000 dochodzi tylko gra wyjątkowa (kilka lokali, duży socjal, wysoka marża) – boty tego nie robią.
Bankructw w tej serii nie ma (agresywny na łatwym: gotówka ~0 w 1 z 3 gier).

**Do autora.** (1) Progi tabeli są założeniem – można je dowolnie przesuwać w danych; (2) czy tydzień „Wielkie otwarcie”
ma ważyć 0,5 wagi tygodnia 2; (3) boty nie przygotowują całego otwarcia (553–695 z 1000).

## Część 2. Pieniądze: kapitał 50 000 zł, debet, banki z lektur (commit „Pieniądze: kapitał…”)

**Co zmieniono.**
- Kapitał startowy 50 000 zł (`finanse.kapital_startowy`).
- Debet zamiast automatycznego kredytu odnawialnego: pole firmy `kredyt_odnawialny` → `debet` (+ `debet_wlaczony`), decyzja
  `debet: true/false` (bank konta). Saldo poniżej zera na koniec tygodnia = debet. Za zgodą: limit banku, **opłata za każdy
  tydzień na minusie** + odsetki banku; kwota ponad limit albo **debet bez zgody** → odsetki karne 19%, alarm i blokada
  inwestycji w następnej rundzie (istniejący mechanizm Z3: inwestor ratunkowy od mistrza gry, Harpagon). Raty kredytów i
  leasingu płaci się tylko z gotówki i wolnego limitu, więc bez debetu brak gotówki daje zaległości jak dotąd.
  Opcja gry `kredyt_odnawialny` (tryb „na_biezaco / jednoczesnie”) przemianowana na `tryb_debetu`.
- Banki (`dane/mapa/banki.yaml`, nazwy z lektur bez „Bank”): Kmicic (szybki kredyt na start, drogi), Wokulski i S-ka
  (kredyt inwestycyjny), Ziemia Obiecana (leasing, wpłata własna 5%), Oszczędności Rzeckiego (lokaty do 4,2%), Soplicowo
  (tanie konto i terminal), Solaris (debet do 40 tys. zł). Każdy ma własny `debet {limit, oplata, oprocentowanie}`.
  Tabela w notatce `notatki/Funkcje/Banki z lektur.md`.
- Budynki banków na mapie (`dane/mapa/budynki.yaml`): zmienione tylko `nazwa` na nazwy z lektur (budynek otwiera zakładkę banku
  po nazwie). **Do koordynatora:** w `panel_gracza/static/zakladki/mapa_budynki.js` stała `BANKI` ma jeszcze kolory i napisy
  prawdziwych marek na fryzach (CRÉDIT AGR., PKO BP, …) – zostawiłem, bo to wygląd mapy.
- Usunięte: nieużywana sekcja `banki` w `katalog.yaml` (stare nazwy „Bank Pod Bramą”, „Kasa Bystrzyca”, …, schemat `Bank`,
  `SekcjaBankow`), prawdziwe logo banków w `ikony_marek.js` (zostały proste ikony „BANK” dla nazw fikcyjnych).
- Boty: poziomy średni, trudny, niemożliwy i „człowiek” średni/dobry włączają debet (`poziomy.*.debet: true`); łatwy i słaby
  „człowiek” o nim zapominają (stąd sporadyczne alarmy i słabszy wynik łatwych botów).
- Panel (rusztowanie): zakładka Bank – podzakładka „Debet” z przyciskiem włącz/wyłącz, opis ofert z debetem.
- Narzędzie `balans/koszty_bankow.py`: koszt scenariuszy na bankach (tabela niżej).

**Testy.** Nowe: debet za zgodą (limit, opłata, odsetki), debet bez zgody, decyzja `debet`. Przemianowane nazwy banków w
testach, poprawione liczby (oprocentowanie, prowizje), kapitał testów botów. Kopia zamrożona: `mapa/banki.yaml` = nowe banki z
flagami starego układu (`tylko_bank_konta: false`, `zastaw_przejecia: false`), z `katalog.yaml` zniknęła sekcja `banki`,
w `boty.yaml` `debet: true` na poziomach średni/trudny/niemożliwy.

**Pomiar po części 2** (`pomiary/c2_punkty.md`, ziarna 7/11/23, kapitał 50 tys.):

| poziom | zrównoważony | tani | premium | agresywny | naśladowca |
|---|---|---|---|---|---|
| łatwy (wynik pkt / gotówka zł) | 635 / 72 200 | 450 / 45 700 | 625 / 44 200 | 440 / 1 100 | 631 / 66 500 |
| średni | 723 / 103 300 | 611 / 86 500 | 688 / 67 600 | 612 / 49 100 | 705 / 91 900 |
| trudny | 771 / 122 700 | 661 / 104 700 | 718 / 78 100 | 694 / 75 800 | 776 / 126 900 |

Wszystko o 10–40 pkt wyżej niż po części 1 (więcej gotówki na starcie). Agresywny na łatwym: gotówka ~1 tys., 1/3 gier bez
gotówki (bez debetu). Strategia zrównoważona najlepsza albo równa naśladowcy, agresywna najsłabsza.

**Czy każdy bank opłaca się innej strategii?** `pomiary/c2_banki/raport.md` (280 gier, wariant `bank:*` wymuszony u badanej firmy,
poziom średni, 8 ziaren): boty domyślnie nie używają lokat, kredytów ani leasingu (strategie nie mają tych parametrów), więc
różnicę robi głównie konto: Soplicowo (najtańsze konto i terminal) daje +1,2…+6,0 pkt dla tani/premium/zrównoważony/naśladowca
(dla taniego „lepszy”, +1,54 pkt przy 100% par), Kmicic i Oszczędności Rzeckiego są o 0,3…0,4 pkt gorsze (droższe konto). Różnice
są małe, bo w skali tygodnia finanse bankowe to ułamek kosztów. Dlatego dodałem analizę scenariuszy (`pomiary/c2_koszty_bankow.md`):

| bank | specjalizacja | konto+terminal, duży obrót (12 tyg., zł) | lokaty | kredyt na start | kredyt inwest. | leasing | debet 30 tys. na 3 tyg. |
|---|---|---|---|---|---|---|---|
| Kmicic | szybki kredyt na start | 2 444 | 185 | 1 113 | – | – | 440, ponad limit 22 000 (alarm) |
| Wokulski i S-ka | kredyt inwestycyjny | 2 221 | 231 | – | 4 512 | – | 435, ponad limit 20 000 (alarm) |
| Ziemia Obiecana | leasing | 2 221 | 222 | – | – | 1 993 | 456, ponad limit 20 000 (alarm) |
| Oszczędności Rzeckiego | lokaty | 2 403 | 388 | – | – | – | 497, ponad limit 25 000 (alarm) |
| Soplicowo | tanie konto | 1 327 | 203 | – | – | – | 453, ponad limit 24 000 (alarm) |
| Solaris | największy debet | 2 221 | 231 | – | – | – | 564, bez alarmu |

Wniosek: każdy bank jest jedynym (albo najtańszym) dla jednego scenariusza: kredyt bez historii tylko Kmicic, kredyt pod zastaw tylko
Wokulski, leasing tylko Ziemia Obiecana, lokaty +90% u Rzeckiego, konto −40% u Soplicowa, debet bez alarmu tylko Solaris. W grach
botów efekt jest mały, dopóki strategie ich nie używają.

**Do autora.** (1) Czy debet włączany jest zawsze za darmo (teraz tak; można dodać abonament za zgodę); (2) czy bez zgody saldo
poniżej zera ma być karane alarmem i blokadą (teraz tak, jak „debet ponad limit” dawniej); (3) czy dodać botom strategie, które
naprawdę korzystają z lokat/kredytów/leasingu (wtedy różnice banków będą widoczne w pomiarach); (4) prawdziwe banki na mapie
(tło) – decyzja koordynatora przy mapie.

## Część 3. Biura rachunkowe: pakiety S/M/L (commit „Biura rachunkowe: pakiety…”)

**Co zmieniono.** `dane/mapa/biura.yaml`: cztery biura (J.K.Ś., Józef K., Scrooge, Asteroida 328), każde w pakietach S, M, L:
`{cena (mies., brutto), dokumenty (limit w miesiącu), doplata (za dokument ponad limit)}`. Limity 60 / 120 / 200 dokumentów
w miesiącu (14 / 28 / 46 na rundę; boty mają ok. 30 dokumentów na rundę). Opłata rundy = cena pakietu × 12/52 + dopłata × (dokumenty
− limit) + kadry. Usunięte: ryczałt, minimum, „bez limitu”, stare biura (Trybunał, Halinka, e-Księgi24, Debet i Kredyt)
oraz martwa sekcja `biura_rachunkowe` w `katalog.yaml`. Decyzja `pakiet` (S/M/L); firma ma `pakiet_biura`. Cechy biur:
J.K.Ś. – OC, ryzyko 0, kadry do 4 osób w cenie; Józef K. – najtańszy po Scrooge'u, bez OC, ryzyko błędu 4%, zmiana pakietu
trwa 2 rundy (decyzja nie przesuwa terminu przy powtórzeniu); Scrooge – najtańszy, ryzyko 2%, w tygodniu ze świętem (kalendarz
miejski) 50%; Asteroida 328 – najdroższa, ryzyko 0, OC, kadry do 6 osób w cenie. Ceny: kb.pl, cennik biur rachunkowych w Lublinie
i okolicy 2026 (KPiR ok. 300 zł netto przy kilkunastu dokumentach, ok. 1 060 zł netto przy 90–100; kadry ok. 112 zł netto za osobę),
źródło w `zrodlo` pliku. Boty i autopilot wybierają biuro i najlepszy pakiet po liczbie dokumentów z ostatniej rundy.
Panel: karta biura z trzema pakietami i przyciskami wyboru.

**Testy.** Nowe: opłata pakietu, cztery biura i ich cechy, zmiana pakietu u Józefa K. (2 rundy) a u J.K.Ś. (od razu), święta w
kalendarzu. Kopia zamrożona `mapa/biura.yaml` = nowe biura z karami starego układu (200 / 500 zł).

**Pomiar** (`pomiary/c3_biura/raport.md`, wariant `biuro:*` wymuszony, 18 par w kontekście, 3 strategie, poziom średni):

| biuro | Δ wynik (pkt) | Δ majątek zł | uwagi |
|---|---|---|---|
| Scrooge (baza botów – najtańsze) | 0 | 0 | |
| Józef K. | −0,9 ± 2,0 | −206 | szum |
| J.K.Ś. | −1,1 ± 2,0 | −280 | szum |
| Asteroida 328 | −2,7 ± 2,0 | −945 | gorsza (drogo, ale bez ryzyka) |
| samodzielnie (idealnie, bez błędów) | +6,1 ± 2,3 | +1 092 | wariant teoretyczny |

Ranking cen zgodny z opisem: Scrooge < Józef K. < J.K.Ś. < Asteroida; różnice małe, bo biuro to ok. 150–250 zł na rundę.
Pełne wyniki botów po części 3: `pomiary/c3_punkty.md` (jak po części 2; zrównoważony 635 / 722 / 772 pkt na łatwym / średnim / trudnym).

**Do autora.** (1) Czy tydzień ze świętem u Scrooge'a ma mieć ryzyko 50%, czy raczej zamknięcie z dopłatą; (2) czy biura mają
mieć dodatkowe różnice (np. czas obsługi), bo w pomiarach botów kosztują niewiele; (3) wybór nazw pakietów S/M/L.

## Część 4. Kadry według Kodeksu pracy (commit „Kadry wg Kodeksu pracy…”)

**Co zmieniono.**
- Pensje kandydatów z ofert gastronomii w Lublinie 2026: 1★ 4 806–5 100 zł (płaca minimalna 2026), 2★ 5 400–6 000, 3★ 6 200–6 900 (wcześniej
  4 785–5 500). Źródła w `zrodlo` pliku: pracuj.pl (kucharz, kuchnia gorąca, Lublin, 5 400–6 800 zł brutto), aplikuj.pl (praca w gastronomii w
  Lublinie), płaca minimalna 2026. Dane GUS dla Lublina i zawodu nie były dostępne w wyszukiwarce, więc to rzędy wielkości z ofert.
- Okres wypowiedzenia zależny od stażu w tygodniach gry (art. 34 i 36 KP): 0–12 tyg. (okres próbny) 1 tydzień, 13–25 tyg. 2 tyg., od 26 tyg. 4 tyg.,
  od 156 tyg. 13 tyg. W obie strony (zwolnienie i wypowiedzenie z niezadowolenia). Zlecenie, student, B2B, staż – bez wypowiedzenia.
- **Odprawa usunięta** (`koszt_odprawy` z kandydatów, modelu, zdarzeń w parkach, panelu): zwolniony pracuje i dostaje pensję do końca
  wypowiedzenia; przy wyprowadzce najemcy pensja za okres wypowiedzenia płaci najemca.
- Umowa o pracę (i pół etatu) z płatnym urlopem (`urlop`, 5% godzin; zlecenie, B2B i staż bez urlopu); inne składki ZUS, brak wypowiedzenia i niższe
  zadowolenie na zleceniu jak dotąd. Boty `tani` i `agresywny` zatrudniają na zleceniu (parametr strategii `umowa`).
- Nowe koszty rekrutacji: ogłoszenie pracuj.pl 400 zł (było 150), a koszt agencji i headhuntera = pensja × 5–9% (było losowe 200–700 zł).
- Własny cennik przygotowania stanowisk: 1 200 / 2 200 / 3 000 / 3 700 / 4 300 zł (było 1 000 … 4 000).

**Warianty urlopu** (`pomiary/c4_urlop/gry.csv`, poziom średni, 6 ziaren, 5 strategii, wynik / gotówka zł):

| urlop | zrównoważony | tani | premium | agresywny | naśladowca |
|---|---|---|---|---|---|
| 0% | 717 / 83 800 | 609 / 85 700 | 625 / 47 700 | 613 / 40 600 | 721 / 85 800 |
| 5% (wybrany) | 679 / 73 200 | 594 / 81 300 | 618 / 43 900 | 584 / 33 000 | 693 / 77 100 |
| 10% (jak w KP) | 666 / 68 900 | 574 / 74 900 | 608 / 39 700 | 535 / 22 500 | 664 / 68 100 |

Zalecenie: 5%. Pełne 10% obniża wynik o ok. 50 pkt i 15 tys. zł gotówki (godziny kuchni są wąskim gardłem). Autor może zmienić jedną liczbę
(`formy_zatrudnienia.prace.urlop`).

**Pomiar po części 4** (`pomiary/c4_punkty.md`; pensje, urlop i rekrutacja podniosły koszty, więc gotówka spadła o 10–25%):

| poziom | zrównoważony | tani | premium | agresywny | naśladowca |
|---|---|---|---|---|---|
| łatwy | 609 | 453 | 542 | 429 (2/3 bez gotówki) | 607 |
| średni | 674 | 602 | 633 | 608 | 696 |
| trudny | 728 | 654 | 653 | 692 | 770 |

Zrównoważona blisko najlepszej (na trudnym 42 pkt za naśladowcą), agresywna najsłabsza na łatwym, bankructwa tylko u agresywnej na łatwym.

**Testy.** Nowy `test_kadry_kp.py` (wypowiedzenie wg stażu, brak odprawy, koszt rekrutacji, pensje, urlop, cennik); poprawione testy z
`koszt_odprawy`, godzin pół etatu, wypowiedzeń. Kopia zamrożona: bez `koszt_odprawy`, z `koszt_rekrutacji_czesc_pensji` (reszta liczb jak była).

**Do autora.** (1) Urlop 5% czy 10%; (2) czy zlecenie ma być jeszcze mniej zadowalające (teraz −0,02 do zadowolenia osoby); (3) wypowiedzenie 13 tygodni po 3 latach
jest w grze nieosiągalne (gra trwa 12–18 tygodni) – zostawiłem dla zgodności z KP.

## Część 5. Pomyłki w szczycie (commit „Pomyłki w szczycie zamiast reklamacji”)
Reklamacje i mnożnik 0,15 usunięte. Szansa pomyłki przy daniu = skłonność kucharza (kandydaci, 0,2–4%) + dodatek za obciążenie kuchni ponad 70% (do +10 pp)
+ dodatek za zmęczenie obsady (nadgodziny, do +6 pp) + 2 pp bez szkoleń, najwyżej 40% (`zalozenia.yaml: pomylki.szansa`). Pomyłka = danie robione drugi raz
(składniki) i niższe zadowolenie gości. Pomiar (`pomiary/c5_punkty.md`): zrównoważony 593 / 671 / 714 pkt (łatwy/średni/trudny), agresywny najsłabszy na łatwym; nowy test `test_pomylki.py`.

## Część 7 i 8 (w WIP commicie)
7: usunięte martwe dane starej reklamy (`katalog.yaml: media_tradycyjne`, `narzedzia_internetowe`, `zalozenia.yaml: reklama`, pola botów `reklama`/`internet`, schematy, walidacja);
zostaje model agencja × kanał. 8: `model_stanowisk: pula` z własnym uzasadnieniem (mały kebab, jeden grill) i komentarzem w kodzie.

## Stan na pauzę
- Zrobione i scommitowane: części 1 (wynik 0–1000), 2 (kapitał 50 tys., debet, banki z lektur), 3 (biura S/M/L), 4 (kadry wg KP), 5 (pomyłki), 7, 8.
- Nie zrobione: część 6 (nowe katalogi udogodnień/wyposażenia/szkoleń/mediów z cenami z researchu; nazwy mediów „Gazeta Pana Cogito”, „Radio Tichy” w `reklama.yaml`).
- Notatki funkcji w `notatki/Funkcje/` napisane dla: wynik, debet, banki, kapitał, biura, kadry (brak: pomyłki, katalogi).
- Pytest/ruff: po części 4 pełny pytest zielony (poza 2 testami wyprowadzki, poprawionymi); po częściach 5, 7, 8 ruff czysty, `silnik.dane sprawdz` OK, wybrane pliki testów zielone;
  pełny pytest po 5/7/8 uruchomiony w tle w chwili pauzy (wynik w `pomiary/pytest_final.txt`, jeśli plik ma „real”) – do sprawdzenia jutro.
- Dla gracza zmieniło się: wynik punktowy w 5 działach z jawną tabelą progów; Wielkie otwarcie w tyg. 1; start 50 tys.; debet włączany ręcznie z opłatą; sześć banków z lektur;
  biura w pakietach S/M/L; pensje z Lublina, wypowiedzenie wg stażu, bez odpraw, urlop; pomyłki w szczycie zamiast reklamacji.
- Otwarte pytania do autora: patrz „Do autora” w częściach 1–4 (progi punktów, urlop 5%/10%, zgoda na debet, ryzyko Scrooge’a).

## 14.11

**1. Dwa czerwone testy.**
- `test_zuzycie_zasobow_na_klienta`: przyczyna to zamierzona zmiana mechaniki (część 5): pomyłka w szczycie to danie robione drugi raz, więc zużywa składniki.
  Test liczy teraz zużycie jako (400 + pomyłki) × zużycie na danie. Mechaniki nie ruszałem.
- `test_zamowienia_ponad_saldo`: zmiana stanu botów po nowej ekonomii (kapitał 50 tys., płace) dodała do listy czerwony błąd „brak składnika” w zakładce Dostawy;
  test sprawdza pomarańczowe ostrzeżenie o saldzie, więc filtruję po poziomie (mechanika bez zmian).
- Przy pełnym przebiegu wyszedł trzeci: `test_bot_z_dwoma_lokalami…`: drugi lokal bot otwiera w tygodniu 7 zamiast 6 (droższa kadra i urlop), test czeka o tydzień dłużej.

**2. Odpowiedzi autora wprowadzone.**
- „Wielkie otwarcie” waży 1,0 (`wynik.otwarcie.waga_tygodnia`), progi tabeli bez zmian.
- Scrooge w tygodniu ze świętem zamknięty (`zamkniete_w_swieta` w `biura.yaml`, z polem `zrodlo`): dokumenty czekają na następny tydzień (`Firma.dokumenty_przeniesione`),
  pakiet płatny jak zawsze, po otwarciu dopłata 3,00 zł brutto za każdy przeniesiony dokument. Pole `ryzyko_w_swieta` (50%) usunięte.
  Uproszczenie: deklaracje podatkowe biuro składa jak zwykle (przenosi się tylko księgowanie i opłata).
- Urlop na umowie o pracę i pół etatu 10% (było 5%).
- Debet bez zmian.

**3. Część 6 (katalogi).** Wyposażenie: ogródek z parasolami, ładowarki, płatności BLIK i QR, kiosk do zamówień, muzyka (licencja), toaleta dla gości, dostawa przez aplikację
(ceny z rynku 2026, źródło w `zrodlo` sekcji). Udogodnienia: karta sportowa dla zespołu, posiłki pracownicze (hojny socjal). Szkolenia: firmy Lubelska Szkoła Kebabu, Rożen i Rozum,
HACCP w Pięć Minut; ceny 650–2 000 zł (kursy branżowe w Lublinie 2026). Media: „Gazeta Pana Cogito” (nowy kanał w Drukarni „Papier Przyjmie”) i „Radio Tichy” (kanał radiowy Fali Koziołka).
Nowy test `test_katalogi_kebab.py`. Kopia zamrożona bez zmian w tych katalogach (testy mechanik nie czytają nowych pozycji).

**4. Notatki funkcji** (poza repo, bez commitu): nowe „Pomyłki w szczycie”, „Wyposażenie i udogodnienia”; zaktualizowane „Wynik 0–1000 pkt”, „Biura rachunkowe – pakiety”, „Kadry wg Kodeksu pracy”.

**5. Pomiar botów** (`pomiary/d14_punkty.md`, 12 rund, ziarna 7/11/23; wynik w pkt, łatwy / średni / trudny):

| strategia | łatwy | średni | trudny |
|---|---|---|---|
| zrównoważony | 579 | 651 | 702 |
| tani | 452 | 594 | 636 |
| premium | 513 | 618 | 624 |
| agresywny | 406 (2/3 bez gotówki) | 593 | 674 |
| naśladowca | 554 | 673 | 736 |

Zrównoważony i naśladowca na czele (różnica do 34 pkt na trudnym), agresywny najsłabszy na łatwym, bankructwa tylko tam.
Wyniki o ok. 10–20 pkt niższe niż 13.11 (urlop 10%, nowe pozycje wyposażenia kosztują).

**6.** Ruff zielony, `silnik.dane sprawdz` OK, pełny pytest: jedyny czerwony test (drugi lokal bota) poprawiony i przechodzi, reszta zielona w przebiegu `pomiary/pytest_14.txt`.

**Otwarte pytania:** (1) czy dopłata 3 zł za dokument po święcie wystarcza, by Scrooge nie był zawsze najlepszy; (2) boty nie kupują nowych pozycji wyposażenia poza liczbą z strategii, więc ich wpływ jest mały;
(3) „Gazeta Pana Cogito” i „Radio Tichy” są kanałami istniejących agencji, a nie osobnymi agencjami; (4) panel nadal rusztowanie.


## 14.11 po przeglądzie

Poprawki według przeglądu toru A z 14.11 (`archiwum/notatki-wycofane/Analizy/Przegląd toru A 14.11.md`), decyzji autora z 14.11 i dopisków (logotypy zostają; liczby z wcześniejszego projektu wymienione). Pomiar po: `pomiary/d14_po_przegladzie.md` (te same profile i ziarna co `d14_punkty.md`).

**Co zmienione**
1. **Debet.** Opłata i ocena salda tylko na koniec tygodnia: `wyrownaj_gotowke` przed `bank.koniec_rundy` spłaca cały debet z przychodów tygodnia (także ten z tego samego tygodnia); chwilowy minus nic nie kosztuje. Bez zgody banku na minusie na koniec tygodnia: stała opłata 120 zł (`oplata_debet_bez_zgody`) + odsetki karne 19%; alarm i blokada bez zmian. Stopa referencyjna NBP 4% to jedna stała w `banki.yaml`, z niej `silnik.dane sprawdz` liczy limity: debet za zgodą ≤ 15% (art. 359 § 2¹ KC), karne ≤ 19% (art. 481 § 2¹ KC). Stopy debetu: Kmicic 15%, Rzecki 15% (było 20%), Soplicowo 13%, Solaris 15%. Teksty w grze (lista błędów, panel Bank, wnioski) mówią „na koniec tygodnia”, „odsetki maksymalne”. Usunięty martwy `kredyt_odnawialny_automatyczny` i zmienna `odnawialny`.
2. **Pomyłki.** `opinie.pomylki` 10,0 → 2,5; `za_szczyt` 0,10 → 0,04 (próg 0,7 → 0,9), `za_zmeczenie` 0,06 → 0,025, `bez_szkolen` 0,02 → 0,01.
3. **Firma bezczynna.** `wynik.aktywnosc` (pełne punkty działów Goście, Zespół, Bezpieczeństwo od 100 obsłużonych gości, proporcjonalnie poniżej); `pk.karta(..., klienci)`. `wnioski.dlaczego_min` 0,05 → 10 pkt.
4. **Okres próbny** (art. 34 KP): nowy pracownik ma w grze zawsze okres próbny 3 miesiące, więc 2 tygodnie (`kandydaci.yaml`, komentarz z trzema progami), test i notatka poprawione.
5. **Scrooge.** W ostatniej rundzie biuro nie zamyka się: `nalicz(..., ostatnia=True)` rozlicza przeniesione i bieżące dokumenty z dopłatą 3 zł. Opis biura mówi o ukrytej dopłacie ponad limit tygodnia.
6. **Stare odwołania.** `sprzedaz.js`, `konkurencja.js`: `reklamacje` → `pomylki`; `hr.js`: „pomyłki” z jednym miejscem po przecinku; `wnioski.py`: bez kredytu odnawialnego; `INSTRUKCJA.md`: kapitał 50 000 zł, wynik gry 0–1000 pkt (nowy rozdział 3), debet zamiast kredytu odnawialnego, brak odprawy, pomyłki w opiniach, wypowiedzenie wg art. 34/36.
7. **Dopisek B (liczby z wcześniejszego projektu).** `katalog.yaml`: 9 udogodnień (nowe nazwy kebabowe, np. „Ekspres do kawy ziarnistej dla zespołu”, „Wiata rowerowa przy lokalu”), 6 pozycji wyposażenia („WiFi dla gości (światłowód)”, „Stoły i ławy z jasnego drewna”, „Ekran z transmisją meczów Motoru Lublin”…) i oceny firm szkoleniowych (87/79/74) z nowymi cenami i `zrodlo` z uzasadnieniem każdej liczby. `zalozenia.yaml`: usunięte martwe `elastycznosc_ceny`, `elastycznosc_wzgledem_rynku`, `wykladnik_liczby_firm`, `mnoznik_bazowy`, `recepcja_1gw_mnoznik`, `korekta_miesiaca`, `postac_ceny`, `utrata_klientow` (z kodem `_utrata_klientow`), `szum_proc` (dublet); żywe przeliczone: `wspolczynniki_jakosci` 0,82/0,654/0,55 → 0,83/0,65/0,52, `wagi_jakosci` 0,407/0,593 → 0,4/0,6, `wyposazenie_na_procent_klientow` 0,073 → 0,07, wszystkie z własnym `zrodlo` (bez „panelu 361 obserwacji”). Te same zmiany w `testy/dane_zamrozone/` (katalog, zalozenia).
8. **Testy** (`testy/pieniadze/test_debet_i_przeglad.py`, 7 testów): koszt bez zgody > za zgodą dla pięciu kwot i stopy w granicach prawa; chwilowy minus bez kosztu; koniec tygodnia na minusie za zgodą i bez zgody; debet w rozegranej grze (10 rund, 5 botów, łatwy); pomyłki a opinie; święto w ostatniej rundzie; firma bezczynna ≤ 100 pkt. Zmienione testy: wypowiedzenie (2 tygodnie), nazwy pozycji katalogu, komunikat „skończy się na minusie”, tryby debetu (ostatni wpis debetu jest ostatni; wcześniej dokładnie jeden).

**Liczby przed/po** (poziomy łatwy+średni, ziarna 7 i 11, 12 rund, 5 botów):
- udział pomyłek: mediana 12,0% → 5,2%, średnia 10,9% → 5,0%, maksimum 20,3% → 10,2%; premium (dobra obsada, szkolenia) 6,1% → 2,8%;
- ocena lokalu: zrównoważony 1,99★ → 2,76★, tani 1,85 → 2,50, premium 2,94 → 3,44, agresywny 1,65 → 2,27, naśladowca 1,81 → 2,49; powód „pomyłki” −1,1…−1,3★ → −0,07…−0,15★.
- wynik botów (średni z 3 ziaren, łatwy / średni / trudny), przed → po: zrównoważony 579/651/702 → 585/665/722; tani 452/594/636 → 461/599/655; premium 513/618/624 → 528/621/620; agresywny 406/593/674 → 432/602/690 (na łatwym 3/3 bez gotówki, wcześniej 2/3); naśladowca 554/673/736 → 543/673/738.
- firma bezczynna: 365 pkt tygodniowo → ≤ 100 (test).

**Kontrola:** pytest 605 zielonych (5 min 34 s), ruff i `silnik.dane sprawdz` zielone.

**Otwarte (wymagają decyzji autora, nie ruszane)**
- Zlecenie 34% tańsze od etatu i bez ryzyka (PIP, ZUS) – znalezisko 7.
- Scrooge: zmiana biura darmowa i natychmiastowa (przeskok), Asteroida 328 zawsze gorsza od J.K.Ś., ryzyko błędu praktycznie bez wagi – znalezisko 8c–e; limit pakietu miesięczny a stosowany co tydzień (8a).
- Obejście opóźnienia zmiany pakietu u Józefa K. (znalezisko 9).
- Wypowiedzenie przy wyprowadzce: kolumna KPiR i ZUS (znalezisko 11); pomyłka przy pustym magazynie nic nie kosztuje; zmiana banku z otwartym debetem; urlop 10% = 26 dni; nowe pozycje wyposażenia bez własnej mechaniki (dostawa, ogródek).
- `konkurencja.py` niesie `zadowolenie_klientow` w skali 0–100.
- Agresywny bot na łatwym wciąż kończy bez gotówki (3/3) – bot łatwy nie włącza debetu; teraz kosztuje to więcej (opłata 120 zł tygodniowo), co jest zamierzone.
- Dopisek A: `ikony_marek.js` i szyldy banków bez zmian.
