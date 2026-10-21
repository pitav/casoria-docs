#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Répercussion groupée de la livraison des Chapitres 10 v5 et 11 — 25 août 2026.

Déroulé v21 → v22, et journal de rédaction. La charte v14 est inchangée : elle
avait déjà corrigé la clause de placement de l'<UAlert>, seul point que ces
deux chapitres auraient pu ouvrir. Le registre a été répercuté à part, le jour
de la rédaction, sa propre règle l'imposant.

Chaque substitution est assertée unique et l'écriture se fait à la toute fin :
une assertion qui saute laisse les fichiers intacts.
"""
import re, sys

NB = ' '
assert NB == chr(160), 'NB doit être un insécable, pas un espace ordinaire'


class Doc:
    def __init__(self, chemin):
        self.chemin = chemin
        self.s = open(chemin, encoding='utf-8').read()
        self.n = 0

    def rep(self, old, new, label, n=1, brut=False):
        # brut : le fragment porte un « ~ » littéral — l'approximatif de « ~6h10 »
        # — et non le marqueur d'insécable.
        if not brut:
            old, new = old.replace('~', NB), new.replace('~', NB)
        trouves = self.s.count(old)
        assert trouves == n, f'{self.chemin} · {label} : {trouves} occurrence(s), {n} attendue(s)'
        self.s = self.s.replace(old, new, n)
        self.n += 1

    def ecrire(self):
        open(self.chemin, 'w', encoding='utf-8').write(self.s)
        print(f'   {self.chemin} — {self.n} substitutions')


d = Doc('deroule-comprendre-la-comptabilite-v21.corps.html')
j = Doc('journalderedactioncomprendrelacomptabilite.md')

# ═══ en-tête et bloc « Changements » ════════════════════════════════════════
d.rep('<p class="kicker">Casoria • Document de référence • v21</p>',
      '<p class="kicker">Casoria • Document de référence • v22</p>', 'kicker')

d.rep("""<strong>Cette v21 enregistre la livraison des Chapitres 9 et 10</strong>
et ne touche ni au plan, ni au scénario chiffré, ni à une ligne d'écriture. La place du panneau automatique
du Chapitre 10, que la v20 laissait à trancher, est décidée et motivée à la section 4. Le recensement des
précisions, section 6, couvre dix chapitres sur treize. Deux mots de fabrication entrent aux vigilances de
vocabulaire, section 12. <strong>Un écart de 22&nbsp;648,50&nbsp;€ entre la grille et le scénario chiffré
est ouvert à la section 14, et il se tranche avant d'écrire le Chapitre 11.</strong>""",
      """<strong>Cette v22 enregistre la livraison du Chapitre 11 et la reprise du Chapitre 10 en v5</strong>,
et ne touche ni au plan ni au scénario chiffré. <strong>L'écart de 22&nbsp;648,50&nbsp;€ ouvert par la v21
est fermé</strong>, et le Bilan de l'exercice avec lui&nbsp;: la grille boucle sur 130&nbsp;410&nbsp;€ des
deux côtés au terme du Chapitre 11, poste par poste. Le prix en est un panneau automatique de vingt-sept
lignes au Chapitre 10, en trois écritures, et l'encadré «&nbsp;Ce qu'aucun des deux régimes ne
montre&nbsp;» de la section 4, devenu faux, est réécrit. <strong>Onze chapitres sont écrits sur
treize.</strong>""", 'chapo')

d.rep("""<h2>Changements v21</h2>""", """<h2>Changements v22</h2>""", 'titre changements')

