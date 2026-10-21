#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Porte la saisie des écritures au déroulé (v27 → v28).

Les totaux calculés, leur comportement, le geste de saisie à la ligne ; les
corrections groupées des Chapitres 7, 9, 10 et 12 ; un nombre annoncé faux à la
section 9. Aucune écriture ne bouge : le total de contrôle reste à
1 294 694,00 €.

Chaque substitution est assertée unique. Le fichier est écrit à la toute fin :
une assertion qui saute le laisse intact (règle 4 des documents de référence).
Les ancres longues passent par rep_s, dont le motif tolère espace ordinaire,
insécable et &nbsp; et les retours à la ligne du source.
Règle 1 : le bloc « Changements » de la v27 saute. Règle 2 : pas de numéro de
version dans un renvoi interne.
"""
import re

NB = chr(0xA0)
assert ord(NB) == 0xA0

DER_IN = 'deroule-comprendre-la-comptabilite-v27.corps.html'
DER_OUT = 'deroule-comprendre-la-comptabilite-v28.corps.html'


class Doc:
    def __init__(self, path):
        self.path = path
        self.s = open(path, encoding='utf-8').read()
        self.n = 0

    def rep(self, old, new, label, n=1):
        c = self.s.count(old)
        assert c == n, f'{label} : {c} occurrence(s), {n} attendue(s)'
        self.s = self.s.replace(old, new, n)
        self.n += 1

    def rep_s(self, old, new, label):
        motif = r'(?:\s|&nbsp;)+'.join(re.escape(p) for p in old.split())
        m = list(re.finditer(motif, self.s))
        assert len(m) == 1, f'{label} : {len(m)} occurrence(s), 1 attendue'
        a, b = m[0].span()
        self.s = self.s[:a] + new + self.s[b:]
        self.n += 1

    def rep_bloc(self, debut, fin, new, label):
        assert self.s.count(debut) == 1, f'{label} : début non unique'
        i = self.s.find(debut)
        j = self.s.find(fin, i)
        assert j >= 0, f'{label} : fin introuvable'
        self.s = self.s[:i] + new + self.s[j + len(fin):]
        self.n += 1

    def compte(self, motif, n, label):
        c = self.s.count(motif)
        assert c == n, f'{label} : {c} occurrence(s) de « {motif} », {n} attendue(s)'

    def write(self, path):
        open(path, 'w', encoding='utf-8').write(self.s)
        print(f'   {path} — {self.n} substitutions, {len(self.s)} caractères')


d = Doc(DER_IN)

# ═══════════════════════════════════════════════════════════════════════════
#  EN-TÊTE
# ═══════════════════════════════════════════════════════════════════════════
d.rep('<p class="kicker">Casoria • Document de référence • v27</p>',
      '<p class="kicker">Casoria • Document de référence • v28</p>', 'kicker')

d.rep_bloc('<p class="chapo">Déroulé annoté', '</p>', """<p class="chapo">Déroulé annoté de la formation. Treize chapitres, un exercice complet
simulé de la création à la clôture, sur le fil rouge d'une PME fictive. <strong>Cette v28 écrit la saisie
des écritures côté application</strong>&nbsp;: les totaux de la grille, calculés et jamais saisis&nbsp;; la
façon dont ils bougent et dont le Bilan signale son équilibre&nbsp;; et le geste de saisie lui-même, à la
ligne, qui refuse une saisie fausse. Elle groupe les corrections que les composants des Chapitres 7, 9, 10
et 12 laissaient en attente, et répare un nombre annoncé faux à la section 9. <strong>Aucune écriture ne
bouge</strong>&nbsp;: le total de contrôle du module reste à 1&nbsp;294&nbsp;694,00&nbsp;€ au débit comme au
crédit, et le Bilan de l'exercice sur 130&nbsp;410&nbsp;€. La charte reste en v16, inchangée.</p>""", 'chapo')

