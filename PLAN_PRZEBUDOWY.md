# LUKRUM – plan przebudowy Levasa

Uzgodniony z autorem 13.11.2026. Plik żyje: po każdej rewizji dopisujemy decyzje i odhaczamy etapy.

## 1. Cel

LUKRUM to symulacja biznesowa dla liceów: program i plan zajęć, dzięki którym nauczyciel WOS poprowadzi kilka lekcji
prowadzenia firmy. Projekt idzie na konkurs „Zwolnieni z Teorii” i przez Urząd Miasta Lublin oraz kuratorium (tym zajmuje się autor).

Wymagania:
1. **Zero śladów Revasa**, czyli brak podobieństw interfejsu, nazw, wzmianek, artefaktów w kodzie i historii gita.
2. **Nowa nazwa: LUKRUM.** Od łac. *lucrum*, czyli zysk, a „Lu” to ukryty Lublin. Na lekcję WOS jest bonus:
   *lucrum cessans* (utracone korzyści, art. 361 § 2 k.c.).
3. **Gra na mapie Lublina** z płynnym przybliżaniem: miasto, potem dzielnica, potem budynek i jego wnętrze. Strefy
   na mapie zastępują dzisiejsze zakładki i menu z boku.
4. **Nawiązania literackie** rozsiane po grze.

## 2. Decyzje autora (13.11.2026)

| Sprawa | Decyzja |
|---|---|
| Model pracy | Opus planuje i sprawdza, agenci Sonnet wykonują, Fable ewentualnie robi niezależny audyt końcowy |
| Mapa | Własna, rysowana (SVG) na prawdziwych granicach dzielnic z OpenStreetMap |
| Poziomy | Płynny zoom (kółko myszy i szczypanie palcami) |
| Wnętrza | Zoom wchodzi do środka budynku. Przekrój lokalu z klikalnymi miejscami (lada, kuchnia…) |
| Nawigacja | Mapa i mały pasek skrótów. Bez menu z boku i bez zakładek |
| Urządzenia | Komputery **i** telefony |
| Tryb lekcyjny | To już robi zakrywanie funkcji. Na razie zostaje ręczne odsłanianie, **presety później** |
| Branże | Na start tylko kebab, ale branża (menu, składniki, sprzęt, klienci) siedzi w danych, żeby dało się dodać następną |
| Lekcje | Jeszcze nieustalone: trochę rund na żywo, trochę między lekcjami |
| Marki | **Prawdziwe nazwy firm zostają** i dochodzi zastrzeżenie (rozdz. 7). Bez prawdziwych logo, tylko nasze ikony |
| Kasyno | Zostaje ukryte. Nowa nazwa **„Pod Złotym Koziołkiem”**, a hasło „koziol” **zawsze** otwiera klub (bez progu rundy) |
| Podobieństwa mechanik | Agent je wypisuje, **decyduje autor** (zmiana wzorów rusza balans) |
| Dokumentacja | Piszemy od nowa i zwięźle. Historia Levasa zostaje w Levasie |
| Repo | github.com/Tom-Wasko/Lukrum, **prywatne** (przestawione 13.11), nowe, bez historii Levasa |
| Commity | Tylko autor Tom-Wasko, bez dopisków o Claude. **Rzadziej niż w Levasie** (rozdz. 9) |
| Folder | `lukrum/` samodzielny jak `Levas/`: repo, nowe notatki, robocze, archiwum |
| README | Zawsze aktualny na GitHubie (rozdz. 9) |
| Terminy | Etapami, z regularnymi rewizjami. Najpierw czysta gra, potem prototyp mapy. Do 16.11 prototyp |

## 3. Folder

