#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Porte le grand journal au déroulé (v26 → v27).

Aucune écriture ne bouge : le total de contrôle reste à 1 294 694,00 €.
Chaque substitution est assertée unique. Le fichier est écrit à la toute fin :
une assertion qui saute le laisse intact (règle 4 des documents de référence).

Règle 1 : une version ne garde que son propre bloc « Changements ». Celui de la
v26 saute. Règle 2 : la chronologie dégage, le raisonnement reste.
"""
import re

NB = chr(0xA0)
assert ord(NB) == 0xA0  # jamais l'insécable au clavier ici : l'outil d'écriture le dégrade

DER_IN = 'deroule-comprendre-la-comptabilite-v26.corps.html'
DER_OUT = 'deroule-comprendre-la-comptabilite-v27.corps.html'


class Doc:
    def __init__(self, path):
        self.path = path
        self.s = open(path, encoding='utf-8').read()
        self.n = 0

    def rep(self, old, new, label, n=1):
        c = self.s.count(old)
        assert c == n, f'{self.path} — {label} : {c} occurrence(s), {n} attendue(s)'
        self.s = self.s.replace(old, new, n)
        self.n += 1

    def rep_bloc(self, debut, fin, new, label):
        assert self.s.count(debut) == 1, f'{self.path} — {label} : début non unique'
        i = self.s.find(debut)
        j = self.s.find(fin, i)
        assert j >= 0, f'{self.path} — {label} : fin introuvable'
        self.s = self.s[:i] + new + self.s[j + len(fin):]
        self.n += 1

    def compte(self, motif, n, label):
        c = self.s.count(motif)
        assert c == n, f'{self.path} — {label} : {c} occurrence(s) de « {motif} », {n} attendue(s)'

    def write(self, path):
        open(path, 'w', encoding='utf-8').write(self.s)
        print(f'   {path} — {self.n} substitutions, {len(self.s)} caractères')


d = Doc(DER_IN)

# ═══════════════════════════════════════════════════════════════════════════
#  EN-TÊTE
# ═══════════════════════════════════════════════════════════════════════════
d.rep('<p class="kicker">Casoria • Document de référence • v26</p>',
      '<p class="kicker">Casoria • Document de référence • v27</p>', 'kicker')

d.rep_bloc('<p class="chapo">Déroulé annoté', '</p>', """<p class="chapo">Déroulé annoté de la formation. Treize chapitres, un exercice complet
simulé de la création à la clôture, sur le fil rouge d'une PME fictive. <strong>Cette v27 écrit le grand
journal côté application</strong>&nbsp;: ce qu'il reçoit, ce qu'il affiche, et les deux seuls endroits où il
sort de son rôle de vue. Elle nomme les quatre lignes qui s'y saisissent, faute de case ailleurs&nbsp;;
elle remonte ici la seule ligne du module qui ne passe pas par lui&nbsp;; elle dit ce que porte sa colonne
de libellé et fixe les trois dates que ni ce document ni les chapitres ne donnaient. Le compte 512 porte
désormais son nom réel, Banque, et le terme pédagogique Trésorerie en seconde ligne. Le point ouvert de la
v26 sur le nombre de comptes est fermé. <strong>Aucune écriture ne bouge</strong>&nbsp;: le total de
contrôle du module reste à 1&nbsp;294&nbsp;694,00&nbsp;€ au débit comme au crédit, et le Bilan de l'exercice
sur 130&nbsp;410&nbsp;€. La charte reste en v16, inchangée.</p>""", 'chapo')

d.rep_bloc('<tr><td class="cle">Documents liés</td>', '</tr>',
           """<tr><td class="cle">Documents liés</td><td>Charte de rédaction Casoria v16 — règles de forme,
applicables à tous les modules. Ce déroulé ne les répète pas, il s'y réfère par numéro de section. La charte
est inchangée, et tous les renvois faits d'ici restent valides.</td></tr>""", 'documents liés')

