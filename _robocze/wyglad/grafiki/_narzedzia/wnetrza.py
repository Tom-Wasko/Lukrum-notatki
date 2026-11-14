# -*- coding: utf-8 -*-
"""Elementy wnętrza, dekor, tła typów lokali i stanów, sklep meblowy."""
import random
from baza import *

K = c('czern')
STYLE = ('podstawowy', 'prl', 'nowoczesny', 'studencki', 'rodzinny')


# ───────────── Lublin: sylwety (własne, uproszczone) ─────────────
def brama(f, f2):
    """Brama Krakowska, pole 60×150, podstawa na y=150."""
    return (rect(8, 70, 44, 80, f) + path('M22 150v-22q8-12 16 0v22z', f2) + rect(4, 64, 52, 8, f) + rect(14, 38, 32, 28, f)
            + circ(30, 51, 6, f2) + path('M11 38h38l-5-7H16z', f) + path('M17 31q13-24 26 0z', f) + rect(27, 4, 6, 10, f)
            + path('M25 6q5-9 10 0z', f) + kreska('M30 0v6', f, 1.600))


def zamek(f, f2):
    """Zamek Lubelski z donżonem, pole 90×60, podstawa na y=60."""
    return (path('M0 60V30h6v-5h6v5h8v-5h6v5h8v-5h6v5h8v-5h6v5h30v30z', f) + rect(60, 8, 22, 52, f) + path('M58 8h4v-5h4v5h5v-5h4v5h5v-5h4v5z', f)
            + ''.join(path(f'M{x} 60V46q4-7 8 0v14z', f2) for x in (8, 24, 40)) + rect(68, 20, 6, 10, f2))


def okienka(x0, y0, kol, rz, dx, dy, w, h, f, op='.75'):
    return ''.join(rect(x0 + i * dx, y0 + j * dy, w, h, f, op=op) for i in range(kol) for j in range(rz))


def widok_stare(niebo=True):
    s = rect(0, 0, 240, 190, c('niebo')) + eli(60, 34, 26, 8, c('biel'), op='.7') + eli(190, 22, 20, 6, c('biel'), op='.7') if niebo else ''
    s += rect(0, 100, 50, 90, A, op='.55') + path('M-4 100L25 74L54 100z', c('drewno')) + okienka(9, 112, 2, 3, 21, 24, 10, 14, c('biel'))
    s += rect(50, 82, 44, 108, c('drewno2')) + path('M50 82h8v-9h8v-9h12v9h8v9h8z', c('drewno2')) + okienka(58, 94, 2, 4, 18, 22, 9, 13, c('czern'), '.45')
    s += g(brama(c('metal2'), c('niebo')), tr='translate(96 40)')
    s += rect(158, 96, 42, 94, A2, op='.5') + path('M155 96l7-18h34l7 18z', c('metal2')) + okienka(165, 108, 2, 3, 18, 25, 10, 14, c('biel'))
    s += rect(200, 72, 44, 118, R) + path('M197 72L222 50L247 72z', c('mieso')) + okienka(208, 86, 2, 4, 17, 24, 9, 13, c('biel'))
    return s + rect(0, 182, 240, 8, c('metal2'), op='.6')


def widok_lsm(niebo=True):
    s = rect(0, 0, 240, 190, c('niebo')) + eli(150, 26, 28, 8, c('biel'), op='.7') if niebo else ''
    s += rect(8, 48, 66, 142, c('biel'), s=c('metal'), sw=1) + okienka(14, 56, 5, 9, 12, 14.500, 7, 8, c('metal2'), '.6') + ''.join(rect(38, y, 7, 8, A) for y in (56, 85, 114, 143))
    s += rect(172, 34, 60, 156, R, op='.75') + okienka(178, 42, 4, 10, 13.500, 14.500, 8, 8, c('biel'), '.7') + ''.join(rect(191.500, y, 8, 8, A2) for y in (56.500, 100, 143.500))
    s += rect(88, 86, 72, 104, c('sciana2')) + okienka(94, 94, 5, 6, 13, 15.500, 8, 9, c('biel'), '.75')
    s += rect(78, 160, 3, 26, c('drewno')) + circ(79.500, 152, 14, c('zielen')) + rect(163, 164, 3, 22, c('drewno')) + circ(164.500, 158, 11, c('zielen2'))
    s += kreska('M128 186V132q0-6 8-6', c('metal2'), 2) + circ(137, 127, 2.500, c('biel'))
    return s + rect(0, 184, 240, 6, c('zielen'), op='.6')


def widok_dworzec(niebo=True):
    s = rect(0, 0, 240, 190, c('niebo')) + eli(70, 24, 24, 7, c('biel'), op='.7') if niebo else ''
    s += kreska('M0 48H240M0 56H240', c('metal2'), 1.200, op='.6') + ''.join(kreska(f'M{x} 48v22', c('metal2'), 1.200, op='.6') for x in (40, 110, 180))
    s += rect(-20, 100, 204, 60, A2, rx=14) + rect(-10, 110, 184, 20, c('szklo')) + ''.join(rect(x, 110, 3, 20, A2) for x in (20, 52, 84, 116, 148))
    s += rect(-20, 140, 204, 6, A) + circ(172, 150, 3, c('biel')) + rect(0, 158, 190, 4, K, op='.5')
    s += rect(0, 66, 240, 9, c('metal2')) + ''.join(rect(x, 75, 6, 115, c('metal2')) for x in (28, 204))
    s += circ(216, 100, 11, c('biel'), s=K, sw=2) + kreska('M216 100v-7M216 100l5 3', K, 1.600)
    return s + rect(0, 164, 240, 26, c('podloga2')) + kreska('M0 169H240', A, 2.500, da='10 6', cap='butt')


WIDOKI = {'stare-miasto': widok_stare, 'lsm': widok_lsm, 'dworzec': widok_dworzec}
for k, f in WIDOKI.items():
    dodaj('tla/widok-' + k, 240, 190, f(), f'Widok strefy za oknem i w tle działki ({k})')


# ───────────── Okna (260×200) ─────────────
def okno_kamienica():
    d = 'M14 194V78Q14 12 130 12Q246 12 246 78V194z'
    return (path(d, 'none', s=c('sciana2'), sw=16) + f'<clipPath id="k-okno-kamienica"><path d="{d}"/></clipPath>'
            + g(g(widok_stare(), tr='translate(10 6)'), **{'clip-path': 'url(#k-okno-kamienica)'})
            + path(d, 'none', s=c('drewno'), sw=6) + kreska('M130 13V194M14 104H246', c('drewno'), 5, cap='butt') + rect(2, 190, 256, 10, c('metal'), rx=2))


def okno_pawilon():
    return (rect(0, 6, 260, 188, c('metal2'), rx=3) + '<clipPath id="k-okno-pawilon"><rect x="8" y="14" width="244" height="172"/></clipPath>'
            + g(g(widok_lsm(), tr='translate(8 10) scale(1.020 .930)'), **{'clip-path': 'url(#k-okno-pawilon)'})
            + kreska('M89 14V186M171 14V186', c('metal2'), 5, cap='butt') + rect(8, 150, 244, 4, c('metal2'))
            + rect(180, 24, 62, 20, A, rx=3) + tekst(211, 38.500, 'OTWARTE', 11, P) + rect(0, 190, 260, 10, c('metal'), rx=2))


