# Katalogi przeliczone od zera (15.11.2026)

Kopia robocza `fable-katalogi`, gałąź `fable-katalogi` (bez commitów). Pomiar: `pomiary/katalogi.md`.

## 1. Efekt w silniku (inwentaryzacja)

- **Sprzęt kuchni (Rożen, Frytownica, Lodówka)**: jedyny efekt to jakość dania. Waga sprzętu w jakości dania to 0,4, a współczynniki gwiazdek to 0,52 / 0,65 / 0,83 (`zalozenia.yaml: popyt`). Daje to ★→★★ około +9% popytu na dania na tym sprzęcie i ★★→★★★ około +11%. Do tego utrzymanie miesięczne (`runda.py`, "Koszty utrzymania sprzętu"). Awarii sprzętu silnik nie modeluje, więc "wadą ★" jest wyższe utrzymanie (serwis) i słabsze dania.
- **Szafa chłodnicza i zamrażarka**: jedyny efekt to `pojemnosc_l`. Nadmiar towaru jedzie do wynajętej chłodni po 1 zł/l przy dostawie. Gwiazdki nie wpływają na jakość dań.
- **Kasa fiskalna, Lada, Tablica menu**: silnik nie daje jakości kasy żadnego efektu na popyt ani tempo. Jakość sprzętu stanowiska wchodzi tylko do zadowolenia osoby (0,02 za gwiazdkę ponad 3★) i przez nie do odejść i tempa.
- **Składniki ★/★★/★★★**: waga 0,6 w jakości dania. ★→★★ to około +12% popytu, ★★→★★★ około +17%. Jakość dania liczy się ze średniej gwiazdek wszystkich składników.
- **Szkolenia**: efekt zależy tylko od `procent`. Ocena firmy (`zadowoleni_klienci`) nie ma żadnego efektu mechanicznego.
- **Udogodnienia, wyposażenie, pakiety stanowisk**: to pozycje jednopoziomowe, bez jakości ★. Zostawione.
- **Zestawy lokali (`mapa/lokale.yaml`)**: opisują tylko jakość sprzętu (liczba 1–3), bez cen. Cena wynika z `sprzet.yaml`, więc pola nie ruszałem.
- **Boty** (`boty.yaml`) kupują jakość na sztywno: tani ★, zrównoważony ★★, naśladowca ★★, premium ★★★, agresywny ★★★. Bot, który zaczyna z zestawem ★, zostaje przy ★. Boty niezmienione.

## 2. Tabela zmian

Zwrot dopłaty to tygodnie względem poprzedniego poziomu. Założenia: marża tygodniowa dań na jednej sztuce to rożen 3 500 zł, frytownica 2 800 zł, lodówka 900 zł (kalibracja z przebiegu bota średniego: 350–550 porcji na rożen, wynik tygodnia 1 100 porcji). Utrzymanie przeliczone z miesiąca na tydzień (÷4,33).