# ═══════════════════════════════════════════════════════════════════════════
#  BLOC « CHANGEMENTS » — celui de la v26 saute
# ═══════════════════════════════════════════════════════════════════════════
d.rep_bloc('<h2>Changements v26</h2>', '</ul>', """<h2>Changements v27</h2>
<p>Le grand journal passe du déroulé à l'application, et cette version écrit ce qui n'y était pas.
<strong>Rien de ce qui suit ne passe une écriture</strong>&nbsp;: le total de contrôle du module reste à
1&nbsp;294&nbsp;694,00&nbsp;€ au débit comme au crédit.</p>
<ul>
<li><strong>La clause de saisie est complète.</strong> La section 2 disait déjà que le journal se remplit en
conséquence et jamais par une seconde saisie&nbsp;; la section 4 écrivait que la saisie se fait «&nbsp;dans
les composants du grand journal, du Bilan et du Compte de Résultat&nbsp;». Les deux ne sont vraies ensemble
que d'une seule façon, désormais écrite&nbsp;: <strong>le journal est en saisie pour les seules lignes dont
le compte n'a pas de case dans la grille</strong>, et il n'y en a que quatre dans tout le module, toutes de
TVA. Elles sont nommées à la section 2.</li>
<li><strong>La ligne qui ne passe pas par le journal est remontée ici.</strong> Le résultat net inscrit au
passif, au Chapitre 11, n'est pas une opération&nbsp;: c'est le solde du Compte de Résultat. Le fait était
écrit à la seule fiche du Chapitre 11. Qui lit la section 2 pour construire le journal ne pouvait pas le
savoir, et l'implémentait faux.</li>
<li><strong>Ce que porte la colonne de libellé du journal est écrit.</strong> Deux lignes dans la même
colonne&nbsp;: l'opération datée, puis le nom du compte. Le journal garde ses quatre colonnes, et le parti
est celui que la grille a retenu pour ses propres libellés.</li>
<li><strong>Trois dates sont fixées</strong>, que ni ce document ni les textes ne donnaient&nbsp;: l'achat
comptant et l'électricité du Chapitre 3, et le remboursement du compte courant du Chapitre 7. Elles
n'engageaient rien tant que le journal n'affichait pas de date&nbsp;; elles sont du contenu dès lors qu'il en
affiche une.</li>
<li><strong>Le compte 512 porte deux noms.</strong> «&nbsp;Banque&nbsp;» en première ligne, qui est son nom
réel et celui qu'emploie l'application&nbsp;; «&nbsp;Trésorerie&nbsp;» en seconde, qui est le terme du module
et celui que définit le lexique. C'est exactement la règle de la grille, appliquée au seul compte qui la
réclamait, et elle se trouvait déjà écrite sans avoir été appliquée là. <strong>Les vingt-quatre occurrences
de «&nbsp;Trésorerie&nbsp;» des chapitres livrés restent vraies</strong>, le mot étant sur la ligne.</li>
<li><strong>Le point ouvert de la v26 sur le nombre de comptes est fermé, par comptage.</strong> Le plan en
porte vingt-neuf. La grille en affiche vingt-sept — les vingt-neuf moins les deux comptes de TVA
«&nbsp;journal seul&nbsp;». Le journal en mouvemente vingt-huit — les vingt-neuf moins le 120, qui n'y passe
jamais. La phrase «&nbsp;vingt-six comptes, pas un de plus&nbsp;» était fausse de trois, et la note de la v26
qui disait vingt-sept parlait de la grille&nbsp;: elle avait raison sans le savoir.</li>
<li><strong>Ce qu'une ligne d'écriture porte côté application</strong> est écrit à la section 2&nbsp;: sa
ligne de journal, le fait qu'elle s'y saisisse ou non, et son identifiant — qui ne dépend d'aucune position,
puisqu'il conditionne la progression de l'apprenant.</li>
<li><strong>Le panneau du Chapitre 10 est complété à la section 10.</strong> Sa fiche annonçait vingt-sept
lignes automatiques et n'en listait que neuf&nbsp;: l'écriture de période du quatrième trimestre y était,
les salaires et les échéances du second semestre et les règlements de l'exercice n'y étaient pas. Les
dix-huit manquantes sont reprises telles quelles du chapitre livré, qui les porte depuis sa reprise.
<strong>Aucune n'est nouvelle</strong>, et c'est ce qui permet au total de contrôle de ne pas bouger — il
les comptait déjà. Le défaut a été trouvé en recomptant les lignes des fiches pour cette version, et il
illustre la règle&nbsp;: un nombre annoncé qu'aucun script ne recalcule dérive sans que rien ne le
signale.</li>
</ul>""", 'bloc changements')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 2 — LE GRAND JOURNAL
# ═══════════════════════════════════════════════════════════════════════════
d.rep_bloc('<p>Structure volontairement minimale', '</p>', """<p>Structure volontairement minimale : numéro de compte, libellé, débit, crédit. Les numéros de compte
sont limités au strict nécessaire et introduits sans commentaire. Le module n'enseigne pas le plan
comptable général : il enseigne le raisonnement qui remplit les colonnes. Aucun quiz ne porte sur un
numéro de compte.</p>
<div class="alert"><span class="t">Ce que porte la colonne de libellé</span>
<p><strong>Deux lignes dans la même colonne&nbsp;: l'opération datée, puis le nom du compte.</strong>
Soit, pour la première écriture du module, <code>17/01 — Vente au comptoir</code> et, dessous,
<code>Banque</code>. <strong>Le journal garde ses quatre colonnes</strong>, ce que le texte du Chapitre 3
annonce au lecteur et qui reste vrai.</p>
<p><strong>Pourquoi la question se pose.</strong> La structure ci-dessus nomme quatre colonnes dont aucune
ne porte la date ni l'opération, alors que le Chapitre 2 présente le journal comme «&nbsp;un cahier où chaque
opération est notée le jour où elle a lieu, dans l'ordre&nbsp;» et que le contrôle du Chapitre 8 demande de
le filtrer sur le compte 512&nbsp;: treize lignes s'affichent, et sans libellé d'opération elles sont treize
fois la même. <strong>Le parti des deux lignes est celui que la grille a déjà retenu</strong> pour ses
propres libellés, et il ne coûte aucune correction aux chapitres livrés.</p>
<p><strong>Ce qui n'est pas repris pour autant.</strong> Le Chapitre 3 énumère les quatre colonnes sans
mentionner l'opération datée. La phrase reste vraie et n'est pas rouverte&nbsp;; si ce chapitre l'est un
jour pour un autre motif, c'est l'endroit où l'ajouter.</p></div>
<div class="alert"><span class="t">Les dates du journal, et les trois qui manquaient</span>
<p>Le journal affiche une date courte. Les textes en fixent douze&nbsp;: 05/01, 17/01, 28/01, 02/02, 27/02,
31/03, 30/04, 01/06, 30/06, 01/07, 30/09 et 31/12. <strong>Trois ne l'étaient nulle part et sont fixées
ici.</strong></p>
<ul>
<li><strong>15/01</strong> — l'achat de café vert au comptant et l'électricité de janvier, au Chapitre 3.
Le texte pose les trois documents sur la table «&nbsp;mi-janvier&nbsp;» sans donner de jour, et la vente au
comptoir du 17 est la seule datée des trois.</li>
<li><strong>31/03</strong> — l'écriture de solde de TVA du premier trimestre, au Chapitre 5. Dans une
entreprise réelle, le solde d'un trimestre se règle le trimestre suivant&nbsp;; le module le passe fin mars,
qui est l'état où la grille l'affiche et où le texte le fait lire.</li>
<li><strong>30/06</strong> — le remboursement partiel du compte courant d'associé, au Chapitre 7. Le jalon
de la section 1 dit «&nbsp;juin&nbsp;» sans donner de jour.</li>
</ul>
<p><strong>Pourquoi elles n'engageaient rien et engagent maintenant.</strong> Tant que le journal n'affichait
pas de date, elles n'étaient qu'un ordre de tri. Elles sont du contenu dès lors qu'un apprenant les lit.</p></div>""",
           'structure du journal')

