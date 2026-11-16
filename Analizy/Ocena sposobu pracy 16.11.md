# Ocena sposobu pracy szefa z AI (16.11.2026)

Recenzja świeżym okiem (Opus, tylko odczyt). Podstawa: AGENTS.md, LIDER.md, Dziennik lidera, Sprawozdanie, definicje
agentów, pamięć lidera (23 pliki), plan porządków (wstęp, e, g), krytyka wnętrz (a), raport researchu, [[Pozew i SWOT – wnioski]],
historia gita. Uwaga: ta ocena to też praca Opusa „o procesie”, a o tę kategorię prac chodzi w kilku zarzutach niżej.

## 0. Werdykt w trzech zdaniach
Sam sposób delegowania jest dobry i ponadprzeciętny: pytania z opcjami, briefy z granicami, dowody, akceptacja szefa.
Problem leży gdzie indziej. **Produkcja dawno przegoniła sprawdzanie przez ludzi**: przez trzy tygodnie powstało ok. 525
commitów (427 w wcześniejszym projekcie, 98 w LUKRUM w 4 dni), ale nikt poza szefem nie zagrał (SWOT 14.11). Do tego od 16.11 po
południu cała energia idzie w proces o procesie: research, plan porządków, krytykę, ocenę, warsztat i panel.
Następny krok to więc mniej organizacji, a pierwsza lekcja z uczniami.

## 1. Co działa i warto utrzymać
- **Pytania z opcjami i rekomendacją.** Zmuszają do decyzji zamiast mglistych życzeń. Szef czyta dokładnie („1 oraz 3”),
  a decyzje są spisane z datą. To najlepsza część całego układu.
- **Brief = zakres i pozwolenie, „gotowe = dowód”, raport w stałym formacie.** Bezpośrednia odpowiedź na noc Fable
  i fałszywe „gotowe”, zgodna z tym, co zaleca Anthropic (raport researchu, rozdz. 5).
- **Dobór modelu do zadania** (Haiku do zwiadu, Sonnet do wykonania, Opus rzadko), jawny `model` i `effort` w definicjach.
- **Worktree na agenta, rozłączne pliki, scalenie po akceptacji.** `main` jest chroniony przed eksperymentami.
- **Stan w plikach** (LIDER.md §8, „Stan prac”). Przy częstych limitach i zmianach konta to konieczność.
- **Architektura gry**: liczby w YAML z polem `zrodlo`, test pilnujący braku liczb w silniku, 740 testów. Dzięki temu
  balans i wersje pod lekcję zmienia się bez kodu.
- **Krytyczne oko na siebie**: symulowany pozew, przegląd prawny, krytyka świeżym okiem. Rzadkie i cenne.

## 2. Co jest ryzykowne lub marnotrawne
**Jakość gry i gotowość na konkurs.**
- Zero graczy-ludzi. Balans jest „z botów”, a „gra testowa” jest odkładana od wcześniejszego projektu (PLAN_PRZEBUDOWY, SWOT). Zwolnieni
  z Teorii nagradzają przeprowadzone zajęcia i liczbę odbiorców, nie jakość aplikacji (SWOT 14.11; termin końcowy
  31.03.2027). Każdy tydzień bez lekcji to ryzyko większe niż jakikolwiek bałagan w plikach.
- Funkcje rosną szerzej niż głębiej: sklep meblowy, dekor, księga gości, kasyno, lektury, oświetlenie mapy od Słońca.
  Tymczasem krytyka mówi: „jedno prawdziwe wnętrze i osiem poczekalni”, scena nie jest miejscem decyzji.
- Terminy się rozjeżdżają: „gra gotowa 17.11 o 16:00” (pamięć 14.11), „bez terminu” (dziennik 16.11), rejestracja ZwzT
  „do 16.11 (do potwierdzenia)” (pamięć 6.11). Nikt tego nie rozstrzygnął na piśmie.

**Szef jako wąskie gardło.** Na rano 17.11 czekają: plan porządków (394 linie + 29 szkiców, 8 pytań), krytyka (418 linii,
59 zrzutów, 16 pytań), research, ta ocena, przeprowadzka folderu o 6:00 i start nowego lidera. Licealista przed lekcjami
tego rzetelnie nie przeczyta, więc w praktyce kliknie rekomendacje. Wtedy pytania z opcjami tracą sens.

**Tokeny i koszty.**
- Jednego wieczoru szły równolegle dwa Fable, Sonnet i Opus `high`, wszystkie tylko czytające i wszystkie „o procesie”.
  Limit przerwał obu Fable naraz.
- Nikt nie mierzy, która seria ile zjadła (LIDER.md §7 każe sprawdzać `/usage`, ale w dzienniku nie ma żadnej liczby).
- Pamięć lidera ma 23 pliki, a większość dotyczy wcześniejszego projektu (B6, poprawki 2–4, ufajnianie, FTP). Indeks ładuje się przy
  każdym starcie, a `uzytkownik.md` wciąż mówi o konkursie wcześniejszego projektu.

