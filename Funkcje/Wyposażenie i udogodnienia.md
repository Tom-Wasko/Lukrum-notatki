# Wyposażenie i udogodnienia

- **Stan:** w grze (PR #2 i #5, 14.11.2026); ceny przeliczone od zera 15.11 (do oceny w grze testowej)
- **Gdzie w grze:** Park handlowy (wyposażenie i sprzęt), Mój kebab → Zaplecze (udogodnienia dla zespołu, szkolenia);
  gotowy lokal z zestawem sprzętu wybiera się przy najmie albo kupnie lokalu

## Dla ucznia (do instrukcji)
Lokal można doposażyć: ogródek z parasolami, ładowarki do telefonów, płatności BLIK, kiosk do zamówień, muzyka,
toaleta dla gości i dostawa przez aplikację. To przyciąga gości, ale każda rzecz kosztuje przy zakupie i co tydzień.
Zespołowi można dać karty sportowe i posiłki. Szkolenia kupuje się w trzech lubelskich firmach, a reklamę
w „Gazecie Pana Cogito” i w „Radiu Tichy”.

Gotowy lokal ma sprzęt od poprzedniego najemcy. Są trzy poziomy: ★ używany i skrzypiący, ★★ zadbany, ★★★
profesjonalny jak z dużej sieci. Sprzęt ★★★ można też dokupić do każdego lokalu. Kosztuje więcej niż ★★, za to
taniej się go utrzymuje. Każdy poziom to wybór z kosztem.

## Zasada działania
- Każda pozycja wyposażenia ma „procent gości, którym odpowiada”. Im więcej odpowiednich rzeczy, tym więcej gości
  wybiera lokal, z nasyceniem: pierwsze dają najwięcej.
- Udogodnienia (karta sportowa, posiłki) podnoszą zadowolenie zespołu w dziale „Zespół”, ale kosztują co tydzień.
- **Zestawy sprzętu gotowych lokali:** zestaw `profesjonalny` (★★★) ma ten sam układ stanowisk co `solidny` (jedna
  kuchnia, jedna kasa), ale cały sprzęt w jakości 3. Ceny i koszty utrzymania bierze z `sprzet.yaml`. Zestaw ★★★ ma
  na razie lokal `centrum_1` (Krakowskie Przedmieście, gra od 6 firm). Czynsz się nie zmienia, więc to dodatkowa
  wartość tego lokalu: założenie do oceny po grze testowej.
- **Jakość a cena (od 15.11):** składniki ★ kosztują 85%, a ★★★ 132% ceny ★★. Sprzęt i szkolenia mają uporządkowany
  cennik. Pomiar: `Analizy/Noc Fable 15-16.11/pomiary/katalogi.md`.
- Boty kupują tylko tyle wyposażenia, ile ma ich strategia (decyzja 14.11).

## Liczby i źródła
Źródło każdej liczby jest w polu `zrodlo` katalogu. Kwoty sprawdzone w danych gry 16.11.2026 (po przeliczeniu 15.11).

| Pozycja | Kwota | Plik i klucz |
|---|---|---|
| ekspres do kawy ziarnistej | 3 400 zł, utrzymanie 320 zł | `dane/katalog.yaml: udogodnienia` (Ekspres do kawy ziarnistej dla zespołu) |
| wiata rowerowa | 1 400 zł | `dane/katalog.yaml: udogodnienia` (Wiata rowerowa przy lokalu) |
| szatnia z szafkami | 1 300 zł | `dane/katalog.yaml: udogodnienia` (Szatnia z szafkami na klucz) |
| stoły i ławy z jasnego drewna | 3 100 zł | `dane/katalog.yaml: wyposazenie` |
| ekran z transmisją meczów Motoru Lublin | 2 900 zł, utrzymanie 120 zł | `dane/katalog.yaml: wyposazenie` |
| meble ogrodowe i parasole (ogródek) | 6 000 zł, utrzymanie 120 zł | `dane/katalog.yaml: wyposazenie` |
| kiosk do zamówień | 9 000 zł, utrzymanie 150 zł (rynkowo 8–10 tys. zł) | `dane/katalog.yaml: wyposazenie` |
| licencja muzyczna | 800 zł zakupu i 60 zł miesięcznie | `dane/katalog.yaml: wyposazenie` (Muzyka w lokalu) |
| szkolenia | 600–2 300 zł | `dane/katalog.yaml: szkolenia.pozycje[].ceny` |
| ogłoszenie ramkowe w „Gazecie Pana Cogito” | 90 zł za emisję | `dane/mapa/reklama.yaml: cena_emisji` |
| rożen ★★★, frytownica ★★★ | 10 000 zł, 6 500 zł | `dane/sprzet.yaml: sprzet.Rożen.ceny`, `sprzet.Frytownica.ceny` |

## Czego uczy (do planu zajęć)
- pojęcia: inwestycja a koszt bieżący, zwrot z inwestycji, nakład a koszt utrzymania, amortyzacja, segmentacja
  klientów, marketing lokalny, motywacja pracowników
- pytania do omówienia: który dodatek zwróci się najszybciej i skąd to wiecie? Czy opłaca się wziąć lokal z dobrym
  sprzętem, jeśli czynsz jest wyższy?
- krótkie zadania dla drużyn: policzcie, po ilu tygodniach zwróci się kiosk do zamówień przy 600 gościach tygodniowo.
  Policzcie, po ilu rundach droższy rożen ★★★ odrobi różnicę ceny dzięki niższemu utrzymaniu.

## Do promocji
„Ogródek, BLIK i Radio Tichy: wszystko, czego brakowało kebabowi w Lublinie.”
„Od używanego rożna do kuchni jak z sieciówki: trzy poziomy sprzętu.”

## Nawiązanie literackie
„Gazeta Pana Cogito” (Herbert, „Pan Cogito”) i „Radio Tichy” (Lem, „Dzienniki gwiazdowe”).
