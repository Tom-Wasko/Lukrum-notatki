# Mapa – wszystkie elementy (spis 14.11.2026)

Spis dla [mapa] i [mechaniki]. Źródła: `gra/dane/mapa/budynki.yaml` (43 budynki), `lokale.yaml` (38 lokali),
`miasto.yaml` (13 miejsc, 14 dróg, rzeka), `strefy.yaml` (10 stref). **Plan** = przewidziane, ale jeszcze nie ma w danych.

**Strefa a miejsce.** `strefa` to jednostka popytu w grze, `miejsce` to prawdziwe położenie (tam rysujemy budynek).
Gdzie się różnią, jest znak ⇄ (strefa w nawiasie). Zasada autora: prawdziwe lokalizacje, ale bez tłoku na Starym
Mieście i Krakowskim Przedmieściu.

## 1. Według dzielnic

### Stare Miasto (strefa `stare_miasto`)
- Piekarnia Koziołek (zaopatrzenie)
- Harpagon, lichwiarz ⇄ (dworzec)
- Błonia pod Zamkiem (park, zdarzenia)
- Zabytki: Zamek Lubelski, Brama Krakowska, Wieża Trynitarska, Plac Po Farze
- Lokale: Grodzka 14, Rynek 8, Bramowa 3 (piwnica), Złota 2 (okienko), Kowalska 6 (od rundy 6)
- **Plan:** klub „Pod Złotym Koziołkiem” (ukryty, bez szyldu na mapie, etap 2–3)

### Śródmieście (strefa `centrum`)
- Krakowskie Przedmieście: **kamienica bankowa** (decyzja 14.11). Na mapie jest jeden budynek. Po kliknięciu
  otwiera się kamienica z szyldami, a potem wybiera się bank: Kmicic, Wokulski i S-ka, Ziemia Obiecana,
  Oszczędności Rzeckiego, Soplicowo, Solaris i biuro maklerskie Byk i Koziołek.
- Sanepid (ul. Karłowicza), Poczta Główna, agencja nieruchomości Klucz, redakcja „Kuriera Kebabowego” (ranking)
- Galeria Pod Zegarem, ul. Lipowa (udogodnienia dla załogi)
- Ogród Saski (park) ⇄ (akademickie)
- Zabytki: Plac Litewski, Centrum Spotkania Kultur
- Lokale: Krakowskie Przedmieście 21, Peowiaków 9, Chmielna 4, 3 Maja 12, Okopowa 7 (od rundy 10)
- **Plan:** bazar przy ul. Ruskiej (tanie warzywa, zaopatrzenie)

### Rury, biurowce przy Zana (strefa `lsm_czuby`, część `politechnika`)
- Kamienica biur rachunkowych ⇄ (stare_miasto)
- Agencja reklamy internetowej Lajk ⇄ (akademickie)
- Radio i billboardy „Fala Koziołka” ⇄ (centrum)
- Kozi Gród Events (festyny, degustacje) ⇄ (stare_miasto)
- TUW Pod Koziołkiem (ubezpieczenia) ⇄ (centrum)
- Park na Rurach (park)
- Lokal: Zana 32 ⇄ (politechnika)
- Te 5 firm siedzi w **jednym biurowcu przy Zana** (decyzja 14.11, tak jak kamienica bankowa). Na mapie jest
  jeden budynek. Po kliknięciu otwiera się hol z szyldami, a potem wybiera się firmę.

### Sławinek i Wieniawa (strefa `akademickie`)
- Agencja pracy Ręce do Rożna ⇄ (centrum)
- Biedronka (zaopatrzenie), drukarnia Papier Przyjmie (ulotki, plakaty, „Gazeta Pana Cogito”)
- Pracownia Analiz UMCS (badanie konkurencji)
- Ogród Botaniczny UMCS (park)
- Zabytki: UMCS, KUL
- Lokale: Radziszewskiego 16, Sowińskiego 10, Langiewicza 20, Głęboka 11 (od rundy 8)

### Politechnika, Nadbystrzycka (strefa `politechnika`)
- Lubelska Szkoła Kebabu (szkolenia)
- Zabytek: Politechnika Lubelska
- Lokale: Nadbystrzycka 38, Nadbystrzycka 42

### Dworzec (strefa `dworzec`)
- Detektyw Sokole Oko, nad lombardem (śledzenie konkurencji)
- Zabytek: Dworzec Metropolitalny
- Lokale: pl. Dworcowy 1 (kiosk), Gazowa 4, Młyńska 15 (hala), Kunickiego 40

### Zygmuntowskie (strefa `zygmuntowskie`)
- Auchan (zaopatrzenie), stolarnia Lada i Syn (meble, lady)
- Park Ludowy (park)
- Zabytek: Arena Lublin
- Lokale: Stadionowa 1 (budka), al. Zygmuntowskie 5, **działka** Krochmalna 30

### Czechów i Kalinowszczyzna (strefa `czechow`)
- Urzędy przy Szeligowskiego (ratusz, ZUS, skarbówka) ⇄ (stare_miasto)
- Stokrotka (zaopatrzenie)
- Górki Czechowskie (miejsce widokowe)
- Lokale: Kompozytorów Polskich 8, Paderewskiego 2, **działka** Szeligowskiego 25, budka Kalinowszczyzna 70 (od rundy 4)