```
lukrum/                     folder główny, poza gitem
  PLAN_PRZEBUDOWY.md        ten plik
  lukrum_gra/               repo Tom-Wasko/Lukrum (gałąź main)
    README.md               zawsze aktualny: co to jest, jak uruchomić, stan
    AGENTS.md               przewodnik dla agenta (nowy, zwięzły)
    gra/                    kod gry (silnik, api, panele, dane, testy)
    dokumentacja/           POSTEP.md (od zera), STACK.md, OPIS_GRY.md (mechaniki LUKRUM, bez Revasa)
    raporty/<etap>/         plan.md etapu, raporty agentów, pomiary
  notatki/                  nowe notatki projektowe (Obsidian), zaczynamy od czystej kartki
  _robocze/                 kopie agentów (worktree), BRIEF_AGENTA.md, narzędzia (cdp.py, nowa_kopia.sh)
  _archiwum/                zakończone etapy, tylko do odczytu
```

Sesje Claude odpala się z `lukrum/`. Ten folder dostanie własną pamięć (założę ją z zasadami: commity, agenci, strategia).
W całym `lukrum/` nie ma niczego z `Levas/_archiwum/revas_26` ani z notatki „Różnice Revas – Levas”.

## 4. Etapy

### Etap 0: plan (13.11)
- [x] nazwa LUKRUM, folder `lukrum/`, repo prywatne
- [x] spisanie planu (ten plik)
- [ ] akceptacja planu przez autora

### Etap 1: czysta gra pod nową nazwą (noc 13/14.11, rewizja 14.11)
Gra działa tak jak dzisiejszy Levas, ale jest już LUKRUM-em i nie ma w niej Revasa.

1. **Przenoszenie po białej liście** (rozdz. 5). Do `lukrum_gra/` trafia tylko plik, który przeszedł filtr. Każde
   przeniesienie ma wpis w `raporty/etap1/przeniesione.md` (plik → co zmieniono).
2. **Zmiana nazw.** Levas → LUKRUM w tekstach, kodzie i nazwach, pakiet Django `gra/levas/` → `gra/lukrum/`. Szablony,
   tytuły stron, PDF instrukcji, ciasteczka i klucze `localStorage` dostają nowe przedrostki.
3. **Revas do zera.** Usuwamy wszystkie wzmianki (dziś ok. 106 w ok. 40 plikach: silnik, dane, testy, zamrożone dane, panel)
   i pola `zrodlo` w yaml, które powołują się na Revasa (przepisane na własne uzasadnienie albo „założenie”).
4. **Lista podobieństw** (`lukrum/_robocze/etap1/podobienstwa.md` – poza repo, bo z natury wymienia Revasa). Agent porównuje grę z `_archiwum/revas_26`, czyli remakiem
   autora (to nie oryginał, porównanie jest przybliżone), oraz ze starymi `WIEDZA_O_GRZE.md` i `ROZNICE_LEVAS_STARY.md`.
   Wypisuje mechaniki, wzory, liczby, nazwy pojęć (np. „karta wyników”) i układ ekranów, które mogą przypominać Revasa.
   Przy każdej pozycji daje ocenę ryzyka i propozycję zmiany. **Niczego nie kopiuje i niczego nie zmienia**, decyduje autor.
   Lista jest gotowa (13.11, ok. 50 pozycji). Etap 1 czyści już teksty, źródła i nazwy własne (banki, biura, media
   z katalogu dostają wymyślone nazwy). Wzory i liczby czekają na decyzję autora (`notatki/Do decyzji.md`).
5. **Stary wygląd** (`?motyw=stary`: górne menu i tabele) **nie przechodzi** (decyzja 13.11). Obecny wygląd zostaje
   bez zmian – w etapie 1 gra ma tylko działać.
6. **Marki:** zastrzeżenie na ekranie „O grze”, w instrukcji i w README. Usuwamy uproszczone prawdziwe logo
   (`ikony_marek.js`) i zastępujemy je naszymi ikonami.
