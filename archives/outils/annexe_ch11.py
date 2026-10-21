#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute l'annexe de relecture au fichier de travail du Chapitre 11.

Annexe RÉDUITE aux points de vigilance : charte v14, section 22. Ce qui a été
arbitré sans consigne, ce qui s'écarte d'une fiche du déroulé, ce qui demande
une décision.
"""
import re

F = 'ch11-travail.html'
s = open(F, encoding='utf-8').read()
NB = '\u00a0'
assert NB == chr(160), 'NB doit être un insécable, pas un espace ordinaire'

ROWS = [

('Relecture profane, tour 1', 'SIX CORRECTIONS — DEUX POINTS OUVERTS', """
<strong>Six corrections de Pascal le 25~août 2026, toutes appliquées.</strong> Trois de forme —
«~le bénéfice d'avant impôt~» devient «~le bénéfice avant impôt~», et le renvoi au Chapitre 2 se lit
«~les quatre premières écritures du Chapitre 2 à la création de la société~».
<strong>Deux appellent une décision, et l'annexe ne les tranche pas seule.</strong>
<strong>Un — «~petite~» retiré du barème.</strong> Le texte disait «~jusqu'à 42~500~€ de bénéfice, une
petite société est imposée à 15~%~», et Pascal signale que l'adjectif laisse supposer qu'une société plus
grosse est imposée autrement sur cette première tranche. Il a raison sur ce que le lecteur comprend.
<strong>Le mot portait pourtant une exactitude</strong>~: le taux de 15~% n'est pas ouvert aux grandes
sociétés, qui sont à 25~% dès le premier euro. Sans lui, les deux phrases se lisent comme un barème
universel, ce qu'elles ne sont pas. <strong>Ce qui rattrape aujourd'hui~:</strong> la phrase suivante dit
que Latitude Café «~reste en dessous, comme la plupart des entreprises de sa taille~»,
l'<code>&lt;UAlert&gt;</code> dit que les conditions du taux réduit sont supposées remplies, et l'entrée
11.3 du registre porte la formulation complète. <strong>Rechange, si le point revient~:</strong>
«~une société de cette taille est imposée à 15~%~», qui dit la condition sans la qualifier.
<strong>Deux — la fin vague du troisième paragraphe.</strong> «~Ce bénéfice-là porte un nom à lui~»
demandait, selon Pascal, ou bien le nom, ou bien une autre tournure. <strong>Le nom était déjà donné deux
paragraphes plus haut</strong>, et le redonner l'aurait dit deux fois~; la phrase a donc été refaite sur
les deux nombres, «~sur les 32~000~€ et non sur les 27~200~€ qui restent une fois l'impôt inscrit~». Elle
répond à la même question et donne au lecteur le second nombre avant que le paragraphe suivant ne le
nomme.
<strong>Une correction porte un accord.</strong> «~Le même nombre~» devient «~la même somme~», au
féminin~; la note de relecture écrivait «~le même somme~».
<strong>Et une entre au déroulé.</strong> Le sigle IS accompagne désormais l'impôt sur les sociétés à sa
première occurrence, sur le patron du Chapitre 2 pour la SAS. <strong>C'est ce qui rend lisible la
seconde ligne du bloc~1</strong>, «~444 État — IS à payer~», que rien ne développait jusqu'ici. À porter
au lexique cumulatif du déroulé, section 11.""" ),

('Volume du texte', 'AU SEUIL — 666', """
<strong>666 mots au périmètre déclaré, 686 avec les sous-titres</strong>, pour un seuil de vigilance de 680
(charte, section 19). Le chapitre tient donc sous le seuil au périmètre que le module mesure, et le
dépasse de six mots si l'on compte les sous-titres, comme la ligne du Chapitre 10 le fait au déroulé,
section 13. Le premier tour de relecture profane a coûté trois mots. <strong>Le premier jet en faisait 503, et c'était un défaut, pas une performance.</strong>
La section 19 le dit~: sur un chapitre à forte densité, un texte nettement sous le seuil signale d'abord
qu'on écrit pour un lecteur qui connaît déjà la réponse. La question qu'elle impose — à quoi ce texte
délègue-t-il~? — a une réponse vide ici, la fiche du déroulé ne prévoyant ni activité ni composant pour ce
chapitre.
<strong>Les 163 mots ajoutés sont deux démonstrations</strong>, la seule catégorie de contenu que la
section 19 dit ne pouvoir sortir d'aucune façon du texte. La première répond à la question que l'accroche
pose et que le premier jet laissait sans réponse~: pourquoi l'écart du Bilan est-il exactement le
résultat. La seconde écarte le contresens le plus probable du chapitre, celui du lecteur qui recalculerait
l'impôt sur le résultat que l'impôt vient de faire baisser.
<strong>Périmètre déclaré, mesuré par script~:</strong> l'accroche et le corps. En sortent la vidéo, les
sous-titres, les blocs d'écritures, leurs légendes, la légende d'illustration, l'<code>&lt;UAlert&gt;</code>,
la précision et le bloc «~Ce que vous avez appris~», qui pèse 92 mots.""" ),

('Budget de deux-points', '1 → 1', """
<strong>Notation~: premier jet → état soumis.</strong> Cinq sections comptées, un seul deux-points en prose,
à l'accroche, où il annonce les deux totaux du Bilan et l'écart entre eux.
<strong>Il est motivé.</strong> C'est un dénombrement suivi immédiatement de ses éléments, la forme que la
charte, section 12, huitième famille, exige quand on annonce un compte.
<strong>Hors compte~:</strong> un dans la légende d'illustration, aucun dans les deux légendes de bloc
d'écritures.""" ),

