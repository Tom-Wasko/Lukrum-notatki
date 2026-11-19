# balans-katalogi – raport

**Stan:** gotowe (lider, 19.11.2026). Gałąź `balans-katalogi`, kopia `_robocze/balans-katalogi`.
Zakres: decyzje szefa z 18.11 (drobne mechaniki katalogów) i z przeglądu dziur (D1–D2, higiena, klub, tydzień 1),
plus decyzja „5 banków”.

## Co weszło
| Decyzja | Zmiana | Pliki |
|---|---|---|
| Asteroida taniej | pakiety S/M/L 470 / 790 / 1 190 zł (było 590 / 990 / 1 500) | `dane/mapa/biura.yaml`, sceny biura i kamienicy |
| Kasa, lada, tablica menu coś dają | `tempo_obslugi` ★/★★/★★★ (kasa 0,9 / 1,0 / 1,15; lada i tablica 0,95 / 1,0 / 1,1); liczy się w przepustowości | `dane/sprzet.yaml`, `silnik/kuchnia/operacje.py: tempo_kasy` |
| Szafa ★★★ | towar w szafie ★★★ trzyma się dzień dłużej (liczy się najsłabsza szafa) | `sprzet.yaml: dluzszy_termin_dni`, `silnik/kuchnia/swiezosc.py` |
| Lodówka | ★★★ 3 000 zł | `dane/sprzet.yaml`, `sprzet_gastro.js` |
| Szkolenia | efekt × ocena firmy szkoleniowej / najlepsza ocena | `katalog.yaml: skutecznosc_z_oceny`, `silnik/ludzie/szkolenia.py: procent_firmy`, `hr.js` |
| D1 tydzień 1 | sprzęt i dostawcy z Parku handlowego od pierwszego tygodnia | `dane/katalog.yaml` |
| D2 cena bota | zrównoważony bot: cena × 1,05 | `dane/boty.yaml` |
| Higiena „brak” | okienko z mandatem i oszczędnością przed rezygnacją ze sprzątania | `zakladki/urzad.js` |
| Klub w panelu MG | „zablokuj / otwórz” w ustawieniach gry; blokada chowa klub uczniom, kasuje zakłady z bieżącej rundy, nie wysyła zaproszeń | `api/widoki.py`, `silnik/runda.py`, `panel_mg/static/mg/mg.js` |
| 5 banków | Solaris usunięty (dane mapy, sceny, ikony); debet przejmuje Soplicowo: 20 000 zł, 80 zł/tydz., 15% | `dane/mapa/banki.yaml`, `budynki.yaml`, `miasto.yaml`, `bank.js`, `pierzeja_bankowa.js`, `nawigacja.js`, `ikony_marek.js` |

Dokumentacja: `INSTRUKCJA.md` (banki, sprzęt kasy, tydzień 1, szafa, szkolenia, okienko sanepidu; klub celowo
pominięty), `dokumentacja/OPIS_GRY.md` (szafa ★★★), `dokumentacja/SCENARIUSZE_LEKCJI.md` (blokada klubu w panelu MG).

## Testy i pomiary
- Nowe testy: `testy/kuchnia/test_balans_katalogi.py` (5, dane gry), `test_kasyno.py::test_mistrz_gry_blokuje_klub_w_grze`.
- `ruff check .` → All checks passed; `silnik.dane sprawdz` → Dane w porządku.
- Boty, 12 rund, poziom średni, średnia gotówka (main → gałąź): ziarno 7: 58 436 → 60 273; ziarno 3: 56 614 → 64 726;
  ziarno 11: 66 447 → 71 802. Zrównoważony (z D2) zyskuje na każdym ziarnie (88 470 → 92 504, 50 309 → 83 508,
  86 010 → 97 477), agresywny nadal najsłabszy.

## Do wiadomości
- `zakladki/mapa_budynki.js` (stara mapa rysowana, układ `?uklad=stary`) ma na fryzach banków prawdziwe marki
  (PKO BP, Pekao, ING, mBank, Santander, Crédit Agricole). Poza zakresem serii; do decyzji szefa, czy podmienić na fikcyjne.
- Majster dostał wpis w `WSPOLPRACA.md` o usunięciu `bank_6`.
