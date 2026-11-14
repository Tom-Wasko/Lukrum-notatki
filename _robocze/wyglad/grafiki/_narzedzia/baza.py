# -*- coding: utf-8 -*-
"""Wspólne pomocniki generatora grafik LUKRUM (podgląd 4).
Wszystkie kolory to zmienne CSS: pięć wspólnych (--papier, --tusz, --akcent, --akcent-2, --ramka)
albo pochodne --g-* z pliku zmienne.css (liczone z tych pięciu przez color-mix)."""

G = {}  # nazwa -> (szer, wys, wnętrze SVG, opis)

P, T, A, A2, R = 'var(--papier)', 'var(--tusz)', 'var(--akcent)', 'var(--akcent-2)', 'var(--ramka)'


def c(n):
    return f'var(--g-{n})'


SKROTY = {'s': 'stroke', 'sw': 'stroke-width', 'op': 'opacity', 'fo': 'fill-opacity', 'cap': 'stroke-linecap',
          'kl': 'class', 'da': 'stroke-dasharray', 'tr': 'transform', 'join': 'stroke-linejoin', 'so': 'stroke-opacity'}


def _a(k):
    return ''.join(f' {SKROTY.get(n, n)}="{v}"' for n, v in k.items() if v is not None)


def n(v):
    return f'{v:.1f}'.rstrip('0').rstrip('.') if isinstance(v, float) else str(v)


def rect(x, y, w, h, f, rx=None, **k):
    return f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}"' + (f' rx="{n(rx)}"' if rx else '') + f' fill="{f}"{_a(k)}/>'


def circ(cx, cy, r, f, **k):
    return f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}" fill="{f}"{_a(k)}/>'


def eli(cx, cy, rx, ry, f, **k):
    return f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{n(rx)}" ry="{n(ry)}" fill="{f}"{_a(k)}/>'


def path(d, f='none', **k):
    return f'<path d="{d}" fill="{f}"{_a(k)}/>'


def kreska(d, s, sw=2, **k):
    k.setdefault('cap', 'round')
    return path(d, 'none', s=s, sw=sw, **k)


def g(inner, **k):
    return f'<g{_a(k)}>{inner}</g>'


def tekst(x, y, t, rozmiar, f, font='szyld', kotwica='middle', **k):
    return (f'<text x="{n(x)}" y="{n(y)}" text-anchor="{kotwica}" font-size="{n(rozmiar)}" fill="{f}" '
            f'style="font-family:var(--font-{font})"{_a(k)}>{t}</text>')


def dodaj(nazwa, w, h, inner, opis):
    G[nazwa] = (w, h, ' '.join(inner.split()), opis)


def siatka(x0, y0, x1, y1, kx, ky, przes=0):
    """Ścieżka kratki (kafelki, płyty). przes: przesunięcie co drugiego rzędu (cegły)."""
    d = ''
    y = y0
    i = 0
    while y <= y1 + .01:
        d += f'M{n(x0)} {n(y)}H{n(x1)}'
        y += ky
        i += 1
    if przes:
        y, i = y0, 0
        while y < y1 - .01:
            x = x0 + (przes if i % 2 else 0)
            while x <= x1:
                d += f'M{n(x)} {n(y)}v{n(min(ky, y1 - y))}'
                x += kx
            y += ky
            i += 1
    else:
        x = x0
        while x <= x1 + .01:
            d += f'M{n(x)} {n(y0)}V{n(y1)}'
            x += kx
    return d
