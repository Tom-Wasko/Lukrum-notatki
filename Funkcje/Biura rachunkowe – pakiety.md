# Biura rachunkowe – pakiety

- **Stan:** na gałęzi mechaniki-a, czeka na zatwierdzenie
- **Gdzie w grze:** Księgowość ▸ Biuro rachunkowe; w mieście Kamienica biur rachunkowych

## Dla ucznia (do instrukcji)
Firma może księgować sama albo oddać papiery biuru. Każde z czterech biur ma trzy pakiety: S, M i L. Pakiet to
miesięczna cena, limit dokumentów i dopłata za każdy dokument ponad limit. Mała firma bierze S, firma z dużym ruchem
L. Biura różnią się charakterem: jedno jest tanie, ale wszystko trwa, inne zamknięte w święta, jeszcze inne dokładne
i drogie.

## Zasada działania
- Opłata za tydzień = cena pakietu (przeliczona z miesiąca na tydzień) + dopłata za każdy dokument ponad limit
  pakietu + opłata za kadry (za każdego pracownika, część biur ma kilka osób w cenie).
- Pakiety są w trzech rozmiarach: S – 60, M – 120, L – 200 dokumentów w miesiącu (w tygodniu ok. 14, 28 i 46).
- Cztery biura:

| Biuro | Cechy |
|---|---|
| J.K.Ś. | dokładne i uczciwe, z ubezpieczeniem OC, kadry do czterech osób w cenie (życzenie autora) |
| Józef K. | tanie, ale wszystko trwa: zmiana pakietu wchodzi dopiero po dwóch tygodniach; bez OC, ryzyko błędu 4% |
| Scrooge | najtańsze; w tygodniu ze świętem zamknięte: dokumenty czekają na następny tydzień z dopłatą 6 zł za dokument (od 14.11), a limit pakietu liczony jest od nowa w każdym tygodniu, więc to bywa drożej (ukryta druga dopłata ponad limit). W ostatniej rundzie rozlicza wszystko przy zamknięciu gry; bez OC |
| Asteroida 328 | dokładne i drogie, nigdy się nie myli, bez limitu dokumentów (od 14.11), OC, kadry do sześciu osób w cenie |

- Pomyłka biura w deklaracji kosztuje mandat. Biuro z OC oddaje go w tym samym tygodniu.
- Ceny wzorowane na ofertach biur z Lublina i okolic na 2026 rok (kb.pl, cenniki biur rachunkowych): ok. 300 zł netto
  miesięcznie przy kilkunastu dokumentach i ok. 1 000 zł netto przy 90–100 dokumentach.

## Czego uczy (do planu zajęć)
- pojęcie z WOS / przedsiębiorczości: księgowość firmy, Księga przychodów i rozchodów, VAT i PIT, outsourcing usług,
  koszt stały a zmienny, ubezpieczenie OC, kara za błąd w deklaracji
- pytanie do omówienia na lekcji: kiedy opłaca się większy pakiet, a kiedy tańsze biuro z ryzykiem pomyłki?
- krótkie zadanie dla drużyn: policzcie dla swojej firmy, który pakiet i które biuro kosztuje najmniej przy 30 dokumentach
  w tygodniu.

## Do promocji
„Cztery biura, trzy pakiety i jeden urząd skarbowy, który nie zapomina.”

## Nawiązanie literackie
J.K.Ś. – biuro z życzenia autora gry; Józef K. – Kafka, „Proces” (biurokracja bez końca); Scrooge – Dickens,
„Opowieść wigilijna” (skąpiec, w święta zamknięte); Asteroida 328 – Saint-Exupéry, „Mały Książę” (Bankier liczący gwiazdy).

## Zmiany 14.11.2026 (decyzje autora)

### Dla ucznia
Zmiana biura kosztuje. Za przejście do nowego biura płacisz jednorazowo tyle, ile wynosi tydzień jego pakietu. Pierwszy wybór
biura na starcie jest bez opłaty, a powrót do dawnego biura jest płatny tak samo jak każda zmiana. Asteroida 328 nie liczy
dokumentów: ma jedną cenę pakietu i nigdy nie dolicza za dokumenty ponad limit. Scrooge w tygodniu ze świętem jest zamknięty
i dolicza 6 zł za każdy dokument, który czekał.

### Zasada działania
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

### Liczby i źródła
| Parametr | Wartość | Pewność | Plik | Źródło |
|---|---|---|---|---|
| dopłata Scrooge'a po święcie | 6 zł za dokument | założenie | `dane/mapa/biura.yaml` | decyzja autora 14.11.2026 |
| opłata za zmianę biura | 1 tydzień pakietu nowego biura | założenie | `dane/mapa/biura.yaml` (`zmiana_biura`) | decyzja autora 14.11.2026 |
| Asteroida 328 bez limitu | tak | decyzja | `dane/mapa/biura.yaml` (`bez_limitu`) | decyzja autora 14.11.2026 |

### Czego uczy
- koszty zmiany dostawcy usług (switching costs), umowa o stałej cenie a rozliczenie za sztukę
- pytanie na lekcji: kiedy opłaca się zapłacić za zmianę biura, żeby oszczędzić na dokumentach?
