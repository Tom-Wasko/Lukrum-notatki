# Przegląd prawny gałęzi `fable` względem `main` (16.11.2026)

To ćwiczenie, a nie porada prawna. Przegląd tylko do odczytu: w repo nic nie zmieniłem.
Zakres: `git diff main...fable` (98 plików) oraz grepy po całym `gra/` na gałęzi fable. Numery linii dotyczą gałęzi fable.

## Podsumowanie

- **Ślady innych gier biznesowych:** czysto. `git grep` po nazwach innych gier biznesowych na `fable` daje 0 trafień w plikach śledzonych. W commitach też nic. Jedyny ślad to wzmianka w `PLAN.md` o rusztowaniu z innych gier biznesowych, ale jest w `.git/info/exclude`, więc nie trafia do repo. Folder `gra/.hypothesis/` zawiera ścieżki do folderów roboczych sprzed zmiany nazwy, ale jest w `.gitignore`.
- **Najpoważniejsze:** (1) instrukcja uczy, że zlecenie jest "bez ZUS pracodawcy", a dwa akapity dalej, że zlecenie nie jest sposobem na etat bez składek; (2) "Nocna 13" nadal zachęca do ukrywania kasyna przed nauczycielem, a instrukcja dla mistrza gry w ogóle o nim nie wspomina; (3) logotypy prawdziwych firm (`LOGA`) nadal są w kodzie, wbrew `grafiki/README.md`; (4) porównania cenowe przypisane prawdziwym sieciom (Stokrotka "trochę drożej", Auchan "drożej niż w hurtowni").
- **OSM i fonty są w porządku:** podpis "© autorzy OpenStreetMap" z linkiem do `openstreetmap.org/copyright` jest widoczny na mapie (`lublin.js:228`) i w README. Plik `fonty/OFL.txt` zawiera licencje wszystkich czterech fontów (Oswald, PT Sans, Alfa Slab One, Atkinson Hyperlegible). Gra nie ładuje nic z zewnętrznych serwerów (patrz pkt 6).

### Do poprawienia od razu (drobne, pewne zmiany tekstu)

1. `INSTRUKCJA.md:248` i `:262`: zdanie o ZUS przy zleceniu (P1).
2. `INSTRUKCJA.md:260`: "art. 34 i 36 KP" na "art. 36 KP" (P5).
3. `INSTRUKCJA.md:257`: "26 dni w roku" na "20 lub 26 dni" (P4).
4. `INSTRUKCJA.md:309`: "zastawem może być ... lokal, budynek" na "zabezpieczeniem (hipoteka na budynku, zastaw na sprzęcie)" (P6).
5. `INSTRUKCJA.md:91`: "odsetki od pożyczek ... nie obniżają podatku" na "kary, mandaty i odsetki za zwłokę od zaległości" (P7).
6. `budynki.yaml:94-96`: "Pięć biur" z innymi nazwami niż w `biura.yaml` i w instrukcji (cztery biura) (M2).
7. `INSTRUKCJA.md:8`: daty 2025/2026 ujednolicić (P9).
8. `jak_grac.html:81`: dopisać "Gra nie jest związana z tymi firmami." (stopka jak w `gra.html:26`).
9. `INSTRUKCJA.pdf` jest z 13.11, a `.md` z 16.11: wygenerować na nowo (`manage.py instrukcja_pdf`).
10. Rodzaj męski w tekstach dla gracza (pkt 7): `reklama.yaml:108, 160, 194, 211`, `kasyno.yaml:91`, `parki.yaml:145`.
11. `AGENTS.md`: "40 000 zł na start", a dane i instrukcja mają 50 000 zł (nie widzi tego gracz, ale wprowadza w błąd kolejnych agentów).

### Do decyzji autora

- Hazard: czy "Nocna 13" ma być w grze dla niepełnoletnich i jak ma ją widzieć nauczyciel (H1, H2).
- Prawdziwe marki: zostają z nazwy bez opisów porównawczych, czy fikcyjne nazwy (M1, M3).
- Debet: zostawić mechanikę "nowy bank przejmuje dług" z adnotacją o uproszczeniu, czy zmienić (P2).
- Zlecenie bez ZUS: dodać adnotację, czy ustawić składki zgodnie z prawem (`podatki_2026.yaml:98`) (P1).
- Józio (Gombrowicz) i "Solaris" (Lem): zostają jako aluzje, czy zamiana (A1).
- Prawdziwe numery domów przy fikcyjnych firmach z "ciemnych" branż: lichwiarz, detektyw, lombard (M4).
- Giełda "prawdziwe notowania S&P 500": skąd dane i na jakiej licencji (M6).

