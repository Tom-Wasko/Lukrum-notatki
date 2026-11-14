# Debet: nowy fragment, zmiana banku z otwartym debetem (decyzja autora 14.11)

Plik do uzupełnienia: `notatki/Funkcje/Debet.md` (dopisać do „Zasady działania” i akapit do „Dla ucznia”).

## Dla ucznia (dopisać do instrukcji)
Gdy zmieniasz bank, a na koncie jest otwarty debet, bank nie przechodzi nad tym do porządku dziennego. Jeśli masz dość
gotówki, debet jest najpierw spłacany w starym banku. Jeśli nie masz, nowy bank przejmuje dług, ale pobiera za to
jednorazową opłatę: 2% kwoty debetu, nie mniej niż najmniejsza opłata za debet w ofercie banków. Opłata jest kosztem firmy.

## Zasada działania
- `silnik/pieniadze/banki.py`, `poczatek_rundy`: przy zmianie banku (stary bank istnieje, nowy jest inny, `debet > 0`) wywołuje
  `_debet_przy_zmianie`. Gotówka ≥ debet: operacja „Spłata debetu przed zmianą banku” (rodzaj „kredyty”, poza KPiR), debet = 0.
  Gotówka < debet: debet przechodzi do nowego banku, opłata `max(najmniejsza opłata debetu, 2% × debet)` w KPiR jako „Opłata za
  przejęcie debetu przez bank …” (dokument typu „Wyciąg bankowy”).
- Komunikat dla gracza jest w wynikach rundy (`bank.poczatek.debet_przy_zmianie.komunikat`), pisany bezosobowo.
- Pierwszy wybór banku i zmiana banku bez debetu nie kosztują nic.
- Uwaga: dług, który idzie z firmą, dalej podlega zwykłym zasadom nowego banku (limit i oprocentowanie nowego banku,
  ponad limit odsetki karne).

## Liczby i źródła
| Parametr | Wartość | Pewność | Plik | Źródło |
|---|---|---|---|---|
| opłata za przejęcie debetu | 2% kwoty, minimum = najmniejsza opłata za debet w bankach (40 zł) | założenie | `dane/mapa/banki.yaml` (`przejecie_debetu`) | decyzja autora 14.11.2026; prowizja za refinansowanie zadłużenia bywa rzędu 1–3% |

## Czego uczy (dopisać)
- refinansowanie długu i koszt przenoszenia zadłużenia do innego banku; dlaczego „tańszy bank” nie zawsze się opłaca,
  gdy trzeba uwzględnić koszt zmiany
- pytanie na lekcji: przy jakiej kwocie debetu zmiana banku na tańszy zwraca się w ciągu miesiąca?
