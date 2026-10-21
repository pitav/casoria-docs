#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Écrit le fichier de travail du Chapitre 12 — Piloter : la décision et les trois ratios.

Le texte est écrit avec « ~ » partout où un insécable est requis, et la
substitution se fait ici, en une passe. Piège 2 du LISEZ-MOI : ne jamais
taper l'insécable au clavier.
"""
NB = ' '
assert NB == chr(160), 'NB doit être un insécable, pas un espace ordinaire'

CORPS = r"""<p class="kicker">Casoria • Comprendre la comptabilité • Chapitre 12</p>
<h1>Piloter : la décision et les trois ratios</h1>

<div class="video"><span class="t">Vidéo d'ouverture — ~2 min</span>
<p>Douze mois de comptes tiennent maintenant dans deux documents complets. La vidéo pose la question
qu'ils servent à trancher, celle qui attend tout dirigeant le lendemain de sa première année. Une
entreprise qui a gagné de l'argent en a-t-elle pour autant~? Elle montre Claire devant la machine qu'elle
voudrait acheter, et annonce que la réponse se lit dans les comptes plutôt qu'elle ne se devine.</p></div>

<p class="accroche">Premiers jours de janvier. Le premier exercice de Latitude Café est arrêté sur
27~200~€ de bénéfice, et Claire voudrait une deuxième machine à torréfier, à 43~200~€ TTC. Le compte en
banque, lui, affiche 17~310~€. L'entreprise peut-elle se le permettre~?</p>

<h2>Le bénéfice de l'année n'est pas l'argent disponible</h2>
<p>Elle ne peut pas se le permettre, et cela ne tient pas à un excès de prudence. Retirer 43~200~€ de
17~310~€ met le compte en banque à −~25~890~€.</p>
<p>Ces 17~310~€ de trésorerie sont même moins disponibles qu'ils n'en ont l'air. Le Passif du Bilan porte deux dettes
envers l'État. La première vaut 4~400~€ de TVA à décaisser, la taxe que Latitude Café a facturée à ses
clients pour le compte de l'État depuis le Chapitre 5. La seconde vaut 4~800~€ d'impôt sur les sociétés,
calculé au chapitre précédent sur le bénéfice de l'année. Ces 9~200~€ partiront dans les mois qui suivent,
et l'entreprise ne peut rien en faire d'autre.</p>
<p>Deux chiffres disent donc deux choses différentes. Les 27~200~€ de bénéfice sont ce que l'activité a
gagné en douze mois, mesurés par le Compte de Résultat. Les 17~310~€ sont ce qui se trouve sur le compte en
banque au 31~décembre, portés par le Bilan. Le Chapitre 4 avait posé l'écart le jour où une facture de
1~450~€ était devenue une créance client sans que le compte en banque bouge.</p>

<h2>Un premier chiffre dit où l'argent est passé, dans le stock et chez les clients</h2>
<p>Reste à comprendre pourquoi la trésorerie est si basse alors que l'année a été bonne. La réponse est à
l'Actif du Bilan.</p>
<p>Le stock vaut 15~000~€. Ce café a été acheté, payé et torréfié, et il n'est pas encore vendu. Les
créances clients valent 63~000~€. Ces ventes-là ont été livrées et facturées, et elles ne sont pas encore
payées. Ces deux lignes sont de l'argent que l'entreprise a avancé sans l'avoir récupéré.</p>
<p>Une troisième ligne joue en sens inverse, au Passif. Les dettes fournisseurs valent 9~000~€, des
marchandises reçues et pas encore réglées. Ce sont autant d'euros que l'entreprise n'a pas eu à
avancer.</p>
<p>Ce que l'activité retient ainsi porte un nom, le BFR~: le <span class="lex">besoin en fonds de
roulement</span>. On l'obtient en ajoutant le stock aux créances clients et en retirant les dettes
fournisseurs. Pour Latitude Café, 15~000~€ plus 63~000~€ moins 9~000~€ font 69~000~€.</p>
<p class="declaration">Ces 69~000~€, l'entreprise ne les a pas perdus, elle les a rangés dans son stock et
dans les factures que ses clients n'ont pas encore payées.</p>
<div class="composant"><code>&lt;SimulateurBfr /&gt;</code>
<span class="cap">Trois curseurs (stock, créances clients, délai accordé par le fournisseur) pour
chercher ce qui financerait la machine</span></div>
<p>Trois manières de réduire ce besoin existent, et ce sont les trois lignes du calcul. Vendre le stock
plus vite, être payé plus tôt, régler le fournisseur plus tard. Le calcul du chapitre ne retient que ces
trois lignes de l'activité courante, alors qu'un banquier en regarde quelques autres.</p>