---

## 1. Ślady innych gier biznesowych

**Brak znalezisk.** Sprawdziłem `git grep` po nazwach innych gier biznesowych, `jak w grze`, `wzorowan`, `inspirowan`. Trafienia dotyczyły tylko słów "obserwacji" i "jak w grze (jednocześnie)" w sensie ustawień debetu. W `zalozenia.yaml:17` jest nawet jawne zdanie "nie dopasowanie do cudzych obserwacji". To zdanie jest dobre.

- **Drobne.** `gra/dane/zalozenia.yaml` i `katalog.yaml` zawierają pola `zrodlo` z odwołaniami do wewnętrznych notatek ("notatka Elementy mapy", "F3a.6", "PRACA_NOCNA pyt. 23"). Nie widzi ich gracz, ale przed upublicznieniem repo to ślady wewnętrznego procesu. Poprawka: zostawić.
- **Ryzyko procesowe (powtórka z poprzedniego przeglądu):** reklamowe frazy typu "lepszy niż X" w README i opisach PR. W `README.md` nie znalazłem żadnych porównań z inną grą.

## 2. Marki i nazwy prawdziwych firm

Stopka "Nazwy prawdziwych firm i miejsc oddają realia..." jest w `gra.html:26`, `start.html:14`, na końcu `INSTRUKCJA.md:536-537` i w README. W `jak_grac.html:81` brakuje zdania "Gra nie jest związana z tymi firmami". W panelu mistrza gry i w `konta/_strona.html` stopki nie ma.

**M1 (średnie).** `dane/dostawcy.yaml:72, 123`, `budynki.yaml:236`, `INSTRUKCJA.md:220`.
Cytaty: Stokrotka: "Lubelski dyskont przy osiedlu - blisko, ale trochę drożej"; Auchan: "drożej niż w hurtowni i bez gazetki"; Eurocash: "Najtańsze warzywa i sosy, bez dań wege". W instrukcji: "ceny Auchan, prowizja 6%, abonament 120 zł tygodniowo".
Dlaczego: to porównania cenowe i jakościowe o prawdziwych firmach (Stokrotka ma siedzibę w Lublinie). Mogą zostać odebrane jako reklama porównawcza albo naruszenie dóbr osobistych (art. 23-24 k.c. w zw. z art. 43 k.c.). Abonament i prowizja przypisane Auchan sugerują usługę, której ta firma nie oferuje.
Poprawka (teksty): Stokrotka: "Dyskont przy osiedlu: blisko domu, mały wybór."; Auchan: "Hipermarket: wszystko pod jednym dachem, odbiór osobisty."; instrukcja: "(ceny z hipermarketu, prowizja 6%, abonament 120 zł tygodniowo – oferta fikcyjna)". Mocniejsza opcja: zamienić nazwy sieci na rodzajowe ("dyskont przy osiedlu", "hipermarket przy Witosa").

**M2 (średnie).** `budynki.yaml:94-96`.
Cytat: "Pięć biur rachunkowych pod jednym dachem (J.K.Ś. Jakuba Klimka-Ślęzaka, Pod Trybunałem, Pani Halinka, e-Księgi24.pl, Debet & Kredyt)".
Dlaczego: `biura.yaml` i `INSTRUKCJA.md:333-342` mają cztery inne biura (J.K.Ś., Józef K., Scrooge, Asteroida 328). To jest stary tekst, który gracz widzi na mapie. Do tego "Jakub Klimek-Ślęzak" wygląda jak imię i nazwisko prawdziwej osoby, a "e-Księgi24.pl" to nazwa w formie domeny, której istnienia nie sprawdzono (poprzedni przegląd też to odnotował).
Poprawka: "Cztery biura rachunkowe pod jednym dachem (J.K.Ś., Józef K., Scrooge i Asteroida 328) i pokój z biurkiem dla tych, którzy księgują sami."; `biura.yaml:28` "Jakub Klimek-Ślęzak" zmienić na wyraźnie fikcyjne imię i nazwisko.

