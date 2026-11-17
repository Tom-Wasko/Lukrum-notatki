# Wygląd LUKRUM

Obowiązujący wygląd gry. Podstawa dla mapy (`[mapa]`) i wnętrz (`[mechaniki]`). Jak powstawał (podglądy 1–4):
[[Historia]]. Sprawy otwarte: [[Do decyzji]], §6. Co z tego już działa i co jeszcze nie: [[Postęp]].

## Charakter
- **Ilustrowana plansza + czytelność nowoczesnej apki + sporo PRL-u.** Mapa wygląda jak plansza gry (papier, żetony,
  tabliczki). Karty, przyciski, paski i typografia są w stylu PRL, ale liczby i przyciski mają być wyraźne jak w apce.
- **Jasny i ciemny tryb zawsze razem**, dla każdego ekranu.
- Inspiracja to tylko pomysł „gość przy ladzie mówi w dymku”. Postacie, grafika i nazwy są nasze i lubelskie.

## Palety i kroje
| Sprawa | Ustalenie |
|---|---|
| Palety | **Bar mleczny** (domyślna), **Pewex**, **wysoka widoczność**; każda jasna i ciemna. Gracz wybiera w menu ⚙ |
| Wysoka widoczność | kontrast tekstu co najmniej 7:1, litery o 25% większe, grube ramki i fokus, krój Atkinson Hyperlegible, bez tekstur. Zob. [[Wysoka widoczność]] |
| Nie tylko kolor | we wszystkich paletach: zysk ▲, strata ▼, uwaga !, wzory w wykresach (`dostepnosc.css`) |
| Kroje | Oswald + PT Sans, gruby krój **Alfa Slab One** (szyld, nagłówki, ceny). Fonty w repozytorium (OFL), bez Google Fonts |
| Zmienne | jeden plik `static/motywy/zmienne.css`; atrybuty `data-paleta` (`bar`, `pewex`, `wysoka`) i `data-tryb` (`jasny`, `ciemny`). Kolory tylko przez zmienne (lista niżej) |
| Ruch | lekkie animacje (wejście postaci, para z kuchni, zegar, neony), wyłączane przy `prefers-reduced-motion` |

## Zmienne wyglądu
Ustawiane w `static/motywy/zmienne.css`; atrybuty na `<html>`: `data-paleta` = `bar` (domyślna) | `pewex` | `wysoka`
i `data-tryb` = `jasny` | `ciemny`, ustawiane przez `lukrum.wyglad.ustaw({paleta, tryb})` (umowa z mapą:
[[WSPOLPRACA]], „Umowy na granicy”). Zmienne: `--papier`, `--tusz`, `--akcent`, `--akcent-2`, `--ramka`, `--zysk`,
`--strata`, `--uwaga`, `--font-tekst`, `--font-szyld`, `--font-gruby`, `--skala-tekstu`, `--ramka-grubosc`, `--ognisko`,
`--tekstura` oraz `--g-*` dla grafik. Stan nigdy samym kolorem (▲ ▼ !, wzory). `data-motyw` zostaje dla starego wyboru
układu panelu, nie używać go w mapie.

## Mapa i pulpit
- Mapa płaska, widok z góry: dzielnice, Bystrzyca, zieleń, główne ulice, budynki jako żetony. Spis i zasady: [[Mapa]].
- Pulpit (mapa na cały ekran, ikony w rogach, portfel, lista wujka i zeszyt wujka) i układ wnętrz: obowiązująca
  decyzja jest w [[Decyzje]], „Pulpit i wnętrza”; stan prac w [[Postęp]].
- Kliknięcie budynku: **od razu jesteś w środku**, bez długiego przejścia. Wyjście tak samo szybkie („Wróć na mapę”).
- Mapa ma swój pasek skrótów (robi `[mapa]`), wnętrza swój (`[mechaniki]`). Pasek wnętrz pokazuje same ikony
  i rozwija się do pełnych nazw.

## Wnętrza
| Sprawa | Ustalenie |
|---|---|
| Gdzie | we wszystkich budynkach: kebab, bank, hurtownia, biura, urzędy, sklep meblowy |
| Rola wnętrza kebaba | lada z gośćmi to podstawa. Decyzje są przypięte do przedmiotów: menu → ceny, kuchnia → jakość, zaplecze → ludzie, biurko → finanse. Klient z propozycją pojawia się od czasu do czasu |
| Gracz | **właściciel z boku**: patrzy, słucha i decyduje. Nie stoi za ladą |
| Klikalne miejsca | wyróżnione w scenie |
| Goście | kilku stałych bywalców z imionami i historiami, obok nich anonimowi goście. Dymek pokazuje się po najechaniu na postać |
| Bywalcy a lektury | postacie z lektur z imionami (np. pan Ignacy Rzecki). **W interfejsie nie podpisujemy, z jakiej lektury jest postać.** Klucz ma tylko mistrz gry, w instrukcji |
| Pracownicy | widoczni na swoich miejscach. **Nastrój i zmęczenie widać na twarzy.** Kliknięcie otwiera kartę pracownika |
| Rozwój | widać kupione rzeczy (rożen, krzesła, neon) oraz brud, kolejkę i tłok. Wnętrze pokazuje stan firmy |
| Typy i stany | kilka wnętrz kebaba: różne typy lokali oraz stany „działka w budowie”, „niewyposażony”, „wyposażony” |
| Wystrój | style trafiają do różnych grup gości. Elementy: ściany i podłoga, szyld i neon, dodatki, meble i oświetlenie. Kupuje się w sklepie meblowym. Zob. [[Sklep meblowy Meblościanka (dekor)]] |
| Wnętrza bez gości | bank i urzędy: okienko z urzędnikiem, który mówi w dymku i daje karty z opcjami. Hurtownia i podobne: przekrój z klikalnymi miejscami (regały, wózek) |
| Wujek | zdjęcie na ścianie (kliknięcie pokazuje jego listy) i wizyty przy ladzie w ważnych momentach |

## Dymki
Cztery rodzaje: opinie o cenie i smaku, plotki z miasta, propozycje i kłopoty, zaczepki WOS. Zasady: [[Decyzje]],
„Goście i dymki”. Opis funkcji: [[Dymki przy ladzie]].

## Jeszcze niewdrożone z ustalonego
Lista (dźwięk, pora dnia we wnętrzach, wizyty wujka, pełne wnętrza poza kebabem) jest w [[Postęp]], etap 3.

## Grafiki
Własne płaskie grafiki SVG bez wpisanych kolorów (zmienne CSS i `currentColor`). Spis i zasady użycia:
`panel_gracza/static/grafiki/README.md`. Generator: `narzedzia/grafiki/`. Żadna grafika nie
odtwarza cudzego logo, a postacie nie wzorują się na ekranizacjach.
