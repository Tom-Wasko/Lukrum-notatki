# Plan na 14.11.2026 (pauza 13.11 wieczorem)

Autor 13.11 wieczorem: „na razie wszystko zaplanuj, a pracę wznowisz jutro”. Ta notatka mówi, gdzie stoimy i co robimy po kolei.

## Na start każdej sesji
1. `git pull` w `lukrum_gra` i w `notatki`. Przeczytaj [[WSPOLPRACA]]: czy `[mapa]` coś dopisał w Dzienniku albo w Pytaniach.
2. Odpowiedz na pytania od `[mapa]`, zanim ruszysz kod na granicy.

## Stan na pauzę
| Co | Gdzie | Stan |
|---|---|---|
| Tor A nowych mechanik | gałąź `mechaniki-a` (worktree `_robocze/mechaniki-a`), raport `_robocze/mechaniki-a-raport/raport.md` | commit WIP cf281e8, bez push. Zrobione części 1–5, 7, 8. **Brak części 6** (katalogi udogodnień, wyposażenia, szkoleń, mediów) i notatek o pomyłkach i katalogach. Pełny pytest: **2 testy czerwone** (`test_zamowienia_ponad_saldo`, `test_zuzycie_zasobow_na_klienta`) |
| Dane wnętrz | gałąź `wnetrza-dane` (commit 03dc12b, wypchnięta), `gra/dane/wnetrza/` | `bywalcy.yaml` (7 postaci) i `dymki.yaml` (42 dymki, 4 rodzaje). Brak silnika |
| Wygląd | [[Wygląd]], podglądy 1 i 2 | decyzje spisane. Paleta, kroje i ikony nieustalone |

## Kolejność pracy
1. **Tor A (mechaniki-a)**
   - naprawić 2 czerwone testy, zrobić część 6 i brakujące notatki funkcji (tym samym agentem);
   - wprowadzić odpowiedzi autora: otwarcie z wagą 1,0; Scrooge w święta zamknięty z dopłatą; urlop 10%; debet bez zmian (zob. [[Do decyzji]]); potem pomiary botów od nowa;
   - pytest + ruff, przegląd zmian;
   - push gałęzi i **PR bez scalania** (scala autor);
   - notatka w `Funkcje/` dla każdej przerobionej funkcji, wpis w Dzienniku [[WSPOLPRACA]], sprawy do [[Do decyzji]].
2. **Wnętrza: silnik dymków (wnetrza-dane)**
   - brief + agent sonnet: `silnik/wnetrza/`, z plikami:
     - `stan.py`: pracownicy z nastrojem i miejscem, kupione wyposażenie, kolejka, ocena;
     - `dymki.py`: wybór dymków z ziarnem rundy, warunki `gdy`, okazje wujka, limity z `zasady`;
     - `schematy.py`;
   - walidacja w `python -m silnik.dane sprawdz`;
   - ustawienie MG: 4 rodzaje dymków (domyślnie wszystkie włączone);
   - endpoint API w nowym pliku (`api/wnetrza.py`);
   - testy w `testy/wnetrza/`;
   - **nie ruszać plików zmienionych na `mechaniki-a`**, bez rysowania frontu;
   - propozycje: 2–3 odpowiedzi z prawdziwym skutkiem (przychód, koszt, opinia, ryzyko kontroli, kandydat), najwyżej jedna na kilka rund;
   - WOS: silnik pokazuje tylko `sprawdzone: true`.
2a. **Teksty dymków (Opus, sam)**
   - sprawdzić każdą zaczepkę WOS w źródłach (ISAP, gov.pl), poprawić, dopisać źródło; lista do zatwierdzenia przez autora;
   - dopisać prawdziwe cytaty z lektur w domenie publicznej (bez Gombrowicza), zostawić humor;
   - rozpisać skutki propozycji (do `zalozenia.yaml` albo `dymki.yaml`, z `zrodlo`).
2b. **Zdarzenia z lektur w parkach**: nowe historie w `dane/zdarzenia/parki.yaml`. Ten plik jest zmieniony na `mechaniki-a`, więc robimy to **po scaleniu toru A** albo na tej gałęzi.
3. **Granica z mapą**
   - uzgodnić w [[WSPOLPRACA]] format listy miejsc i `otworzWnetrze(idMiejsca)`;
   - dopisać, że zdarzenia z parków (`dane/zdarzenia/parki.yaml`) pokazuje mapa w parkach;
   - ustalić wspólny plik zmiennych CSS (PRL-owy interfejs).
4. **Wygląd wnętrza kebaba**: podgląd 3 z PRL-owym interfejsem: lada, bywalcy z `bywalcy.yaml`, prawdziwe dymki z `dymki.yaml`, jasny i ciemny tryb. Przy okazji propozycja palety i krojów do wyboru.
5. Później:
   - wnętrza banku, urzędów i hurtowni;
   - tor B mechanik;
   - przepisanie wszystkich opisów w grze pod nowe mechaniki.

## Do sprawdzenia przez autora (z danych wnętrz)
- Zaczepki WOS w `dymki.yaml` mają `sprawdzone: false`: paragon, alergeny, ceny brutto, reklamacja 14 dni, młodociani, monitoring, płatność kartą, „na zeszyt”. Każdą trzeba sprawdzić ze źródłem przed lekcją.
- Teksty bywalców (Rzecki, Zagłoba, Dulska, Judym, Papkin, Józio, Wujek): czy ton pasuje do klasy.