# ═══════════════════════════════════════════════════════════════════════════
#  BLOC « CHANGEMENTS » — celui de la v27 saute
# ═══════════════════════════════════════════════════════════════════════════
d.rep_bloc('<h2>Changements v27</h2>', '</ul>', """<h2>Changements v28</h2>
<p>L'enregistrement des écritures passe du déroulé à l'application. Chaque décision ci-dessous a été prise
sur un banc qui rejoue les Chapitres 2 à 6 avec les montants de ce document. <strong>Rien de ce qui suit ne
passe une écriture</strong>&nbsp;: le total de contrôle du module reste à 1&nbsp;294&nbsp;694,00&nbsp;€ au
débit comme au crédit.</p>
<ul>
<li><strong>Les totaux sont calculés, jamais saisis.</strong> Tout le document le supposait — le modèle
de données, le pied de bloc, le panneau — et aucune phrase ne le disait. C'est la quatrième décision de la
grille, à la section 2.</li>
<li><strong>Le comportement des totaux est écrit à la section 4.</strong> Seuls les totaux du Bilan
portent une couleur, slate tant qu'ils diffèrent et lime quand ils sont égaux, avec un signe ≠ ou =. Le
rouge, proposé d'abord, est écarté&nbsp;: il est réservé au geste refusé, et le déséquilibre n'est pas une
erreur. Un nombre qui change est chassé par le nouveau, jamais par un compteur, et l'écart s'affiche un
instant sous le total. Le panneau automatique suit le même processus, ligne à ligne.</li>
<li><strong>Toutes les lignes de la grille restent visibles dès le début, à trois niveaux</strong> —
vide, à saisir, remplie —, sans couleur sur aucune. La hiérarchie fait le tri que le masquage ferait
mal.</li>
<li><strong>Le geste de saisie est écrit à la section 4.</strong> Un clic sur la ligne du compte ouvre un
popover qui ne demande que le montant&nbsp;: ni débit ni crédit dans la grille, ce que le Chapitre 2 publié
dit déjà du Bilan. Jamais de fenêtre modale. <strong>Une saisie fausse est refusée</strong>, et c'est ce
qui permet à la ligne de montrer en lecture seule les écritures passées sur elle.</li>
<li><strong>Les Chapitres 7 et 9 n'ont plus de composant.</strong> <code>&lt;MensualiteDecomposee /&gt;</code>
a été écrit deux fois puis retiré, <code>&lt;CoutEmployeur /&gt;</code> écarté avant d'être écrit&nbsp;: une
illustration remplace chacun. Corrigé aux sections 5 et 7, aux deux fiches, et dans l'encadré du principe
d'illustration, dont la phrase sur le Chapitre 7 devenait fausse.</li>
<li><strong>Le composant du Chapitre 10 a changé de place</strong>, après les blocs et non avant, seule
exception du module à l'ordre de la section 7. Corrigé à la section 7, à la fiche, et au volume du
chapitre à la section 13.</li>
<li><strong>Le composant du Chapitre 12 déplace des montants, pas des délais</strong>&nbsp;: ses trois
curseurs sont en euros, et «&nbsp;délai fournisseur&nbsp;» devient «&nbsp;dettes fournisseurs&nbsp;» aux
sections 5 et 7.</li>
<li><strong>La section 9 annonçait 7 lignes automatiques au Chapitre 5 et 52 au module</strong>, quand la
section 4 et la fiche en portent 13 et 58. Recomptées depuis les fiches, 13 et 58 sont justes. Trouvé en
relisant pour cette version&nbsp;: un nombre annoncé qu'aucun script ne recalcule dérive sans que rien ne le
signale.</li>
</ul>""", 'bloc changements')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 2 — la grille
# ═══════════════════════════════════════════════════════════════════════════
d.rep_s("""Une case allumée pour la première fois et une case qui varie ensuite doivent se distinguer
visuellement dans l'application.</p>""", """Une case allumée pour la première fois et une case qui varie ensuite doivent se distinguer
visuellement dans l'application. <strong>Toutes les lignes sont visibles dès le Chapitre 1</strong>, vides
ou non&nbsp;: c'est la grille de mots croisés entière, et sa forme enseigne déjà où va l'argent. La
hiérarchie décrite à la section 4 fait le tri que le masquage ferait mal.</p>""", 'mots croisés')

