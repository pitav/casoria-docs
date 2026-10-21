#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Porte au registre des écarts les cinq entrées du Chapitre 12 et la sortie
par le haut de l'entrée 1.5.

Le registre est le seul document de référence touché avant validation : sa
propre règle l'impose — « au fil de la rédaction, jamais après ». Le déroulé,
la charte et le journal attendent la relecture profane.

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


# ─── 1. les cinq entrées du Chapitre 12 ─────────────────────────────────────
ENTREES = """### Chapitre 12 — Piloter

| # | Écart | Nature | Statut lecteur | Destination | Formulation |
|---|---|---|---|---|---|
| 12.1 | Les autres outils de lecture d'un bilan | notion non traitée | silencieux | candidat | Trois nombres ne font pas une lecture complète. Un banquier en regarde d'autres : ce que l'entreprise rapporte à l'argent que ses associés y ont mis, le nombre de jours de vente que représente son stock, la part de son résultat qui suffirait à rembourser ses emprunts. Chacun répond à une question différente, et aucun ne se lit seul. |
| 12.2 | Le besoin en fonds de roulement réduit à trois postes | simplification de la simulation | signalé (une phrase du corps) | candidat | Le calcul du chapitre retient le stock, les créances clients et les dettes fournisseurs. Un vrai besoin en fonds de roulement ajoute tout ce que l'exploitation doit ou avance par ailleurs : les cotisations sociales dues, la taxe due à l'État, les charges payées d'avance et les produits encaissés d'avance. Toutes ces lignes figurent au Bilan de Latitude Café, et les retenir donnerait un nombre plus bas que 69 000 €. |
| 12.3 | Le financement du besoin, fonds de roulement et trésorerie nette | notion non traitée | silencieux | candidat | Le chapitre dit combien l'exploitation retient d'argent, il ne dit pas avec quoi ce besoin est financé. C'est pourtant la question suivante. Une entreprise le couvre avec les ressources dont elle dispose pour longtemps, le capital, les sommes prêtées par ses associés, la part d'emprunt qu'elle n'a pas encore remboursée, et ce qui dépasse ce besoin se retrouve sur son compte en banque. Le rapprochement des deux est ce qu'un banquier regarde avant la trésorerie elle-même. |
| 12.4 | Les financements de court terme | notion non traitée | silencieux | module ultérieur | Une entreprise dont les clients paient à soixante ou quatre-vingt-dix jours n'est pas obligée d'attendre son argent. Sa banque peut lui avancer le montant des factures non encore payées ou lui autoriser un découvert, et une société spécialisée peut lui racheter ses créances. Ces solutions ont toutes un coût, et elles existent précisément pour le problème que ce chapitre décrit. |
| 12.5 | Où trouver les repères sectoriels | notion non traitée | signalé (une phrase du corps) | candidat | Le chapitre dit de comparer ses ratios à ceux d'entreprises du même métier, sans dire où on les trouve. Ils existent : les organisations professionnelles publient des moyennes par secteur, la Banque de France en tient pour la plupart des activités, et un expert-comptable les a sous la main. Une marge nette de 10 % ne vaut pas la même chose dans la torréfaction et dans le commerce de gros. |

### Chapitre 13

*À remplir à la rédaction.*
"""

rep("""### Chapitres 12, 13

*À remplir à la rédaction.*
""", ENTREES, 'entrées du Chapitre 12')

# ─── 2. la sortie par le haut de 1.5, dans un autre chapitre que le sien ────
rep('| 1.5 | Les colonnes N et N–1 d\'un état financier | simplification de la simulation | silencieux | candidat |',
    '| 1.5 | Les colonnes N et N–1 d\'un état financier | simplification de la simulation | '
    'signalé (précision du Chapitre 12) | **précision** |',
    'destination de 1.5')

rep("""**Note sur 1.5, la plus sérieuse des cinq qui restent.** C'est le seul écart du Chapitre 1 qui porte sur ce que le lecteur
verra à coup sûr le jour où il ouvrira de vrais comptes, et sur quoi le module ne l'aura jamais entraîné :
deux colonnes de chiffres au lieu d'une. La grille du module ne peut pas la porter, puisque Latitude Café
n'a pas d'exercice précédent. **Piste alternative à l'aside, à examiner au Chapitre 12 plutôt qu'au 13 :**
ce chapitre lit le Bilan de clôture pour décider ; une deuxième colonne fictive y trouverait un emploi réel,
et l'écart cesserait d'en être un.""",
    """**Sortie par le haut de 1.5 — 25 août 2026, et elle remonte dans un autre chapitre que le sien.**
C'était le seul écart du Chapitre 1 portant sur ce que le lecteur verra à coup sûr le jour où il ouvrira de
vrais comptes, et sur quoi le module ne l'aura jamais entraîné : deux colonnes de chiffres au lieu d'une.
Le Chapitre 1 ne pouvait pas la porter, le lecteur y regardant une grille vierge. **Elle remonte donc au
Chapitre 12**, ancrée sur « tout seul », au troisième sous-titre, sur la réserve que le corps pose en
écrivant qu'un ratio ne dit rien seul. C'est **le premier cas du module où une entrée sort par le haut dans
un autre chapitre que celui qui l'a produite**, et la piste était ouverte par la fiche du Chapitre 12
elle-même : c'est le seul chapitre qui lit le Bilan de fin d'exercice pour trancher une décision, et
comparer deux exercices est exactement ce qu'un lecteur fait devant de vrais comptes.
Test de la charte, section 20 : une phrase et un repère dans un champ restreint, donc elle remonte ; le
lecteur peut l'ignorer sans que rien de ce qui suit devienne faux, et elle n'explique l'origine d'aucun
nombre. **Quatre entrées restent candidates pour le Chapitre 1**, dont 1.6, qui est sur le même terrain et
reste seule à apprendre la méfiance devant une comparaison.""",
    'note sur 1.5')

