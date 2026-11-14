# LUKRUM – samodzielna praca Fable (od wieczora 15.11 do 16.11.2026 15:50)

## Cel
O 16:00 17.11 autor ma mieć **gotową grę**: drużyny licealistów przechodzą w przeglądarce całą grę od pierwszej do ostatniej
rundy, na mapie Lublina, z wnętrzami, instrukcją i panelem mistrza gry. To eksperyment: autor chce
zobaczyć, ile ulepszysz bez nadzoru. Masz **pełną swobodę**: wdrażaj ustalone rzeczy, wymyślaj nowe funkcje, przebudowuj
istniejące, a jeśli uznasz, że gra na tym zyska, zmieniaj nawet **fundamentalne zasady gry** (punkty, rundy, balans, ekrany,
mapę kolegi – autor się na to zgodził). Nie pytaj, tylko decyduj. Niedokończone końcówki dopnie później Opus, więc lepiej
więcej dobrych funkcji niż perfekcyjnie wygładzona jedna – ale **każda zmiana musi być świetnie opisana** (niżej).

**Najważniejsze: dokumentacja do wybierania.** Jeśli autorowi coś się nie spodoba, ma móc wziąć tylko wybrane zmiany i dodać
je do oryginalnego LUKRUM. Dlatego każda funkcja albo zmiana zasady to osobna, samodzielna gałąź-temat i osobne commity,
z pełnym opisem w katalogu zmian (sekcja „Dziennik i raport”).

**„Gotowa” znaczy:**
1. Pełna gra pokazowa (`manage.py gra_pokazowa`) przechodzi wszystkie rundy bez błędów w konsoli i w logach serwera.
2. Każdy budynek z mapy da się otworzyć i coś w nim zrobić, albo jest uczciwie oznaczony jako „wkrótce”.
3. Instrukcja gracza i MG opisuje obecne mechaniki (nie stare z Levasa).
4. Wszystko w trzech paletach × jasny/ciemny jest czytelne, także w palecie wysokiej widoczności.
5. Uczeń rozumie po 10 minutach, co ma robić (pierwsza runda prowadzi za rękę).

## Na start (przeczytaj)
- `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\BRIEF_AGENTA.md`: zasady kodu, Python, testy, zrzuty. Obowiązują Cię, z wyjątkiem
  zakazu commitów (Ty commitujesz, zasady niżej).
- `lukrum/notatki/`: `PLAN_PRZEBUDOWY.md`, `WSPOLPRACA.md`, `Do decyzji.md`, `Wygląd.md`, `Mapa – elementy.md`, `Funkcje/`.
- Zaległa kolejka (ustalone przez autora, nie zrobione): w „Do decyzji” punkty `[x]` z dopiskiem „Do zrobienia” oraz pamięć
  koordynatora: panel i instrukcja dla kontroli PIP, opłaty za zmianę biura i przejęcia debetu; katalogi przeliczone od zera
  (ceny mają zmuszać do wyboru: ★★★ wyraźnie droższe od ★; priorytet rozgrywka, podatki i przepisy prawdziwe); nazwy ekranów
  w duchu mapy, bez zgadywania (np. „Kurier rankingowy”); harmonogram odblokowań; sklep meblowy z wnętrzem (wózek, kasa,
  paragon); pawilon na działce z wnętrzem; hol kamienicy bankowej i biurowca przy Zana; dekor 900–3 200 zł, próg 40% (z pomiarem);
  lekcje: 2–3 rundy na żywo, dalej między lekcjami.

## Twarde zasady (bez wyjątków)
- Gałąź główna Fable: `fable`, od `main` po scaleniu mapy (15.11), w worktree `lukrum/_robocze/fable`. Jeśli jej nie ma,
  utwórz: `git worktree add ../_robocze/fable -b fable main`. Od `fable` możesz robić własne gałęzie tematyczne
  (`fable/<temat>`) i scalać je do `fable`. **`main` jest nietykalny: nie commituj, nie scalaj, nie pushuj na main, nic na FTP.**
  Push `fable` i `fable/*` na GitHub co kilka commitów (kopia zapasowa).
- Agenci: najwyżej 3 naraz, na Sonnecie, do jasno opisanych zadań; większość pracy i myślenia robisz sam. Agent pracuje
  na swojej gałęzi `fable/<temat>`, Ty przeglądasz i scalasz.
