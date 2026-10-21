#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute l'annexe de relecture au fichier de travail du Chapitre 9.

Annexe RÉDUITE aux points de vigilance : charte v13, section 22. L'annexe de
contrôle complète ne se produit qu'à la livraison.
"""
import re

F = 'ch09-travail.html'
s = open(F, encoding='utf-8').read()
NB = '\u00a0'
assert NB == chr(160), 'NB doit être un insécable, pas un espace ordinaire'

ROWS = [
('Volume du texte', 'SOUS LE SEUIL', """
<strong>v4 —</strong> 630 mots au périmètre déclaré, 661 avec les sous-titres. Le seuil de vigilance de la
charte, section 19, est de 680, et le chapitre reste en dessous sans avoir rien coupé.
<strong>Périmètre déclaré, mesuré par script :</strong> l'accroche et le corps. En sortent la vidéo, les
sous-titres, les blocs d'écritures, leurs légendes, le composant, l'<code>&lt;UAlert&gt;</code>, la
précision et le bloc « Ce que vous avez appris », qui pèse 97 mots à lui seul.
<strong>Ce que le chapitre délègue</strong>, ce que la section 19 demande de savoir dire : le révélateur
coût employeur porte à lui seul la démonstration des trois montants, et le bloc de paie porte le décalage
entre la charge et le décaissement. Le texte ne les redit ni l'un ni l'autre.
<strong>Point de comparaison :</strong> sept termes de lexique, autant que le Chapitre 8, pour 229 mots de
moins.""" ),

('Budget de deux-points', '0 → 0', """
<strong>Notation : premier jet → état soumis.</strong> Six sections comptées — vidéo, accroche, trois
sous-titres, bloc de clôture — et pas un deux-points en prose dans aucune.
<strong>Ce n'est pas un objectif</strong>, la charte, section 10, fixant un maximum et non une cible. C'est
la conséquence d'avoir écrit sous la règle plutôt que de la corriger après coup, et c'est le premier
chapitre du module dans ce cas.
<strong>Hors compte :</strong> aucun non plus dans les légendes de bloc.""" ),

('Écritures manuelles', '4 LIGNES', """
Un bloc unique de quatre lignes, rattaché au sous-titre du coût employeur, conformément à la fiche du
déroulé et à la ligne du Chapitre 9 au tableau de la section 4. C'est le seul chapitre du module à ne
porter qu'un bloc.
<strong>Le mécanisme que ce bloc introduit et qu'aucun bloc antérieur n'introduit</strong>, contrôle que la
section 4 du déroulé impose devant chaque bloc manuel : une charge qui se scinde en deux destinations, une
part versée tout de suite et une part due à un tiers. Aucun bloc antérieur ne fait cela.
<strong>Panneau automatique en fin de texte</strong>, comme la fiche l'indique. Le bloc de paie porte sur
les salaires et les dettes sociales, que l'écriture de période n'alimente pas, et aucun de ses quatre
montants ne se forme à partir d'un solde.""" ),

('La précision — arbitrée sans consigne', 'À VALIDER', """
Ancre «~42~% du brut~», au deuxième sous-titre. Elle porte le fait que le taux de charges patronales n'est
pas le même pour tous les salaires, l'État l'allégeant sur les rémunérations proches du salaire minimum.
<strong>Ce point demande une décision, parce que le déroulé ne l'avait pas prévu.</strong> Le recensement
de la section 6 dit seulement que les chapitres 9 à 13 poseront chacun la leur à la rédaction. La seule
entrée connue d'avance pour ce chapitre est la comparaison avec le gérant majoritaire de SARL, et
<strong>elle est disqualifiée</strong> par l'exception absolue de la charte, section 20 : une information
qui apprend au lecteur que le chapitre ne s'applique pas à lui n'est jamais une précision. Elle reste donc
au registre, comme la franchise en base au Chapitre 5.
<strong>Pourquoi celle-ci passe le test :</strong> le mécanisme du chapitre vaut à l'identique quel que
soit le taux, seul le montant change. C'est une variante, pas une disqualification.
<strong>Ce qu'elle coûte au corps : rien.</strong> Le corollaire de la charte, section 18, ne se paie que
sur un nombre venu du décor, et 42~% est un nombre que le chapitre démontre — les 924~€ de Léa en sortent
et entrent dans le bloc.
<strong>Aucun chiffre n'est écrit dans la note</strong>, volontairement. Le détail du calcul des
allègements est du droit social qui bouge d'une loi de finances à l'autre, et une note chiffrée
vieillirait mal. La note donne le sens de la variation, pas son barème.""" ),

