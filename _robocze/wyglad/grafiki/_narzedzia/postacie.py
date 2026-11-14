# -*- coding: utf-8 -*-
"""Ikony paska i postacie (pole 120×260, stopy na y=256, środek x=60). Własne interpretacje, jeden płaski styl."""
from baza import *

K = c('czern')

# ───────────── Ikony paska (24×24, kreska currentColor) ─────────────
IK = {
    'lokal': ('Lokal', 'M3.5 9l1.5-5h14l1.5 5M3.5 9a2.85 2.85 0 0 0 5.67 0a2.85 2.85 0 0 0 5.66 0a2.85 2.85 0 0 0 5.67 0M5 12.5V20h14v-7.5M10 20v-4.5h4V20'),
    'menu': ('Menu i ceny', 'M6 3h12a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zM8 8h5M8 12h5M8 16h5M16 8h.01M16 12h.01M16 16h.01'),
    'kuchnia': ('Kuchnia', 'M12 2v20M8 6h8l-1.6 11H9.6zM7 22h10M19.5 7v3M19.5 13v3M4.5 7v3M4.5 13v3'),
    'ludzie': ('Ludzie', 'M9 11a3 3 0 1 0 0-6a3 3 0 0 0 0 6zM3 20c0-3.6 2.6-6 6-6s6 2.4 6 6M17 11.500a2.500 2.500 0 1 0 0-5M17.5 14.6c2.300.5 3.500 2.400 3.500 5.400'),
    'finanse': ('Finanse', 'M5 6c0-1.660 3.130-3 7-3s7 1.340 7 3s-3.130 3-7 3s-7-1.340-7-3zM5 6v4c0 1.660 3.130 3 7 3s7-1.340 7-3V6M5 10v4c0 1.660 3.130 3 7 3s7-1.340 7-3v-4M5 14v4c0 1.660 3.130 3 7 3s7-1.340 7-3v-4'),
    'dekor': ('Dekor', 'M5.500 3h10a1.500 1.500 0 0 1 1.500 1.500v3A1.500 1.500 0 0 1 15.500 9h-10A1.500 1.500 0 0 1 4 7.500v-3A1.500 1.500 0 0 1 5.500 3zM17 6h3v5h-8v3M10.500 14h3v7h-3z'),
    'sklep': ('Sklep meblowy', 'M3 4h2.500l2.200 11h10.500l1.800-8H6.300M9 20.500a1.500 1.500 0 1 0 0-3a1.500 1.500 0 0 0 0 3zM17 20.500a1.500 1.500 0 1 0 0-3a1.500 1.500 0 0 0 0 3z'),
    'mapa': ('Mapa', 'M3 6l6-2l6 2l6-2v14l-6 2l-6-2l-6 2zM9 4v14M15 6v14'),
    'ustawienia': ('Ustawienia', 'M4 7h9M17 7h3M4 12h3M11 12h9M4 17h11M19 17h1M15 9a2 2 0 1 0 0-4a2 2 0 0 0 0 4zM9 14a2 2 0 1 0 0-4a2 2 0 0 0 0 4zM17 19a2 2 0 1 0 0-4a2 2 0 0 0 0 4z'),
    'rozwin': ('Rozwiń pasek', 'M6 6l6 6l-6 6M13 6l6 6l-6 6'),
    'dymek': ('Dymek', 'M4 5h16v10h-9l-4 4v-4H4z'),
    'zamknij': ('Zamknij', 'M6 6l12 12M18 6L6 18'),
    'wroc': ('Wróć', 'M20 12H5M11 6l-6 6l6 6'),
    'punkt': ('Miejsce do kliknięcia', 'M12 21a9 9 0 1 0 0-18a9 9 0 0 0 0 18zM12 8v8M8 12h8'),
    'wozek': ('Wózek', 'M3 4h2.500l2.200 11h10.500l1.800-8H6.300M9 20.500a1.500 1.500 0 1 0 0-3a1.500 1.500 0 0 0 0 3zM17 20.500a1.500 1.500 0 1 0 0-3a1.500 1.500 0 0 0 0 3zM10 10h6M13 7v6'),
}
for nazwa, (opis, d) in IK.items():
    dodaj('ikony/' + nazwa, 24, 24,
          f'<path d="{d}" fill="none" stroke="currentColor" stroke-width="1.800" stroke-linecap="round" stroke-linejoin="round"/>',
          f'Ikona: {opis}')