### LSM i Czuby (strefa `lsm_czuby`)
- Lidl (zaopatrzenie)
- Lokale: Wileńska 3, al. Jana Pawła II 13, Filaretów 18, **działka** Armii Krajowej 60

### Węglin (strefa `felin` i `lsm_czuby`)
- Sprzęt gastronomiczny ⇄ (felin)
- Park handlowy: Leroy Merlin, IKEA, OBI, Jula, Castorama ⇄ (lsm_czuby)
- **Plan:** sklep meblowy jako osobny budynek obok parku handlowego, z własnym wnętrzem (wózek, kasa z paragonem, dekor)

### Felin i Tatary (strefa `felin`)
- Hurtownie przy Mełgiewskiej: Makro, Selgros, Eurocash
- Park Bronowicki (park)
- Lokale: Doświadczalna 30, Witosa 12, **działka** Mełgiewska 80

### Zemborzyce (strefa `zemborzyce`)
- Zalew Zemborzycki (woda, sezon)
- Rożen z Łęcznej (producent stożków, odbiór od rundy 3)
- Lokale: budka Tymka nad Zalewem (tylko kupno), Krężnicka 10, **działka** Żeglarska 20

### Poza miastem
- Port Lotniczy Lublin (Świdnik), obwodnica S19/S17/S12
- **Plan:** Elizówka, rynek hurtowy (warzywa i owoce w hurcie)

## 2. Według rodzaju

| Rodzaj | Elementy | Ile |
|---|---|---|
| Urzędy | Urzędy przy Szeligowskiego, Sanepid, Poczta Główna | 3 |
| Finanse | 6 banków, Byk i Koziołek (giełda), TUW Pod Koziołkiem, Harpagon | 9 |
| Usługi dla firmy | biura rachunkowe, Klucz (nieruchomości), Ręce do Rożna (praca), Lubelska Szkoła Kebabu | 4 |
| Reklama | Papier Przyjmie (z „Gazetą Pana Cogito”), Fala Koziołka (z „Radiem Tichy”), Lajk, Kozi Gród Events | 4 |
| Informacje o rynku | Kurier Kebabowy (ranking), Pracownia Analiz UMCS, Sokole Oko | 3 |
| Zaopatrzenie: hurt | Makro, Selgros, Eurocash, Rożen z Łęcznej; **plan:** Elizówka | 4 + 1 |
| Zaopatrzenie: sklepy | Auchan, Biedronka, Lidl, Stokrotka, Piekarnia Koziołek; **plan:** bazar na Ruskiej | 5 + 1 |
| Wyposażenie i wnętrze | Sprzęt gastronomiczny, park handlowy, stolarnia Lada i Syn, Galeria Pod Zegarem; **plan:** sklep meblowy | 4 + 1 |
| Parki i woda (zdarzenia, plotki) | Ogród Saski, Park Ludowy, Ogród Botaniczny, Park Bronowicki, Park na Rurach, Błonia, Zalew Zemborzycki | 7 |
| Zabytki i miejsca (tło, bez wnętrz) | Zamek, Brama Krakowska, Wieża Trynitarska, Plac Po Farze, Plac Litewski, CSK, UMCS, KUL, Politechnika, Dworzec Metropolitalny, Arena, Górki Czechowskie, lotnisko | 13 |
| Lokale do wynajęcia i kupna | 28 gotowych i niewyposażonych | 28 |
| Działki | Krochmalna, Armii Krajowej, Szeligowskiego, Mełgiewska, Żeglarska; po budowie **pawilon z własnym wnętrzem** (decyzja 14.11) | 5 |
| Kebaby na mapie | lokale graczy (wnętrze kebaba) i konkurencji (boty, z zewnątrz) | zależy od gry |
| Ukryte | **plan:** klub „Pod Złotym Koziołkiem” | 1 |
| Drogi i rzeki (tylko obraz) | 14 dróg z koleją, Bystrzyca | 15 |
| Billboardy | 3 billboardy Fali Koziołka przy rondach (pokazać na mapie, gdy kampania trwa) | 3 |

Razem: 43 budynki + 38 lokali + 13 miejsc w danych. W planie jest 5 elementów: Elizówka, bazar, sklep meblowy,
klub i pawilon na działce.

## 3. Decyzje 14.11
- [x] Gazeta Pana Cogito i Radio Tichy zostają kanałami drukarni Papier Przyjmie i Fali Koziołka, bez osobnych miejsc
- [x] banki i giełda są w jednej kamienicy przy Krakowskim Przedmieściu: najpierw klik w kamienicę, potem w bank
- [x] 5 firm przy Zana to jeden biurowiec, działa tak samo jak kamienica bankowa

**Dla [mapa]:** w `gra/dane/mapa/budynki.yaml` jest lista `zespoly` (`kamienica_bankowa`, `biurowiec_zana`), a budynki
w środku mają pole `zespol` (main ddb885c, PR #4). Na mapie rysujesz tylko zespół. `lukrum.otworzWnetrze(id_zespolu)`
otwiera hol z szyldami (to robią [mechaniki]). Adres i `geo` dopisz w zespole, nie w budynkach w środku.