**Kilka źródeł zasad, które sobie przeczą.**
- `strategia-poprawek` („ZAWSZE”) wskazuje ścieżki wcześniejszego projektu, `BRIEF_AGENTA.md` i `?motyw=stary`.
- `agenci-sonnet` mówi „Opus tylko gdy Sonnet nie da rady”, a dziś Opus i Fable robią recenzje.
- LIDER.md każe commitować `plan.md`, a `.git/info/exclude` go ignoruje (plan porządków, uwaga 1).
- Ten sam zestaw zasad żyje w AGENTS.md, w definicjach agentów i w pamięci.

**Rozjazd z majstrem.**
- Dziennik daje agentom lidera prawo zmieniać mapę „bez ograniczeń”, a WSPOLPRACA mówi „PR przeglądany przez drugą stronę”.
- Plan spłaszcza repo, choć majster pracuje na `maciex` w starym układzie (ryzyko 2).
- Raporty agentów mają trafić do jego sejfu notatek (pytanie 4).
- Majster podpisuje commity „nie podam”, więc w historii nie widać jego wkładu.
- Wszystko to decyduje szef, a majster dowiaduje się z wpisu w dzienniku.

**Czego szef się uczy.**
- Uczy się dużo i rzeczy cennych: precyzji wymagań, decyzji pod niepewność, prawa podatkowego, kierowania pracą.
- Nie uczy się działania własnej gry: „autor nie wymyśla wzorów, tylko wybiera z propozycji” (pamięć `lukrum`).
  Badanie Anthropic z raportu researchu: pełna delegacja daje najsłabsze rozumienie.
- Jury i kapitan zapytają „dlaczego zysk spadł w tygodniu 4?” albo „jak liczycie VAT?”. Odpowiedź „agent tak zrobił” zabije projekt.

**Odbiór przez kapitana i jury.**
- Historia gita przypisuje cały kod szefowi, a zasady wprost zabraniają śladów AI.
- Przy produkcie, który w ~95% napisali agenci, to tykająca bomba. Wystarczy pytanie o kod albo porównanie tempa
  (59 commitów szefa 16.11, w tym rano kilkadziesiąt scaleń Fable).
- Tymczasem jawnie opisana metoda („uczeń prowadzi zespół agentów AI, decyduje, testuje i odpowiada za treść”) jest
  atutem. Ślady pochodzenia z wcześniejszego projektu i otwarta rozmowa z prawnikiem (plan, pytanie 2) dokładają powód, żeby wszystko było
  przejrzyste.

## 3. Czy szef → lider → agenci to przerost formy?
**Sama trójka nie.** To w praktyce jedna sesja, która zleca zadania i sprawdza wyniki. Przy grze w Django i JS, robionej
przez nieprogramistę, kontrola dowodów i rozłączne gałęzie są uzasadnione. Taki układ jest też zgodny z raportem researchu.

**Przerostem jest warstwa wokół trójki, w tej chwili.**
- Pliki o procesie: AGENTS.md, LIDER.md, Sprawozdanie, Dziennik, research, ocena, plan porządków z 10 krokami
  i planem B, warsztat jako osobne repo, panel na claude.ai.
- Do tego nazwy ról (majster, kapitan) w dokumentach agentów, które tych ludzi nie potrzebują.
- Po scaleniach Fable 16.11 o 12:55 po stronie szefa nie przybyła ani jedna zmiana w grze. Popołudnie i noc poszły
  w organizację.

Test, który warto sobie zadawać: czy ta rzecz przybliża pierwszą lekcję z uczniami? Jeśli nie, poczeka.

## 4. Zmiany (od najważniejszej)
1. **Gra testowa z ludźmi w ciągu 7–10 dni, na obecnym `main`, a do tego czasu bez nowych funkcji.**
   - Plan: kapitan i 4–8 uczniów, zestaw „Pierwsza gra”, 2–3 rundy, stoper, kartka „co było niejasne”.
   - Uzasadnienie: to jedyny brakujący dowód, a konkurs ocenia zajęcia.
   - Koszt: jedna lekcja i jedna sesja lidera na przygotowanie (Sonnet: lista kontrolna i instrukcja MG). Oszczędza wiele serii funkcji.
2. **Jedna strona „Cel i termin” uzgodniona z kapitanem.**
   - Treść: co i kiedy oceniają ZwzT, data pierwszej lekcji, definicja „wersji na pierwszą lekcję” (lista ekranów, które muszą działać).
   - Uzasadnienie: dziś są trzy sprzeczne terminy, a seria bez związku z tą listą idzie do „później”.
   - Koszt: 30 minut rozmowy i jedna strona w notatkach.
3. **Porządki wąsko i bez spłaszczania repo teraz.**
   - Zrobić tylko to, co jest potrzebne: usunąć ślady starej nazwy i gry, raporty do notatek, `_robocze` na czysto.
   - Spłaszczenie (20 punktów zmian, konflikt z `maciex`) przesunąć na moment uzgodniony z majstrem albo z niego zrezygnować.
   - Koszt: decyzja szefa. Oszczędność: dzień pracy i ryzyko zepsucia środowiska.
