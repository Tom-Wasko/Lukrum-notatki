# Historia

Kronika prac. Tu się nie planuje i nie decyduje: obowiązujący stan jest w [[Decyzje]],
[[Wygląd]] i [[Mapa]]. Wpis dopisuje lider przy zamknięciu serii, najnowsze na górze. Szczegóły techniczne serii:
[[Serie]].

## Kronika

### 17.11.2026 – porządki
- Seria `porzadki`: repo gry spłaszczone (kod w korzeniu, bez folderu `gra/` w ścieżkach), `warsztat/` jako osobne repo,
  `archiwum/` poza gitem, notatki odchudzone (jeden właściciel informacji, wycofane pliki w `archiwum/notatki-wycofane/`),
  kody dawnych serii w danych zastąpione realiami, nowy pomiar zwrotu z wystroju (10,9 tygodnia). Szczegóły: [[Serie]].
- Zmiany majstra scalane do `main` od razu; push bez pytania ([[Decyzje]], „Sposób pracy i repozytoria”).
- Noc 16/17.11: agent Fable przygotował projekt wnętrz, treść zeszytu wujka i raport o dziurach w ekonomii; pytania
  czekają w [[Do decyzji]], §8.

### 16.11.2026 – nowy sposób pracy
- Role: autor to **szef**, główna sesja to **lider**, podagenci to **agenci**. Nowy `AGENTS.md`, protokół lidera,
  własne definicje agentów. Powód i źródła: [[Sprawozdanie – zespół agentów]].
- Gałąź `fable` i mapa majstra scalone do `main` gry i wypchnięte (740 testów). Scalone gałęzie zdalne usunięte.
- Decyzje szefa: bez terminu, biura i agencje w osobnych budynkach, pulpit z mapą na cały ekran, pełna przebudowa
  notatek. Zapis: [[Dziennik lidera]]. Dorobione tego dnia: panel pokazuje kontrolę PIP, opłatę za zmianę biura i przejęcie
  debetu; mistrz gry ma przełącznik rodzajów dymków. Po krytyce wnętrz: 5 banków, giełda osobno, Kamienica rachmistrzów,
  Dom reklamy ([[Decyzje]]).

### 15–16.11.2026 – samodzielna praca agenta Fable i mapa majstra
- Agent pracował sam na gałęzi `fable` (15.11 od 16:55 do 17:25, potem 16.11 od 06:49 do 12:47). Zrobił 18 tematów:
  miejsca z wnętrzami, palety w całym panelu, list od wujka, sklep meblowy i wystrój, „Kurier rankingowy”, księgę
  gości, podium, tryb lekcyjny, nową instrukcję, ceny katalogów od zera, projekt scenariuszy lekcji, przegląd prawny.
- Majster oddał mapę Lublina z OpenStreetMap (gałąź `maciex`): żetony, tabliczki, trzy poziomy szczegółów, pora dnia.
  Przy okazji zmienił dwie decyzje z 14.11 (strefa = jedna dzielnica, nowe adresy siedmiu lokali): czekają na akceptację.
- Wniosek z tej nocy: swoboda bez listy plików wyjściowych dała dużo funkcji, ale też plany, dzienniki i zrzuty
  w wielu miejscach. Stąd zasada „tylko pliki z briefu” i porządki z 17.11.

### 14.11.2026 – tor A, wspólne podstawy mapy, podgląd 4
- Niezależny przegląd toru A znalazł 12 usterek, m.in.: pomyłki w szczycie zbijały oceny lokali, debet liczył się
  w środku tygodnia i bez zgody był tańszy niż za zgodą, firma bezczynna dostawała 353 pkt, okres próbny i stopy
  debetu nie zgadzały się z prawem. Autor zdecydował o poprawkach tego samego dnia i weszły one przed scaleniem.
- Scalone PR #2 (tor A), #3 (wspólne z mapą: pola miejsc, zmienne wyglądu, fonty, grafiki), #4 (zespoły budynków),
  #5 (poprawki toru A i silnik dymków).
- Przegląd ryzyka prawnego: liczby katalogów i stałe modelu mają być własne, policzone od zera i udokumentowane.
  Stąd decyzja „ceny pod rozgrywkę” i przeliczenie katalogów 15.11. Decyzja o markach: nazwy i uproszczone znaki zostają.
- Analiza mocnych i słabych stron projektu. Mocne: szybki, powtarzalny silnik; liczby w danych ze źródłem; narzędzia
  dla nauczyciela. Słabe: nikt poza autorem nie grał; balans tylko z botów; ponad 40 otwartych decyzji. Lista braków
  trafiła do [[Plan]], rozdz. 3.
- Wygląd: po podglądzie 3 wybrane palety Bar mleczny i Pewex; po podglądzie 4 krój Alfa Slab One, trzecia paleta
  wysokiej widoczności, grafiki SVG wnętrz.
- Zatwierdzone osiem zaczepek WOS i cztery cytaty z lektur.

### 13.11.2026 – start
- Nazwa LUKRUM, nowe prywatne repozytoria gry i notatek, plan w pięciu etapach.
- Etap 1: gra pod nową nazwą z nową dokumentacją. Stary wygląd z tabelami nie został przeniesiony.
- Majster (kolega autora) dołącza do projektu i bierze mapę. Powstaje tablica [[WSPOLPRACA]].
- Decyzje o nowych mechanikach w dwóch torach: A (niezależny od mapy) i B (po mapie).
- Wygląd po podglądach 1 i 2: plansza + apka + PRL, wnętrza we wszystkich budynkach, bywalcy z lektur.
- Wieczorem pauza z planem na 14.11: dokończyć tor A, napisać silnik dymków, uzgodnić granicę z mapą, zrobić podgląd 3.
