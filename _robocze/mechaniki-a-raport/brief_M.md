# Agent M – nowe mechaniki, tor A, z pomiarami botów (pracuje w tle)

Najpierw przeczytaj `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\BRIEF_AGENTA.md` oraz rozdział 11 w
`C:\Users\PC\Pulpit\Levas\lukrum\PLAN_PRZEBUDOWY.md` (decyzje autora, tor A). Listę podobieństw do Revasa z numerami pozycji
masz w `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\etap1\podobienstwa.md`.

## Miejsce pracy
- Kod: worktree `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\mechaniki-a` (gałąź `mechaniki-a`, katalog `gra/`).
  Python: `C:\Users\PC\Pulpit\Levas\lukrum\lukrum_gra\gra\.venv\Scripts\python.exe` (uruchamiaj z `mechaniki-a/gra`).
- Raporty i pomiary: `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\mechaniki-a-raport\`.
- Commituj na gałęzi `mechaniki-a` po każdej skończonej części (autor commitów to Tom-Wasko, który jest już w konfiguracji;
  **bez** linii Co-Authored-By, Claude-Session ani „Generated with”). Nie pushuj i nie scalaj z main.
- Równolegle koordynator robi mapę (etap 2) w `panel_gracza/` i `dane/mapa/`. Tych plików dotykaj tylko tyle, ile trzeba,
  żeby gra działała z nowymi danymi (obecny panel to rusztowanie do wymiany, więc liczy się poprawność, nie wygląd).
  Zmiany w silniku, danych (`dane/*.yaml` poza `mapa/`), `balans/` i testach są Twoje.

## Cel
Zastąpić mechaniki i liczby podobne do Revasa własnymi, zgodnie z decyzjami autora. Każda zmiana zachowuje grywalność,
a dobór stałych potwierdzają pomiary botów. Liczby mogą być arbitralne, ale muszą dawać sensowny balans.

## Części (w tej kolejności, każda = commit + wpis w raporcie)
1. **Wynik 0–1000 pkt** (zastępuje iloczyn 5 wskaźników i stałe regresji 0,9464 / 0,8486 / 0,5353 itd., pozycje 1.8, 1.9).
   Pięć działów: finanse, goście, zespół, rozwój, bezpieczeństwo finansowe, każdy 0–200 pkt według **jawnych progów**
   (tabela w danych, tak żeby panel mógł ją pokazać uczniowi). Dział może przekroczyć 200 przy wyjątkowej grze, więc
   wynik może być > 1000. Wskaźniki zadowolenia klientów i pracowników na razie licz prostymi, własnymi wzorami punktowymi
   (w torze B zastąpią je gwiazdki i nastrój zespołu), bez starych stałych. Ranking = suma punktów z tygodni, ostatnie
   tygodnie ważą więcej (wagi w danych). Tydzień 1 to „Wielkie otwarcie” z bonusem za przygotowanie (lokal, menu, ekipa).
2. **Pieniądze:** kapitał 50 000 zł; debet włączany ręcznie decyzją (limit, opłata za każdy tydzień na minusie + odsetki)
   zamiast automatycznego kredytu odnawialnego (1.13); bez debetu brak gotówki kończy się jak dziś u Harpagona/inwestora.
   **Banki ze specjalizacjami** według tabeli w rozdz. 11 planu (nazwy z lektur, bez przedrostka „Bank”, liczby dowolne,
   każdy bank opłacalny dla innej strategii). Banki to fikcyjne instytucje z katalogu, a prawdziwe banki na mapie zostają.
   Sprawdź, gdzie w danych są zmyślone banki (Bank Pod Bramą itd. z etapu 1), i podmień je.
3. **Biura rachunkowe:** pakiety S/M/L z limitem dokumentów i dopłatą za każdy dokument ponad limit (1.15). Biura według
   tabeli w planie: J.K.Ś., Józef K., Scrooge, Asteroida 328 (cechy w tabeli). Ceny orientacyjnie z rynku Lublina 2026
   (szybki research w sieci, źródło wpisz w `zrodlo`).
4. **Kadry według Kodeksu pracy** (2.8): pensje z ofert pracy w gastronomii w Lublinie 2026 (research + GUS), okres
   wypowiedzenia zależny od stażu (art. 36 KP, przelicz na tygodnie gry) zamiast odprawy w % pensji, wybór umowy o pracę
   albo zlecenia (inne składki ZUS, zlecenie bez urlopu i wypowiedzenia). Nowe koszty rekrutacji. Pakiety stanowisk (2.7)
   zamień na własny cennik.
5. **Pomyłki w szczycie** zamiast reklamacji (1.14): prawdopodobieństwo rośnie z obciążeniem kuchni, zmęczeniem
   (nadgodziny) i brakiem szkoleń, kosztuje ponowne danie i obniża wskaźnik gości. Stary mnożnik 0,15 znika.
6. **Katalogi** (2.3–2.6, 2.10): nowe zestawy dla kebaba (np. ogródek, ładowarki, BLIK, kiosk do zamówień, muzyka, toaleta
   dla gości, dostawa przez aplikację) zamiast tabel z Revasa, z cenami z researchu i własnym wpływem na wskaźniki.
   Szkolenia: inne firmy, liczby i ceny. Media w katalogu: „Gazeta Pana Cogito”, „Radio Tichy” i inne własne nazwy.
7. **Stara reklama** (1.11): usuń tradycyjną ln(1+k·emisje) i internetową z wagą konkurencji, zostaje model z mapą
   „agencja × kanał”. Usuń martwe dane i testy.
8. **Pula godzin zostaje** (1.7), ale komentarz i `zrodlo` mają ją uzasadniać własnymi słowami (mały kebab, jeden grill).

Popytu (1.10), gwiazdek, nastroju, wydarzeń i fabuły **nie ruszaj**, to tor B.

## Pomiary
- Narzędzia: `python -X utf8 -m balans.symuluj <rundy> <poziom> <ziarno>` i reszta `balans/` (przeczytaj nagłówki).
  Przed zmianami zrób pomiar bazowy (kilka ziaren, 12 rund, poziomy łatwy/średni/trudny) i zapisz go w raporcie.
- Po każdej części: te same pomiary. Kryteria: strategia zrównoważona najlepsza albo bliska najlepszej; agresywna wyraźnie
  słabsza; bankructwa rzadkie poza agresywną; rozrzut wyników sensowny (wynik w pkt: dobra gra ok. 1000, słaba ok. 400–600).
- Gdy wybór stałych jest niejasny, zmierz 2–3 warianty i opisz je w raporcie z zaleceniem. Autor wybiera.
- Gdy boty nie umieją nowej decyzji (debet, umowa, pakiet biura), naucz je w `silnik/boty.py` (proste reguły).

## Testy i dane zamrożone
Testy mechanik korzystają z `testy/dane_zamrozone/`. Po świadomej zmianie liczb przegeneruj kopię według zasad w
`AGENTS.md` (sekcja o danych zamrożonych) i popraw testy pod nowe zasady. W trakcie uruchamiaj testy dotkniętych plików,
pełny pytest raz na koniec części. Ruff i `python -X utf8 -m silnik.dane sprawdz` muszą przechodzić.

## Raport
`_robocze/mechaniki-a-raport/raport.md`: dla każdej części co zmieniłeś, tabela pomiarów przed i po, warianty i zalecenie,
otwarte pytania do autora. Na koniec 5–10 linijek streszczenia. Gdy utkniesz na decyzji, która należy do autora, opisz ją
w raporcie i idź dalej z najrozsądniejszym wariantem.