| pozycja | poziom | było (zakup / utrz. mies.) | jest | zwrot dopłaty (tyg.) |
|---|---|---|---|---|
| Rożen | ★ | 2 500 / 60 | 2 500 / 120 | punkt wyjścia |
| Rożen | ★★ | 4 500 / 40 | 4 500 / 55 | ok. 6 |
| Rożen | ★★★ | 7 000 / 30 | 10 000 / 25 | ok. 14 (2,2×) |
| Frytownica | ★ | 1 500 / 40 | 1 500 / 90 | punkt wyjścia |
| Frytownica | ★★ | 2 800 / 30 | 2 800 / 45 | ok. 5 |
| Frytownica | ★★★ | 4 500 / 20 | 6 500 / 20 | ok. 12 (2,3×) |
| Lodówka na napoje | ★ | 1 200 / 30 | 1 000 / 60 | punkt wyjścia |
| Lodówka na napoje | ★★ | 2 000 / 25 | 1 600 / 35 | ok. 7 |
| Lodówka na napoje | ★★★ | 3 200 / 20 | 3 600 / 15 | ok. 18 (2,25×); napój to mała marża, więc pozycja dla dużego ruchu |
| Szafa chłodnicza | ★ / ★★ | 2 200 i 3 500 (600 / 800 l) | bez zmiany ceny i pojemności, utrzymanie 90 / 55 | pojemność zamiast popytu |
| Szafa chłodnicza | ★★★ | 5 200 (1 000 l) / 35 | 7 800 (1 400 l) / 30 | zwraca się tylko przy stałym nadmiarze towaru ponad 500 l (wynajem 1 zł/l) |
| Zamrażarka | ★ / ★★ | 1 400 i 2 200 (250 / 300 l) | bez zmiany ceny i pojemności, utrzymanie 70 / 40 | pojemność zamiast popytu |
| Zamrażarka | ★★★ | 3 400 (400 l) / 25 | 4 800 (600 l) / 20 | jak szafa |
| Kasa fiskalna | ★ / ★★ / ★★★ | 900 / 1 500 / 2 400, utrz. 20 / 10 / 0 | 900 / 1 500 / 3 300, utrz. 70 / 30 / 5 | brak efektu na popyt (patrz wątpliwości) |
| Lada z witryną | ★ / ★★ / ★★★ | 1 500 / 2 500 / 4 000, utrz. 15 / 10 / 5 | 1 500 / 2 500 / 5 500, utrz. 40 / 20 / 5 | jak kasa |
| Tablica menu | ★ / ★★ / ★★★ | 300 / 600 / 1 200 | 300 / 600 / 1 400, utrz. 10 / 0 / 0 | jak kasa |
| Składniki, wszystkie | ★ | ok. 0,88 ceny ★★ | 0,85 ceny ★★ | −3% ceny, −12% popytu: tanio, ale słabiej |
| Składniki, wszystkie | ★★ | punkt odniesienia | bez zmiany | |
| Składniki, wszystkie | ★★★ | ok. 1,18 ceny ★★ | 1,32 ceny ★★ | dopłata ok. 1,5–2 zł za porcję, zwrot z marży 15 zł × 17% = ok. 2,5 zł; opłaca się przy wolnych mocach albo wyższej cenie dania |
| Szkolenia, 8 pozycji | firmy | trzecia firma bywała droższa od drugiej przy niższej ocenie | Lubelska Szkoła Kebabu ok. +20% względem Rożen i Rozum, HACCP w Pięć Minut ok. −10% | wybór: cena kontra ocena; druga firma (domyślna botów) bez zmiany |

Składniki zmieniono w `zasoby.yaml` (`srednie_ceny`) i w `dostawcy.yaml` (ceny z października, u 8 dostawców). Dyskonty mają tylko ★/★★, hurtownie ★/★★/★★★, a zakłady mięsne ★★/★★★. Ceny ★★ bez zmian.

## 3. Pliki i testy

- Zmienione: `gra/dane/sprzet.yaml` (przepisany generatorem, pola `zrodlo` i `opis` poprawione), `gra/dane/zasoby.yaml`, `gra/dane/dostawcy.yaml` (ceny jakości i `zrodlo`), `gra/dane/katalog.yaml` (tylko ceny szkoleń i `zrodlo` szkoleń).
- Nie ruszałem `podatki_2026.yaml`, `mapa/*`, kodu, frontu ani testów.
- Testów nie zmieniałem. Wszystkie przeszły (pełny przebieg bez `-x` nie zgłosił błędów, kolumna do 100%). `ruff check .` czysty, `silnik.dane sprawdz` w porządku.
- `pewnosc` w `sprzet.yaml`, `zasoby.yaml`, `dostawcy.yaml` nie istnieje, bo pliki mają tylko `zrodlo`. Poprawiłem `zrodlo` i `opis`.

## 4. Pomiar przed i po (12 tygodni, ziarna 7, 11, 23)

Pełna tabela jest w `pomiary/katalogi.md`.