7. **Kasyno:** „Pod Złotym Koziołkiem”, hasło „koziol” działa od 1. rundy.
8. **Nowa dokumentacja:** README, AGENTS.md, OPIS_GRY.md, STACK.md, POSTEP.md (od zera), INSTRUKCJA.md + PDF.
9. **Kontrola:** pytest (ok. 440 testów), ruff, `silnik.dane sprawdz`, gra botów, uruchomienie panelu i 2 zrzuty.
   Na koniec grep po całym repo: `revas|levas|fitness|klub fitness|siłownia` i nazwy z listy podobieństw = 0 trafień.
10. Pierwszy commit i push do prywatnego repo.

### Etap 1½: planowanie wyglądu (rozmowa z autorem, po rewizji etapu 1)
Seria pytań i próbek (artefakty, zrzuty): styl mapy, kolory, kroje, ikony, wnętrze kebaba, pasek skrótów, telefon.
Wynik: [[Wygląd]] w tym repozytorium notatek. To podstawa etapu 2. Do tego czasu wygląd się nie zmienia.

### Etap 2: prototyp mapy (od 14.11, prototyp na 16.11)
Od 13.11 mapą (pkt 1, 2 i 4) zajmuje się kolega autora. Wnętrza (pkt 3) i mechaniki robimy my. Szczegóły są w [[WSPOLPRACA]].

1. **Dane mapy:** skrypt pobiera granice dzielnic Lublina, parki, rzeki (Bystrzyca, Czechówka) i główne drogi
   z OpenStreetMap (Overpass). Potem upraszcza je do SVG (`dane/mapa/lublin.svg` + `dzielnice.yaml`). Licencja ODbL
   wymaga podpisu „© autorzy OpenStreetMap” w rogu mapy i w README.
2. **Silnik mapy w panelu:** jeden moduł (`mapa/`) z płynnym zoomem i przesuwaniem (mysz, kółko, szczypanie, przeciąganie).
   Poziomy szczegółów zależne od skali: dzielnice → strefy i lokale → budynek → wnętrze.
3. **Wnętrze własnego kebaba:** przekrój z klikalnymi miejscami, podpięty do obecnego silnika (rozdz. 6).
4. **Pasek skrótów:** kilka ikon (mój lokal, bank, hurtownie, raport rundy, wyślij decyzje). Na telefonie pasek na dole.
5. Strefy, które jeszcze nie mają wnętrza, otwierają na razie dotychczasowe okna. Gra jest grywalna na każdym kroku.
6. Rewizja z autorem: zrzuty komputer + telefon.

### Etap 3: wszystkie strefy na mapie (po 16.11)
- Wszystkie dzisiejsze zakładki dostają swoje miejsca (rozdz. 6) i wnętrza tam, gdzie to ma sens.
- Nawiązania literackie (rozdz. 8).
- Boty i konkurencja widoczne na mapie (ich lokale, warstwa popytu, billboardy).
- Pomiary: czy gra przez mapę nie jest wolniejsza (czas decyzji w rundzie).

### Etap 4: lekcje
- Scenariusze lekcji WOS dla nauczyciela (cele z podstawy programowej, przebieg, karty pracy, pytania do omówienia).
- Presety funkcji pod lekcje (autor: później).
- Gra testowa w klasie i poprawki po niej.

### Etap 5: audyt i publikacja
- Niezależny audyt Revasa (Fable albo świeży agent bez kontekstu): cały kod, dane, teksty, zrzuty ekranu.
- Sprawdzenie nazwy w UPRP, jeśli LUKRUM wychodzi poza szkoły.
- Ewentualne upublicznienie repo albo strony, tylko za zgodą autora.

## 5. Przenoszenie po białej liście (etap 1)

Plik trafia do `lukrum_gra/` dopiero wtedy, gdy:
1. jest na białej liście: silnik, api, panel_gracza, panel_mg, gry, konta, balans, testy, dane, manage.py, requirements,
   pyproject, start.bat;
