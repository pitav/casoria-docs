#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fabrique le PDF du plan depuis son corps HTML et casoria.css.
Même chaîne que pdf_relecture.py : HTML + casoria.css + weasyprint.
Ajoute seulement un style pour <pre class="code">, absent de casoria.css.
"""
import html, os, subprocess, sys, datetime, shutil

CORPS = sys.argv[1]
SORTIE = sys.argv[2]
CSS = sys.argv[3]
TITRE = "L'ordre des écritures"
VERSION = 'v3'

_M = ('janvier février mars avril mai juin juillet août septembre octobre '
      'novembre décembre').split()
_d = datetime.date.today()
PIED = (f'Casoria · plan — l’ordre des écritures · {VERSION} · '
        f'{_d.day} {_M[_d.month - 1]} {_d.year}')

SUP = '''
pre.code{
  font-family: "DejaVu Sans Mono", monospace; font-size: 7.6pt; line-height: 1.42;
  background: var(--fond-doux); border-left: 3px solid var(--trait-fort);
  padding: 9px 11px; margin: 10px 0 14px; white-space: pre-wrap;
  color: var(--encre); break-inside: avoid;
}
code{
  font-family: "DejaVu Sans Mono", monospace; font-size: 8.6pt;
  color: var(--lexique);
}
pre.code code{ color: inherit; font-size: inherit }
ol{ padding-left: 20px }
ol.checklist{ padding-left: 0 }
td.ch{ width: 5%; font-weight: 700; color: var(--encre) }
'''

src = open(CORPS, encoding='utf-8').read()
# Insécables des guillemets : « X » ne doit jamais se couper en fin de ligne.
src = src.replace('« ', '« ').replace(' »', ' »')
page = f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>{html.escape(TITRE)}</title>
<link rel="stylesheet" href="casoria.css">
<style>{SUP}</style></head>
<body>
<p class="pied">{html.escape(PIED)}</p>
{src}
</body></html>'''

d = os.path.dirname(os.path.abspath(SORTIE))
tmp = os.path.join(d, 'plan.pdf.html')
shutil.copy(CSS, os.path.join(d, 'casoria.css'))
open(tmp, 'w', encoding='utf-8').write(page)
subprocess.run(['python3', '-m', 'weasyprint', tmp, SORTIE], check=True)
os.remove(tmp)
os.remove(os.path.join(d, 'casoria.css'))
print('écrit :', SORTIE, f'({os.path.getsize(SORTIE) // 1024} Ko)')