4. **Budżet czytania szefa.**
   - Na dzień najwyżej jedna strona „do decyzji”, najwyżej 8 pytań, a raport agenta dla szefa ma najwyżej 1 stronę (dłuższe tylko dla lidera).
   - Krytykę (16 pytań) i plan (8) lider łączy w jedną listę z rekomendacjami i zaznacza 3–5 spraw, w których zdanie szefa naprawdę coś zmienia.
   - Koszt: kilka linii w LIDER.md §6.
5. **Jawność AI wobec kapitana i jury.**
   - Notka „Jak powstał LUKRUM”: kto projektował i decydował, kto pisał kod, jak sprawdzano.
   - Sprawdzić regulamin ZwzT pod kątem AI.
   - Rozważyć zgodę na dopisek o AI w commitach albo przynajmniej plik `METODA.md` w repo.
   - Koszt: około godziny. Ryzyko odwrotne (wyjdzie samo) jest dużo droższe.
6. **Szef musi umieć obronić grę.**
   - Po każdej serii lider zadaje 3 pytania sprawdzające („dlaczego tak, co się zepsuje, jak to sprawdzić”), jak w raporcie researchu, punkt 6.
   - Raz w tygodniu szef tłumaczy jedną mechanikę od danych do wyniku bez notatek.
   - Koszt: 20–30 minut tygodniowo. To też najlepsze przygotowanie do jury.
7. **Jedno źródło zasad i czysta pamięć przy przeprowadzce 17.11.**
   - Do nowej pamięci przenieść tylko: commity, rolę szefa, odsyłacz do Dziennika i LIDER.md.
   - Pliki o wcześniejszym projekcie zarchiwizować.
   - `strategia-poprawek` i `agenci-sonnet` wchłonąć do LIDER.md.
   - `uzytkownik.md` poprawić: ZwzT zamiast wcześniejszego konkursu.
   - Koszt: 30 minut, okazja i tak jest.
8. **Ustalenia z majstrem twarzą w twarz, nie przez dziennik.**
   - Do ustalenia: kto może ruszać mapę (cofnąć „bez ograniczeń” albo wpisać to do WSPOLPRACA za jego zgodą), kiedy spłaszczenie, czy raporty w jego sejfie.
   - Prośba: commity pod prawdziwym nazwiskiem (jego wkład liczy się w konkursie).
   - Koszt: 15 minut rozmowy.
9. **Mierzyć koszt, nie czuć.**
   - W „Stan prac” jedna kolumna: model, przybliżone zużycie limitu, czy wynik wszedł do gry.
   - Bez Fable od 17.11 Sonnet jest domyślny, Opus rzadko.
   - Zasada: najwyżej jedna duża praca tylko do odczytu („o procesie”) na tydzień.
   - Koszt: jedna linia na serię.
10. **Warsztat i panel po pierwszej lekcji.**
    - Do tego czasu panelem jest `STAN.md` albo „Stan prac” (tak radzi też research, punkt 8).
    - Osobne repo `warsztat` założyć dopiero, gdy zacznie się drugi projekt. Wtedy będzie wiadomo, co jest ogólne, a co tylko LUKRUM.
    - Koszt: ujemny, to oszczędność.

## 5. Szablon „warsztat”: co wziąć, czego nie
**Wziąć:**
- krótki AGENTS.md dla agenta (brief = zakres, dowód, raport w stałym formacie, „po 2 próbach stop”);
- szablon briefu z ogrodzeniem plików i binarnym warunkiem końca;
- trzy definicje agentów z jawnym `model` i `effort`;
- regułę rozłącznych plików i worktree na agenta piszącego;
- plan B „stan w plikach” i plik stanu z hashem commita;
- Dziennik: decyzje, wybory lidera i pytania do szefa, z regułą „idź dalej tylko tam, gdzie da się cofnąć”;
- rundy pytań z rekomendacją;
- `_robocze/` z obowiązkowym sprzątaniem po serii;
- zasadę „liczby w danych, test tego pilnuje” (ogólna, nie tylko dla gier).

**Dodać, bo dziś tego brakuje:**
- **bramka użytkownika**: żadna seria funkcji bez kontaktu z prawdziwym odbiorcą co N serii;
- strona „cel i termin”;
- budżet czytania szefa;
- pytania sprawdzające rozumienie;
- licznik kosztu.

**Nie brać:**
- nazw i ról specyficznych dla LUKRUM (majster, kapitan, palety PRL, kebab), które należą do `CLAUDE.md` projektu;
- wierszy o Fable i dat okresów próbnych;
- reguły „autor commitów tylko X, bez śladów AI”: to decyzja projektu, i to dyskusyjna (punkt 5);
- liczb 4×/15×/90% jako dogmatu (dotyczą wyszukiwania, nie kodu);
- sztywnego „5 agentów, 3 piszących” (zależy od komputera i limitu);
- nocnych prac bez limitu kosztu;
- panelu jako aplikacji przed pierwszą potrzebą;
- pamięci Claude jako źródła zasad: zasady mają żyć w plikach repo, które czyta każdy lider i każdy agent.