def okno_dworzec():
    return (rect(6, 0, 248, 200, c('metal2'), rx=2) + '<clipPath id="k-okno-dworzec"><rect x="12" y="6" width="236" height="188"/></clipPath>'
            + g(g(widok_dworzec(), tr='translate(10 5)'), **{'clip-path': 'url(#k-okno-dworzec)'})
            + kreska('M71 6V194M130 6V194M189 6V194M12 68H248M12 132H248', c('metal2'), 4, cap='butt'))


dodaj('wnetrze/okno-kamienica', 260, 200, okno_kamienica(), 'Okno kamienicy (łuk) z widokiem na Stare Miasto')
dodaj('wnetrze/okno-pawilon', 260, 200, okno_pawilon(), 'Witryna pawilonu z widokiem na bloki')
dodaj('wnetrze/okno-dworzec', 260, 200, okno_dworzec(), 'Okno przemysłowe z widokiem na peron')


# ───────────── Sprzęt: poziomy 1–3 (zestawy ★, ★★, ★★★) ─────────────
def lada(p):
    if p == 1:
        return (rect(0, 40, 450, 14, c('drewno'), rx=3) + rect(6, 54, 438, 94, c('drewno2'))
                + path(''.join(f'M{x} 54V148' for x in range(30, 440, 24)), s=c('drewno'), sw=1.600, op='.45') + rect(6, 148, 438, 12, c('metal2')))
    salatki = eli(330, 37, 16, 9, c('zielen')) + eli(366, 37, 16, 9, A) + eli(402, 37, 16, 9, c('drewno2'))
    if p == 2:
        return (rect(300, 6, 140, 34, c('szklo'), rx=4, fo='.6', s=c('metal'), sw=2) + salatki + rect(0, 40, 450, 14, c('metal'), rx=3)
                + rect(6, 54, 438, 94, c('biel'), s=c('metal'), sw=1) + rect(6, 80, 438, 22, A) + rect(6, 148, 438, 12, c('metal2')))
    return (rect(232, 0, 208, 40, c('szklo'), rx=5, fo='.6', s=c('metal'), sw=2.500) + eli(262, 37, 16, 9, c('mieso')) + eli(296, 37, 16, 9, c('biel')) + salatki
            + kreska('M300 2V40M370 2V40', c('metal'), 2) + rect(0, 40, 450, 14, K, rx=3) + rect(4, 42, 442, 2.500, c('biel'), op='.3')
            + rect(6, 54, 438, 94, c('drewno')) + path(''.join(f'M{x} 60V146' for x in range(14, 444, 11)), s=K, sw=1.400, op='.28')
            + rect(6, 54, 438, 4, A, kl='neon') + rect(6, 148, 438, 12, c('metal2')))


def kasa(p):
    terminal = rect(86, 32, 19, 32, K, rx=3) + rect(89, 36, 13, 10, c('szklo')) + ''.join(circ(x, y, 1.100, c('metal')) for x in (91.500, 95.500, 99.500) for y in (51, 55, 59))
    if p < 3:
        s = (path('M8 64V44L21 22H67L80 44V64z', c('metal2')) + rect(28, 4, 32, 18, K, rx=2) + rect(31, 7, 26, 9, c('zielen'), op='.8')
             + ''.join(rect(27 + i * 9, 27 + j * 7, 6.500, 4.500, c('biel'), rx=1) for i in range(4) for j in range(3))
             + rect(12, 51, 64, 9, K, op='.3', rx=1.500) + circ(44, 55.500, 1.800, c('metal')))
        return s + (terminal if p == 2 else '')
    return (rect(40, 40, 10, 16, c('metal2')) + rect(22, 56, 46, 8, c('metal2'), rx=2) + rect(12, 2, 62, 40, K, rx=4) + rect(16, 6, 54, 32, c('szklo'))
            + ''.join(rect(20 + i * 12.500, 10 + j * 13, 9.500, 10, A if (i + j) % 3 == 0 else A2, rx=1.500, op='.85') for i in range(4) for j in range(2))
            + terminal + path('M108 30h-1v-14h-14v14h-1', c('biel'), s=c('metal'), sw=1) + kreska('M96 20h8M96 24h6', c('metal2'), 1))


def para(xs, y):
    return g(''.join(kreska(f'M{x} {y}q7-9 0-18', c('metal'), 3) for x in xs), kl='para', op='.75')


def stozek(cx, gora, dol, wg, wd):
    s = path(f'M{cx - wg} {gora}q{wg}-8 {2 * wg} 0l{-(wg - wd)} {dol - gora}q{-wd} 6 {-2 * wd} 0z', c('mieso'))
    kroki = 4
    for i in range(1, kroki):
        y = gora + (dol - gora) * i / kroki
        w = wg - (wg - wd) * i / kroki
        s += kreska(f'M{n(cx - w + 2.0)} {n(y)}q{n(w - 2.0)} 5 {n(2 * w - 4.0)} 0', c('drewno'), 1.800, op='.7')
    return s


def rozen(p):
    if p == 1:
        return (g(rect(80, 34, 14, 122, K, rx=3, op='.45') + rect(82.500, 38, 9, 114, A, rx=3, op='.8') + rect(58, 8, 4, 172, c('metal')) + circ(60, 9, 5, c('metal2'))
                  + stozek(60, 32, 160, 23, 13), tr='rotate(-2 60 180)')
                + rect(26, 178, 68, 8, c('metal2'), rx=2) + rect(36, 186, 48, 14, c('metal2')) + para((46, 60, 74), 26))
    s = ''
    if p == 3:
        s += rect(6, 26, 108, 152, c('metal'), op='.55') + path(''.join(f'M{x} 28V176' for x in range(18, 110, 12)), s=c('metal2'), sw=1, op='.5')
    s += rect(55.500, 40, 9, 118, K, rx=3, op='.45') + rect(57, 44, 6, 110, A, rx=3, op='.85')
    for cx in (32, 88):
        s += rect(cx - 2, 28 if p == 3 else 12, 4, 166 - (16 if p == 3 else 0), c('metal')) + stozek(cx, 46 if p == 3 else 36, 162, 20, 12)
    s += rect(6, 178, 108, 8, c('metal2'), rx=2) + rect(18, 186, 84, 14, c('metal2'))
    if p == 3:
        s += path('M0 0h120l-12 24H12z', c('metal')) + rect(12, 24, 96, 5, c('metal2')) + circ(104, 192, 2.500, A, kl='neon')
    return s + para((24, 40, 80, 96) if p == 2 else (30, 60, 90), 30 if p == 2 else 0)


def tablica(p):
    if p == 1:
        return (rect(0, 0, 260, 140, c('drewno'), rx=4) + rect(8, 8, 244, 124, c('tablica')) + kreska('M30 120q40-8 90 2M150 30q40 6 80-4', c('biel'), 9, op='.05')
                + rect(92, 132, 76, 6, c('drewno2'), rx=2) + rect(100, 129, 16, 4, c('biel'), rx=1.500))
    if p == 2:
        return (rect(0, 0, 260, 140, c('metal2'), rx=4) + rect(6, 6, 248, 128, c('tablica')) + rect(6, 6, 248, 32, A)
                + path(''.join(f'M10 {y}H250' for y in range(42, 134, 7)), s=c('biel'), sw=1, op='.09'))
    return (rect(0, 0, 260, 140, K, rx=7) + rect(6, 6, 248, 128, c('biel'), rx=3) + rect(6, 6, 248, 32, A2) + rect(6, 36, 248, 2.500, A, kl='neon')
            + kreska('M16 67H244M16 89H244M16 111H244', c('metal'), 1, op='.7'))


