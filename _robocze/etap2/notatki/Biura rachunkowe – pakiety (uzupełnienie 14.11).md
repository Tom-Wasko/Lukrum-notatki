# Biura rachunkowe – pakiety: nowy fragment (decyzje autora 14.11)

Plik do uzupełnienia: `notatki/Funkcje/Biura rachunkowe – pakiety.md`. Podmienić w tabeli wiersze Scrooge'a i Asteroidy,
dopisać poniższe punkty do „Zasady działania” i akapit do „Dla ucznia”.

## Dla ucznia (dopisać do instrukcji)
Zmiana biura kosztuje. Za przejście do nowego biura płacisz jednorazowo tyle, ile wynosi tydzień jego pakietu. Pierwszy wybór
biura na starcie jest bez opłaty, a powrót do dawnego biura jest płatny tak samo jak każda zmiana. Asteroida 328 nie liczy
dokumentów: ma jedną cenę pakietu i nigdy nie dolicza za dokumenty ponad limit. Scrooge w tygodniu ze świętem jest zamknięty
i dolicza 6 zł za każdy dokument, który czekał.

## Zasada działania (nowe punkty)
- **Scrooge:** dopłata za dokument przeniesiony po święcie wynosi 6 zł (było 3 zł). Dokumenty przeniesione z ostatniej
  rundy gry są rozliczone w ostatniej rundzie, więc nic nie przepada.
- **Asteroida 328:** pakiety mają `bez_limitu: true`, więc dopłata za dokumenty ponad limit nie występuje. To jej przewaga
  nad J.K.Ś., które jest tańsze przy małej liczbie dokumentów, ale dolicza za nadmiar. Uwaga projektowa: skoro limit nie
  ma znaczenia, pakiety M i L Asteroidy nie mają sensu (zawsze wygrywa S). Do decyzji autora, czy je różnicować.
- **Opłata za zmianę biura:** jednorazowo `tygodni_pakietu` (1) × tydzień pakietu NOWEGO biura, liczona przy pierwszym
  rozliczeniu w nowym biurze. Koszt usług obcych, z dokumentem do KPiR „Koszt biura rachunkowego: opłata za zmianę biura”
  (VAT 23%). Pierwszy wybór biura w grze jest bez opłaty. Powrót płatny. Przejście na samodzielną księgowość nic nie
  kosztuje, a gra pamięta „ostatnie biuro” (`ostatnie_biuro`): powrót po przerwie do tego samego biura jest bez opłaty,
  do innego – płatny. Samodzielna księgowość nie służy więc do obejścia opłaty przy zmianie biura A na B.
- **Józef K., opóźnienie zmiany pakietu:** pierwszy jawny wybór pakietu w grze zawsze się zapisuje (także równy
  domyślnemu M), więc nie da się go potem „zmienić od razu”. Zapowiedź zmiany pakietu nie znika po wyjściu do innego biura:
  nowa decyzja w biurze bez opóźnienia zmienia pakiet docelowy, ale nie termin. Obejście przez dwa płatne przeskoki
  kosztuje więcej niż dwa tygodnie czekania.

## Liczby i źródła
| Parametr | Wartość | Pewność | Plik | Źródło |
|---|---|---|---|---|
| dopłata Scrooge'a po święcie | 6 zł za dokument | założenie | `dane/mapa/biura.yaml` | decyzja autora 14.11.2026 |
| opłata za zmianę biura | 1 tydzień pakietu nowego biura | założenie | `dane/mapa/biura.yaml` (`zmiana_biura`) | decyzja autora 14.11.2026 |
| Asteroida 328 bez limitu | tak | decyzja | `dane/mapa/biura.yaml` (`bez_limitu`) | decyzja autora 14.11.2026 |

## Czego uczy (dopisać)
- koszty zmiany dostawcy usług (switching costs), umowa o stałej cenie a rozliczenie za sztukę
- pytanie na lekcji: kiedy opłaca się zapłacić za zmianę biura, żeby oszczędzić na dokumentach?
