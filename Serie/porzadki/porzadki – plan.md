# Porządki w `lukrum/` – plan (17.11.2026)

Plan i szkice, nic nie zostało zmienione poza `_robocze/porzadki/`. Wszystkie ścieżki są względne od `lukrum/`
(folder zostanie przeniesiony poza `Levas/`). Stan wyjściowy: repo gry `main` 08268aa, repo notatek `main` 91b2c4a.
Szkice nowych plików: `_robocze/porzadki/szkice/` (29 plików, cel w pierwszej linii każdego).

Zasady układu:
- **`gra/`** = tylko gra. **`notatki/`** = wszystko o projekcie. **`warsztat/`** = sposób pracy, ogólny, **osobne prywatne repo** (np. `Tom-Wasko/warsztat`), bez związku z LUKRUM.
  **`_robocze/`** = tylko tymczasowe.
- Jeden temat = jedna notatka. Stan obecny osobno od historii. Sprawa otwarta żyje tylko w `Do decyzji`.
- Role: szef (autor), lider (Claude Opus), agenci, **majster** (kolega od mapy), **kapitan** (nauczyciel, opiekun).

## (0) Zmiany po decyzjach szefa 16.11 (noc) – wpisał nowy lider 17.11

Ta sekcja ma pierwszeństwo przed resztą planu. Tam, gdzie niżej coś się z nią kłóci, obowiązuje ta sekcja
(drzewo (a), wiersze (b) i kroki (f) są już poprawione; zmienione miejsca mają znak **[Z]**).

| # | Co się zmienia | Było w planie | Teraz |
|---|---|---|---|
| Z1 | **Repo notatek zostaje w `notatki/`** (szef 17.11, pytanie 11b) | – | bez przenoszenia `.git`; analizy jako podfolder sejfu `notatki/Analizy/`, odsyłacze `[[…]]` działają, majster nic nie robi |
| Z2 | **Nowy folder `notatki/Analizy/`** (oceny, research, krytyki, sprawozdania, pozew, SWOT, raporty z nocy) | raporty nocy w `Serie/fable/`, pozew i SWOT poza `lukrum/` | `notatki/Analizy/` (lista w (a)); pozew i SWOT → `archiwum/`, w Analizach tylko streszczenie bez nazwy (9a). `Serie/` zostaje tylko na plany i raporty serii |
| Z3 | **`archiwum/` bez gita** zamiast `_archiwum/` i zamiast usuwania artefaktów | podglądy, makiety, zrzuty, surowe pomiary → „usuń” | → `archiwum/` (podglądy wyglądu 1–4, makiety i zrzuty krytyki, stare zrzuty, surowe wyniki nocy, stare briefy, słownik kodów serii). Usuwamy tylko śmieci: `__pycache__`, `.hypothesis`, `.ruff_cache`, `.pyc` |
| Z4 | **Kody dawnych serii (ok. 420) i martwe odsyłacze czyścimy od razu** | osobna seria `zrodla` po porządkach | nowe kroki 4d–4e: słownik kodów → `archiwum/`, `zrodlo` i komentarze na realia. `testy/dane_zamrozone/` zostają bez zmian (10a) |
| Z5 | **Zwrot z wystroju** (9,8 czy 10,9 tyg.) | pytanie 7 | pomiar w kroku 4d, wynik z datą w `dekor.yaml: zrodlo` |
| Z6 | **`METODA.md` w repo gry** („Jak powstał LUKRUM”, jawność AI) + sprawdzenie regulaminu ZwzT pod kątem AI | brak | nowy krok 11 (research Sonnet + szkic lidera, akceptacja szefa) |
| Z7 | **Panel kontrolny tylko na claude.ai** | `warsztat/panel/README.md` | bez folderu `panel/`; panel to osobna praca po kroku 2 (kroku 12) |
| Z8 | **Fable poza zespołem** od 17.11 8:00 | wiersz Fable w `AGENTS.md` §2 i `LIDER.md` §2 | usunąć w kroku 2 (warsztat) i 4c (AGENTS gry) |
| Z9 | **Majster: scalamy od razu** (szef 17.11) | „scalić aktualny `maciex` przed startem” | zrobione 17.11: `a0e123d` (2 commity: żetony jako przedmioty). Przed krokiem 4 jeszcze raz `git fetch` i scalenie |
| Z10 | **Pamięć** | krok 1: skopiować pamięć | zrobione 17.11 (czysty pakiet z `_robocze/pamiec/`) |
| Z11 | Kopia `_robocze/krytyka` | `worktree remove` w kroku 1 | już jej nie ma (`git worktree list` = tylko `main`) |
| Z12 | `Sprawozdanie – zespół agentów.md` | zostaje w `notatki/Zespół/` | → `notatki/Analizy/` (to sprawozdanie); w `Zespół/` zostaje Dziennik lidera |

Pytania 5–8 z (g) są rozstrzygnięte decyzjami z nocy (zob. (g)). Nowe pytania 9–11 są w (h), na końcu planu.

## (a) Drzewo docelowe

```
lukrum/                         (bez gita)
  CLAUDE.md                     dołącza @warsztat/ZESPOL.md i @gra/AGENTS.md   [szkic lukrum-CLAUDE.md]
  .claude/agents/               KOPIA generowana przez warsztat/zainstaluj.ps1 (nie edytować ręcznie)

  gra/                          repo Tom-Wasko/Lukrum (dziś lukrum_gra/), zawartość dawnego gra/ w korzeniu
    README.md                   [szkic gra-01]
    AGENTS.md                   tylko rzeczy gry: mapa repo, polecenia, silnik, zasady kodu  [szkic gra-03]
    INSTRUKCJA.md, INSTRUKCJA.pdf
    .gitignore [szkic gra-02], .gitattributes
    manage.py, start.bat, hostuj.bat, staly_link.bat, requirements.txt, pyproject.toml
    silnik/ dane/ api/ gry/ konta/ lukrum/ panel_gracza/ panel_mg/ balans/ testy/
    narzedzia/                  mapa/, grafiki/ (+ lokalnie cloudflared.exe, poza gitem)
    dokumentacja/               STACK.md, OPIS_GRY.md, SCENARIUSZE_LEKCJI.md, LOGOWANIE_MICROSOFT.md
    (lokalnie, poza gitem: .venv/, db.sqlite3, lokalne.json, zapisy/)

  notatki/                      repo Tom-Wasko/Lukrum-notatki (sejf Obsidiana, wspólny z majstrem)
    README.md                   indeks i zasady sejfu                    [szkic notatki-01]
    Plan.md                     cel, etapy, role, braki                  [notatki-02]
    Postęp.md                   jedyna lista zadań (dawny POSTEP.md)     [notatki-15]
    Decyzje.md                  obowiązujące decyzje szefa, tematami     [notatki-03]
    Do decyzji.md               tylko sprawy otwarte                     [notatki-04]
    Wygląd.md                   obowiązujący wygląd                      [notatki-05]
    Mapa.md                     strefy, zespoły, spis elementów          [notatki-06]
    Nawiązania literackie.md                                             [notatki-07]
    WSPOLPRACA.md               tablica szef ↔ majster                   [notatki-09]
    Historia.md                 kronika i sprawy rozstrzygnięte          [notatki-08]
    Funkcje/                    18 notatek + _Szablon funkcji.md         [notatki-10…14, warsztat-06]
    Zespół/                     Dziennik lidera.md  [Z] (Sprawozdanie → Analizy/)
    Serie/                      plany i raporty serii (z repo gry i z _robocze)
      Serie.md                  indeks serii                             [notatki-16]
      etap2-mapa/               etap2-mapa – raport.md
      mechaniki-a/              mechaniki-a – raport.md, pomiary/*.md   [Z] (przegląd → Analizy/)
      mechaniki-b/              mechaniki-b – raport.md, pomiary/*.md
      wnetrza-dane/             wnetrza-dane – silnik.md, wnetrza-dane – dane-2.md
      porzadki/                 porzadki – plan.md (ten plik po wykonaniu), porzadki – recenzja.md, STAN.md
    .obsidian/

    Analizy/                    [Z] oceny, research, krytyki, sprawozdania (11b: w sejfie notatek)
    Analizy.md                  indeks: co, kiedy, kto napisał, które wnioski weszły do Decyzje/Postęp
    Sprawozdanie – zespół agentów.md               (z notatki/Zespół/)
    Research – strategia pracy z AI.md            (_robocze/research-strategia/raport.md)
    Ocena sposobu pracy 16.11.md                  (_robocze/ocena-sposobu-pracy/ocena.md)
    Krytyka wnętrz 16.11.md                       (_robocze/krytyka-wyniki/krytyka.md; makiety i zrzuty → archiwum/)
    Przegląd toru A 14.11.md                      (_robocze/przeglad-a-fable.md)
    Pozew i SWOT – wnioski.md                     streszczenie bez starej nazwy (9a); całe pliki → archiwum/
    Noc Fable 15-16.11/         raport.md [notatki-17], przegląd prawny.md, instrukcja.md, katalogi.md, lekcje.md,
                                pip.md, pomiary/dekor.md, pomiary/katalogi.md, zrzuty/*.png (8 zrzutów, ilustracja)

  archiwum/                     [Z] BEZ gita (zastępuje pusty _archiwum/), tylko lokalnie
    LEGENDA.md                  co tu jest i skąd (jedna linia na folder)
    wyglad-podglady/            podglądy 1–4, brief_podglady2, zrzuty4/, wyglad/grafiki/
    krytyka-16.11/              makiety/, zrzuty/
    etap1/, etap2-briefy/, mechaniki-a-surowe/, fable-noc-surowe/   briefy, csv, log, txt, png z _robocze i fable_noc
    briefy/                     BRIEF_AGENTA.md, BRIEF_FABLE_NOC.md, wnetrza-silnik-brief.md
    prawne/                     podobienstwa.md, pozew-…-fable.md, swot-fable.md (9a)
    kody-serii.md               słownik starych kodów (U20, UF6, F3a…) → co znaczyły (krok 4d)

  warsztat/                     OSOBNE repo git (prywatne, np. Tom-Wasko/warsztat), bez LUKRUM w treści  [szkice warsztat-01…08]
    README.md, ZESPOL.md, LIDER.md
    szablony/                   brief.md, raport.md, plan-serii.md, notatka-funkcji.md
    agents/                     zwiadowca.md, wykonawca.md, recenzent.md
    narzedzia/                  cdp.py, zrzuty.py, nowa_kopia.sh
    zainstaluj.ps1, .gitignore
                                [Z] bez panel/: panel kontrolny jest tylko stroną na claude.ai (krok 12)

  _robocze/                     puste poza bieżącą serią: <seria>/ i kopie <seria>-<temat>/
```
[Z] `_archiwum/` zmienia nazwę na `archiwum/` (bez gita). Dokumenty ze starą nazwą (pozew, SWOT, podobieństwa) → `archiwum/prawne/` (9a).