for nazwa, f, opis in (('lada', lada, 'Lada (pole 450×160, blat na y=40)'), ('kasa', kasa, 'Kasa fiskalna'), ('rozen', rozen, 'Rożen z parą (klasa .para)'),
                       ('tablica', tablica, 'Tablica menu bez napisów (ceny dopisuje gra)')):
    wym = {'lada': (450, 160), 'kasa': (110, 64), 'rozen': (120, 200), 'tablica': (260, 140)}[nazwa]
    for p in (1, 2, 3):
        dodaj(f'wnetrze/{nazwa}-{p}', wym[0], wym[1], f(p), f'{opis}, poziom {p} (zestaw {"★" * p})')

dodaj('wnetrze/drzwi-zaplecze', 110, 240,
      rect(0, 22, 110, 218, c('drewno')) + rect(8, 30, 94, 210, A2) + rect(18, 124, 74, 100, 'none', s=K, sw=1.600, op='.3', rx=3)
      + circ(55, 78, 17, c('szklo'), s=c('metal'), sw=3) + circ(92, 138, 4, c('metal')) + rect(10, 0, 90, 17, c('biel'), rx=2, s=A2, sw=2)
      + tekst(55, 12.500, 'ZAPLECZE', 10.500, A2, **{'letter-spacing': '.8'}), 'Drzwi na zaplecze z tabliczką')

dodaj('wnetrze/portret-wujka', 64, 80,
      rect(0, 0, 64, 80, c('drewno'), rx=2) + rect(6, 6, 52, 68, c('drewno2')) + path('M11 74q0-23 21-23q21 0 21 23z', A)
      + kreska('M22 56v18M32 52v22M42 56v18', c('biel'), 1.200, op='.4') + circ(32, 37, 12.500, c('skora'))
      + path('M19 32q0-14 13-14q13 0 13 14z', c('metal2')) + path('M17 32q15-5 31 1q-1 4-6 3q-11-3-25-1z', c('metal2'))
      + path('M25 42q7-5 14 0q-2 4-7 2q-5 2-7-2z', c('siwy')) + circ(27.500, 37, 1.400, K) + circ(36.500, 37, 1.400, K), 'Portret wujka w ramce (stały element lokalu)')

dodaj('wnetrze/karton', 80, 64,
      path('M4 16L0 4h34l6 12zM76 16L80 4H46l-6 12z', c('drewno2')) + path('M4 16L0 4h34l6 12zM76 16L80 4H46l-6 12z', K, op='.12')
      + rect(4, 16, 72, 48, c('drewno2'), s=c('drewno'), sw=1.500) + rect(36, 16, 8, 48, c('biel'), op='.5')
      + kreska('M16 48v-14l-5 5M16 34l5 5M60 48v-14l-5 5M60 34l5 5', c('drewno'), 2), 'Karton (lokal w urządzaniu)')
dodaj('wnetrze/drabina', 70, 190,
      kreska('M24 6L5 188M31 6L35 188M46 6L65 188', c('drewno2'), 5) + kreska('M21 40h11M17 76h16M13 112h20M9 148h25', c('drewno2'), 4)
      + rect(18, 0, 34, 8, c('drewno'), rx=2) + kreska('M34 150L62 150', c('metal2'), 2), 'Drabina malarska')
dodaj('wnetrze/wiadro', 44, 46,
      kreska('M5 12q17-18 34 0', c('metal2'), 2) + path('M5 12h34l-4 34H9z', c('metal')) + rect(2, 8, 40, 6, c('metal2'), rx=2) + rect(6, 9.500, 32, 3, A)
      + path('M30 14v9q0 3 2.500 3q2.500 0 2.500-3v-9z', A), 'Wiadro z farbą')
dodaj('wnetrze/zarowka', 34, 96,
      kreska('M17 0V62', K, 1.600) + circ(17, 78, 17, c('biel'), op='.18') + rect(13, 60, 8, 9, c('metal2')) + circ(17, 78, 9, c('biel'), s=c('metal'), sw=1.200)
      + kreska('M14 78q3-5 6 0', A, 1.400), 'Goła żarówka na kablu (lokal w urządzaniu)')


# ───────────── Dekor: ściany i podłoga ─────────────
def sciana(st):
    s = rect(0, 0, 1220, 380, c('sciana'))
    if st == 'podstawowy':
        return s + rect(0, 366, 1220, 14, c('sciana2'))
    if st == 'prl':
        return (s + rect(0, 200, 1220, 180, A2, fo='.28') + path(siatka(0, 200, 1220, 380, 30, 30), s=c('sciana2'), sw=1.500)
                + rect(0, 193, 1220, 7, A2) + rect(0, 184, 1220, 2.500, A2, op='.6'))
    if st == 'nowoczesny':
        return (s + rect(305, 0, 305, 380, A2, fo='.18') + path('M305 0V380M610 0V380M915 0V380M0 190H1220', s=c('sciana2'), sw=2)
                + ''.join(circ(x + dx, y, 2.600, c('sciana2')) for x in (0, 305, 610, 915) for dx in (14, 291) for y in (14, 176, 204, 356))
                + rect(0, 372, 1220, 8, K, op='.45'))
    if st == 'studencki':
        los = random.Random(7)
        kol = ''
        for _ in range(22):
            rz = los.randrange(0, 17)
            x = los.randrange(0, 21) * 56 + (28 if rz % 2 else 0)
            kol += rect(x + 1.500, rz * 22 + 1.500, 53, 19, los.choice((A, A2, c('drewno2'))), fo='.4')
        return s + kol + path(siatka(0, 0, 1220, 380, 56, 22, przes=28), s=c('sciana2'), sw=1.500) + rect(0, 370, 1220, 10, K, op='.45')
    los = random.Random(3)
    listki = ''.join(path(f'M{x + (22 if j % 2 else 0)} {y}q5-7 10 0q-5 7-10 0z', c('zielen'), op='.4' if (i + j) % 3 else '.7')
                     for j, y in enumerate(range(18, 240, 34)) for i, x in enumerate(range(8, 1220, 44)))
    return (s + listki + rect(0, 250, 1220, 130, c('drewno2')) + path(''.join(f'M{x} 256V368' for x in range(34, 1220, 34)), s=c('drewno'), sw=1.600, op='.45')
            + rect(0, 244, 1220, 10, c('drewno')) + rect(0, 368, 1220, 12, c('drewno')))


def podloga(st):
    s = rect(0, 0, 1220, 232, c('podloga')) + rect(0, 0, 1220, 3, K, op='.3')
    if st == 'podstawowy':
        return s + path('M0 70H1220M0 150H1220', s=c('podloga2'), sw=1.500, op='.6')
    if st == 'prl':
        los = random.Random(11)
        return s + ''.join(circ(los.randrange(0, 1220), los.randrange(6, 230), 1.200 + los.random() * 2.600, los.choice((c('podloga2'), c('metal2'), c('biel'), A2)),
                                op=n(.35 + los.random() * .45)) for _ in range(330))
    if st == 'nowoczesny':
        return (s + path(siatka(0, 0, 1220, 232, 152.500, 116), s=c('podloga2'), sw=1.500)
                + ''.join(path(f'M{x} 0l-70 232h46l70-232z', c('biel'), op='.14') for x in (240, 660, 1040)))
    if st == 'studencki':
        return (s + rect(0, 0, 1220, 232, c('drewno2'), fo='.45') + path(siatka(0, 0, 1220, 232, 210, 38, przes=105), s=c('drewno'), sw=1.500, op='.45'))
    d = ''
    for y in range(-29, 232, 29):
        d += f'M0 {y}' + ''.join(f'l29 29l29-29' for _ in range(22))
    return (s + rect(0, 0, 1220, 232, c('drewno2'), fo='.55') + '<clipPath id="k-podloga-rodzinny"><rect width="1220" height="232"/></clipPath>'
            + g(path(d, s=c('drewno'), sw=1.500, op='.45'), **{'clip-path': 'url(#k-podloga-rodzinny)'}))