_i = d.s.find('<h2>Changements v22</h2>')
_j = d.s.find('<h2 class="saut">1 — Le fil rouge', _i)
assert _i > 0 and _j > _i, 'bloc des changements introuvable'
d.s = d.s[:_i] + """<h2>Changements v22</h2>
<p>Le Chapitre 11 est écrit, relu et livré, et le Chapitre 10 est repris pour qu'il tienne. Le plan et le
scénario chiffré de la section 3 sont intacts&nbsp;: aucun montant du scénario n'a bougé. Ce qui change est
le contenu d'un panneau automatique, un encadré de la section 4 devenu faux, et deux points de scénario que
la réparation a fait apparaître.</p>
<ul>
<li><strong>L'écart de 22&nbsp;648,50&nbsp;€ est fermé</strong>, sections 4 et 14. Pascal a retenu les deux
voies recommandées&nbsp;: porter les lignes manquantes à l'écriture de période du Chapitre 10, et y réparer
aussi le Bilan. Le Compte de Résultat n'a plus aucun écart au scénario, et les huit postes de Bilan
contrôlés sont conformes.</li>
<li><strong>Le panneau automatique du Chapitre 10 passe de 9 à 27 lignes</strong>, en trois écritures sous
un panneau qui reste unique et groupé&nbsp;: l'écriture de période du quatrième trimestre, les salaires du
quatrième trimestre avec les échéances d'emprunt du second semestre, et les règlements de l'exercice.
Chacune s'équilibre séparément.</li>
<li><strong>L'encadré «&nbsp;Ce qu'aucun des deux régimes ne montre&nbsp;» est réécrit</strong>, section 4.
Il listait six familles d'opérations exécutées sans figurer nulle part&nbsp;; ce sont exactement les six que
la reprise inscrit. <strong>Le motif qu'il donnait était vrai de la notion et faux de l'affichage</strong>
— sans ces écritures, le Bilan ne pouvait pas boucler au Chapitre 11, qui est le moment fort du module.</li>
<li><strong>Le Chapitre 11 quitte la famille des dualités</strong>, section 14, comme le Chapitre 7 en
était sorti et pour le même motif. Sa dualité est déjà déléguée à un geste manipulable, et
<strong>la règle s'élargit&nbsp;: ce geste peut être un bloc d'écritures et pas seulement un
composant.</strong></li>
<li><strong>Deux points de scénario s'ouvrent à la section 14</strong>, tous deux issus de la réparation et
tous deux à trancher&nbsp;: les trente centimes qui séparent six mensualités d'emprunt de ce que la grille
décaisse, et les 808&nbsp;€ de TVA versée, que les déclarations trimestrielles ne reconstituent pas.</li>
<li><strong>Le sigle IS entre au lexique</strong>, section 11, sur le patron de la SAS au Chapitre 2. C'est
lui qui rend lisible la ligne «&nbsp;444 État — IS à payer&nbsp;» du premier bloc du Chapitre 11.</li>
<li><strong>Une précision entre au recensement</strong>, section 6. «&nbsp;perte&nbsp;» au Chapitre 11,
troisième ancre du module qui est une réserve que le corps posait déjà. Onze chapitres sur treize en
portent une.</li>
<li><strong>Le Chapitre 11 dépose six entrées au registre des écarts</strong>, qui passe de 51 à 57.</li>
<li><strong>Volumes&nbsp;:</strong> Chapitre 11, 666 mots au périmètre déclaré, 686 avec les sous-titres&nbsp;;
Chapitre 10 v5, 677 et 716. Les deux dépassements sont motivés à l'annexe de chacun.</li>
</ul>

""" + d.s[_j:]
d.n += 1

# ═══ section 4 ══════════════════════════════════════════════════════════════
d.rep('<tr><td class="ch">10</td><td class="num">6</td><td class="num">3</td>'
      '<td class="num">9</td><td>Les trois ajustements de clôture</td></tr>',
      '<tr><td class="ch">10</td><td class="num">6</td><td class="num">3</td>'
      '<td class="num">27</td><td>Les trois ajustements de clôture. Les 27 automatiques sont trois '
      'écritures — la période du T4, les salaires du T4 avec les échéances de juillet à décembre, et les '
      'règlements de l\'exercice</td></tr>', 's4 ligne 10')

d.rep('<tr class="total"><td class="ch">Total</td><td class="num">49</td><td class="num">22</td>'
      '<td class="num">40</td><td>Total du module</td></tr>',
      '<tr class="total"><td class="ch">Total</td><td class="num">49</td><td class="num">22</td>'
      '<td class="num">58</td><td>Total du module</td></tr>', 's4 total')

