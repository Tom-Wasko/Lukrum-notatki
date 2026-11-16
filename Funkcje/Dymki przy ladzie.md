# Dymki przy ladzie


- **Stan:** w grze (PR #5; wnętrze kebaba i przełącznik mistrza gry 16.11.2026); 8 zaczepek WOS zatwierdzonych, 4 cytaty sprawdzone w Wolnych Lekturach (14.11)
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

## Zaczepki WOS i ich podstawa prawna
Zatwierdzone przez szefa, sprawdzone 14.11.2026 (`dane/wnetrza/dymki.yaml`, pole `sprawdzone`). Gra pokazuje tylko zatwierdzone.
1. **Paragon** (Józio): kasa musi wydać paragon bez proszenia; e-paragon za zgodą klienta. Ustawa o VAT, art. 111 ust. 3a pkt 1.
2. **Alergeny** (Zagłoba): 14 alergenów z listy UE także przy jedzeniu bez opakowania. Rozp. (UE) 1169/2011, art. 44 ust. 1 lit. a, zał. II. Forma informacji zależy od przepisów krajowych, więc dymek jej nie narzuca.
3. **Cena z VAT** (Rzecki): cena dla klienta zawsze brutto. Ustawa z 9.05.2014 o informowaniu o cenach, art. 3 ust. 1 pkt 1 (numer punktu do potwierdzenia w ISAP).
4. **Reklamacja** (gość): 14 dni na odpowiedź, milczenie = przyjęcie. Ustawa o prawach konsumenta, art. 7a.
5. **Praca 16-latka** (Józio): tylko lekkie prace, badanie lekarskie, w wakacje 7 h dziennie i 35 h tygodniowo, bez nadgodzin i nocy. KP art. 200¹, 200², 201, 203.
6. **Monitoring** (Judym): informacja 2 tygodnie przed uruchomieniem, cel, oznaczenie terenu. KP art. 22², RODO art. 13.
7. **Płatność kartą** (gość): obowiązek płatności bezgotówkowej od 2022, kasa połączona z terminalem od 2025. Prawo przedsiębiorców, art. 19a (zakres do potwierdzenia).
8. **„Na zeszyt”** (Papkin): odroczona płatność; ryzyko po stronie sprzedawcy, sprzedaż i tak na kasie. KC art. 535, ustawa o VAT art. 111. Najsłabiej udokumentowana; można ją usunąć.

## Do promocji
„Klienci przy ladzie gadają jak prawdziwi: o cenie, o kolejce i o paragonie. Czasem cytują Fredrę.”

## Nawiązanie literackie
Zaczepki i dymki mówią bywalcy z lektur: pani Dulska (Zapolska, „Moralność pani Dulskiej”), Zagłoba (Sienkiewicz, „Ogniem i mieczem”),
Papkin (Fredro, „Zemsta”), Rzecki („Lalka”), Józio (Gombrowicz), doktor Judym (Żeromski). Cztery cytaty sprawdzone dosłownie
w Wolnych Lekturach 14.11 (pole `cytat_zrodlo` w danych).
