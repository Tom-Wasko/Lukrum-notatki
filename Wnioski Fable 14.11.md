# Wnioski Fable (14.11.2026)

Trzy raporty agenta Fable. Poniżej tylko streszczenie. Pełne raporty leżą poza repo, w `lukrum/_robocze/`:
- `przeglad-a-fable.md` – przegląd PR #2;
- `pozew-revas-fable.md` – symulowany pozew;
- `swot-fable.md` – SWOT.

Decyzje są w [[Do decyzji]].

## 1. Przegląd PR #2 (tor A, `mechaniki-a`)
Werdykt: **nie scalać przed poprawkami**. Testy przechodzą (598), ale liczby psują grę:
- **Pomyłki w szczycie:** waga 10 w `klienci.yaml` pochodzi z czasów reklamacji (ok. 0,3%). Przy obecnych 10–19% pomyłek dobra firma traci ok. 1,5★.
- **Debet liczy się w trakcie tygodnia.** Firma ma 16,7 tys. zł gotówki, a i tak płaci za debet. Bez zgody banku dostaje alarm przy dodatnim saldzie.
- **Debet bez zgody jest tańszy niż za zgodą** (ok. 7 zł wobec 47–97 zł tygodniowo) i nie ma limitu.
- **Firma bezczynna dostaje 353 pkt** (bot agresywny 381).
- **Prawo:**
  - okres próbny 3 miesiące = 2 tygodnie wypowiedzenia (art. 34 KP);
  - debet 16–20% przekracza odsetki maksymalne (ok. 15%).
- **Stare opisy:** `INSTRUKCJA.md` (40 000 zł, kredyt odnawialny), pole `reklamacje` w JS.
- **Scrooge** nie wygrywa zawsze tylko dzięki ukrytej dopłacie. Przy święcie w ostatniej rundzie przeniesione dokumenty przepadają za darmo.
- **Bot agresywny na łatwym poziomie** to sens gry, nie błąd.

Decyzje autora 14.11:
- debet liczony na koniec tygodnia; bez zgody zawsze drożej; stopy do limitu odsetek maksymalnych;
- pomyłki 2–5%, lżejsza kara niż za kolejkę;
- firma bezczynna 0–100 pkt.

Poprawki zaczęte i wstrzymane do końca pracy Fable.

## 2. Symulowany pozew REVAS
**Mocne zarzuty:**
1. **Katalogi z liczbami jak w REVAS.**
   - w `main`: banki, biura, media, pakiety stanowisk, kandydaci;
   - w PR #2: 9 udogodnień, 6 pozycji wyposażenia, oceny firm szkoleniowych.
2. **Pochodzenie materiałów** w `_archiwum/revas_26`: do rozmowy z prawnikiem, razem z regulaminem platformy.
3. **Stałe modelu wspólne z REVAS** (popyt, reklama, karta wyników): w `main` 45, w PR #2 22, część martwa. Opisy źródeł bez nazwy gry wyglądają jak zacieranie śladów.
4. **Harmonogram odblokowań zakładek** w tej samej kolejności. Nazwy „Karta wyników”, „Lista błędów”, „Wyślij decyzje”.

**Słabe zarzuty:** kod (0 wspólnych linii), teksty (jedno zdanie), znak REVAS, regulamin konkursu.

**Logotypy prawdziwych firm:** decyzja autora 14.11 – **zostają** (IKEA, Pewex itd.).

**Ryzyka w planie:**
- postacie z lektur autorów wciąż chronionych (Gombrowicz, Lem, Herbertowie) bez podpisu źródła;
- bywalcy podobni do aktorów z ekranizacji;
- cel „zero śladów w historii gita”, który w sporze działa przeciw nam. Lepiej dokumentować balansowanie od zera.

Raport kończy się listą kontrolną na następny przegląd gotowego LUKRUM.

## 3. SWOT całego projektu
- **Mocne:** szybki silnik (gra botów 3 s); narzędzia lekcyjne już są: zestaw „Krótka lekcja”, zegar rundy, refleksje, eksport CSV.
- **Słabe:**
  - nikt poza autorem nie grał, balans jest tylko z botów;
  - czeka ponad 40 decyzji autora;
  - dokumenty przeczą sobie w sprawie logotypów: plan, [[WSPOLPRACA]] i [[LUKRUM]] mówią „bez logo”, a decyzja z 14.11 mówi, że zostają.
- **Szanse:** konkurs „Zwolnieni z Teorii” nagradza przeprowadzone zajęcia (termin 31.03.2027, niepotwierdzony); podstawa programowa biznesu i zarządzania.
- **Zagrożenia:**
  - PR #2 blokuje wnętrza, mapę i zdarzenia;
  - mapa jest na ścieżce krytycznej, a gałęzi kolegi nie ma w repo; pytania z 13.11 są bez odpowiedzi; prototyp ma termin 16.11;
  - kasyno jest domyślnie włączone i ukryte przed nauczycielem, co może zamknąć drogę przez kuratorium.
- **Brakuje w planie:**
  - lekcji 45 minut ze zmierzonym czasem rundy;
  - przewodnika nauczyciela;
  - zasad oceniania;
  - tabeli „mechanika a podstawa programowa”;
  - serwera (dziś laptop i tunel);
  - RODO uczniów;
  - dostępności.
- **Propozycja Fable:** przełącznik „ikony ogólne” na pokaz dla urzędów.

**Kroki przed pierwszą lekcją (wg Fable):**
1. Zgłoszenie do konkursu z datą lekcji.
2. Jedna sesja decyzji autora.
3. Scalenie poprawionego PR #2.
4. Z kolegą: najmniejszy prototyp mapy.
5. Spisanie „wersji na pierwszą lekcję”.
6. Gra próbna z 4–6 osobami ze stoperem. Wymaga zgody autora na pokazanie panelu w zamkniętym gronie.
7. Nowy wygląd tylko dla ekranów podstawowych.
8. Pakiet nauczyciela z testem przed i po.

## 4. W toku
Podgląd 4 z nową oprawą i grafikami SVG (Fable): `_robocze/wyglad/podglad4.html`, `_robocze/wyglad/grafiki/`.
