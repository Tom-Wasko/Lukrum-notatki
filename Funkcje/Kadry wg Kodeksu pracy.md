# Kadry wg Kodeksu pracy

- **Stan:** w grze (PR #2 i #5, 14.11.2026); ostrzeżenie o kontroli PIP w panelu od 16.11
- **Gdzie w grze:** Mój kebab → Zaplecze (zespół, umowy i grafik); Miasteczko akademickie → tablica ogłoszeń (rynek pracy)

## Dla ucznia (do instrukcji)
Pensje w grze wzorowane są na ofertach pracy z lubelskich lokali: kucharz zarabia ok. 5 400–6 800 zł brutto, a kasjer
bliżej płacy minimalnej (4 806 zł w 2026 roku). Można zatrudnić na umowę o pracę albo na zlecenie. Umowa o pracę
daje płatny urlop i okres wypowiedzenia zależny od stażu. Zlecenie jest tańsze w składkach, ale pracownik może
odejść od razu i jest mniej zadowolony z pracy. Nie ma odpraw: zwolniony pracuje do końca wypowiedzenia i dostaje za
ten czas pensję.

Zlecenie nie jest sposobem na etat bez składek. Jeśli osoba na zleceniu pracuje jak etatowiec, czyli codziennie na
ustalone godziny, pod kierownictwem i w pełnym wymiarze (co najmniej 30 godzin w tygodniu), przez cztery tygodnie
z rzędu, co tydzień grozi kontrola Państwowej Inspekcji Pracy. Kontrola kończy się karą 2 000 zł.

## Zasada działania
- **Okres wypowiedzenia** (w tygodniach gry): do 6 miesięcy pracy 2 tygodnie (okres próbny 3 miesiące: 2 tygodnie,
  art. 34 pkt 3 KP; nowy pracownik w grze zawsze ma umowę próbną na 3 miesiące), od 6 miesięcy 4 tygodnie, od 3 lat
  13 tygodni (art. 36 KP). Liczy się staż u tego pracodawcy. Obowiązuje w obie strony.
- **Umowa o pracę:** ZUS pracodawcy; 10% czasu to płatny urlop (20 albo 26 dni w roku, art. 154 KP), więc pracownik
  daje mniej godzin za tę samą pensję.
- **Zlecenie:** niższe składki, bez urlopu i bez wypowiedzenia, składnik zadowolenia −0,04. Student na zleceniu jest
  bez składek. W grze zlecenie nie ma składek pracodawcy: to uproszczenie opisane w instrukcji. Staż i kontrakt B2B
  bez zmian.
- **Kontrola PIP** (`silnik/ludzie/kontrola_pip.py`): na koniec rundy osobie na zleceniu, która ma stanowisko
  i pracuje w pełnym wymiarze (godziny rundy × etat formy ≥ próg), rośnie licznik `tygodnie_jak_etat`; w innym
  przypadku spada do zera. Student pracuje 60% godzin (24 h), więc jest poniżej progu. Gdy licznik osiągnie 4,
  co tydzień losowanie ze strumienia `pip` (powtarzalne ziarno): z szansą 5% kontrola. Kara jest jedna na firmę,
  poza KPiR (rodzaj „kary”), liczy się do mandatów rundy i trafia do wniosków oraz wyników rundy. Liczniki po karze
  się nie zerują: kontrola może się powtarzać, dopóki firma nie zmieni umowy albo godzin.
- **Pensja za okres wypowiedzenia przy wyprowadzce** (`silnik/nieruchomosci/przejecia.py`): gdy najemca traci lokal
  i pracownik nie ma gdzie pójść, pensja za okres wypowiedzenia idzie do kolumny „wynagrodzenia” KPiR, a składki
  ZUS pracodawcy według formy zatrudnienia są osobnym kosztem.
- **Rekrutacja:** ogłoszenie w portalu z ofertami pracy kosztuje 400 zł, agencja pracy i headhunter liczą opłatę
  jako część pensji kandydata (5–9% pensji, headhunter trzy razy tyle).
- **Stanowiska** (przygotowanie: BHP, instalacje, szafki) mają własny cennik: 1 200 zł za pierwsze, 4 300 zł za pięć.
- Pomyłki w szczycie: zob. [[Pomyłki w szczycie]].

## Liczby i źródła
| Parametr | Wartość | Pewność | Plik | Źródło |
|---|---|---|---|---|
| próg godzin | 30 h w tygodniu | założenie | `dane/zalozenia.yaml` (`pracownicy.kontrola_pip`) | decyzja autora 14.11.2026 |
| tygodni z rzędu | 4 | założenie | tamże | decyzja autora 14.11.2026 |
| szansa kontroli | 5% na tydzień | założenie | tamże | decyzja autora 14.11.2026 |
| kara | 2 000 zł | założenie | tamże | art. 281 KP: grzywna 1 000–30 000 zł |
| zadowolenie, zlecenie | −0,04 (było −0,02) | założenie | `dane/zalozenia.yaml` (`zadowolenie_osoby`) | decyzja autora 14.11.2026 |
| urlop | 10% czasu | założenie | `dane/zalozenia.yaml` | decyzja autora 13.11.2026 |

## Czego uczy (do planu zajęć)
- pojęcia: Kodeks pracy, umowa o pracę a umowa zlecenie, okres wypowiedzenia, okres próbny, płaca minimalna, składki
  ZUS pracodawcy, urlop wypoczynkowy, koszt zatrudnienia, rola Państwowej Inspekcji Pracy
- art. 22 § 1 Kodeksu pracy: o stosunku pracy decydują warunki wykonywania pracy, a nie nazwa umowy
- pytania do omówienia: czemu zlecenie jest tańsze dla firmy, a pracownicy wolą umowę o pracę? Kiedy PIP może uznać
  zlecenie za etat?
- krótkie zadanie dla drużyn: policzcie pełny miesięczny koszt zatrudnienia kucharza na umowie o pracę i na zleceniu.

## Do promocji
„Zatrudniasz jak w prawdziwym życiu: okres próbny, wypowiedzenie i urlop.”

## Nawiązanie literackie
Brak.
