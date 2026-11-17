# Pozew symulowany i SWOT – wnioski (14.11.2026)

Streszczenie dwóch analiz z 14.11.2026: symulowanego pozwu (przegląd ryzyka prawnego) i analizy strategicznej (SWOT, TOWS,
ocena planu). Autor obu: agent Fable (model Claude), na zlecenie lidera. To ćwiczenie, a nie porada prawna.
Pełne wersje zawierają nazwy i ścieżki wcześniejszego projektu i innej gry biznesowej, więc leżą poza repozytoriami,
w `archiwum/prawne/` (tylko na dysku szefa). Tu są wyłącznie wnioski, bez nazw.

## Pozew symulowany – co ustalono

Porównano `main`, tor A (PR #2), dane wnętrz i odtworzenie „innej gry biznesowej” zrobione wcześniej przez autora.
- **Kod, teksty, nazwy:** LUKRUM nie ma wspólnych linii kodu ani ścieżek ikon z tą grą, a wspólne zdanie z podręcznika było jedno.
  Zarzut o kod jest słaby, bo wcześniejszy projekt napisał ten sam autor.
- **Liczby były najpoważniejsze:** w `main` pełne tabele katalogów (udogodnienia, wyposażenie, oceny firm szkoleniowych, pakiety
  stanowisk, media, narzędzia internetowe, banki, biura, kandydaci) i ok. 45 stałych modelu zgadzały się z wcześniejszym projektem
  co do wartości; w PR #2 zostało ok. 22 stałych i trzy tabele. Siła zarzutu: mocna co do faktów, średnia co do prawa
  (ochrona zbioru wymaga twórczego doboru, a nakład na wymyślenie danych nie liczy się do ochrony baz).
- **Sposób pozyskania danych** wcześniej: masowe zgranie z konta instruktora innej platformy. To zarzut spoza gry,
  ale obciąża całość i zależy od regulaminu tej platformy, którego nie udało się znaleźć.
- **Zacieranie śladów:** przepisanie opisów źródeł tak, że liczba zostaje, a nazwa źródła znika, wygląda w sporze gorzej
  niż jawne „wzorowane na”.
- **Uproszczone logotypy prawdziwych firm** i nazwy marek: ryzyko średnie, niezależne od tej sprawy; właściciele znaków
  wysyłają wezwania rutynowo.
- **Układ gry** (harmonogram odblokowań, nazwy ekranów, klucze): słaby do średniego; identyczny siedmiostopniowy
  harmonogram najtrudniej wytłumaczyć przypadkiem.
- **Postacie i cytaty z lektur:** słabe ryzyko. Rośnie, gdy postać chronionego autora dostaje własne kwestie i rysunek.
- Pozostałe: fonty (lokalnie, z licencjami), dźwięki (tylko CC0 lub własne), kasyno (domyślnie wyłączone i widoczne
  dla nauczyciela), regulaminy konkursów (oświadczenia o autorstwie).

**Co zrobiono i co zalecono:** własne mechaniki (nowe katalogi, wynik 0–1000 pkt, debet, kadry wg Kodeksu pracy, pomyłki
w szczycie, wujek, popyt z mapy) zmniejszają ryzyko; każda tabela ma mieć w `zrodlo` prawdziwe, sprawdzalne źródło;
zachować historię commitów i surowe pomiary botów jako dowód własnego pochodzenia; nie niszczyć dowodów; lista
kontrolna na kolejny przegląd (stałe wspólne ≥ 3 miejsca po przecinku → 0, brak nazw z dawnej gry w danych, panelu,
instrukcji i PDF, `ikony_marek.js` bez prawdziwych logo, tabela nawiązań literackich, wykaz grafik i fontów).
Do prawnika: regulamin tamtej platformy, los archiwum ze zgranymi materiałami, treść oświadczeń konkursowych,
zasady użycia prawdziwych marek.

## SWOT – co ustalono

- **Mocne strony:** wspólny rynek klasy na mapie prawdziwego miasta; silnik oddzielony od strony, powtarzalny, szybki
  (gra 5 firm na 8 tygodni w ok. 3 s); liczby w danych z polem `zrodlo`; narzędzia nauczyciela (zakrywanie funkcji,
  zegar rundy, refleksje, eksport); treść prawdziwa i lokalna; notatki funkcji gotowe jako półprodukt scenariuszy;
  proces z agentami, który sam siebie sprawdza; lektury jako drugi przedmiot.
- **Słabe strony:** nikt poza autorem nie zagrał (balans tylko z botów); mechaniki toru A uczyły błędów (12 znalezisk
  z przeglądu); `main` w najgorszym stanie prawnym; stary interfejs do wyrzucenia; opisy rozjechane z grą; kolejka
  decyzji u jednej osoby; współpraca z majstrem tylko w jedną stronę; serwer to laptop autora; brak RODO, dostępności
  i telefonu.
- **Szanse i zagrożenia:** konkurs „Zwolnieni z Teorii” i podstawa programowa „biznesu i zarządzania”; nabór
  „Przedsiębiorczej Młodzieży”; zagrożenia: terminy konkursu, regulamin (oświadczenia o AI i autorstwie), zależność od
  jednej osoby, ryzyko prawne marek i danych.
- **Gdzie projekt najpewniej utknie:** między etapem 2 a 3 (granica mapa ↔ wnętrza), w kolejce decyzji autora,
  w pętli przebudowy bez daty pierwszej lekcji, na scaleniu PR #2.
- **Priorytety (10 kroków):** zgłoszenie do konkursu i data pierwszej lekcji; jedna sesja decyzji; dokończenie PR #2
  i wymiana wspólnych katalogów i stałych; rozmowa z majstrem o granicy; wersja „na pierwszą lekcję”; gra próbna
  z 4–6 osobami; nowy wygląd tylko dla tej wersji; pakiet nauczyciela (scenariusze, karta pracy, test przed i po,
  serwer, konta na pseudonimach); rozmowa z prawnikiem; po lekcji: dalsze zgłoszenia, polityka prywatności, dostępność.
- **Pomysły:** test przed i po w grze; role w drużynie przypięte do miejsc we wnętrzu; raport „lucrum cessans” po
  rundzie; prognoza przed rundą; widok na projektor z trzema pytaniami do omówienia.

## Gdzie te wnioski weszły
`Decyzje`, `Do decyzji`, `Plan` (§3), `Historia` oraz `Postęp` w głównych notatkach sejfu. Tabela źródeł liczb: pole
`zrodlo` w `dane/*.yaml`.
