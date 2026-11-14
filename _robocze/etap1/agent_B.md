# Agent B – raport (silnik, dane, testy)

Stan końcowy: grep z briefu w moich plikach = 0 trafień. `silnik.dane sprawdz` OK, `ruff check .` OK.
Pełny pytest: 578 passed, 4 failed, 2 errors – dokładnie 6 znanych testów zależnych od kolejności (patrz niżej), nic nowego.

## Zmienione pliki
- **Dane (`dane/` i kopie w `testy/dane_zamrozone/`, tylko teksty, liczby bez zmian):** `zalozenia.yaml`, `katalog.yaml`, `boty.yaml`,
  `kandydaci.yaml`, `uslugi.yaml`, `zasoby.yaml`, `sprzet.yaml`, `podatki_2026.yaml`, `mapa/{biura,klienci,popyt,promocje,reklama}.yaml`
  (pola `zrodlo`, `opis`, komentarze przepisane na „założenie autora”, „kalibracja pomiarami botów (balans/)”, cennik, ustawa o PIT itd.).
  Kopie zamrożone mają inną treść niż żywe (np. brak `hr_zatrudnienie` w tygodniu 1), więc zamieniałem teksty tą samą listą podmian, nie kopiowałem plików.
- **`pewnosc`:** `potwierdzone` zostało tylko tam, gdzie jest realne źródło: `placa_minimalna` (rozporządzenie, 4806 zł 2026), `amortyzacja_prog`
  (ustawa o PIT, 10 000 zł). Zmienione na `zalozenie`: `zaokraglenie`, `zajecia_zaokraglane_w_gore`, `sprzedaz_udogodnien`, `lokata_odsetki`,
  `kredyt_odsetki`, `kredyt_odnawialny_automatyczny`, `zus_pracodawcy`; na `skalibrowane`: `model_stanowisk`. Wartości nietknięte.
- **Nazwy własne w katalogu** (nazwy nie są kluczami, nic poza katalogiem i `boty.yaml` ich nie używa; testy też nie):
  banki: Bank Pod Bramą, Kasa Bystrzyca, Bank Zalew, Bank Kalinowy, Bank Wieniawski, Bank Lubartowska;
  biura: Biuro Rachunkowe Sumator / Abakus / Bilans / Liczydło / Grodzka / Saldo;
  media: Kurier Staromiejski (dziennik), Dziennik Bystrzycki (dziennik), Radio Czechówka, Radio Wieniawa (Radio Fakty także w `boty.yaml`);
  narzędzie: „Księga Firm Lubelskich” (zamiast Panorama Firm). Proszę autora o rzut oka na nazwy.
- **Kasyno** (`dane/zdarzenia/kasyno.yaml` i kopia): `nazwa: „Pod Złotym Koziołkiem”`. `kod_od_rundy: 1` z komentarzem. UWAGA: kopia zamrożona
  w ogóle nie ma pola `kod_od_rundy` (była starsza), więc tam zmieniła się tylko nazwa; pola nie dodawałem, bo to zmiana danych mechaniki.
- **Kod/komentarze (`silnik/`, `api/`, `lukrum/`, `manage.py`, `panel_gracza/*.py`, `management/`, `pyproject.toml`):** usunięte odwołania do
  REVAS/ATH/A-B-C/Apex/Vela/dashboard, „Levas” → „LUKRUM”, `WIEDZA_O_GRZE.md` → `OPIS_GRY.md` albo własne słowa (`finanse.py`, `operacje.py`),
  opis w `pyproject.toml` i komentarz ruff („Starszy kod”). Przy okazji słowo „klub” w znaczeniu fitness zamienione na „firma”
  (`operacje.py`, `karta.py`); „klub” jako tajne kasyno zostaje. Komentarz `model.py` „instruktor/trener” → „kucharz albo kasa”.
  Drobiazg: w `lukrum/settings.py` zawinąłem dwa za długie komentarze (E501, ruff by inaczej padał).
