# Kadry wg Kodeksu pracy

- **Stan:** na gałęzi mechaniki-a, czeka na zatwierdzenie
- **Gdzie w grze:** Ludzie ▸ Zatrudnienie, Zespół i Rynek pracy

## Dla ucznia (do instrukcji)
Pensje w grze wzorowane są na ofertach pracy z lubelskich lokali: kucharz zarabia ok. 5 400–6 800 zł brutto, a kasjer
bliżej płacy minimalnej (4 806 zł w 2026 roku). Można zatrudnić na umowę o pracę albo na zlecenie. Umowa o pracę
daje płatny urlop i okres wypowiedzenia zależny od stażu, zlecenie jest tańsze w składkach, ale pracownik może
odejść od razu. Nie ma odpraw: zwolniony pracuje do końca wypowiedzenia i dostaje za ten czas pensję.

## Zasada działania
- **Okres wypowiedzenia** (w tygodniach gry): do 6 miesięcy pracy – 2 tygodnie (okres próbny 3 miesiące: 2 tygodnie, art. 34 pkt 3 KP;
  krótszy okres próbny dałby 3 dni robocze albo 1 tydzień – nowy pracownik w grze zawsze ma umowę na 3 miesiące), od 6 miesięcy – 4 tygodnie (miesiąc), od 3 lat – 13 tygodni (art. 36 KP). Liczy się staż u tego pracodawcy.
  Obowiązuje w obie strony: kiedy firma zwalnia i kiedy pracownik składa wypowiedzenie.
- **Umowa o pracę:** ZUS pracodawcy, 10% czasu to płatny urlop (26 dni w roku, art. 154 KP), więc pracownik daje
  mniej godzin za tę samą pensję. **Zlecenie:** niższe składki, bez urlopu i bez wypowiedzenia, ale niższe
  zadowolenie. Student na zleceniu – bez składek. Staż i kontrakt B2B jak dotąd.
- **Rekrutacja:** ogłoszenie na pracuj.pl kosztuje 400 zł, agencja pracy i headhunter liczą opłatę jako część pensji
  kandydata (5–9% pensji, headhunter trzy razy tyle).
- **Stanowiska** (przygotowanie: BHP, instalacje, szafki) mają własny cennik: 1 200 zł za pierwsze, 4 300 zł za pięć.
- **Pomyłki w szczycie** – zob. osobna notatka.

## Czego uczy (do planu zajęć)
- pojęcie z WOS / przedsiębiorczości: Kodeks pracy, umowa o pracę a umowa zlecenie, okres wypowiedzenia, okres próbny,
  płaca minimalna, składki ZUS pracodawcy, urlop wypoczynkowy, koszt zatrudnienia pracownika
- pytanie do omówienia na lekcji: czemu umowa zlecenie jest tańsza dla firmy, a pracownicy wolą umowę o pracę?
- krótkie zadanie dla drużyn: policzcie pełny miesięczny koszt zatrudnienia kucharza na umowie o pracę i na zleceniu.

## Do promocji
„Zatrudniasz jak w prawdziwym życiu: okres próbny, wypowiedzenie i urlop.”

## Nawiązanie literackie
Brak.

## Zmiany 14.11.2026 (decyzje autora)

### Dla ucznia
Umowa zlecenie nie jest sposobem na etat bez składek. Jeśli osoba na zleceniu pracuje jak etatowiec, czyli codziennie na
ustalone godziny, pod kierownictwem szefa i w pełnym wymiarze (co najmniej 30 godzin w tygodniu), przez cztery tygodnie
z rzędu, co tydzień grozi Wam kontrola Państwowej Inspekcji Pracy. Kontrola kończy się karą 2 000 zł. Zleceniobiorcy są też
mniej zadowoleni z pracy niż osoby na umowie o pracę (składnik zadowolenia −0,04 zamiast −0,02).

### Zasada działania
- `silnik/ludzie/kontrola_pip.py`. Na koniec rundy dla każdej osoby z formą `kara_zlecenia` (zlecenie, zlecenie ze studentem),
  która ma stanowisko i pracuje w pełnym wymiarze (godziny rundy × etat formy ≥ `prog_godzin`), rośnie licznik
  `tygodnie_jak_etat`; w innym przypadku spada do zera. Student pracuje 60% godzin (24 h), więc poniżej progu.
- Gdy ktoś ma licznik ≥ `tygodni_z_rzedu`, losowanie ze strumienia `pip` (powtarzalne ziarno, jak sanepid): z szansą 5% kontrola.
  Kara jest jedna na firmę (nie na osobę), poza KPiR (rodzaj „kary”), liczy się do mandatów rundy i trafia do wniosków
  („Kontrola PIP: zlecenie jak etat”) oraz do wyników rundy (`pip`: osoby, tekst, kara).
- Bez zmiany liczników po karze: kontrola może się powtarzać, dopóki firma nie zmieni umowy albo godzin.
- **Pensja za okres wypowiedzenia przy wyprowadzce** (`silnik/nieruchomosci/przejecia.py`): gdy najemca traci lokal i pracownik
  nie ma gdzie pójść, pensja za okres wypowiedzenia idzie do kolumny „wynagrodzenia” KPiR (wcześniej do „pozostałych”),
  a składki ZUS pracodawcy według formy zatrudnienia (`formy.stawka_zus`, jak w liście płac) są osobnym kosztem.

### Liczby i źródła
| Parametr | Wartość | Pewność | Plik | Źródło |
|---|---|---|---|---|
| próg godzin | 30 h w tygodniu | założenie | `dane/zalozenia.yaml` (`pracownicy.kontrola_pip`) | decyzja autora 14.11.2026 |
| tygodni z rzędu | 4 | założenie | tamże | decyzja autora 14.11.2026 |
| szansa kontroli | 5% na tydzień | założenie | tamże | decyzja autora 14.11.2026 |
| kara | 2 000 zł | założenie | tamże | art. 281 KP: grzywna 1 000–30 000 zł |
| zadowolenie, zlecenie | −0,04 (było −0,02) | założenie | `dane/zalozenia.yaml` (`zadowolenie_osoby`) | decyzja autora 14.11.2026 |

### Czego uczy
- art. 22 § 1 Kodeksu pracy: o stosunku pracy decydują warunki wykonywania pracy, a nie nazwa umowy; rola Państwowej
  Inspekcji Pracy; koszt „oszczędzania” na składkach
- pytanie na lekcji: czym różni się zlecenie od umowy o pracę i kiedy PIP może uznać zlecenie za etat?