OPIS_ST = {'podstawowy': 'podstawowy (bez dekoru)', 'prl': 'PRL', 'nowoczesny': 'nowoczesny', 'studencki': 'studencki', 'rodzinny': 'rodzinny'}
for st in STYLE:
    dodaj(f'dekor/sciana-{st}', 1220, 380, sciana(st), f'Ściana, styl {OPIS_ST[st]}')
    dodaj(f'dekor/podloga-{st}', 1220, 232, podloga(st), f'Podłoga, styl {OPIS_ST[st]}')


# ───────────── Dekor: szyld (260×66, napis dopisuje gra) ─────────────
def szyld(st):
    if st == 'podstawowy':
        return rect(0, 9, 260, 48, c('biel'), rx=3, s=c('metal2'), sw=2) + circ(8, 17, 2, c('metal2')) + circ(252, 17, 2, c('metal2')) + circ(8, 49, 2, c('metal2')) + circ(252, 49, 2, c('metal2'))
    if st == 'prl':
        return (kreska('M40 0v8M220 0v8', c('metal2'), 3, cap='butt') + rect(0, 6, 260, 54, c('tablica'), rx=8)
                + rect(4, 10, 252, 46, 'none', rx=6, s=A, sw=2, kl='neon') + kreska('M24 51q14-6 28 0t28 0', A2, 2.200, kl='neon') + kreska('M180 51q14-6 28 0t28 0', A2, 2.200, kl='neon'))
    if st == 'nowoczesny':
        return rect(0, 9, 260, 48, A2, rx=24) + rect(4, 13, 252, 40, 'none', rx=20, s=P, sw=1.500, op='.6') + circ(26, 33, 7, P) + circ(234, 33, 7, P)
    if st == 'studencki':
        return (kreska('M0 4q65 12 130 2t130-2', K, 1.400) + ''.join(circ(x, y, 4, (A, A2, c('biel'))[i % 3], kl='neon') for i, (x, y) in enumerate(((22, 9), (56, 12), (92, 11), (130, 8), (168, 6), (204, 6), (240, 5))))
                + g(rect(8, 16, 244, 44, c('drewno2'), rx=2) + kreska('M8 30H252M8 45H252', c('drewno'), 1.200, op='.45') + rect(2, 12, 22, 9, A, op='.85') + rect(236, 55, 22, 9, A2, op='.85'), tr='rotate(-1.500 130 38)'))
    return (kreska('M50 0V12M210 0V12', c('metal2'), 2.200) + path('M14 12h232q12 23 0 46H14q-12-23 0-46z', c('drewno')) + path('M18 16h224q9 19 0 38H18q-9-19 0-38z', 'none', s=c('drewno2'), sw=1.500)
            + path('M24 35q5-9 10 0q-5 9-10 0z', c('zielen')) + path('M226 35q5-9 10 0q-5 9-10 0z', c('zielen')))


# ───────────── Dekor: lampy (60×120, wiszą od y=0) ─────────────
def lampa(st):
    if st == 'podstawowy':
        return kreska('M30 0V52', K, 1.600) + path('M18 70l6-18h12l6 18z', c('metal2')) + eli(30, 70, 8, 3, c('biel'))
    if st == 'prl':
        return kreska('M30 0V50', c('metal2'), 2.200) + circ(30, 76, 30, c('biel'), op='.14') + rect(24, 48, 12, 8, c('metal2'), rx=2) + circ(30, 74, 19, c('biel'), s=c('metal'), sw=1.500) + kreska('M19 68q5-9 13-10', P, 2.500, op='.7')
    if st == 'nowoczesny':
        return rect(0, 0, 60, 5, K) + rect(28.500, 5, 3, 30, K) + rect(21, 35, 18, 34, K, rx=2) + rect(21, 64, 18, 5, A) + path('M21 69h18l16 51H5z', c('biel'), op='.12')
    if st == 'studencki':
        return (kreska('M30 0q-7 14 0 26t0 26', A, 2.400) + rect(26, 50, 8, 9, c('metal2')) + circ(30, 72, 24, c('biel'), op='.14') + path('M22 66q0-8 8-8q8 0 8 8q0 6-4 11h-8q-4-5-4-11z', c('biel'), s=c('metal'), sw=1.200)
                + kreska('M27 70l3-5l3 5', A, 1.400) + path('M16 60q14-10 28 0v12q-14 16-28 0z', 'none', s=K, sw=1.200) + kreska('M30 55V84M16 66H44', K, 1))
    return (kreska('M30 0V46', c('drewno'), 2.200) + path('M8 84L20 46h20l12 38z', c('drewno2')) + rect(8, 80, 44, 6, A)
            + ''.join(kreska(f'M{x} 86v6', A, 1.600) for x in range(11, 52, 5)) + eli(30, 84, 10, 3, c('biel'), op='.8'))


# ───────────── Dekor: meble (220×150, podłoga na y=150) ─────────────
def krzeslo(x, lustro, siedzisko, rama, oparcie=True):
    s = rect(12, 98, 38, 8, siedzisko, rx=2) + (rect(12, 56, 7, 44, siedzisko, rx=3) if oparcie else '') + kreska('M16 106L13 149M46 106L49 149', rama, 3.500)
    return g(s, tr=f'translate({x + 62} 0) scale(-1 1)' if lustro else f'translate({x} 0)')