('Écritures manuelles', '3 LIGNES', """
Deux blocs d'écritures, répartis <strong>1~/~0</strong> sur les deux sous-titres, le second en fin de
texte comme la fiche l'impose.
<strong>Le mécanisme que chaque bloc introduit~:</strong> bloc~1, une charge qui naît d'un calcul et non
d'un document reçu, et dont la contrepartie est une dette envers l'État~; bloc~2, le report du résultat au
Passif, qui n'est pas une opération et ne passe pas par le grand journal. Aucune répétition.
<strong>Le bloc~2 est le seul du module qui ne se rattache à aucun sous-titre</strong>, l'exception prévue
et bornée par la charte, section 15~: il conclut le chapitre et, à travers lui, le module. Il est précédé
d'un paragraphe qui n'appartient lui non plus à aucune section, et c'est ce paragraphe qui met le geste en
scène.""" ),

('Place de l\'affectation du résultat', 'ÉCART À LA FICHE — DÉCISION', """
<strong>La fiche du déroulé range l'affectation en dernier</strong>, après le moment fort, «~puisque
l'opération intervient après la clôture~». <strong>Elle est ici au second sous-titre, avant le moment
fort.</strong>
<strong>Le motif est que l'affectation est ce qui démontre le moment fort.</strong> La question à laquelle
le chapitre doit répondre est pourquoi un bénéfice s'inscrit du côté des ressources. La réponse est qu'il
revient à quelqu'un — aux associés — et l'affectation est précisément ce que ce quelqu'un en décide. Placée
après le report, elle devient une information de plus~; placée avant, elle est la raison du report.
<strong>Le prix payé~:</strong> le lecteur lit une décision de dividende sur un résultat qui n'est pas
encore inscrit au Bilan. Le texte le dit — la décision se prend «~plus tard, quelques mois après~» — et la
légende d'illustration le redit.
<strong>À trancher.</strong> Revenir à l'ordre de la fiche coûterait la démonstration, ou obligerait à
l'écrire deux fois.""" ),

('L\'illustration et la famille du chapitre', 'ÉCART À LA FICHE — DÉCISION', """
<strong>La section 14 du déroulé range le Chapitre 11 dans les dualités</strong> et laisse sa légende à
trancher en l'écrivant, ce qui est fait ici. <strong>Le chapitre en sort, comme le Chapitre 7 en était
sorti, et pour le même motif.</strong>
<strong>La dualité de ce chapitre est déjà portée par un geste, et ce geste n'est pas une image.</strong>
Les 27~200~€ lus deux fois — au bas du Compte de Résultat, puis au Passif du Bilan — sont exactement ce que
le bloc~2 fait faire à l'apprenant sur les documents eux-mêmes. Une illustration sur le même axe serait le
doublon que le test des axes interdit, et elle montrerait en petit ce que l'écran montre en grand.
<strong>L'illustration porte donc l'autre axe</strong>, celui que la grille ne montre pas~: le partage des
27~200~€ entre réserve légale, dividende et report à nouveau, hors Bilan et hors Compte de Résultat,
quelques mois plus tard. C'est aussi ce que la fiche demandait — «~en schéma illustré, hors grille~».
<strong>Ce que le cas ajoute à la règle du Chapitre 7</strong>, et qui vaut d'être écrit~: un chapitre
illustre autre chose que sa dualité dès lors que celle-ci est déjà déléguée à un geste manipulable, que ce
geste soit un composant, comme au Chapitre 7, ou un bloc d'écritures sur les deux documents, comme
ici.""" ),