('Le régime social des dirigeants', 'CONFORME À LA FICHE', """
Traité au troisième sous-titre, en quatre paragraphes, sur exactement la substance que la fiche impose :
régime général et assimilé salarié, même mécanique que le bulletin de Léa, pas d'assurance chômage, et la
distinction entre être associé et être rémunéré.
<strong>La promesse du Chapitre 2 est honorée</strong>, comme la fiche le demande.
<strong>Ce que le chapitre écarte, et qui part au registre :</strong> la comparaison avec le gérant
majoritaire de SARL, travailleur non salarié. La fiche l'interdit explicitement — question de choix de
forme juridique, pas de comptabilité — et le critère 3 du tri du Chapitre 13 l'enverra probablement en
module ultérieur.
<strong>L'annonce du dividende dit pourquoi elle attend</strong>, la charte, section 7, l'exigeant : il
faut un résultat à partager, et il ne se sait qu'une fois l'année finie. Le mot « clôture » n'est pas
employé, il appartient au Chapitre 10.""" ),

('Rejeu du journal', 'FAIT — AUCUN ÉCART', """
Toutes les phrases du chapitre qui décrivent un mouvement dans la grille ont été rejouées par script, bloc
par bloc, depuis la première écriture du Chapitre 2.
<strong>Vérifiés au centime :</strong> le compte en banque descend bien de 61~371,10~€ à 52~635,10~€ au
passage du bloc de paie, et remonte bien à 70~635,10~€ après l'écriture de période ; le total des charges
monte bien de 84~687,50~€ à 100~591,50~€ ; la ligne Dettes sociales s'ouvre bien à 7~168~€. Le
61~371,10~€ de l'accroche est bien ce que la grille affiche au moment où le lecteur la lit.
<strong>Arithmétique du bloc, refaite :</strong> 9~000~€ pour Thomas et Claire sur trois mois, 2~200~€
pour Léa en septembre, soit 11~200~€ de brut ; 22~% retenus font 2~464~€ et 8~736~€ de nets ; 42~% à la
charge de l'employeur font 4~704~€ ; les cotisations dues totalisent 7~168~€. Le bloc s'équilibre à
15~904~€.
<strong>Total de contrôle du module au terme du Chapitre 9 : 554~232,90~€</strong> au débit comme au
crédit.
<strong>Ce que les scripts n'avaient jamais vu :</strong> rien de nouveau dans ce chapitre. Les comptes à
trois chiffres, les quatre chiffres et les centimes leur avaient déjà été présentés.""" ),

('Ce que le chapitre n\'inscrit pas', 'DÉCISION DEMANDÉE — VOIR CHAPITRE 10', """
Le bloc de paie ne porte que le troisième trimestre, comme la fiche le prévoit. <strong>Les rémunérations
du quatrième trimestre ne sont inscrites nulle part</strong>, ni ici, ni à la fiche du Chapitre 10, ni à
celle du Chapitre 11.
<strong>Ce que cela représente : 15~600~€ de brut et 6~552~€ de charges patronales.</strong> Le
scénario chiffré du déroulé, section 3, attend 26~800~€ de salaires bruts et 11~256~€ de charges
patronales sur l'exercice ; la grille en portera 11~200~€ et 4~704~€ au terme du Chapitre 10.
<strong>Le point est traité en entier à l'annexe du Chapitre 10</strong>, avec la troisième ligne manquante
et les voies possibles. Il est signalé ici parce que c'est ce chapitre qui ouvre les deux comptes
concernés.""" ),