d.rep("""<h3>Ce qu'aucun des deux régimes ne montre</h3>
<p>Le cumul des écritures listées ne reconstitue pas à lui seul le Bilan de clôture, et c'est voulu. Six familles
d'opérations sont exécutées par l'application sans figurer nulle part, parce qu'elles ne portent aucune notion
nouvelle et n'ont aucune valeur d'affichage : les encaissements de créances clients, les règlements de
dettes fournisseurs, les échéances d'emprunt de juillet à décembre, les bulletins de paie du quatrième
trimestre, les versements de TVA et les versements de cotisations sociales. Chacune répète un mécanisme
déjà passé à la main au moins une fois.</p>""",
      """<h3>Ce que les deux régimes ne montraient pas, et pourquoi ils le montrent</h3>
<p><strong>Ce document a porté jusqu'à la v21 un encadré qui disait l'inverse de ce qui suit</strong>, et le
cas vaut d'être gardé. Il listait six familles d'opérations exécutées par l'application sans figurer nulle
part, «&nbsp;parce qu'elles ne portent aucune notion nouvelle et n'ont aucune valeur d'affichage&nbsp;»&nbsp;:
les encaissements de créances clients, les règlements de dettes fournisseurs, les échéances d'emprunt de
juillet à décembre, les bulletins de paie du quatrième trimestre, les versements de taxe et les versements
de cotisations sociales.</p>
<p><strong>Le motif était vrai de la notion et faux de l'affichage.</strong> Chacune de ces familles répète
bien un mécanisme déjà passé à la main, et aucune n'apprend rien&nbsp;: le régime automatique est le bon.
Mais sans elles, le compte en banque finissait l'année à 99&nbsp;435,10&nbsp;€ contre 17&nbsp;310&nbsp;€
attendus, les créances clients à 252&nbsp;000&nbsp;€ contre 63&nbsp;000&nbsp;€, et le résultat à
54&nbsp;648,50&nbsp;€ contre 32&nbsp;000&nbsp;€. <strong>Le Bilan ne pouvait donc pas boucler au
Chapitre 11, qui est le moment fort du module.</strong> C'est l'écart que la v21 avait ouvert à la
section 14 et que la v22 ferme.</p>
<p><strong>Les six familles sont inscrites, et elles le sont au panneau du Chapitre 10</strong>, en deux
des trois écritures qu'il porte. La règle qui en sort&nbsp;: <strong>une opération sans notion nouvelle
peut malgré tout être indispensable à ce que la grille affiche</strong>, et le régime automatique existe
précisément pour celles-là. Le contrôle à faire devant un panneau n'est pas seulement «&nbsp;qu'apprend
cette ligne&nbsp;», c'est aussi «&nbsp;que manque-t-il aux deux documents si elle n'y est pas&nbsp;».</p>""",
      's4 encadré')

# ═══ section 6 ══════════════════════════════════════════════════════════════
d.rep('<tr><td class="ch">10</td><td class="cle">Une seule provision</td>'
      '<td>Traitée en profondeur plutôt qu\'un tour d\'horizon des types de provisions.</td></tr>',
      '<tr><td class="ch">10</td><td class="cle">Une seule provision, et les règlements de l\'année groupés</td>'
      '<td>La provision est traitée en profondeur plutôt qu\'un tour d\'horizon des types de provisions. '
      'Et les opérations du dernier trimestre comme les règlements de l\'année sont regroupés en trois '
      'écritures, enregistrées automatiquement.</td></tr>', 's6 alerte 10')

d.rep('<tr><td class="ch">11</td><td class="cle">Impôt simplifié</td>'
      '<td>Pas d\'acomptes trimestriels, conditions d\'éligibilité au taux réduit supposées remplies, '
      'pas de régime mère-fille.</td></tr>\n</tbody>',
      '<tr><td class="ch">11</td><td class="cle">Impôt simplifié</td>'
      '<td>Pas d\'acomptes trimestriels, conditions d\'éligibilité au taux réduit supposées remplies, et '
      'impôt calculé sur le bénéfice que le Compte de Résultat affiche plutôt que sur le bénéfice corrigé '
      'des charges que la loi n\'admet pas en déduction. <strong>Le régime mère-fille sort de l\'alerte</strong> '
      'à la rédaction&nbsp;: il ne concerne pas une société détenue par des personnes, et le signaler '
      'apprendrait au lecteur une exception qui ne le regarde pas. Il reste au registre des écarts.</td></tr>\n</tbody>',
      's6 alerte 11')

