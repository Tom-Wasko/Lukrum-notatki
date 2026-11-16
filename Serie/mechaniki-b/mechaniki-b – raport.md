# Raport: mechaniki-b (Tor A, decyzje autora 14.11)

Kopia robocza `mechaniki-b` (gałąź mechaniki-b). Nic nie commitowane. Pełny pytest: **619 przeszło** (274 s),
`ruff check .` czysto, `silnik.dane sprawdz` w porządku. Test `test_mistrz_gry_nie_widzi_klubu` przeszedł.

## Co zrobione (pliki)

1. **Scrooge 6 zł.** `dane/mapa/biura.yaml` (`doplata: 6.0`, opis i źródło „decyzja autora 14.11.2026”). Dokumenty przeniesione
   po święcie z ostatniej rundy były już rozliczane w `nalicz` (parametr `ostatnia`, wprowadzony po przeglądzie), więc kod
   bez zmian, dodany test z ostatnią rundą.
2. **Asteroida 328 bez limitu.** `dane/mapa/biura.yaml` (`bez_limitu: true`, `doplata: 0.0` w S/M/L), `silnik/schematy.py`
   (pole `BiuroMapy.bez_limitu`), `silnik/ksiegowosc/biuro.py` (`oplata`: `ponad = 0` dla biura bez limitu).
3. **Opłata za zmianę biura.** `biura.yaml` (`zmiana_biura: {tygodni_pakietu: 1, pewnosc: zalozenie, zrodlo}`), `schematy.py`
   (`ZmianaBiura`), `model.py` (`Firma.ostatnie_biuro`), `biuro.py` (`oplata_zmiany`, wywołana w `nalicz`): tydzień pakietu NOWEGO
   biura, osobna pozycja KPiR „Koszt biura rachunkowego: opłata za zmianę biura (…)” (VAT 23%, typ dokumentu jak opłaty biura),
   pole `zmiana_biura` w wyniku biura i w `razem`. Pierwszy wybór bez opłaty; A→B→A płatne.
4. **Józef K.** `biuro.py` (`ustaw_pakiet` przepisana): (a) pierwszy jawny wybór pakietu zapisuje się zawsze, także równy
   domyślnemu; (b) zapowiedź zmiany pakietu trzyma się firmy, nie biura: w biurze bez opóźnienia nowa decyzja zmienia
   tylko pakiet docelowy, termin zostaje, „zostaję przy obecnym” nie anuluje zapowiedzi (anuluje tylko w biurze z opóźnieniem).
5. **Zmiana banku z debetem.** `dane/mapa/banki.yaml` (`przejecie_debetu: {procent: 0.02, ...}`), `schematy.py`
   (`PrzejecieDebetu`), `silnik/pieniadze/banki.py` (`oplata_przejecia_debetu`, `_debet_przy_zmianie`, wywołane w `poczatek_rundy`):
   gotówka ≥ debet: spłata ze starego banku; inaczej nowy bank przejmuje dług za `max(2% kwoty, najmniejsza opłata debetu = 40 zł)`,
   koszt w KPiR (dokument „Wyciąg bankowy”). Komunikat w `info["debet_przy_zmianie"]["komunikat"]`, bezosobowy.
6. **Zlecenie, PIP.** Nowy `silnik/ludzie/kontrola_pip.py`, `silnik/losowosc.py` (cel `pip`), `silnik/model.py`
   (`Pracownik.tygodnie_jak_etat`), `silnik/runda.py` (wywołanie po sanepidzie, `w["pip"]`, kara w `mandaty_rundy`),
   `silnik/wyniki/wnioski.py` (rada „Kontrola PIP”), `dane/zalozenia.yaml` (`pracownicy.kontrola_pip`: 30 h, 4 tygodnie,
   5%, 2000 zł, tekst zdarzenia; `umowa_zlecenie: -0.04`), `biuro.py` (etykieta typu dokumentu kar). Mechanizm taki sam jak
   sanepid (strumień losowy, kara poza KPiR rodzaj „kary”). Godziny to `godziny_pracownika × formy.etat` osoby ze stanowiskiem,
   więc student (24 h) nie podlega. Dane bez sekcji (zamrożone) nie mają kontroli.
7. **Pensja za wypowiedzenie przy wyprowadzce.** `silnik/nieruchomosci/przejecia.py`: pensja w kolumnie `wynagrodzenia`,
   osobna pozycja ZUS pracodawcy przez `fz.stawka_zus(dane, umowa, student)` (ta sama funkcja co lista płac w `runda.py`).
8. **Pomyłka przy pustym magazynie.** `silnik/kuchnia/operacje.py`. Wybrane rozwiązanie: po losowaniu pomyłek liczony jest
   zapas składników ponad potrzeby obsłużonych klientów; pomyłka, której powtórka się mieści, zużywa składniki jak dotąd,
   a pomyłka bez składników na powtórkę **odbiera klienta** (obsłużeni −1, przyczyna „pomyłka bez składników na powtórkę
   dania”), przy czym składniki zepsutej porcji schodzą z magazynu. Częstości pomyłek (5,2%/2,8%) bez zmian, brak nowych liczb.

