# Seria `fable` – raport zbiorczy (15–16.11.2026)

Samodzielna praca agenta Fable na gałęzi `fable`, w 18 tematach (`fable-<temat>`). Całość jest w `main`
(scalenia 4afdd60 i 9ee8192, 16.11.2026). Przegląd prawny, pomiary i zrzuty z nocy leżą w `archiwum/notatki-wycofane/Analizy/Noc Fable 15-16.11/`
(przegląd prawny, `pomiary/`, `zrzuty/`); jego otwarte sprawy są w [[Do decyzji]]. Surowe dzienniki nocy: `archiwum/fable-noc-surowe/`.

**Przebieg.** Start 15.11 o 16:55. O 17:25 sesja stanęła na limicie użycia i wznowiła pracę 16.11 o 06:49.
Koniec 16.11 o 12:47. Mapa majstra (`maciex`) weszła bez zmian w jego plikach.

**Stan na koniec serii.** Gra pokazowa przechodzi 12 rund bez błędów w konsoli i w logu serwera. Pełny pytest: 739
testów, ruff i `silnik.dane sprawdz` czyste. Automat kliknął wszystkie 75 znaczników mapy i przeszedł 39 ekranów
w trybie ciemnym bez `undefined` i `NaN`.

## 1. Tematy

Kolumna „Zasady” mówi, czy temat zmienia mechanikę gry. „Ocena” to ocena autora zmian, a nie przegląd szefa.

