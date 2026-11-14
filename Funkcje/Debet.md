# Debet

- **Stan:** na gałęzi mechaniki-a, czeka na zatwierdzenie
- **Gdzie w grze:** Pieniądze ▸ Bank ▸ zakładka „Debet”

## Dla ucznia (do instrukcji)
Debet to pozwolenie banku, żeby konto firmy zeszło poniżej zera, gdy zabraknie gotówki. Nie działa samo: trzeba go
włączyć w banku, w którym firma ma konto. Każdy bank daje inny limit. Liczy się saldo na koniec tygodnia: chwilowy minus w trakcie
tygodnia nic nie kosztuje. Tydzień zakończony na minusie to opłata i odsetki. Kto nie włączył debetu, a tydzień kończy na minusie,
placi drożej (stała opłata i odsetki karne), dostaje alarm i blokadę inwestycji.

## Zasada działania
- Decyzja „debet: włącz / wyłącz” działa w banku konta. Włączyć można zawsze, wyłączyć dopiero, gdy konto jest na plusie.
- Przychody tygodnia najpierw spłacają debet z wydatków (chwilowy minus nic nie kosztuje). Opłata i ocena salda dotyczą tylko
  salda na koniec tygodnia (14.11.2026, decyzja autora).
- Za zgodą: w granicach limitu banku opłata za tydzień na minusie i odsetki. Stopy banków (13–15%) nie przekraczają odsetek
  maksymalnych 2 × (stopa ref. NBP + 3,5 pp) = 15%, art. 359 § 2¹ KC.
- Bez zgody (albo ponad limit): odsetki karne 19% = maksymalne odsetki za opóźnienie 2 × (ref. + 5,5 pp), art. 481 § 2¹ KC,
  a bez zgody także stała opłata 120 zł za „niedozwolone saldo debetowe”. Zawsze drożej niż za zgodą (test na kilku kwotach).
  Stopa referencyjna (4%) to jedna stała w banki.yaml; `silnik.dane sprawdz` pilnuje limitów. Taka firma dostaje alarm,
  a w następnym tygodniu nie może inwestować, brać kredytów, leasingu ani zakładać lokat. Mistrz gry może jej
  przysłać inwestora ratunkowego albo zostaje Harpagon.
- Wolny limit debetu liczy się też przy ratach kredytów i leasingu: bez zgody rata, na którą nie stać, jest zaległa.

## Czego uczy (do planu zajęć)
- pojęcie z WOS / przedsiębiorczości: debet w rachunku, kredyt odnawialny, koszt pieniądza, płynność finansowa,
  odsetki karne, zdolność kredytowa, ryzyko
- pytanie do omówienia na lekcji: kiedy debet to rozsądne narzędzie, a kiedy pułapka? Czym różni się od kredytu?
- krótkie zadanie dla drużyn: policzcie, ile kosztuje trzy tygodnie na minusie w dwóch różnych bankach.

## Do promocji
„Debet nie włącza się sam. Kto nie przeczytał umowy, płaci karne odsetki.”

## Nawiązanie literackie
Solaris (Lem, „Solaris”): bank z największym debetem, „bezkresny ocean” limitu, ale nieprzewidywalny koszt.

## Zmiany 14.11.2026 (decyzje autora)

### Dla ucznia
Gdy zmieniasz bank, a na koncie jest otwarty debet, bank nie przechodzi nad tym do porządku dziennego. Jeśli masz dość
gotówki, debet jest najpierw spłacany w starym banku. Jeśli nie masz, nowy bank przejmuje dług, ale pobiera za to
jednorazową opłatę: 2% kwoty debetu, nie mniej niż najmniejsza opłata za debet w ofercie banków. Opłata jest kosztem firmy.

### Zasada działania
- `silnik/pieniadze/banki.py`, `poczatek_rundy`: przy zmianie banku (stary bank istnieje, nowy jest inny, `debet > 0`) wywołuje
  `_debet_przy_zmianie`. Gotówka ≥ debet: operacja „Spłata debetu przed zmianą banku” (rodzaj „kredyty”, poza KPiR), debet = 0.
  Gotówka < debet: debet przechodzi do nowego banku, opłata `max(najmniejsza opłata debetu, 2% × debet)` w KPiR jako „Opłata za
  przejęcie debetu przez bank …” (dokument typu „Wyciąg bankowy”).
- Komunikat dla gracza jest w wynikach rundy (`bank.poczatek.debet_przy_zmianie.komunikat`), pisany bezosobowo.
- Pierwszy wybór banku i zmiana banku bez debetu nie kosztują nic.
- Uwaga: dług, który idzie z firmą, dalej podlega zwykłym zasadom nowego banku (limit i oprocentowanie nowego banku,
  ponad limit odsetki karne).

### Liczby i źródła
| Parametr | Wartość | Pewność | Plik | Źródło |
|---|---|---|---|---|
| opłata za przejęcie debetu | 2% kwoty, minimum = najmniejsza opłata za debet w bankach (40 zł) | założenie | `dane/mapa/banki.yaml` (`przejecie_debetu`) | decyzja autora 14.11.2026; prowizja za refinansowanie zadłużenia bywa rzędu 1–3% |

### Czego uczy
- refinansowanie długu i koszt przenoszenia zadłużenia do innego banku; dlaczego „tańszy bank” nie zawsze się opłaca,
  gdy trzeba uwzględnić koszt zmiany
- pytanie na lekcji: przy jakiej kwocie debetu zmiana banku na tańszy zwraca się w ciągu miesiąca?
