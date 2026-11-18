# Rejestr agentów

Prowadzi lider: wiersz przy zleceniu, uzupełnienie po zakończeniu (tokeny i czas z powiadomienia agenta, wynik z raportu).
Panel postępu ([[Dziennik lidera]], strona na claude.ai) pokazuje tę tabelę w sekcji „Agenci”. Pole „Postęp” wypełnia
lider tylko wtedy, gdy agent prowadzi `STAN.md` albo raport cząstkowy (np. „3/7 punktów briefu”).

| Agent | Model | Zlecenie | Stan | Postęp | Tokeny (tys.) | Czas (min) | Wynik |
|---|---|---|---|---|---|---|---|
| pulpit-powloka | Sonnet | seria pulpit, krok 1: powłoka ekranu (mapa na cały ekran, pasek, portfel, zeszyt) | pracuje | – | – | – | gałąź `pulpit-powloka`, raport `_robocze/pulpit-powloka-raport.md` |
| research ZwzT | Sonnet | regulamin konkursu a AI | gotowe | – | 70 | 2 | `Analizy/Regulamin ZwzT a AI.md` (regulaminu 2026/27 nie udało się pobrać) |
| porządki 13B | Sonnet | odchudzenie notatek: korzeń i Dziennik | gotowe | – | 206 | 7 | `notatki` 9107479 |
| porządki 13A | Sonnet | odchudzenie notatek: Serie, Analizy, Funkcje | gotowe | – | 169 | 4 | `notatki` 9107479 |
| mapa notatek | Haiku | przeczytanie wszystkich notatek, propozycje zmian | gotowe | – | 302 | 6 | lista „zostaje / scal / archiwum” (do kroku 13) |
| recenzja porządków | Sonnet | 4e + 9: próbka 30 źródeł liczb, odsyłacze, stara nazwa | gotowe | – | 124 | 4 | 8 braków, żaden wysoki; naprawione `gra` 96c925c |
| kody serii (zwiad) | Haiku | lista kodów dawnych serii (688 trafień) | gotowe | – | 61 | 1 | `kody.md` w archiwum |
| porządki 4/4d (G) | Sonnet | spłaszczenie repo gry, potem kody serii i pomiar dekoru | gotowe | – | 91+ | 12+ | 740 testów, `gra` 3aac792, 6f85cb8, 607aa1d |
| porządki 5 (N2) | Sonnet | notatki główne | gotowe | – | 120 | 2 | `notatki` f1e08cb |
| porządki 6 (N3) | Sonnet | notatki funkcji | gotowe | – | 76 | 1 | `notatki` 040be65 |
| porządki 3 (N1) | Sonnet | Serie, Analizy, archiwum (kopiowanie) | gotowe | – | 136 | 4 | `notatki` 3e5176e |
| porządki 2 (W) | Sonnet | repo warsztat | gotowe | – | 92 | 2 | `warsztat` 98fa093 |
| Fable: dziury | Fable | szukanie dziur w ekonomii (90 prób) | gotowe | – | brak danych | ok. 2 h | 6 dziur, raport w `archiwum/fable-17.11/` |
| Fable: zeszyt | Fable | treść zeszytu wujka (48 zadań) | gotowe | – | brak danych | ok. 5 h | szkic danych i treść w archiwum |
| Fable: wnętrza | Fable | projekt 34 wnętrz, 39 makiet | gotowe | – | brak danych | ok. 14 h | makiety i specyfikacje w archiwum |
