# Kadry wg Kodeksu pracy: nowy fragment, zlecenie jak etat i pensja przy wyprowadzce (decyzje autora 14.11)

Plik do uzupełnienia: `notatki/Funkcje/Kadry wg Kodeksu pracy.md`.

## Dla ucznia (dopisać do instrukcji)
Umowa zlecenie nie jest sposobem na etat bez składek. Jeśli osoba na zleceniu pracuje jak etatowiec, czyli codziennie na
ustalone godziny, pod kierownictwem szefa i w pełnym wymiarze (co najmniej 30 godzin w tygodniu), przez cztery tygodnie
z rzędu, co tydzień grozi Wam kontrola Państwowej Inspekcji Pracy. Kontrola kończy się karą 2 000 zł. Zleceniobiorcy są też
mniej zadowoleni z pracy niż osoby na umowie o pracę (składnik zadowolenia −0,04 zamiast −0,02).

## Zasada działania
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

## Liczby i źródła
| Parametr | Wartość | Pewność | Plik | Źródło |
|---|---|---|---|---|
| próg godzin | 30 h w tygodniu | założenie | `dane/zalozenia.yaml` (`pracownicy.kontrola_pip`) | decyzja autora 14.11.2026 |
| tygodni z rzędu | 4 | założenie | tamże | decyzja autora 14.11.2026 |
| szansa kontroli | 5% na tydzień | założenie | tamże | decyzja autora 14.11.2026 |
| kara | 2 000 zł | założenie | tamże | art. 281 KP: grzywna 1 000–30 000 zł |
| zadowolenie, zlecenie | −0,04 (było −0,02) | założenie | `dane/zalozenia.yaml` (`zadowolenie_osoby`) | decyzja autora 14.11.2026 |

## Czego uczy (dopisać)
- art. 22 § 1 Kodeksu pracy: o stosunku pracy decydują warunki wykonywania pracy, a nie nazwa umowy; rola Państwowej
  Inspekcji Pracy; koszt „oszczędzania” na składkach
- pytanie na lekcji: czym różni się zlecenie od umowy o pracę i kiedy PIP może uznać zlecenie za etat?
