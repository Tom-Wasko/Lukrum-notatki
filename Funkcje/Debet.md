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