d.rep('<h3>Trois décisions à retenir sur la grille</h3>',
      '<h3>Quatre décisions à retenir sur la grille</h3>', 'titre des décisions')
d.rep_s("""l'affectation est traitée en schéma illustré au Chapitre 11.</li>
</ul>""", """l'affectation est traitée en schéma illustré au Chapitre 11.</li>
<li><strong>Les totaux sont calculés, jamais saisis.</strong> Les totaux de la grille sont calculés par
l'application à chaque ligne inscrite, comme les deux lignes de résultat du Compte de Résultat à partir du
Chapitre 11&nbsp;; ils ne se saisissent jamais. Seul le résultat net porté au passif, au compte 120, est
écrit par l'apprenant. Leur comportement à l'écran est écrit à la section 4.</li>
</ul>""", 'quatrième décision')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 4 — panneau, bloc manuel, geste de saisie, totaux
# ═══════════════════════════════════════════════════════════════════════════
d.rep_s("""que le Chapitre 3 s'emploie à désamorcer.</li>""", """que le Chapitre 3 s'emploie à désamorcer.</li>
<li><strong>Chaque ligne déplace les totaux comme une ligne saisie</strong>&nbsp;: même transition, même
écart affiché — voir le comportement des totaux, plus bas. Le défilé laisse à la transition le temps de se
voir, de l'ordre de trois quarts de seconde par ligne, et un bouton «&nbsp;Tout afficher&nbsp;» termine le
défilé d'un coup&nbsp;: le panneau du Chapitre 10 porte vingt-sept lignes.</li>""", 'panneau : totaux')

d.rep_s("""<li><strong>La saisie se fait dans la grille — le Bilan et le Compte de Résultat — jamais dans le bloc
lui-même</strong>,""", """<li><strong>La saisie se fait à la ligne, dans la grille — le Bilan et le Compte de Résultat — jamais
dans le bloc lui-même</strong>,""", 'bloc : saisie à la ligne')
d.rep_s("""partout ailleurs il reçoit ce que la grille enregistre.</li>
<li><strong>Le texte et les éléments de saisie""", """partout ailleurs il reçoit ce que la grille enregistre. Le geste est
décrit plus bas.</li>
<li><strong>Le texte et les éléments de saisie""", 'bloc : renvoi au geste')