dodaj('ikony/gwiazdka', 24, 24, '<path d="M12 2.600l2.900 6l6.500.900l-4.700 4.600l1.100 6.500L12 17.500l-5.800 3.100l1.100-6.500L2.600 9.500l6.500-.900z" fill="currentColor"/>',
      'Ikona: gwiazdka (zestaw, ocena)')


# ───────────── Części postaci ─────────────
def mina_grupa(nazwa, inner, domyslna):
    return f'<g class="mina mina-{nazwa}"' + ('' if domyslna else ' display="none"') + f'>{inner}</g>'


def _mina(m):
    if m == 'zmeczona':
        return (kreska('M49.500 52.500h7M63.500 52.500h7', K, 2.200)
                + kreska('M49.500 57.500q3.500 2.600 7 0M63.500 57.500q3.500 2.600 7 0', c('skora2'), 1.800)
                + kreska('M54 65.500q6-2.500 12 0', K, 2.200)
                + path('M84 28q-4.500 7 0 10.500q4.500-3.500 0-10.500z', A2))
    oczy = circ(53, 52, 2.400, K) + circ(67, 52, 2.400, K)
    if m == 'dobra':
        return oczy + kreska('M52.500 61.500q7.500 7 15 0', K, 2.200) + circ(46.500, 60, 4, A, op='.22') + circ(73.500, 60, 4, A, op='.22')
    if m == 'zla':
        return oczy + kreska('M53 66.500q7-5 14 0', K, 2.200) + kreska('M48 44.500l8.500 3M72 44.500l-8.500 3', K, 2)
    return oczy + kreska('M54 64.500h12', K, 2.200)


def twarz(miny=('dobra', 'zwykla', 'zla'), jedna=None):
    nos = kreska('M60 54q3.400 3.600 0 6.200', c('skora2'), 1.900)
    if jedna:
        return _mina(jedna) + nos
    return ''.join(mina_grupa(m, _mina(m), m == 'zwykla') for m in miny) + nos


WLOSY = {
    'krotkie': 'M41 49q-2-25 19-25q21 0 19 25q-3-9-8-12q-11 4-22 0q-5 3-8 12z',
    'przedzialek': 'M41 51q-3-27 19-27q22 0 19 27q-2-10-7-14q-14 6-26-2q-4 6-5 16z',
    'boki': 'M40.500 55q-3.500-10 1.500-17q1 9 3 15zM79.500 55q3.500-10-1.500-17q-1 9-3 15z',
    'grzywa': 'M41 51q-5-22 13-27q5-7 15-4q13 4 10 31q-3-12-9-15q-13 3-24 2q-4 4-5 13z',
    'rozczochrane': 'M41 50q-4-14 4-20l2-6l5 4l4-7l6 5l6-5l4 7l5-3l1 7q7 6 3 18q-3-10-8-12q-12 4-24 0q-5 3-8 12z',
}


def wlosy(rodzaj, kolor):
    return path(WLOSY[rodzaj], kolor)


def glowa(skora='skora', tyl='', wl='', pod='', nad='', miny=('dobra', 'zwykla', 'zla'), jedna=None):
    """tyl: za głową; wl: włosy; pod: pod twarzą (broda); nad: na twarzy (okulary, wąsy, czapka)."""
    s = tyl + rect(54, 68, 12, 18, c(skora)) + rect(54, 68, 12, 18, K, op='.14')
    s += circ(41, 53, 4.200, c(skora)) + circ(79, 53, 4.200, c(skora))
    s += eli(60, 50, 19, 22, c(skora)) + pod + wl + twarz(miny, jedna) + nad
    return s


