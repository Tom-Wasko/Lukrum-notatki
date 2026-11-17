# Debet

- **Stan:** w grze (PR #2 i #5, 14.11.2026); widok przejęcia debetu od 16.11
- **Gdzie w grze:** Kamienica bankowa → bank, w którym firma ma konto

## Dla ucznia (do instrukcji)
Debet to pozwolenie banku, żeby konto firmy zeszło poniżej zera, gdy zabraknie gotówki. Nie działa sam: trzeba go
włączyć w banku, w którym firma ma konto. Każdy bank daje inny limit. Liczy się saldo na koniec tygodnia: chwilowy
minus w trakcie tygodnia nic nie kosztuje. Tydzień zakończony na minusie to opłata i odsetki. Kto nie włączył debetu,
a tydzień kończy na minusie, płaci drożej (stała opłata i odsetki karne), dostaje alarm i blokadę inwestycji.

Przy zmianie banku z otwartym debetem dług nie znika. Jeśli firma ma dość gotówki, debet jest najpierw spłacany
w starym banku. Jeśli nie ma, nowy bank przejmuje dług i pobiera jednorazową opłatę: 2% kwoty debetu, nie mniej niż
najmniejsza opłata za debet w ofercie banków. To uproszczenie względem prawdziwej bankowości, opisane w instrukcji.

## Zasada działania
- Decyzja „debet: włącz / wyłącz” działa w banku konta. Włączyć można zawsze, wyłączyć dopiero, gdy konto jest na plusie.
- Przychody tygodnia najpierw spłacają debet z wydatków. Opłata i ocena salda dotyczą tylko salda na koniec tygodnia.
- **Za zgodą:** w granicach limitu banku opłata za tydzień na minusie i odsetki. Stopy banków (13–15%) nie
  przekraczają odsetek maksymalnych 2 × (stopa referencyjna NBP + 3,5 pp) = 15%, art. 359 § 2¹ KC.
- **Bez zgody albo ponad limit:** odsetki karne 19% = maksymalne odsetki za opóźnienie 2 × (stopa referencyjna +
  5,5 pp), art. 481 § 2¹ KC. Bez zgody dochodzi stała opłata 120 zł za „niedozwolone saldo debetowe”. Zawsze drożej
  niż za zgodą (pilnuje test na kilku kwotach). Taka firma dostaje alarm, a w następnym tygodniu nie może inwestować,
  brać kredytów, leasingu ani zakładać lokat. Mistrz gry może jej przysłać inwestora ratunkowego albo zostaje Harpagon.
- Stopa referencyjna (4%) to jedna stała w `banki.yaml`. `silnik.dane sprawdz` pilnuje limitów.
- Wolny limit debetu liczy się też przy ratach kredytów i leasingu: bez zgody rata, na którą nie stać, jest zaległa.
- **Zmiana banku z debetem** (`silnik/pieniadze/banki.py`, początek rundy):
  - gotówka ≥ debet: operacja „Spłata debetu przed zmianą banku” (poza KPiR), debet = 0;
  - gotówka < debet: debet przechodzi do nowego banku, opłata `max(najmniejsza opłata debetu, 2% × debet)` w KPiR
    jako „Opłata za przejęcie debetu przez bank …” (dokument „Wyciąg bankowy”).
  - Pierwszy wybór banku i zmiana banku bez debetu nic nie kosztują.
  - Przeniesiony dług podlega zasadom nowego banku (jego limit i oprocentowanie, ponad limit odsetki karne).
  - Komunikat dla gracza jest w wynikach rundy. Przed zmianą karty innych banków pokazują informację o przejęciu
    i ostrzeżenie, gdy limit nowego banku jest za niski.

## Liczby i źródła
| Parametr | Wartość | Pewność | Plik | Źródło |
|---|---|---|---|---|
| stopy debetu za zgodą | 13–15% | założenie | `dane/mapa/banki.yaml` | limit z art. 359 § 2¹ KC |
| odsetki karne | 19% | założenie | `dane/mapa/banki.yaml` | limit z art. 481 § 2¹ KC |
| opłata za saldo bez zgody | 120 zł | założenie | `dane/mapa/banki.yaml` | – |
| opłata za przejęcie debetu | 2% kwoty, minimum = najmniejsza opłata za debet w bankach (40 zł) | założenie | `dane/mapa/banki.yaml` (`przejecie_debetu`) | decyzja autora 14.11.2026; prowizja za refinansowanie bywa rzędu 1–3% |

## Czego uczy (do planu zajęć)
- pojęcia: debet w rachunku, kredyt odnawialny, koszt pieniądza, płynność finansowa, odsetki karne, zdolność
  kredytowa, ryzyko, refinansowanie długu
- pytania do omówienia: kiedy debet to rozsądne narzędzie, a kiedy pułapka? Czym różni się od kredytu? Przy jakiej
  kwocie debetu zmiana banku na tańszy zwraca się w ciągu miesiąca?
- krótkie zadanie dla drużyn: policzcie, ile kosztują trzy tygodnie na minusie w dwóch różnych bankach.

## Do promocji
„Debet nie włącza się sam. Kto nie przeczytał umowy, płaci karne odsetki.”

## Nawiązanie literackie
Solaris (Lem, „Solaris”): bank z największym debetem, „bezkresny ocean” limitu, ale nieprzewidywalny koszt.