GESTE = """
<h4>Le geste de saisie</h4>
<p>Tranché le 18 septembre 2026, sur un banc qui rejoue les Chapitres 2 à 6. Le geste est celui que JDC
emploie déjà, à quelques détails près.</p>
<ul>
<li><strong>Un clic sur la ligne du compte ouvre un popover accroché à elle</strong>
(<code>UPopover</code>)&nbsp;; sur un téléphone, un tiroir qui monte du bas (<code>UDrawer</code>).
<strong>Jamais de fenêtre modale</strong>&nbsp;: elle cacherait le texte, donc la consigne, et la grille au
moment même où les totaux bougent.</li>
<li><strong>Dans la grille, le popover ne demande que le montant.</strong> Ni débit ni crédit, ni emploi ni
ressource. Le Chapitre 2 publié écrit «&nbsp;Le Bilan, lui, n'a ni débit ni crédit&nbsp;», et poser ces
mots sur une ligne du Bilan embrouillerait la notion qu'il vient d'installer. Le sens vient de la consigne du
bloc. <strong>Au grand journal</strong>, pour les quatre lignes de TVA, la colonne se choisit, puisque débit
et crédit y sont les noms des colonnes.</li>
<li><strong>On saisit le mouvement, la case affiche le solde.</strong> Le popover ne l'explique pas&nbsp;:
les totaux le montrent déjà, et l'écran porte assez de texte.</li>
<li><strong>L'ordre est libre à l'intérieur d'un bloc.</strong> La ligne qui suit dans la consigne porte un
cadre slate et un badge «&nbsp;À saisir&nbsp;» (<code>UBadge</code>, neutre) décalé en haut à droite, jamais à
la place du montant&nbsp;: une case qui en porte déjà un doit le laisser lisible.</li>
<li><strong>Une saisie fausse est refusée.</strong> Elle est signalée dans le popover et ne peut pas être
validée&nbsp;: compte absent de l'écriture en cours, montant qui n'est pas celui de la consigne, colonne
fausse au journal. C'est le seul rouge de l'écran, celui du geste refusé. <strong>Motif</strong>&nbsp;: dans
JDC, gérer les erreurs de saisie est un casse-tête où le formateur perd beaucoup de temps, pour un apport
pédagogique négligeable&nbsp;; accepter l'erreur ne se justifierait que dans une formation comptable pure.
L'exception possible passe par une activité, ou par un montant que l'apprenant calcule lui-même — les
27&nbsp;200&nbsp;€ du Chapitre 11 —, et même là une réponse fausse ne s'inscrit pas.</li>
<li><strong>Un clic sur une ligne déjà remplie montre les écritures passées sur elle</strong>, en lecture
seule&nbsp;: date, libellé, et ce que chacune a fait à la case, en plus ou en moins, sans débit ni crédit.
C'est le grand livre du compte, la même source que le filtre du journal. <strong>Le refus des erreurs est
ce qui rend cette liste sûre</strong>&nbsp;: rien de faux n'y entre, donc rien n'y est à modifier ni à
effacer — ce que JDC doit offrir, et qui y tourne vite au désordre.</li>
</ul>

<h4>Comportement des totaux</h4>
<ul>
<li><strong>Seuls les totaux du Bilan portent une couleur.</strong> Slate tant que l'Actif et le Passif
diffèrent, lime quand ils sont égaux — le lime est déjà, dans le vocabulaire des composants, la couleur de
ce qui est acquis. Un signe les sépare, ≠ ou =, pour que la couleur ne porte pas seule l'information. Deux
totaux à zéro restent neutres. <strong>Pas de rouge</strong>&nbsp;: il est réservé au geste refusé, et le
déséquilibre n'est pas une erreur — l'<code>&lt;UAlert&gt;</code> du Chapitre 2 le dit, et un total rouge
pendant neuf chapitres le contredirait sur chaque écran. Le lime s'allume dès le premier apport,
30&nbsp;000&nbsp;€ des deux côtés, s'éteint à la première vente du Chapitre 3 et revient au Chapitre 11&nbsp;:
c'est l'arc du module.</li>
<li><strong>Le Compte de Résultat ne porte pas de couleur.</strong> Ses deux totaux diffèrent par
construction jusqu'au Chapitre 11, puis sont égaux par construction&nbsp;: une couleur n'y apprendrait
rien.</li>
<li><strong>Un nombre qui change est chassé par le nouveau</strong>, qui glisse à sa place en trois dixièmes
de seconde, vers le haut quand il monte, vers le bas quand il baisse. <strong>Jamais de compteur</strong>&nbsp;:
un compteur fait défiler des valeurs intermédiaires, donc une suite de nombres faux, ce que la règle de la
<code>&lt;CalculetteTva /&gt;</code> interdit.</li>
<li><strong>L'écart s'affiche un instant sous le total</strong>, «&nbsp;▲ +320&nbsp;€&nbsp;» ou
«&nbsp;▼ −1&nbsp;450&nbsp;€&nbsp;», puis s'efface. C'est ce qui distingue un total qui baisse d'un total qui
monte, comme le panneau automatique l'exige. Sous <code>prefers-reduced-motion</code>, pas de
glissement&nbsp;: l'écart seul.</li>
<li><strong>Trois niveaux de ligne, aucune couleur.</strong> Une ligne vide est plus petite, aux mêmes
teintes, et sa hauteur ne change pas quand elle se remplit, pour que rien ne se décale. La ligne à saisir
porte le cadre et le badge décrits plus haut. Une ligne remplie est à pleine encre, avec son montant. Le
passage de la petite taille à la pleine encre est ce qui distingue une case allumée pour la première fois
d'une case qui varie. <strong>Motif de garder toutes les lignes</strong>&nbsp;: masquer les lignes vides
coûterait le but des mots croisés, la structure que la forme de la grille enseigne déjà, et la stabilité de
l'écran. JDC montre tout avec le même poids, et c'est ce poids, non le nombre de lignes, qui charge
l'écran.</li>
<li><strong>Rien de cela ne change la règle de rédaction ci-dessus.</strong> Sur un téléphone, les totaux
sont à un défilement de la ligne saisie&nbsp;: l'animation est un plus sur grand écran, et le texte ne compte
jamais dessus. C'est le pied de bloc qui porte le mouvement là où l'œil se trouve.</li>
</ul>
<p class="legende">Les deux bancs qui ont servi à trancher, <code>banc-totaux.html</code> et
<code>banc-saisie.html</code>, sont dans le dossier des livraisons.</p>
"""
d.rep_s("""à la charte, section 16, avec sa case de checklist.</p></div>""",
        """à la charte, section 16, avec sa case de checklist.</p></div>""" + GESTE, 'geste et totaux')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 5 — composants