rep('le lecteur peut l\'ignorer sans que rien de ce qui suit devienne faux, et elle n\'explique l\'origine d\'aucun\nnombre. Cinq entrées restent candidates pour ce chapitre.',
    'le lecteur peut l\'ignorer sans que rien de ce qui suit devienne faux, et elle n\'explique l\'origine d\'aucun\nnombre. Quatre entrées restent candidates pour ce chapitre, 1.5 étant sortie par le haut à son tour.',
    'compte des candidates du Chapitre 1')

# ─── 3. la liste des sorties par le haut ────────────────────────────────────
rep("""déficit sur les bénéfices des années suivantes, ancrée sur « perte » au Chapitre 11.
**Les onze chapitres écrits en portent donc chacun une.**""",
    """déficit sur les bénéfices des années suivantes, ancrée sur « perte » au Chapitre 11 ; et 1.5, les deux
colonnes d'un vrai état financier, ancrée sur « tout seul » au Chapitre 12 — la seule qui remonte dans un
autre chapitre que celui qui l'a produite.
**Les douze chapitres écrits en portent donc chacun une.**""",
    'liste des sorties par le haut')

rep('**Dix entrées sont sorties par le haut et sont écrites**, au 25 août 2026 :',
    '**Onze entrées sont sorties par le haut et sont écrites**, au 25 août 2026 :',
    'compte des sorties par le haut')

# ─── 4. ce que le Chapitre 12 ajoute à la règle ─────────────────────────────
rep("""**`statut lecteur` reste renseigné, mais n'exclut plus rien.**""",
    """**Ce que le Chapitre 12 ajoute, et c'est une règle nouvelle.** Une entrée peut sortir par le haut dans
**un autre chapitre que celui qui l'a produite**. 1.5 est née au Chapitre 1 et remonte au Chapitre 12,
parce que la note ne vaut que là où le lecteur a la chose sous les yeux — et il n'a un Bilan chiffré à lire
qu'à la fin. Le corollaire est un ordre de travail : **une entrée refusée comme précision de son propre
chapitre n'est pas pour autant condamnée à l'aside**, elle attend le chapitre où son ancre existe. Il
confirme aussi le patron pour la quatrième fois, l'ancre étant une réserve que le corps posait déjà.

**`statut lecteur` reste renseigné, mais n'exclut plus rien.**""",
    'leçon du Chapitre 12')

# ─── 5. les nombres annoncés, tous recomptés par script ─────────────────────
lignes = re.findall(r'^\| (\d+\.\d+) \|(.*)$', s, re.M)
n = len(lignes)
dest = [l.split('|')[3].strip() for _, l in lignes]
n_prec = sum(d == '**précision**' for d in dest)
n_ult = sum(d == 'module ultérieur' for d in dest)
n_cand = n - n_prec - n_ult
assert n_prec + n_ult + n_cand == n

rep('**57 entrées au 25 août 2026**, après le Chapitre 11. Toutes formulées. Recomptées par script.',
    f'**{n} entrées au 25 août 2026**, après le Chapitre 12. Toutes formulées. Recomptées par script.',
    'compte annoncé en tête')

rep("""**Décompte à ce jour : 57 entrées, toutes formulées, recomptées par script.** Cinquante-quatre candidates
à l'aside, une en `module ultérieur` — 11.5, la fiscalité du dividende chez l'associé — et deux remontées
en précision, 3.5 au Chapitre 3 et 10.1 au Chapitre 10.""",
    f"""**Décompte à ce jour : {n} entrées, toutes formulées, recomptées par script.** {n_cand} candidates à
l'aside, {n_ult} en `module ultérieur` — 11.5, la fiscalité du dividende chez l'associé, et 12.4, les
financements de court terme — et {n_prec} remontées en précision, une par chapitre écrit.

**Ce décompte était faux, et c'est le quatorzième nombre annoncé pris en défaut dans le module.** La
version précédente annonçait cinquante-quatre candidates et deux remontées en précision, quand le fichier
en portait déjà dix. Le total tombait juste, ce qui est précisément ce qui l'a rendu invisible : un nombre
qu'aucune règle ne recalcule dérive sans que rien ne le signale (charte, section 21). Les trois sous-totaux
se recomptent désormais par script, à la même passe que le total.""",
    'décompte du tri')

open(F, 'w', encoding='utf-8').write(s)
print(f'registre mis à jour — {n} entrées ({n_cand} candidates, {n_prec} précisions, '
      f'{n_ult} module ultérieur), cinq neuves au Chapitre 12 et la sortie de 1.5')
