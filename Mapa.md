# Mapa

Co jest na mapie Lublina i jak to działa. Dla majstra (`[mapa]`) i strony mechanik (`[mechaniki]`). Umowy techniczne między
stronami: [[WSPOLPRACA]]. Sprawy otwarte: [[Do decyzji]], §3. Raport z budowy mapy: [[etap2-mapa – raport]].
Spis odświeżony 17.11.2026 z `dane/mapa/budynki.yaml`, `lokale.yaml`, `miasto.yaml` i `strefy.yaml`. Gdy dane się zmienią,
poprawiamy ten spis (nie odwrotnie).

## 1. Zasady
- Mapa własna, rysowana na granicach dzielnic z OpenStreetMap (podpis „© autorzy OpenStreetMap”), z płynnym
  przybliżaniem i trzema poziomami szczegółów: miasto → dzielnica → ulica.
- **10 stref gry.** `strefa` to jednostka popytu w grze, `miejsce` to prawdziwe położenie, w którym rysujemy budynek.
  Gdzie się różnią, w spisie jest znak ⇄ (strefa w nawiasie). Pozostałe dzielnice to tło.
- Prawdziwe miejsca, ale bez tłoku na Starym Mieście i Krakowskim Przedmieściu. **Majdanka na mapie nie ma** (decyzja
  autora 8.11).
- Od 15.11 każda strefa jest na mapie jedną prawdziwą dzielnicą (zmiana majstra, czeka na akceptację autora):

| Strefa gry | Dzielnica na mapie |
|---|---|
| Stare Miasto | Stare Miasto |
| Centrum | Śródmieście |
| Miasteczko Akademickie | Wieniawa |
| Politechnika | Rury |
| LSM i Czuby | Czuby Północne |
| Zygmuntowskie | Za Cukrownią |
| Dworzec | Dziesiąta |
| Czechów i Kalinowszczyzna | Czechów Południowy |
| Felin | Felin |
| Zemborzyce | Zemborzyce |

- Budynek to żeton. Kliknięcie woła `lukrum.otworzWnetrze(id)` i od razu otwiera wnętrze. Znaczniki rozróżnia kształt
  i znak (★ ✓), a nie sam kolor. Kolory tylko ze wspólnych zmiennych ([[Wygląd]]).
- Zdarzenia z parków pokazuje mapa w parkach. Przy ladzie są o nich tylko plotki.
- Na nowej mapie miejsca mają własne żetony (`detektyw`, `gielda`, `akademia`, `makro`, `selgros`, `auchan`, `biedronka`,
  `lidl`…) i mają mieć własne wnętrza ([[Decyzje]], „Mapa i miejsca”).

## 2. Zespoły budynków
Na mapie jest jeden budynek. Po kliknięciu otwiera się hol z szyldami, a potem wybiera się firmę. W danych: lista
`zespoly` w `dane/mapa/budynki.yaml`, a budynki w środku mają pole `zespol`. Adres i `geo` są w zespole.

| Zespół | Co w środku | Stan |
|---|---|---|
| Kamienica bankowa (pierzeja), Krakowskie Przedmieście 37 | **pięć banków** (decyzja 16.11 noc); w danych jeszcze 6: Kmicic, Wokulski i S-ka, Ziemia Obiecana, Oszczędności Rzeckiego, Soplicowo, Solaris. Który znika: [[Do decyzji]], §8c | w danych jeszcze 6, decyzja: 5 |
| Biurowiec przy Zana 39 | dziś: biura rachunkowe oraz trzy firmy od reklamy (Lajk, Fala Koziołka, Kozi Gród Events). Docelowo zostaje dla księgi KPiR i reszty firm | jest, do zmiany |
| Kamienica rachmistrzów | biura rachunkowe z szyldami jak banki: J.K.Ś., Józef K., Scrooge, Asteroida 328 | decyzja 16.11, do zrobienia |
| Dom reklamy (biurowiec z windą) | parter z portiernią i „Twoimi kampaniami”, piętra: drukarnia, radio, eventy, internet; budynek „drukarnia” znika | decyzja 16.11, do zrobienia |

Ubezpieczyciel (ul. Hipoteczna 4) i giełda (biuro maklerskie, Krakowskie Przedmieście 59) są osobnymi budynkami (giełda:
decyzja 16.11 noc, osobno od pierzei). „Gazeta Pana Cogito” i „Radio Tichy” to kanały drukarni Papier Przyjmie i Fali
Koziołka, bez osobnych miejsc.

## 3. Spis elementów według stref
W nawiasie `miejsce`, gdy różni się od strefy (⇄). **Plan** = przewidziane, jeszcze nie ma w danych.

