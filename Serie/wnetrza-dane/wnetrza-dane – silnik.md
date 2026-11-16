# Silnik wnętrza kebaba: raport (gałąź `wnetrza-dane`)

## Pliki

Nowe (kod w `gra/`):
- `silnik/wnetrza/__init__.py`, `schematy.py`, `stan.py`, `dymki.py`, `propozycje.py`, `ustawienia.py`, `widok.py`
- `api/wnetrza.py`
- `dane/wnetrza/silnik.yaml` (nowy plik z liczbami silnika: skala nastroju, progi min, `waga_dba_o`, imię gościa;
  to plik mój, nie koordynatora, ale leży w folderze danych wnętrz)
- `testy/wnetrza/` (5 plików `test_wnetrza_*.py`, `conftest.py`, `dane_testowe/`): 62 testy

Zmienione (małe dopiski):
- `silnik/dane.py`: `_wczytaj_wnetrza`, pole `Dane.wnetrza` (brak folderu = `None` = gra bez wnętrz), walidacja
  w `sprawdz()` (`python -m silnik.dane sprawdz` sprawdza 3 pliki i odwołania: kto, wskaźniki, okazje wujka).
- `silnik/losowosc.py`: nowy cel strumienia `"wnetrza"` w `CELE`.
- `api/urls.py`: 3 ścieżki.
- `testy/rdzen/test_dane_zamrozone.py`: `test_zamrozona_kopia_ma_wszystkie_pliki_danych` pomija folder `wnetrza/`
  (inaczej padał od samego dodania yaml; dane wnętrz nie są w kopii zamrożonej, bo brak folderu = gra bez wnętrz).
  Nic nie osłabiono.
- Plików z listy „nie ruszaj” nie zmieniałem. `Dane.wersja` (skrót danych) nie obejmuje `dane/wnetrza/` (zmiany tekstów
  nie mają zmieniać wersji gry); po podpięciu skutków warto to dodać (patrz pytania).

Schematy akceptują nowe pola od koordynatora: `sprawdzil` (WOS), `cytat`, `cytat_zrodlo` (opcjonalne). API przekazuje
`sprawdzil` oraz `cytat: true` + `cytat_zrodlo`, ale `cytat` tylko wtedy, gdy jest true.

## Jak to działa

- **Wskaźniki** (`stan.wskazniki`): z `stan.wyniki[runda-1][firma]` i lokali firmy. `cena_wzgledem_strefy` tą samą funkcją co
  karta wyników (`wyniki/karta.py`), `kolejka` i `brak_dan` jako udział utraconej sprzedaży z przyczyn kolejki
  (`KOLEJKI`) i pozostałych, `ocena` średnia z lokali, `zmiana_ceny` porównuje te same dania z poprzednią rundą,
  `nastroj_zespolu` to zadowolenie osób przeskalowane na 0–100 (`silnik.yaml: nastroj`: 0,75 → 0, 1,05 → 100, więc próg
  odejść 0,87 ≈ 40). Dodatkowe pola tekstu `cena`, `cena_strefy`. Brak sprzedaży, opinii albo załogi = wskaźnika nie ma
  w wyniku i warunek `gdy` jest niespełniony. W danych zamrożonych testów nie ma opinii ani zadowolenia, więc tam
  `ocena` i `nastroj_zespolu` nie istnieją (to zamierzone).
- **Stan wnętrza** (`stan.stan_wnetrza`): pracownicy z miejscem (`lada` dla stanowisk kasy, `kuchnia`), miną
  (`smutna` < nastrój 40, `zmeczona` ≥ wykorzystanie 0,85, `wesola` ≥ 75, inaczej `neutralna`; kolejność w yaml),
  `wyposazenie`, `udogodnienia` (nazwy z katalogu, bo katalog nie ma osobnych id), `tlok` = średnie wykorzystanie załogi.
- **Dymki**: `dymki.wylosowane` losuje przed filtrami (strumień ziarno+runda+firma), `dymki_rundy` odcina wyłączone
  rodzaje (wujek zostaje). Dzięki temu filtr nie zmienia tego, kto przychodzi. Historia bywalców jest odtwarzana
  z losowania poprzednich rund (bez zapisu). Temat dymka = klucze `gdy` (bez `gdy` temat „runda”); pasujący `dba_o`
  bywalca ma wagę ×3 (`silnik.yaml`). Wujek: jedna okazja naraz, kolejność ostatnia_runda > pierwsza_strata > rekord > start;
  nie liczy się do limitu dymków ani przerw.
- **Plotki**: `park` z `eventy_parku` bieżącej rundy (te, co widać na mapie), `kalendarz` z wydarzeń zaczynających się
  w następnej rundzie („za tydzień”), `konkurencja` z lokali innych firm (nazwa firmy, nazwa strefy jako `{dzielnica}`).
