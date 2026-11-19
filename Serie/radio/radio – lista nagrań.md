# radio – lista nagrań

Stan: 19.11.2026. Lista zaakceptowana przez szefa (Decyzje.md, radio), pliki pobrane i w grze.
**Ostateczny spis z licencjami jest w `dane/radio.yaml`** (repo gry) i na stronie `/nagrania-w-radiu`.
Niżej jest lista kandydatów z dnia akceptacji. Zmiany względem niej opisuje ramka „Wynik”.

## Wynik (stan końcowy)
| Stacja | Nagrań | Minut | MB |
|---|---|---|---|
| Program Polski (66,9) | 17 | 52 | 17,9 |
| Synkopa – jazz (68,3) | 13 | 36 | 12,5 |
| Filharmonia – klasyczna (70,1) | 13 | 65 | 22,3 |
| Teatr przy mikrofonie – „Lalka”, rozdz. I–III (71,6) | 3 | 63 | 14,4 |
| Między stacjami – szum (73,4) | 0 (generowany) | – | 0 |
| **Razem** | **46** | **~3,6 h** | **~67 MB** |

Zmiany względem listy kandydatów:
- **Pozycje niepewne (sprawdził lider, decyzja szefa: „sprawdzę, odrzucę niepewne”):**
  - zostają jako utwory anonimowe (art. 36 pkt 2 pr. aut.): „Polak nie sługa”, „Modlitwa przed bitwą”,
    „Hej te góry”, „Idzie Maciek”;
  - zostaje „Marsz Sokołów”;
  - odpadają: „Krakowiak” (A.E. Brunner, nie udało się ustalić roku śmierci), „Hej mazury” (Schillo),
    „Oj ten mazur” (Zalewski), „Wlazł kotek” (opracowanie Świerzyńskiego, zm. 1957).
- **„Taniec polski” (Scharwenka) odpada**: plik w archiwum jest uszkodzony (3 s), a strona LoC blokuje pobieranie.
- **Klasyka z Internet Archive zamiast Wikimedia Commons** (Commons blokowało pobieranie, błąd 429). Te same nagrania
  Musopen:
  - Chopin z „musopen-chopin-complete-works-flac” (CC0);
  - Mozart, Bach, Beethoven i Brahms z „musopen-dvd-in-lossless-flac-format” (znak domeny publicznej 1.0);
  - zamiast uwertury „Egmont” (brak w zbiorze) gra III Symfonia „Eroica”, cz. III;
  - wykonawca Mazurka a-moll według IA to Luke Faulkner.

## Zasada prawna (krótko)
- **Nagranie**: prawa wykonawców i producentów fonogramów do nagrań sprzed 1963 r. w Polsce wygasły. W USA nagrania
  wydane do 1925 r. są w domenie publicznej. Bierzemy więc **nagrania do 1925 r.** albo nowe nagrania oddane do domeny
  publicznej (Musopen).
- **Utwór** (kompozytor, autor słów, aranżer): w Polsce chroniony 70 lat od śmierci autora. Bezpieczni są autorzy
  zmarli **najpóźniej w 1955 r.** (domena od 1.01.2026) oraz pieśni ludowe.
- Wykluczone mimo starego nagrania, bo autor żył po 1955 r.: Nick LaRocca (ODJB), W.C. Handy, Louis Armstrong,
  Ford Dabney („Castle walk”), Michał Świerzyński (opracowanie „Wlazł kotek”), bracia Spikes („Wolverine blues”).
- Źródła z jawnym znakiem domeny publicznej:
  - LoC National Jukebox na Internet Archive (`loc-jukebox-*`, Public Domain Mark 1.0);
  - Musopen na Wikimedia Commons (Public domain);
  - pojedyncze pliki IA z PD Mark.
- Great 78 (George Blood) i „USA-Archives” na IA nie mają wpisanej licencji. Nagrania są w domenie z mocy prawa
  (rok ≤1925), ale nie mają znaku. → **pytanie do szefa**.

## Rozmiar paczki
Plan: MP3 mono, 48 kb/s dla muzyki i 32 kb/s dla słowa, co daje około 0,36 MB i 0,24 MB na minutę.

| Stacja | Minut | MB |
|---|---|---|
| Polska sprzed 1956 | ~52 | ~19 |
| Jazz (do 1925) | ~33 | ~12 |
| Klasyczna (Musopen) | ~60 | ~22 |
| „Lalka” (3 rozdziały) | ~63 | ~15 |
| Szum (generowany w przeglądarce, bez pliku) | – | 0 |
| **Razem** | **~3,5 h** | **~68 MB** |

## 1. Polska sprzed 1956 (LoC National Jukebox, PD Mark)
Identyfikator to adres `https://archive.org/details/<id>`. Ocena: ✔ autorzy pewnie w domenie; ? autor lub aranżer
niesprawdzony (data śmierci nieznana).

