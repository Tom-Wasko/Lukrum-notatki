# Wygląd LUKRUM (etap 1½)

To plan wyglądu, który wychodzi z rozmów i podglądów. Jest podstawą dla mapy (`[mapa]`) i wnętrz (`[mechaniki]`).
Podglądy (pliki HTML) są w `../_robocze/wyglad/` u autora. Jeśli chcesz je zobaczyć, poproś o link.

## Ustalone (13.11.2026)

| Sprawa | Decyzja |
|---|---|
| Charakter | **Ilustrowana plansza + czytelność nowoczesnej apki + nutka PRL.** Mapa wygląda jak plansza gry (papier, rysowane budynki), a karty, liczby i przyciski są czyste jak w apce. **Zmiana po podglądach 2 (13.11): sporo PRL-u.** Próbujemy całego interfejsu w stylu PRL (karty, przyciski, paski, typografia), a mapa zostaje mniej więcej planszówkowa. Czytelność apki dalej obowiązuje: liczby i przyciski mają być wyraźne |
| Mapa | **Płaska, z budynkami-ikonami** w miejscach stref. Widok z góry: dzielnice, Bystrzyca, zieleń, główne ulice |
| Kliknięcie budynku | **Wejście do środka**: przybliżenie do budynku, potem wnętrze, potem „Wróć na mapę” |
| Tryby | **Jasny i ciemny robimy równolegle** dla każdego ekranu |
| Wnętrza | We wszystkich budynkach: kebab, bank, hurtownia, biuro J.K.Ś., urzędy… |
| Gracz we wnętrzu kebaba | **Właściciel z boku**: patrzy, jak pracownicy obsługują klientów, słucha ich i decyduje. Nie stoi za ladą |
| Klienci | **Kilku stałych bywalców** z imionami i historiami. Wracają, pamiętają ceny, niosą nawiązania literackie. Obok nich anonimowi goście |
| Bywalcy a lektury | **Wprost, z imionami** (np. pan Ignacy Rzecki z „Lalki” mówi cytatem i pamięta dawne ceny). Postacie z lektur szkolnych są w domenie publicznej |
| Co mówią klienci | Cztery rodzaje dymków: **opinie o cenie i smaku**, **plotki z miasta** (zapowiedzi zdarzeń), **propozycje i kłopoty** (z wyborem odpowiedzi), **zaczepki WOS** (paragon, prawa konsumenta, podatki). **Każdy rodzaj da się włączać i wyłączać**: mistrz gry w ustawieniach (np. pod lekcję), a gracz u siebie |
| Wnętrza bez klientów | **Zależnie od budynku**: bank i urzędy mają okienko z urzędnikiem (gracz jest klientem, postać mówi w dymku i daje karty z opcjami), a hurtownia i podobne mają przekrój z klikalnymi miejscami (regały, wózek). Wszędzie są **lekkie animacje** (wejście postaci, para z kuchni, zegar, migające neony), wyłączane przy `prefers-reduced-motion` |
| Rozwój wnętrza | **Widać kupione rzeczy**: nowy rożen, krzesła, neon nad wejściem. Brud, kolejka i tłok też są widoczne. Wnętrze pokazuje stan firmy |
| Pracownicy we wnętrzu | **Widoczni jako postacie** na swoich miejscach (lada, kuchnia). **Nastrój i zmęczenie widać na twarzy.** Kliknięcie otwiera kartę pracownika (umowa, grafik, szkolenia) |
| Wujek | **Zdjęcie na ścianie** przy dawnym barze (kliknięcie pokazuje jego listy) i **wizyty osobiście** przy ladzie w ważnych momentach („Za moich czasów…”) |
| Dźwięk | **Lekkie dźwięki, domyślnie włączone** (dzwonek nad drzwiami, skwierczenie, gwar, stempel w urzędzie). Łatwy przycisk wyciszenia. Mistrz gry może wyciszyć dźwięk całej klasie |
| Pora dnia | **Zgodna z prawdziwą godziną**: za oknem rano jasno, wieczorem ciemno, w porze obiadowej więcej ludzi. Niezależna od trybu jasny/ciemny |
| Inspiracja | Gry z obsługą klientów przy ladzie (np. „Good Pizza, Great Pizza”). **Bierzemy tylko pomysł:** klient przy ladzie mówi w dymku. Postacie, grafika i nazwy są nasze i lubelskie |