('Titre du chapitre', 'DÉCISION DEMANDÉE', """
<strong>Le titre retenu est celui du déroulé, «~La clôture~», amputé de sa parenthèse de
fabrication.</strong>
<strong>Il pose un problème que la rédaction n'a pas le droit de trancher seule.</strong> Le mot
«~clôture~» est introduit et coloré au Chapitre 10, dont le titre est «~Fin d'exercice~», et ce sont les
écritures du Chapitre 10 qui font la clôture. Un lecteur qui arrive au Chapitre 11 a donc déjà appris le
mot, et son titre lui annonce ce qu'il vient de faire.
<strong>Deux formulations de rechange, si le point est retenu~:</strong> «~Le résultat rejoint le Bilan~»,
qui dit l'objectif de la fiche — boucler la boucle ouverte au Chapitre 1 — et «~Ce qu'il reste à la fin~»,
plus proche du registre des autres titres. Le second sous-titre du chapitre reste le même dans les deux
cas.""" ),

('La précision', 'NEUVE — ANCRÉE SUR «~PERTE~»', """
<strong>Ancre~: «~perte~», au premier sous-titre</strong>, sur la réserve que le corps pose déjà en
écrivant que l'impôt ne se calcule que sur un bénéfice. <strong>Troisième fois du module qu'une ancre est
une réserve du corps</strong>, après «~le plus souvent~» au Chapitre 7 et «~probable~» au Chapitre 10.
<strong>Elle vient de l'entrée 11.1 du registre, créée en écrivant</strong>, et non d'une entrée connue
d'avance. Second cas du module après le Chapitre 9.
<strong>Aucun chiffre n'y est écrit, volontairement</strong>, comme à la précision du Chapitre 9~: le
plafond annuel d'imputation d'un déficit bouge d'une loi de finances à l'autre et une note chiffrée
vieillirait mal. Elle ne coûte rien au corps, l'ancre n'étant pas un nombre venu du décor.""" ),

('La ligne «~Bilan seul~»', 'PREMIÈRE DU MODULE — OUTIL', """
<strong>Le report du résultat au Passif est la première ligne «~Bilan seul~» du module</strong>, la
destination que la charte, section 17, définit comme un report calculé par l'application, sans écriture au
journal.
<strong>rejeu.py ne sait pas la lire</strong>, son motif ne reconnaissant que «~Bilan~», «~CR~» et
«~GdJal seul~». Il l'annonce comme ligne non lue et son contrôle d'équilibre reste vrai, le bloc ne portant
aucune écriture de journal. <strong>C'est la loi des défauts d'outil du LISEZ-MOI</strong> — un script ne se
trompe que sur ce qu'aucun chapitre antérieur ne lui avait présenté — et le script n'a pas été modifié.
<strong>Un script neuf a été écrit à la place, <code>outils/verif_cloture.py</code></strong>, qui rejoue
les panneaux, sépare les comptes par leur destination et reconstruit les deux documents. Il vérifie le
Bilan poste par poste contre le scénario chiffré du déroulé, section 3. <strong>Tous les nombres des deux
légendes de bloc en sortent</strong>, et aucun n'a été écrit de mémoire.""" ),

('Ce que le chapitre ajoute à sa fiche', 'DEUX PARAGRAPHES', """
<strong>La fiche liste cinq contenus. Le chapitre en porte deux de plus, et les deux sont des
démonstrations.</strong>
<strong>Premier~:</strong> l'impôt est une charge de l'année, il fait baisser le résultat, et il ne se
recalcule pas sur le résultat qu'il vient de faire baisser. C'est la question qu'un lecteur non comptable
se pose immédiatement après avoir vu 32~000~€ devenir 27~200~€, et c'est ce qui justifie qu'un bénéfice
d'avant impôt porte un nom à lui.
<strong>Second~:</strong> pourquoi l'écart entre les deux colonnes du Bilan vaut exactement le résultat.
L'accroche pose la question et le premier jet ne la rappelait jamais. <strong>Une accroche qui pose une
tension doit la dénouer dans le texte</strong>, faute de quoi elle est un effet et pas un ordre de mission
(charte, section 3).""" ),

