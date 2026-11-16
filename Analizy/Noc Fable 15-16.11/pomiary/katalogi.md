# Pomiar katalogów: przed i po (15.11.2026)

`balans.symuluj 12 latwy,sredni,trudny 7,11,23`. Gotówka w zł na koniec 12. tygodnia, wynik w pkt (0–1000). Zmiana końcowa: sprzęt wg `sprzet.yaml` (nowe ceny i utrzymanie), składniki ★ = 85%, ★★★ = 132% ceny ★★, szkolenia z uporządkowanym cennikiem. Pierwsze podejście (★★★ składników = 145%) dało premium o ok. 30–60% mniej gotówki, więc złagodzone.

## latwy

| strategia | ziarno | gotówka przed | gotówka po | wynik przed | wynik po |
|---|---|---|---|---|---|
| zrownowazony | 7 | 67309 | 66862 | 633 | 632 |
| tani | 7 | 31016 | 31644 | 360 | 361 |
| premium | 7 | 37489 | 32011 | 521 | 486 |
| agresywny | 7 | 0 | 0 | 357 | 293 |
| nasladowca | 7 | 61398 | 60867 | 592 | 591 |
| zrownowazony | 11 | 59986 | 60979 | 606 | 602 |
| tani | 11 | 46686 | 47422 | 438 | 440 |
| premium | 11 | 44300 | 38936 | 607 | 587 |
| agresywny | 11 | 0 | 0 | 443 | 416 |
| nasladowca | 11 | 45409 | 45292 | 578 | 577 |
| zrownowazony | 23 | 35597 | 33484 | 515 | 516 |
| tani | 23 | 49834 | 50279 | 459 | 461 |
| premium | 23 | 22898 | 14869 | 459 | 459 |
| agresywny | 23 | 0 | 0 | 396 | 382 |
| nasladowca | 23 | 55279 | 54755 | 589 | 588 |

Średnia gotówka: przed 37147, po 35827 (-3.6%).

## sredni

| strategia | ziarno | gotówka przed | gotówka po | wynik przed | wynik po |
|---|---|---|---|---|---|
| zrownowazony | 7 | 89900 | 88470 | 691 | 689 |
| tani | 7 | 76841 | 77286 | 577 | 577 |
| premium | 7 | 61453 | 47474 | 655 | 633 |
| agresywny | 7 | 19090 | 5642 | 514 | 474 |
| nasladowca | 7 | 73807 | 73310 | 657 | 656 |
| zrownowazony | 11 | 85717 | 86010 | 692 | 690 |
| tani | 11 | 87825 | 88564 | 603 | 604 |
| premium | 11 | 43137 | 33087 | 602 | 575 |
| agresywny | 11 | 45402 | 22860 | 585 | 524 |
| nasladowca | 11 | 101853 | 101714 | 725 | 725 |
| zrownowazony | 23 | 57434 | 56888 | 614 | 613 |
| tani | 23 | 83213 | 84501 | 569 | 571 |
| premium | 23 | 55159 | 41333 | 615 | 614 |
| agresywny | 23 | 61407 | 48987 | 641 | 612 |
| nasladowca | 23 | 65529 | 64685 | 638 | 636 |

Średnia gotówka: przed 67184, po 61387 (-8.6%).

## trudny

| strategia | ziarno | gotówka przed | gotówka po | wynik przed | wynik po |
|---|---|---|---|---|---|
| zrownowazony | 7 | 121343 | 120717 | 762 | 759 |
| tani | 7 | 88721 | 89018 | 611 | 610 |
| premium | 7 | 48142 | 44061 | 629 | 646 |
| agresywny | 7 | 44412 | 47512 | 646 | 598 |
| nasladowca | 7 | 97053 | 113053 | 738 | 753 |
| zrownowazony | 11 | 111195 | 110355 | 754 | 752 |
| tani | 11 | 104746 | 105437 | 647 | 645 |
| premium | 11 | 60346 | 50339 | 647 | 637 |
| agresywny | 11 | 68083 | 28864 | 676 | 618 |
| nasladowca | 11 | 112970 | 117026 | 753 | 761 |
| zrownowazony | 23 | 65731 | 62277 | 645 | 631 |
| tani | 23 | 88047 | 99988 | 610 | 648 |
| premium | 23 | 45964 | 39754 | 585 | 593 |
| agresywny | 23 | 85936 | 65750 | 717 | 697 |
| nasladowca | 23 | 106268 | 104258 | 737 | 737 |

Średnia gotówka: przed 83264, po 79894 (-4.0%).

## Średnie według strategii (wszystkie poziomy i ziarna)

| strategia | gotówka przed | gotówka po | wynik przed | wynik po |
|---|---|---|---|---|
| zrownowazony | 77135 | 76227 | 657 | 654 |
| tani | 72992 | 74904 | 542 | 546 |
| premium | 46543 | 37985 | 591 | 581 |
| agresywny | 36037 | 24402 | 553 | 513 |
| nasladowca | 79952 | 81662 | 667 | 669 |

Jakości kupowane przez boty (`dane/boty.yaml`, pole `jakosc`, dotyczy sprzętu, składników i ludzi): tani ★, zrównoważony ★★, naśladowca ★★, premium ★★★, agresywny ★★★. Boty niezmienione.

Uwaga: agresywny kończy z 0 gotówki na poziomie łatwym także PRZED zmianą (we wszystkich trzech ziarnach) – to stan wyjściowy, nie skutek tej zmiany.