2. grep nie znajduje w nim `revas`, `levas` ani nazw z listy podobieństw. Każde trafienie jest przepisane, a nie
   tylko usunięte, jeśli niesie sens;
3. komentarze powołujące się na serie Levasa (U20, B8, UF2…) zostają tylko tam, gdzie wyjaśniają „dlaczego”.
   Odnośniki do raportów, których w LUKRUM nie ma, usuwamy.

Nie przenosimy: `.git`, `db.sqlite3`, `lokalne.json`, `zapisy/`, `__pycache__`, `.venv`, `INSTRUKCJA.pdf` (generujemy
na nowo), `narzedzia/cloudflared.exe` (pobierany przy hostowaniu), `dokumentacja/`, `raporty/`, `zadania/`,
`plan.txt`, stary motyw (jeśli autor potwierdzi pkt 5 etapu 1).

## 6. Strefy na mapie

Prawdziwe miejsca Lublina. Autor uznał, że w centrum jest za dużo, więc urzędy i biura są rozrzucone po mieście.
Dokładne adresy sprawdzimy na OSM w etapie 2.

| Miejsce | Dzielnica | Co tam się robi (dzisiejsze zakładki) |
|---|---|---|
| **Twój kebab, wnętrze** | tam, gdzie lokal | Lada: menu, ceny, promocje · Kuchnia: magazyn, świeżość, obciążenie · Sala: wyposażenie · Zaplecze: pracownicy, szkolenia, grafik, czas właściciela · Biuro: finanse, KPiR, VAT, właściciel |
| **Krakowskie Przedmieście** | Śródmieście | banki, dom maklerski (giełda) |
| **Urzędy** (ul. Szeligowskiego) | Czechów | urząd skarbowy (podatki), ZUS, urząd (sprawy lokalu) |
| **Sanepid** | do ustalenia na OSM | kontrole, higiena |
| **Biurowce przy Zana** | LSM / Rury | biuro rachunkowe, ubezpieczyciel |
| **Agencja reklamowa i radio** | do ustalenia | reklama, internet, ulotki |
| **Węglin, park handlowy** | Węglin Południowy | meble, sprzęt kuchenny, wyposażenie |
| **Mełgiewska / Tatary** | Tatary | hurtownie, dostawcy, przewozy |
| **Elizówka** | za granicą miasta (płn.) | rynek hurtowy: warzywa |
| **Dyskonty** | po osiedlach | zakupy z odbiorem osobistym |
| **Miasteczko akademickie** | Sławinek / Rury | tablica ogłoszeń = rynek pracy |
| **Stare Miasto** | Stare Miasto | Harpagon w bramie kamienicy, biuro nieruchomości (lokale, licytacje, przejęcia), ukryty klub „Pod Złotym Koziołkiem” |
| **Bazar** | okolice ul. Ruskiej | handel między drużynami |
| **Cała mapa** | – | kebaby konkurencji, warstwa popytu, billboardy przy drogach, zdarzenia miejskie |

## 7. Marki i zastrzeżenie

Darmowa gra edukacyjna raczej nie jest używaniem znaku „w obrocie gospodarczym” (art. 296 p.w.p.), więc ryzyko jest małe.
Gdyby LUKRUM było komercjalizowane, wracamy do tematu. Zasady:
- prawdziwe nazwy firm i miejsc zostają, **bez prawdziwych logo** (logo chroni prawo autorskie), tylko nasze ikony;
- bez ośmieszania i bez złych cech przypisanych prawdziwej firmie (oszust, lichwiarz, trucizna to zawsze postacie wymyślone, jak Harpagon);
- zastrzeżenie (ekran „O grze”, instrukcja, README):
  > LUKRUM to gra edukacyjna. Nazwy prawdziwych firm i miejsc służą tylko do oddania realiów Lublina. Oferty, ceny,
  > oprocentowania i zdarzenia w grze są fikcyjne. Gra nie jest związana z tymi firmami ani przez nie wspierana.