# ═══════════════════════════════════════════════════════════════════════════
d.rep_s("""<tr><td class="ch">7</td><td><code>&lt;MensualiteDecomposee /&gt;</code></td><td>Curseur sur l'échéancier, ventilation intérêts / capital</td></tr>""",
        """<tr><td class="ch">7</td><td>—</td><td>Aucun composant. <code>&lt;MensualiteDecomposee /&gt;</code> a été écrit deux fois puis retiré&nbsp;: il faisait deviner une réponse que le paragraphe suivant donne. Une illustration le remplace, à sa place exacte</td></tr>""", 's5 ch7')
d.rep_s("""<tr><td class="ch">9</td><td><code>&lt;CoutEmployeur /&gt;</code></td><td>Décomposition du brut en trois blocs</td></tr>""",
        """<tr><td class="ch">9</td><td>—</td><td>Aucun composant. <code>&lt;CoutEmployeur /&gt;</code> a été écarté avant d'être écrit&nbsp;: les cinq nombres qu'il devait révéler sont dans le texte qui le précède. Une illustration le remplace</td></tr>""", 's5 ch9')
d.rep_s("""<td>Curseurs stock, encours, délai fournisseur</td>""",
        """<td>Trois curseurs en euros&nbsp;: stock, créances clients, dettes fournisseurs</td>""", 's5 ch12')
d.rep_s("""<tr><td class="ch">—</td><td><code>&lt;BlocEcritures /&gt;</code></td>""",
        """<tr><td class="ch">—</td><td>Grille — Bilan et Compte de Résultat</td><td>Saisie à la ligne par popover, montant seul, saisie fausse refusée. Totaux calculés, jamais saisis. Comportement à la section 4</td></tr>
<tr><td class="ch">—</td><td><code>&lt;BlocEcritures /&gt;</code></td>""", 's5 grille')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 7 — activités
# ═══════════════════════════════════════════════════════════════════════════
d.rep_s("""l'activité vient toujours avant : elle prépare, l'écriture acte.""",
        """l'activité vient toujours avant : elle prépare, l'écriture acte. <strong>Une
exception, au Chapitre 10</strong>&nbsp;: le tri à quatre issues vient après les blocs, parce qu'aucune des
quatre issues n'est enseignée avant eux.""", 's7 exception')
d.rep_s("""<tr><td class="ch">7</td><td class="cle">Décomposition de mensualité</td><td>Un curseur parcourt les échéances ; la barre se scinde en intérêts et capital, avec le trajet de chaque part.</td></tr>""",
        """<tr><td class="ch">7</td><td class="cle">—</td><td>La décomposition de mensualité a été retirée&nbsp;: au curseur sur le temps, elle démontrait un échéancier bancaire quand le chapitre parle de nature&nbsp;; au curseur sur le partage, elle faisait deviner ce que la phrase suivante écrit. Une illustration de la déclaration «&nbsp;Rembourser une dette n'appauvrit pas&nbsp;» prend sa place.</td></tr>""", 's7 ch7')