### Stare Miasto (`stare_miasto`)
- Piekarnia Koziołek (ul. Grodzka 5; zaopatrzenie)
- Błonia pod Zamkiem (park, zdarzenia)
- Urzędy przy Szeligowskiego (ul. Szeligowskiego 24) ⇄ (Czechów Południowy)
- Biura rachunkowe ⇄ (biurowiec przy Zana, Rury), Kozi Gród Events ⇄ (Rury)
- Zabytki: Zamek Lubelski, Brama Krakowska, Wieża Trynitarska, Plac Po Farze
- Lokale: Grodzka 14, Rynek 8, Bramowa 3 (piwnica), Złota 2 (okienko), Kowalska 6 (od rundy 6)
- Klub „Pod Złotym Koziołkiem” (ekran „Nocna 13”): drzwi bez szyldu w scenie Starego Miasta, widoczne po haśle
  albo zaproszeniu

### Centrum (`centrum`, dzielnica Śródmieście)
- Krakowskie Przedmieście: kamienica bankowa (banki, zob. rozdz. 2) i osobno giełda „Byk i Koziołek”
  (Krakowskie Przedmieście 59)
- Sanepid (ul. Uniwersytecka 12, róg Karłowicza), Poczta Główna (Krakowskie Przedmieście 50), biuro nieruchomości „Klucz”
  (ul. Narutowicza 30), Redakcja „Kuriera Kebabowego” (ul. Chopina 11; gazeta „Kurier rankingowy”), TUW „Pod Koziołkiem”
  (ul. Hipoteczna 4), Galeria „Pod Zegarem” (ul. Lipowa 13; udogodnienia dla załogi)
- Agencja pracy „Ręce do Rożna” ⇄ (Miasteczko Akademickie), Radio i billboardy „Fala Koziołka” ⇄ (Rury)
- Ogród Saski (park) ⇄ (strefa akademickie)
- Zabytki: Plac Litewski, Centrum Spotkania Kultur
- Lokale: Krakowskie Przedmieście 21, Peowiaków 9, Chmielna 4, 3 Maja 12, Okopowa 7 (od rundy 10)
- **Plan:** bazar przy ul. Ruskiej (tanie warzywa, zaopatrzenie; bez żetonu, [[Do decyzji]] §8c pyt. 7)

### Miasteczko Akademickie (`akademickie`, dzielnica Wieniawa)
- Drukarnia „Papier Przyjmie” (ul. Akademicka 15; ulotki, plakaty, „Gazeta Pana Cogito”), po zmianie: w Domu reklamy
- Agencja „Lajk i Spółka” ⇄ (biurowiec przy Zana, Rury)
- Biedronka ⇄ (ul. Nałęczowska 24, Konstantynów)
- Pracownia Analiz UMCS (pl. Marii Curie-Skłodowskiej 5; badanie konkurencji)
- Ogród Botaniczny UMCS (park)
- Zabytki: UMCS, KUL
- Lokale: Radziszewskiego 16, Sowińskiego 10, Langiewicza 20, Głęboka 11 (od rundy 8)

### Politechnika (`politechnika`, dzielnica Rury)
- Lubelska Szkoła Kebabu (ul. Nadbystrzycka 36; szkolenia)
- Zabytek: Politechnika Lubelska
- Lokale: Nadbystrzycka 38, Nadbystrzycka 42, Zana 32

### Dworzec (`dworzec`, dzielnica Dziesiąta)
- Biuro detektywistyczne „Sokole Oko” (ul. 1 Maja 20, nad lombardem; śledzenie konkurencji)
- Kantor „U Harpagona” (ul. Rybna 4) ⇄ (miejsce: Stare Miasto)
- Zabytek: Dworzec Metropolitalny
- Lokale: Nowy Świat 20 (kiosk), Wyścigowa 31, Nowy Świat 34 (hala), Kunickiego 40

### Zygmuntowskie (`zygmuntowskie`, dzielnica Za Cukrownią)
- Auchan (al. Witosa 32) ⇄ (miejsce: Felin; zaopatrzenie), stolarnia „Lada i Syn” (ul. Krochmalna 13; stanowiska)
- Park Ludowy (park), zabytek: Arena Lublin
- Lokale: Stadionowa 1 (budka), al. Zygmuntowskie 5, **działka** Krochmalna 30

### Czechów i Kalinowszczyzna (`czechow`, dzielnica Czechów Południowy)
- Stokrotka (ul. Braci Wieniawskich 12; zaopatrzenie), Górki Czechowskie (miejsce widokowe)
- Lokale: Kompozytorów Polskich 8, Lipińskiego 3, **działka** Szeligowskiego 25, Elsnera 5 (od rundy 4)