d.rep("""après «~le plus souvent~» au Chapitre 7. Elle ne coûte rien au corps, les 3~500~€ qu'elle
entoure étant ceux que le chapitre démontre.</td></tr>

</tbody>""",
      """après «~le plus souvent~» au Chapitre 7. Elle ne coûte rien au corps, les 3~500~€ qu'elle
entoure étant ceux que le chapitre démontre.</td></tr>
<tr><td class="ch">11</td><td class="cle">«~perte~»</td><td><strong>Écrite.</strong> Qu'une année qui se
termine sur une perte ne donne lieu à aucun impôt sur les sociétés, et que la perte n'est pas perdue pour
autant&nbsp;: elle vient en déduction des bénéfices des années suivantes et réduit l'impôt de ces
années-là. Ancrée au premier sous-titre, sur la réserve que le corps pose en écrivant que l'impôt ne se
calcule que sur un bénéfice. Vient de l'entrée 11.1 du registre, née de l'écriture et non connue d'avance
— second cas du module, après le Chapitre 9, mais pour un motif différent, aucune entrée n'existant encore
pour ce chapitre. <strong>Troisième fois du module que l'ancre est une réserve que le corps posait
déjà</strong>, après «~le plus souvent~» au Chapitre 7 et «~probable~» au Chapitre 10&nbsp;: trois
attestations font de ce patron le premier endroit où chercher, avant même d'ouvrir le registre.
<strong>Aucun chiffre n'y est écrit</strong>, comme au Chapitre 9 et pour la même raison — le plafond
annuel d'imputation d'un déficit bouge d'une loi de finances à l'autre.</td></tr>

</tbody>""", 's6 précision 11')

d.rep("""<strong>État~: dix chapitres écrits, dix précisions écrites, au 25~août 2026.</strong>
Les chapitres 11 à 13, non encore écrits, n'en portent aucune~; chacun posera la sienne à sa rédaction, en confrontant ses entrées du registre des écarts au test de la charte,
section 20 — une phrase remonte au texte, un paragraphe reste au registre. <strong>Sept des huit viennent
d'une entrée du registre sortie par le haut</strong>, la huitième étant celle du Chapitre 8, qui a fait
naître le dispositif.""",
      """<strong>État~: onze chapitres écrits, onze précisions écrites, au 25~août 2026.</strong>
Les chapitres 12 et 13, non encore écrits, n'en portent aucune~; chacun posera la sienne à sa rédaction, en confrontant ses entrées du registre des écarts au test de la charte,
section 20 — une phrase remonte au texte, un paragraphe reste au registre. <strong>Neuf des onze viennent
d'une entrée du registre sortie par le haut</strong>&nbsp;; celle du Chapitre 8 a fait naître le dispositif,
et celles des Chapitres 9 et 11 sont nées de l'écriture.""", 's6 état')

# ═══ section 9 ══════════════════════════════════════════════════════════════
d.rep('<tr><td class="ch">10</td><td>Fin d\'exercice</td><td class="num">30 min</td>'
      '<td class="num">6</td><td class="num">9</td></tr>',
      '<tr><td class="ch">10</td><td>Fin d\'exercice</td><td class="num">30 min</td>'
      '<td class="num">6</td><td class="num">27</td></tr>', 's9 ligne 10')

d.rep('Total (hors pauses)</td><td class="num">~6h10</td><td class="num">49</td>'
      '<td class="num">34</td></tr>',
      'Total (hors pauses)</td><td class="num">~6h10</td><td class="num">49</td>'
      '<td class="num">52</td></tr>', 's9 total', brut=True)

