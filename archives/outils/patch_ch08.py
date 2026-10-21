#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Passe des deux-points du Chapitre 8. Pas de précision nouvelle : le chapitre
porte déjà la sienne, « cinq ans », et la charte n'en autorise qu'une.
Chaque substitution est assertée unique : rien d'autre ne bouge.
"""
import re

SRC = 'v08-original.html'
DST = 'ch08-travail.html'
NB = '\u00a0'
assert NB == chr(160), 'NB doit être un insécable, pas un espace ordinaire'

s = open(SRC, encoding='utf-8').read()
avant = s

def sub(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, f'{c} occurrence(s) au lieu de {n} pour : {old[:70]!r}'
    s = s.replace(old, new)

# ═══ 1. Vidéo · 2 → 1 ═══════════════════════════════════════════════════════
# Gardé : le premier, dénombrement suivi de ses trois éléments.
sub("La vidéo pose la\nquestion du chapitre : à partir de quand une entreprise cesse d'acheter ce qu'elle consomme et commence à\ninvestir, et pourquoi la réponse change entièrement la lecture de ses deux documents.",
    "La vidéo pose la\nquestion du chapitre, celle du moment où une entreprise cesse d'acheter ce qu'elle consomme et commence à\ninvestir, et de ce que la réponse change à la lecture de ses deux documents.")

# ═══ 2. Accroche · 2 → 1 ════════════════════════════════════════════════════
# Gardé : le premier, qui chiffre la sortie de trésorerie.
sub("le total des charges ne\nbougera pas d'un euro : il restera à 81" + NB + "087,50" + NB + "€.",
    "le total des charges ne\nbougera pas d'un euro. Il restera à 81" + NB + "087,50" + NB + "€.")

# ═══ 3. Premier sous-titre · 5 → 1 ══════════════════════════════════════════
sub("n'a acheté que des choses qui disparaissent : du café vert qu'elle\ntorréfie et qu'elle vend, de l'électricité qu'elle brûle.",
    "n'a acheté que des choses qui disparaissent, du café vert qu'elle\ntorréfie et qu'elle vend, de l'électricité qu'elle brûle.")

sub("Un torréfacteur de 15 kg ne disparaît pas\nainsi : il sera encore là dans cinq ans,",
    "Un torréfacteur de 15 kg ne disparaît pas\nainsi. Il sera encore là dans cinq ans,")

# gardé : la définition que la relecture du 22 août a arrêtée mot pour mot
assert s.count("n'est pas une charge : c'est un\n<span class=\"lex\">investissement</span>.") == 1

sub("Là, ce bien a un nom : c'est une <span class=\"lex\">immobilisation</span>.",
    "Là, ce bien a un nom. C'est une <span class=\"lex\">immobilisation</span>.")

sub("Elle se récupère comme celle payée sur le café vert : c'est de la TVA déductible, vue au\nChapitre 5, que l'entreprise retranchera de ce qu'elle doit à l'État.",
    "Elle se récupère comme celle payée sur le café vert. C'est de la TVA déductible, vue au\nChapitre 5, que l'entreprise retranchera de ce qu'elle doit à l'État.")

# ─── légende du bloc 1 · 1 → 0 ──────────────────────────────────────────────
sub("Au Compte de Résultat, rien : le total des charges reste à 81" + NB + "087,50" + NB + "€.",
    "Au Compte de Résultat, rien. Le total des charges reste à 81" + NB + "087,50" + NB + "€.")

# ═══ 4. Deuxième sous-titre · 9 → 1 ═════════════════════════════════════════
sub("et le torréfacteur se consomme lui aussi : pas d'un coup\nle jour où on le paie, mais un peu chaque jour où il tourne.",
    "et le torréfacteur se consomme lui aussi, pas d'un coup\nle jour où on le paie, mais un peu chaque jour où il tourne.")

sub("et elle l'inscrit lentement : elle étale le prix du bien sur sa\ndurée d'usage et en compte une part par année.",
    "et elle l'inscrit lentement. Elle étale le prix du bien sur sa\ndurée d'usage et en compte une part par année.")

sub("partage la valeur du bien en parts égales, une par année d'usage : c'est\nl'<span class=\"lex\">amortissement linéaire</span>.",
    "partage la valeur du bien en parts égales, une par année d'usage. C'est\nl'<span class=\"lex\">amortissement linéaire</span>.")

sub("ici <button type=\"button\" class=\"prec\" aria-describedby=\"p8-duree\">cinq ans</button> :\n36" + NB + "000" + NB + "€ étalés sur cette durée donnent 7" + NB + "200" + NB + "€ par an.",
    "ici <button type=\"button\" class=\"prec\" aria-describedby=\"p8-duree\">cinq" + NB + "ans</button>.\nÉtalés sur cette durée, les 36" + NB + "000" + NB + "€ donnent 7" + NB + "200" + NB + "€ par an.")

# la note de précision est de la prose et entre au budget comme le reste
sub("Cinq ans n'est ni une règle ni un hasard : c'est la durée\npendant laquelle l'entreprise pense se servir de la machine, et c'est elle qui l'estime. Les usages donnent\ndes repères : trois ans pour un ordinateur,",
    "Cinq ans n'est ni une règle ni un hasard. C'est la durée\npendant laquelle l'entreprise pense se servir de la machine, et c'est elle qui l'estime. Les usages donnent\ndes repères, trois ans pour un ordinateur,")

sub("ce qu'on appelle le <span class=\"lex\">prorata temporis</span> : la moitié de 7" + NB + "200" + NB + "€, soit 3" + NB + "600" + NB + "€.",
    "ce qu'on appelle le <span class=\"lex\">prorata temporis</span>. La moitié de 7" + NB + "200" + NB + "€, soit\n3" + NB + "600" + NB + "€.")

sub("Ces 3" + NB + "600" + NB + "€ sont une charge : l'entreprise a réellement consommé six mois de machine.",
    "Ces 3" + NB + "600" + NB + "€ sont une charge. L'entreprise a réellement consommé six mois de machine.")

# gardé : la glose du dernier terme du chapitre, en quatre mots
assert s.count("C'est la <span class=\"lex\">valeur nette comptable</span> de la machine : ce qu'elle vaut\nencore dans les comptes.") == 1

# ─── légende du bloc 2 · 2 → 0 ──────────────────────────────────────────────
sub("Regardez le Compte de Résultat avant de passer le bloc, puis après : le total des charges\nmonte de 81" + NB + "087,50" + NB + "€ à 84" + NB + "687,50" + NB + "€,",
    "Regardez le Compte de Résultat avant de passer le bloc, puis après. Le total des charges\nmonte de 81" + NB + "087,50" + NB + "€ à 84" + NB + "687,50" + NB + "€,")

sub("Aucun montant négatif n'est écrit nulle\npart : la machine est arrivée à l'Actif par un débit,",
    "Aucun montant négatif n'est écrit nulle\npart. La machine est arrivée à l'Actif par un débit,")

# ═══ 5. Troisième sous-titre · 8 → 1 ════════════════════════════════════════
sub("relire les deux\ndocuments avec les deux questions du Chapitre 1 : où est l'argent de l'entreprise\net d'où vient-il, qu'est-ce que son activité a consommé et gagné depuis janvier.",
    "relire les deux\ndocuments avec les deux questions du Chapitre 1. Où est l'argent de l'entreprise\net d'où vient-il, qu'est-ce que son activité a consommé et gagné depuis janvier.")

sub("Rien de tout cela ne se ressemble, mais tout y figure pour\nla même raison : c'est ce que l'entreprise détient. En face, au Passif, se lit d'où chaque euro est venu :\ndes associés, de la banque, des fournisseurs, de l'État.",
    "Rien de tout cela ne se ressemble, et tout y figure pourtant pour\nla même raison. C'est ce que l'entreprise détient. En face, au Passif, se lit d'où chaque euro est venu.\nDes associés, de la banque, des fournisseurs, de l'État.")

sub("et elle a été annoncée dès le Chapitre 2 : les deux totaux ne sont\npas égaux,",
    "et elle a été annoncée dès le Chapitre 2. Les deux totaux ne sont\npas égaux,")

sub("filtrez-le sur le\ncompte 512, celui de la trésorerie : treize lignes s'affichent, une par mouvement depuis janvier.",
    "filtrez-le sur le\ncompte 512, celui de la trésorerie. Treize lignes s'affichent, une par mouvement depuis janvier.")

sub("Ici, les deux colonnes d'un seul compte n'ont aucune\nraison d'être égales : c'est leur différence qui compte, et c'est elle que le Bilan affiche.",
    "Ici, les deux colonnes d'un seul compte n'ont aucune\nraison d'être égales. C'est leur différence qui compte, et c'est elle que le Bilan affiche.")

# gardé : la chute du point d'étape, et le geste du sous-titre
assert s.count("remplirait à côté du journal : c'est le journal résumé, compte par compte.") == 1

# ─── légende d'illustration · 3 → 1, le parallèle « En haut / En bas » gardé ─
sub("En haut, la grille de ce module :\ndeux lignes à l'Actif, 36" + NB + "000" + NB + "€ pour la machine et 3" + NB + "600" + NB + "€ qui s'en retranchent juste\ndessous, la soustraction restant à faire. En bas, la présentation\nd'un vrai bilan : une seule ligne et trois colonnes, brut 36" + NB + "000" + NB + "€, amortissements 3" + NB + "600" + NB + "€, net 32" + NB + "400" + NB + "€.",
    "En haut, la grille de ce module montre\ndeux lignes à l'Actif, 36" + NB + "000" + NB + "€ pour la machine et 3" + NB + "600" + NB + "€ qui s'en retranchent juste\ndessous, la soustraction restant à faire. En bas, la présentation\nd'un vrai bilan tient en une seule ligne et trois colonnes, brut 36" + NB + "000" + NB + "€, amortissements 3" + NB + "600" + NB + "€, net 32" + NB + "400" + NB + "€.")

# ─── l'alerte ───────────────────────────────────────────────────────────────
sub("L'Actif de la grille, par ailleurs, n'a qu'une colonne : c'est\ncelle que l'illustration ci-dessus appelle le net.",
    "L'Actif de la grille, par ailleurs, n'a qu'une colonne, celle que l'illustration ci-dessus appelle le\nnet.")

# ═══ 6. Bloc de clôture · 1 → 0 ═════════════════════════════════════════════
sub("et cette part-là est une charge : 3" + NB + "600" + NB + "€ ici, pour six mois de machine sur les soixante qu'elle servira.",
    "et cette part-là est une charge, 3" + NB + "600" + NB + "€ ici, pour six mois de machine sur les soixante qu'elle servira.")

assert s != avant
open(DST, 'w', encoding='utf-8').write(s)
print('écrit :', DST)