def cialo(w=1.0, gora=A, dol=None, buty=None, skora='skora', dl=170, rece=True, rekaw=None, nw=None, spodnica=None, obrys=None):
    dol = dol or c('metal2')
    buty = buty or K
    nw = nw or w
    L, Rr = 60 - 22 * w, 60 + 22 * w
    s = ''
    if spodnica:
        s += rect(49, spodnica[1] - 12, 8.500, 262 - spodnica[1], c('skora2')) + rect(62.500, spodnica[1] - 12, 8.500, 262 - spodnica[1], c('skora2'))
        s += rect(45, 247, 14, 9, buty, rx=4) + rect(61, 247, 14, 9, buty, rx=4)
    else:
        s += rect(60 - 13 * nw, 158, 11 * nw, 92, dol) + rect(60 + 2 * nw, 158, 11 * nw, 92, dol)
        s += rect(60 - 15 * nw - 1, 246, 13 * nw + 3, 10, buty, rx=4) + rect(60 + 1 * nw, 246, 13 * nw + 3, 10, buty, rx=4)
    if rece:
        rk = rekaw or gora
        s += rect(L - 7, 88, 13, 76, rk, rx=6.500, s=obrys, sw=1.200 if obrys else None) + rect(Rr - 6, 88, 13, 76, rk, rx=6.500, s=obrys, sw=1.200 if obrys else None)
        s += circ(L - .500, 166, 6.300, c(skora)) + circ(Rr + .500, 166, 6.300, c(skora))
    s += rect(L, 82, 44 * w, dl - 82, gora, rx=15, s=obrys, sw=1.200 if obrys else None)
    if spodnica:
        s += path(f'M{n(L + 1)} 140H{n(Rr - 1)}L{n(Rr + 7)} {spodnica[1]}H{n(L - 7)}z', spodnica[0])
    return s


def kamizelka(L, Rr, kolor, dol=166):
    return (path(f'M{n(L)} 97q0-15 15-15h5l-2 {dol - 82}h-18z', kolor) + path(f'M{n(Rr)} 97q0-15-15-15h-5l2 {dol - 82}h18z', kolor))


# ───────────── Bywalcy ─────────────
def rzecki():
    s = cialo(gora=c('metal2'), dol=c('metal2'))
    s += path('M51 82L60 105L69 82z', c('biel')) + kreska('M51 82L45 101L60 113M69 82L75 101L60 113', K, 1.600, op='.4')
    s += path('M53 85l7 3.500l7-3.500v8l-7-3.500l-7 3.500z', A2) + circ(60, 126, 1.900, K, op='.55') + circ(60, 140, 1.900, K, op='.55')
    s += rect(69.500, 108, 8, 3.500, c('biel'))
    s += rect(26, 116, 14, 40, A, rx=2) + rect(28.500, 118, 2.500, 36, c('biel')) + circ(38, 150, 6.300, c('skora'))
    nad = (circ(53, 52, 6.200, 'none', s=K, sw=1.500) + circ(67, 52, 6.200, 'none', s=K, sw=1.500) + kreska('M59.200 52h1.600', K, 1.500)
           + path('M51 59.500q9-5.500 18 0q-9 4-18 0z', c('siwy')))
    return s + glowa(wl=wlosy('przedzialek', c('siwy')), nad=nad)


def zagloba():
    w = 1.420
    L, Rr = 60 - 22 * w, 60 + 22 * w
    s = cialo(w=w, gora=c('drewno2'), dol=c('drewno'), nw=1.200, buty=K)
    s += eli(60, 140, 34, 31, c('drewno2'))
    s += path(f'M{n(L)} 97q0-15 15-15h6l-3 82q-12 6-18-2z', c('zielen')) + path(f'M{n(Rr)} 97q0-15-15-15h-6l3 82q12 6 18-2z', c('zielen'))
    s += rect(32, 122, 13, 14, c('zielen2'), rx=2) + rect(75, 122, 13, 14, c('zielen2'), rx=2) + rect(33, 104, 10, 8, c('zielen2'), rx=1.500) + rect(77, 104, 10, 8, c('zielen2'), rx=1.500)
    s += rect(38, 160, 44, 6, K, op='.5') + rect(56, 159, 8, 8, c('metal'), rx=1)
    nad = (kreska('M41.500 39L78.500 55.500', K, 1.700) + eli(67, 52, 6.500, 5.500, K)
           + path('M42 61q9-9 18-2q9-7 18 2q-9 8-18 2q-9 6-18-2z', c('siwy')) + circ(46, 57, 4, A, op='.22'))
    return s + glowa(wl=wlosy('boki', c('siwy')), nad=nad)