## 8. Nawiązania literackie

Zasada: najwyżej jedno na ekran, subtelnie, bez cytowania długich fragmentów autorów chronionych (Lem, Herbert, Gombrowicz,
Zajdel: tylko aluzje i nazwy). Stereotypy są dopuszczalne (decyzja autora).

| Gdzie | Nawiązanie | Źródło |
|---|---|---|
| Zakładanie firmy | „Ja nie mam nic, ty nie masz nic, on nie ma nic. To razem właśnie mamy tyle, żeby założyć wielką fabrykę.” | Reymont, *Ziemia obiecana* |
| Rynek pracy | kandydat Ignacy Rzecki, sumienny subiekt | Prus, *Lalka* |
| Opinie klientów | zła recenzja = „przyprawiona gęba” | Gombrowicz, *Ferdydurke* |
| Sanepid | inspektor Pimko | Gombrowicz, *Ferdydurke* |
| Hurtownia | sepulki na półce („nie pytaj, do czego”) | Lem, *Dzienniki gwiazdowe* |
| Sklep ze sprzętem | „Konstruktorzy T&K” | Lem, *Cyberiada* (Trurl i Klapaucjusz) |
| Biura i banki | zob. rozdz. 11 (lektury) | – |
| Hasło przyprawy | „Kto kontroluje przyprawę, kontroluje rynek” | Herbert, *Diuna* |
| Zdarzenie miejskie | Carnaval Sztukmistrzów | Lublin + Singer, *Sztukmistrz z Lublina* |
| Pożyczki | Harpagon i Mistrz Jakub (już są) | Molier, *Skąpiec* |
| Kasyno | „Pod Złotym Koziołkiem” | herb Lublina, koziołek |
| Do dopisania | Zajdel (np. *Limes inferior*: punkty, klasy), Winnetou, inne lektury | – |
| Zadanie dla nauczyciela | „Znajdź 10 nawiązań literackich” | – |

## 9. Sposób pracy

**Rewizje i commity**
- Każdy etap ma `raporty/<etap>/plan.md` z checkboxami. Rewizja z autorem jest na końcu etapu albo po nocy pracy.
- Commity rzadziej niż w Levasie: **jeden commit na skończoną część etapu** (np. „Etap 1: zmiana nazw”), a nie na każdą poprawkę.
  Push na koniec sesji i zawsze przed rewizją.
- Autor commitów to tylko Tom-Wasko, bez linii o Claude (także w opisach PR).
- **README zawsze aktualny:** każdy commit, który zmienia to, co widzi gracz albo jak się uruchamia grę, poprawia README
  w tym samym commicie (co to jest, jak uruchomić, stan prac, licencja mapy, zastrzeżenie marek).

**Agenci, mądrzej niż w Levasie**
1. **Opus to dyrygent:** decyzje, briefy, przegląd zmian, teksty dla graczy i nawiązania literackie. **Sonnet** robi prace
   mechaniczne (przenoszenie plików, podmiany nazw, testy, moduł mapy według specyfikacji). **Fable** robi raz niezależny
   audyt na końcu (etap 5).
2. **Brief zamiast odkrywania:** agent dostaje gotową listę plików, zasady i kryterium „gotowe”. Nie czyta AGENTS.md w
   całości ani dużych plików, tylko grep i potrzebne fragmenty. Brief wzorcowy jest w `_robocze/BRIEF_AGENTA.md`.
3. **Wynik do pliku, nie do rozmowy:** agent zapisuje raport w `raporty/<etap>/` i zwraca 5–10 linijek streszczenia.
4. **Kontynuacja zamiast nowego agenta:** poprawki do pracy agenta wysyłamy temu samemu agentowi (SendMessage), bo zna
   już kontekst. Nowy agent to ponowne czytanie wszystkiego.
