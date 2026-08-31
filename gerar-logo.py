# -*- coding: utf-8 -*-
"""Gera o logotipo Simulado.dev em vetor, com o texto convertido em curvas.
Sem dependência de fonte no destino: o SVG é autossuficiente.
Uso: python3 gerar-logo.py
"""
import re
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform

FONT = "node_modules/@fontsource/inter/files/inter-latin-800-normal.woff2"
_f = TTFont(FONT); _gs = _f.getGlyphSet(); _cmap = _f.getBestCmap()
_hm = _f["hmtx"]; UPEM = _f["head"].unitsPerEm
CAP = 1490 / UPEM            # altura de caixa alta da Inter

ESCUDO = "M3 14Q3 6 11 6H69Q77 6 77 14V48C77 73 63 88 40 96C17 88 3 73 3 48Z"
CORPO  = 46                  # corpo do wordmark em unidades do viewBox
GAP    = 20

def _limpa(d, casas=2):
    return re.sub(r'-?\d+\.?\d*', lambda m: f"{round(float(m.group()), casas):g}", d)

def texto_path(txt, size, x0, baseline):
    saida = []; x = x0
    for ch in txt:
        g = _cmap[ord(ch)]
        pen = SVGPathPen(_gs)
        _gs[g].draw(TransformPen(pen, Transform(size/UPEM, 0, 0, -size/UPEM, x, baseline)))
        d = pen.getCommands()
        if d: saida.append(d)
        x += _hm[g][0] * size / UPEM
    return _limpa(" ".join(saida)), x

def largura(txt, size):
    return sum(_hm[_cmap[ord(c)]][0] * size / UPEM for c in txt)

def lockup(cores=None, classes=False):
    """cores=None + classes=True gera SVG que herda as cores via CSS."""
    base = 50 + CORPO*CAP/2
    x0 = 80 + GAP
    d_nome, xf = texto_path("Simulado", CORPO, x0, base)
    d_dev, xe  = texto_path(".dev", CORPO, xf, base)
    fsg = CORPO * 0.66
    d_g, _ = texto_path("{?}", fsg, 40 - largura("{?}", fsg)/2, 50 + fsg*0.355)
    W = round(xe + 3, 1)
    def pinta(cls, cor):
        return f'class="{cls}"' if classes else f'fill="{cor}"'
    return f'''<svg viewBox="0 0 {W} 100" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Simulado.dev"><path {pinta("lg-sh", (cores or {}).get("shield"))} d="{ESCUDO}"/><path {pinta("lg-gl", (cores or {}).get("glyph"))} d="{d_g}"/><path {pinta("lg-wd", (cores or {}).get("word"))} d="{d_nome}"/><path {pinta("lg-dv", (cores or {}).get("dev"))} d="{d_dev}"/></svg>'''

def icone(cores):
    """Marca isolada, quadrada, para ícone de app e favicon."""
    fsg = 30
    d_g, _ = texto_path("{?}", fsg, 40 - largura("{?}", fsg)/2, 50 + fsg*0.355)
    return f'''<svg viewBox="-8 -2 96 106" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Simulado.dev"><path fill="{cores['shield']}" d="{ESCUDO}"/><path fill="{cores['glyph']}" d="{d_g}"/></svg>'''

DARK  = {'shield':'#6EE7B7','glyph':'#0A0F1D','word':'#EEF2FA','dev':'#F2A65A'}
LIGHT = {'shield':'#1B8F5E','glyph':'#FFFFFF','word':'#211E17','dev':'#C06A1E'}

if __name__ == "__main__":
    open("logo.svg","w").write(lockup(DARK))
    open("logo-tema-claro.svg","w").write(lockup(LIGHT))
    open("logo-icone.svg","w").write(icone(DARK))
    open("/tmp/inline.svg","w").write(lockup(classes=True))
    print("logo.svg", len(lockup(DARK)), "bytes")
    print("inline (com classes CSS)", len(lockup(classes=True)), "bytes")
