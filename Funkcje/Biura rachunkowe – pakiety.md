# Biura rachunkowe – pakiety

- **Stan:** w grze (PR #2 i #5, 14.11.2026); widok opłaty za zmianę biura od 16.11
- **Gdzie w grze:** dziś Biurowiec przy Zana → biura rachunkowe; docelowo osobna kamienica z szyldami (decyzja 16.11)

## Dla ucznia (do instrukcji)
Firma może księgować sama albo oddać papiery biuru. Każde z czterech biur ma trzy pakiety: S, M i L. Pakiet to
miesięczna cena, limit dokumentów i dopłata za każdy dokument ponad limit. Mała firma bierze S, firma z dużym ruchem
L. Biura różnią się charakterem: jedno jest tanie, ale wszystko trwa, inne zamknięte w święta, jeszcze inne dokładne
i drogie.

Zmiana biura kosztuje. Za przejście do nowego biura płaci się jednorazowo tyle, ile wynosi tydzień jego pakietu.
Pierwszy wybór biura jest bez opłaty, a powrót do dawnego biura kosztuje tak samo jak każda zmiana.

## Zasada działania
- Opłata za tydzień = cena pakietu (przeliczona z miesiąca na tydzień) + dopłata za każdy dokument ponad limit
  pakietu + opłata za kadry (za każdego pracownika; część biur ma kilka osób w cenie).
- Pakiety: S – 60, M – 120, L – 200 dokumentów w miesiącu (w tygodniu ok. 14, 28 i 46).
- Cztery biura:

| Biuro | Cechy |
|---|---|
| J.K.Ś. | dokładne i uczciwe, z ubezpieczeniem OC, kadry do czterech osób w cenie. Tańsze od Asteroidy przy małej liczbie dokumentów, ale dolicza za nadmiar |
| Józef K. | tanie, ale wszystko trwa: zmiana pakietu wchodzi dopiero po dwóch tygodniach; bez OC, ryzyko błędu 4% |
| Scrooge | najtańsze, bez OC. W tygodniu ze świętem zamknięte: dokumenty czekają na następny tydzień z dopłatą 6 zł za dokument. Limit pakietu liczy się od nowa w każdym tygodniu, więc przeniesione dokumenty mogą dać drugą dopłatę ponad limit. Dokumenty z ostatniej rundy są rozliczane przy zamknięciu gry, nic nie przepada |
| Asteroida 328 | dokładne i drogie, nigdy się nie myli, **bez limitu dokumentów** (`bez_limitu: true`), OC, kadry do sześciu osób w cenie |

- Pomyłka biura w deklaracji kosztuje mandat. Biuro z OC oddaje go w tym samym tygodniu.
- **Opłata za zmianę biura:** jednorazowo jeden tydzień pakietu nowego biura, liczona przy pierwszym rozliczeniu
  w nowym biurze. To koszt usług obcych z dokumentem do KPiR („Koszt biura rachunkowego: opłata za zmianę biura”,
  VAT 23%). Przejście na samodzielną księgowość nic nie kosztuje, a gra pamięta ostatnie biuro (`ostatnie_biuro`):
  powrót po przerwie do tego samego biura jest bez opłaty, do innego płatny. Samodzielna księgowość nie służy więc
  do obejścia opłaty.
- **Józef K., opóźnienie zmiany pakietu:** pierwszy jawny wybór pakietu zawsze się zapisuje (także równy domyślnemu
  M), więc nie da się go potem „zmienić od razu”. Zapowiedź zmiany pakietu nie znika po wyjściu do innego biura.
  Obejście przez dwa płatne przeskoki kosztuje więcej niż dwa tygodnie czekania.

## Liczby i źródła
| Parametr | Wartość | Pewność | Plik | Źródło |
|---|---|---|---|---|
| ceny pakietów | ok. 300 zł netto miesięcznie przy kilkunastu dokumentach, ok. 1 000 zł przy 90–100 | założenie | `dane/mapa/biura.yaml` | oferty biur z Lublina i okolic na 2026 rok |
| dopłata Scrooge'a po święcie | 6 zł za dokument | założenie | `dane/mapa/biura.yaml` | decyzja autora 14.11.2026 |
| opłata za zmianę biura | 1 tydzień pakietu nowego biura | założenie | `dane/mapa/biura.yaml` (`zmiana_biura`) | decyzja autora 14.11.2026 |
| Asteroida 328 bez limitu | tak | decyzja | `dane/mapa/biura.yaml` (`bez_limitu`) | decyzja autora 14.11.2026 |

## Czego uczy (do planu zajęć)
- pojęcia: księgowość firmy, Księga przychodów i rozchodów, VAT i PIT, outsourcing usług, koszt stały a zmienny,
  ubezpieczenie OC, kara za błąd w deklaracji, koszt zmiany dostawcy, umowa o stałej cenie a rozliczenie za sztukę
- pytania do omówienia: kiedy opłaca się większy pakiet, a kiedy tańsze biuro z ryzykiem pomyłki? Kiedy warto
  zapłacić za zmianę biura, żeby oszczędzić na dokumentach?
- krótkie zadanie dla drużyn: policzcie dla swojej firmy, który pakiet i które biuro kosztuje najmniej przy 30
  dokumentach w tygodniu.

## Do promocji
„Cztery biura, trzy pakiety i jeden urząd skarbowy, który nie zapomina.”

## Nawiązanie literackie
J.K.Ś. – biuro z życzenia autora gry; Józef K. – Kafka, „Proces” (biurokracja bez końca); Scrooge – Dickens,
„Opowieść wigilijna” (skąpiec, w święta zamknięte); Asteroida 328 – Saint-Exupéry, „Mały Książę” (Bankier liczący gwiazdy).

## Otwarte
Skoro Asteroida nie ma limitu, jej pakiety M i L nie mają sensu (zawsze wygrywa S). Sprawa jest w [[Do decyzji]].