d.rep('<tr><td>512</td><td>Trésorerie</td><td></td><td></td></tr>',
      '<tr><td>512</td><td>Banque</td><td></td><td></td></tr>', 'plan de comptes — 512')

d.rep('<tr><td><div class="libelle"><div><span class="cpt">512</span> Trésorerie</div></div></td>',
      '<tr><td><div class="libelle"><div><span class="cpt">512</span> Banque</div>'
      '<div><span class="cpt">Trésorerie</span></div></div></td>', 'grille — 512')

d.rep_bloc("<li><strong>Le solde du compte 512 s'affiche en permanence</strong>", '</ul>',
           """<li><strong>Le solde du compte 512 s'affiche en permanence</strong>, hors du journal, comme le solde bancaire
d'une vraie application. Un clic sur n'importe quel autre compte donne son solde.</li>
<li><strong>Il est en saisie pour les seules lignes dont le compte n'a pas de case dans la
grille.</strong> Il y en a quatre dans tout le module, toutes de TVA&nbsp;: au Chapitre 5, la taxe sur les
ventes professionnelles du premier trimestre, 6&nbsp;000&nbsp;€ au crédit du compte 4457, puis les deux
lignes de l'écriture de solde, 7&nbsp;800&nbsp;€ au débit du 4457 et 6&nbsp;600&nbsp;€ au crédit du
4456&nbsp;; au Chapitre 8, la taxe sur le torréfacteur, 7&nbsp;200&nbsp;€ au débit du 4456. <strong>Partout
ailleurs, l'apprenant écrit dans la grille et le journal reçoit</strong>, y compris pour les écritures
qu'il passe lui-même. C'est ce que la section 4 disait de travers.</li>
<li><strong>Une ligne du module n'y passe pas</strong>&nbsp;: le résultat net inscrit au passif au
Chapitre 11, 27&nbsp;200&nbsp;€ au crédit du compte 120. Ce n'est pas une opération, c'est le solde du
Compte de Résultat qui vient se poser au Bilan, et c'est pour cela que le total de contrôle du module,
1&nbsp;294&nbsp;694,00&nbsp;€, ne la compte pas. <strong>Aucune formule du type «&nbsp;toute écriture
remplit le journal&nbsp;» n'est donc exacte</strong>, et l'exception tombe au moment fort du parcours.</li>
</ul>""", 'comportement du journal')