# ═══ section 10 — la fiche du Chapitre 11 ══════════════════════════════════
d.rep("""<p><strong>Rattachement — l'exception prévue par la charte.</strong> Le bloc 1 suit le sous-titre consacré à
l'impôt. Le bloc 2 ne se rattache à aucun sous-titre : il conclut le chapitre et, à travers lui, le module entier.
Il reste donc en fin de texte, seul, avant «~Ce que vous avez appris~». C'est le seul bloc manuel du module
qui n'est pas rattaché à une section.</p>""",
      """<p><strong>Rattachement — l'exception prévue par la charte.</strong> Le bloc 1 suit le sous-titre consacré à
l'impôt. Le bloc 2 ne se rattache à aucun sous-titre : il conclut le chapitre et, à travers lui, le module entier.
Il reste donc en fin de texte, seul, avant «~Ce que vous avez appris~». C'est le seul bloc manuel du module
qui n'est pas rattaché à une section.</p>
<p><strong>Deux arbitrages de la rédaction, tranchés le 25~août 2026 et validés à la livraison.</strong></p>
<p><strong>L'affectation du résultat passe avant le moment fort</strong>, et non après comme cette fiche le
prévoyait. Le motif est qu'elle est ce qui <em>démontre</em> le moment fort&nbsp;: la question à laquelle le
chapitre doit répondre est pourquoi un bénéfice s'inscrit du côté des ressources, et la réponse est qu'il
revient à quelqu'un — aux associés — dont l'affectation est précisément la décision. Placée après le report,
elle n'est qu'une information de plus. Le prix payé est que le lecteur lit une décision de dividende sur un
résultat qui n'est pas encore inscrit&nbsp;; le texte et la légende disent tous deux qu'elle se prend
«~plus tard, quelques mois après~».</p>
<p><strong>Le chapitre n'écrit pas que le résultat comble l'écart qu'on voyait</strong>, la section 4
l'interdisant. Il dit deux choses vérifiées par le rejeu&nbsp;: que le Bilan traîne un écart depuis le
premier jour d'activité, vrai à chaque instant du module, et que cet écart vaut 27~200~€ une fois le bloc 1
passé. Ce qui rend la phrase vraie au 31~décembre et ne l'était pas avant, c'est que l'écriture de soldes de
taxe du panneau du Chapitre 10 ferme les deux comptes de taxe — conséquence de la reprise du 10, et elle
n'était pas cherchée.</p>
<p><strong>Volume et forme, à la livraison&nbsp;:</strong> 666 mots au périmètre déclaré, 686 avec les
sous-titres. Deux sous-titres, trois lignes manuelles, aucune activité et aucun panneau automatique, comme
les sections 4 et 7 le prévoient. Le sigle IS accompagne l'impôt sur les sociétés à sa première occurrence,
sur le patron de la SAS au Chapitre 2&nbsp;: c'est lui qui rend lisible la seconde ligne du bloc 1.</p>""",
      's10 fiche 11')

# ═══ section 11 — lexique ══════════════════════════════════════════════════
d.rep('<tr><td class="cle">Impôt sur les sociétés</td><td class="ch">11</td>'
      '<td>Impôt assis sur le bénéfice</td></tr>',
      '<tr><td class="cle">Impôt sur les sociétés</td><td class="ch">11</td>'
      '<td>Impôt assis sur le bénéfice. Le sigle IS accompagne le nom complet à sa première occurrence '
      'dans le chapitre, sur le patron de «~SAS~» au Chapitre 2, et la forme courte s\'emploie ensuite. '
      'C\'est lui qui rend lisible l\'intitulé du compte 444, «~État — IS à payer~»</td></tr>',
      's11 lexique IS')

# ═══ section 13 — ordre de rédaction ═══════════════════════════════════════
d.rep("""<li><strong>Chapitre 11</strong> ensuite. <strong>L'écart de 22~648,50~€ de la section 14 se tranche
avant.</strong></li>""",
      """<li><strong>Chapitre 10, v5 — reprise du 25~août 2026.</strong> 677 mots, 716 avec les sous-titres.
Son panneau automatique passe de 9 à 27 lignes, en trois écritures, pour fermer l'écart de 22~648,50~€ et
réparer le Bilan de l'exercice. Aucune écriture manuelle ne bouge et le texte gagne quinze mots nets&nbsp;:
une phrase au premier sous-titre, qui prévient le lecteur de ce qui va défiler, payée par la coupe de seize
mots que l'annexe v4 proposait sans l'appliquer. <strong>C'est le chapitre qui a montré qu'un document de
référence peut documenter un trou au lieu de le combler</strong> — l'encadré de la section 4 listait
exactement les six familles d'opérations qui manquaient au Bilan.</li>
<li><strong>Chapitre 11 — livré.</strong> 666 mots, 686 avec les sous-titres. Deux sous-titres, trois lignes
manuelles, aucune activité et aucun composant. <strong>Son premier jet faisait 503 mots, et c'était un
défaut</strong>&nbsp;: la fiche ne lui donnant rien à déléguer, la section 19 de la charte fait d'un texte
nettement sous le seuil un signal d'alerte, celui du rédacteur qui écrit pour un lecteur connaissant déjà la
réponse. Les 163 mots ajoutés sont deux démonstrations, la seule catégorie de contenu qui ne sorte du texte
par aucun moyen. <strong>La première est celle que l'accroche réclamait</strong> — pourquoi l'écart des deux
colonnes du Bilan vaut exactement le résultat — et le premier jet ne la dénouait jamais. La règle qui en
sort&nbsp;: une accroche qui pose une tension doit la dénouer dans le texte, faute de quoi elle est un effet
et non un ordre de mission. Un tour de relecture profane, six corrections.</li>
<li><strong>Chapitres 12 et 13</strong> ensuite, quand le vocabulaire réellement employé est connu.</li>""",
      's13 ligne 11')