def meble(st):
    if st == 'podstawowy':
        return (krzeslo(0, False, c('biel'), c('metal2'), False) + krzeslo(158, True, c('biel'), c('metal2'), False)
                + rect(58, 70, 104, 8, c('biel'), rx=2, s=c('metal'), sw=1) + rect(106, 78, 8, 66, c('metal2')) + rect(84, 143, 52, 7, c('metal2'), rx=3))
    if st == 'prl':
        return (krzeslo(0, False, A, c('metal')) + krzeslo(158, True, A, c('metal'))
                + rect(54, 68, 112, 9, c('biel'), rx=2) + rect(54, 74, 112, 3.500, A) + rect(105, 77, 10, 66, c('metal')) + eli(110, 145, 30, 5, c('metal'))
                + rect(96, 54, 12, 14, c('metal'), rx=1.500) + rect(98, 50, 8, 6, c('biel')) + rect(116, 58, 5, 10, c('biel'), rx=1.500) + rect(124, 58, 5, 10, A2, rx=1.500))
    if st == 'nowoczesny':
        hoker = lambda x: rect(x, 62, 32, 8, A2, rx=4) + rect(x + 14.500, 70, 3, 74, K) + rect(x + 6, 108, 20, 2.500, K) + eli(x + 16, 146, 15, 4, K)
        return (hoker(14) + hoker(174) + rect(68, 38, 84, 7, K, rx=2) + rect(107, 45, 6, 99, K) + eli(110, 146, 24, 4.500, K)
                + rect(100, 22, 9, 16, c('szklo'), rx=1.500) + rect(113, 28, 16, 10, A, rx=2))
    if st == 'studencki':
        skrzynka = rect(62, 84, 100, 62, c('drewno2')) + kreska('M62 100H162M62 116H162M62 132H162', c('drewno'), 2, op='.5', cap='butt') + rect(56, 76, 112, 9, c('drewno'), rx=1.500) + rect(70, 86, 6, 60, c('drewno')) + rect(148, 86, 6, 60, c('drewno'))
        return (krzeslo(0, False, A, K) + skrzynka + path('M170 150q-6-34 20-40q26 4 24 40z', A2) + kreska('M178 122q12-6 26 2', K, 1.400, op='.3')
                + rect(100, 60, 8, 16, c('zielen2'), rx=2) + rect(102, 54, 4, 7, c('zielen2')) + rect(116, 66, 18, 10, c('biel'), rx=1.500, s=c('metal'), sw=1))
    lawka = rect(2, 98, 48, 8, c('drewno'), rx=2) + rect(2, 60, 6, 40, c('drewno'), rx=2) + rect(2, 66, 6, 4, c('drewno2')) + kreska('M8 106V149M44 106V149', c('drewno'), 4.500) + rect(10, 90, 36, 8, A, rx=4)
    krz = g(rect(12, 98, 38, 8, c('drewno'), rx=2) + rect(12, 52, 8, 48, c('drewno'), rx=3) + kreska('M16 106L14 149M46 106L48 149', c('drewno'), 4.500) + rect(20, 90, 28, 8, A2, rx=4), tr='translate(220 0) scale(-1 1)')
    obrus = path('M54 70h112v16l-8-5l-8 5l-8-5l-8 5l-8-5l-8 5l-8-5l-8 5l-8-5l-8 5l-8-5l-8 5l-8-5l-8 5z', c('biel')) + path('M54 70h112v5H54zM70 70v14M94 70v14M118 70v14M142 70v14', 'none', s=A, sw=1.500, op='.7')
    return (lawka + krz + rect(52, 66, 116, 7, c('drewno'), rx=2) + kreska('M64 73V149M156 73V149', c('drewno'), 5.500) + obrus
            + rect(104, 50, 12, 16, A2, rx=3) + kreska('M110 50V38', c('zielen2'), 1.800) + circ(110, 35, 5, A) + circ(110, 35, 1.800, c('biel')))


# ───────────── Dekor: dodatki ─────────────
def zdjecie(st):
    if st == 'prl':
        return (rect(0, 0, 100, 76, c('drewno'), rx=2) + rect(6, 6, 88, 64, c('drewno2')) + rect(6, 62, 88, 8, c('drewno'), op='.5')
                + g(brama(c('drewno'), c('drewno2')), tr='translate(36 8) scale(.420)') + rect(10, 46, 22, 24, c('drewno'), op='.75') + path('M8 46L21 34L34 46z', c('drewno'), op='.75')
                + rect(66, 40, 24, 30, c('drewno'), op='.75') + path('M64 40l5-9h18l5 9z', c('drewno'), op='.75'))
    if st == 'nowoczesny':
        return (rect(0, 0, 100, 76, K, rx=1) + rect(3, 3, 94, 70, c('biel')) + kreska('M8 60q18-26 40-22t44-26', A2, 4) + kreska('M14 14L60 66M40 8L84 62M8 34H92M30 10V70', c('metal'), 1.200)
                + circ(54, 36, 5, A) + circ(54, 36, 9.500, 'none', s=A, sw=1.200))
    if st == 'studencki':
        fot = lambda x, y, kat, kol: g(rect(0, 0, 26, 30, c('biel'), s=c('metal'), sw=.800) + rect(3, 3, 20, 18, kol) + circ(13, 1.500, 2.200, A), tr=f'translate({x} {y}) rotate({kat})')
        return (rect(0, 0, 100, 76, c('drewno2'), rx=2, s=c('drewno'), sw=3) + ''.join(circ(x, y, .900, c('drewno'), op='.5') for x in range(8, 96, 9) for y in range(8, 72, 9))
                + kreska('M6 12q44 14 88 0', K, 1) + fot(10, 14, -8, A2) + fot(40, 20, 5, c('zielen')) + fot(66, 12, -4, A) + rect(34, 56, 34, 13, c('biel'), tr='rotate(-3 50 62)') + kreska('M38 61h24M38 65h16', c('metal2'), 1.200))
    return (eli(50, 38, 49, 37, c('drewno2'), s=c('drewno'), sw=3) + eli(50, 38, 40, 29, c('niebo')) + '<clipPath id="k-zdjecie-rodzinny"><ellipse cx="50" cy="38" rx="40" ry="29"/></clipPath>'
            + g(rect(0, 56, 100, 20, c('zielen')) + g(zamek(c('biel'), c('metal2')), tr='translate(14 6) scale(.850)') + circ(26, 22, 6, A, op='.8'), **{'clip-path': 'url(#k-zdjecie-rodzinny)'}))


def plakat(st):
    if st == 'prl':
        return (rect(0, 0, 64, 96, c('biel'), s=c('metal'), sw=1) + circ(32, 34, 21, A) + path('M14 34q18-17 36 0q-18 17-36 0z', c('biel')) + circ(32, 34, 7, K)
                + path('M8 66l10-10l10 10l10-10l10 10l8-8v16H8z', A2) + tekst(32, 90, 'LUBLIN', 11, K, font='gruby'))
    if st == 'nowoczesny':
        return (rect(0, 0, 64, 96, c('biel'), s=K, sw=2) + path('M10 50a22 22 0 0 1 44 0z', A) + path('M10 54h44L32 86z', A2) + kreska('M10 14h30M10 20h18', K, 2, cap='butt'))
    if st == 'studencki':
        return (rect(0, 0, 64, 96, c('tablica')) + path('M36 8L16 46h14l-8 30l28-42H36l8-26z', A) + ''.join(rect(6, y, 52, 3, c('biel'), op='.8') for y in (80, 86))
                + path('M50 10l1.800 4l4.200.500l-3 3l.800 4.200l-3.800-2l-3.800 2l.800-4.200l-3-3l4.200-.500z', A2) + rect(24, -3, 16, 7, c('biel'), op='.6'))
    return (rect(0, 0, 64, 96, c('biel'), s=c('metal'), sw=1) + rect(22, -3, 20, 7, A2, op='.6') + circ(14, 16, 7, A) + kreska('M14 4v3M14 25v3M2 16h3M23 16h3M6 8l2 2M20 22l2 2M22 8l-2 2M8 22l-2 2', A, 1.400)
            + path('M32 52L46 38L60 52V72H32z', 'none', s=A2, sw=2) + rect(42, 58, 8, 14, 'none', s=A2, sw=1.600)
            + ''.join(circ(x, 62 - h, 3, 'none', s=K, sw=1.400) + kreska(f'M{x} {65 - h}v{8 + h}M{x - 4} {70 - h}h8M{x} {73}l-3 6M{x} {73}l3 6', K, 1.400) for x, h in ((10, 6), (20, 0)))
            + kreska('M4 84q8-5 14 0t14 0t14 0t14 0', c('zielen'), 2.200))


