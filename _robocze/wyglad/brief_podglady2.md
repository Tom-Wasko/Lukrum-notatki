# Brief: podglądy 2 – wygląd LUKRUM (etap 1½)

Zrób **jeden samodzielny plik HTML**: `C:\Users\PC\Pulpit\Levas\lukrum\_robocze\wyglad\podglady2.html`.
Nie publikuj go – zrobi to główna sesja. Wszystkie teksty i komentarze w kodzie po polsku.
Niczego nie bierz z folderu Revas ani z obecnego panelu gry.

## Punkt wyjścia
Przeczytaj `podglady.html` w tym samym folderze (pierwsze podglądy). Możesz kopiować z niego kod:
dane mapy `PLAN`, `mapaPlaskaSVG`, rysowanie budynków, `ekranPlansza`, `ekranApka`, `wnetrzeKebab`,
`wnetrzeBank`, lightbox, podsumowanie z kopiowaniem, zapis wyborów w localStorage (try/catch).

Wybory autora po pierwszych podglądach:
- charakter: **połączenie „ilustrowana plansza” (podgląd 1) i „nowoczesna apka” (podgląd 3) z nutką PRL-u**.
  Autor woli planszę, ale nie chce pełnej stylizacji na PRL. Boi się, że gryzłaby się z nowoczesnymi
  funkcjami i przepisami;
- mapa: **płaska z budynkami-ikonami**;
- po kliknięciu budynku: **wejście do środka** (przybliżenie do wnętrza);
- **jasny i ciemny tryb robimy równolegle**. Każdy podgląd ma mieć obie wersje.

Inspiracja autora do wnętrz: **gatunek gier „obsługa klientów przy ladzie”**. Klient podchodzi do lady, mówi
w dymku, czego chce albo co myśli, a gracz reaguje. Bierzemy wyłącznie ten pomysł na mechanikę.
Postacie, grafika, nazwy i układ muszą być nasze, lubelskie, a nie kopia żadnej konkretnej gry.

## Zawartość strony (3 pytania + podsumowanie)

Każde pytanie ma 2–3 opcje z przyciskiem „Wybieram”. Przy wszystkich podglądach jest przełącznik
**Jasny / Ciemny**. Dodatkowo w każdej opcji pokaż oba tryby obok siebie (albo w zakładkach). Używaj tej
samej sceny co wcześniej: Tydzień 3 z 4, Kasa 48 320 zł, kebab na Krakowskim Przedmieściu 12, list od wujka.

### Pytanie 1: Ile PRL-u? (pełny ekran główny 960×540, plansza + apka)
Wspólny układ dla wszystkich opcji:
- czysty, czytelny jak apka (karty, kafelki z liczbami, Inter/Manrope);
- mapa jak plansza: papier, rysowane budynki, płaska z ikonami;
- ciemny tryb to „Lublin nocą”: ciemny granat, świecące okna.

Opcje:
- **A „Szczypta”**: PRL tylko w liście od wujka (maszyna do pisania, pieczątka) i w drobnym znaczku-logo.
- **B „Akcenty”**: to co A oraz:
  - neony nad lokalami na mapie, które w ciemnym trybie świecą;
  - emaliowane tabliczki z nazwami dzielnic;
  - pieczątka „ZATWIERDZONO” po wysłaniu decyzji.
- **C „PRL w środku”**: mapa i interfejs nowoczesne. PRL jest tylko we wnętrzach: lokal po wujku to dawny
  bar mleczny (lastryko, kafelki, menu z literkami wsuwanymi na tablicę).

Oznacz B jako „Polecane”.

### Pytanie 2: Jaką rolę ma wnętrze kebaba? (widok lady z boku, 960×540)
Klienci to nasze oryginalne postacie, proste i płaskie, np.:
- student UMCS z plecakiem;
- emerytka z siatką;
- budowlaniec;
- nastolatka z telefonem.

