# Pomyłki w szczycie

- **Stan:** na gałęzi mechaniki-a, czeka na zatwierdzenie
- **Gdzie w grze:** Sprzedaż (kolumna „Pomyłki w szczycie”), Wnioski z tygodnia

## Dla ucznia (do instrukcji)
Kiedy w lokalu jest tłok, kucharze się mylą: kebab trzeba zrobić drugi raz, a gość czeka dłużej i jest mniej zadowolony.
Pomyłek jest więcej, gdy kuchnia jest przeciążona, załoga zmęczona nadgodzinami i nikt nie był na szkoleniu.

## Zasada działania
Każde danie ma szansę na pomyłkę: skłonność kucharza (kilka procent) plus dodatek za przeciążoną kuchnię (od 90% obciążenia, do +4 pp),
plus dodatek za zmęczenie (wykorzystanie czasu pracy ponad 85%, do +2,5 pp), plus +1 pp, gdy firma nie ma żadnego szkolenia.
Po pomiarze botów (14.11.2026): dobrze obsadzona firma myli się w ok. 2–4% porcji, przeciążona w ok. 10%. W opiniach gości pomyłki
ważą 2,5 gwiazdki na cały udział (kolejka 4,0): 10% pomyłek to ok. −0,25★, a nie −1,6★ jak przy starej wadze.
Pomyłka zużywa składniki jeszcze raz i obniża zadowolenie gości (dział „Goście” w wyniku punktowym) i ocenę lokalu.
Rada: dodać kucharza albo stanowisko, nie przepracowywać ludzi, kupić szkolenie.

## Czego uczy (do planu zajęć)
- pojęcie z WOS / przedsiębiorczości: jakość usługi, koszt złej jakości, przeciążenie pracowników, szkolenia pracownicze, zarządzanie ryzykiem
- pytanie do omówienia na lekcji: czy opłaca się sprzedać więcej, jeśli rośnie liczba pomyłek?
- krótkie zadanie dla drużyn: znajdźcie w tabeli sprzedaży dzień z największą liczbą pomyłek i zaproponujcie dwie zmiany.

## Do promocji
„Tłok w kuchni to nie wymówka. To kosztuje.”

## Nawiązanie literackie
Brak.

## Zmiany 14.11.2026 (decyzje autora)

### Dla ucznia
Pomyłka to danie zrobione drugi raz, więc zużywa dodatkowe składniki. Jeśli składników starcza tylko dla klientów
i na powtórkę nie ma z czego, zepsuta porcja przepada razem z klientem: wychodzi bez dania, a składniki i tak zostały zużyte.
Dlatego zapas „na styk” kosztuje więcej, niż widać w prognozie.

### Zasada działania
- `silnik/kuchnia/operacje.py`, po losowaniu pomyłek. Dla każdego składnika liczony jest zapas ponad potrzeby obsłużonych
  klientów. Każda pomyłka, której powtórka mieści się w zapasie, zużywa składniki (jak dotąd). Każda pomyłka, której
  powtórka się nie mieści, zmniejsza liczbę obsłużonych klientów o jednego (przyczyna utraty: „pomyłka bez składników na
  powtórkę dania”), a składniki zepsutej porcji i tak schodzą z magazynu.
- Liczba pomyłek (opinie, zadowolenie gości, częstości 5,2% i 2,8%) bez zmian. Zmiana dotyczy tylko skutku, gdy brakuje
  składników. Zużycie = obsłużeni + pomyłki zostaje poprawne w obu przypadkach, bo zepsuta porcja zajmuje miejsce klienta.
- Wybrane jako najprostsze spójne rozwiązanie: nie wymaga nowych liczb w danych i działa tak samo dla wszystkich dań.

### Liczby i źródła
Brak nowych liczb gry. Częstości pomyłek: `dane/zalozenia.yaml` (`pomylki.szansa`), bez zmian.

### Czego uczy
- koszt braku zapasu bezpieczeństwa (safety stock), strata materiałowa a utracona sprzedaż
- pytanie na lekcji: ile zapasu ponad prognozę opłaca się trzymać, skoro pomyłki zdarzają się w szczycie?