def roslina(st):
    if st == 'prl':
        liscie = ''.join(kreska(f'M32 60q{dx} {-dy} {2 * dx} {-dy + 14}', c('zielen'), 4.500) for dx, dy in ((-14, 26), (14, 26), (-10, 40), (10, 40), (-15, 12), (15, 12), (0, 46)))
        return liscie + path('M20 58h24l-3 18H23z', A) + rect(18, 56, 28, 5, A, rx=2) + rect(18, 56, 28, 5, K, op='.15', rx=2) + kreska('M24 76L16 111M40 76L48 111M32 76V111M19 96H45', c('drewno'), 2.800)
    if st == 'nowoczesny':
        lisc = lambda tr, kol: g(path('M0 0q-18-10-16-32q6-4 8 2q-2-10 6-14q4 6 2 12q6-8 12-4q4 22-12 36z', kol), tr=tr)
        return (kreska('M32 84Q30 60 18 46M32 84Q34 56 46 40M32 84V50', c('zielen2'), 2.200) + lisc('translate(20 50) rotate(-28)', c('zielen2')) + lisc('translate(46 44) rotate(24)', c('zielen')) + lisc('translate(33 36) rotate(-4) scale(.900)', c('zielen2'))
                + rect(18, 82, 28, 30, c('metal'), rx=2) + rect(18, 82, 28, 5, c('metal2'), rx=2))
    if st == 'studencki':
        return (rect(25, 34, 14, 54, c('zielen'), rx=7) + kreska('M25 62h-7q-5 0-5-6v-8M39 54h7q5 0 5-6v-6', c('zielen'), 7) + kreska('M32 40v44M28 44v40M36 44v40', c('zielen2'), 1, op='.6')
                + circ(32, 32, 4.500, A) + circ(32, 32, 1.600, c('biel')) + path('M18 86h28l-4 26H22z', A) + rect(16, 84, 32, 6, A, rx=2) + rect(16, 84, 32, 6, K, op='.15', rx=2)
                + kreska('M27 98q5 4 10 0', K, 1.600) + circ(27, 94, 1.200, K) + circ(37, 94, 1.200, K))
    return (kreska('M32 86V44', c('drewno'), 3.500) + ''.join(eli(x, y, 11, 7, c('zielen') if i % 2 else c('zielen2'), tr=f'rotate({kat} {x} {y})') for i, (x, y, kat) in enumerate(((20, 40, -30), (44, 38, 30), (16, 22, 20), (48, 20, -20), (32, 10, 0), (30, 28, 90), (22, 56, 10), (44, 54, -14))))
            + path('M16 84h32l-4 28H20z', c('drewno2')) + path('M17 90h30M18 97h28M19 104h26M24 84l2 28M32 84v28M40 84l-2 28', 'none', s=c('drewno'), sw=1.200, op='.6') + rect(14, 82, 36, 5, c('drewno'), rx=2))


for st in STYLE:
    dodaj(f'dekor/szyld-{st}', 260, 66, szyld(st), f'Szyld bez napisu, styl {OPIS_ST[st]} (elementy z klasą .neon świecą)')
    dodaj(f'dekor/lampa-{st}', 60, 120, lampa(st), f'Lampa wisząca, styl {OPIS_ST[st]}')
    dodaj(f'dekor/meble-{st}', 220, 150, meble(st), f'Stolik z krzesłami, styl {OPIS_ST[st]}')
    if st != 'podstawowy':
        dodaj(f'dekor/zdjecie-{st}', 100, 76, zdjecie(st), f'Dodatek: obraz z Lublinem, styl {OPIS_ST[st]}')
        dodaj(f'dekor/plakat-{st}', 64, 96, plakat(st), f'Dodatek: plakat, styl {OPIS_ST[st]}')
        dodaj(f'dekor/roslina-{st}', 64, 112, roslina(st), f'Dodatek: roślina, styl {OPIS_ST[st]}')


# ───────────── Tła typów lokalu (1220×612, przezroczyste, kładzione na ścianę i podłogę) ─────────────
dodaj('tla/typ-kamienica', 1220, 612,
      path('M0 0H586V48Q293-28 0 48z', c('sciana2')) + path('M594 0H1220V48Q907-28 594 48z', c('sciana2'))
      + kreska('M0 48Q293-28 586 48M594 48Q907-28 1220 48', K, 2, op='.22') + rect(578, 0, 16, 380, c('sciana2')) + path(siatka(578, 52, 594, 380, 16, 14), s=K, sw=1, op='.2')
      + rect(573, 42, 26, 9, c('sciana2')) + rect(573, 42, 26, 9, K, op='.15')
      + path('M1052 64q42-12 92 0q26 20 8 42q-52 12-100 0q-20-20 0-42z', A, fo='.22') + path(siatka(1060, 70, 1144, 106, 28, 12, przes=14), s=A, sw=1.200, op='.55')
      + rect(0, 372, 1220, 8, c('sciana2')) + rect(0, 372, 1220, 8, K, op='.12'),
      'Typ lokalu: kamienica na Starym Mieście (sklepienie, filar, odkryta cegła)')

dodaj('tla/typ-pawilon', 1220, 612,
      rect(0, 0, 1220, 20, c('biel')) + path(siatka(0, 0, 1220, 20, 61, 20), s=c('metal'), sw=1.200, op='.7')
      + ''.join(rect(x - 6, 3, 132, 14, c('biel'), op='.25', rx=6) + rect(x, 7, 120, 6, c('biel'), rx=3, s=c('metal'), sw=1) for x in (400, 700, 990))
      + rect(60, 314, 200, 54, c('biel'), rx=5, s=c('metal'), sw=1.200) + path(''.join(f'M{x} 318V364' for x in range(72, 256, 13)), s=c('metal'), sw=1.600)
      + kreska('M260 356h16V380', c('metal2'), 3, cap='butt') + rect(1100, 40, 62, 30, c('metal'), op='.7', rx=2) + path('M1106 48h50M1106 55h50M1106 62h50', s=c('metal2'), sw=1.600)
      + rect(0, 370, 1220, 10, c('metal2'), op='.5'),
      'Typ lokalu: pawilon osiedlowy (sufit kasetonowy, świetlówki, kaloryfer)')

dodaj('tla/typ-dworzec', 1220, 612,
      rect(0, 0, 1220, 18, c('metal2')) + rect(0, 0, 1220, 4, K, op='.3') + rect(0, 14, 1220, 4, K, op='.3') + ''.join(circ(x, 9, 2, K, op='.4') for x in range(20, 1220, 40))
      + path('M556 18L586 58L616 18z', c('metal2'), op='.8') + circ(586, 34, 3, K, op='.4')
      + circ(1140, 82, 36, c('biel'), s=c('metal2'), sw=5) + ''.join(kreska('M1140 52v6', K, 2, tr=f'rotate({k} 1140 82)') for k in range(0, 360, 30))
      + kreska('M1140 82V62M1140 82l15 8', K, 3) + g(kreska('M1140 88V56', A, 1.400), kl='sekundnik') + circ(1140, 82, 2.600, K)
      + rect(1006, 50, 84, 24, A2, rx=3) + tekst(1048, 67, 'PERONY →', 12, P, **{'letter-spacing': '.6'})
      + rect(0, 372, 1220, 8, K, op='.4') + path(''.join(f'M{x} 600h14' for x in range(0, 1220, 22)), s=A, sw=5, op='.7'),
      'Typ lokalu: przy dworcu (stalowa belka, zegar dworcowy, tablica „Perony”)')