### LSM i Czuby (`lsm_czuby`, dzielnica Czuby Północne)
- Lidl (ul. Romantyczna 2), Park Rury (park)
- Park handlowy na Węglinie (al. Kraśnicka 150; Leroy Merlin, IKEA, OBI, Jula, Castorama oraz sklep meblowy
  „Meblościanka”, zob. [[Sklep meblowy Meblościanka (dekor)]]) ⇄ (miejsce: Węglin Południowy)
- Lokale: Wileńska 3, al. Jana Pawła II 13, Filaretów 18, **działka** Armii Krajowej 60

### Felin (`felin`, dzielnica Felin)
- Hurtownie: Makro (ul. Chemiczna 5, Bronowice) ⇄, Eurocash (ul. Łęczyńska 9d, Bronowice) ⇄, Selgros (al. Jana Pawła II 59,
  Węglin Południowy) ⇄
- Hurtownia sprzętu gastronomicznego (al. Kraśnicka 152, park handlowy na Węglinie) ⇄
- Park Bronowicki (park)
- Lokale: Doświadczalna 30, Witosa 30, **działka** Vetterów 1

### Zemborzyce (`zemborzyce`, dzielnica Zemborzyce)
- Zalew Zemborzycki (woda, sezon), Zakłady Mięsne „Rożen” z Łęcznej (ul. Turystyczna 120, Hajdów-Zadębie; odbiór od rundy 3)
- Lokale: Żeglarska 1 (budka), Krężnicka 10, **działka** Żeglarska 20

### Poza miastem
- Port Lotniczy Lublin (Świdnik), obwodnica S19/S17/S12
- **Plan:** Elizówka, rynek hurtowy (warzywa i owoce w hurcie)

## 4. Spis elementów według rodzaju
Liczby z danych (17.11.2026).

| Rodzaj | Elementy | Ile |
|---|---|---|
| Urzędy i poczta | Urzędy przy Szeligowskiego, Sanepid, Poczta Główna | 3 |
| Finanse | banki (w danych 6, decyzja: 5), giełda „Byk i Koziołek”, TUW „Pod Koziołkiem”, Harpagon | 9 (po zmianie 8) |
| Usługi dla firmy | biura rachunkowe, Klucz (nieruchomości), Ręce do Rożna (praca), Lubelska Szkoła Kebabu | 4 |
| Reklama | Papier Przyjmie (z „Gazetą Pana Cogito”), Fala Koziołka (z „Radiem Tichy”), Lajk, Kozi Gród Events | 4 |
| Informacje o rynku | Redakcja („Kurier rankingowy”), Pracownia Analiz UMCS, Sokole Oko | 3 |
| Zaopatrzenie: hurt i producent | Makro, Selgros, Eurocash, Rożen z Łęcznej; **plan:** Elizówka | 4 + 1 |
| Zaopatrzenie: sklepy | Auchan, Biedronka, Lidl, Stokrotka, Piekarnia Koziołek; **plan:** bazar na Ruskiej | 5 + 1 |
| Wyposażenie i wnętrze | hurtownia sprzętu gastronomicznego, park handlowy (z sklepem meblowym), stolarnia Lada i Syn, Galeria Pod Zegarem | 4 |
| Parki i woda (zdarzenia, plotki) | Ogród Saski, Park Ludowy, Ogród Botaniczny, Park Bronowicki, Park Rury, Błonia, Zalew Zemborzycki | 7 |
| Zabytki i miejsca (tło, bez wnętrz) | Zamek, Brama Krakowska, Wieża Trynitarska, Plac Po Farze, Plac Litewski, CSK, UMCS, KUL, Politechnika, Dworzec Metropolitalny, Arena, lotnisko, Górki Czechowskie | 13 |
| Lokale do wynajęcia i kupna | 19 gotowych, 14 niewyposażonych, 5 działek (po budowie **pawilon z własnym wnętrzem**, decyzja 14.11) | 38 |
| Kebaby na mapie | lokale graczy (wnętrze kebaba) i konkurencji (boty, z zewnątrz) | zależy od gry |
| Ukryte | klub „Pod Złotym Koziołkiem” („Nocna 13”) | 1 |
| Drogi i rzeki (tylko obraz) | 14 dróg z koleją, Bystrzyca | 15 |
| Billboardy | 3 billboardy Fali Koziołka przy rondach (pokazać na mapie, gdy kampania trwa) | 3 |

Razem w danych: 43 budynki, 38 lokali, 13 miejsc orientacyjnych. W planie: Elizówka i bazar.