**M3 (średnie).** `budynki.yaml:314`, `INSTRUKCJA.md:117`, `katalog.yaml:257-304`.
Cytat: "Park handlowy (Leroy Merlin, IKEA, OBI, Jula, Castorama)". W `katalog.yaml` pozycje wyposażenia mają `sklep: Leroy Merlin` / `IKEA` z cenami.
Dlaczego: pięć prawdziwych marek w jednej nazwie budynku, bez ich udziału. Nowy sklep "Meblościanka" (`miejsca.js:73`, `dekor.js:78`) jest fikcyjny, więc nazwy prawdziwych sieci są już zbędne. Wspomniane ceny z "IKEA" to przypisywanie firmie ofert.
Poprawka: nazwa budynku "Park handlowy na Węglinie"; w `katalog.yaml` `sklep: Leroy Merlin` zamienić na "Market budowlany", `sklep: IKEA` na "Meblościanka" (po dostosowaniu testów).

**M4 (średnie).** `budynki.yaml:525` (Harpagon, ul. Rybna 4), `:578` (detektyw, ul. 1 Maja 20, "nad lombardem przy dworcu"), `:346` (ul. Lipowa 13), `:404`.
Dlaczego: fikcyjni lichwiarz, detektyw i lombard dostali prawdziwe adresy z OSM. Lokatorzy tych budynków mogą się rozpoznać (dobra osobiste, pośrednio).
Poprawka: dla budynków "ciemnych" branż (Harpagon, detektyw, kasyno) usunąć numer domu i `adres:`, zostawić ulicę w polu `miejsce`.

**M5 (drobne).** `budynki.yaml:398-404`, `miejsca.js:83`.
Cytat: "Pracownia Analiz UMCS... Studenci ekonomii badają rynek". Dlaczego: instytucja publiczna "wykonuje" w grze fikcyjną działalność. Ryzyko niskie. Poprawka: "Pracownia Analiz przy uniwersytecie", bez "UMCS" i bez adresu rektoratu (pl. Marii Curie-Skłodowskiej 5). Ogród Botaniczny UMCS i mecze Motoru Lublin (`losowe.yaml:239`, `INSTRUKCJA.md:160, 423`) są neutralne i mogą zostać.

**M6 (średnie).** `budynki.yaml:593`.
Cytat: "prawdziwe notowania spółek S&P 500". Giełda jest dopiero w budowie (`gielda.js:6-12`: "otwiera się wkrótce"), a `INSTRUKCJA.md:119` już ją zapowiada.
Dlaczego: nazwa S&P 500 jest znakiem, a dane notowań mają licencje; skąd dane, nie wiadomo. Gra dla niepełnoletnich "inwestuje" za prywatne pieniądze właściciela.
Poprawka: opis "kursy spółek fikcyjnych" albo dane z jawnej licencji; w instrukcji dopisać, że to symulacja, nie porada inwestycyjna.

**M7 (średnie).** `ikony_marek.js:4, 105-149` (`LOGA`), `grafiki/README.md` ("Żadna grafika nie odtwarza cudzego logo").
Dlaczego: logotypy Biedronki, Lidla, IKEA, banków w barwach firm nadal są w kodzie i rysują się na kartach dostawców i banków (`kartaMarki`, `znakMarki`). Nowa mapa (`mapa/ikony.js:1`) jest czysta, ale ekrany zakładek nie. README grafik kłamie, a nie powinno.
Poprawka: usunąć słownik `LOGA` i zostawić zapasowe ikony (`KOSZYK`, `DOM`, `BANK`), których plik już używa.

**M8 (drobne).** `motyw.js:88`, `zmienne.css:39, 63`, `INSTRUKCJA.md:129`. Paleta "Pewex" to nazwa używanej marki. Poprawka: "Dewizowa" (opisowo).

**M9 (drobne).** Reklamy: "TikTok" (`reklama.yaml:198-228`), "Mapy Google", "BLIK" (`INSTRUKCJA.md:382`), "pracuj.pl" (`INSTRUKCJA.md:228, 401`, `kandydaci.yaml:152`) jako rodzaje usług. Użycie nazwy opisowo jest akceptowalne. Ryzyko pojawia się, gdy firmie przypisuje się cenę lub negatywną cechę: "ogłoszenie kosztuje 400 zł" przy pracuj.pl to cena przypisana prawdziwemu serwisowi. Poprawka: "portal z ogłoszeniami o pracę (ogłoszenie kosztuje 400 zł)", zostawić pracuj.pl tylko w polu źródła.

## 3. Prawa autorskie