def dulska():
    w = 1.100
    s = cialo(w=w, gora=c('mieso'), spodnica=(c('mieso'), 224), rece=False, buty=K)
    s += kreska('M60 102V222', K, 1.600, op='.3') + ''.join(circ(55, y, 2.200, c('drewno2')) for y in (124, 146, 168, 190))
    s += kreska('M38 96q-7 24 9 40', c('mieso'), 13) + kreska('M82 96q7 24-9 40', c('mieso'), 13)
    s += path('M35 93q25-24 50 0q-6 15-25 8q-19 7-25-8z', c('drewno2')) + kreska('M40 93q5 5 10 1M50 97q5 4 10 0M60 97q5 4 10-1M70 95q5 3 9-3', c('drewno'), 1.400, op='.6')
    s += kreska('M51 130q9-15 18 0', K, 3) + rect(45.500, 129, 29, 23, K, rx=3) + circ(60, 133, 2.400, c('drewno2'))
    s += circ(47, 136, 6.300, c('skora')) + circ(73, 136, 6.300, c('skora'))
    tyl = circ(60, 30, 13, c('drewno'))
    nad = (eli(60, 33, 29, 6.500, K) + path('M44 33q-1-19 16-19q17 0 16 19z', K) + rect(44.500, 26.500, 31, 5, A2)
           + path('M75 27q11-11 7-22q-8 8-10 20z', A2) + circ(41, 61, 2, c('drewno2')) + circ(79, 61, 2, c('drewno2')))
    return s + glowa(tyl=tyl, wl=path('M41 49q0-10 8-13q11 4 22 0q8 3 8 13q-3-7-8-9q-11 4-22 0q-5 2-8 9z', c('drewno')), nad=nad)


def judym():
    s = cialo(gora=c('biel'), dol=c('metal2'), rekaw=A2, obrys=None)
    s += path('M40 150h40l3 54h-46z', c('biel'), s=c('metal'), sw=1)
    s += path('M38 97q0-15 15-15l-4 84h-11z', A2) + path('M82 97q0-15-15-15l4 84h11z', A2)
    s += path('M53 82l7 10l7-10z', c('skora'), op='.9') + kreska('M60 96V200', c('metal'), 1.200)
    s += kreska('M53 85q-6 24 7 35q13-11 7-35', c('metal2'), 2.400) + circ(60, 121, 4.600, c('metal')) + circ(60, 121, 2, c('metal2'))
    s += rect(66, 132, 9, 10, 'none', s=c('metal'), sw=1.200) + rect(68.500, 127, 2, 8, A)
    return s + glowa(wl=wlosy('przedzialek', K))


def papkin():
    tyl = g(rect(56, 6, 8, 120, c('drewno2')) + rect(53.500, -6, 13, 18, c('metal2'), rx=2) + eli(60, 168, 27, 31, c('drewno2')) + circ(60, 160, 8, K, op='.5'), tr='rotate(-24 60 130)')
    s = tyl + cialo(w=.860, gora=c('drewno'), dol=A2, rece=False, buty=K)
    s += rect(24.500, 86, 15, 74, c('drewno'), rx=7.500) + rect(80.500, 86, 15, 74, c('drewno'), rx=7.500) + circ(32, 163, 6.300, c('skora')) + circ(88, 163, 6.300, c('skora'))
    s += rect(33, 80, 54, 86, c('drewno'), rx=15) + kreska('M60 92V164', c('metal'), 1.700) + kreska('M40 150h12M68 150h12', K, 1.500, op='.4')
    s += kreska('M42 88L79 160', A, 4)
    s += path('M47 83l-6-10l14 5zM73 83l6-10l-14 5z', c('drewno'))
    s += path('M49 80q11 9 22 0l2 7q-13 9-26 0z', A) + path('M66 86l5 27l-8-3l-2-21z', A)
    nad = kreska('M50 60.500q-2-3 1-3.500q5 0 9 2.500q4-2.500 9-2.500q3 .500 1 3.500', K, 1.800) + kreska('M48 44q4.500-3 9 0M63 44q4.500-3 9 0', K, 1.800)
    return s + glowa(wl=wlosy('grzywa', K), nad=nad)


def jozio():
    tyl = eli(60, 76, 28, 17, A2) + eli(60, 76, 28, 17, K, op='.2')
    s = cialo(w=1.080, gora=A2, dol=c('metal2'), buty=c('biel'), rece=False)
    s += rect(29.200, 88, 13, 76, A2, rx=6.500) + circ(35.700, 166, 6.300, c('skora'))
    s += path('M45 138h30l5 24h-40z', 'none', s=K, sw=1.500, op='.35') + kreska('M55 86v21M65 86v21', c('biel'), 2)
    s += kreska('M84 95q9 23-7 37', A2, 13) + rect(70.500, 111, 11.500, 20, K, rx=2.500) + rect(72, 113.500, 8.500, 13.500, c('szklo')) + circ(77, 130, 6.300, c('skora'))
    return g(tyl + s + glowa(wl=wlosy('rozczochrane', c('drewno'))), tr='translate(4.200 18) scale(.930)')