5. **Podział po plikach:** równolegle pracują tylko agenci z rozłącznymi plikami, każdy w swojej kopii `_robocze/<etap>-<temat>`
   (sparse-checkout `gra/`).
6. **Tanie sprawdzanie:** w trakcie testy tylko dotkniętych plików, pełny pytest raz na koniec. Zrzuty najwyżej 2 na
   zmianę wyglądu.
7. **Drobiazgi bez agentów:** jedna linijka albo tekst to robota dla Opusa, bo rozruch agenta kosztuje więcej.
8. **Szukanie:** szerokie przeszukiwanie robi agent Explore, który zwraca wniosek zamiast całych plików.

## 10. Do decyzji na rewizjach

- [x] Stary wygląd: nie przenosimy (13.11)
- [x] Obecny panel (z Levasa) to tylko rusztowanie do wymiany, nikomu go nie pokazujemy (13.11)
- [ ] Wygląd LUKRUM – etap 1½
- [x] Pozycje z listy podobieństw do Revasa – rozdz. 11 (13.11)
- [x] Sanepid, urzędy: prawdziwe adresy (sanepid ul. Prószyńskiego); agencje reklamowe po dzielnicach (13.11)
- [ ] Przebieg lekcji: na start ok. 4 tygodnie gry, „ale się tym nie sugeruj”; presety później
- [ ] Kolejne nawiązania literackie (Zajdel, Winnetou, lektury)
- [x] Kasyno: „koziol” otwiera każdemu (także MG), zakładka zostaje „Nocna 13”; w surowych danych easter egg
  „Rękopis znaleziony w JSON-ie” + hasło „saragossa” = odznaka Szperacz (13.11)
- [x] Nazwy w kodzie (usluga, zasob, prowadzacy) zostają (13.11)

## 11. Nowe mechaniki zamiast podobnych do Revasa (decyzje 13.11)

Autor nie wymyśla wzorów: koordynator proponuje, agent pomiarowy mierzy warianty botami na osobnej gałęzi, autor
zatwierdza raport. Tor A idzie w tle równolegle z etapami 1½ i 2, tor B po prototypie mapy.

**Tor A (niezależny od mapy, w tle)**
- **Wynik 0–1000 pkt:** pięć działów (finanse, goście, zespół, rozwój, bezpieczeństwo finansowe) po 0–200 pkt według
  jawnych progów. 1000 = bardzo dobra gra, ale wyjątkowi gracze mogą przekroczyć 200 w dziale (np. bardzo hojny
  socjal), więc wynik może być > 1000. Ranking = suma punktów z tygodni, ostatnie tygodnie warte więcej.
- **„Wielkie otwarcie”** w tygodniu 1 (wybór lokalu, menu, ekipa) z punktami bonusowymi za przygotowanie.
- **Debet z opłatą** włączany ręcznie (opłata za tydzień na minusie + odsetki); bez debetu brak gotówki = Harpagon.
  Automatyczny kredyt odnawialny znika.
- **Pomyłki w szczycie** zamiast reklamacji: rosną przy przeciążeniu kuchni, zmęczeniu i braku szkoleń; kosztują danie
  i gwiazdki.
- **Biuro rachunkowe: pakiety S/M/L** z limitem dokumentów i dopłatą (ceny z rynku Lublina 2026).
- **Kapitał startowy 50 000 zł.**
- **Banki ze specjalizacjami** (liczby mogą być arbitralne), każdy opłacalny dla innej strategii.
- **Kadry wg Kodeksu pracy:** pensje z ofert Lublina 2026, okres wypowiedzenia zamiast odprawy, umowa o pracę albo
  zlecenie z innymi składkami.
- **Nowe katalogi** (udogodnienia, wyposażenie, szkolenia, stanowiska, media) z pozycjami dla kebaba i cenami z rynku.
- **Stara reklama usunięta** (tradycyjna i internetowa), zostaje model z mapą „agencja × kanał”.
- **Pula godzin zostaje** z własnym uzasadnieniem (w małym kebabie wszyscy stoją przy jednym grillu).