| poziom | średnia gotówka przed | po | zmiana |
|---|---|---|---|
| łatwy | 37 147 | 35 827 | −3,6% |
| średni | 67 184 | 61 387 | −8,6% |
| trudny | 83 264 | 79 894 | −4,0% |

Średnia według strategii (gotówka, wynik): zrównoważony 77 135 → 76 227 (657 → 654); tani 72 992 → 74 904 (542 → 546); premium 46 543 → 37 985 (591 → 581); agresywny 36 037 → 24 402 (553 → 513); naśladowca 79 952 → 81 662 (667 → 669).

- Kolejność strategii nie odwraca się. Zrównoważony i naśladowca są nadal na górze, premium nie jest najlepsze ani bezużyteczne (wynik w punktach prawie bez zmiany, mniej gotówki, bo kupuje drożej).
- Pierwsza próba (składniki ★★★ = 145% ceny ★★) dała premium o 30–60% mniej gotówki, więc złagodzone do 132%.
- Agresywny miał 0 gotówki na poziomie łatwym już przed zmianą (3 z 3 ziaren, stan wyjściowy). Po zmianie w średnim ziarnie 7 jest bliski bankructwa (5 642), ale nie bankrutuje poza łatwym. Bot kupuje ★★★ i rzuca się na marketing, więc najmocniej odczuwa droższe jakości.

## 5. Dla ucznia (do instrukcji)

Każda gwiazdka to decyzja, a nie "im więcej, tym lepiej". Poziom ★ jest tani i wystarczy na start, ale dania wychodzą słabsze, a serwis kosztuje więcej co tydzień. Poziom ★★ zwraca dopłatę po kilku tygodniach, więc to rozsądny środek. Poziom ★★★ kosztuje ponad dwa razy więcej niż ★★ i zwraca się dopiero po kilkunastu tygodniach, czyli opłaca się przy dużym ruchu albo wyższych cenach dań. Zanim kupisz ★★★, policz, czy lokal ma tylu gości i czy starczy Ci gotówki na te kilkanaście tygodni.

## 6. Wątpliwości do autora

1. **Kasa fiskalna, Lada, Tablica menu**: silnik nie daje ich jakości żadnego efektu na sprzedaż. Zostało tylko zadowolenie kasjera (+0,02 za gwiazdkę). ★★★ kasy nie zwróci się więc prawie nigdy (komfort zespołu). Żeby to był prawdziwy dylemat, trzeba efektu w silniku, np. tempo obsługi kasy zależne od gwiazdek. To zmiana kodu, więc jej nie robiłem.
2. **Firmy szkoleniowe**: ocena `zadowoleni_klienci` nie ma efektu mechanicznego, więc rozsądny gracz zawsze bierze najtańszą (HACCP w Pięć Minut). Dylemat będzie prawdziwy dopiero, gdy ocena firmy da np. większy procent oczekujących.
3. **Szafa i zamrażarka**: gwiazdki to tylko pojemność. Poziom ★★★ opłaca się tylko przy stałym nadmiarze towaru, więc dla botów jest to czysty koszt (premium je kupuje).
4. **Lodówka ★★★** zwraca się w ok. 18 tygodni, czyli na górnej granicy zakresu. Napój ma małą marżę, więc pełne 2,2× kłóci się z zakresem 10–14 tygodni. Trzeba albo to zaakceptować, albo obniżyć do ok. 3 000.
5. **Agresywny bot** jest bliski bankructwa na poziomie łatwym już przed zmianą. To problem balansu botów, nie katalogów (boty zostawiłem bez zmian).
6. Zwrot dopłaty liczyłem z założonej marży na sztukę (sekcja 2), a nie z pomiaru: silnik nie wypisuje marży na jeden rożen. Przy lokalu z mniejszym ruchem zwroty ★★★ wydłużą się proporcjonalnie.
7. Liczby w zestawach lokali nie mają cen, ale lokale z zestawem ★★★ stają się de facto droższe w wyposażeniu (środki trwałe z `sprzet.yaml`). Test amortyzacji to uwzględnia, nic nie pękło.