**A1 (średnie).** Gombrowicz (zm. 1969, ochrona do końca 2039). `dane/wnetrza/bywalcy.yaml:64-69`, `dymki.yaml:74-78, 182, 189, 217`, `miejsca.js:83` (`postac: "bywalec-jozio"`), `grafiki/postacie/bywalec-jozio.svg`.
Cytat: "Boi się, że ktoś mu 'przyprawi gębę'"; dymek "Nie dam sobie przyprawić gęby frajera"; Józio jako klient z własną grafiką i kilkoma kwestiami.
Dlaczego: sam komentarz w `bywalcy.yaml:15` zapowiada "tylko imię i aluzja, a nie cytaty", a kilkanaście linijek niżej jest "przyprawić gębę", czyli centralny motyw "Ferdydurke". Do tego kilka kwestii z rysunkiem to korzystanie z postaci, nie aluzja. Sama aluzja jest bezpieczna; własna kwestia i grafika to już nowy utwór zależny od cudzej postaci.
Poprawka: zamienić Józia na postać z domeny publicznej (np. "Zygmunt Wokulski" jest już w banku; pasuje "Kazio" z "Syzyfowych prac" Żeromskiego), albo zostawić jedno zdanie bez "gęby": "Za {cena} zł? Koledzy by się ze mnie śmiali."

**A2 (średnie).** Lem (zm. 2006, ochrona do 2076). `banki.yaml:100-103`, `budynki.yaml:76`, `miejsca.js:36`.
Cytat: "Nawiązanie: 'Solaris' Lema - bezkresny ocean, który trudno przewidzieć." Opis jest widoczny dla gracza (`banki.js:51, 66`).
Dlaczego: sama nazwa "Solaris" nie jest chroniona jako utwór (tytuł), ale to zarazem znak firmy Solaris Bus & Coach; wskazanie autora nie robi z tego cytatu. Ryzyko niskie, jedno nawiązanie do Lema.
Poprawka: zostawić lub zmienić nazwę na "Ocean" z domeny publicznej; przy zachowaniu wpisać autora i tytuł (jak jest). Gra nie ma ekranu "Nawiązania i źródła", który zalecał poprzedni przegląd.

**A3 (drobne).** Domena publiczna (pasuje autor i rok zgonu): Sienkiewicz (Kmicic, Zagłoba), Prus (Wokulski, Rzecki), Reymont (Ziemia Obiecana), Mickiewicz (Soplicowo), Zapolska (Dulska), Fredro (Papkin), Żeromski (Judym), Molier (Harpagon, Mistrz Jakub), Dickens (Scrooge), Kafka (Józef K.), Potocki ("Rękopis znaleziony w Saragossie" w `kasyno.yaml`), Saint-Exupéry ("Asteroida 328", "Pan Bankier"; zm. 1944, w Polsce wolny od 2015). Uwaga: polskie tłumaczenia "Małego Księcia" są chronione. Nazwa "Asteroida 328" i "Pan Bankier" nie cytują tłumaczenia, więc bez problemu, ale nie wolno wkleić zdań z polskiej wersji.

**A4 (OK).** Fonty: `fonty/OFL.txt` zawiera pełne licencje i noty copyright wszystkich czterech rodzin; pliki `.woff2` są lokalne. Drobna uwaga: Alfa Slab One i PT Sans mają "Reserved Font Name"; podzbiory z Google Fonts używa się powszechnie, ale kto chce być ostrożny, niech nie przemianowuje plików. `chart.umd.min.js` (MIT) ma nagłówek licencji.

**A5 (drobne).** Dane OSM (`mapa/lublin.json`, `pobierz_osm.py`). Podpis jest (`lublin.js:211, 228`). ODbL wymaga także, by udostępniana pochodna baza (`lublin.json`) była dostępna na ODbL. `lublin.json` ma pole `zrodlo: ... licencja ODbL`, co wystarcza. Poprawka: w README dopisać zdanie "Plik `lublin.json` udostępniamy na licencji ODbL" i zmienić tekst na oficjalny "© współtwórcy OpenStreetMap" (`© OpenStreetMap contributors`). W skrypcie `pobierz_osm.py:31` `User-Agent` to "geokoder-skrypt/1.0"; polityka Nominatim wymaga identyfikacji aplikacji: "LUKRUM-pobierz-mape/1.0".

**A6 (drobne).** Grafiki. `grafiki/README.md` zapowiada "własne grafiki SVG ... postacie są własnymi interpretacjami, nie wzorują się na ekranizacjach" i tak jest zapisane. Brakuje wpisu, kto je narysował (skrypty `narzedzia/grafiki/`), co przydaje się w sporze o autorstwo.

