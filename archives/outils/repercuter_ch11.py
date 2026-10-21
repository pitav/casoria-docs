#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Porte les six entrées du Chapitre 11 au registre des écarts.

Le registre est le seul document de référence touché avant validation : sa
propre règle l'impose — « au fil de la rédaction, jamais après ; reconstitué
treize chapitres plus tard, ce registre sera faux et incomplet ». Le déroulé,
la charte et le journal attendent la relecture et se répercutent en une fois.

Chaque substitution est assertée unique. L'écriture se fait à la toute fin :
une assertion qui saute laisse le fichier intact.
"""
import re

F = 'registredesecartscomprendrelacomptabilite.md'
s = open(F, encoding='utf-8').read()


def rep(old, new, label, n=1):
    global s
    assert s.count(old) == n, f'{label} : {s.count(old)} occurrence(s), {n} attendue(s)'
    s = s.replace(old, new, n)


ENTREES = """### Chapitre 11 — La clôture

| # | Écart | Nature | Statut lecteur | Destination | Formulation |
|---|---|---|---|---|---|
| 11.1 | Le déficit et son report sur les années suivantes | notion non traitée | signalé (précision du corps) | **précision** | Une année qui se termine sur une perte ne donne lieu à aucun impôt sur les sociétés, et la perte n'est pas perdue pour autant : elle vient en déduction des bénéfices des années suivantes et réduit l'impôt de ces années-là. Une entreprise qui perd de l'argent sa première année et en gagne la deuxième ne paie donc pas sur la totalité de ce second bénéfice. |
| 11.2 | Les acomptes d'impôt sur les sociétés | simplification de la simulation | signalé (`<UAlert>`) | candidat | Latitude Café calcule et inscrit son impôt en une fois, le 31 décembre. Une société qui a déjà un exercice derrière elle ne fonctionne pas ainsi : elle verse quatre acomptes dans l'année, calculés sur le bénéfice de l'année précédente, et ne règle que la différence quelques mois après la fin de l'exercice. Le mécanisme du chapitre est le même, seul le calendrier change. |
| 11.3 | Les conditions d'accès au taux réduit de 15 % | cas particulier ignoré | signalé (`<UAlert>`) | candidat | Le taux de 15 % n'est pas ouvert à toutes les petites sociétés. Il suppose un chiffre d'affaires sous un plafond, un capital entièrement versé, et un capital détenu pour l'essentiel par des personnes plutôt que par d'autres sociétés. Latitude Café remplit ces trois conditions, et le chapitre le suppose sans le démontrer. |
| 11.4 | Le passage du résultat comptable au résultat fiscal | notion non traitée | signalé (`<UAlert>`, une phrase) | candidat | L'impôt ne se calcule pas tout à fait sur le bénéfice que le Compte de Résultat affiche. Certaines charges sont enregistrées en comptabilité et refusées par la loi fiscale, une amende par exemple, ou la part d'un véhicule qui dépasse un certain prix. L'entreprise repart donc du bénéfice comptable, y rajoute ces charges-là, et c'est sur le résultat ainsi corrigé que l'impôt se calcule. |
| 11.5 | La fiscalité du dividende chez l'associé | notion non traitée | silencieux | module ultérieur | Le chapitre s'arrête au moment où le dividende est décidé. Ce qui se passe ensuite ne regarde plus la société : l'associé qui reçoit un dividende est imposé dessus à son tour, à titre personnel. Le même bénéfice supporte donc deux impôts, celui de la société d'abord, celui de la personne ensuite, et c'est l'un des arguments qui pèsent dans le choix entre se verser un salaire et se verser un dividende. |
| 11.6 | La réserve légale, son taux et son plafond | cas particulier ignoré | silencieux | candidat | Le chapitre dit que la loi oblige une part du bénéfice à rester dans l'entreprise, sans dire combien ni jusqu'à quand. La règle est simple : un vingtième du bénéfice de chaque année, jusqu'à ce que la réserve atteigne le dixième du capital social. Passé ce seuil, l'obligation tombe, et tout le bénéfice redevient distribuable. |

### Chapitres 12, 13

*À remplir à la rédaction.*
"""

rep("""### Chapitres 11, 12, 13

*À remplir à la rédaction.*
""", ENTREES, 'entrées du Chapitre 11')

# ─── le compte annoncé, recompté par script et jamais repris ────────────────
n = len(re.findall(r'^\| \d+\.\d+ \|', s, re.M))
rep('**51 entrées au 25 août 2026**, après le Chapitre 10. Toutes formulées. Recomptées par script.',
    f'**{n} entrées au 25 août 2026**, après le Chapitre 11. Toutes formulées. Recomptées par script.',
    'compte annoncé')

# ─── la liste des entrées sorties par le haut ───────────────────────────────
rep("""et 10.1, la reprise de provision, ancrée sur « probable » au Chapitre 10.
**Les dix chapitres écrits en portent donc chacun une.**""",
    """10.1, la reprise de provision, ancrée sur « probable » au Chapitre 10 ; et 11.1, le report d'un
déficit sur les bénéfices des années suivantes, ancrée sur « perte » au Chapitre 11.
**Les onze chapitres écrits en portent donc chacun une.**""",
    'liste des sorties par le haut')

rep('**Neuf entrées sont sorties par le haut et sont écrites**, au 25 août 2026 :',
    '**Dix entrées sont sorties par le haut et sont écrites**, au 25 août 2026 :',
    'compte des sorties par le haut')

# ─── ce que le Chapitre 11 ajoute à la règle du tri ─────────────────────────
rep("""**`statut lecteur` reste renseigné, mais n'exclut plus rien.**""",
    """**Ce que le Chapitre 11 ajoute.** Son entrée est le second cas du module, après le Chapitre 9, où la
précision **naît de l'écriture et non du registre** — mais pour un motif différent : aucune entrée n'était
connue d'avance, le chapitre n'ayant jamais été écrit. Elle confirme surtout la leçon des Chapitres 7 et 10
pour la troisième fois : **l'ancre est une réserve que le corps posait déjà**. Le corps écrit que l'impôt ne
se calcule que sur un bénéfice, « jamais sur une perte », et ne disait rien de ce qui arrive dans l'autre
cas. Trois attestations font de ce patron le premier endroit où chercher, avant même d'ouvrir le registre.

**`statut lecteur` reste renseigné, mais n'exclut plus rien.**""",
    'leçon du Chapitre 11')

open(F, 'w', encoding='utf-8').write(s)
print(f'registre mis à jour — {n} entrées, six neuves au Chapitre 11')