('Relecture profane — deux tours', 'FAITE — 2 CORRECTIONS', """
<strong>Pascal, 24~août 2026.</strong> Une seule correction sur tout le chapitre.
<strong>Accroche, «~et~» devient «~mais~» :</strong> «~Ce montant est le seul que le contrat porte, mais
il n'est ni celui que Léa recevra, ni celui que l'entreprise paiera.~» La coordination neutre juxtaposait
deux faits ; l'opposition est la tension même de l'accroche, et le signe qui la porte doit la dire. Zéro
mot de coût.
<strong>Ce n'est pas une famille nouvelle</strong> au sens de la charte, section 12 : c'est une faiblesse
de liaison, pas une tournure de métier déguisée. À consigner au journal, table des relectures profanes,
sans remontée à la charte.
<strong>Le reste du chapitre est passé sans remarque</strong>, y compris le sous-titre du régime social
des dirigeants, qui était le passage le plus exposé.
<strong>Second tour — «~bloc~» est un mot de fabricant, comme «~la grille~».</strong> La correction est
venue du Chapitre 10 et s'applique ici sans que Pascal l'ait demandé pour ce chapitre~: le mot désigne en
interne une suite d'écritures, et il n'a jamais été présenté à l'apprenant. Trois occurrences corrigées en
«~bloc d'écritures~», une au corps et deux aux légendes. Coût~: un mot.
<strong>Une quatrième occurrence a été traitée autrement.</strong> La légende du composant disait
«~en trois blocs~», au sens des trois parts du brut, et non au sens d'une suite d'écritures. Deux sens du
même mot dans le même chapitre valent pire qu'un mot obscur~: la légende dit désormais «~en trois parts~».
Le libellé vient de la fiche du déroulé, section 7, qui est à corriger avec elle.""" ),

('Checklist de relecture', 'QUARANTE CASES — AUCUNE EN DÉFAUT', """
Charte, section 21. <strong>Vingt-quatre cases sont passées par script</strong>, le reste à la lecture.
<strong>Ce que le script vérifie et qui est vert :</strong> aucun mot de la liste des interdits ;
«~toucher~» absent ; au plus un tiret cadratin en prose, et il y en a zéro ; la glose (emploi) et
(ressource) une fois chacune et pas davantage ; une seule déclaration en gras, sans terme de lexique
dedans ; chaque terme du lexique coloré une seule fois, aucun coloré dans un titre ; une précision au plus,
son ancre hors lexique, sa note présente et son <code>aria-describedby</code> résolu ; Bilan et Compte de
Résultat jamais en minuscules ; toutes les sommes avec leurs insécables et leur unité ; le plafond de huit
lignes manuelles ; un <code>&lt;UAlert&gt;</code> au plus, après le dernier sous-titre ; deux à trois
sous-titres et aucun niveau 3 ; un seul nom propre de personne à l'accroche ; le bloc de clôture à trois
points. <strong>Et les deux cases nées de la relecture du 25~août :</strong> «~bloc~» ne s'emploie jamais
nu, «~la grille~» est absente.
<strong>Deux défauts du script lui-même ont été trouvés en l'écrivant</strong>, et ils suivent la loi
connue — un script ne se trompe que sur ce qu'aucun chapitre antérieur ne lui avait présenté. Le contrôle
d'unité levait sur le dernier caractère du chapeau de rubrique, une chaîne vide étant sous-chaîne de
n'importe quoi en Python. Et le compte des noms propres de l'accroche comptait les occurrences là où la
charte compte les personnes~: deux mentions de la même personne ne font qu'un nom.
<strong>Les cases de jugement, vérifiées à la lecture</strong>, sont détaillées aux lignes ci-dessus~:
volume, budget de deux-points, rattachement des blocs d'écritures, place du panneau, précision, renvois aux
chapitres antérieurs, refrain, relecture profane. <strong>La quarantième case</strong>, celle que le
rédacteur ne peut pas cocher seul, est cochée par les deux tours de Pascal.""" ),