def wujek():
    w = 1.150
    L, Rr = 60 - 22 * w, 60 + 22 * w
    s = cialo(w=w, gora=A, dol=c('metal2'), buty=c('drewno'))
    s += kreska('M46 85V167M54 84V168M66 84V168M74 85V167M37 104H83M37 122H83M37 140H83M37 158H83', c('biel'), 1.800, op='.35')
    s += kamizelka(L, Rr, c('drewno'), 168) + circ(47, 120, 1.800, K, op='.5') + circ(47, 138, 1.800, K, op='.5')
    s += g(rect(84, 112, 11, 50, c('biel'), rx=3, s=c('metal'), sw=1) + kreska('M86.500 120h6M86.500 127h6M86.500 134h6M86.500 141h6', c('metal2'), 1.200), tr='rotate(10 89 137)')
    s += circ(Rr + .500, 160, 6.300, c('skora'))
    nad = (path('M40 41q-1-20 20-20q21 0 20 20z', c('metal2')) + path('M37 41q23-7 47 1q-1 6-8 5q-18-5-39-1z', c('metal2')) + kreska('M40 41q20-5 40 0', K, 1.400, op='.35')
           + path('M49 60q11-7 22 0q-2 6-11 3q-9 3-11-3z', c('siwy')) + kreska('M48 45.500h9M63 45.500h9', c('siwy'), 2.800))
    return s + glowa(wl=wlosy('boki', c('siwy')), nad=nad)


# ───────────── Goście ─────────────
def turystka():
    tyl = path('M38 50q-2-28 22-28q24 0 22 28l4 46q-26 9-52 0z', c('rudy'))
    s = cialo(w=.950, gora=A, dol=c('biel'), buty=A2, obrys=None)
    s += rect(60 - 13 * .950, 158, 11 * .950, 92, 'none', s=c('metal'), sw=1) + rect(60 + 2 * .950, 158, 11 * .950, 92, 'none', s=c('metal'), sw=1)
    s += kreska('M45 84v42M75 84v42', c('drewno'), 4.500)
    s += kreska('M51 84L60 116L69 84', K, 1.700) + rect(49.500, 112, 21, 15, K, rx=3) + circ(60, 119.500, 5, c('metal')) + circ(60, 119.500, 2.300, c('szklo')) + rect(51.500, 109.500, 6, 3, K)
    nad = eli(60, 34, 29, 6.200, c('drewno2')) + path('M45 34q-1-17 15-17q16 0 15 17z', c('drewno2')) + rect(45.500, 28, 29, 4.500, A2)
    return s + glowa(tyl=tyl, wl=path('M41 49q0-9 6-13q13 4 26 0q6 4 6 13q-3-6-7-8q-12 4-24 0q-4 2-7 8z', c('rudy')), nad=nad)


def podrozny():
    s = rect(92, 196, 25, 54, A, rx=4) + kreska('M98 196v-32h13v32', c('metal2'), 2.600) + kreska('M92 212h25M92 232h25', K, 1.400, op='.3') + circ(97, 253, 3.500, K) + circ(112, 253, 3.500, K)
    s += cialo(w=1.050, gora=R, dol=c('metal2'), skora='skora3')
    s += path('M37 148h46l4 60h-54z', R) + kreska('M60 100V208', K, 1.500, op='.35') + ''.join(circ(65, y, 2, K, op='.5') for y in (118, 140, 162))
    s += kreska('M52 83L46 104L60 114M68 83L74 104L60 114', K, 1.500, op='.35')
    s += path('M47 79q13 10 26 0l2 9q-15 10-30 0z', A2) + path('M52 88l-3 34l10 2l1-34z', A2) + kreska('M50 116h9', K, 1.200, op='.4')
    pod = path('M43 56q2 24 17 24q15 0 17-24q-6 12-17 12q-11 0-17-12z', K, op='.7')
    return s + glowa(skora='skora3', wl=wlosy('krotkie', K), pod=pod)