## 4. Błędy merytoryczne (prawo, podatki)

**P1 (poważne).** `INSTRUKCJA.md:248`, `:262`, `zalozenia.yaml:521`, `podatki_2026.yaml:98`.
Cytaty: "umowa zlecenie - bez ZUS pracodawcy i bez wypowiedzenia"; kilka linijek niżej: "Umowa zlecenie nie jest sposobem na etat bez składek (art. 22 § 1 KP)".
Dlaczego: w prawdziwym prawie od zlecenia płaci się składki (emerytalna, rentowa, wypadkowa; wyjątek: student do 26 lat, art. 6 ust. 1 pkt 4 ustawy o systemie ubezpieczeń społecznych). `podatki_2026.yaml:98` przyznaje, że to uproszczenie ("naprawdę zlecenie ma składki jak etat"), ale gracz tego komentarza nie widzi. Dwa zdania w jednym rozdziale sobie przeczą, a uczeń wyniesie "zlecenie jest tańsze niż etat".
Poprawka (tekst): "*umowa zlecenie* - w grze bez składek pracodawcy (uproszczenie: naprawdę od zlecenia płaci się składki ZUS, wyjątek to student do 26 lat) i bez wypowiedzenia, ale obniża zadowolenie..." Lub `zus_pracodawcy_zlecenie: 0.2048`.

**P2 (średnie).** `INSTRUKCJA.md:321-326`, `banki.js:27-36`.
Cytat: "nowy bank przejmuje dług i pobiera jednorazową opłatę: 2% kwoty debetu".
Dlaczego: banki nie przejmują debetu przy zmianie rachunku; trzeba go spłacić (lub zaciągnąć kredyt konsolidacyjny). Uczy fałszywego mechanizmu.
Poprawka: dopisać "(uproszczenie gry: w prawdziwym życiu debet trzeba spłacić przed zamknięciem konta albo zaciągnąć kredyt na jego spłatę)".

**P3 (średnie).** Kontrola PIP. `INSTRUKCJA.md:262-267`, `zalozenia.yaml:595-611`, `hr.js` (nowy blok PIP).
Cytaty: "z szansą 5% ... wystawia karę 2 000 zł (jedną na firmę, nie na osobę)"; "co najmniej 30 godzin w tygodniu przez 4 tygodnie z rzędu"; w tekście zdarzenia "Wystawia mandat".
Dlaczego: (a) próg 30 h i 4 tygodnie wygląda w instrukcji jak norma prawna, a prawo liczy charakter pracy, nie godziny; (b) prawdziwa sankcja to grzywna za wykroczenie (art. 281 KP: 1 000-30 000 zł; mandat inspektora ma niższy limit), nałożona na osobę odpowiedzialną, a nie na "firmę"; (c) pomija najdotkliwsze skutki: zaległe składki ZUS i ustalenie stosunku pracy (od 2026 r. mogą być w tym nowe uprawnienia PIP; to do sprawdzenia przez prawnika, niczego tu nie twierdzę); (d) tylko zlecenie jest "ryzykowne", a B2B na pełnym etacie ma to samo ryzyko ("bez względu na nazwę", art. 22 § 1^1 KP).
Poprawka (tekst, dopisek do `INSTRUKCJA.md:267`): "Progi (30 godzin, 4 tygodnie, 5%) to uproszczenie gry. W prawdziwym życiu inspektor ocenia sposób pracy: podległość, stałe godziny i miejsce, wynagrodzenie za czas. Poza karą grożą zaległe składki. To samo dotyczy kontraktu B2B, jeśli osoba pracuje jak etatowiec."

**P4 (średnie).** `INSTRUKCJA.md:257`. Cytat: "26 dni w roku, art. 154 KP". Dlaczego: 20 dni przy stażu poniżej 10 lat, 26 dni od 10 lat. Młodzi pracownicy w kebabie mają 20. Poprawka: "20 albo 26 dni w roku zależnie od stażu (art. 154 KP); w grze liczymy uśrednione 10% czasu".

**P5 (drobne).** `INSTRUKCJA.md:260`. Cytat: "(art. 34 i 36 KP)". Dlaczego: art. 34 dotyczy wypowiedzenia umowy na okres próbny (3 dni, tydzień, 2 tygodnie), a nie tej tabeli. Poprawka: "(art. 36 KP)".