def surowa_sciana():
    los = random.Random(5)
    s = rect(0, 0, 1220, 380, c('sciana')) + rect(0, 0, 1220, 380, c('podloga2'), fo='.45')
    for x, y, w, h in ((80, 240, 190, 90), (420, 60, 260, 120), (760, 210, 220, 110), (1010, 40, 150, 70)):
        s += path(f'M{x} {y}q{w / 2} {-18} {w} {4}q{14} {h / 2} {-6} {h}q{-w / 2} {14} {-w + 10} {-6}q{-18} {-h / 2} {-4} {-h + 2}z', c('biel'), op='.4')
    s += path('M318 250q30-10 62 4q10 30-6 52q-34 8-58-6q-10-28 2-50z', A, fo='.25') + path(siatka(322, 256, 378, 304, 28, 12, przes=14), s=A, sw=1.200, op='.55')
    s += kreska('M620 0q-10 60 20 84M640 84q16 10 6 28', K, 2) + kreska('M940 0V40q0 16 16 16h60', K, 2) + rect(1014, 48, 16, 16, c('biel'), s=K, sw=1.200)
    s += ''.join(kreska(f'M{x} {y}h{los.randrange(18, 50)}', c('metal2'), 1.200, op='.6') for x, y in ((600, 330), (604, 338), (700, 200), (150, 120), (154, 128), (880, 150)))
    return s + rect(0, 372, 1220, 8, K, op='.2')


dodaj('tla/stan-surowy-sciana', 1220, 380, surowa_sciana(), 'Lokal niewyposażony: surowy tynk z łatami, kable')
dodaj('tla/stan-surowy-podloga', 1220, 232,
      rect(0, 0, 1220, 232, c('podloga2')) + rect(0, 0, 1220, 3, K, op='.3') + kreska('M120 30l60 40l-20 50M700 10l40 70l80 20M1000 120l90 30', K, 1.200, op='.3')
      + path('M380 60L760 40L820 190L340 214z', c('biel'), op='.3') + kreska('M380 60L760 40L820 190L340 214z', c('metal'), 1.200)
      + eli(250, 180, 60, 10, c('biel'), op='.25') + eli(980, 70, 46, 8, c('biel'), op='.25'), 'Lokal niewyposażony: wylewka z folią malarską')


# ───────────── Działka w budowie ─────────────
def teren():
    s = rect(0, 0, 1220, 432, c('niebo')) + eli(240, 70, 70, 16, c('biel'), op='.7') + eli(300, 84, 50, 12, c('biel'), op='.7') + eli(860, 50, 80, 16, c('biel'), op='.7')
    for x in (10, 420, 880):
        s += g(widok_lsm(False), tr=f'translate({x} 196) scale(1.240)', op='.5')
    s += rect(0, 430, 1220, 182, c('podloga2')) + rect(0, 430, 1220, 182, c('drewno2'), fo='.4') + rect(0, 430, 1220, 3, K, op='.25')
    for x in range(0, 1220, 122):
        s += rect(x + 2, 368, 118, 66, A2, fo='.55', s=c('metal2'), sw=1.500) + path(''.join(f'M{x + 2 + i} 370V432' for i in range(12, 118, 12)), s=c('metal2'), sw=1, op='.5') + rect(x - 2, 362, 5, 76, c('metal2'))
    s += kreska('M0 520q200-16 420 6M700 560q200-20 520 0', c('drewno'), 3, op='.35') + eli(160, 566, 70, 10, c('niebo'), op='.7')
    s += path('M1070 612l40-46q14-12 30 0l50 46z', c('drewno2')) + path('M1070 612l40-46q14-12 30 0l50 46z', K, op='.1')
    return s


dodaj('tla/dzialka-teren', 1220, 612, teren(), 'Działka: niebo, bloki w tle, ziemia, ogrodzenie')


def rusztowanie(x0, x1, gora):
    s = ''.join(kreska(f'M{x} {gora}V320', c('metal2'), 4, cap='butt') for x in range(x0, x1 + 1, 130))
    for y in (gora + 40, gora + 120):
        if y < 310:
            s += rect(x0 - 6, y, x1 - x0 + 12, 6, c('drewno2')) + kreska(f'M{x0} {y - 26}H{x1}', c('metal2'), 2.500, cap='butt')
    return s + ''.join(kreska(f'M{x} 320L{x + 130} {gora + 46}', c('metal2'), 2, op='.7') for x in range(x0, x1, 260))


def mur(gora):
    s = rect(40, gora, 480, 286 - gora, c('mieso'), op='.6') + path(siatka(40, gora, 520, 286, 40, 14, przes=20), s=K, sw=1, op='.25')
    return s


OTWORY = rect(86, 188, 112, 64, c('niebo')) + rect(252, 196, 64, 90, c('niebo')) + rect(366, 188, 112, 64, c('niebo'))


def etap(i):
    plyta = path('M10 320l22-26h496l22 26z', K, op='.22') + rect(36, 296, 488, 9, c('drewno2')) + rect(40, 284, 480, 14, c('metal'))
    if i == 1:
        return (plyta + ''.join(kreska(f'M{x} 284v-26', c('metal2'), 2.500, cap='butt') for x in (44, 60, 76, 250, 266, 282, 484, 500, 516))
                + path('M360 284l34-40q10-10 22 0l40 40z', c('drewno2')) + rect(120, 262, 70, 22, c('mieso'), op='.7') + path(siatka(120, 262, 190, 284, 18, 7, przes=9), s=K, sw=1, op='.3'))
    if i == 2:
        return (plyta + mur(170) + OTWORY + path('M40 170h100v-14h80v14h120v-22h90v22h90v-10', 'none', s=c('mieso'), sw=10, op='.6', join='miter')
                + rusztowanie(20, 540, 130))
    dach = rect(26, 96, 508, 16, c('metal2')) + rect(26, 90, 508, 7, K, op='.5')
    if i == 3:
        return plyta + mur(110) + OTWORY + dach + rusztowanie(20, 280, 80) + rect(330, 78, 60, 14, K, rx=7) + rect(400, 82, 40, 10, c('drewno2'))
    return (rect(0, 302, 560, 18, c('metal')) + path(siatka(0, 302, 560, 320, 40, 18), s=c('metal2'), sw=1, op='.6') + rect(40, 110, 480, 194, c('biel'), s=c('metal'), sw=1.500) + rect(40, 262, 480, 42, A2, fo='.3')
            + ''.join(rect(x, 188, 112, 64, c('szklo'), s=c('metal2'), sw=4) + kreska(f'M{x + 56} 188v64', c('metal2'), 3, cap='butt') for x in (86, 366))
            + rect(252, 196, 64, 108, A2, s=c('metal2'), sw=3) + rect(262, 206, 44, 44, c('szklo')) + circ(306, 256, 3, c('metal'))
            + dach + path('M232 176h104l10 14H222z', A) + rect(184, 124, 200, 38, c('biel'), rx=4, s=A, sw=2, da='7 5') + tekst(284, 149, 'TU BĘDZIE SZYLD', 14, A, **{'letter-spacing': '1'})
            + rect(440, 284, 22, 20, c('metal')) + rect(438, 281, 26, 5, A) + kreska('M40 300q120 24 240 0t240 0', A, 3))


OPIS_ETAP = {1: 'fundamenty', 2: 'ściany i rusztowanie', 3: 'dach', 4: 'wykończenie, przed otwarciem'}
for i in (1, 2, 3, 4):
    dodaj(f'stany/budowa-etap{i}', 560, 320, etap(i), f'Budowa lokalu, etap {i}: {OPIS_ETAP[i]} (podstawa na y=320)')