| # | Temat | Co widzi gracz albo mistrz gry | Zasady | Główne pliki | Ocena |
|---|---|---|---|---|---|
| 1 | `swiat` | Menu z boku to miejsca w mieście. Wejście pokazuje scenę z klikalnymi punktami i listę „Co tu zrobisz”. Kebab ma pełne wnętrze (tablica, lada, rożen, zaplecze, bywalcy z dymkami). | bez zmian | `static/swiat/*`, `zakladki/index.js`, `app.js`, `testy/aplikacja/test_swiat.py` | pewne |
| 2 | `wyglad` | Panel, lista gier, panel mistrza gry i logowanie w trzech paletach × jasny/ciemny. Wybór w menu ⚙. Fonty tylko lokalne. Favicon. | bez zmian | `motywy/lukrum.css`, `styl.css`, `pulpit.css`, `motyw.js`, `mg.css`, 4 szablony | pewne dla głównych ekranów |
| 3 | `katalogi` | Jakość ★ / ★★ / ★★★ to wybór z kosztem: składniki ★ = 85%, ★★★ = 132% ceny ★★. Uporządkowany cennik sprzętu i szkoleń. | tylko liczby w `dane/*.yaml` | `sprzet.yaml`, `zasoby.yaml` i inne | do oceny w grze testowej |
| 4 | `dekor` | Wystrój lokalu: cztery grupy elementów (ściany 2 400 zł, szyld 1 800 zł, dodatki 900 zł, meble 3 200 zł) w pięciu stylach. | **nowa mechanika** | `silnik/rynek/dekor.py`, `dane/mapa/dekor.yaml`, `testy/nieruchomosci/test_dekor.py` | działa; wielkość efektu do oceny |
| 5 | `sklep` | Park handlowy → „Meblościanka”: regały stylów z pieczęcią dopasowania, wózek, paragon. | bez zmian | `zakladki/dekor.js`, `swiat/miejsca.js` | pewne |
| 6 | `instrukcja` | `/jak-grac` opisuje obecną grę i ma część „Dla mistrza gry”. Strona w paletach. | bez zmian | `INSTRUKCJA.md` (repozytorium gry), `jak_grac.html` | do przeczytania przez autora |
| 7 | mapa `maciex` | Mapa Lublina majstra scalona z wnętrzami. | bez zmian | – | pewne |
| 8 | `wujek` | Plan tygodnia jako lista kroków. W tygodniach 1–4 list od wujka. Krok „teraz” zaznaczony też na mapie i we wnętrzu. Ekran „Dashboard” nazywa się „Plan tygodnia”. | bez zmian | `zakladki/wujek.js`, `ogolne.js`, `swiat/swiat.css` | pewne |
| 9 | `nazwy` | Tytuły ekranów mówią, gdzie i co („Kamienica bankowa – konto, kredyty i lokaty”). | bez zmian | tabela `NAZWY` w `zakladki/index.js` | nazwy do akceptacji |
| 10 | `kurier` | Co tydzień wydanie gazety: lider, tabela ze zmianami miejsc, „Z ostatniej chwili”, „Wasz tydzień w liczbach”, „Redakcja radzi”. | bez zmian | `swiat/kurier.js` | pewne |
| 11 | `pip` | Ostrzeżenie o kontroli PIP przy zleceniu „jak etat”, kwota przejścia na kartach innych biur, informacja o przejęciu debetu. | bez zmian (silnik liczył to od 14.11) | `api/prezentacja.py`, `ksiegowosc/biuro.py`, `hr.js`, `finanse.js`, `banki.js` | nieobejrzane w grze z debetem |
| 12 | `lekcje` | Kreator gry: „Na żywo” albo „Tryb lekcyjny” (ile rund na żywo, ile dni na kolejną rundę). Drużyna widzi plakietkę z terminem. | bez zmian w silniku | `gry/lekcje.py`, `gry/harmonogram.py`, `panel_mg/*`, `settings.py` | do sprawdzenia w klasie |
| 13 | `final` | Po końcu gry podium ligi, wynik drużyny, jej najlepszy tydzień i ostatni list od wujka. | bez zmian | `zakladki/final.js` | pewne |
| 14 | `ksiega` | Księga gości pod sceną kebaba: ocena w pięciu wymiarach (smak, czekanie, cena, obsługa, wnętrze) i trzy ostatnie wpisy. | bez zmian | `swiat/ksiega.js` | pewne |
| 15 | `dymki-mg` | Panel mistrza gry: cztery przełączniki rodzajów dymków. | bez zmian | `panel_mg/static/mg/mg.js` | pewne |
| 16 | poprawki prawne | Instrukcja: zlecenie i debet jako uproszczenia, urlop 20/26 dni, art. 36 KP, hipoteka i zastaw. „Nocna 13” bez zachęty do ukrywania. Teksty neutralne płciowo. | bez zmian | `INSTRUKCJA.md`, `reklama.yaml`, `parki.yaml`, `kasyno.yaml` | pewne |
| 17 | `scenariusze` | Projekt pięciu lekcji po 45 minut. | – | `dokumentacja/SCENARIUSZE_LEKCJI.md` | projekt |
| 18 | klucz lektur | Instrukcja mistrza gry: tabela postać → utwór → autor (13 pozycji), źródła mapy i fontów. | – | `INSTRUKCJA.md` | pewne |

### Szczegóły tematów, które zmieniają zasady albo wymagają obsługi

**Wystrój lokalu (4).** Styl działa, gdy lubi go co najmniej 40% gości strefy lokalu (20–40%: połowa efektu). Każda
dopasowana grupa daje +0,8% popytu i +0,07 gwiazdki oceny tygodnia. Kupione zostaje na zawsze, zmiana stylu jest
darmowa. Wyłącznik: `dane/mapa/dekor.yaml: wlaczony: false`.

**Tryb lekcyjny (12).** Ustawienie siedzi w `konfiguracja["lekcje"]` gry, brak klucza oznacza grę na żywo. Wartości
domyślne i zakresy: `settings.LUKRUM_TRYB_LEKCYJNY` (3 rundy na żywo, 7 dni na rundę). Rundy po terminie zamyka
komenda `manage.py zamykaj_rundy`, którą trzeba uruchamiać na serwerze z harmonogramu zadań.

**Księga gości (14).** Czystości silnik nie liczy, więc piąty wymiar to „wnętrze” (wyposażenie i wystrój).