- **Testy (komentarze/nazwy):** `test_api`, `test_ksiegowosc`, `test_srodki_trwale`, `test_czas_wlasciciela`, `test_zadowolenie`, `test_harmonogram`
  (zmienna `revas` → `bazowe`), `test_mechaniki`, `test_popyt`, `test_reklama`, `test_karta`; `test_kasyno.py`: krotka `SLADY` ma „Złotym Koziołkiem”.
  Test `test_haslo_otwiera_drzwi_bez_zaproszenia` sam ustawia `kod_od_rundy = 2` przez monkeypatch, więc dalej sprawdza to samo (przed terminem
  drzwi zamknięte, po terminie otwarte); nie wymagał zmiany. Żaden test `testy/aplikacja/*` nie sprawdzał starego nagłówka „Levas Kebab”.

## Martwy kod trybu REVAS
Nie jest martwy w całości: `lokale.tryb_lokali(dane, konfiguracja)` (mapa w danych + flaga `lokale` w konfiguracji) jest używana w `runda.py`,
`harmonogram.py`, a `gra.py` sprawdza `konfiguracja.get("lokale")`. Wiele testów buduje konfiguracje bez tej flagi, więc usunięcie byłoby zmianą
zachowania. Zrobiłem tylko: komunikaty błędów w `gra.py` i `runda.py` bez słowa REVAS („Gra bez lokali nie jest obsługiwana”), komentarz przy
`"lokale": True`. Propozycja na później: usunąć `tryb_lokali`, flagę `lokale` i gałęzie „bez lokali” razem z poprawką testów (osobne zadanie).

## Kasyno: czego API oczekuje od JS (`kasyno.js`, agent C)
- Hasło „koziol” nie jest sprawdzane po stronie serwera; `silnik/pieniadze/kasyno.py::drzwi` i `api/prezentacja.py` nie mają innej blokady (stan funkcji,
  runda): przy `kod_od_rundy: 1` drzwi są otwarte od rundy 1 dla każdej firmy w grze z kasynem (serwer `LUKRUM_KASYNO=1`, MG go nie widzi).
- Widok firmy (`/api/gry/<id>/widok/<firma>`) zawiera więc klucz `kasyno` z `otwarte: true`, `klub` (nazwa, tekst), `gry`, `limity`, `decyzja`
  już od rundy 1. JS ma pokazywać zakładkę tylko po wpisaniu „koziol” w tej przeglądarce albo gdy `kasyno.zaproszenie` nie jest `null`
  (obecnie to robi `HASLO` w `kasyno.js`, `app.js`); sam obecny klucz `kasyno` nie może już oznaczać „zakładka widoczna”. Zakłady idą w decyzjach
  jako `kasyno: [{gra, zaklad, stawka}]`.
- Zmiana wymaga zgody autora: skoro dane są w widoku od 1. rundy, uczeń z podglądem JSON może zobaczyć kasyno bez hasła (do tej pory od 4. rundy).

## Testy zależne od kolejności: przyczyna
`testy/aplikacja/test_staly_link.py` (test `hostuj`, ok. linii 156) uruchamia `call_command("hostuj")`, a ta komenda zapisuje na globalnych
ustawieniach (`panel_gracza/management/commands/hostuj.py`, ok. linii 86–89): `ALLOWED_HOSTS.append`, `CSRF_TRUSTED_ORIGINS`, `SECURE_PROXY_SSL_HEADER`, `DEBUG`.
Test zabezpiecza przez `monkeypatch.setattr(settings, "ALLOWED_HOSTS", …)` tylko jedno pole, a undo monkeypatcha i fixture `settings` z pytest-django
kończą się w złej kolejności, więc `settings._wrapped` zostaje z uszkodzonym `UserSettingsHolder` (`AttributeError` na `ALLOWED_HOSTS`) i
wszystkie późniejsze testy z `client` padają. Odtworzone: `pytest testy/aplikacja/test_staly_link.py testy/swiat/test_zdarzenia.py::test_widok_api`.
Zweryfikowana poprawka (potem cofnięta, zgodnie z briefem): zamiast monkeypatcha przypisać przez fixture `settings` wszystkie cztery pola przed
`call_command` (`for n in (...): setattr(settings, n, <ta sama wartość, dla ALLOWED_HOSTS kopia listy>)`), wtedy teardown fixture przywraca stan
i oba testy przechodzą razem (10 passed). Nie dotyczy 6 błędów po jednym: pochodzą od tego jednego testu.
