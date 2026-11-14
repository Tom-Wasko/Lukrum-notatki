# Zadanie: silnik wnętrza kebaba (dymki, bywalcy, propozycje) – gałąź `wnetrza-dane`

Najpierw przeczytaj wspólne zasady: `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\BRIEF_AGENTA.md`. Obowiązują z jedną zmianą:
**pracujesz w worktree `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\wnetrza-dane`** (kod w `gra/`, venv bierz z `lukrum_gra/gra/.venv`),
a commit robisz sam na końcu: autor Tom-Wasko (`git -c user.name=Tom-Wasko commit`), **bez Co-Authored-By i bez stopek
o Claude**, bez push.

## Po co
Wnętrze kebaba to lada z gośćmi. Bywalcy z lektur i anonimowi goście mówią w dymkach to, co policzył silnik w ostatniej
rundzie (cena, ocena, kolejka, brak dań, nastrój zespołu). Od czasu do czasu klient przychodzi z propozycją, a drużyna
wybiera odpowiedź ze skutkiem. Decyzje autora: `C:\Users\PC\Pulpit\Levas\lukrum\notatki\Wygląd.md`
(sekcje „Ustalone po podglądach 2” i „Dymki i bywalcy”).

## Dane (gotowe, czytaj, nie zmieniaj tekstów)
- `gra/dane/wnetrza/bywalcy.yaml`: 7 bywalców (pola opisane w nagłówku).
- `gra/dane/wnetrza/dymki.yaml`: `zasady`, `rodzaje`, `wskazniki`, `dymki` (cena_smak / plotki / wos) i `propozycje`
  z `propozycje_zasady` (format skutków opisany w komentarzu nad nimi).
Teksty pisze autor z Opusem, mogą się zmieniać równolegle. Ty nie ruszasz `tekst`, `wyjasnienie`, `reakcja`.
Jeśli format danych trzeba poprawić, opisz to w raporcie.

## Co zrobić
1. **Schematy (pydantic)**: nowy `gra/silnik/wnetrza/schematy.py` dla obu plików, z walidacją:
   - `kto` to id bywalca, „gosc” albo „kazdy”;
   - wskaźniki w `gdy` muszą być z listy `wskazniki`;
   - `zrodlo` plotek: park | kalendarz | konkurencja;
   - `okazja` wujka: start | pierwsza_strata | rekord | ostatnia_runda;
   - odpowiedzi propozycji mają unikalne id, a `bez_odpowiedzi` wskazuje istniejące id w każdej propozycji;
   - klucze `skutki` tylko ze słownika z komentarza.
   Podłącz ładowanie i walidację do `silnik/dane.py` (`python -m silnik.dane sprawdz`): brak folderu `wnetrza` = gra bez wnętrz.
2. **Wskaźniki**: `gra/silnik/wnetrza/stan.py`, z wyników zapisanych rundy firmy (szukaj w `model.py` / wynikach rundy,
   czym dziś liczą się ocena, kolejka, odejścia i nastrój):
   - liczy `cena_wzgledem_strefy`, `zmiana_ceny`, `ocena`, `kolejka`, `brak_dan`, `nastroj_zespolu`, `runda`;
   - zwraca też stan wnętrza do rysowania: pracownicy z miejscem (lada/kuchnia) i miną (z nastroju i zmęczenia,
     progi w yaml), kupione wyposażenie i udogodnienia (lista id), tłok (0–1);
   - wskaźnika, którego nie da się policzyć, nie ma w wyniku, a warunek na nim jest wtedy niespełniony.
3. **Wybór dymków**: `gra/silnik/wnetrza/dymki.py`. Funkcja czysta: (dane, wskaźniki, kontekst rundy, włączone rodzaje,
   historia bywalców) → lista dymków [{rodzaj, kto, imie, tekst, wyjasnienie?, zrodlo_prawne?}].
   - Deterministyczna: ziarno z `silnik/losowosc.py` (Strumien) z gry, firmy i rundy.
   - Liczba dymków, udział bywalców, przerwy między wizytami bywalca, limit WOS i `od_rundy` bywalców wg `zasady`.
   - Bywalcy częściej mówią na tematy ze swojego `dba_o`.
   - WOS: tylko `sprawdzone: true`. Dziś wszystkie mają false, więc w testach użyj danych testowych.
   - Plotki: wstawiają `{park}`/`{tytul}` z najbliższego zdarzenia parkowego (`dane/zdarzenia/parki.yaml`, tylko czytaj),
     `{wydarzenie}` z `dane/kalendarz/` i `{konkurent}`/`{dzielnica}` z konkurencji. Bez danych taki dymek odpada.
   - Wujek mówi tylko przy swojej okazji (start = runda 1, pierwsza_strata, rekord utargu, ostatnia runda) i nie
     podlega filtrom rodzajów.