def sasiadka():
    w = 1.100
    s = kreska('M33 166L22 180M38 166L44 180', K, 1.300) + path('M21 180q-3 32 12 34q14-2 12-34z', c('biel'), fo='.25', s=K, sw=1.300) \
        + circ(29, 198, 5.500, A) + circ(38, 201, 5.500, A) + circ(33, 190, 5.500, A) + kreska('M23 188h21M22 198h23M25 207h17M28 181v32M38 181v32', K, .900, op='.5')
    s += cialo(w=w, gora=c('zielen'), spodnica=(c('drewno'), 220), buty=c('drewno'))
    s += path('M52 82l8 22l8-22z', c('biel')) + kreska('M60 104V168', K, 1.400, op='.3') + ''.join(circ(63.500, y, 1.800, c('biel')) for y in (114, 128, 142, 156))
    s += ''.join(circ(x, y, 1.500, c('biel')) for x, y in ((53, 88), (56, 91.500), (60, 93), (64, 91.500), (67, 88)))
    tyl = circ(60, 24, 11, c('siwy'))
    nad = rect(46.500, 47.500, 12.500, 9, 'none', rx=3, s=K, sw=1.500) + rect(61, 47.500, 12.500, 9, 'none', rx=3, s=K, sw=1.500) + kreska('M59 52h2', K, 1.500)
    return s + glowa(tyl=tyl, wl=wlosy('krotkie', c('siwy')), nad=nad)


def student():
    s = rect(34, 86, 52, 70, K, rx=12, op='.55')
    s += cialo(gora=c('zielen'), dol=A2, buty=c('biel'))
    s += kreska('M46 84v44M74 84v44', K, 4.500) + kreska('M60 86V168', K, 1.400, op='.3') + rect(64, 112, 12, 10, 'none', s=K, sw=1.200, op='.4')
    s += kreska('M47 82q13 13 26 0', K, 4.500) + rect(42.500, 76, 8, 12, K, rx=3.500) + rect(69.500, 76, 8, 12, K, rx=3.500)
    pod = path('M43 55q1 25 17 25q16 0 17-25q-5 15-17 14q-12 1-17-14z', c('drewno'))
    nad = path('M40 45q-2-25 20-25q22 0 20 25z', A) + rect(38.500, 38, 43, 9, A, rx=3.500) + kreska('M39 42.500h42', K, 1.200, op='.3') + circ(60, 19, 4, A)
    return s + glowa(pod=pod, nad=nad)


# ───────────── Obsługa i inni ─────────────
MINY_OBS = ('dobra', 'zwykla', 'zmeczona')


def kasjerka(jedna=None):
    tyl = path('M74 30q20 4 15 34q-7-4-10-16z', c('rudy'))
    s = cialo(w=.980, gora=A, dol=c('metal2'))
    s += kreska('M48 101L52 84M72 101L68 84', c('biel'), 3.200) + path('M45 100h30v62q-15 6-30 0z', c('biel'), s=c('metal'), sw=1)
    s += rect(52, 128, 16, 13, 'none', rx=2, s=c('metal'), sw=1.200) + rect(63, 105, 10, 6, A, rx=1)
    nad = path('M40.500 41q-1-19 19.500-19q20.500 0 19.500 19z', A) + path('M40.500 41h39q7 2 9 7h-52z', A) + kreska('M41 36.500q19-5 38 0', c('biel'), 2.400)
    return s + glowa(tyl=tyl, wl=path('M41 50q0-6 3-9h32q3 3 3 9q-3-5-6-6h-26q-3 1-6 6z', c('rudy')), nad=nad, miny=MINY_OBS, jedna=jedna)


def kucharz(jedna=None):
    s = cialo(w=1.080, gora=c('biel'), dol=c('metal2'), obrys=c('metal'))
    s += ''.join(circ(x, y, 2, K, op='.5') for x in (53, 67) for y in (100, 114, 128, 142)) + kreska('M60 92V168', c('metal'), 1.200)
    s += path('M49 81q11 10 22 0l-3 11q-8 5-16 0z', A2)
    nad = (path('M42 35v-11q-10-6-4-17q6-8 14-3q8-8 16 0q8-5 14 3q6 11-4 17v11z', c('biel'), s=c('metal'), sw=1.200)
           + rect(42, 31, 36, 8, c('biel'), s=c('metal'), sw=1.200) + kreska('M52 22v9M60 20v11M68 22v9', c('metal'), 1.200))
    return s + glowa(skora='skora3', wl=path('M41 50q-1-6 1.500-11h35q2.500 5 1.500 11q-2-4-4-5h-30q-2 1-4 5z', K), nad=nad, miny=MINY_OBS, jedna=jedna)