- Commit: `git -c user.name=Tom-Wasko commit`, **bez** Co-Authored-By, Claude-Session i „Generated with Claude Code”.
- Commit małymi krokami: jedna rzecz, testy dotkniętych plików na zielono, krótki opis po polsku. Pełny pytest
  przynajmniej co 3–4 commity i na końcu. Nigdy nie zostawiaj gałęzi z czerwonymi testami. Testów nie osłabiaj.
- Nic z folderów `Levas/_archiwum` (w tym `revas_26`) ani z gry REVAS: ani tekstów, ani liczb, ani nazw, ani układu ekranów.
  Nie ruszaj `Levas/levas_gra` ani `Levas/notatki`.
- Liczby gry tylko w `dane/*.yaml` (`{wartosc, pewnosc, zrodlo}`); zmiana balansu = pomiar przed/po (`balans.symuluj`).
- Teksty po polsku, neutralne płciowo; nawiązania literackie mile widziane (jak banki i biura).
- Mapę kolegi możesz zmieniać jak resztę gry; każdą zmianę mapy opisz też krótko w `WSPOLPRACA.md` (dziennik), żeby kolega wiedział.
- Dane osobowe autora (e-mail itp.) nigdzie poza gitem.

## Jak pracujesz
1. Zacznij od 30-minutowego przeglądu: przejdź grę pokazową jak uczeń (zrzuty), wypisz w `_robocze/fable/PLAN.md`
   listę braków i pomysłów z oceną (wartość dla ucznia × koszt). Kolejność wybierasz sam, ale najpierw to, co blokuje
   „gotową grę”, potem ulepszenia, na końcu dodatki.
2. Pomysły autorskie: śmiało, bez ograniczeń. Każdy ma być do wzięcia osobno: własna gałąź `fable/<temat>`, możliwie mało
   zależności od innych tematów (a jeśli są, wypisz je w katalogu zmian), przy mechanikach przełącznik w yaml, gdy to rozsądne.
   Zmiana balansu albo zasad = pomiar przed/po (`balans.symuluj`, wyniki w `_robocze/fable/pomiary/`).
3. Sprawy, które naprawdę wymagają autora (prawo, pieniądze, nazwy marek), zapisz w `Do decyzji.md` z 2–3 wariantami,
   wybierz rozsądny domyślny i jedź dalej.
4. Każda nowa lub przerobiona funkcja: notatka w `notatki/Funkcje/` (szablon `_Szablon funkcji.md`); notatki commituj
   w repo notatek (też jako Tom-Wasko, bez dopisków).
5. Ok. 2/3 czasu (około 9:00 16.11): **zespół pozywający LUKRUM** – przegląd wszystkiego z nocy pod kątem śladów REVAS,
   praw autorskich, marek i błędów prawnych (jak `_robocze/pozew-revas-fable.md`); raport do `_robocze/fable/pozew-2.md`,
   poprawki drobnych rzeczy.
6. Od 15:00: koniec nowych rzeczy. Pełny pytest, ruff, `silnik.dane sprawdz`, push gałęzi, raport końcowy.

## Dziennik i raport
- `_robocze/fable/DZIENNIK.md`: godzina, commit, co i dlaczego, „decyzja Fable” albo „ustalone przez autora”.
- **Katalog zmian** `_robocze/fable/ZMIANY.md` (najważniejszy plik nocy), jeden wpis na temat:
  nazwa, gałąź `fable/<temat>` i zakres commitów (`git log fable/<temat>` / hashe), co gracz widzi, co zmieniono w
  zasadach, pliki, zależności od innych tematów, wynik pomiaru, notatka w `Funkcje/`, ocena Fable (pewne / do sprawdzenia),
  **jak wziąć do main** (np. `git cherry-pick a1b2..c3d4` albo `git merge fable/<temat>`, możliwe konflikty).
- Raport końcowy `_robocze/fable/RAPORT.md` (do 2 stron): stan względem 5 punktów „gotowej gry”, ranking tematów od
  najbardziej wartych wzięcia, co jest niedokończone (dla Opusa), otwarte decyzje autora, 3–5 zrzutów najważniejszych ekranów.
- `_robocze/` jest poza gitem: na koniec skopiuj `PLAN.md`, `DZIENNIK.md`, `ZMIANY.md`, `RAPORT.md` i `pozew-2.md` także do
  gałęzi `fable` (folder `fable_noc/` w repo), żeby były na GitHubie.