**P6 (drobne).** `INSTRUKCJA.md:309`. Cytat: "zastawem może być kupiony lokal, budynek albo sprzęt". Dlaczego: nieruchomość zabezpiecza się hipoteką, zastaw (rejestrowy) dotyczy ruchomości. Poprawka: "zabezpieczeniem może być kupiony lokal lub budynek (hipoteka) albo sprzęt (zastaw)".

**P7 (średnie).** `INSTRUKCJA.md:91`. Cytat: "Mandaty i odsetki od pożyczek (skarbowe, sanepidu, PIP, odsetki Harpagona) nie obniżają podatku". Dlaczego: kary i mandaty nie są kosztem uzyskania przychodu, ale zapłacone odsetki od zwykłej pożyczki lub kredytu już tak. Zdanie uczy błędu. Poprawka: "Kary i mandaty (skarbowe, sanepidu, PIP) oraz odsetki za zwłokę od zaległości podatkowych nie obniżają podatku, ale obniżają wynik. W grze to samo zakładamy dla odsetek od Harpagona (uproszczenie)."

**P8 (drobne).** `INSTRUKCJA.md:251-252`. Staż z urzędu pracy: "przez 6 tygodni nie płaci się pensji". Prawdziwy staż trwa co najmniej 3 miesiące, a stypendium wypłaca urząd. Poprawka: "(w grze staż jest skrócony do 6 tygodni)". Także `INSTRUKCJA.md:203`: "Sanepid musi też odebrać lokal" i `:121`: "Urząd miasta (rejestracja)". Prawda: firmę rejestruje się w CEIDG (online), a zakład żywienia zgłasza do PIS. Poprawka: "Urząd miasta (zgody i odbiory lokalu)" i "odbiór sanitarny" jako skrót gry.

**P9 (drobne).** `INSTRUKCJA.md:8` ("1.09.2025 - 4.01.2026") a płaca minimalna 2026 (`:268`) i dane `podatki_2026`. Dziś jest listopad 2026, więc daty są nieaktualne. Poprawka: "1.09.2026 - 3.01.2027" lub bez dat.

**P10 (drobne).** `INSTRUKCJA.md:294`: "ZUS rozliczają się same na koniec tygodnia". W prawdziwym życiu miesięcznie. Poprawka: dopisek "(w grze co tydzień)". `INSTRUKCJA.md:315`: "odsetki karne (art. 481 § 2¹ KC)": w KC są "odsetki za opóźnienie"; "karne" to żargon. Poprawka: "odsetki za opóźnienie".

**P11 (OK).** Płaca minimalna 4 806 zł (2026), próg środka trwałego 10 000 zł, art. 359 § 2¹ KC (odsetki maksymalne), art. 22 § 1 KP, art. 281 KP w źródle liczb, student do 26 lat bez ZUS i PIT, wypowiedzenie 2 tygodnie / miesiąc / 3 miesiące, odpraw w małej firmie nie ma. Liczby PIP w instrukcji zgadzają się z `zalozenia.yaml:595-611` (30 h, 4 tygodnie, 5%, 2 000 zł); zlecenie -0,04 zgadza się z `zalozenia.yaml:362`; limity debetu 5 000-40 000 zł z `banki.yaml`.
Poza zakresem diffu, ale do sprawdzenia przez prawnika: `dane/wnetrza/dymki.yaml:215-218` (odpowiedź o 16-latku w wakacje powołuje art. 200¹, 200² i 203 KP; wątpię, czy przepisy o "lekkich pracach" pasują do 16-latka, który jest już młodocianym (art. 190 KP i dalsze). Nie weryfikowałem, trzeba sprawdzić).

## 5. Hazard i nieletni

**H1 (poważne).** `kasyno.js:7-13` (zakładka "Zasada milczenia").
Cytat: "Pierwsza zasada Nocnej 13: księgowa nie musi wiedzieć wszystkiego. Druga zasada: mistrz gry tym bardziej"; "Kto mówi o nim mistrzowi gry, ten sam rozumie, że kebab i hazard to dwa różne fartuchy".
Dlaczego: w grze szkolnej dla niepełnoletnich tekst zachęca do ukrywania hazardu przed nauczycielem. Samo kasyno jest ukryte (hasło "koziol" i zaproszenie, `kasyno.yaml`), ale wejść może każdy uczeń; ruletka i automat ("Jednoręki Zenek", zwrot ok. 82%) działają na pieniądzach gry. Odpowiedzialność za treść spada na szkołę i autora. To powtórka z ostrzeżenia z poprzedniego przeglądu i nic się nie zmieniło.
Poprawka: usunąć z `ZASADA_MILCZENIA` "Druga zasada: mistrz gry tym bardziej" i ostatni akapit; dopisać jednoznaczny znacznik edukacyjny: "Hazard to ryzyko. W prawdziwym życiu gry hazardowe są dozwolone dopiero po ukończeniu 18 lat (ustawa o grach hazardowych)."