def sprzedawca():
    s = cialo(gora=c('biel'), dol=c('metal2'), obrys=c('metal'))
    s += kamizelka(38, 82, A2, 166) + path('M53 82l7 10l7-10z', c('skora'), op='.9')
    s += rect(66, 106, 11, 8, c('biel'), rx=1, s=K, sw=.800) + kreska('M68 109h7M68 111.500h5', K, .900, op='.6') + rect(43, 102, 2.500, 10, A)
    return s + glowa(wl=wlosy('przedzialek', c('drewno2')), jedna='dobra')


def budowlaniec():
    w = 1.120
    L, Rr = 60 - 22 * w, 60 + 22 * w
    s = cialo(w=w, gora=R, dol=c('metal2'), buty=c('drewno'))
    s += kamizelka(L, Rr, A, 166) + kreska(f'M{n(L + 1)} 126h17M{n(Rr - 1)} 126h-17M{n(L + 1)} 148h17M{n(Rr - 1)} 148h-17', c('biel'), 4, cap='butt')
    s += circ(L - .500, 166, 7, c('drewno2')) + circ(Rr + .500, 166, 7, c('drewno2'))
    pod = path('M43 56q2 22 17 22q15 0 17-22q-6 11-17 11q-11 0-17-11z', K, op='.25')
    nad = path('M39 42q-1-23 21-23q22 0 21 23z', A) + rect(35, 40, 50, 5.500, A, rx=2.500) + kreska('M60 19v21', K, 1.400, op='.3') + rect(35, 40, 50, 5.500, K, rx=2.500, op='.15')
    return s + glowa(pod=pod, nad=nad, jedna='dobra')


OS = [
    ('bywalec-rzecki', rzecki, 'Bywalec: starszy pan w wytartym garniturze, z zeszytem pod pachą'),
    ('bywalec-zagloba', zagloba, 'Bywalec: tęgi wąsacz w kamizelce wędkarskiej, z opaską na oku'),
    ('bywalec-dulska', dulska, 'Bywalczyni: pani w płaszczu z futrzanym kołnierzem, torebka jak tarcza'),
    ('bywalec-judym', judym, 'Bywalec: młody lekarz w kurtce na fartuchu, ze stetoskopem'),
    ('bywalec-papkin', papkin, 'Bywalec: chudy elegant w za dużej skórzanej kurtce, z gitarą na plecach'),
    ('bywalec-jozio', jozio, 'Bywalec: licealista w za dużej bluzie, z telefonem'),
    ('wujek', wujek, 'Wujek: kraciasta koszula, kamizelka, kaszkiet, zwinięta gazeta'),
    ('gosc-turystka', turystka, 'Gość: turystka z aparatem (Stare Miasto)'),
    ('gosc-podrozny', podrozny, 'Gość: podróżny z walizką (Dworzec)'),
    ('gosc-sasiadka', sasiadka, 'Gość: sąsiadka z siatką (osiedla)'),
    ('gosc-student', student, 'Gość: student w czapce, ze słuchawkami i plecakiem'),
    ('obsluga-kasjerka', kasjerka, 'Obsługa: kasjerka, miny przełączane przez data-mina (dobra, zwykla, zmeczona)'),
    ('obsluga-kucharz', kucharz, 'Obsługa: kucharz, miny przełączane przez data-mina (dobra, zwykla, zmeczona)'),
    ('sprzedawca', sprzedawca, 'Sprzedawca w sklepie meblowym'),
    ('budowlaniec', budowlaniec, 'Budowlaniec na działce'),
]
for nazwa, f, opis in OS:
    dodaj('postacie/' + nazwa, 120, 260, f(), opis)
for rola, f in (('kasjerka', kasjerka), ('kucharz', kucharz)):
    for m in MINY_OBS:
        dodaj(f'postacie/obsluga-{rola}-{m}', 120, 260, f(jedna=m), f'Obsługa: {rola}, mina „{m}” (plik z jedną miną)')
