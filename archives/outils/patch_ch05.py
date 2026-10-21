#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Passe des deux-points du Chapitre 5 + pose de la précision 5.5.
Produit le fichier de travail (chapo + annexe complète).
Chaque substitution est assertée unique : rien d'autre ne bouge.
"""
import re

SRC = 'v05-original.html'
DST = 'ch05-travail.html'
NB = ' '

s = open(SRC, encoding='utf-8').read()
avant = s

def sub(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, f'{c} occurrence(s) au lieu de {n} pour : {old[:70]!r}'
    s = s.replace(old, new)

# ═══ 1. Vidéo d'ouverture · 3 → 1 ═══════════════════════════════════════════
# Gardé : le premier, qui pose la thèse du chapitre.
sub("La vidéo suit cette taxe de bout en bout : du client à Latitude Café, puis de Latitude Café\nà l'État.",
    "La vidéo suit cette taxe de bout en bout, du client à Latitude Café, puis de Latitude Café\nà l'État.")

sub("celle qui surprend le plus quand on découvre un compte\nen banque d'entreprise : cet argent est bien arrivé sur le compte, mais a-t-il jamais appartenu à\nl'entreprise ?",
    "celle qui surprend le plus quand on découvre un compte\nen banque d'entreprise. Cet argent est bien arrivé sur le compte, mais a-t-il jamais appartenu à\nl'entreprise ?")

# ═══ 2. Accroche · 2 → 1 ════════════════════════════════════════════════════
# Gardé : le second, qui porte la tension de l'accroche.
sub("Le premier trimestre de Latitude Café est terminé : 46" + NB + "800" + NB + "€ facturés aux\ncafés et restaurants ou encaissés au comptoir.",
    "Le premier trimestre de Latitude Café est terminé, 46" + NB + "800" + NB + "€ facturés aux\ncafés et restaurants ou encaissés au comptoir.")

# ═══ 3. Premier sous-titre · 9 → 1 ══════════════════════════════════════════
# Gardé : l'énumération des trois montants, reprise par « tous ces montants ».
assert s.count("de café vert livrés par Verdecafé : tous ces montants") == 1

sub("à un taux fixé par la loi et non par le vendeur :\nici, 20" + NB + "%.",
    "à un taux fixé par la loi et non par le vendeur. Ici, 20" + NB + "%.")

# les deux gloses de lexique se ponctuent pareil, comme au Chapitre 4
sub("C'est la <span class=\"lex\">TVA collectée</span> : la taxe facturée aux clients.",
    "C'est la <span class=\"lex\">TVA collectée</span>, la taxe facturée aux clients.")

sub("C'est la <span class=\"lex\">TVA déductible</span> : la taxe payée aux fournisseurs, et\nrécupérable.",
    "C'est la <span class=\"lex\">TVA déductible</span>, la taxe payée aux fournisseurs et\nrécupérable.")

sub("Cette taxe-là, elle ne la supporte pas non plus : elle la retranchera de ce\nqu'elle doit à l'État.",
    "Cette taxe-là, elle ne la supporte pas non plus. Elle la retranchera de ce\nqu'elle doit à l'État.")

# le numéro de compte ne reste jamais seul : chacun garde son libellé
sub("sur deux comptes séparés : le compte 4457 pour la TVA collectée, le compte 4456 pour la TVA\ndéductible.",
    "sur deux comptes séparés. Le compte 4457 reçoit la TVA collectée, le compte 4456 la TVA\ndéductible.")

sub("C'est un raccourci de la formation : une vraie comptabilité\nenregistre chaque facture séparément",
    "C'est un raccourci de la formation. Une vraie comptabilité\nenregistre chaque facture séparément")

sub("taxe comprise cette fois, et il n'y a rien à\nressaisir : l'application s'en charge.",
    "taxe comprise cette fois, et il n'y a rien à\nressaisir. L'application s'en charge.")

# ─── légende d'illustration · 2 → 1 (le « Légende : » de format reste) ───────
sub("Latitude Café, elle, y lit deux montants : 10" + NB + "€ hors taxes, qui sont le prix de son café,\net 2" + NB + "€ de taxe, qu'elle reçoit pour l'État et devra lui remettre.",
    "Latitude Café, elle, y lit deux montants, 10" + NB + "€ hors taxes qui sont le prix de son café,\net 2" + NB + "€ de taxe qu'elle reçoit pour l'État et devra lui remettre.")

# ─── légende du bloc 1 · 4 → 0 ──────────────────────────────────────────────
sub("Regardez la ligne\nCréances clients avant de passer le bloc : elle est à zéro.",
    "Regardez la ligne\nCréances clients avant de passer le bloc. Elle est à zéro.")

sub("C'est au Compte de Résultat que la vente de janvier est\nencore là : la ligne Ventes aux professionnels porte déjà 1" + NB + "450" + NB + "€,",
    "C'est au Compte de Résultat que la vente de janvier est\nencore là. La ligne Ventes aux professionnels porte déjà 1" + NB + "450" + NB + "€,")

sub("et Latitude Café n'a gagné que 30" + NB + "000" + NB + "€ : les 6" + NB + "000" + NB + "€\nd'écart ouvrent une troisième ligne,",
    "et Latitude Café n'a gagné que 30" + NB + "000" + NB + "€. Les 6" + NB + "000" + NB + "€\nd'écart ouvrent une troisième ligne,")

sub("Le\nChapitre 3 l'annonçait : une opération ne tient pas toujours en deux lignes.",
    "Le\nChapitre 3 l'annonçait, une opération ne tient pas toujours en deux lignes.")

# ─── phrase de liaison ──────────────────────────────────────────────────────
sub("Le reste du trimestre suit dans la foulée : ventes au comptoir, achats, charges externes, et la taxe de\nchacun.",
    "Le reste du trimestre suit dans la foulée, ventes au comptoir, achats, charges externes, et la taxe\nde chacun.")

# ─── légende du panneau, premier sous-bloc · 3 → 0 ──────────────────────────
# Le « pendant que ces six lignes s'inscrivent » est laissé en l'état : c'est
# un point de fond non tranché, signalé à l'annexe avec sa version de repli.
sub("Regardez le Compte de Résultat pendant que ces six lignes\ns'inscrivent : les ventes aux professionnels redescendent de 31" + NB + "450" + NB + "€ à 30" + NB + "000" + NB + "€, le chiffre du trimestre,\nqui comprend les 1" + NB + "450" + NB + "€ de janvier.",
    "Regardez le Compte de Résultat pendant que ces six lignes\ns'inscrivent. Les ventes aux professionnels redescendent de 31" + NB + "450" + NB + "€ à 30" + NB + "000" + NB + "€, le chiffre du\ntrimestre, qui comprend les 1" + NB + "450" + NB + "€ de janvier.")

sub("La vente au comptoir du 17 janvier fait le même chemin : elle sort ici,\net les 9" + NB + "000" + NB + "€ du trimestre, inscrits juste en dessous, la réinscrivent.",
    "La vente au comptoir du 17 janvier fait le même chemin. Elle sort ici,\net les 9" + NB + "000" + NB + "€ du trimestre, inscrits juste en dessous, la réinscrivent.")

sub("Le solde\ndu compte en banque se déplace de 270" + NB + "€ au même moment : les règlements au comptant de janvier avaient été\npassés hors taxes, et c'est le trimestre qui les porte désormais.",
    "Le solde\ndu compte en banque se déplace de 270" + NB + "€ au même moment. Les règlements au comptant de janvier avaient\nété passés hors taxes, et c'est le trimestre qui les porte désormais.")

# ─── légende du panneau, second sous-bloc · 3 → 0 ───────────────────────────
sub("Le trimestre est maintenant complet : ouvrez le grand journal et filtrez sur le\ncompte 4457, celui de la TVA collectée : il porte 7" + NB + "800" + NB + "€. Puis sur le 4456, celui de la TVA déductible :\n6" + NB + "600" + NB + "€.",
    "Le trimestre est maintenant complet. Ouvrez le grand journal et filtrez sur le\ncompte 4457, celui de la TVA collectée, qui porte 7" + NB + "800" + NB + "€. Puis sur le compte 4456, celui de la TVA\ndéductible, qui porte 6" + NB + "600" + NB + "€.")

# ═══ 4. Deuxième sous-titre · 3 → 0 ═════════════════════════════════════════
# Le symbole € manquait sur la seconde somme ; la coupe rend l'ellipse illisible.
sub("les deux comptes de taxe portent son total : Latitude Café a facturé 7" + NB + "800" + NB + "€ de taxe à ses clients et en a payé 6" + NB + "600 à ses fournisseurs.",
    "les deux comptes de taxe portent son total. Latitude Café a facturé\n7" + NB + "800" + NB + "€ de taxe à ses clients et en a payé 6" + NB + "600" + NB + "€ à ses fournisseurs.")

# la glose du terme prend la même forme qu'aux deux autres du chapitre,
# et l'ancre de la précision se pose sur ce que le lecteur a sous les yeux
sub("et n'inscrit que leur\ndifférence : la\n<span class=\"lex\">TVA à décaisser</span>, la somme réellement due à l'État. Pour le premier trimestre,\n1" + NB + "200" + NB + "€.</p>",
    "et n'inscrit que leur\ndifférence. C'est la <span class=\"lex\">TVA à décaisser</span>, la somme réellement\n"
    "<button type=\"button\" class=\"prec\" aria-describedby=\"p5-exigible\">due" + NB + "à" + NB + "l'État</button>.\n"
    "Pour le premier trimestre, 1" + NB + "200" + NB + "€.</p>\n"
    "\n"
    "<p class=\"prec-note\" id=\"p5-exigible\" role=\"note\">L'entreprise la doit dès qu'elle facture, sans\n"
    "attendre d'être payée. Les 1" + NB + "200" + NB + "€ du trimestre partiront au Trésor public même si les clients\n"
    "n'ont pas encore réglé, et le Chapitre 4 a montré qu'une facture professionnelle attend son échéance.\n"
    "La règle change pourtant avec le métier. Qui vend des services ne doit sa taxe qu'une fois encaissé, ce\n"
    "qui protège sa trésorerie là où celle du vendeur de biens souffre.</p>")

sub("a payé plus de taxe qu'elle n'en a facturé : c'est alors l'État qui lui doit la différence, et\nelle en demande le remboursement.",
    "a payé plus de taxe qu'elle n'en a facturé. C'est alors l'État qui lui doit la différence, et\nelle en demande le remboursement.")

# ─── légende du bloc 2 · 1 → 0 ──────────────────────────────────────────────
sub("Les deux comptes de taxe\ntombent à zéro : ils avaient servi à compter, ils n'ont plus rien à porter.",
    "Les deux comptes de taxe\ntombent à zéro. Ils avaient servi à compter, ils n'ont plus rien à porter.")

# ═══ 5. Troisième sous-titre · 4 → 1 ════════════════════════════════════════
sub("Le Compte de Résultat le confirme : il porte 30" + NB + "000" + NB + "€ de ventes aux professionnels et 9" + NB + "000" + NB + "€ de ventes\nau comptoir,",
    "Le Compte de Résultat le confirme. Il porte 30" + NB + "000" + NB + "€ de ventes aux professionnels et 9" + NB + "000" + NB + "€ de ventes\nau comptoir,")

# gardé : il présente la reprise du refrain, comme au Chapitre 4
assert s.count("l'écart joue dans l'autre sens : la\ntrésorerie porte de l'argent que le résultat n'a jamais compté.") == 1

sub("L'entreprise ne fait que tenir la caisse de l'État : elle avance la taxe à l'achat, la reçoit à la\nvente,",
    "L'entreprise ne fait que tenir la caisse de l'État. Elle avance la taxe à l'achat, la reçoit à la\nvente,")

# ─── l'alerte ───────────────────────────────────────────────────────────────
sub("Un seul taux de TVA est retenu, 20" + NB + "% : le café relève en réalité de plusieurs taux, selon son\nconditionnement",
    "Un seul taux de TVA est retenu, 20" + NB + "%. Le café relève en réalité de plusieurs taux, selon son\nconditionnement")

# ═══ 6. Bloc de clôture · 1 → 0 ═════════════════════════════════════════════
sub("n'inscrit que leur différence, au Passif du Bilan : ce que l'entreprise doit réellement à l'État.",
    "n'inscrit que leur différence, au Passif du Bilan. C'est ce que l'entreprise doit réellement à l'État.")

assert s != avant
open(DST, 'w', encoding='utf-8').write(s)
print('écrit :', DST)