Nazwy plików w `Serie/` mają postać `<seria> – <temat>.md`, a nie `plan.md`/`raport.md`: w Obsidianie nazwy muszą
być unikalne w sejfie, inaczej `[[raport]]` jest niejednoznaczny.

### Co łamie spłaszczenie `lukrum_gra/gra/` → korzeń repo (sprawdzone grepem)

| # | Miejsce | Skutek | Poprawka |
|---|---|---|---|
| 1 | `.gitignore`: `gra/zapisy/`, `gra/lokalne.json`, `gra/narzedzia/` | baza, ustawienia lokalne i `cloudflared.exe` (60 MB) przestają być ignorowane | szkic `gra-02-gitignore.txt` (`zapisy/`, `lokalne.json`, `narzedzia/cloudflared.exe`) |
| 2 | kolizja `gra/narzedzia/` (lokalny `cloudflared.exe`) z `narzedzia/` (grafiki, mapa) | po spłaszczeniu to jeden folder; `hostuj.py:47` szuka `BASE_DIR/narzedzia/cloudflared.exe` | przenieść exe ręcznie do `narzedzia/`; kod bez zmian |
| 3 | `testy/aplikacja/test_swiat.py:52` `GRA.parent / "narzedzia" / "grafiki" / "zestaw.py"` | **test czerwony** | `GRA / "narzedzia" / …` |
| 4 | `balans/warianty.py:58` `KATALOG_GRY.parent / "raporty" / "kalibracja" / "pomiary"` | pomiary lądują w `lukrum/raporty/` | `KATALOG_GRY.parent / "_robocze" / "pomiary" / "kalibracja"`; poprawić opis w `STACK.md` |
| 5 | `narzedzia/grafiki/zbuduj.py:16` `os.path.join(REPO, 'gra', 'panel_gracza', 'static')` + teksty w liniach 1, 58–59 | generator pisze w złe miejsce | usunąć człon `'gra'`; po zmianie uruchomić, bo generuje `static/grafiki/README.md` |
| 6 | `narzedzia/grafiki/zestaw.py:15` `parents[2] / "gra" / "panel_gracza"…` | jw. (używany przez test z #3) | usunąć `"gra"` |
| 7 | `narzedzia/mapa/pobierz_osm.py:28–29` `REPO / "gra" / "dane"…`, docstring l. 1 i 8 | skrypt majstra pisze w złe miejsce | usunąć `"gra"`; **uprzedzić majstra** |
| 8 | `start.bat`, `hostuj.bat`, `staly_link.bat` | **nic** – używają `%~dp0` i ścieżek względnych, przenoszą się razem z `manage.py` | tylko sprawdzić uruchomieniem |
| 9 | `pyproject.toml` (`testpaths`, `pythonpath`, ruff) | **nic** – ścieżki względne do własnego folderu | – |
| 10 | `silnik/dane.py:37` `parents[1]`, `lukrum/settings.py:8` `BASE_DIR`, `panel_gracza/instrukcja.py:16`, testy z `parents[2]` (`test_ikony_marek.py:9`, `test_nazwy_zakladek.py:11`) | **nic** – liczone względem pliku | – |
| 11 | `.venv/` (`pyvenv.cfg` i programy w `Scripts/` mają ścieżkę bezwzględną `…\Levas\lukrum\lukrum_gra\gra\.venv`) | środowisko przestaje działać już po samym przeniesieniu `lukrum/` | usunąć i założyć od nowa (`start.bat` robi to sam) |
| 12 | pliki lokalne poza gitem w `gra/`: `db.sqlite3`, `lokalne.json`, `zapisy/`, `narzedzia/cloudflared.exe`, `.hypothesis/` | `git mv` ich nie przeniesie | przenieść ręcznie (`.hypothesis/` i `.ruff_cache/` usunąć) |
| 13 | dokumenty z przedrostkiem `gra/`: `README.md` (5), `AGENTS.md` (4), `STACK.md` (6), `OPIS_GRY.md` (2), `static/grafiki/README.md` (generowany) | martwe ścieżki | README i AGENTS ze szkiców; w STACK i OPIS podmiana; komentarze `lukrum/settings.py:39`, `static/mapa/lublin.js:2`, `silnik/schematy.py:656` |
| 14 | `LOGOWANIE_MICROSOFT.md` → `dokumentacja/` | odsyłacze w README, OPIS_GRY, STACK, `settings.py:39` | podmiana ścieżki |
| 15 | `.git/info/exclude` (wpisy `zrzuty/`, `pomiary/`, `PLAN.md`, `RAPORT.md`…; `core.ignorecase=true`) | ukrywa przed gitem każdy `plan.md`, `raport.md` i `pomiary/` w repo gry | wyczyścić plik |
| 16 | gałąź `maciex` majstra i jego lokalna kopia | po spłaszczeniu każda jego zmiana trafia w przeniesione pliki; git zwykle rozpozna przeniesienie, ale konflikty są możliwe | spłaszczać zaraz po scaleniu aktualnego `maciex`; majster robi `git pull` i odtwarza `.venv`; wpis w WSPOLPRACA |
| 17 | kopia robocza `_robocze/krytyka` (worktree, 08268aa) | po przeniesieniu `lukrum/` ma martwe ścieżki, a układ sprzed spłaszczenia | po odebraniu wyników `git worktree remove` (albo `git worktree repair`) |
| 18 | `CLAUDE.md` (`@lukrum_gra/AGENTS.md`), `.claude/agents/*.md` („`lukrum_gra/AGENTS.md`”), `AGENTS.md` §5 (`../../_robocze/narzedzia/cdp.py`), `LIDER.md` | martwe ścieżki | szkice `lukrum-CLAUDE.md`, `warsztat-02` |
| 19 | pamięć Claude Code: katalog `~/.claude/projects/C--Users-PC-Pulpit-Levas/memory/` jest przypisany do starej ścieżki startu | sesje z nowego miejsca nie wczytają pamięci (23 wpisy, w tym zasady commitów) | skopiować `memory/` do katalogu nowej ścieżki albo przenieść treść do `CLAUDE.md`/warsztatu; poprawić ścieżki we wpisach |
| 20 | `dane/mapa/dekor.yaml:12, 21, 25` – `zrodlo` wskazuje `_robocze/fable/pomiary/dekor.md` (nie istnieje) i podaje 9,8 tyg., a pomiar 10,9 | martwy odsyłacz w danych gry | **[Z]** `zrodlo`: „pomiar <data>, notatki/Analizy/Noc Fable 15-16.11/pomiary/dekor.md”; liczba z nowego pomiaru (krok 4d) |

Nie łamie się nic więcej: w repo nie ma CI (`.github/`), a adresy URL `/gra/…` to trasy Django, nie ścieżki plików.

## (b) Każdy obecny plik i folder → akcja

Akcje: **zostaje**, **przenieś**, **scal**, **przepisz** (jest szkic), **popraw** (kilka linii), **usuń**.

### Korzeń `lukrum/`
| Obecnie | Akcja | Powód |
|---|---|---|
| `CLAUDE.md` | przepisz (szkic `lukrum-CLAUDE.md`) | nowe nazwy folderów, dołącza warsztat i `gra/AGENTS.md`, nazywa role |
| `.claude/agents/{zwiadowca,wykonawca,recenzent}.md` | przenieś źródło do `warsztat/agents/`, tu zostaje kopia z instalatora | definicje mają być ogólne i przenośne między projektami |
| `_archiwum/` (pusty) | **[Z]** zmień nazwę → `archiwum/` (bez gita) | decyzja 16.11 (noc) |
| `lukrum_gra/` | zmień nazwę folderu na `gra/` | decyzja szefa |

### Repo gry (`lukrum_gra/`, poza kodem)
| Obecnie | Akcja | Powód |
|---|---|---|
| `README.md` | przepisz (szkic `gra-01`) | opisuje „gałąź fable do przeglądu” i `fable_noc/`, tabela stanu nieaktualna |
| `AGENTS.md` (zmieniony, niezacommitowany) | podziel: gra → `gra/AGENTS.md` (szkic `gra-03`), zespół → `warsztat/ZESPOL.md` | podział w `szkice/warsztat-02` |
| `gity.txt` | usuń | dwa adresy repo, są w README i `CLAUDE.md` |
| `.gitignore` | przepisz (szkic `gra-02`) | ścieżki z `gra/` po spłaszczeniu |
| `.gitattributes` | zostaje | – |
| `.ruff_cache/`, `gra/.hypothesis/`, `narzedzia/grafiki/__pycache__/` | usuń (lokalne, poza gitem) | śmieci; `.hypothesis` ma w środku stare ścieżki ze starą nazwą projektu |
| `dokumentacja/POSTEP.md` | przenieś i przepisz → `notatki/Postęp.md` (szkic `notatki-15`) | to stan projektu, nie gry; obecny ma nieodhaczone rzeczy zrobione 14–16.11 |
| `dokumentacja/OPIS_GRY.md` | zostaje, popraw teraz ścieżki i 40 000 → 50 000 zł; pełne przepisanie w osobnej serii | opisuje układ z zakładkami sprzed mapy (dług wpisany w `Postęp.md`) |
| `dokumentacja/STACK.md` | zostaje, popraw: ścieżki `gra/`, liczba testów (440 → 740), motywy, `raporty/kalibracja` | dokumentacja techniczna gry |
| `dokumentacja/SCENARIUSZE_LEKCJI.md` | zostaje, popraw nagłówek „projekt Fable” → „projekt z 16.11.2026” | materiał dla nauczyciela, część gry |
| `dokumentacja/zespol/LIDER.md` (nieśledzony) | przenieś → `warsztat/LIDER.md`, bez nazw LUKRUM | protokół ogólny; zmiany w `szkice/warsztat-02` |
| `raporty/etap2-mapa/raport.md` | przenieś → `notatki/Serie/etap2-mapa/etap2-mapa – raport.md` | raporty serii idą do notatek |
| `fable_noc/RAPORT.md`, `ZMIANY.md`, `DZIENNIK.md`, `PLAN.md`, `MAPA_POMYSLY.md` | **[Z]** scal → `notatki/Analizy/Noc Fable 15-16.11/raport.md` (szkic `notatki-17`), oryginały → `archiwum/fable-noc-surowe/`, w repo gry `git rm` | pięć dzienników nocy = jeden raport zbiorczy; historia w gicie gry |
| `fable_noc/pozew-2.md` | **[Z]** przenieś → `notatki/Analizy/Noc Fable 15-16.11/przegląd prawny.md`, popraw | zmiany: tytuł „Przegląd prawny”, usunąć zdanie „Wzór: `_robocze/pozew-…`”, zaślepki „[inna gra]”/„[poprzednia gra]” → „innych gier biznesowych”, ścieżki `gra/…` |
| `fable_noc/pomiary/dekor.md`, `katalogi.md` | **[Z]** przenieś → `notatki/Analizy/Noc Fable 15-16.11/pomiary/` | wyniki, na które powołują się dane gry |
| `fable_noc/pomiary/dekor_pomiar.py` | przenieś → `gra/balans/dekor_pomiar.py` | to kod pomiaru; sprawdzić importy i `ruff` |
| `fable_noc/pomiary/katalogi_{przed,po1,po2}.txt`, `czas_{przed,po1}.txt` | **[Z]** → `archiwum/fable-noc-surowe/` | surowe wydruki, streszczone w `katalogi.md` |
| `fable_noc/zrzuty/*.png` (8 plików, 1,6 MB) | **[Z]** przenieś → `notatki/Analizy/Noc Fable 15-16.11/zrzuty/` | decyzja 16.11 (noc): ilustracja raportu |
| `narzedzia/grafiki/{baza,postacie,wnetrza,zbuduj,zestaw}.py`, `dane.json`, `szablon4.html` | zostaje, popraw ścieżki w `zbuduj.py` i `zestaw.py` | generator grafik, używa go test |
| `narzedzia/grafiki/podglad4.html` (generowany, ignorowany) | zostaje lokalnie | odtwarza go `zbuduj.py` |
| `narzedzia/mapa/pobierz_osm.py` | zostaje, popraw ścieżki | skrypt majstra |
| `gra/INSTRUKCJA.md`, `gra/INSTRUKCJA.pdf` | przenieś do korzenia repo (spłaszczenie); PDF przegenerować | czyta je `panel_gracza/instrukcja.py` z `BASE_DIR` |
| `gra/LOGOWANIE_MICROSOFT.md` | przenieś → `gra/dokumentacja/LOGOWANIE_MICROSOFT.md` | dokument techniczny dla informatyka, nie dla gracza |
| `gra/panel_gracza/static/mapa/podglad_lokali.html` | zostaje do decyzji o ikonie lokalu, potem usuń | strona wyboru wariantu (w `Do decyzji`) |
| `gra/panel_gracza/static/grafiki/README.md` | zostaje (generuje `zbuduj.py`) | spis grafik przy grafikach |
| `gra/start.bat`, `hostuj.bat`, `staly_link.bat`, `manage.py`, `pyproject.toml`, `requirements.txt` | przenieś do korzenia (spłaszczenie), bez zmian treści | – |
| `gra/db.sqlite3`, `gra/lokalne.json`, `gra/zapisy/`, `gra/narzedzia/cloudflared.exe` | przenieś ręcznie do korzenia / `narzedzia/` | poza gitem |
| `gra/.venv/` | usuń i załóż od nowa | ścieżki bezwzględne |
| `.git/info/exclude` | wyczyść | ukrywa `plan.md`, `raport.md`, `pomiary/` |

### Repo notatek (`notatki/`)
| Obecnie | Akcja | Powód |
|---|---|---|
| `README.md` | przepisz (szkic `notatki-01`) | staje się jedynym indeksem |
| `LUKRUM.md` | scal z `README.md`, usuń | drugi indeks o tej samej treści; mówi „bez logo”, co jest nieaktualne |
| `PLAN_PRZEBUDOWY.md` | podziel i usuń: rozdz. 1, 4, 12 → `Plan.md`; 2, 7, 10, 11 → `Decyzje.md`; 6 → `Mapa.md`; 8 i tabela nazw z 11 → `Nawiązania literackie.md`; 3, 5, 9 → nieaktualne (`Historia.md`, warsztat) | miesza cel, decyzje, historię i sposób pracy; 24 wzmianki starej nazwy |
| `Do decyzji.md` | przepisz (szkic `notatki-04`) | 2/3 treści to sprawy odhaczone; zostają tylko otwarte |
| `Wygląd.md` | przepisz (szkic `notatki-05`) | chronologia podglądów → jeden obowiązujący stan |
| `WSPOLPRACA.md` | przepisz (szkic `notatki-09`) | „Start dla [mapa]” wykonany, zasada PR zmieniona 16.11, dziennik odsyła do usuwanych plików |
| `Mapa – elementy.md` | przenieś i scal → `Mapa.md` (szkic `notatki-06`) | jedna notatka o mapie, z rozdz. 6 planu i zmianami z 15–16.11 |
| `Wnioski Fable 14.11.md` | streszczone w `Historia.md` i `Plan.md` §3, usuń | notatka z datą; 6 wzmianek starej nazwy |
| `Plan na 14.11.md` | streszczone w `Historia.md`, usuń | plan jednego dnia, wykonany |
| `Funkcje/Biura rachunkowe – pakiety.md`, `Debet.md`, `Kadry wg Kodeksu pracy.md`, `Pomyłki w szczycie.md`, `Wyposażenie i udogodnienia.md` | przepisz (szkice `notatki-10…14`) | doklejone sekcje „Zmiany 14.11” wtopione w treść; nieaktualny „Stan” |
| `Funkcje/Banki z lektur.md`, `Kapitał startowy.md`, `Wynik 0–1000 pkt.md` | popraw `Stan` → „w grze (PR #2, 14.11.2026)” i `Gdzie w grze` (Kamienica bankowa; Plan tygodnia; redakcja „Kuriera rankingowego”) | „na gałęzi mechaniki-a, czeka na zatwierdzenie” jest nieprawdą od 14.11 |
| `Funkcje/Dymki przy ladzie.md` | popraw `Stan` → „w grze (PR #5; wnętrze kebaba i przełącznik mistrza gry 16.11)”; dopisać listę 8 zaczepek WOS ze źródłami (z obecnego `Do decyzji`) | lista zaczepek znika z `Do decyzji`, a jest potrzebna do lekcji |
| `Funkcje/Księga gości…`, `Kurier rankingowy (gazeta).md`, `List od wujka…`, `Miejsca zamiast zakładek…`, `Sklep meblowy Meblościanka (dekor).md` | popraw `Stan` → „w grze (main, 16.11.2026); do akceptacji szefa” | gałęzie `fable-*` już nie istnieją |
| `Funkcje/Wysoka widoczność.md` | popraw `Stan` → przełącznik w menu ⚙ działa od 16.11 | – |
| `Funkcje/Logo i zastrzeżenie marek.md` | popraw 2 odsyłacze: `[[Wnioski Fable 14.11]]` → `[[Decyzje]]`, „rozdz. 7 planu przebudowy” → `[[Decyzje]]` | cele odsyłaczy znikają |
| `Funkcje/Kasyno Pod Złotym Koziołkiem.md`, `Szperacz (rękopis w danych).md` | zostaje | aktualne |
| `Funkcje/_Szablon funkcji.md` | przepisz (szkic `warsztat-06`) | dochodzi „Liczby i źródła”, „Otwarte” i zasada „bez sekcji Zmiany” |
| `Zespół/Dziennik lidera.md` (nieśledzony) | zostaje; lider poprawia ścieżkę startu sesji i nazwy ról | dziennik projektu |
| `Zespół/Sprawozdanie – zespół agentów.md` | **[Z]** przenieś → `notatki/Analizy/`; część ogólna staje się podstawą `warsztat/ZESPOL.md` | zob. `szkice/warsztat-02` |
| `_robocze/` (210 śledzonych plików, 4,5 MB, w tym 4 pliki `.pyc`) | usuń z repo w całości | migawka folderu roboczego: briefy, logi, csv, podglądy HTML; 17 plików ze starą nazwą; to, co warte zachowania, idzie do `Serie/` z oryginałów w `lukrum/_robocze/` |
| `.obsidian/`, `.gitignore` | zostaje | – |
| gałąź zdalna `fable` | usuń (scalona, = `main`) | pytanie z dziennika lidera |

### `_robocze/` (poza repo)
| Obecnie | Akcja | Powód |
|---|---|---|
| `BRIEF_AGENTA.md` | **[Z]** → `archiwum/briefy/` | zastąpiony przez `AGENTS.md` i warsztat; stare ścieżki i stara nazwa |
| `BRIEF_FABLE_NOC.md` | **[Z]** → `archiwum/briefy/` | jednorazowy brief; przebieg streszczony w `Historia.md` i `fable – raport.md` |
| `etap1/brief_*.md`, `agent_{B,C,D}.md`, `D_pytest.txt`, `D_*.png`, `zrzuty/` | **[Z]** → `archiwum/etap1/` | etap 1 zamknięty 13.11, wynik w `Serie.md`; pliki mają starą nazwę |
| `etap1/podobienstwa.md` | **[Z]** → `archiwum/prawne/podobienstwa.md` | 57 wzmianek starej nazwy, nie może trafić do żadnego repo |
| `etap2/mechaniki-b-raport.md` | przenieś → `notatki/Serie/mechaniki-b/mechaniki-b – raport.md` | raport serii |
| `etap2/wnetrza-dane-2-raport.md`, `wnetrza-silnik-raport.md` | przenieś → `notatki/Serie/wnetrza-dane/wnetrza-dane – dane-2.md`, `– silnik.md` | raporty serii |
| `etap2/pomiary/{przed,po}_punkty.md` | przenieś → `notatki/Serie/mechaniki-b/pomiary/` | tabele wyników |
| `etap2/mechaniki-b.md`, `wnetrza-dane-2.md`, `wnetrza-silnik-brief.md` (i `_robocze/wnetrza-silnik-brief.md`) | **[Z]** → `archiwum/etap2-briefy/` | briefy wykonane, ścieżki bezwzględne |
| `etap2/notatki/*.md` (6 szkiców) | usuń | treść jest w `Funkcje/` (sprawdzone: 4 „uzupełnienia” = sekcje „Zmiany 14.11”, „Zestawy wyposażenia” = część „Wyposażenie i udogodnienia”, „Dymki przy ladzie” istnieje) |
| `etap2/pomiary/*.txt` | **[Z]** → `archiwum/etap2-briefy/pomiary/` | surowe wydruki |
| `fable-raporty/{instrukcja,katalogi,lekcje,pip}.md` | **[Z]** przenieś → `notatki/Analizy/Noc Fable 15-16.11/<temat>.md`, popraw ścieżki | **jedyne kopie** raportów czterech agentów; `katalogi.md` ma inwentarz skutków jakości w silniku |
| `mechaniki-a-raport/raport.md` | przenieś → `notatki/Serie/mechaniki-a/mechaniki-a – raport.md`, popraw linie 3, 274, 283 | dowód własnego balansowania; 3 wzmianki starej nazwy do usunięcia |
| `mechaniki-a-raport/pomiary/*_punkty.md`, `d14_*.md`, `c2_koszty_bankow.md`, `c2_banki/raport.md`, `c3_biura/raport.md`, `c4_urlop/raport.md` | przenieś → `notatki/Serie/mechaniki-a/pomiary/` (nazwy `c2_banki.md` itd.) | tabele wyników |
| `mechaniki-a-raport/pomiary/*.csv`, `*.log`, `*.time`, `*.txt`, `brief_M.md` | **[Z]** → `archiwum/mechaniki-a-surowe/` | surowe dane i brief |
| `przeglad-a-fable.md` | **[Z]** przenieś → `notatki/Analizy/Przegląd toru A 14.11.md`, usuń linię 172 | 12 znalezisk z uzasadnieniem prawnym; 1 wzmianka |
| `pozew-revas-fable.md`, `swot-fable.md` | **[Z]** → `archiwum/prawne/` + streszczenie wniosków bez nazwy → `notatki/Analizy/Pozew i SWOT – wnioski.md` (9a) | 38 i 22 wzmianki starej nazwy; wnioski są w `Decyzje`, `Do decyzji`, `Plan` §3, `Historia` |
| `wyglad/podglady.html`, `podglady2.html`, `podglad3.html`, `podglad3_szablon.html`, `podglad4.html`, `brief_podglady2.md`, `zrzuty4/`, `zrzuty4$1.png` | **[Z]** → `archiwum/wyglad-podglady/` | decyzja 16.11 (noc): artefakty do archiwum |
| `wyglad/grafiki/` (SVG, `_narzedzia/`, `zmienne.css`) | **[Z]** → `archiwum/wyglad-podglady/grafiki/` | starsza kopia tego, co jest w repo gry (`static/grafiki/`, `narzedzia/grafiki/`) |
| `narzedzia/cdp.py`, `zrzuty.py` | przenieś → `warsztat/narzedzia/` | narzędzia agentów; poprawić stałą ścieżkę Chrome na zmienną środowiskową z wartością domyślną |
| `narzedzia/__pycache__/` | usuń | – |
| `krytyka-wyniki/` | **[Z]** `krytyka.md` → `notatki/Analizy/Krytyka wnętrz 16.11.md` (odsyłacze do zrzutów → `archiwum/krytyka-16.11/`), `makiety/`, `zrzuty/` → `archiwum/krytyka-16.11/` | kopia `krytyka/` już usunięta |
| `research-strategia/raport.md`, `ocena-sposobu-pracy/ocena.md` | **[Z]** → `notatki/Analizy/Research – strategia pracy z AI.md`, `notatki/Analizy/Ocena sposobu pracy 16.11.md` | decyzja 16.11 (noc) |
| `pamiec/` | **[Z]** usuń (skopiowane do pamięci Claude Code 17.11) | – |
| `porzadki/` | po wykonaniu: `plan.md` → `notatki/Serie/porzadki/porzadki – plan.md`, `szkice/` usuń | – |

**Liczby.** Usunięcia: ok. 290 plików (210 śledzonych w `notatki/_robocze`, ok. 75 w `lukrum/_robocze`, 12 w repo gry
i notatek). Scalone albo przepisane: 21 (5 plików `fable_noc` → 1; `README`+`LUKRUM` → 1; `PLAN_PRZEBUDOWY` → 5 notatek;
`Mapa – elementy` + rozdz. 6 → 1; 5 notatek funkcji; `Do decyzji`, `Wygląd`, `WSPOLPRACA`, `POSTEP`, README gry).
Przeniesione do `notatki/Serie/`: ok. 30 (raporty i tabele pomiarów). Nowe: repo `warsztat/` (ok. 15 plików).

## (c) Decyzje i informacje do przeniesienia przy scalaniu

Każda pozycja była sprawdzona: skąd pochodzi i gdzie jest w szkicach. Wykonawca nie skraca tych fragmentów.

| Co | Skąd (usuwane albo przepisywane) | Dokąd (szkic) |
|---|---|---|
| Nazwa LUKRUM, *lucrum cessans*, cel projektu, konkurs, UM i kuratorium | `PLAN_PRZEBUDOWY` rozdz. 1 | `Plan.md` §1 |
| Tabela 17 decyzji z 13.11 (branże w danych, kasyno, marki, commity, README…) | `PLAN_PRZEBUDOWY` rozdz. 2 i 10 | `Decyzje.md` (Projekt, Marki, Klub) |
| Tekst zastrzeżenia marek i zasada „złe cechy tylko postaciom wymyślonym” | `PLAN_PRZEBUDOWY` rozdz. 7 | `Decyzje.md` „Marki i prawo” |
| **Zmiana decyzji o logo** (13.11 „bez logo” → 14.11 „uproszczone znaki zostają”) | `Wnioski Fable`, `Do decyzji`, `Logo i zastrzeżenie marek` | `Decyzje.md` + `Historia.md` (tabela spraw rozstrzygniętych) |
| Tor A i tor B: lista mechanik | `PLAN_PRZEBUDOWY` rozdz. 11 | `Decyzje.md` (Wynik, Pieniądze, Biura, Ludzie, Katalogi) + `Postęp.md` „Mechaniki” |
| Decyzje toru A z 13–14.11 (waga otwarcia 1,0; debet; Scrooge 6 zł; urlop 10%; zlecenie −0,04 i PIP; Asteroida bez limitu; opłata za zmianę biura; pomyłki 5,2%/2,8%; boty i wyposażenie) | `Do decyzji` (odhaczone) | `Decyzje.md` |
| Firma bezczynna 0–100 pkt, debet na koniec tygodnia, stopy do limitu | `Wnioski Fable` | `Decyzje.md` |
| „Ceny pod rozgrywkę, podatki i przepisy prawdziwe” | `Do decyzji` | `Decyzje.md` „Marki i prawo” |
| Style wystroju → grupy gości; ceny 900–3 200 zł; próg 40%; cel zwrotu 8–12 tyg. | `Do decyzji` „Podgląd 4” | `Decyzje.md` „Katalogi i wystrój” |
| Dymki: gracz nie wyłącza; wskazówka bez liczb; plotka w tej samej rundzie | `Do decyzji` „Wnętrza i testy” | `Decyzje.md` „Goście i dymki” |
| **8 zaczepek WOS z podstawą prawną** (paragon, alergeny, cena brutto, reklamacja, praca 16-latka, monitoring, płatność kartą, odroczona płatność) | `Do decyzji` | `Funkcje/Dymki przy ladzie.md` – **do dopisania przez wykonawcę 1:1** (nie ma szkicu) |
| 4 sprawdzone cytaty i uwagi (Rzecki, Judym, Józio) | `Do decyzji` | `Nawiązania literackie.md` |
| Zasady nawiązań, 13 nawiązań, tabela 11 nazw banków, biur i mediów | `PLAN_PRZEBUDOWY` rozdz. 8 i 11 | `Nawiązania literackie.md` |
| Tabela 13 miejsc na mapie; 10 stref; sanepid; park handlowy; zespoły | `PLAN_PRZEBUDOWY` rozdz. 6, `Mapa – elementy` §3 | `Mapa.md` §1–2 (spis §3–4 przeniesiony bez zmian) |
| Decyzje z 16.11: bez terminu; scalenia po akceptacji; agenci mogą zmieniać mapę; biura w osobnej kamienicy; agencje w biurowcu z windą; pulpit z mapą na cały ekran; lista wujka przybliża mapę; krytyka wnętrz | `Zespół/Dziennik lidera` (zostaje) | powtórzone w `Decyzje.md`, `Wygląd.md`, `Mapa.md` §2, `Postęp.md` „Teraz” |
| Wygląd: 14 ustaleń z 13.11, rola wnętrza A + C, wejście bez animacji, palety, kroje, wysoka widoczność, osobne paski, dźwięk, pora dnia, wujek | `Wygląd.md` (stary) | `Wygląd.md` (nowy), niewdrożone w osobnym rozdziale |
| Umowy na granicy: lista miejsc, `otworzWnetrze`/`wrocNaMape`, lista zmiennych CSS, `data-paleta`/`data-tryb`, zależność od `data-id` i `.lm-kafel` | `WSPOLPRACA` (stary) | `WSPOLPRACA` (nowy) – przeniesione w całości |
| Zmiany majstra z 15.11, które odwracają decyzje szefa (strefa = dzielnica; 7 lokali z nowymi adresami) | `raporty/etap2-mapa/raport.md` | raport zostaje w `Serie/`; pytania w `Do decyzji` §3; tabela stref w `Mapa.md` |
| 11 otwartych spraw po przeglądzie prawnym (Nocna 13, znaki marek, opisy cen sieci, zlecenie, debet, Józio i Solaris, numery domów, „Pewex”…) | `Do decyzji` „Po nocy Fable” | `Do decyzji` §1–2 |
| Otwarte od 13–14.11: stałe modelu, harmonogram odblokowań, pakiety M/L Asteroidy, różnice biur, rozmowa z prawnikiem | `Do decyzji` | `Do decyzji` §1 i §4 |
| „Przebieg lekcji ok. 4 tygodnie, ale się nie sugeruj”; presety później | `PLAN_PRZEBUDOWY` rozdz. 10 | `Do decyzji` §5, `Decyzje.md` „Lekcje” |
| Braki w planie (lekcja 45 min, przewodnik nauczyciela, podstawa programowa, serwer, RODO, gra próbna, termin konkursu 31.03.2027) | `Wnioski Fable` §3 (ze SWOT) | `Plan.md` §3 |
| 12 usterek z przeglądu toru A i co z nimi zrobiono | `Wnioski Fable` §1 | `Historia.md` (streszczenie); pełny przegląd w `Serie/mechaniki-a/` |
| 18 tematów nocy: co widzi gracz, pliki, ocena; 9 decyzji agenta bez szefa; niedokończone; pomysły do mapy | `fable_noc/ZMIANY`, `DZIENNIK`, `RAPORT`, `MAPA_POMYSLY`, `PLAN` | `Serie/fable/fable – raport.md` |
| Parametry wystroju (+0,8% popytu, +0,07★, próg 40%/20%), trybu lekcyjnego (3 rundy, 7 dni, `zamykaj_rundy`) | `fable_noc/ZMIANY` | `fable – raport.md` „Szczegóły”; `Funkcje/Sklep meblowy…` już to ma |
| Wyniki pomiarów katalogów i wystroju | `fable_noc/pomiary/*.md` | przeniesione + streszczone w `Serie.md` |
| Nieodhaczone zadania mapy (geo lokali, odsyłacze w opisach, opisy 11 punktów, boty, „Stara mapa”) | `POSTEP.md`, raport mapy | `Postęp.md` „Etap 2” |
| Zasada z rozdz. 9 planu: jeden commit na skończoną część, README zawsze aktualny, brief zamiast odkrywania | `PLAN_PRZEBUDOWY` rozdz. 9 | już w `AGENTS.md`/`LIDER.md` → warsztat; z notatek znika |

Świadomie **nie** przenoszę (nieaktualne albo dotyczy tylko historii): biała lista przenoszenia plików (rozdz. 5),
drzewo folderu z rozdz. 3, „Start dla [mapa]”, pytanie o `serce` stref, plan dnia 14.11, harmonogram nocy.

## (d) Ślady starej gry („Revas/REVAS”) i starej nazwy projektu („Levas”)

### Repo gry
| Gdzie | Co | Co zrobić |
|---|---|---|
| pliki śledzone w `main` | **0 trafień** (`git grep -i`) | – |
| historia: treść i opisy commitów (`git log --all -G`, `--grep`) | **0 trafień** | – |
| `AGENTS.md` l. 25 (zmiana niezacommitowana) | „Nie czytaj `Levas/levas_gra`, `Levas/_archiwum`…” | **usunąć przed commitem**; po przeniesieniu folderu zdanie i tak jest zbędne |
| `fable_noc/PLAN.md`, `RAPORT.md`, `pozew-2.md` | zaślepki „[inna gra]”, „[poprzednia gra]”, „rusztowanie z [poprzedniej gry]” (7 miejsc) | nie zawierają nazwy, ale głośno mówią, że coś ukryto; znikają z repo gry, a w przenoszonym przeglądzie prawnym → „innych gier biznesowych” |
| `gra/.hypothesis/`, `.ruff_cache/`, `.venv/` (poza gitem) | ścieżka dysku `…\Levas\…` | usunąć; odtworzą się z nową ścieżką |
| nazwy gałęzi i plików | brak | – |
| pośrednie: w danych i komentarzach kody dawnych serii (U20, B8, UF6, F3a… ok. 420 miejsc) i ok. 25 odsyłaczy do nieistniejących dokumentów (`raporty/funkcje/plan.md`, `notatki/Menu i składniki.md`, `raporty/kalibracja/…`) | nie wymieniają nazwy, ale wskazują na wcześniejszy projekt | poza zakresem porządków (to kod); wpisane jako dług w `Postęp.md`; proponuję osobną serię |

### Repo notatek
| Gdzie | Ile | Co zrobić |
|---|---|---|
| `PLAN_PRZEBUDOWY.md` (tytuł „plan przebudowy Levasa”, wymaganie „Zero śladów Revasa”, etap 1, rozdz. 5 i 11) | 24 | plik znika; w `Plan.md` wymaganie brzmi „gra własna, nic z innych gier biznesowych” |
| `Wnioski Fable 14.11.md` | 6 | plik znika |
| `Do decyzji.md` (nagłówek „Symulowany pozew REVAS”, „stałe wspólne z REVAS”, „folder `revas_26`”, „testy na Levasie”) | 4 | przepisane bez nazw („stałe modelu popytu i reklamy przeliczyć od zera”, „rozmowa z prawnikiem o materiałach porównawczych”) |
| `WSPOLPRACA.md` zasada 7 „Nic z gry Revas” | 1 | „Nic z innych gier biznesowych” |
| `_robocze/` – 17 plików, w tym **nazwa pliku `_robocze/pozew-revas-fable.md`**, `etap1/podobienstwa.md` (57), `swot-fable.md` (22), briefy, 4 pliki `.pyc` ze ścieżką dysku | ok. 190 | cały folder znika z repo |
| `Zespół/Dziennik lidera.md` l. 13 (nieśledzony) | 1 (ścieżka `Pulpit\Levas\lukrum`) | lider poprawia po przenosinach |
| historia gita | 6 z 28 commitów | **zostaje w historii** – pytanie 3 |

### Poza repo (`lukrum/_robocze/`)
22 pliki, wszystkie do usunięcia poza: `mechaniki-a-raport/raport.md` (3 miejsca: l. 3 ścieżka, l. 274 i 283) i
`przeglad-a-fable.md` (l. 172) – czyszczone przy przenoszeniu do `Serie/`; `pozew-revas-fable.md`, `swot-fable.md`,
`etap1/podobienstwa.md` – nie da się ich wyczyścić, bo są o tym (pytanie 2).

### Kontrola po wykonaniu
```
git -C gra grep -i -n -E "revas|levas|\[inna gra\]|\[poprzedni"        → 0
git -C notatki grep -i -n -E "revas|levas"                             → 0   [Z] razem z Analizy/
git -C notatki ls-files | grep -i -E "revas|levas"                     → 0
grep -r -i -l -E "revas|levas" warsztat CLAUDE.md .claude              → 0
```

## (e) Ryzyka

| # | Ryzyko | Skutek | Zabezpieczenie |
|---|---|---|---|
| 1 | Spłaszczenie repo gry (20 punktów w (a)) | czerwony test, generator i skrypt OSM piszą w złe miejsce, 60 MB exe w gicie | osobny krok, osobna gałąź `porzadki`, pełny pytest + ruff + `silnik.dane sprawdz` + `start.bat` przed scaleniem |
| 2 | Majster pracuje na `maciex` w starym układzie | konflikty przy jego następnym scaleniu, zepsute `.venv` | spłaszczyć tuż po scaleniu aktualnego `maciex`; wpis w WSPOLPRACA i wiadomość przed pushem |
| 3 | Odsyłacze Obsidiana do usuwanych notatek: `[[PLAN_PRZEBUDOWY]]` (7), `[[Mapa – elementy]]` (2), `[[Plan na 14.11]]` (1), `[[Wnioski Fable 14.11]]` (1), `[[LUKRUM]]` (1) | martwe linki w sejfie | wszystkie są w plikach przepisywanych albo usuwanych; jedyny poza nimi to `Funkcje/Logo i zastrzeżenie marek.md` (w tabeli (b)). Kontrola skryptem z kroku 9 |
| 4 | Zmiany nazw plików w sejfie robione poza Obsidianem | Obsidian nie poprawi linków sam | linki są już poprawione w szkicach; po wykonaniu szef otwiera sejf i sprawdza „Niepołączone odnośniki” |
| 5 | `.obsidian/workspace.json` majstra i szefa wskazuje otwarte stare pliki | pusta karta po starcie | nieszkodliwe (plik jest ignorowany przez git) |
| 6 | Majster albo jego agenci mają w instrukcjach nazwy `WSPOLPRACA.md`, `PLAN_PRZEBUDOWY.md`, `Mapa – elementy.md` | jego agent nie znajdzie pliku | `WSPOLPRACA.md` zachowuje nazwę; o dwóch pozostałych wpis w Dzienniku WSPOLPRACA |
| 7 | Usunięcie `notatki/_robocze/` zanim raporty trafią do `Serie/` | utrata jedynych kopii (`fable-raporty/` są **tylko** w `lukrum/_robocze/`) | kolejność: najpierw krok 5 (przenoszenie), kontrola, dopiero potem usuwanie (krok 8) |
| 8 | Odwołania z kodu do przenoszonych dokumentów | – | sprawdzone grepem: kod czyta z dysku tylko `INSTRUKCJA.md`/`.pdf` (zostają przy `manage.py`) i `narzedzia/grafiki/zestaw.py` (test). `dokumentacja/OPIS_GRY.md` w 3 komentarzach – plik zostaje. Do `fable_noc/`, `raporty/`, `POSTEP.md`, `gity.txt` kod i testy się nie odwołują (poza `dekor.yaml`, #20) |
| 9 | `raporty/` znika z repo gry, a `AGENTS.md` §9 i definicje agentów każą tam pisać raporty | agent założy folder od nowa | nowy `AGENTS.md`, `ZESPOL.md` i szablon briefu wskazują folder serii w notatkach |
| 10 | Agenci piszą teraz do repo notatek wspólnego z majstrem | więcej commitów w jego sejfie | raporty tylko w `Serie/<seria>/`, commituje lider, po serii |
| 11 | Pamięć Claude Code zostaje przy starej ścieżce | lider traci zasady (commity bez dopisków, model agentów) | krok 1; najważniejsze zasady i tak są w `CLAUDE.md`/warsztacie |
| 12 | Inny agent pracuje w `_robocze/krytyka` na starym układzie | jego wyniki mają ścieżki `lukrum_gra/gra/…` | odebrać wyniki przed krokiem 3; w raporcie krytyki podmienić ścieżki przy przenoszeniu |
| 13 | Dwie zmiany niezacommitowane (`AGENTS.md`, `dokumentacja/zespol/`, `notatki/Zespół/`) czekają na przegląd szefa | porządki mogą je nadpisać | krok 2 zaczyna się dopiero po uwagach szefa do plików zespołu; `Zespół/` przenoszony bez zmian treści |
| 14 | Przepisane notatki funkcji (5) zmieniają teksty, z których powstanie instrukcja | zgubiona liczba | szkice zachowują każdą liczbę i każdy przepis ze starych wersji; recenzent porównuje stare i nowe (krok 9) |
| 15 | W szkicach są fakty wpisane z notatek, a nie z gry (kwoty wyposażenia sprzed przeliczenia 15.11, kolumna „Stan” nawiązań, spis mapy z 14.11) | notatka rozminie się z danymi | oznaczone w szkicach zdaniem „sprawdzić w danych”; nie blokuje porządków |

## (f) Kolejność wykonania (po przeniesieniu folderu przez szefa)

Seria `porzadki`. Agenci nie commitują: commit po każdym kroku robi lider na gałęzi `porzadki` (zob. „Plan B”). Najwyżej 3 piszących naraz, pliki
rozłączne. Każdy brief wskazuje ten plan, właściwe wiersze tabeli (b) i szkice.

**Przed startem (szef i lider)**
- odpowiedzi szefa na pytania z (g), przynajmniej 1–4;
- uwagi szefa do plików zespołu (AGENTS, LIDER, definicje agentów), bo krok 2 je dzieli;
- odebrane wyniki agenta krytyki (`_robocze/krytyka-wyniki/`), zatrzymane serwery gry;
- aktualny `maciex` scalony do `main`, majster uprzedzony o spłaszczeniu (ryzyko 2).

| Krok | Kto | Co | Pliki (zakres wyłączny) | Dowód |
|---|---|---|---|---|
| 1 | lider sam | Założyć `_robocze/porzadki/STAN.md`. `lukrum_gra/` → `gra/`; `git pull` w obu repo; gałąź `porzadki` w repo gry i w repo notatek; `_archiwum/` → `archiwum/` + `LEGENDA.md`. **[Z]** Pamięć i kopia `krytyka` – już zrobione. | nazwy folderów, nic w treści | `git -C gra status -sb`, `git -C gra worktree list` |
| 2 | **W** (Sonnet) | `git init` w `warsztat/` (gałąź `main`), potem ze szkiców `warsztat-01…08`: README, `.gitignore`, szablony, `zainstaluj.ps1`, `panel/README.md`; przenieść `_robocze/narzedzia/{cdp,zrzuty}.py`; napisać `nowa_kopia.sh` (z `LIDER.md` §4); `ZESPOL.md` i `LIDER.md` według podziału `warsztat-02` (bez słowa LUKRUM); definicje agentów do `warsztat/agents/` w wersji ogólnej; uruchomić instalator; `CLAUDE.md` ze szkicu | `warsztat/**`, `CLAUDE.md`, `.claude/agents/**`, `_robocze/narzedzia/` | `grep -ri -E "lukrum|kebab|lublin" warsztat` → 0; lista `.claude/agents/`; zrzut próbny `cdp.py`; `git -C warsztat status` czysty po commicie lidera |
| 3 | **N1** (Sonnet) | **[Z]** Założyć `notatki/Analizy/` (+ `Analizy.md`) i `archiwum/` według (a) i (b), oraz `notatki/Serie/`: przenieść raporty i tabele pomiarów według (b) z `gra/raporty/`, `gra/fable_noc/` (tylko kopiuje, nie usuwa w repo gry) i z `_robocze/`; wkleić `Serie.md` i `fable – raport.md` ze szkiców; nazwy `<seria> – <temat>.md`; poprawić ścieżki i 4 miejsca ze starą nazwą; przegląd prawny z poprawkami z (b) | `notatki/Serie/**`, `notatki/Analizy/**`, `archiwum/**` (tylko kopiuje z `_robocze/`, nie usuwa) | `grep -ri -E "revas\|levas\|\[inna gra" notatki/Serie analizy` → 0 ; lista plików = (a) |
| 4 | **G** (Sonnet), po kroku 3 | Repo gry, gałąź `porzadki`: `git mv gra/* .` i pliki lokalne ręcznie; 15 poprawek z tabeli spłaszczenia (#1–#15, #20); `git rm` `fable_noc/`, `raporty/`, `gity.txt`, `dokumentacja/POSTEP.md`; `dekor_pomiar.py` → `balans/`; README, `.gitignore`, `AGENTS.md` ze szkiców `gra-01…03` (treść rozdziałów z obecnego AGENTS); poprawki w STACK, OPIS_GRY, SCENARIUSZE; wyczyścić `.git/info/exclude`; nowe `.venv`; przegenerować grafiki i PDF instrukcji | całe `gra/` | `pytest … \| tail -5` (740 passed), `ruff check .`, `silnik.dane sprawdz`, `python narzedzia/grafiki/zestaw.py --sprawdz`, `git status --short` bez `db.sqlite3`/`cloudflared.exe`, `git grep -n -E "(^\|[^a-z_/])gra/(silnik\|dane\|panel\|testy)"` → 0 |
| 4d | **G** (ten sam agent co krok 4), po 4c **[Z]** | Kody dawnych serii i martwe odsyłacze (Z4): najpierw `zwiadowca` (Haiku) robi listę `plik:linia → kod/odsyłacz` do `_robocze/porzadki/kody.md`; G pisze `archiwum/kody-serii.md` (kod → co znaczył), potem przepisuje `zrodlo` w `dane/*.yaml` na realia i usuwa kody z komentarzy kodu; ponowny pomiar zwrotu z wystroju (Z5) → `dekor.yaml: zrodlo` z datą. **Nie rusza `testy/dane_zamrozone/`** (pytanie 10) | `gra/dane/**`, komentarze w `gra/**/*.py`, `*.js` | `git grep -c -E "<wzorzec kodów z listy>"` → 0 poza zamrożonymi; `silnik.dane sprawdz`; pełny pytest |
| 4e | **R** (recenzent), po 4d **[Z]** | Próbka 30 zmienionych `zrodlo`: czy realia są prawdziwe i czy nie zgubiono liczby | nic nie zmienia; `notatki/Serie/porzadki/porzadki – zrodla.md` | lista braków |
| 5 | **N2** (Sonnet), równolegle z 4 i 6 | Notatki główne: wkleić szkice `notatki-01…09` i `-15` (`README`, `Plan`, `Decyzje`, `Do decyzji`, `Wygląd`, `Mapa`, `Nawiązania literackie`, `Historia`, `WSPOLPRACA`, `Postęp`); `git rm` `LUKRUM.md`, `PLAN_PRZEBUDOWY.md`, `Wnioski Fable 14.11.md`, `Plan na 14.11.md`, `Mapa – elementy.md` | pliki `.md` w korzeniu `notatki/` | skrypt linków z kroku 9 dla korzenia; `grep -i -E "revas\|levas"` → 0 |
| 6 | **N3** (Sonnet), równolegle z 4 i 5 | `notatki/Funkcje/`: wkleić 5 szkiców `notatki-10…14` i szablon `warsztat-06`; poprawki `Stan`/`Gdzie w grze` w 10 notatkach według (b); 8 zaczepek WOS do `Dymki przy ladzie.md` (z `git show HEAD:"Do decyzji.md"`); 2 odsyłacze w `Logo i zastrzeżenie marek.md`; sprawdzić w danych gry kwoty oznaczone „sprawdzić w danych” | `notatki/Funkcje/**` | `grep -l "czeka na zatwierdzenie\|mechaniki-a\|fable-" Funkcje/*` → 0; `grep -c "## Zmiany" Funkcje/*` → same zera |
| 7 | lider sam | Pliki zespołu w notatkach: `Zespół/Dziennik lidera.md` (ścieżka startu, role majster i kapitan, odhaczone pytanie o gałąź `fable`), `Sprawozdanie` (ścieżki); wpis w Dzienniku WSPOLPRACA o spłaszczeniu i nowych nazwach notatek | `notatki/Zespół/**` | – |
| 8 | lider sam, **po** kontroli kroków 3–6 | Usunięcia: `git rm -r notatki/_robocze`; z `lukrum/_robocze/` usunąć to, co krok 3 skopiował do `notatki/Analizy/`, `Serie/` i `archiwum/` (porównanie list), i śmieci; `plan.md` → `notatki/Serie/porzadki/porzadki – plan.md`, `szkice/` → `archiwum/porzadki-szkice/` | to, co w (b) ma „usuń” | `git -C notatki ls-files \| wc -l` (ok. 75); `ls _robocze` puste poza bieżącymi |
| 9 | **R** (recenzent, Sonnet, tylko odczyt) | Kontrola: 4 polecenia z (d) → 0; martwe odsyłacze Obsidiana (każdy `[[X]]` ma plik `X.md` w sejfie); martwe ścieżki w `gra/*.md` i `gra/dokumentacja/`; porównanie 5 notatek funkcji „przed/po” pod kątem zgubionych liczb; tabela (c): każda pozycja obecna w pliku docelowym; `git -C gra ls-files` bez png poza `static/` | nic nie zmienia; raport `notatki/Serie/porzadki/porzadki – recenzja.md` | lista braków albo „0 braków” |
| 10 | lider | Poprawki po recenzji (do tych samych agentów); commity (repo gry: jeden „Porządki: spłaszczenie repo…”, notatki: 2–3 tematyczne, warsztat: pierwszy commit), bez dopisków; założenie prywatnego repo warsztatu na GitHubie tylko za zgodą szefa; **akceptacja szefa**; push; usunięcie zdalnej gałęzi `fable` w notatkach; wiadomość do majstra; wpis w `Historia.md` i `Serie.md` | – | `git log --oneline -3` obu repo, pytest z `main` |
| 11 | **W2** (Sonnet: research w sieci) + lider **[Z]** | `METODA.md` w repo gry („Jak powstał LUKRUM”, jawność AI): W2 sprawdza regulamin ZwzT pod kątem AI (cytaty ze źródłem) → `notatki/Analizy/Regulamin ZwzT a AI.md`; lider pisze szkic `METODA.md`, szef akceptuje | `gra/METODA.md`, `notatki/Analizy/` | link w README gry |
| 12 | lider + W (Sonnet) **[Z]** | Panel kontrolny na claude.ai (Z7): osobna seria po kroku 2, plan do akceptacji szefa | – | – |

### Plan B na wyczerpanie limitu (przerwanie w dowolnej chwili)
- **Plik stanu:** `_robocze/porzadki/STAN.md`, jedna linia na krok: `krok | agent | start | koniec | wynik dowodu | commit`.
  Lider dopisuje linię przy starcie kroku i uzupełnia ją po kontroli. Nowa sesja zaczyna od przeczytania `STAN.md`
  i tego planu, niczego nie zgaduje z rozmowy.
- **Każdy krok kończy się commitem** na gałęzi `porzadki` (repo gry i notatek; `warsztat` na `main`), z opisem
  „Porządki, krok N: …”. Commit robi lider zaraz po dowodzie, bez czekania na koniec serii. Do `main` nic nie
  trafia przed krokiem 10, więc przerwana seria nie psuje pracy majstra. (To zmienia regułę „commity dopiero
  w kroku 10”: krok 10 tylko scala gałęzie i wypycha.)
- **Krok 1** nie ma commita: jego stan widać po nazwach folderów; w `STAN.md` zapisać, które podpunkty zrobiono.
- **Krok 4 jest najdłuższy, więc ma trzy commity pośrednie:** 4a same przeniesienia (`git mv`, nic więcej),
  4b poprawki ścieżek + zielone testy, 4c dokumenty i usunięcia. Po przerwaniu `git log --oneline porzadki` mówi,
  gdzie skończono; niezacommitowane resztki ocenia się przez `git status` i albo kończy, albo `git stash`.
- **Agent przerwany w połowie:** nie wznawiać „z pamięci”. Nowy agent dostaje ten sam brief z dopiskiem „zrobione
  są: <lista z `git status`/`git diff --stat`>; dokończ resztę”.
- **Krok 8 (usunięcia poza gitem) jest nieodwracalny**, więc robi się go jednym ciągiem i dopiero wtedy, gdy kroki
  3–6 mają commity, a `STAN.md` ma ich dowody. Przerwany w połowie: powtórzyć listę z (b), usuwanie jest idempotentne.
- `STAN.md` po kroku 10 idzie razem z planem do `notatki/Serie/porzadki/`.

Skrypt kontroli odsyłaczy (krok 5 i 9), z korzenia `notatki/`:
```
grep -rhoE '\[\[[^]|#]+' --include=*.md . | sed 's/\[\[//' | sort -u | while read n; do
  find . -name "$n.md" -not -path './.git/*' | grep -q . || echo "BRAK: $n"; done
```

Szacunek: kroki 2–3 równolegle ok. 1 h, kroki 4–6 równolegle ok. 1,5 h (najdłuższy krok 4 przez pełne testy),
kontrola i poprawki ok. 1 h.

## (g) Pytania do szefa (z rekomendacją)

Pierwsza czwórka blokuje start, druga może poczekać do kroku 8.

1. **Kiedy spłaszczyć repo gry względem pracy majstra?**
   (a) od razu po scaleniu jego aktualnego `maciex`, z uprzedzeniem – **rekomendacja**; (b) poczekać, aż skończy
   bieżący temat; (c) nie spłaszczać. Spłaszczenie to jeden commit z samymi przeniesieniami i 15 poprawkami ścieżek.
2. **Trzy dokumenty, których nie da się oczyścić ze starej nazwy** (`pozew-…-fable.md`, `swot-fable.md`,
   `etap1/podobienstwa.md`; wnioski są już w notatkach):
   (a) wynieść poza `lukrum/`, do archiwum starego projektu – **rekomendacja**, bo rozmowa z prawnikiem jest wciąż
   otwarta, a to jedyne pełne wersje; (b) usunąć; (c) zostawić `lukrum/_archiwum/` tylko na nie.
3. **Historia repo notatek** ma starą nazwę w 6 z 28 commitów (i nazwę pliku w `_robocze/`). Repo gry ma historię czystą.
   (a) zostawić historię, wyczyścić tylko stan bieżący – **rekomendacja, jeśli** notatki widzą tylko szef i majster;
   (b) nowa historia od jednego commita (force push, majster klonuje od nowa) – konieczne, jeśli dostęp dostanie
   kapitan, kuratorium albo ktokolwiek z zewnątrz. Wcześniejszy przegląd prawny ostrzegał, że kasowanie historii
   w razie sporu wygląda gorzej niż jej zostawienie.
4. **Raporty agentów w repo notatek** (wspólnym z majstrem), w `Serie/<seria>/`, z nazwami `<seria> – <temat>.md`:
   zgoda? **Rekomendacja: tak.** Skutek: w repo gry nie ma już `raporty/` ani listy zadań; majster widzi raporty.
5. **Osiem zrzutów z nocy 15/16.11** (1,6 MB): (a) do `notatki/Serie/fable/zrzuty/` jako ilustracja raportu –
   **rekomendacja**; (b) usunąć (zostają w historii repo gry).
6. **Podglądy wyglądu 1–3** (pliki HTML, ok. 285 kB) i zrzuty podglądu 4: (a) usunąć – **rekomendacja** (kopie
   zostają w historii repo notatek, podgląd 4 odtwarza generator); (b) zachować w `notatki/Wygląd/podglądy/`.
7. **Zwrot z wystroju: 9,8 czy 10,9 tygodnia?** Dane gry (`dekor.yaml`) mówią 9,8, tabela pomiaru 10,9.
   **Rekomendacja:** w kroku 4 uruchomić pomiar ponownie i wpisać do `zrodlo` wynik z datą.
8. **Kody dawnych serii i martwe odsyłacze w danych i komentarzach kodu** (ok. 420 kodów typu „U20”, „UF6”
   i ok. 25 odsyłaczy do dokumentów, których nie ma). Nie zawierają starej nazwy, ale pola `zrodlo` zobaczy każdy,
   kto otworzy dane. **Rekomendacja:** osobna seria `zrodla` po porządkach (zwiadowca robi listę, wykonawca
   przepisuje `zrodlo` na realia, recenzent sprawdza), bo to zmiana w plikach gry i w zamrożonych danych testów.

Drobne, rozstrzygnę zgodnie z rekomendacją, jeśli szef nie zaprotestuje: `WSPOLPRACA.md` zachowuje nazwę (zna ją
majster); `LOGOWANIE_MICROSOFT.md` idzie do `gra/dokumentacja/`; `Postęp.md` jest jedyną listą zadań, a README gry
ma tylko tabelę etapów; `.claude/agents/` jest kopią z instalatora.

## Uwagi do plików zespołu (dla lidera)
1. **`.git/info/exclude` w repo gry** ignoruje `PLAN.md`, `RAPORT.md`, `pomiary/`, `zrzuty/` bez względu na wielkość
   liter. `LIDER.md` §5.2 każe commitować `raporty/<seria>/plan.md`: dziś git by go nie zobaczył.
2. `AGENTS.md` §3.2 ma jedyny w repo gry ślad starej nazwy (ścieżka `Levas/levas_gra`). Nie commitować w tej postaci.
3. `AGENTS.md` §2 i `LIDER.md` §2 wymieniają model Fable; po 17.11 8:00 wiersz do usunięcia (historia jest w notatkach).
4. `AGENTS.md` §9 i format raportu wskazują `raporty/<seria>/` w repo gry; po zmianie: folder serii w notatkach.
   `LIDER.md` §5.2 „commit planu na gałęzi serii” nie pasuje do repo notatek (tam jest tylko `main`).
5. `AGENTS.md` §5: `../../_robocze/narzedzia/cdp.py` → `warsztat/narzedzia/cdp.py`; `cdp.py` ma na sztywno ścieżkę Chrome.
6. Definicje agentów powtarzają 9 zasad z `AGENTS.md` §3. Po podziale jedno źródło: `warsztat/ZESPOL.md`, a definicja
   ma tylko rolę, model i to, czym różni się od pozostałych.
7. `Sprawozdanie` i `LIDER.md` nie znają ról majster i kapitan. Proponuję: role zewnętrzne definiuje `CLAUDE.md`
   projektu, a warsztat zna tylko szefa, lidera i agentów.
8. Zasada „agent nie tworzy plików poza wskazanymi” potrzebuje pary po stronie lidera: krok „po serii `_robocze/<seria>*`
   usunięte” (jest w szablonie planu serii). Bez tego `_robocze/` znów urośnie.
9. `Dziennik lidera` trzyma decyzje szefa dzień po dniu, a `Decyzje.md` stan obowiązujący. Żeby nie powstały dwa
   źródła: dziennik jest zapisem, a po każdej serii lider przenosi do `Decyzje.md` to, co obowiązuje (wpisane w nagłówku szkicu).

## Odpowiedzi szefa na (g) 1–4 (16.11, wpisał lider)
1. Spłaszczenie: ściągnąć najnowszy `maciex`, robić po swojemu, wpis dla majstra w WSPOLPRACA.
2. Pozew, SWOT, podobieństwa: wynieść poza `lukrum/` (np. `Levas/_prawne/`).
3. Historia repo notatek zostaje (bez force push).
4. Raporty: `notatki/Serie/<seria>/`.
Pytania 5–8: rozstrzygnięte decyzjami 16.11 (noc), wpisał lider 17.11:
5. Zrzuty z nocy → `notatki/Analizy/Noc Fable 15-16.11/zrzuty/` (ilustracja raportu).
6. Podglądy wyglądu 1–4 i makiety → `archiwum/` (nie usuwamy).
7. Zwrot z wystroju: zmierzyć ponownie w porządkach (krok 4d), wynik z datą.
8. Kody serii i martwe odsyłacze: czyścimy **od razu** w porządkach (kroki 4d–4e), słownik kodów → `archiwum/`.

## (h) Nowe pytania do szefa (17.11) – odpowiedzi: **9a, 10a, 11b**
9. **Pozew symulowany i SWOT mają starą nazwę (38 i 22 razy).** Decyzja z nocy kładzie je w `notatki/Analizy/`, czyli w repo
   notatek wspólnym z majstrem, a to łamie kontrolę „0 trafień” z (d).
   (a) `archiwum/` (bez gita, tylko na dysku szefa), a w `notatki/Analizy/` krótkie streszczenie wniosków bez nazwy –
   **rekomendacja**; (b) `notatki/Analizy/` w całości, a kontrola (d) je pomija; (c) `notatki/Analizy/` z nazwą zastąpioną „[gra
   porównywana]”.
10. **Kody serii w `testy/dane_zamrozone/`** (3 pliki: `dostawcy.yaml`, `kalendarz.yaml`, `kandydaci.yaml`). Agenci
    nie mogą zmieniać zamrożonych danych.
    (a) zostawić, bo to migawka do testów i nikt jej nie widzi – **rekomendacja**; (b) wyczyścić i przeliczyć
    oczekiwane wyniki testów (ryzyko ukrycia błędu wzoru).
11. **Korzeń repo notatek w `lukrum/`** (wybór poprzedniego lidera, do potwierdzenia). Skutek: majster ma po `git pull`
    sejf o piętro niżej (`notatki/`), a odsyłacze `[[…]]` z notatek do `notatki/Analizy/` nie działają, gdy sejfem jest `notatki/`.
    (a) korzeń `lukrum/`, sejf szefa = `lukrum/` z wykluczeniem `gra/`, `archiwum/`, `_robocze/`, sejf majstra =
    `notatki/`; (b) **`notatki/Analizy/` jako podfolder `notatki/Analizy/`**, repo zostaje tam, gdzie jest: zero przenoszenia
    `.git`, majster nic nie robi, odsyłacze działają – **rekomendacja**; (c) jak (a), ale bez odsyłaczy `[[…]]` do analiz.

## (i) Krok 13 – odchudzenie `notatki/` (polecenie szefa 17.11, po scaleniu porządków)
Cel: mniej plików. Zostają tylko aktualne, informacje się nie powtarzają, wszystko stare i nieaktualne → `archiwum/`.
1. **Zwiadowca (Haiku, tylko odczyt):** czyta wszystkie pliki w `notatki/` (nie `.git`, nie `.obsidian`) i zapisuje mapę do
   `_robocze/porzadki/mapa-notatek.md`: plik | o czym (1 zdanie) | aktualny? | powtarza informacje z … | propozycja (zostaje / scal z … / do archiwum).
2. **Lider:** przegląda mapę, pokazuje szefowi listę zmian (najpierw mapa, potem wykonanie), wykonuje przez wykonawcę (Sonnet):
   scalenia, przeniesienia do `archiwum/notatki-wycofane/` (poza gitem), poprawa odsyłaczy `[[…]]`.
3. **Kontrola:** skrypt odsyłaczy z (f), każda decyzja szefa nadal w `Decyzje.md`, `git -C notatki ls-files | wc -l` mniej niż 77.