dodaj('stany/zuraw', 220, 420,
      kreska('M96 44V420M116 44V420', c('metal2'), 4, cap='butt') + path(''.join(f'M96 {y}l20 30l-20 30' for y in range(60, 400, 60)), s=c('metal2'), sw=2)
      + kreska('M14 44H216', A, 6, cap='butt') + path(''.join(f'M{x} 44l12-14l12 14' for x in range(20, 200, 24)), s=A, sw=1.600) + kreska('M24 30H206', A, 2.500)
      + kreska('M106 6L30 30M106 6L200 30M106 6V44', c('metal2'), 2) + rect(14, 48, 36, 24, c('metal2')) + rect(88, 62, 36, 30, A, rx=3) + rect(94, 68, 16, 12, c('szklo'))
      + g(kreska('M182 44V156', K, 1.600) + path('M176 156h12v10q0 8-8 8q-6 0-6-6', 'none', s=K, sw=3) + rect(166, 174, 34, 22, c('drewno2'), s=c('drewno'), sw=1.500), kl='hak'),
      'Żuraw budowlany (grupa .hak lekko się kołysze)')
dodaj('stany/betoniarka', 110, 110,
      kreska('M26 104L44 60M84 104L66 60M20 104H90', c('metal2'), 5) + g(path('M-30-20h44l16 16v22l-16 16h-44q-10-27 0-54z', A) + eli(30, 7, 7, 15, K, op='.6') + kreska('M-22-20v54M-6-20v54', K, 1.600, op='.25'), tr='translate(56 44) rotate(-24)')
      + circ(28, 98, 11, K) + circ(28, 98, 4, c('metal')) + circ(82, 98, 11, K) + circ(82, 98, 4, c('metal')), 'Betoniarka')
dodaj('stany/tablica-budowy', 150, 130,
      rect(20, 60, 8, 70, c('drewno2')) + rect(122, 60, 8, 70, c('drewno2')) + rect(0, 0, 150, 86, c('biel'), rx=3, s=K, sw=2) + path('M1 3q0-2 2-2h144q2 0 2 2v21H1z', A)
      + tekst(75, 17.500, 'BUDOWA LOKALU', 12, P, **{'letter-spacing': '.6'}) + kreska('M12 38h126M12 50h96M12 62h110M12 74h70', K, 2, op='.45'), 'Tablica informacyjna budowy')
dodaj('stany/projekt', 130, 100,
      kreska('M18 58L8 100M34 58L44 100M96 58L86 100M112 58L122 100', c('drewno2'), 4) + rect(0, 50, 130, 8, c('drewno2'), rx=2) + path('M12 50l10-32h92l6 32z', A2)
      + path('M30 44l5-18h56l4 18zM50 44l3-18M70 26l2 10h22', 'none', s=c('biel'), sw=1.400) + rect(96, 38, 28, 8, c('biel'), rx=4, s=c('metal'), sw=1, tr='rotate(-14 110 42)'),
      'Stół z projektem lokalu')


# ───────────── Sklep meblowy ─────────────
dodaj('tla/sklep-hala', 1220, 612,
      rect(0, 0, 1220, 400, c('sciana')) + rect(0, 0, 1220, 74, c('sciana2')) + kreska('M0 18H1220M0 74H1220', c('metal2'), 3, cap='butt', op='.7')
      + path('M0 74' + ''.join('l61-56l61 56' for _ in range(10)), s=c('metal2'), sw=2.500, op='.6') + rect(0, 86, 1220, 8, A)
      + ''.join(path(f'M{x - 18} 104h36l70 296h-176z', c('biel'), op='.07') + kreska(f'M{x} 74V92', c('metal2'), 2) + path(f'M{x - 20} 106l8-14h24l8 14z', c('metal2')) + eli(x, 106, 14, 3, c('biel')) for x in (190, 450, 710, 970))
      + rect(0, 400, 1220, 212, c('podloga')) + rect(0, 400, 1220, 3, K, op='.3') + path(siatka(0, 400, 1220, 612, 152.500, 106), s=c('podloga2'), sw=1.200, op='.7')
      + ''.join(path(f'M{x} 400l-64 212h40l64-212z', c('biel'), op='.13') for x in (330, 800)) + kreska('M0 452H1060', A2, 3.500, da='26 16', cap='butt', op='.6'),
      'Hala sklepu meblowego (kratownice, lampy, alejka)')
dodaj('sklep/regal', 230, 300,
      rect(10, 38, 210, 258, K, op='.08') + rect(2, 34, 8, 266, c('metal2')) + rect(220, 34, 8, 266, c('metal2'))
      + ''.join(rect(6, y, 218, 7, c('metal')) + rect(10, y + 7, 210, 3, c('biel'), op='.5') for y in (118, 202)) + rect(6, 288, 218, 9, c('metal'))
      + rect(8, 0, 214, 36, A, rx=3) + rect(8, 0, 214, 36, 'none', rx=3, s=K, sw=1.500, op='.25'), 'Regał sklepowy z tabliczką działu (napis i towar dokłada gra)')
dodaj('sklep/wozek', 150, 130,
      path('M30 30h106l-13 56H44z', c('biel'), fo='.25', s=c('metal2'), sw=3, join='round') + path('M52 30l6 56M76 30l3 56M100 30v56M122 30l-4 56M33 48h99M38 66h90', 'none', s=c('metal2'), sw=1.300)
      + kreska('M28 20l16 66l-5 22h86', c('metal2'), 3.500) + kreska('M6 18h24', A, 6) + circ(50, 119, 8.500, K) + circ(50, 119, 3, c('metal')) + circ(116, 119, 8.500, K) + circ(116, 119, 3, c('metal')), 'Wózek sklepowy')
dodaj('sklep/kasa', 170, 170,
      rect(124, 0, 44, 20, A, rx=3) + tekst(146, 14.500, 'KASA', 11, P, **{'letter-spacing': '.8'}) + kreska('M146 20V36', c('metal2'), 3, cap='butt')
      + rect(128, 36, 38, 28, K, rx=3) + rect(131, 39, 32, 22, c('szklo')) + rect(143, 64, 8, 10, c('metal2')) + rect(110, 58, 12, 22, c('metal2'), rx=2) + rect(112, 61, 8, 4, A, kl='neon')
      + rect(6, 70, 100, 11, K, rx=4) + kreska('M14 75.500h84', c('metal2'), 1.200, da='3 5') + rect(0, 80, 170, 90, c('biel'), rx=4, s=c('metal'), sw=1.500) + rect(0, 106, 170, 16, A2) + rect(0, 160, 170, 10, c('metal2'), rx=3),
      'Kasa sklepowa z taśmą')
dodaj('sklep/paczka', 60, 44,
      rect(2, 8, 56, 36, c('drewno2'), s=c('drewno'), sw=1.500) + path('M2 8l6-8h44l6 8z', c('drewno2')) + path('M2 8l6-8h44l6 8z', K, op='.1') + rect(26, 0, 8, 44, c('biel'), op='.5')
      + rect(38, 24, 15, 12, c('biel')) + kreska('M41 28h9M41 32h6', K, 1, op='.6'), 'Paczka z zakupem (w wózku)')
dodaj('sklep/puszka', 34, 40,
      kreska('M5 12q12-16 24 0', c('metal2'), 1.800) + rect(3, 10, 28, 30, c('metal'), rx=2) + rect(1, 7, 32, 5, c('metal2'), rx=2) + rect(3, 18, 28, 14, 'currentColor'), 'Puszka farby (kolor etykiety: currentColor)')

for st in STYLE:
    pass
