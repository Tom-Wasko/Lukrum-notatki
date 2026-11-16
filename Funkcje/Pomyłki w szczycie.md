# Pomyłki w szczycie

- **Stan:** w grze (PR #2 i #5, 14.11.2026); częstości do oceny po grze testowej
- **Gdzie w grze:** wyniki sprzedaży (kolumna „Pomyłki w szczycie”), wnioski z tygodnia, księga gości

## Dla ucznia (do instrukcji)
Kiedy w lokalu jest tłok, kucharze się mylą: kebab trzeba zrobić drugi raz, a gość czeka dłużej i jest mniej
zadowolony. Pomyłek jest więcej, gdy kuchnia jest przeciążona, załoga zmęczona nadgodzinami i nikt nie był na szkoleniu.

Pomyłka zużywa składniki drugi raz. Jeśli składników starcza tylko dla klientów i na powtórkę nie ma z czego,
zepsuta porcja przepada razem z klientem: wychodzi bez dania, a składniki i tak zostały zużyte. Dlatego zapas „na
styk” kosztuje więcej, niż widać w prognozie.

## Zasada działania
- Każde danie ma szansę na pomyłkę: skłonność kucharza (kilka procent) + dodatek za przeciążoną kuchnię (od 90%
  obciążenia, do +4 pp) + dodatek za zmęczenie (wykorzystanie czasu pracy ponad 85%, do +2,5 pp) + 1 pp, gdy firma
  nie ma żadnego szkolenia.
- Pomiar botów (14.11.2026): dobrze obsadzona firma myli się w ok. 2–4% porcji, przeciążona w ok. 10%.
- W opiniach gości pomyłki ważą 2,5 gwiazdki na cały udział (kolejka 4,0): 10% pomyłek to ok. −0,25★.
- Pomyłka obniża zadowolenie gości (dział „Goście” w wyniku punktowym) i ocenę lokalu.
- **Gdy brakuje składników na powtórkę** (`silnik/kuchnia/operacje.py`): dla każdego składnika liczony jest zapas
  ponad potrzeby obsłużonych klientów. Pomyłka, której powtórka mieści się w zapasie, zużywa składniki. Pomyłka,
  której powtórka się nie mieści, zmniejsza liczbę obsłużonych klientów o jednego (przyczyna utraty: „pomyłka bez
  składników na powtórkę dania”), a składniki zepsutej porcji i tak schodzą z magazynu.
- Rada dla gracza: dodać kucharza albo stanowisko, nie przepracowywać ludzi, kupić szkolenie.

## Liczby i źródła
| Parametr | Wartość | Pewność | Plik | Źródło |
|---|---|---|---|---|
| częstość pomyłek | 5,2% i 2,8% | założenie | `dane/zalozenia.yaml` (`pomylki.szansa`) | decyzja autora 14.11.2026: zostaje do testu gotowej gry |
| waga pomyłek w opinii | 2,5★ na cały udział | skalibrowane | `dane/mapa/klienci.yaml` | pomiar botów 14.11.2026 |

## Czego uczy (do planu zajęć)
- pojęcia: jakość usługi, koszt złej jakości, przeciążenie pracowników, szkolenia, zarządzanie ryzykiem, zapas
  bezpieczeństwa, strata materiałowa a utracona sprzedaż
- pytania do omówienia: czy opłaca się sprzedać więcej, jeśli rośnie liczba pomyłek? Ile zapasu ponad prognozę warto
  trzymać?
- krótkie zadanie dla drużyn: znajdźcie w tabeli sprzedaży dzień z największą liczbą pomyłek i zaproponujcie dwie zmiany.

## Do promocji
„Tłok w kuchni to nie wymówka. To kosztuje.”

## Nawiązanie literackie
Brak.