## 2. Decyzje podjęte przez agenta bez autora (do akceptacji)
- Scena budynku jest „obrazkowym menu”: ekrany decyzji zostały te same, zmieniła się droga do nich.
- Sprzęt i wyposażenie kupuje się w Parku handlowym, a nie w kebabie.
- Motyw „Grafik zmian” zdjęty z listy wyboru (plik został), bo miał kolory spoza palet.
- Nazwa sklepu „Meblościanka”. W wózku najwyżej jeden styl na grupę elementów. Sklep jest częścią ekranu „Wyposażenie”.
- List od wujka tylko w tygodniach 1–4. Kroki prowadzą do miejsc, a nie do działów.
- Konkretne brzmienia tytułów ekranów (temat 9).
- Księga gości bez nowej mechaniki. Nastrój pracownika 0–100 zostaje jako „zadowolenie” w Zapleczu.
- Klucz do nawiązań literackich tylko dla prowadzących, bo grafiki celowo nie podpisują postaci.
- Instrukcja nie opisuje klubu „Nocna 13” w części dla graczy.

## 3. Pomiary
| Pomiar | Wynik | Plik |
|---|---|---|
| Ceny katalogów, 3 poziomy × 3 ziarna × 5 botów | średnia gotówka na poziomie łatwym −3,6%; premium traci najwięcej; bot agresywny bankrutuje przed i po | `archiwum/…/pomiary/katalogi.md` |
| Zwrot z wystroju, 24 rundy, 3 ziarna × 5 botów średnich | komplet 8 300 zł zwraca się średnio w 10,9 tyg. (tani 17,2, agresywny 7,5); w symulacji botów +112 zł na tydzień | `archiwum/…/pomiary/dekor.md`; skrypt w repozytorium gry: `balans/dekor_pomiar.py` |
| Czas pełnego pomiaru katalogów | ok. 1 minuta przed i po | – |

Uwaga: pole `zrodlo` w `dane/mapa/dekor.yaml` podawało 9,8 tygodnia; pomiar z 17.11 daje 10,9 i jest już w danych.
Ścieżka pomiaru w tym polu wskazuje teraz archiwum (do poprawy w repo gry).

## 4. Niedokończone
- Telefon sprawdzony na kilku ekranach (Plan tygodnia, wnętrze, mapa, sklep, gazeta, zespół). Wysoka widoczność na trzech.
- Temat 11 nieobejrzany w przeglądarce w grze z debetem i zleceniami (są testy widoku).
- Wnętrza poza kebabem są schematyczne. Pawilon na działce korzysta ze sceny budowy i zwykłego wnętrza.
- Strona startowa pokazuje „Nowe w tej rundzie” starymi nazwami („Zakładki”, „HR”). Próba zmiany łamała 2 testy silnika.
- Harmonogram odblokowań prowadzony listami wujka: nie zaczęty.
- Ścieżka pierwszego tygodnia (lokal → bank → biuro → menu → ludzie → wyślij) przechodzi, ale nie była sprawdzona na ludziach.

## 5. Pomysły (nic z tego nie jest wdrożone)
**Do mapy, do rozmowy z majstrem:**
1. Znacznik własnego lokalu z szyldem w kupionym stylu (`v.dekor.lokale[id].aktywne.szyld`).
2. Ocena z księgi gości jako plakietka „3,1 ★” przy znacznikach lokali na poziomie dzielnicy.
3. Grupowanie znaków w Śródmieściu w jeden znak z liczbą przy widoku całego miasta.
4. Pole `geo` lokali w `lokale.yaml` zamiast w `lublin.json`.
5. Odsyłacze dla twórców usunąć z opisów w danych, zamiast wycinać je przy rysowaniu.
6. Przycisk „Stara mapa” zdjąć po teście z klasą.

**Do wnętrz:** dźwięki (dzwonek, stempel), pora dnia za oknem, wizyta wujka przy ladzie w ważnych momentach, boty
widoczne we wnętrzu („u konkurencji kolejka”), na telefonie scena przewijana w poziomie.