- **Propozycje**: odtworzenie rund od `od_rundy`: co `co_ile_rund`, każda raz w grze, `gdy` na wskaźnikach tej rundy,
  wybór strumieniem. Odpowiedź drużyny zapisana w konfiguracji gry (patrz niżej).
- **Ustawienia MG**: `konfiguracja["wnetrza"]["dymki"] = {rodzaj: bool}`, brak klucza = wszystkie włączone, czytane
  przy każdym wyliczeniu. Rodzaj `propozycje` wyłączony = brak propozycji i brak skutków.

## Zapis odpowiedzi (własny, nie przez `decyzje`)

Odpowiedź ląduje w `konfiguracja["wnetrza"]["odpowiedzi"][firma][str(runda)] = {"propozycja", "odpowiedz"}` (jak
`odsloniete` w funkcjach, zapisuje ją `Gra.konfiguracja` w bazie i w pliku gry). Dlaczego nie decyzja rundy: `PUT
decyzje` nadpisuje cały słownik firmy, `serwisy.zapisz` odrzuca nieznane klucze `_…` rundy (wymagałoby migracji modelu
`Runda`), a nowy klucz w decyzji rusza `decyzje.py` (poza listą dozwolonych plików).

## API (wszystko pod `/api/gry/<id>/`)

- `GET wnetrza/<firma>[?rodzaje=cena_smak,wos][&lokal=<id>]`: widok drużyny. `rodzaje` to własny filtr gracza (sam widok;
  pusty tekst = żadnych dymków poza wujkiem; nieznany rodzaj = 400). Propozycji filtr nie chowa.
- `POST wnetrza/<firma>/odpowiedz` `{"odpowiedz": "tak"}`: zwraca ten sam widok z `propozycja.wybrana` i `reakcja`.
  Błędy: nieznana odpowiedź lub brak propozycji = 400, decyzje wysłane = 400, cudza firma = 403, MG przy drużynie
  uczniów = 403 (jak `PUT decyzje`).
- `GET|POST wnetrza-ustawienia`: tylko MG (inni 403). `POST {"dymki": {"wos": false}}`, wystarczy część rodzajów.
- Gra bez `dane/wnetrza/` = 404 „Ta gra nie ma wnętrz.”; zakończona gra = 400 (poza ustawieniami MG).

Przykład odpowiedzi `GET` (skrócony):

```json
{"runda": 3,
 "rodzaje": {"cena_smak": "Opinie o cenie i smaku", "plotki": "Plotki z miasta", "propozycje": "Propozycje i kłopoty", "wos": "Zaczepki WOS"},
 "wlaczone": {"cena_smak": true, "plotki": true, "propozycje": true, "wos": true},
 "filtr_gracza": null,
 "stan": {"runda": 2, "lokal": "akademickie_1", "tlok": 0.158, "wyposazenie": [], "udogodnienia": [],
   "pracownicy": [{"id": "g0-Kuc-11", "imie_nazwisko": "Michał Król", "zawod": "Kucharz", "gwiazdki": 2, "miejsce": "kuchnia",
                   "lokal": "akademickie_1", "nastroj": 68.0, "wykorzystanie": 0.208, "mina": "neutralna"}]},
 "wskazniki": {"runda": 3, "ocena": 3.1, "cena_wzgledem_strefy": 1.0503, "cena": 13.53, "cena_strefy": 12.89,
               "kolejka": 0.0, "brak_dan": 0.0459, "nastroj_zespolu": 61.4},
 "dymki": [{"rodzaj": "plotki", "kto": "gosc", "imie": "Gość", "tekst": "Znajomi chwalą „Bot”. Podobno tańszy…"},
           {"rodzaj": "cena_smak", "kto": "dulska", "imie": "Pani Aniela Dulska", "tekst": "…", "cytat": true, "cytat_zrodlo": "Zapolska, …"},
           {"rodzaj": "wos", "kto": "jozio", "imie": "Józio", "tekst": "…", "wyjasnienie": "…", "zrodlo_prawne": "…", "sprawdzil": "…"}],
 "propozycja": {"id": "catering_umcs", "kto": "gosc", "imie": "Gość", "tekst": "…",
                "odpowiedzi": [{"id": "tak", "tekst": "…"}, {"id": "rabat", "tekst": "…"}, {"id": "odmowa", "tekst": "…"}],
                "wybrana": null, "reakcja": null, "domyslna": "odmowa"}}
```

`propozycja` ma `null`, gdy w tej rundzie nie ma propozycji. Skutków odpowiedzi widok nie pokazuje (gracz poznaje je
po rundzie).

## Jak podpiąć skutki propozycji po scaleniu toru A

Nic w `runda.py` nie zostało zmienione. Do podpięcia gotowa jest jedna funkcja:

