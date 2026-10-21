#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recompte, dans le déroulé v27 lui-même, les quatre nombres que la v27 annonce.

Règle : tout nombre annoncé se recompte par script, jamais de mémoire. Les
sources sont le tableau du plan de comptes, la grille de la section 2, et les
lignes d'écriture des fiches de la section 10.
"""
import re, html, sys

s = open('deroule-comprendre-la-comptabilite-v29.corps.html', encoding='utf-8').read()
faux = 0


def dit(ok, libelle, obtenu, attendu):
    global faux
    if not ok:
        faux += 1
    print(f'{"  " if ok else "!!"} {libelle} : {obtenu}' + ('' if ok else f'  — attendu {attendu}'))


# ── 1. le plan de comptes ──────────────────────────────────────────────────
i = s.find('<h3>Le grand journal et le plan de comptes</h3>')
j = s.find('</table>', i)
plan = set(re.findall(r'<tr><td>(\d{3,4})</td>', s[i:j])) | \
       set(re.findall(r'</td><td>(\d{3,4})</td>', s[i:j]))
dit(len(plan) == 29, 'comptes au plan', len(plan), 29)

# ── 2. la grille de la section 2 ───────────────────────────────────────────
k = s.find('2 — La grille')
grille = set(re.findall(r'<span class="cpt">(\d{3,4})</span>', s[k:i]))
dit(len(grille) == 27, 'comptes affichés à la grille', len(grille), 27)
dit(grille == plan - {'4456', '4457'}, 'la grille = le plan moins les deux TVA journal seul',
    sorted(plan - grille), "['4456', '4457']")

# ── 3. les lignes d'écriture des fiches ────────────────────────────────────
fiches = s[s.find('10 — Chapitres détaillés'):s.find('11 — Lexique cumulatif')]
txt = html.unescape(re.sub(r'<[^>]+>', ' ', fiches)).replace('\xa0', ' ')
# Le nom d'un compte peut porter un tiret cadratin — « 4455 État — TVA à
# décaisser » — donc on borne sur le guillemet du libellé, pas sur le tiret.
lignes = re.findall(
    r'(Bilan seul|GdJal seul|Bilan|CR)\s+—\s+(\d{3,4})\s.{0,60}?«[^»]*»\s*—\s*'
    r'([\d  ]+(?:,\d+)?)\s*€\s*au\s+(débit|crédit)', txt)
D = C = 0.0
comptes = set()
for doc, cpt, somme, sens in lignes:
    v = float(somme.replace(' ', '').replace(' ', '').replace(',', '.'))
    comptes.add(cpt)
    if doc == 'Bilan seul':      # le résultat du Chapitre 11 ne passe pas par le journal
        continue
    if sens == 'débit':
        D += v
    else:
        C += v

dit(len(lignes) == 107, 'lignes d\'écriture lues aux fiches', len(lignes), 107)
dit(abs(D - C) < 0.005, 'le journal équilibre', f'{D:,.2f} / {C:,.2f}', 'égaux')
dit(abs(D - 1294694.00) < 0.005, 'total de contrôle du module', f'{D:,.2f}', '1 294 694,00')

jal = {c for doc, c, _, _ in lignes if doc != 'Bilan seul'}
dit(len(jal) == 28, 'comptes mouvementés au journal', len(jal), 28)
dit(plan - jal == {'120'}, 'le seul compte du plan absent du journal', sorted(plan - jal), "['120']")

# ── 4. le contrôle du compte 512 du Chapitre 8 ─────────────────────────────
fin8 = fiches.find('Chapitre 9')
t8 = html.unescape(re.sub(r'<[^>]+>', ' ', fiches[:fin8])).replace('\xa0', ' ')
l512 = re.findall(r'Bilan\s+—\s+512\s[^—]*—\s*«[^»]*»\s*—\s*([\d  ]+(?:,\d+)?)\s*€\s*au\s+(débit|crédit)', t8)
d8 = sum(float(v.replace(' ', '').replace(',', '.')) for v, sens in l512 if sens == 'débit')
c8 = sum(float(v.replace(' ', '').replace(',', '.')) for v, sens in l512 if sens == 'crédit')
dit(len(l512) == 13, 'lignes du compte 512 à la fin du Chapitre 8', len(l512), 13)
dit(abs(d8 - 112240) < 0.005, '  dont au débit', f'{d8:,.2f}', '112 240,00')
dit(abs(c8 - 50868.90) < 0.005, '  dont au crédit', f'{c8:,.2f}', '50 868,90')
dit(abs(d8 - c8 - 61371.10) < 0.005, '  différence, soit la ligne Trésorerie du Bilan',
    f'{d8 - c8:,.2f}', '61 371,10')

sys.exit(1 if faux else 0)