Opcje:
- **A „Lada z gośćmi”**: klienci po kolei podchodzą do lady i komentują w dymkach to, co policzyła gra,
  np. „Za 24 zł? U konkurencji 19…”, „Najlepszy sos w mieście!”. Decyzje są przypięte do przedmiotów:
  - tablica z menu → ceny;
  - kuchnia → przepisy i jakość;
  - drzwi na zaplecze → grafik i ludzie;
  - biurko → finanse.
- **B „Mini-gra przy ladzie”**: klient zamawia w dymku („duży w bułce, ostry, bez cebuli”). Gracz klika
  składniki w pojemnikach i składa kebaba. Pasek cierpliwości klienta, napiwek i ocena. Gra opcjonalna,
  w godzinach szczytu.
- **C „Klient z propozycją”**: przy ladzie staje ktoś z ofertą albo kłopotem, np.:
  - „Catering dla UMCS, 200 porcji na piątek”;
  - „Sanepid: kontrola w środę”.
  Gracz wybiera jedną z dwóch kart odpowiedzi i widzi skutki (kasa, ocena, nastrój).

Oznacz A jako „Polecane”. Opcje A i C da się łączyć, napisz o tym w opisie.

### Pytanie 3: Jak wchodzimy do środka?
- Animowany podgląd przejścia **mapa → budynek → wnętrze**, zrobiony w CSS/SVG:
  - przybliżenie do budynku;
  - drzwi się otwierają;
  - wnętrze się pojawia;
  - przycisk „← Wróć na mapę”.
  Uwzględnij `prefers-reduced-motion`.
- Pokaż dwie wersje: **A „płynne przybliżenie”** i **B „szybkie przejście”** (zaciemnienie, jak zmiana
  sceny).
- Pod spodem dodaj miniatury wnętrz innych budynków w tym samym stylu, jasne i ciemne:
  - bank Soplicowo: okienko kasjera, portret Kościuszki, zegar „od 1811”;
  - hurtownia: regały, wózek, kartka z cenami;
  - biuro J.K.Ś.: segregatory, wieszak z kapeluszem.

### Podsumowanie
Tak jak w `podglady.html`:
- lista wyborów;
- pole „Uwagi”;
- przycisk „Kopiuj do schowka”;
- tekst zaczynający się od „Wygląd LUKRUM 2 – wybory:”;
- localStorage pod kluczami `lukrum-wyglad2` i `lukrum-wyglad2-uwagi`.

## Zasady techniczne
- Na początku pliku `<meta charset="utf-8">` i `<title>Wygląd LUKRUM 2</title>`.
- Fonty tylko z Google Fonts. Skrypty tylko inline, bez zewnętrznych bibliotek.
- Kolory jako zmienne w `:root`. Ciemny tryb ma działać na trzy sposoby:
  - `@media (prefers-color-scheme: dark)` z `:root:not([data-theme="light"])`;
  - `:root[data-theme="dark"]`;
  - przełącznik na stronie ustawiający `data-theme`.
- `body` ma jawne tło.
- Strona działa na szerokości telefonu: margines 16px, bez poziomego przewijania.
- Uwaga na pułapkę z pierwszych podglądów: element z atrybutem `hidden` i z `display:grid` w CSS był
  widoczny. Dodaj regułę `[hidden]{display:none!important}`.

## Sprawdzenie przed oddaniem
1. Wytnij skrypt i uruchom `node --check`.
2. Zrób zrzut w Chrome bez okna:
   `"/c/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu
   --user-data-dir=<scratch>/chr --virtual-time-budget=4000 --window-size=1300,5000 --screenshot=<scratch>/p2.png
   "file:///C:/Users/PC/Pulpit/Levas/lukrum/_robocze/wyglad/podglady2.html"`
   Obejrzyj go. Najwyżej 2 zrzuty na poprawkę, w tym jeden w ciemnym trybie (dopisz `#ciemny` do adresu
   i obsłuż to w kodzie).
3. Na koniec zwróć 5–8 zdań: co jest na stronie, co sprawdziłeś, co mogło wyjść słabiej.