**H2 (średnie).** `INSTRUKCJA.md` nie wspomina "Nocnej 13" ani kasyna (rozdział dla mistrza gry też nie). `kasyno.yaml` mówi, że "w przeglądzie, rankingu i eksporcie klubu nie ma". Instrukcja niczego więc nie obiecuje, ale też nie informuje nauczyciela o istnieniu hazardu w grze. `miejsca.js:96` dodaje punkt "Nocna 13 - Drzwi bez szyldu" w scenie Starego Miasta; `swiat.js:36` ukrywa go, gdy zakładka jest ukryta, więc zwykły uczeń go nie zobaczy. Przełącznik jest tylko w ustawieniach serwera (`LUKRUM_KASYNO=0`, `widoki.py:103-105`), a nie w panelu mistrza gry ani w `funkcje.yaml`.
Poprawka: w rozdziale "Dla mistrza gry" dopisać: "W grze jest ukryty klub z grami losowymi ('Nocna 13'), dostępny po zaproszeniu lub haśle. Gra jest dla uczniów niepełnoletnich: wyłączysz klub na serwerze zmienną `LUKRUM_KASYNO=0`." i dodać go do zestawów funkcji ("Krótka lekcja" i "Pierwsza gra" bez klubu).

**H3 (drobne).** Wątki przemocy w żartach: `INSTRUKCJA.md:329` ("wizyty, po których w lokalu brakuje krzeseł"), `:376-378` (gazetka "zrolowana" jako broń), `budynki.yaml:529` ("pytania zadaje Mistrz Jakub"). To humor, ale dla uczniów lichwa przedstawiona jako zabawny "kantor" bez słowa o tym, że jest przestępstwem (art. 304 k.k. i odsetki maksymalne), jest edukacyjnym przeoczeniem. Poprawka: w `INSTRUKCJA.md:328` dopisać "W prawdziwym życiu pożyczka z odsetkami powyżej maksymalnych jest nielegalna (lichwa)."

## 6. Dane osobowe, RODO, prywatność

- **Brak ładowania zasobów z zewnętrznych serwerów** (grep `https://` w szablonach i `static/`): jedyny zewnętrzny adres w interfejsie to link `<a href>` do `openstreetmap.org/copyright` (`lublin.js:228`), który otwiera się dopiero po kliknięciu. Fonty (`fonty/*.woff2`), Chart.js (`vendor/`), mapa (`lublin.json`) są lokalne. `fonty.css` wspomina "Montserrat" tylko jako zapasowy krój (`styl.css`), bez ładowania. **Bez uwag.**
- **Pozostałe adresy zewnętrzne** są poza interfejsem gracza: `pobierz_osm.py` (Overpass, Nominatim) to narzędzie autora; `hostuj.py` (tunel Cloudflare `trycloudflare.com`) i `LOGOWANIE_MICROSOFT.md` (logowanie kontem szkolnym) wysyłają dane przez podmioty trzecie. Poprawka: w dokumentacji dla szkoły dopisać, że przy tunelu i logowaniu Microsoft ruch przechodzi przez serwery Cloudflare/Microsoft (szkoła jest administratorem danych uczniów).
- **Dane osobowe w repo (średnie).** Historia git: 34 commity autora z prywatnym adresem Gmail (`waskotomek1212@gmail.com`) i 1 commit z adresem Gmail drugiej osoby (`stunterpodlogadwa@gmail.com`, podpis "nie podam"). W plikach śledzonych adresów e-mail nie znalazłem (przykłady `jan.kowalski@szkola.edu.pl`, `anna.kowalska@szkola.edu.pl` w `LOGOWANIE_MICROSOFT.md` są fikcyjne). Repo jest prywatne, więc obecnie bez skutku. Przed upublicznieniem trzeba będzie albo użyć adresu `noreply` GitHuba (`users.noreply.github.com`) i przepisać historię, albo opublikować świadomie. To decyzja autora. Drugą osobę o jej adresie w historii trzeba uprzedzić.
- **Prawdziwe osoby w tekstach (średnie).** Imiona i nazwiska w grze są fikcyjne, ale dwa wyglądają na prawdziwe: "Jakub Klimek-Ślęzak" (`biura.yaml:28`, `budynki.yaml:94`) i "Zenon Lupa" (`budynki.yaml:582`). Poprawka: sprawdzić w wyszukiwarce, a przy trafieniu zmienić.
- **Dymki i zdarzenia:** "Motor Lublin właśnie strzelił gola", "Ogród Botaniczny UMCS" (zdarzenia): neutralne.
- **Konta uczniów:** `INSTRUKCJA.md:457-458` ("login i hasło przekazuje się uczniom") w porządku; warto dopisać, żeby loginy nie zawierały nazwisk (dane minimalne).