d.rep_bloc('Vingt-six comptes,', 'Une phrase au Chapitre 3',
           """<strong>Vingt-neuf comptes au plan, pas un de plus, et la liste est fermée</strong> : si une écriture
semble en réclamer un trentième, c'est le scénario qu'il faut revoir. Ils ne se répartissent pas de la même
façon selon l'endroit où on les compte, et les trois nombres sont justes ensemble : <strong>la grille en
affiche vingt-sept</strong>, les vingt-neuf moins les deux comptes de TVA « journal seul », qui n'y ont
aucune case ; <strong>le journal en mouvemente vingt-huit</strong>, les vingt-neuf moins le compte 120, qui
n'y passe jamais. Une phrase au Chapitre 3""", 'nombre de comptes')

d.rep('<div class="note"><span class="t">Ce que ces numéros sont',
      """<h4>Ce qu'une ligne d'écriture porte côté application</h4>
<p>Écrit ici pour la même raison que les trois comportements ci-dessus&nbsp;: la construction du journal
s'appuyait dessus sans que ce soit nulle part.</p>
<ul>
<li><strong>Chaque ligne porte sa ligne de journal</strong> — le numéro de compte, le libellé daté, la somme
et la colonne. Elle vaut pour les cent six lignes du module&nbsp;; la cent-septième, le résultat du
Chapitre 11, ne la porte pas, et c'est ainsi que l'exception se lit dans les données plutôt que dans un
commentaire.</li>
<li><strong>Chaque ligne dit si elle se saisit au journal</strong>, ce qui n'est vrai que des quatre lignes
de TVA nommées plus haut. Le reste s'y inscrit en conséquence de la saisie faite dans la grille.</li>
<li><strong>Chaque ligne porte un identifiant qui ne dépend d'aucune position</strong>&nbsp;: chapitre
abrégé, opération, compte et sens — <code>tva-solde1-4457d</code>, <code>inv-torref-4456d</code>. <strong>Le
motif est que cet identifiant conditionne la progression de l'apprenant</strong>&nbsp;: il dit si une
écriture est faite. Un identifiant tiré d'un rang dans une liste change dès qu'une écriture se déplace, et
la progression devient fausse sans que rien ne le signale. <strong>Le segment du milieu est l'opération et
non le bloc</strong>&nbsp;: le panneau du Chapitre 10 porte deux opérations dont deux lignes créditent
toutes deux le compte 512, et sans cette finesse les deux identifiants seraient les mêmes.</li>
</ul>
<div class="note"><span class="t">Ce que ces numéros sont""", 'contrat de ligne côté application')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 10 — LE PANNEAU DU CHAPITRE 10 ANNONÇAIT 27 LIGNES ET EN LISTAIT 9
# ═══════════════════════════════════════════════════════════════════════════
# Les dix-huit lignes manquantes sont reprises telles quelles du Chapitre 10
# livré, qui les porte depuis sa v5. La fiche, elle, était restée à 9.
d.rep(f'<span class="t">Enregistré automatiquement — 9 lignes</span>\n'
      f'<p class="op">Écriture de période — quatrième trimestre</p>',
      f'<span class="t">Enregistré automatiquement — 27 lignes</span>\n'
      f'<p class="op">Écriture de période — quatrième trimestre</p>',
      'panneau du Chapitre 10 — compte annoncé')