('Registre des écarts', 'SIX ENTRÉES NEUVES', """
<strong>11.1 le déficit et son report</strong> — sortie par le haut, c'est la précision du chapitre.
<strong>11.2 les acomptes d'impôt sur les sociétés</strong>, signalée à l'<code>&lt;UAlert&gt;</code>.
<strong>11.3 les conditions du taux réduit</strong>, signalée elle aussi.
<strong>11.4 le passage du résultat comptable au résultat fiscal</strong>, signalée en une phrase de
l'<code>&lt;UAlert&gt;</code> — les charges que la loi n'admet pas en déduction.
<strong>11.5 la fiscalité du dividende chez l'associé</strong>, silencieuse, candidate au module ultérieur~:
c'est un impôt de la personne, pas de la société, et le chapitre n'en dit rien.
<strong>11.6 la réserve légale et son plafond</strong>, silencieuse — le corps dit que la loi l'exige et ne
dit ni combien ni jusqu'à quand.
Chacune arrive avec sa phrase rédigée, la contrainte principale du registre.""" ),

('Déclaration en gras et refrain', 'CONFORME', """
<strong>La déclaration est une subordonnée causale</strong> — «~le résultat figure au Passif parce qu'il
appartient à quelqu'un d'autre que l'entreprise qui l'a gagné~». <strong>Onzième forme du module</strong>,
et elle ne ressemble ni à celle du Chapitre 10, une hypothétique à sujet infinitif, ni à celle du
Chapitre 9, une comparative. À consigner au journal de rédaction.
<strong>Aucune reprise du refrain</strong>, le déroulé n'en prévoyant pas ici — les reprises sont aux
Chapitres 4, 5, 7, 10 et 12. Le chapitre en touche pourtant le terrain, l'impôt étant une charge de 2026
qui ne quittera le compte en banque qu'en 2027. <strong>Le fait est posé sans être commenté</strong>, comme
le Chapitre 6 et le Chapitre 3 l'avaient fait avant lui~: la légende du bloc~1 dit que le compte en banque
ne bouge pas, et rien n'en conclut.""" ),

('Ce qui reste à faire', 'AVANT LIVRAISON', """
<strong>Le second tour de relecture profane</strong>, si les deux points ouverts ci-dessus en appellent
un. Le fichier de livraison ne se produit qu'après, et son existence est la preuve que la relecture a eu
lieu (charte, section 22).
<strong>Le Chapitre 10 v5 circule avec celui-ci</strong> et les deux se relisent ensemble~: le Bilan que ce
chapitre fait boucler n'existe que si la reprise du 10 est validée.
<strong>Répercussions à passer après validation</strong>, en une fois~: déroulé, section 14 (l'écart se
ferme et la ligne disparaît), section 3 (rien à changer, le scénario est atteint à l'euro), section 4 et
section 9 (le panneau du Chapitre 10 passe de 9 à 27 lignes), section 6 (la précision du Chapitre 11,
ancre «~perte~»), section 13 (les lignes des Chapitres 10 v5 et 11), section 14 (la famille d'illustration
du Chapitre 11, qui quitte les dualités)~; registre des écarts (six entrées)~; déroulé, section 11 (le sigle IS au lexique cumulatif)~; journal de rédaction (la
onzième forme de déclaration, les six corrections du premier tour à la table «~Relectures profanes~», et
le total de contrôle du module qui passe de 773~584,90~€ à 1~294~694,00~€).""" ),
]

