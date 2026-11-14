# Pomyłki w szczycie: nowy fragment, pomyłka przy pustym magazynie (decyzja autora 14.11)

Plik do uzupełnienia: `notatki/Funkcje/Pomyłki w szczycie.md` (dopisać do „Zasady działania”).

## Dla ucznia (dopisać do instrukcji)
Pomyłka to danie zrobione drugi raz, więc zużywa dodatkowe składniki. Jeśli składników starcza tylko dla klientów
i na powtórkę nie ma z czego, zepsuta porcja przepada razem z klientem: wychodzi bez dania, a składniki i tak zostały zużyte.
Dlatego zapas „na styk” kosztuje więcej, niż widać w prognozie.

## Zasada działania
- `silnik/kuchnia/operacje.py`, po losowaniu pomyłek. Dla każdego składnika liczony jest zapas ponad potrzeby obsłużonych
  klientów. Każda pomyłka, której powtórka mieści się w zapasie, zużywa składniki (jak dotąd). Każda pomyłka, której
  powtórka się nie mieści, zmniejsza liczbę obsłużonych klientów o jednego (przyczyna utraty: „pomyłka bez składników na
  powtórkę dania”), a składniki zepsutej porcji i tak schodzą z magazynu.
- Liczba pomyłek (opinie, zadowolenie gości, częstości 5,2% i 2,8%) bez zmian. Zmiana dotyczy tylko skutku, gdy brakuje
  składników. Zużycie = obsłużeni + pomyłki zostaje poprawne w obu przypadkach, bo zepsuta porcja zajmuje miejsce klienta.
- Wybrane jako najprostsze spójne rozwiązanie: nie wymaga nowych liczb w danych i działa tak samo dla wszystkich dań.

## Liczby i źródła
Brak nowych liczb gry. Częstości pomyłek: `dane/zalozenia.yaml` (`pomylki.szansa`), bez zmian.

## Czego uczy (dopisać)
- koszt braku zapasu bezpieczeństwa (safety stock), strata materiałowa a utracona sprzedaż
- pytanie na lekcji: ile zapasu ponad prognozę opłaca się trzymać, skoro pomyłki zdarzają się w szczycie?
