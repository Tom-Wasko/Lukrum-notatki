# Radio „Fala Koziołka”

- **Stan:** w grze (19.11.2026, gałąź `radio-odtwarzacz`)
- **Gdzie w grze:** lewy pasek pulpitu (ikona odbiornika) i ⚙ → Dźwięk; spis nagrań: strona `/nagrania-w-radiu`

## Dla ucznia (do instrukcji)
Na pasku jest radio z pięcioma stacjami: polskie pieśni i fortepian z płyt sprzed stu lat, wczesny jazz, muzyka
klasyczna, „Lalka” Prusa czytana po kolei i sam szum eteru. Między płytami odzywa się prowadzący z krótkimi
przypomnieniami o grze. Radio gra tylko dla nastroju i nie zmienia wyniku. Włącza się je przyciskiem.

## Zasada działania
- Dane: `dane/radio.yaml` (stacje, nagrania z autorem, wykonawcą, rokiem, źródłem i licencją, teksty prowadzącego).
  Silnik gry go nie czyta. `panel_gracza/radio.py` daje `/radio.json` dla odbiornika i stronę `/nagrania-w-radiu`.
  Obie strony są dostępne bez logowania.
- Pliki MP3 (mono) leżą w repozytorium gry (`panel_gracza/static/radio/<stacja>/`), więc radio działa bez internetu.
- Odbiornik (`static/pulpit/radio.js`):
  - stacje muzyczne grają w losowej kolejności;
  - słuchowisko gra po kolei i zapamiętuje miejsce w przeglądarce (localStorage);
  - szum robi przeglądarka (Web Audio), a przy zmianie stacji słychać trzask;
  - prowadzący to syntezator mowy przeglądarki z polskim głosem; co `co_ile` nagrań mówi wtrącenie i zapowiedź;
  - bez polskiego głosu tekst prowadzącego pokazuje się na ekraniku radia.
- Nic nie gra samo: radio rusza dopiero po kliknięciu ▶ Włącz albo stacji.
- Test `testy/aplikacja/test_radio.py` pilnuje, że:
  - każde nagranie ma pełny opis i dozwoloną licencję;
  - każdy plik z opisu istnieje i w paczce nie ma plików spoza opisu;
  - paczka ma mniej niż 80 MB;
  - nagrania „z mocy prawa” są sprzed 1926 r.

## Liczby i źródła
| Parametr | Wartość | Pewność | Plik | Źródło |
|---|---|---|---|---|
| Licencje dozwolone | domena publiczna, CC0, CC BY, CC BY-SA, LWS 1.3 | potwierdzone | `panel_gracza/radio.py` | decyzja szefa 19.11.2026 |
| Wiek nagrań bez znaku PD | do 1925 r. | potwierdzone | `dane/radio.yaml` | decyzja szefa 19.11.2026; prawo USA i art. 89–98 pr. aut. |
| Prowadzący co ile nagrań | 2 | założenie | `dane/radio.yaml` | do odsłuchu w grze testowej |
| Limit paczki | 80 MB | założenie | `test_radio.py` | decyzja 19.11 (~67 MB) |

Lista nagrań i podstawa prawna każdej pozycji: [[radio – lista nagrań]].

## Czego uczy (do planu zajęć)
- pojęcia: prawo autorskie i prawa pokrewne, domena publiczna, utwór anonimowy, wolne licencje (CC, Licencja Wolnej Sztuki)
- pytanie do omówienia na lekcji: dlaczego lokal może puszczać w sali nagranie z 1911 r. bez opłat, a przebój z radia
  już nie (ZAiKS, licencje na odtwarzanie publiczne)?
- krótkie zadanie dla drużyn: znaleźć na stronie „Nagrania w radiu” jedno nagranie z mocy prawa i jedno na wolnej
  licencji i wyjaśnić różnicę.

## Do promocji
W LUKRUM gra radio z płytami sprzed stu lat, a każde nagranie ma wpisane źródło i licencję.

## Nawiązanie literackie
„Lalka” Bolesława Prusa na stacji „Teatr przy mikrofonie”: Wokulski też był kupcem, który liczył zysk.

## Otwarte
Sprawy do decyzji mają jedno miejsce: [[Do decyzji]].