d.rep_bloc(f'<li>Bilan — 401 Dettes fournisseurs — «{NB}Fournisseurs T4{NB}» — 86{NB}352{NB}€ au crédit</li>',
           '</ul>', """<li>Bilan — 401 Dettes fournisseurs — «&nbsp;Fournisseurs T4&nbsp;» — 86&nbsp;352&nbsp;€ au crédit</li>
</ul>
<p class="op">Salaires du quatrième trimestre et échéances d'emprunt du second semestre</p>
<ul class="lignes">
<li>CR — 641 Salaires bruts — «&nbsp;Salaires bruts T4&nbsp;» — 15&nbsp;600&nbsp;€ au débit</li>
<li>CR — 645 Charges sociales patronales — «&nbsp;Charges patronales T4&nbsp;» — 6&nbsp;552&nbsp;€ au débit</li>
<li>Bilan — 512 Trésorerie — «&nbsp;Nets versés T4&nbsp;» — 12&nbsp;168&nbsp;€ au crédit</li>
<li>Bilan — 431 Dettes sociales — «&nbsp;Cotisations à verser T4&nbsp;» — 9&nbsp;984&nbsp;€ au crédit</li>
<li>CR — 661 Charges d'intérêts — «&nbsp;Échéances d'emprunt, juillet à décembre — intérêts&nbsp;» — 496,50&nbsp;€ au débit</li>
<li>Bilan — 164 Emprunt bancaire — «&nbsp;Échéances d'emprunt, juillet à décembre — capital&nbsp;» — 3&nbsp;276,60&nbsp;€ au débit</li>
<li>Bilan — 512 Trésorerie — «&nbsp;Échéances d'emprunt, juillet à décembre&nbsp;» — 3&nbsp;773,10&nbsp;€ au crédit</li>
</ul>
<p class="op">Règlements de l'exercice</p>
<ul class="lignes">
<li>Bilan — 512 Trésorerie — «&nbsp;Règlements de clients&nbsp;» — 189&nbsp;000&nbsp;€ au débit</li>
<li>Bilan — 411 Créances clients — «&nbsp;Règlements de clients&nbsp;» — 189&nbsp;000&nbsp;€ au crédit</li>
<li>Bilan — 401 Dettes fournisseurs — «&nbsp;Paiements de fournisseurs&nbsp;» — 240&nbsp;552&nbsp;€ au débit</li>
<li>Bilan — 512 Trésorerie — «&nbsp;Paiements de fournisseurs&nbsp;» — 240&nbsp;552&nbsp;€ au crédit</li>
<li>Bilan — 431 Dettes sociales — «&nbsp;Cotisations versées, juillet à novembre&nbsp;» — 13&nbsp;824&nbsp;€ au débit</li>
<li>Bilan — 512 Trésorerie — «&nbsp;Cotisations versées, juillet à novembre&nbsp;» — 13&nbsp;824&nbsp;€ au crédit</li>
<li>GdJal seul — 4457 TVA collectée — «&nbsp;Soldes de TVA des trois derniers trimestres&nbsp;» — 46&nbsp;200&nbsp;€ au débit</li>
<li>GdJal seul — 4456 TVA déductible — «&nbsp;Soldes de TVA des trois derniers trimestres&nbsp;» — 42&nbsp;192&nbsp;€ au crédit</li>
<li>Bilan — 4455 État — TVA à décaisser — «&nbsp;Soldes de TVA des trois derniers trimestres&nbsp;» — 4&nbsp;008&nbsp;€ au crédit</li>
<li>Bilan — 4455 État — TVA à décaisser — «&nbsp;TVA versée en cours d'exercice&nbsp;» — 808&nbsp;€ au débit</li>
<li>Bilan — 512 Trésorerie — «&nbsp;TVA versée en cours d'exercice&nbsp;» — 808&nbsp;€ au crédit</li>
</ul>""", 'panneau du Chapitre 10 — les dix-huit lignes manquantes')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 4 — LA PHRASE FAUSSE
# ═══════════════════════════════════════════════════════════════════════════
d.rep_bloc('<li><strong>La saisie se fait dans les composants', '</li>',
           """<li><strong>La saisie se fait dans la grille — le Bilan et le Compte de Résultat — jamais dans le bloc
lui-même</strong>, et au grand journal pour les seules lignes dont le compte n'a pas de case dans la grille.
Il y en a quatre dans tout le module, toutes de TVA, nommées à la section 2. Le journal n'est pas un second
formulaire&nbsp;: partout ailleurs il reçoit ce que la grille enregistre.</li>""", 'saisie, bloc manuel')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 14 — POINTS OUVERTS
# ═══════════════════════════════════════════════════════════════════════════
d.rep_bloc('<li><strong>Forme visuelle des blocs dans le flux du texte.</strong>', '</li>',
           """<li><strong>Forme visuelle des blocs dans le flux du texte.</strong> Un bloc manuel inséré en fin de
sous-titre doit se distinguer du corps sans casser la colonne de lecture, et le grand journal doit continuer
de distinguer une ligne saisie d'une ligne injectée une fois qu'elles y cohabitent. <strong>Le discriminant
existe et voyage avec l'écriture</strong> — chaque ligne sait déjà si elle est passée à la main ou
enregistrée automatiquement. Il ne reste qu'une décision de forme.</li>""", 'forme visuelle des blocs')