**Tor B (po prototypie mapy)**
- **Opinie gości w gwiazdkach 1–5** (smak, czekanie, cena, czystość, obsługa), widoczne na mapie, z przykładowymi recenzjami.
- **Nastrój zespołu 0–100** dla każdego pracownika (płaca vs rynek, nadgodziny, szkolenia, socjal); przy niskim odchodzi.
- **Losowe wydarzenia dla każdej filii:** kontrola sanepidu, „Basia chce L4”, profesor Pimko „upupia” kucharza itd.
- **Popyt z mapy:** pule głodnych w strefach (studenci, biura, nocne życie) wybierają lokal po odległości, cenie,
  gwiazdkach i reklamie.
- **Fabuła z wujkiem-restauratorem** (bar mleczny „jeszcze za Gierka”): co tydzień list z radą, nawiązaniami i
  odblokowaniem kolejnej części gry. Zastępuje harmonogram rund; liczbę dań ogranicza sprzęt kuchni.

**Na koniec obu torów:** przepisać wszystkie opisy w grze pod nowe mechaniki (INSTRUKCJA + PDF, dymki „i”, „Jak grać”,
podpowiedzi, OPIS_GRY, README).

**Nazwy z nawiązaniami** („wszystko albo nic”: wszystkie banki i biura poza J.K.Ś. nawiązują do lektur, sensownie;
bez przedrostków „Bank …”/„Biuro …”). Kiedyś dopisać krótkie opisy z nawiązaniem do lektury.

| Nazwa | Specjalizacja | Dlaczego |
|---|---|---|
| Wokulski i S-ka | kredyt inwestycyjny | Prus, *Lalka*: kupiec, który rozkręca wielki interes |
| Oszczędności Rzeckiego | najlepsze lokaty | *Lalka*: Rzecki, sumienny subiekt, liczy każdy grosz |
| Soplicowo | tanie konto | *Pan Tadeusz*: gościnny dworek, gość nie płaci |
| Kmicic | szybki kredyt na start, drogi | Sienkiewicz, *Potop*: porywczy, działa od razu |
| Solaris | największy debet | Lem, *Solaris*: bezkresny ocean, nieprzewidywalny |
| Ziemia Obiecana | leasing sprzętu | Reymont: „ja nie mam nic…” – fabryka bez własnych pieniędzy |
| J.K.Ś. | biuro rachunkowe (życzenie autora) | – |
| Józef K. | biuro tanie, ale wszystko trwa | Kafka, *Proces*: biurokracja bez końca |
| Scrooge | biuro najtańsze, zamknięte w święta | Dickens, *Opowieść wigilijna* |
| Asteroida 328 | biuro dokładne i drogie | *Mały Książę*: Bankier liczący gwiazdy |
| Gazeta Pana Cogito, Radio Tichy | media | Herbert; Lem, *Dzienniki gwiazdowe* |

## 12. Współpraca (od 13.11.2026)

Do projektu dołącza kolega autora. Podział i zasady:
- **Mapa** (dane z OSM, silnik mapy, zoom, budynki-ikony, pasek skrótów) robi kolega ze swoimi agentami.
- **Mechaniki i wnętrza** (silnik gry, ekrany wewnątrz budynków, klienci przy ladzie) robi autor z Claude.
- Repozytorium gry to `Tom-Wasko/Lukrum`. Każdy pracuje na swojej gałęzi i wysyła zmiany do `main` przez pull
  request, który przegląda druga strona.
- Notatki to repozytorium `Tom-Wasko/Lukrum-notatki` (ten sejf Obsidiana). Agenci obu stron przed pracą robią
  `git pull` w obu repozytoriach.
- Wymiana informacji między agentami: [[WSPOLPRACA]].