d.rep("""<li><strong>Chapitres 12 et 13</strong> en dernier, quand le vocabulaire réellement employé est connu.</li>""",
      '', 's13 ancienne ligne 12-13')

# ═══ section 14 — points ouverts ═══════════════════════════════════════════
_i = d.s.find('<li><strong>Le Compte de Résultat ne bouclera pas au Chapitre 11')
_j = d.s.find('</li>', d.s.find('outils/verif_ecart.py', _i)) + len('</li>')
assert _i > 0 and _j > _i, 'entrée de l\'écart introuvable à la section 14'
d.s = d.s[:_i] + """<li><strong>Les trente centimes de l'échéancier.</strong> Le panneau du Chapitre 10 fait
sortir 3&nbsp;773,10&nbsp;€ du compte en banque pour les six échéances de juillet à décembre, alors que six
mensualités de 628,90&nbsp;€ en font 3&nbsp;773,40&nbsp;€. <strong>L'écart vient de la section 3, pas du
chapitre</strong>&nbsp;: elle arrondit à l'euro les deux cumuls de l'exercice, 584&nbsp;€ d'intérêts et
3&nbsp;818&nbsp;€ de capital remboursé, et c'est de là que sortent le solde d'emprunt de 31&nbsp;182&nbsp;€
et la trésorerie de 17&nbsp;310&nbsp;€. L'échéancier réel donne 583,96&nbsp;€, 3&nbsp;818,34&nbsp;€ et un
solde de 31&nbsp;181,66&nbsp;€. Les nombres retenus sont ceux qui font tomber le Bilan sur
130&nbsp;410&nbsp;€&nbsp;; les prendre exacts déplacerait trois lignes du Bilan de trente centimes, donc son
total, donc le moment fort du Chapitre 11 et les trois ratios du Chapitre 12. <strong>La réparation la moins
chère est de ne rien changer aux nombres et d'écrire l'arrondi ici</strong>, à la ligne
«&nbsp;Emprunt&nbsp;» de la section 3. Un apprenant connaît la mensualité depuis le Chapitre 7 et peut
multiplier par six.</li>
<li><strong>Les 808&nbsp;€ de TVA versée ne se reconstituent pas.</strong> La section 3 écrit
«&nbsp;due sur l'exercice 5&nbsp;208&nbsp;€, dont 808&nbsp;€ versés et 4&nbsp;400&nbsp;€ restant dus au
31/12&nbsp;», et le panneau du Chapitre 10 porte cette ligne telle quelle. <strong>Les quatre trimestres
donnent autre chose</strong>&nbsp;: le premier doit 1&nbsp;200&nbsp;€, montant que l'apprenant calcule
lui-même au Chapitre 5&nbsp;; le deuxième 1&nbsp;800&nbsp;€&nbsp;; le troisième dégage un crédit de
4&nbsp;200&nbsp;€, le torréfacteur ayant été acheté le 1<sup>er</sup>&nbsp;juillet&nbsp;; le quatrième doit
6&nbsp;408&nbsp;€. Le total tombe bien sur 5&nbsp;208&nbsp;€, mais aucune combinaison de versements n'en
laisse 4&nbsp;400&nbsp;€ dus au 31 décembre. <strong>Or les 4&nbsp;400&nbsp;€ portent le Bilan</strong>, donc
les 130&nbsp;410&nbsp;€ et les ratios du Chapitre 12. Deux voies&nbsp;: tenir les 808&nbsp;€ pour un
paramètre du scénario et l'écrire à la section 3, ou refaire le calendrier des versements de taxe — ce qui
impose de recalculer l'ensemble du scénario et de le reporter dans les textes.</li>""" + d.s[_j:]
d.n += 1