d.rep_bloc('<tr><td class="ch">9</td><td class="cle">Révélateur', '</tr>',
        """<tr><td class="ch">9</td><td class="cle">—</td><td>Le révélateur coût employeur / net perçu a été écarté avant d'être écrit&nbsp;: décomposer le brut par un geste referait ce que les trois paragraphes précédents viennent de faire. Une illustration le remplace, une barre à l'échelle lue par trois accolades.</td></tr>""", 's7 ch9')
d.rep_s("""<td>Curseurs sur le stock, l'encours client et le délai fournisseur.""",
        """<td>Curseurs en euros sur le stock, l'encours client et les dettes fournisseurs.""", 's7 ch12')

# ═══════════════════════════════════════════════════════════════════════════
#  FICHES — Chapitres 7, 9, 10
# ═══════════════════════════════════════════════════════════════════════════
d.rep('<p>Décomposition de mensualité, au curseur.</p>',
      """<p>Aucune. Le composant prévu a été retiré le 16 septembre 2026&nbsp;; une seconde illustration porte la
déclaration «&nbsp;Rembourser une dette n'appauvrit pas&nbsp;», à l'emplacement exact où il se trouvait. Le
Chapitre 7 est le premier du module à porter deux illustrations et aucun composant.</p>""", 'fiche 7 activité')
d.rep_s("""le partage de la mensualité est déjà porté par le composant, et l'illustration
travaille donc l'autre axe""", """le partage de la mensualité est porté par la seconde illustration, et la
première travaille donc l'autre axe""", 'fiche 7 axes')
d.rep('<p>Révélateur coût employeur / net perçu, en trois blocs.</p>',
      """<p>Aucune. Le révélateur coût employeur / net perçu a été écarté&nbsp;: les cinq nombres qu'il devait
révéler sont dans les trois paragraphes qui le précèdent. Une illustration le remplace, une barre à
l'échelle lue par trois accolades — le coût total employeur, le brut du contrat, et ce qui part aux
organismes sociaux.</p>""", 'fiche 9 activité')
d.rep('<p>Tri à quatre issues, six situations.</p>',
      """<p>Tri à quatre issues, six situations. <strong>Placé en fin du troisième sous-titre, après le bloc
Hôtel Bellevue et avant le <code>&lt;UAlert&gt;</code></strong>, précédé d'une transition de trente-cinq
mots. À sa première place, après la déclaration du premier sous-titre, aucune des quatre issues n'était
encore enseignée. C'est la seule exception du module à l'ordre de la section 7.</p>""", 'fiche 10 activité')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 9 — le nombre annoncé faux
# ═══════════════════════════════════════════════════════════════════════════
d.rep_s("""<tr><td class="ch">5</td><td>La TVA : compléter le cycle achats-ventes</td><td class="num">25 min</td><td class="num">6</td><td class="num">7</td></tr>""",
        """<tr><td class="ch">5</td><td>La TVA : compléter le cycle achats-ventes</td><td class="num">25 min</td><td class="num">6</td><td class="num">13</td></tr>""", 's9 ch5')