| # | Tytuł | Wykonawca | Rok | Utwór (autor †) | Min | Ocena | id |
|---|---|---|---|---|---|---|---|
| 1 | Halka – pieśń | Marcella Sembrich | 1907 | Moniuszko †1872, Wolski †1882 | 4,2 | ✔ | loc-jukebox-125605-halka-polish-song |
| 2 | Hrabina – polonez | Henryk Adamus (fort.) | 1903 | Moniuszko †1872 | 3,4 | ✔ | loc-jukebox-1064141-hrabina-polonez |
| 3 | Jeszcze Polska nie zginęła | Chopin Conservatory Mixed Quartet | 1911 | Wybicki †1822, melodia lud. | 2,2 | ✔ | loc-jukebox-187338-jeszce-polska-nie-zgineta |
| 4 | Witaj majowa jutrzenko | jw. | 1911 | Suchodolski †1831 | 1,9 | ✔ | loc-jukebox-130649-witaj-majowa-jutrzenko |
| 5 | Idzie Maciek | Chopin Conservatory Quintette | 1911 | ludowa | 3,1 | ✔ | loc-jukebox-130641-idzie-maciek-idzie |
| 6 | Hej te góry | Chopin Conservatory Male Quartet | 1911 | ludowa | 2,3 | ✔ | loc-jukebox-130637-hej-te-g-ry |
| 7 | Mazur | Orkiestra Rybowiaka | 1911 | M.K. Ogiński †1833 | 2,9 | ✔ | loc-jukebox-224703-mazur |
| 8 | Wójt – mazur | B. Rybowiak | 1911 | L. Lewandowski †1896 | 2,3 | ✔ | loc-jukebox-224698-w-jt-mazur |
| 9 | Piękna nasza Polska cała | B. Rybowiak | 1911 | ludowa | 2,4 | ✔ | loc-jukebox-224694-pi-kna-nasza-polska-cala |
| 10 | Wiązanka melodyi ludowych | Orkiestra Rybowiaka | 1911 | ludowe | 3,2 | ✔ | loc-jukebox-224702-wi-zanka-melodyi-ludowych |
| 11 | Polak nie sługa | Chopin Conservatory Mixed Quartet | 1911 | pieśń XIX w. | 2,6 | ? | loc-jukebox-130650-polak-nie-s-uga |
| 12 | Modlitwa przed bitwą | jw. | 1911 | pieśń XIX w. | 2,8 | ? | loc-jukebox-130651-modlitwa-przed-bitwa |
| 13 | Krakowiak | Orkiestra Rybowiaka | 1911 | A.E. Brunner † ? | 3,3 | ? | loc-jukebox-130659-krakowiak |
| 14 | Marsz Sokołów | R. Kiolbassa-Kwasigroch | 1911 | S. Kuźniewicz † ? | 2,5 | ? | loc-jukebox-130660-marsz-soko-ow |
| 15 | Hej mazury | jw. | 1911 | W. Schillo † ? | 2,3 | ? | loc-jukebox-130662-hej-mazury |
| 16 | Oj ten mazur | Orkiestra Rybowiaka | 1911 | B.J. Zalewski † ? | 2,3 | ? | loc-jukebox-130666-oj-ten-mazur-czysta-bieda |
| 17 | Marsz żałobny | Royal Guards Band | 1909 | Chopin †1849 | 4,2 | ✔ | loc-jukebox-761759-chopin-s-funeral-march |
| 18 | Nokturn Es-dur | V. Sorlin (wiolonczela) | 1910 | Chopin †1849 | 4,0 | ✔ | loc-jukebox-129301-nocturne-in-e-flat |
| 19 | Fantazja-impromptu | X. Scharwenka (fort.) | 1910 | Chopin †1849 | 4,4 | ✔ | loc-jukebox-762513-fantasie-impromptu |
| 20 | Taniec polski | X. Scharwenka | 1910 | Scharwenka †1924 | 3,3 | ✔ | loc-jukebox-762507-polish-dance |
| 21 | Menuet G-dur | Victor Orchestra | 1910 | Paderewski †1941 | 3,9 | ✔ | loc-jukebox-128505-minuet-in-g-major-op-14-no-1 |

Odrzucone: „Wlazł kotek” (opracowanie Świerzyńskiego, †1957). Pozycje oznaczone „?” wejdą tylko wtedy, gdy przed
pobraniem znajdę daty śmierci autorów. W przeciwnym razie odpadają, a stacja ma wtedy około 39 minut.