CONTROLES = [

('Rejeu du journal', 'FAIT — AUCUN ÉCART', """
Toutes les phrases du chapitre qui décrivent un mouvement dans les deux documents ont été rejouées par
script, bloc par bloc, depuis la première écriture du Chapitre 2. <strong>Aucun nombre n'a été écrit de
mémoire.</strong>
<strong>Vérifiés à l'euro :</strong> l'accroche annonce 130~410~€ à l'Actif et 98~410~€ au Passif, et
c'est ce que la grille affiche au moment où le lecteur la lit~; le total des charges monte bien de
251~000~€ à 255~800~€ au passage du bloc~1, et le résultat descend bien de 32~000~€ à 27~200~€~; le Passif
monte bien de 98~410~€ à 103~210~€, puis à 130~410~€ au bloc~2, l'Actif ne bougeant à aucun des deux.
<strong>L'écart de 27~200~€ annoncé au second sous-titre</strong> est bien celui que la grille porte à cet
instant-là, c'est-à-dire après le bloc~1 et avant le bloc~2. C'est le seul nombre du chapitre qui dépende
de l'endroit où il est écrit.
<strong>Arithmétique refaite :</strong> 32~000~€ à 15~% font 4~800~€, et 32~000~€ moins 4~800~€ font
27~200~€. Le Bilan de clôture se referme sur 130~410~€ des deux côtés, poste par poste, conformément au
scénario chiffré du déroulé, section 3.
<strong>Total de contrôle du module au terme du Chapitre 11 : 1~294~694,00~€</strong> au débit comme au
crédit. Il ne comprend pas le report du résultat, qui ne passe pas par le grand journal.""" ),

('L\'écart des deux colonnes et le résultat', 'MISE EN GARDE DE LA SECTION 4 — RESPECTÉE', """
<strong>Le déroulé, section 4, interdit à ce chapitre de présenter l'inscription du résultat comme
«~le résultat comble l'écart qu'on voyait~».</strong> Le motif est mesuré~: au point d'étape du
Chapitre 8, l'écart entre les deux colonnes vaut 20~912,50~€ et le résultat implicite 26~312,50~€, la
différence de 5~400~€ étant le solde net des deux comptes de taxe, qui vivent au grand journal seul et
n'ont aucune case au Bilan.
<strong>Le texte ne dit pas cela.</strong> Il dit deux choses, et les deux sont vraies~: que le Bilan
traîne un écart depuis le premier jour d'activité, ce qui est vrai à chaque instant du module~; et que cet
écart vaut 27~200~€ ce soir, ce qui est vérifié par le rejeu. <strong>Il ne dit à aucun moment que l'écart
a toujours valu le résultat.</strong>
<strong>Ce qui rend la phrase vraie au 31~décembre</strong>, et ne l'était pas avant~: l'écriture de
soldes de TVA du panneau du Chapitre 10 ferme les deux comptes de taxe. C'est une conséquence de la
reprise du 10, et elle n'était pas cherchée.""" ),

('Checklist de relecture', 'QUARANTE-DEUX CASES — AUCUNE EN DÉFAUT', """
Charte, section 21. <strong>Vingt-quatre cases sont passées par script</strong>, le reste à la lecture.
<strong>Ce que le script vérifie et qui est vert :</strong> aucun mot de la liste des interdits~;
«~toucher~» absent~; au plus un tiret cadratin en prose, et il y en a zéro~; la glose (emploi) et
(ressource) une fois chacune~; une seule déclaration en gras, sans terme de lexique dedans~; les sept
termes du lexique colorés une seule fois, aucun coloré dans un titre~; une précision, son ancre hors
lexique, sa note présente et son <code>aria-describedby</code> résolu~; Bilan et Compte de Résultat jamais
en minuscules~; toutes les sommes avec leurs insécables et leur unité~; trois lignes manuelles sur un
plafond de huit~; un <code>&lt;UAlert&gt;</code> après le dernier sous-titre~; deux sous-titres et aucun
niveau 3~; aucun nom propre de personne à l'accroche~; «~bloc~» jamais nu et «~la grille~» absente~; le
bloc de clôture à trois points.
<strong>Les cases de jugement</strong> sont détaillées aux lignes ci-dessus~: volume, budget de
deux-points, rattachement des blocs, précision, renvois aux Chapitres 1 et 2 avec leur substance et leur
nom, illustration, déclaration, refrain non repris.
<strong>La quarante-deuxième case</strong>, celle que le rédacteur ne peut pas cocher seul, est cochée par
le tour de relecture de Pascal du 25~août 2026 et ses six corrections.""" ),

('Production du fichier', 'CONFORME', """
Fichier produit sous la charte, section 22. <strong>Le fichier de livraison ne porte que ce qui
s'affichera à l'apprenant</strong>~: le chapo de version et cette annexe en sortent et vivent au PDF de
livraison. Les deux fichiers portent le même texte au caractère près, contrôlé sur le source dépouillé de
ses balises par expression régulière — jamais par un parseur, qui avalerait le contenu d'un
<code>&lt;template&gt;</code>.
La précision est écrite en dur, et l'<code>&lt;UAlert&gt;</code> est converti depuis la classe
<code>.alert</code> du fichier de travail. <strong>Le PDF de livraison revient au pointillé sur
l'ancre</strong>, qui est la forme réelle~; les PDF de relecture la portaient en souligné plein.
<strong>Le fichier n'a été produit qu'après la demande de Pascal</strong>, la charte interdisant au
rédacteur de le produire de sa propre initiative.""" ),

('Répercussion', 'DÉROULÉ v22 ET JOURNAL — FAITE', """
<strong>Au registre des écarts :</strong> six entrées, 11.1 à 11.6, écrites le jour de la rédaction. Le
compte passe de 51 à 57, recompté par script.
<strong>Au déroulé, section 6 :</strong> la ligne du Chapitre 11 au recensement des précisions, ancre
«~perte~», et la mention <strong>Écrite.</strong> L'<code>&lt;UAlert&gt;</code> du Chapitre 11 est réécrit
au recensement — il porte les acomptes, les conditions du taux réduit et le résultat fiscal, et non le
régime mère-fille que la fiche annonçait.
<strong>Au déroulé, section 11 :</strong> le sigle IS au lexique cumulatif, sur le patron de la SAS au
Chapitre 2.
<strong>Au déroulé, section 13 :</strong> la ligne du Chapitre 11, 666 mots.
<strong>Au déroulé, section 14 :</strong> le Chapitre 11 quitte la famille des dualités et rejoint les
méthodes, avec la règle élargie — un chapitre illustre autre chose que sa dualité dès lors que celle-ci
est déjà déléguée à un geste manipulable, que ce geste soit un composant ou un bloc d'écritures.
<strong>Au déroulé, section 10 :</strong> la fiche du Chapitre 11 reçoit ses deux arbitrages, la place de
l'affectation et la famille d'illustration.
<strong>Au journal de rédaction :</strong> la déclaration du Chapitre 11 est une subordonnée causale,
onzième forme du module~; les six corrections du tour de relecture à la table des relectures profanes~; le
total de contrôle du module.
<strong>À la charte : rien.</strong> La v14 avait déjà corrigé la clause de placement de
l'<code>&lt;UAlert&gt;</code>, seul point que ce chapitre aurait pu ouvrir.""" ),
]