d.rep_bloc('<li><strong>Migration des libellés côté application.</strong>', '</li>',
           """<li><strong>Migration des libellés côté application.</strong> Le grand journal, la grille et tout libellé
d'interface passent de « dépense / recette » à « débit / crédit ». À recenser dans le code avant la reprise
de la rédaction : c'est un renommage de contrat de données autant que d'affichage. S'y
ajoute la capitale d'Actif et de Passif dans les en-têtes de colonne de la grille (charte, section 9).
C'est un changement d'affichage seul, mais il se fait dans la même passe : les textes des Chapitres 1 et 2
l'appliquent déjà, et un écran qui écrirait « passif » là où le texte écrit « Passif » produirait exactement
le défaut que la règle prétend éviter. <strong>Le compte 512 ne fait plus partie de cette passe</strong> :
l'application affiche « Banque », le module dit « Trésorerie », et les deux se posent en deux lignes du même
libellé, ce que la grille sait déjà faire.</li>""", 'migration des libellés')

# ═══════════════════════════════════════════════════════════════════════════
#  PIED DE PAGE — il portait encore v24
# ═══════════════════════════════════════════════════════════════════════════
d.rep_bloc('<p class="fin">', '</p>', """<p class="fin">Document de référence — Casoria, v27 du 12 septembre 2026. Le grand journal porté à
l'application.
<strong>Aucune écriture ne bouge et aucun montant n'est touché</strong>&nbsp;: le Bilan de l'exercice boucle
sur 130&nbsp;410&nbsp;€ des deux côtés, le Compte de Résultat sur 283&nbsp;000&nbsp;€, et le total de
contrôle du module vaut 1&nbsp;294&nbsp;694,00&nbsp;€ au débit comme au crédit.
<strong>Ce total a été recalculé ligne à ligne depuis les cent sept lignes du module</strong>, et non repris
de ce document&nbsp;: il tombe juste, et il exclut le résultat du Chapitre 11, qui ne passe pas par le
journal. <strong>Le contrôle du compte 512 du Chapitre 8 a été rejoué de la même façon</strong>&nbsp;:
treize lignes, 112&nbsp;240,00&nbsp;€ au débit, 50&nbsp;868,90&nbsp;€ au crédit, différence
61&nbsp;371,10&nbsp;€ — les trois nombres du texte publié, au centime.
<strong>Trois définitions de la section 11 restent à trancher</strong>, et elles sont le seul point de fond
que cette version laisse ouvert. «&nbsp;Marge nette — Résultat net rapporté au chiffre d'affaires&nbsp;» et
«&nbsp;Autonomie financière — Capitaux propres rapportés au total du Bilan&nbsp;» sont exactement les
tournures que la relecture profane du Chapitre 12 a déclarées illisibles, et que le corps de ce chapitre a
dû réécrire&nbsp;; leurs rechanges sont écrites à l'annexe du Chapitre 13. Un troisième cas, plus
léger&nbsp;: «&nbsp;Impôt assis sur le bénéfice&nbsp;», où «&nbsp;assis sur&nbsp;» est une tournure de métier
que le Chapitre 11 n'emploie pas.
<strong>Ce qui reste en attente et ne dépend plus de la rédaction.</strong> Au Chapitre 5, la légende du
panneau automatique demande de regarder un total bouger <em>pendant</em> qu'une ligne s'inscrit, ce qui est
faux sur un écran étroit&nbsp;: les deux réparations sont écrites, l'une rédactionnelle et l'autre à la
charge du produit, et le choix appartient au décideur. Au Chapitre 6, l'origine des 15&nbsp;000&nbsp;€ de
stock n'est pas écrite au corps, ce qui interdit d'en faire une précision.
<strong>Toute modification d'un montant impose de recalculer l'ensemble du scénario avant de le reporter
dans les textes.</strong></p>""", 'pied de page')