4. **Propozycje**: w tym samym module albo `propozycje.py`:
   - wybór propozycji na rundę (najwyżej jedna co `co_ile_rund`, od `od_rundy`, każda najwyżej raz w grze, deterministycznie);
   - zapis odpowiedzi drużyny jako decyzji rundy, przez istniejący mechanizm decyzji, jeśli da się to zrobić bez ruszania
     plików z listy niżej; inaczej we własnym zapisie i z opisem w raporcie;
   - czysta funkcja `skutki_propozycji(dane, propozycja, odpowiedz, strumien) -> dict` (z rzutem `szansa`).
   **Nie podpinaj skutków do przeliczenia rundy** (runda.py jest zmieniany na innej gałęzi). W raporcie opisz dokładnie,
   gdzie i jak to podpiąć po scaleniu (porcje → sprzedaż i składniki, koszt, opinia, ryzyko_kontroli → sanepid, kandydat).
5. **Ustawienie MG**: cztery rodzaje dymków włączane i wyłączane przez mistrza gry, domyślnie wszystkie włączone.
   - Zapis w konfiguracji gry (zobacz, jak `silnik/funkcje.py` trzyma stany w konfiguracji) jako `wnetrza: {dymki: {rodzaj: bool}}`.
   - Mistrz gry może to zmieniać w trakcie gry, więc zmiana działa od następnego wyliczenia dymków.
   - Gracz ma dodatkowo własny filtr (tylko widok, parametr zapytania API).
   - Formularza MG nie rysuj, wystarczy endpoint.
6. **API**: nowy plik `gra/api/wnetrza.py` i linie w `api/urls.py`:
   - GET wnętrza firmy dla drużyny: stan, dymki rundy, propozycja (jeśli jest) i jej odpowiedzi;
   - POST odpowiedzi na propozycję;
   - GET/POST ustawień dymków dla MG.
   Uprawnienia zrób jak w istniejących widokach `api/` (drużyna widzi tylko swoją firmę, ustawienia tylko MG).
7. **Testy**: `gra/testy/wnetrza/`, obejmują:
   - walidację danych (także błędy);
   - determinizm wyboru;
   - warunki `gdy`, filtry rodzajów, `sprawdzone: false` (taki dymek nie wychodzi);
   - okazje wujka, przerwy bywalców;
   - propozycje (częstotliwość, raz w grze, `bez_odpowiedzi`, szansa);
   - API z uprawnieniami.

## Nie ruszaj (zmieniane na gałęzi `mechaniki-a`)
`AGENTS.md`, `dokumentacja/POSTEP.md`, `gra/api/prezentacja.py`, `gra/api/widoki.py`, `gra/balans/*`,
`gra/dane/{boty,kandydaci,katalog,zalozenia}.yaml`, `gra/dane/mapa/{banki,biura,budynki}.yaml`, `gra/dane/zdarzenia/parki.yaml`,
`gra/panel_gracza/static/zakladki/*`, `gra/panel_mg/*`, oraz w `gra/silnik/`: `autopilot.py`, `boty.py`, `decyzje.py`,
`gra.py`, `model.py`, `runda.py`, `schematy.py`, `ksiegowosc/*`, `ludzie/*`, `nieruchomosci/*`, `pieniadze/*`,
`rynek/konkurencja.py`, `wyniki/*`, oraz `testy/aplikacja/test_ikony_marek.py`.
Czytać je wolno. Jeśli bez zmiany któregoś się nie da, zrób najmniejszą możliwą zmianę i wypisz ją w raporcie (plik,
linie, po co), bo przy scalaniu będzie konflikt. `silnik/dane.py` i `api/urls.py` możesz zmieniać (małe dopiski).
Frontu nie rysujemy (to osobny etap z podglądem).

## Koniec
- Pełny pytest, ruff, `silnik.dane sprawdz`: wszystko zielone.
- Commit jak wyżej.
- Raport: `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\wnetrza-silnik-raport.md`. Zawiera:
  - pliki;
  - API z przykładami JSON;
  - jak podpiąć skutki propozycji po scaleniu toru A;
  - pytania do autora.
- Odpowiedź końcowa: 5–10 linijek.
