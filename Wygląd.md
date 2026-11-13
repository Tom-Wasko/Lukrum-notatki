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
- **Losowe zdarzenia zostają w parkach** (autor: „random eventy zostaw w parkach”). Moje odczytanie: zdarzenia
  miejskie pojawiają się na mapie w parkach (Ogród Saski, Park Ludowy…), a nie przy ladzie. *Do potwierdzenia.*
- **Wejście do środka bez animacji:** klikasz i jesteś w środku. Długie przejście znudziłoby się w późniejszych
  rundach. Wyjście tak samo szybkie („Wróć na mapę”).

## Do ustalenia później
- Paleta kolorów (jasna i ciemna) i kroje pisma.
- Ikony (styl kreski).
- Pasek skrótów i układ na telefonie (wspólnie z `[mapa]`).