## 7. Język (rodzaj gramatyczny w tekstach dla gracza)

Instrukcja i nowe pliki JS (`kurier.js`, `wujek.js`, `final.js`, `dekor.js`, `miejsca.js`) piszą neutralnie ("Wasz", "Wy", "Twoja firma", "Redakcja gratuluje"). Rodzaj męski zostaje w starszych tekstach danych:

| Plik:linia | Cytat | Poprawka |
|---|---|---|
| `dane/mapa/reklama.yaml:108` | "Fakturę grzecznie odrzuciłeś." | "Faktura została grzecznie odrzucona." |
| `reklama.yaml:160` | "Ty kroiłeś do czwartej." | "mięso kroiło się do czwartej." |
| `reklama.yaml:194` | "Wygrałeś: wszyscy już znają nazwę lokalu." | "Wygrana: wszyscy już znają nazwę lokalu." |
| `reklama.yaml:211` | "Kupiłeś grubsze serwetki." | "Grubsze serwetki kupione." |
| `dane/zdarzenia/kasyno.yaml:91` | "tyle, ile wrzuciłeś ({kwota})" | "tyle, ile wpadło ({kwota})" |
| `dane/zdarzenia/parki.yaml:145` | "że skłóciłeś się z..." | "że doszło do kłótni z..." |
| `INSTRUKCJA.md:285`, `hr.js:116` | "Właściciel sam na nim staje" | "Właściciel staje na nim osobiście" |

Rola "mistrz gry" (wszędzie, np. `INSTRUKCJA.md:14, 21, 53, 473`, `kasyno.js:8`) jest męska; zamiennik "prowadzący/prowadząca grę" to decyzja autora, bo to nazwa roli używana w całym panelu. Rzeczowniki "właściciel", "kucharz", "kasjer" w instrukcji to nazwy stanowisk i postaci, nie zwroty do gracza. W `wujek.js`/`final.js` męski głos wujka ("Mówiłem", "nie wygrałem") to cecha postaci, więc w porządku.

## 8. Kontrola pomocnicza

- Stopka z zastrzeżeniem: `gra.html:26`, `start.html:14`, `INSTRUKCJA.md:536-537`; brak pełnej wersji w `jak_grac.html:81`, panelu MG i na stronach logowania.
- Ekranu "Nawiązania i źródła" (autor, tytuł, wydanie) w grze nadal nie ma. Przy A1 i A2 byłby przydatny.
- `INSTRUKCJA.pdf` (13.11) nie odpowiada `INSTRUKCJA.md` (16.11).

## Co sprawdziłem, a czego nie

- Przeczytałem całą `INSTRUKCJA.md`, `miejsca.js`, `kurier.js`, `wujek.js`, `final.js`, `dekor.yaml`, `budynki.yaml`, `OFL.txt`, `lekcje.py` oraz fragmenty `hr.js`, `finanse.js`, `banki.js`, `kasyno.js`, `dekor.js`, `dostawcy.yaml`, `reklama.yaml`, `zalozenia.yaml`. `lekcje.py` to tylko logika terminów: bez problemów prawnych.
- Nie sprawdzałem w sieci, czy "Jakub Klimek-Ślęzak", "Zenon Lupa", "e-Księgi24.pl", "Lublin Jedzie" i "Kebabowa Królowa" istnieją naprawdę.
- Przepisów (KP, KC, ustawa o systemie ubezpieczeń społecznych) nie sprawdzałem w ISAP; cytuję z pamięci. Zmiany z 2026 r. dotyczące PIP wymagają weryfikacji prawnika.
- Prawnik jest potrzebny do: P3 (sankcje PIP), H1-H2 (hazard w grze szkolnej), oświadczeń konkursowych i decyzji o publikacji historii git.