<h2>Deux ratios en disent plus que les sommes elles-mêmes</h2>
<p>Le besoin en fonds de roulement est une somme, et une somme ne se compare qu'à une autre somme de
même taille. Les deux outils qui suivent divisent un chiffre du Bilan ou du Compte de Résultat par un autre
et donnent un pourcentage. On appelle <span class="lex">ratio</span> ce genre de division, et son intérêt
est là~: un pourcentage se compare d'une année sur l'autre, et d'une entreprise à une autre, même si elles
n'ont pas la même taille.</p>
<p>La <span class="lex">marge nette</span> décrit ce qui reste à l'entreprise sur ce qu'elle a vendu.
Latitude Café a vendu pour 268~000~€ dans l'année, les deux lignes de ventes du Compte de Résultat
additionnées, et elle en a gardé 27~200~€ une fois tout payé, fournisseurs, salaires, banque et État
compris. Cela fait 10,1~%, soit dix euros gardés sur cent euros vendus. C'est un bon résultat pour une
première année dans ce métier.</p>
<p>L'<span class="lex">autonomie financière</span> décrit autre chose, la part de ce que l'entreprise
détient qu'elle gardera tant qu'elle vivra, par opposition à ce qu'elle devra rendre. Le Bilan de Latitude
Café totalise 130~410~€. Sur cette somme, 57~200~€ viennent des associés et de l'année écoulée, les
30~000~€ de capital apportés à la création et les 27~200~€ de bénéfice. Ces deux lignes réunies sont ce que le Chapitre 2 appelle les
capitaux propres. Les 15~000~€ du compte courant d'associé n'en font pas partie, cette somme ayant été prêtée à
la société et non apportée à son capital.</p>
<p>57~200~€ sur 130~410~€ font 43,9~%. Un peu moins de la moitié de ce que l'entreprise détient, elle le
gardera donc tant qu'elle vivra. Plus ce pourcentage est bas, plus elle dépend de ceux à qui elle doit de l'argent,
et c'est l'une des premières choses qu'une banque regarde avant de prêter.</p>
<p>Un ratio ne dit rien
<button aria-describedby="p12-colonnes" class="prec" type="button">tout seul</button>. Ces deux
pourcentages ne prennent leur sens que comparés, à d'autres entreprises de la même taille et à ceux que
Latitude Café affichera l'an prochain.</p>
<p class="prec-note" id="p12-colonnes" role="note">Le Bilan et le Compte de Résultat de ce module portent
une seule colonne de chiffres. Ceux qu'une entreprise publie en portent deux, l'exercice qui vient de se
terminer et le précédent, côte à côte. C'est le premier exercice de Latitude Café, il n'a rien à côté de
quoi se ranger. Sur de vrais comptes, la comparaison des deux colonnes est souvent ce qu'on regarde avant
les montants eux-mêmes.</p>
<div class="image-slot"><span class="t">[IMAGE]</span>
<p class="cap">Légende : Où est l'argent de Latitude Café au 31~décembre. Les 63~000~€ de créances
clients et les 15~000~€ de stock pèsent chacun plus lourd que les 17~310~€ de trésorerie, et les 9~000~€
de dettes fournisseurs n'en couvrent qu'une petite part. À la même échelle, à côté, les 43~200~€ de la
machine.</p></div>
<p>Lire ces trois chiffres est un début. Les manier ensemble pour décider quand emprunter, quand allonger
un délai ou quand refuser une commande est l'objet d'une formation à part, qui suppose des comptes déjà
tenus et déjà lus.</p>
<div class="appris">
<h2>Ce que vous avez appris</h2>
<ul>
<li>Latitude Café a gagné 27~200~€ et n'avait que 17~310~€ de trésorerie au 31~décembre, dont 9~200~€
promis à l'État. La machine à 43~200~€ attendra.</li>
<li>Les 69~000~€ de besoin en fonds de roulement disent où l'argent est passé, dans 15~000~€ de stock et
63~000~€ de factures clients impayées, moins 9~000~€ dus aux fournisseurs.</li>
<li>Deux ratios situent l'entreprise. Sa marge nette vaut 10,1~%, dix euros gardés sur cent vendus, et son
autonomie financière 43,9~%, la part de son Bilan financée par ses associés et par son bénéfice.</li>
</ul>
</div>"""

CHAPO = r"""<p class="chapo"><strong>Version v2, livrée.</strong> Rédigée le 25~août 2026 sous la
charte v14 et le déroulé v22, avec les Chapitres 1, 2, 4, 5, 6, 8 et 11 sous les yeux — ceux dont ce
chapitre relit les lignes. <strong>Un tour de relecture profane, vingt corrections, toutes
appliquées</strong>, dont sept qui portent sur la lisibilité pour un profane. Trois sous-titres, aucune
écriture, un composant, une illustration et une précision neuve ancrée sur «~tout seul~». La piste ouverte
par la fiche, les colonnes N et N–1, a été tranchée avec Pascal avant rédaction~; l'entrée 1.5 du registre
sort par le haut et devient la précision du chapitre. <strong>Trois points laissés ouverts au tour de
relecture sont tranchés en faveur du texte à la livraison</strong>, et leurs rechanges restent écrites à
l'annexe. Ce fichier est le fichier de travail~: il porte le chapo et l'annexe de contrôle, que le fichier
de livraison ne porte pas. <strong>Le registre, le déroulé et le journal sont répercutés</strong> le
26~août 2026, le déroulé passant en v23. La charte v14 est inchangée.</p>"""

out = CORPS.replace('~', NB).replace(
    '<h1>Piloter : la décision et les trois ratios</h1>',
    '<h1>Piloter : la décision et les trois ratios</h1>\n' + CHAPO.replace('~', NB), 1)
assert '<p class="chapo">' in out
open('ch12-travail.html', 'w', encoding='utf-8').write(out + '\n')
print('écrit : ch12-travail.html —', len(out), 'caractères,', out.count(NB), 'insécables')
