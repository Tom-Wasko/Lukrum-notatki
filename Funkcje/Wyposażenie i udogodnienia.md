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
  cennik. Pomiar: `archiwum/notatki-wycofane/Analizy/Noc Fable 15-16.11/pomiary/katalogi.md` (poza gitem).
- Boty kupują tylko tyle wyposażenia, ile ma ich strategia (decyzja 14.11).

## Liczby i źródła
Wszystkie ceny i koszty utrzymania są w `dane/katalog.yaml` (`udogodnienia`, `wyposazenie`, `szkolenia`), `dane/sprzet.yaml`
(sprzęt i poziomy ★) oraz `dane/mapa/reklama.yaml` (reklama); źródło każdej liczby jest w jej polu `zrodlo`.
Tabeli nie powielamy tu, żeby nie rozjeżdżała się z danymi. Przykłady (stan 16.11.2026): kiosk do zamówień 9 000 zł
(utrzymanie 150 zł), meble ogrodowe i parasole 6 000 zł, rożen ★★★ 10 000 zł.

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