## 2. Jazz i ragtime (do 1925)
| # | Tytuł | Wykonawca | Rok | Utwór (autor †) | Min | Źródło |
|---|---|---|---|---|---|---|
| 1 | Too much mustard | Europe's Society Orchestra | 1913 | C. Macklin †1944 | 3,8 | LoC, PD Mark: loc-jukebox-134232-too-much-mustard |
| 2 | Temptation rag | Arthur Pryor's Band | 1910 | H. Lodge †1933 | 2,5 | LoC: loc-jukebox-129052-temptation-rag |
| 3 | Red pepper | Fred Van Eps (banjo) | 1911 | H. Lodge †1933 | 2,2 | LoC: loc-jukebox-131253-red-pepper |
| 4 | Dill pickles rag | Arthur Pryor's Band | 1909 | C.L. Johnson †1950 | 2,4 | LoC: loc-jukebox-127191-dill-pickles-rag |
| 5 | That flying rag | Arthur Pryor's Band | 1911 | L.P. Laurendeau †1916 | 2,9 | LoC: loc-jukebox-131075-that-flying-rag |
| 6 | Desecration rag | Felix Arndt (fort.) | 1914 | Arndt †1918 | 3,1 | LoC: loc-jukebox-134701-desecration-rag-a-classic-nightmare |
| 7 | Shreveport stomp | Jelly Roll Morton (fort.) | 1924 | Morton †1941 | 2,9 | IA, PD Mark: shreveport-stomp-jelly-roll-morton-1924 |
| 8 | Maple leaf rag | Vess L. Ossman's Banjo Orch. | 1907 | S. Joplin †1917 | 2,7 | IA bez znaku: 1907-USA-Archives-…-Maple-Leaf-Rag |
| 9 | Snake rag | King Oliver's Creole Jazz Band | 1923 | J. Oliver †1938 | 3,0 | IA bez znaku: 1923-USA-Archives-…-Snake-Rag- |
| 10 | Zulu's ball | jw. | 1923 | J. Oliver †1938 | 2,6 | Great 78: 78_zulus-ball_king-olivers-creole-jazz-band_gbia0366412a |
| 11 | Working man blues | jw. | 1923 | J. Oliver †1938 | 2,5 | Great 78: 78_working-man-blues_king-olivers-creole-jazz-band_gbia0553119a |
| 12 | London café blues | jw. | 1923 | J.R. Morton †1941 | 3,0 | Great 78: 78_london-cafe-blues_king-olivers-creole-jazz-band_gbia0553146a |
| 13 | Davenport blues | Bix Beiderbecke and His Rhythm Jugglers | 1925 | Beiderbecke †1931 | 2,8 | IA bez znaku: 1925-USA-Archives-1925-01-26-Bix-… |

Pozycje 1–7 mają jawny znak PD i dają razem około 20 minut. Pozycje 8–13 są w domenie z mocy prawa, ale nie mają
znaku. → pytanie do szefa.

## 3. Klasyczna (Musopen na Wikimedia Commons, „Public domain”, nagrania współczesne)
Każdy plik jest na stronie `https://commons.wikimedia.org/wiki/File:<nazwa>`. Około 60 minut, przemieszane:

| # | Utwór | Wykonawca | Min |
|---|---|---|---|
| 1 | Chopin – Polonez A-dur op. 40 nr 1 „Wojskowy” | Aya Higuchi | 5,2 |
| 2 | Chopin – Etiuda c-moll op. 10 nr 12 „Rewolucyjna” | Edward Neeman | 2,8 |
| 3 | Chopin – Nokturn Es-dur op. 9 nr 2 | Frank Levy | 4,5 |
| 4 | Chopin – Mazurek a-moll op. 17 nr 4 | Edward Neeman | 4,5 |
| 5 | Chopin – Fantazja-impromptu op. 66 | Frank Levy | 5,5 |
| 6 | Chopin – Walc As-dur op. 64 nr 3 | Diana Hughes | 3,1 |
| 7 | Chopin – Polonez As-dur op. 53 „Heroiczny” | Luke Faulkner | 7,3 |
| 8 | Chopin – Etiuda E-dur op. 10 nr 3 | Edward Neeman | 4,6 |
| 9 | Mozart – Wesele Figara, uwertura | Musopen Symphony | 4,0 |
| 10 | Mozart – Czarodziejski flet, uwertura | Musopen Symphony | 6,7 |
| 11 | Bach – Wariacje Goldbergowskie, Aria | Shelley Katz | 4,9 |
| 12 | Beethoven – Uwertura „Egmont” | Musopen Symphony | 9,0 |
| 13 | Brahms – Symfonia nr 3, cz. III | Musopen Symphony | 6,2 |

## 4. „Lalka” – słuchowisko
- Źródło: Wolne Lektury, audiobook Bolesława Prusa „Lalka”, tom I, rozdziały I–III (około 63 minut). Rozdziały
  to: sklep Wokulskiego, rządy starego subiekta i pamiętnik starego subiekta, więc temat pasuje do gry.
- Czyta Albert Osik, reżyseria Dominik Lehman, © 2020 Fundacja Wolne Lektury.
- Licencja: **Licencja Wolnej Sztuki 1.3** (LAL, Free Art License, http://artlibre.org/licence/lal/pl/). To licencja
  copyleft podobna do CC BY-SA, a Creative Commons uznaje ją za zgodną z CC BY-SA 4.0. **Nie ma jej na liście szefa**,
  więc trzeba decyzji.
- Adres pliku: `https://wolnelektury.pl/media/book/mp3/lalka-tom-pierwszy_00N_tom-i-rozdzial-…mp3`.

## 5. Szum
Bez pliku: szum generowany w przeglądarce (Web Audio, szum różowy z trzaskami). Nie ma licencji, nie zajmuje miejsca.

## Strona „Nagrania w radiu”
Każda pozycja w grze dostaje wiersz: tytuł, wykonawca, rok, autor utworu, źródło (link) i licencja. Dane będą w
`dane/radio.yaml`, a strona będzie generowana z nich.