## Testy
Nowe: `testy/ksiegowosc/test_biuro_14_11.py` (6: Scrooge 6 zł i ostatnia runda, Asteroida, opłata za zmianę, zmiana w grze,
obejścia Józefa K. (a) i (b)), `testy/pieniadze/test_zmiana_banku_z_debetem.py` (3), `testy/ludzie/test_kontrola_pip.py` (4),
`testy/rdzen/test_mechaniki.py::test_pomylka_przy_pustym_magazynie_…` (1). Rozszerzony (bez osłabiania)
`testy/nieruchomosci/test_licytacje.py::test_wypowiedzenie_wyprowadzka_…` o kolumnę wynagrodzeń i ZUS. Nowe pliki testów mają
`pytestmark = dane_gry` (czytają aktualne `dane/`, a nie zamrożoną kopię). `dane_zamrozone` nie ruszane.

## Pomiary (`balans.symuluj 12 latwy,sredni,trudny 7,11,23` i `balans.pomiar_punktow`, przed i po)
Pliki: `etap2/pomiary/przed.txt`, `po.txt`, `przed_punkty.md`, `po_punkty.md`. Średni wynik (pkt, 0–1000) przed → po:

| poziom | zrównoważony | tani | premium | agresywny | naśladowca |
|---|---|---|---|---|---|
| łatwy | 585 → 585 | 461 → 419 | 528 → 529 | 432 → 399 | 543 → 586 |
| średni | 665 → 666 | 599 → 583 | 621 → 624 | 602 → 580 | 673 → 673 |
| trudny | 722 → 720 | 655 → 623 | 620 → 620 | 690 → 680 | 738 → 742 |

Średnia gotówka poziomu (symuluj): łatwy 36 643 → 37 147, średni 69 028 → 67 184, trudny 85 182 → 83 264. Bankructwa bez zmian
(tylko agresywny na łatwym, 3/3, jak przed). Wnioski: boty „tani” i „agresywny” tracą 10–40 pkt (przypuszczalnie kontrole PIP:
zatrudniają na zleceniu, oraz utrata klientów przy pustym magazynie; osobno nie rozdzielałem), reszta bez zmian w granicach
szumu. Skutek jest zamierzony: zlecenie przestaje być „za darmo”. Gra jako całość się nie zmieniła (spread strategii 99–167).

## Wątpliwości do autora
- **Asteroida:** skoro limit nie działa, pakiety M i L są zawsze droższe bez korzyści. Do decyzji, czy różnicować pakiety
  (np. kadry w cenie, szybsza obsługa) albo zostawić jeden pakiet.
- **Opłata za zmianę biura** dotyczy tylko zmiany na inne biuro z mapy. Samodzielna księgowość „w międzyczasie” nie czyści
  pamięci (A→samo→B płatne), ale A→samo→A jest bez opłaty. Jeśli ma być płatne, trzeba zmienić regułę w `oplata_zmiany`.
- **Józef K. (b):** obejście przez dwa płatne przeskoki (A→JKŚ ze zmianą pakietu, powrót) nadal zmienia pakiet w biurze bez
  opóźnienia, ale zapowiedź i termin zostają, a kosztuje to dwie opłaty za zmianę biura. Tego nie blokowałem dalej.
- **PIP:** liczą się zlecenie i zlecenie ze studentem na stanowisku w pełnym wymiarze. B2B i staż pominięte (autor tego nie
  wymienił). Po karze licznik nie jest zerowany, więc kontrola może się powtarzać co tydzień z szansą 5%.
- **Bot:** boty zatrudniające na zleceniu (agresywny, tani) płacą teraz kary PIP i mają niższe wyniki; nie zmieniałem botów.
- Instrukcja gracza (`INSTRUKCJA.md`) i panel nie opisują jeszcze: opłaty za zmianę biura, PIP, przejęcia debetu. Panel nie
  wyświetla `w["pip"]` ani `debet_przy_zmianie`: dane są w wynikach rundy i we wnioskach (PIP), UI do dopisania przy panelu.

## Notatki funkcji (szkice, bez ruszania repo notatek)
W roboczym folderze etapu 2 (po wtopieniu w notatki funkcji usunięte): `Biura rachunkowe – pakiety (uzupełnienie 14.11).md` (do uzupełnienia: `Biura rachunkowe – pakiety.md`),
`Debet (uzupełnienie 14.11).md` (→ `Debet.md`), `Kadry wg Kodeksu pracy (uzupełnienie 14.11).md` (→ `Kadry wg Kodeksu pracy.md`),
`Pomyłki w szczycie (uzupełnienie 14.11).md` (→ `Pomyłki w szczycie.md`).