# — le principe d'illustration : le Chapitre 11 quitte les dualités
d.rep("""Sont des dualités : les Chapitres 4 ✓, 5 ✓, 6 ✓, 8 ✓ et 11.
Sont des méthodes : les Chapitres 3 ✓, 7 ✓, 10 et 12. À trancher chapitre par chapitre, en écrivant la
légende, jamais après.</p>""",
      """Sont des dualités : les Chapitres 4 ✓, 5 ✓, 6 ✓ et 8 ✓.
Sont des méthodes : les Chapitres 3 ✓, 7 ✓, 11 ✓, 10 et 12. À trancher chapitre par chapitre, en écrivant la
légende, jamais après.</p>
<p><strong>Le Chapitre 11 est sorti des dualités en s'écrivant, comme le Chapitre 7, et pour le même
motif.</strong> Sa dualité est pourtant la plus nette du module — les mêmes 27~200~€ lus au bas du Compte de
Résultat, puis au Passif du Bilan — mais <strong>elle est déjà déléguée à un geste manipulable</strong>&nbsp;:
c'est exactement ce que son bloc de bouclage fait faire à l'apprenant sur les deux documents eux-mêmes. Une
illustration sur le même axe serait le doublon que le test des axes interdit, et elle montrerait en petit ce
que l'écran montre en grand. Son illustration porte donc l'autre axe, celui que les deux documents ne
montrent pas&nbsp;: le partage des 27~200~€ entre réserve légale, dividende et report à nouveau, hors Bilan
et hors Compte de Résultat, quelques mois plus tard.
<strong>La règle du Chapitre 7 s'élargit d'un cran, et c'est la partie utile&nbsp;:</strong> un chapitre
illustre autre chose que sa dualité dès lors que celle-ci est déjà déléguée à un geste manipulable,
<em>que ce geste soit un composant, comme au Chapitre 7, ou un bloc d'écritures sur les deux documents,
comme au Chapitre 11.</em> C'est l'illustration qui cède, jamais le geste.</p>""", 's14 familles')

d.rep("""montant au 4, un prix au 5, un stock au 6. Le principe ne s'use pas. Reste le Chapitre 11.</p>""",
      """montant au 4, un prix au 5, un stock au 6. Le principe ne s'use pas. Le Chapitre 11, qui restait,
n'a pas eu à s'en servir.</p>""", 's14 reste le 11')

d.rep("""Question à se poser aux Chapitres 5 et 11, qui sont des dualités et
portent aussi un composant.</p>""",
      """Question posée au Chapitre 5, qui est une dualité et porte aussi un composant. <strong>Le
Chapitre 11 l'a posée autrement et a répondu autrement&nbsp;:</strong> n'ayant pas de composant, c'est son
bloc d'écritures qui occupait l'axe de la dualité, et l'illustration a changé d'axe.</p>""",
      's14 question 5 et 11')

# — la ligne de pied du document
d.rep("""<p class="fin">Document de référence — Casoria, v20 du 24 août 2026. Aucune livraison de chapitre.""",
      """<p class="fin">Document de référence — Casoria, v22 du 25 août 2026. Livraison du Chapitre 11 et
reprise du Chapitre 10 en v5. Le Bilan de l'exercice boucle sur 130~410~€ des deux côtés, et le total de
contrôle du module vaut 1~294~694,00~€ au débit comme au crédit. Ce qui suit est le bilan de la v20, gardé
pour son raisonnement.""", 'pied')

# ═══ journal de rédaction ══════════════════════════════════════════════════
j.rep("""| 7 | « Le résultat et le solde bancaire ne mesurent pas la même chose, et ils ne bougent pas aux mêmes moments. » |""",
      """| 7 | « Le résultat et le solde bancaire ne mesurent pas la même chose, et ils ne bougent pas aux mêmes moments. » |

**Le Chapitre 11 n'en porte aucune, et le déroulé ne lui en prévoyait pas.** Il en touche pourtant le
terrain : l'impôt sur les sociétés est une charge de 2026 qui ne quittera le compte en banque qu'en 2027.
**Le fait est posé sans être commenté** — la légende du premier bloc dit que le compte en banque ne bouge
pas, et rien n'en conclut. C'est le troisième chapitre à faire ce choix, après le 3 et le 6, et il confirme
la règle qui en était sortie : un chapitre peut toucher le terrain du refrain sans le reprendre, à condition
de décrire et de ne pas conclure.""", 'refrain ch11')

j.ecrire()
d.ecrire()

# ─── renommage du déroulé en v22 ────────────────────────────────────────────
import os
os.rename('deroule-comprendre-la-comptabilite-v21.corps.html',
          'deroule-comprendre-la-comptabilite-v22.corps.html')
print('   déroulé renommé en v22')