('Production du fichier', 'CONFORME', """
Fichier produit sous la charte, section 22. <strong>Le fichier de livraison ne porte que ce qui s'affichera
à l'apprenant</strong>~: le chapo de version et cette annexe en sortent, et vivent au PDF de livraison.
Les deux fichiers portent le même texte, au caractère près, contrôlé par le script de livraison sur le
source dépouillé de ses balises par expression régulière — jamais par un parseur, qui avalerait le contenu
d'un <code>&lt;template&gt;</code>.
La précision est écrite en dur, et l'<code>&lt;UAlert&gt;</code> est converti depuis la classe
<code>.alert</code> du fichier de travail. <strong>Le PDF de livraison revient au pointillé sur l'ancre</strong>,
qui est la forme réelle~; les PDF de relecture la portaient en souligné plein.
<strong>Le fichier n'a été produit qu'après la validation de Pascal</strong>, la charte interdisant au
rédacteur de le produire de sa propre initiative~: son existence est la preuve que la relecture a eu lieu.""" ),

('Répercussion différée', 'CE QUE LA PASSE GROUPÉE DEVRA RECEVOIR', """
La répercussion ne se fait plus chapitre par chapitre depuis le 24~août 2026.
<strong>Au registre des écarts :</strong> ouvrir la section du Chapitre 9 et y porter l'entrée connue
d'avance, la comparaison avec le gérant majoritaire de SARL, avec sa formulation rédigée. Trois autres
entrées sont à écrire — le détail du calcul des allègements de cotisations patronales, l'absence de
treizième mois et de primes dans le scénario, et les cotisations dues par les dirigeants au titre des
mandats sans rémunération. Le compte du registre passera de 42 à 46 entrées, à recompter par script.
<strong>Au déroulé, section 6 :</strong> ajouter la ligne du Chapitre 9 au recensement des précisions,
ancre «~42~% du brut~», et la mention <strong>Écrite.</strong>
<strong>Au déroulé, section 13 :</strong> créer la ligne du Chapitre 9 à l'ordre de rédaction, 629 mots.
<strong>Au journal de rédaction :</strong> la déclaration en gras du Chapitre 9 est un comparatif — «~le
coût d'un salarié est toujours plus élevé que la rémunération qu'il perçoit~» — forme neuve dans le module,
huitième employée sur treize chapitres. À porter à la table des déclarations.
<strong>Au déroulé, section 7 :</strong> la ligne du Chapitre 9 aux activités dit «~le brut se décompose
en trois blocs~». À écrire «~en trois parts~», pour la même raison que ci-dessus.
<strong>À la charte : rien.</strong> Aucune règle n'a manqué à ce chapitre.""" ),
]

TETE = """<h2 class="saut">Annexe de contrôle</h2>
<p>Annexe complète, produite à la livraison : elle recense tout ce qui a été vérifié, et c'est elle qui
permet de revérifier la checklist un chapitre plus tard. Les premières lignes portent ce qui a été arbitré
sans consigne, ce qui s'écarte d'une fiche du déroulé et ce qui demande une décision ; les dernières
portent les contrôles. Charte, section 22.</p>
<table>
<thead><tr><th>Point</th><th>État</th><th>Détail</th></tr></thead>
<tbody>
"""

corps = ''.join(
    f'<tr><td class="cle">{cle}</td><td>{etat}</td><td>' + ' '.join(detail.split()) + '</td></tr>\n'
    for cle, etat, detail in ROWS).replace('~', NB)

annexe = TETE + corps + '</tbody>\n</table>\n'

# ─── insécables de l'annexe : guillemets et sommes (piège 3 du LISEZ-MOI) ────
annexe = re.sub(r'«\s+', '«' + NB, annexe)
annexe = re.sub(r'\s+»', NB + '»', annexe)
for _ in range(3):
    annexe = re.sub(r'(?<=\d)[ ](?=\d{3}\b)', NB, annexe)
annexe = re.sub(r'(?<=\d)[ ](?=[€%])', NB, annexe)

assert '<h2 class="saut">' not in s, 'le fichier porte déjà une annexe'
open(F, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n\n' + annexe)
print('annexe de relecture ajoutée à', F, '—', annexe.count(NB), 'insécables')
