#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Passe des deux-points du Chapitre 4 + pose de la précision 4.1.
Produit le fichier de travail (chapo + annexe complète).
Chaque substitution est assertée unique : rien d'autre ne bouge.
"""
import re, sys

SRC = 'v5-original.html'
DST = 'ch04-travail.html'
NB = ' '

s = open(SRC, encoding='utf-8').read()
avant = s

def sub(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, f'{c} occurrence(s) au lieu de {n} pour : {old[:70]!r}'
    s = s.replace(old, new)

# ─── 1. Vidéo d'ouverture · 2 → 1 ────────────────────────────────────────────
sub("elle annonce que ce décalage\nn'est pas un accident de janvier : c'est la situation ordinaire",
    "elle annonce que ce décalage\nn'est pas un accident de janvier, mais la situation ordinaire")

# ─── 2. Accroche · 1, au budget, inchangée ───────────────────────────────────

# ─── 3. Premier sous-titre · 4 → 1 ───────────────────────────────────────────
sub("arrivaient sur le compte le soir même : la vente\net l'argent tombaient ensemble. C'est le cas le plus simple, et c'est aussi l'exception. Entre\nprofessionnels, on livre",
    "arrivaient sur le compte le soir même. La vente\net l'argent tombaient ensemble. C'est le cas le plus simple, et c'est aussi l'exception.</p>\n"
    "\n<p>Entre professionnels, on livre")

# origine du délai au corps + ancre de la précision
sub("Le délai figure sur la facture, ici c'est trente jours.\nLa date à laquelle le paiement est dû s'appelle l'<span class=\"lex\">échéance</span>.</p>",
    "Le délai est convenu entre les deux entreprises et figure sur la facture. Ici, c'est\n"
    "<button type=\"button\" class=\"prec\" aria-describedby=\"p4-delai\">trente" + NB + "jours</button>.\n"
    "La date à laquelle le paiement est dû s'appelle l'<span class=\"lex\">échéance</span>.</p>\n"
    "\n"
    "<p class=\"prec-note\" id=\"p4-delai\" role=\"note\">Les deux entreprises ne sont pourtant pas\n"
    "entièrement libres. Entre\n"
    "professionnels, la loi française plafonne le délai de paiement à soixante" + NB + "jours à compter de la\n"
    "facture, et un délai plus long expose les deux entreprises à une amende. Un client qui paie en retard\n"
    "doit des pénalités dès le lendemain de l'échéance, même si personne ne les lui réclame.</p>")

# celui-ci reste : il répond à la question posée juste au-dessus
assert s.count("Le Chapitre 1 a déjà donné la réponse : dans le Compte de") == 1

sub("dépendrait alors de la ponctualité des\nclients : deux entreprises",
    "dépendrait alors de la ponctualité des\nclients. Deux entreprises")

# parallèle avec « une dette fournisseur, une somme facturée par… » du bloc suivant
sub("C'est une <span class=\"lex\">créance client</span> :\nune somme facturée à un client et pas encore reçue.",
    "C'est une <span class=\"lex\">créance client</span>,\nune somme facturée à un client et pas encore reçue.")

# légende d'illustration · 3 → 1 (le « Légende : » de format reste)
sub("À gauche, au\nCompte de Résultat : la vente est faite, le produit est compté. À droite, à l'Actif du Bilan : ce que Le\nComptoir des Halles doit encore, et qui n'est pas encore de l'argent.",
    "À gauche, au\nCompte de Résultat, la vente est faite et le produit est compté. À droite, à l'Actif du Bilan, ce que Le\nComptoir des Halles doit encore, et qui n'est pas encore de l'argent.")

# légende du bloc 1 · 1 → 0
sub("la facture ; en face, ce n'est pas de l'argent qui entre : c'est ce que le client doit encore, inscrit à\nl'Actif.",
    "la facture. En face, ce n'est pas de l'argent qui entre, mais ce que le client doit encore, inscrit à\nl'Actif.")

# ─── 4. Deuxième sous-titre · 3 → 1 ──────────────────────────────────────────
sub("L'argent quittera le compte le 4 mars : ce sera un <span class=\"lex\">décaissement</span>",
    "L'argent quittera le compte le 4 mars. Ce sera un <span class=\"lex\">décaissement</span>")

# celui-ci reste : il porte la démonstration du sous-titre
assert s.count("l'activité l'a consommé : la\ncharge se compte dès la facture") == 1

sub("la colonne qui dit d'où vient l'argent : pendant trente jours, c'est Verdecafé\nqui finance ce lot.",
    "la colonne qui dit d'où vient l'argent. Pendant trente jours, c'est Verdecafé\nqui finance ce lot.")

# légende du bloc 2 · 1 → 0
sub("et n'a rien sorti\nde son compte : la contrepartie est une dette, au Passif.",
    "et n'a rien sorti\nde son compte. La contrepartie est une dette, au Passif.")

# ─── 5. Troisième sous-titre · 3 → 1 ─────────────────────────────────────────
sub("des deux ne concerne le Compte de Résultat : elles sont toutes les deux à l'Actif du Bilan.",
    "des deux ne concerne le Compte de Résultat. Elles sont toutes les deux à l'Actif du Bilan.")

sub("l'argent en banque monte de 1" + NB + "450" + NB + "€. L'entreprise ne détient ni plus ni moins qu'avant :\n"
    "une promesse de paiement est devenue de l'argent.</p>",
    "l'argent en banque monte de 1" + NB + "450" + NB + "€.</p>\n"
    "\n<p>L'entreprise ne détient ni plus ni moins qu'avant. Une promesse de paiement est devenue de\n"
    "l'argent.</p>")

# celui-ci reste : il installe le refrain du module
assert s.count("C'est la phrase qui traverse tout le reste de la formation : le résultat n'est pas la trésorerie.") == 1

# ─── 6. Bloc de clôture · 2 → 0 ──────────────────────────────────────────────
sub("L'attente porte un nom de chaque côté : une créance client",
    "L'attente porte un nom de chaque côté. Une créance client")

sub("Le jour du règlement, seul le Bilan bouge : ce que le client devait tombe à zéro,",
    "Le jour du règlement, seul le Bilan bouge. Ce que le client devait tombe à zéro,")

# ─── contrôle : rien n'a bougé hors des substitutions ────────────────────────
assert s != avant
open(DST, 'w', encoding='utf-8').write(s)
print('écrit :', DST)
