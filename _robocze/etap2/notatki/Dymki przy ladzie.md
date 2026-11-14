# Dymki przy ladzie

Fragment do notatki (nowa notatka funkcji, w `notatki/Funkcje/` jeszcze nie ma), stan na 14.11, gałąź `wnetrza-dane`.

- **Stan:** dane i silnik na gałęzi `wnetrza-dane`; zatwierdzone 8 zaczepek WOS i 4 cytaty sprawdzone w Wolnych Lekturach (14.11). Rysowanie dymków w panelu: osobne zadanie
- **Gdzie w grze:** wnętrze kebaba (widok od drzwi, przy ladzie)

## Dla ucznia (do instrukcji)
Przy ladzie staje co rundę kilku gości i mówią to, co policzyła gra: czy cena jest wysoka, czy smak średni, czy kolejka za długa.
Czasem ktoś plotkuje o parku albo o konkurencji, a czasem zadaje pytanie z WOS-u i od razu dostaje krótką odpowiedź.
Raz na jakiś czas ktoś składa propozycję (catering, kapela, skarga sąsiadki). Przed wyborem widzisz przy każdej odpowiedzi
wskazówkę, w którą stronę pójdą skutki, ale bez liczb i bez szansy powodzenia. Konkretny wynik poznasz po rundzie.
Dymków nie da się wyłączyć u siebie, bo to źródło wiedzy o grze. Wyłączyć rodzaj może tylko mistrz gry.

## Zasada działania
- Dane: `dane/wnetrza/dymki.yaml` (dymki, propozycje), `bywalcy.yaml`, `silnik.yaml`. Silnik: `silnik/wnetrza/`.
- Co rundę losuje się 3–6 dymków (ziarno gry, runda i firma, więc wynik się powtarza). Wskaźniki (cena względem strefy, ocena,
  kolejka, nastrój zespołu) liczy silnik z ostatniej rundy. Bywalec nie mówi częściej niż co 2 rundy.
- Plotka o parku wchodzi w tej samej rundzie, w której zdarzenie pojawia się na mapie (pierwszy dymek rundy). Plotka o wydarzeniu z kalendarza
  jest zapowiedzią na następną rundę („za tydzień”).
- Propozycja: każda odpowiedź ma `wskazowka` (pole w yaml, schemat pilnuje, żeby nie było w niej cyfr ani „%”).
- Gracz nie ma własnego filtra. Mistrz gry włącza i wyłącza rodzaje (cena i smak, plotki, propozycje, WOS).

## Czego uczy (do planu zajęć)
- pojęcia z WOS i przedsiębiorczości: obowiązek wydania paragonu, informacja o alergenach, cena brutto, reklamacja (14 dni),
  praca nieletnich w wakacje, monitoring w pracy, płatność bezgotówkowa, sprzedaż „na zeszyt” (kredyt kupiecki)
- pytanie do omówienia na lekcji: czym różni się opinia klienta o cenie od opinii o smaku i co z każdą z nich zrobić?
- krótkie zadanie dla drużyn: wybierzcie jedną zaczepkę WOS i sprawdźcie w ISAP, czy odpowiedź pod dymkiem jest prawdziwa.
  Podajcie numer przepisu.

## Do promocji
„Klienci przy ladzie gadają jak prawdziwi: o cenie, o kolejce i o paragonie. Czasem cytują Fredrę.”

## Nawiązanie literackie
Zaczepki i dymki mówią bywalcy z lektur: pani Dulska (Zapolska, „Moralność pani Dulskiej”), Zagłoba (Sienkiewicz, „Ogniem i mieczem”),
Papkin (Fredro, „Zemsta”), Rzecki („Lalka”), Józio (Gombrowicz), doktor Judym (Żeromski). Cztery cytaty sprawdzone dosłownie
w Wolnych Lekturach 14.11 (pole `cytat_zrodlo` w danych).
