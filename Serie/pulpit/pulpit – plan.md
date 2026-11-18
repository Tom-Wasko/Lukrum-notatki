# Seria pulpit – plan (18.11.2026)

Decyzje szefa: [[Decyzje]], sekcja „Pulpit – nawigacja i układ ekranu”. Szkic: `archiwum/szkice-szefa/pulpit-nawigacja-18.11.jpg`.

## Krok 1: powłoka pulpitu (agent Sonnet, gałąź `pulpit-powloka` z `main`)
- Mapa na cały ekran jako ekran domyślny; stary nagłówek, menu zakładek i stopka znikają z widoku (stary układ dostępny
  tymczasowo przez `?uklad=stary`, do usunięcia po akceptacji szefa).
- Lewy górny róg: ⚙ (ustawienia: istniejący wybór motywu/palety z `motyw.js`) nad wąskim pionowym paskiem z napisem
  LUKRUM pionowo (szyld PRL) i ikonami: „Wyślij decyzje” (istniejąca akcja, z potwierdzeniem), konto, „Jak grać”, koszyk
  (zakupy: istniejący ekran zamówień, jeśli jest; jeśli nie ma – ikona wyszarzona z podpowiedzią). Pod paskiem „Tydzień N” (tylko informacja).
- Dół ekranu: portfel (plik banknotów rysowany SVG, wystaje z krawędzi). Najechanie/fokus pokazuje gotówkę i debet, klik
  otwiera okno finansów (istniejąca zakładka finansów w oknie).
- Prawa krawędź: zeszyt wystający z brzegu z następnym krokiem z listy wujka. Najechanie/fokus wysuwa listę zadań,
  klik otwiera pełny widok (na razie istniejąca lista wujka w oknie; strony, animacja i tutorial to seria `zeszyt`).
- Wnętrza (wejście w budynek) zostają bez zmian poza tym, że pasek i portfel pozostają widoczne.
- Wymagania: 3 palety × jasny/ciemny, kolory tylko przez zmienne, stan nie samym kolorem, obsługa klawiatury i
  fokusu, `prefers-reduced-motion`, tylko komputer. Testy: istniejące zielone + nowe (zakładki i okna, `testy/aplikacja`).
- Dowód: pełny pytest, ruff, `node --check`, 2 zrzuty (mapa w palecie „bar” jasnej i „wysoka” ciemnej).

## Kolejne kroki (po akceptacji kroku 1)
2. `zeszyt` (strony, animacja przewracania, samouczek, odhaczanie w grze, treść z `archiwum/fable-17.11/fable-zeszyt/`)
3. `budynki` i `wnetrza` według makiet Fable (`archiwum/fable-17.11/fable-wnetrza/makiety/`)
4. lista wujka przesuwa i przybliża mapę do budynku