import sys
if len(sys.argv) > 1 and sys.argv[1] == 'complete':
    ROWS = ROWS + CONTROLES

_COMPLETE = len(sys.argv) > 1 and sys.argv[1] == 'complete'
_TITRE = 'Annexe de contrôle' if _COMPLETE else 'Annexe de relecture'
_INTRO = ("""Annexe complète, produite à la livraison~: elle recense tout ce qui a été vérifié, et c'est
elle qui permet de revérifier la checklist un chapitre plus tard. Les premières lignes portent ce qui a été
arbitré sans consigne et ce qui s'écarte d'une fiche du déroulé~; les dernières portent les contrôles.
Charte, section 22."""
 if _COMPLETE else
 """Annexe réduite aux points de vigilance, charte v14, section 22~: ce qui a été arbitré sans consigne, ce
qui s'écarte d'une fiche du déroulé, ce qui demande une décision. Les contrôles conformes ne sont pas
recensés ici~; ils le seront à l'annexe de contrôle complète, produite à la livraison.""")

TETE = f"""<h2 class="saut">{_TITRE}</h2>
<p>{_INTRO}</p>
<table>
<thead><tr><th>Point</th><th>État</th><th>Détail</th></tr></thead>
<tbody>
"""

corps = ''.join(
    f'<tr><td class="cle">{cle}</td><td>{etat}</td><td>' + ' '.join(detail.split()) + '</td></tr>\n'
    for cle, etat, detail in ROWS)

annexe = (TETE + corps + '</tbody>\n</table>\n')

# ─── insécables de l'annexe : guillemets et sommes (piège 3 du LISEZ-MOI) ────
annexe = annexe.replace('~', NB)
annexe = re.sub(r'«\s+', '«' + NB, annexe)
annexe = re.sub(r'\s+»', NB + '»', annexe)
for _ in range(3):
    annexe = re.sub(r'(?<=\d)[ ](?=\d{3}\b)', NB, annexe)
annexe = re.sub(r'(?<=\d)[ ](?=[€%])', NB, annexe)

assert '<h2 class="saut">' not in s, 'le fichier porte déjà une annexe'
open(F, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n\n' + annexe)
print('annexe de relecture ajoutée à', F, '—', annexe.count(NB), 'insécables')