d.rep('<td class="num">49</td><td class="num">52</td>', '<td class="num">49</td><td class="num">58</td>', 's9 total')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 13 — volume du Chapitre 10
# ═══════════════════════════════════════════════════════════════════════════
d.rep_s("""exactement les six familles d'opérations qui manquaient au Bilan.</li>""",
        """exactement les six familles d'opérations qui manquaient au Bilan. <strong>Le 16 septembre
2026</strong>, le déplacement de son composant y ajoute une transition de trente-cinq mots&nbsp;: 712 mots,
751 avec les sous-titres, dépassement du seuil à motiver à la validation.</li>""", 's13 ch10')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 14 — points ouverts et principe d'illustration
# ═══════════════════════════════════════════════════════════════════════════
d.rep_s("""Les Chapitres 1, 2, 3, 4 et 7 en portent une chacun.""",
        """Onze chapitres en portent, douze illustrations en tout&nbsp;: tous sauf le 10 et le 13, et le 7 en
porte deux.""", 's14 liste')
d.rep_s("""<strong>Treize chapitres, dix illustrations</strong>, et le principe de la chose lue deux fois n'a plus servi depuis le Chapitre 8 — les cinq derniers sont des méthodes ou des synthèses, et ni l'une ni l'autre ne se montre deux fois.</p>""",
        """<strong>Treize chapitres, douze illustrations</strong> depuis que le Chapitre 9 en a reçu une à la
place de son composant et que le 7 en porte deux. Parmi les cinq derniers chapitres, aucun n'a resservi le
principe de la chose lue deux fois&nbsp;: ce sont des méthodes ou des synthèses, et ni l'une ni l'autre ne se
montre deux fois.</p>""", 's14 dix illustrations')
d.rep_s("""l'erreur a vécu six chapitres.</p>""", """l'erreur a vécu six chapitres.
<strong>Le 16 septembre 2026, le composant a été retiré</strong>, et l'axe qu'il occupait s'est libéré. Une
seconde illustration le prend&nbsp;: la mensualité partagée en deux, la part du capital lue des deux côtés du
Bilan. La règle tient dans les deux sens&nbsp;: l'illustration cède au geste manipulable quand il existe, et
reprend l'axe quand il disparaît.</p>""", 's14 ch7 retrait')
d.rep_s("""passent de « dépense / recette » à « débit / crédit ».""",
        """passent de « dépense / recette » à « débit / crédit ». La grille, elle, n'affiche ni l'un ni
l'autre&nbsp;: son popover de saisie ne demande que le montant (section 4).""", 's14 migration')

# ═══════════════════════════════════════════════════════════════════════════
#  PIED DE PAGE
# ═══════════════════════════════════════════════════════════════════════════
d.rep_s("""<p class="fin">Document de référence — Casoria, v27 du 12 septembre 2026. Le grand journal porté à
l'application.""", """<p class="fin">Document de référence — Casoria, v28 du 18 septembre 2026. La saisie des écritures
portée à l'application&nbsp;: totaux calculés, comportement des totaux, geste de saisie à la ligne. Les
corrections des Chapitres 7, 9, 10 et 12 sont groupées, et les lignes automatiques de la section 9 sont
recomptées depuis les fiches&nbsp;: 13 au Chapitre 5, 58 au module.""", 'pied')

# ═══════════════════════════════════════════════════════════════════════════
#  CONTRÔLES
# ═══════════════════════════════════════════════════════════════════════════
d.compte('v27', 0, 'mention de la v27')
d.compte('v26', 0, 'mention de la v26')
d.compte('délai fournisseur', 1, 'ancien libellé du 12, cité au seul bloc Changements')
d.compte('<code>&lt;MensualiteDecomposee /&gt;</code></td><td>Curseur', 0, 'ancienne ligne du 7')
d.compte('Trois décisions à retenir', 0, 'ancien titre')
d.compte('<h4>Le geste de saisie</h4>', 1, 'geste')
d.compte('<h4>Comportement des totaux</h4>', 1, 'totaux')

mauvais = re.findall(r'\d[ \t]\d{3}\b|\d[ \t]€', d.s)
assert not mauvais, f'sommes sans insécable : {mauvais[:5]}'

print('── déroulé v27 → v28')
d.write(DER_OUT)