# ═══════════════════════════════════════════════════════════════════════════
#  CONTRÔLES
# ═══════════════════════════════════════════════════════════════════════════
# Règle 2 : un renvoi interne ne porte jamais de numéro de version. Les trois
# mentions de la v26 qui restent sont au chapo et au bloc « Changements », les
# deux seuls endroits où un document en désigne un autre à la bascule.
d.compte('v26', 3, 'mentions de la v26 hors chapo et Changements')
d.compte('v24', 0, 'mention de version périmée')
d.compte('Vingt-six comptes', 0, 'ancien nombre de comptes')
# « vingt-six » ne subsiste qu'une fois, dans la phrase du bloc « Changements »
# qui cite l'ancien compte pour dire qu'il était faux.
d.compte('vingt-six', 1, 'ancien nombre de comptes, en toutes lettres')
d.compte('<tr><td>512</td><td>Trésorerie</td>', 0, 'ancien libellé du 512 au plan de comptes')
d.compte('<span class="cpt">512</span> Trésorerie', 0, 'ancien libellé du 512 à la grille')
d.compte('<span class="cpt">512</span> Banque', 1, 'nouveau libellé du 512 à la grille')

# typographie : aucune somme sans insécable dans ce qui vient d'être écrit
mauvais = re.findall(r'\d[ \t]\d{3}\b|\d[ \t]€', d.s)
assert not mauvais, f'sommes sans insécable : {mauvais[:5]}'

print('── déroulé v26 → v27')
d.write(DER_OUT)