```python
from .wnetrza import widok as wnetrza
w = wnetrza.skutki_rundy(dane, stan_przed_runda, konfiguracja, firma, r)   # None albo słownik
# {"propozycja": "catering_umcs", "odpowiedz": "rabat", "udane": True,
#  "skutki": {"porcje": 120, "rabat": 0.15, "opinia": 0.1, "ryzyko_kontroli": 0.05}}
```

`stan_przed_runda` = stan po rundzie `r-1` (w `przelicz_runde` to `stan`/`s` na wejściu, zanim zacznie mutować). Funkcja
jest deterministyczna: wybór propozycji, odpowiedź (zapisana albo `bez_odpowiedzi`) i rzut `szansa` (strumień
`(ziarno, r, "wnetrza", firma, "skutki", id_propozycji)`) powtarzają się przy każdym przeliczeniu rundy. Przy `dane.wnetrza
is None` zwraca `None`. Miejsca w przeliczeniu (dla jednej firmy, w jej pętli):

- **porcje** (`porcje` i `darmowe_porcje`): po zwykłej sprzedaży dodać sprzedaż `porcje` × średnia cena menu
  × (1 − `rabat`), przychód księgować jak sprzedaż (z VAT jak w `_wyniki_firmy`), a składniki zdjąć z magazynu według
  receptur dania (`silnik/kuchnia/operacje.py`, `magazyn`). Przy braku składników sprzedać tyle, na ile starcza.
  `darmowe_porcje`: te same składniki, bez przychodu. Do średniej ceny wystarczy `stan.wyniki`/`f.ceny` firmy.
- **koszt**: `ksieguj(f, ks, rach, opis, koszt, "pozostale")` jak w `rynek/konkurencja.py` (brutto, jednorazowo).
- **opinia**: dodać do `lok.ocena` głównego lokala (`per_lokal.glowny`) na następną rundę, przycięcie do 1–5
  (patrz `rynek/opinie.py`), np. przez dopisanie komentarza lub bezpośrednią zmianę `ocena`.
- **ryzyko_kontroli**: dodać do szansy sanepidu w następnej rundzie (`kuchnia/magazyn.py`, `zalozenia.yaml: magazyn.sanepid`)
  przez `Efekt(typ="kontrola", wartosc=…, od_rundy=r+1, do_rundy=r+1)` (typ „kontrola” już istnieje w modelu).
- **kandydat**: dodać osobę do puli kandydatów widoczną tylko dla tej drużyny, jak skutek `kandydat` historii z parków
  (`swiat/zdarzenia.py`, pole `tylko_dla`), bez kosztu ogłoszenia.
- Wynik pokazać drużynie w wynikach rundy (np. `w["wnetrza"] = {…}` z tekstem `reakcja` wybranej odpowiedzi).
- Po scaleniu rozważyć dodanie `dane/wnetrza/*.yaml` do `Dane.wersja`, bo skutki propozycji wpływają na wynik gry.

## Zgłoszone przy okazji

- Dane: format wystarczył. Drobiazgi: `{wydarzenie}` w tekście plotki daje nazwę w mianowniku („Za tydzień Powrót
  studentów”), a `{dzielnica}` nazwę strefy w mianowniku („Na Stare Miasto”). Wymaga to poprawy tekstów albo form
  w danych. Dymek WOS o `kto: wujek` i propozycje z `kto: kazdy` są dozwolone w schemacie, ale propozycja `kazdy` mówi
  zawsze jako gość.
- `dane/wnetrza/silnik.yaml` jest nowym plikiem, do wspólnego commita z pozostałymi yaml wnętrz (koordynator),
  bo kod go wymaga. Commit całości zrobił koordynator 14.11 (agentowi zabrakło uprawnień).

## Pytania do autora

1. Czy gracz ma widzieć skutki odpowiedzi przed wyborem (np. „+120 porcji, ryzyko kontroli”), czy tylko po rundzie?
   Teraz widok ich nie zdradza (poza rzutem na ryzyko, którego też nie pokazuje).
2. Własny filtr gracza dotyczy tylko dymków; propozycje zostają widoczne (inaczej brak odpowiedzi cicho dałby `odmowa`).
   Dobrze?
3. Plotki o parkach opisują zdarzenia z bieżącej rundy (te same, co na mapie), a nie przyszłej. Czy zapowiadać
   zdarzenia już o rundę wcześniej?
4. Progi min i skala nastroju (`silnik.yaml`) są założeniem, do sprawdzenia po grze testowej.
5. Odtwarzanie historii bywalców i propozycji liczy `gdy` na dzisiejszym stanie (np. ocena z lokali), więc w grze
   wskaźniki dawnych rund mogą się minimalnie różnić od tych sprzed tygodni. Dla obecnych danych (propozycje bez `gdy`) to
   bez znaczenia.