## Ustalone po podglądach 2 (13.11)
- **Rola wnętrza kebaba: A + C.** Lada z gośćmi to podstawa: bywalcy i goście komentują w dymkach, a decyzje są
  przypięte do przedmiotów (menu → ceny, kuchnia → jakość, zaplecze → ludzie, biurko → finanse). Klient
  z propozycją (C) pojawia się od czasu do czasu jako dodatek.
- **Losowe zdarzenia zostają w parkach** (potwierdzone 13.11). Zdarzenia z `dane/zdarzenia/parki.yaml` zostają
  i **pokazuje je mapa w parkach** (Ogród Saski, Park Ludowy…). Przy ladzie są tylko plotki o nich i od czasu do czasu
  klient z propozycją. **Dopisujemy zdarzenia z lektur** (np. „bal” jak u Dulskiej, kulig, pojedynek na słowa).
- **Wejście do środka bez animacji:** klikasz i jesteś w środku. Długie przejście znudziłoby się w późniejszych
  rundach. Wyjście tak samo szybkie („Wróć na mapę”).

## Dymki i bywalcy (decyzje 13.11 wieczorem)
- **Ton bywalców:** po swojemu i z humorem (jak w pierwszej wersji `dymki.yaml`) **oraz** z prawdziwymi cytatami z lektur
  w domenie publicznej. Gombrowicz (Józio) bez cytatów, tylko aluzje.
- **Zaczepki WOS:** Claude sprawdza każdy przepis w źródłach (ISAP, gov.pl), poprawia tekst i dopisuje źródło. Autor
  zatwierdza (`sprawdzone: true`). Silnik pokazuje tylko zatwierdzone.
- **Klient z propozycją:** 2–3 odpowiedzi z **prawdziwym skutkiem** w liczbach (jednorazowy przychód, koszt, opinia,
  ryzyko kontroli, nowy kandydat). Najwyżej jedna propozycja na kilka rund.

## Decyzje po podglądzie 3 (14.11)
- Paleta: **Bar mleczny i Pewex**, gracz wybiera jedną z nich (każda w wersji jasnej i ciemnej).
- Fonty: zostają chude litery (Oswald + PT Sans), a w niektórych miejscach grube (szyld, nagłówki). Grubego fontu nie wybrano: w podglądzie 4 będą do porównania Alfa Slab One i Rubik Mono One.
- W lokalu wyróżnione są miejsca, które da się kliknąć.
- Pasek z lewej pokazuje same ikony i rozwija się do pełnych nazw.
- Jest kilka wnętrz kebabów: różne typy lokali oraz stany „działka w budowie”, „niewyposażony” i „wyposażony”.
- Dymki ludzi pokazują się dopiero po najechaniu na postać.
- Nowa funkcja **dekorowanie lokalu**:
  - Każdy styl trafia do innych grup klientów. Gdy pasuje do klientów strefy, daje mały plus do opinii i popytu (uczy segmentacji).
  - Elementy: ściany i podłoga, szyld i neon, dodatki (Lublin, postacie), meble i oświetlenie.
  - **Nie podpisujemy, z jakiej lektury są postacie i inne odniesienia.**
  - Dekor kupuje się w **sklepie meblowym** na mapie (wejście do sklepu, jak w inne budynki).
  - Dekor kupuje się raz i zostaje, nie starzeje się.
- Następny krok: podgląd 4 (grafiki może zrobić Fable) i notatka `Funkcje/Dekorowanie lokalu.md`.

## Do ustalenia później
- Paleta kolorów (jasna i ciemna) i kroje pisma.
- Ikony (styl kreski).
- Pasek skrótów i układ na telefonie (wspólnie z `[mapa]`).
