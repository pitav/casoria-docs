#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute l'annexe au fichier de travail du Chapitre 12.

Sans argument : annexe RÉDUITE aux points de vigilance (charte v14, section 22).
Avec « complete » : annexe de contrôle, produite à la livraison seulement.
"""
import re
import sys

F = 'ch12-travail.html'
s = open(F, encoding='utf-8').read()
NB = ' '
assert NB == chr(160), 'NB doit être un insécable, pas un espace ordinaire'

ROWS = [

('Relecture profane, tour 1', 'VINGT CORRECTIONS — TOUTES APPLIQUÉES', """
<strong>Vingt corrections de Pascal, toutes appliquées.</strong> C'est le tour de relecture le plus lourd
du module en volume, et il a coûté 165 mots.
<strong>Sept portent sur la même chose et forment le vrai enseignement du chapitre~: la densité de notions
neuves y dépasse ce qu'un profane absorbe sans explication.</strong> «~L'autonomie financière rapporte les
capitaux propres au total du Bilan~» était exacte et illisible. Le mot «~ratio~» était employé sans qu'on
dise jamais ce que l'opération fait ni à quoi elle sert. Les deux pourcentages étaient calculés sans qu'on
dise ce qu'ils signifient. Chacun de ces points est désormais écrit, et c'est de là que vient l'essentiel
du volume ajouté.
<strong>Quatre corrections portent sur un mot pris pour un autre.</strong> «~nombres~» devient
«~chiffres~» ou «~sommes~» partout où il désignait des montants. «~rapports~» quittait le sous-titre 3,
Pascal l'ayant lu comme des rapports écrits. «~torréfacteurs~» quitte le corps, le mot désignant à la fois
le métier et la machine du Chapitre 8. «~rapporte~» et «~compte~» deviennent «~décrit~» et «~regarde~».
<strong>Trois portent sur une référence qui ne se rattache à rien.</strong> «~La réponse est non~»
répondait à une question que l'accroche ne posait pas — elle la pose maintenant, et le corps y répond par
une phrase entière. «~Ceux de Latitude Café~» ne renvoyait à rien de nommé. «~Trois manières de le
réduire~» ne disait pas quoi.
<strong>Une porte sur un titre qui mélangeait deux choses</strong>, «~ce que l'entreprise a gagné~» et le
compte en banque~; il oppose désormais le bénéfice et l'argent disponible.
<strong>Une porte sur une image trop étroite</strong>~: «~le café~» devient «~le stock~» au sous-titre 2
et partout ailleurs, pour que le lecteur transpose à son propre métier.
<strong>Et une entre au déroulé.</strong> Le sigle BFR accompagne désormais le besoin en fonds de
roulement, ligne ci-dessous.
<strong>Deux mots de fabrication ont été trouvés en réparant les autres, et par script.</strong>
«~exploitation~» et «~poste~» n'apparaissent dans aucun des onze chapitres livrés, et le déroulé les
emploie partout~; la v1 les avait laissés passer trois fois. Ils sont remplacés par «~activité~» et
«~ligne~», que le lecteur a déjà lus. <strong>Le contrôle est reproductible et vaut pour les chapitres à
venir~:</strong> un mot que le déroulé emploie et qu'aucun chapitre livré ne porte est un candidat au
vocabulaire de fabrication (charte, section 12). Troisième famille attestée après «~la grille~» et
«~bloc~», et la première trouvée sans relecteur.""" ),

('Volume du texte, et la question du découpage', 'DÉPASSEMENT MOTIVÉ — 833', """
<strong>833 mots au périmètre déclaré, 865 avec les sous-titres</strong>, pour un seuil de vigilance de 680
(charte, section 19). <strong>La v1 en faisait 668 et le tour de relecture a ajouté 165 mots.</strong>
<strong>Motif du dépassement, en une phrase, comme la section 19 l'exige~:</strong> le chapitre porte
quatre termes de lexique neufs et trois outils de lecture qu'aucun schéma ni aucun geste ne peut définir à
la place du texte, et la relecture profane a montré que les définir coûte des mots qu'il n'y a nulle part
où prendre.
<strong>Il reste le deuxième chapitre du module, pas le premier.</strong> Le Chapitre 8 en fait 858 au même
périmètre.
<strong>Pascal demande s'il faut le couper en deux.</strong> La charte, section 19, fixe le seuil où le
découpage du module est en cause à «~environ 900 mots~», et ce chapitre est en dessous. <strong>Il n'est
donc pas encore un problème de découpage</strong>, et la réponse par défaut est de le laisser entier.
<strong>La coupure existe pourtant, et elle est propre</strong>~: le sous-titre 3 est d'une autre nature
que les deux premiers. Les deux premiers tranchent une décision, le troisième apprend à lire. Un Chapitre
12 «~La décision~» de 480 mots et un Chapitre 13 «~Lire ses comptes~» de 350 se tiendraient.
<strong>Ce que la coupure coûterait~:</strong> un chapitre de plus, donc treize qui deviennent quatorze, et
une reprise du déroulé aux sections 5, 7, 8, 9, 10, 11 et 13 — vue d'ensemble, durées de la séance 4,
calibrage des quiz, composants et activités. <strong>Ce n'est pas une décision de rédaction.</strong>
<strong>Périmètre déclaré, mesuré par script~:</strong> l'accroche et le corps. En sortent la vidéo, les
sous-titres, la légende du composant, la légende d'illustration, la précision et le bloc «~Ce que vous avez
appris~», qui pèse 95 mots.""" ),

('Budget de deux-points', '0 → 2', """
<strong>Notation~: v1 → état soumis.</strong> Six sections comptées, deux deux-points en prose, un par
section, <strong>le budget étant d'un par section et non d'un par chapitre</strong> (charte, section 10).
<strong>Le premier est demandé par Pascal</strong>, au sous-titre 2~: «~porte un nom, le BFR~: le besoin en
fonds de roulement~». C'est une explicitation, l'emploi que le tableau de la section 10 lui reconnaît.
<strong>Le second est de la même famille</strong>, au sous-titre 3~: «~son intérêt est là~: un pourcentage
se compare d'une année sur l'autre~». Il annonce ce qui répond à la question que la phrase précédente
laisse ouverte.
<strong>Hors compte~:</strong> un dans la légende d'illustration, le «~Légende~:~» que le gabarit impose.
<strong>Le titre du chapitre en porte un</strong>, celui du déroulé. Il n'entre pas au budget, qui ne
compte que la prose du corps.""" ),

('Le sigle BFR', 'DEMANDÉ — INVERSE LE PATRON', """
<strong>Écrit comme Pascal le demande~: «~porte un nom, le BFR~: le besoin en fonds de roulement~».</strong>
<strong>Cela inverse le patron du module.</strong> La SAS au Chapitre 2 et l'IS au Chapitre 11 donnent le
nom complet d'abord et le sigle entre parenthèses. Ici le sigle vient en premier et le nom le développe.
<strong>L'inversion se défend, et c'est probablement elle qui a raison ici~:</strong> BFR est un sigle que
le lecteur rencontrera avant le nom complet, chez son banquier comme chez son expert-comptable, alors que
personne ne dit «~IS~» avant d'avoir dit «~impôt~». Le sigle est ce qu'il faut reconnaître, le nom est ce
qui l'explique.
<strong>Il n'entre pas en conflit avec la vigilance sur les sigles</strong> (déroulé, section 12)~: elle
proscrit «~CCA~» et «~PCA~» parce que ce seraient des conventions maison. BFR se lit sur des documents
réels, comme SAS, TVA et IS.
<strong>Rechange, si le patron doit primer~:</strong> «~porte un nom, le besoin en fonds de roulement
(BFR)~», qui coûte le deux-points que Pascal vient d'accorder.
<strong>À porter au lexique cumulatif du déroulé, section 11</strong>, sur le patron de l'IS~: la ligne
«~Besoin en fonds de roulement~» reçoit la mention du sigle et de son ordre d'apparition.""" ),

('Le titre, et le mot «~ratio~»', 'TRANCHÉ À LA LIVRAISON — RECHANGES ÉCRITES', """
<strong>Le titre retenu est celui du déroulé, amputé du chiffre~: «~Piloter~: la décision et les trois
ratios~».</strong> La forme en lettres est celle de l'annexe A de la charte.
<strong>Il annonce trois ratios, et l'un des trois n'en est pas un.</strong> Le besoin en fonds de
roulement est une somme en euros, pas une division — et le corps le dit maintenant en toutes lettres, «~le
besoin en fonds de roulement est une somme~», puis définit le ratio comme une division qui donne un
pourcentage.
<strong>Le sous-titre 3 dit désormais «~deux ratios~» et non «~deux rapports~»</strong>, Pascal ayant lu
«~rapports~» comme des rapports écrits. La distinction entre la somme et les deux ratios est donc portée
par le corps, et le titre du chapitre est le seul endroit qui la contredise encore.
<strong>Deux rechanges, si le point est retenu~:</strong> «~Piloter~: une décision et trois chiffres~», qui
ne qualifie plus~; ou «~Piloter~: lire ses comptes pour décider~», plus proche du registre des autres
titres. Le bloc «~Ce que vous avez appris~» écrit déjà «~deux ratios~» et non trois.
<strong>Tranché à la livraison du 26~août 2026~: le titre du déroulé est conservé.</strong> Le motif est
que le corps porte désormais la distinction en toutes lettres, ce qui était le vrai risque~; un titre qui
regroupe trois outils sous un mot d'usage courant ne trompe plus personne une fois le premier paragraphe du
sous-titre 3 lu. Les deux rechanges ci-dessus restent écrites, et le point se rouvre sans coût si les tests
utilisateurs le rendent nécessaire.""" ),

('L\'achat à crédit, la question que le lecteur va poser', 'TRANCHÉ À LA LIVRAISON — NON APPLIQUÉ', """
<strong>Le chapitre répond non parce que l'argent n'est pas là. Il ne dit pas un mot d'un second
emprunt.</strong> Or l'entreprise en a obtenu un au Chapitre 7 pour financer la première machine, et un
lecteur qui vient de lire ce chapitre-là posera la question dans la seconde qui suit.
<strong>La réponse du chapitre reste juste</strong>~: la question posée est celle de la trésorerie
disponible, et 43~200~€ ne sortent pas d'un compte qui en porte 17~310~€. Emprunter est une autre décision,
qui suppose de savoir ce que l'entreprise peut rembourser — précisément ce que l'aside «~Œil du banquier~»
du Chapitre 11 annonce et que la formation dédiée au pilotage traite.
<strong>L'ajout se chiffre et se gage, comme la charte, section 19, l'impose.</strong> Une phrase de
dix-huit mots à la fin du premier sous-titre~: «~Emprunter à nouveau est une autre question, et elle se
pose une fois celle-ci tranchée.~»
<strong>Le gage a changé depuis la v1.</strong> Le chapitre étant maintenant à 833 mots, l'ajout ne se paie
plus sur la marge au seuil~: il faudrait couper les vingt mots de teasing du dernier paragraphe, qui disent
déjà la même chose autrement.
<strong>Tranché à la livraison du 26~août 2026~: la phrase n'est pas ajoutée.</strong> Deux motifs. Le
chapitre est à 833 mots et le gage porterait sur les vingt mots de teasing, qui font le lien avec la
formation suivante et que la fiche impose. Et l'entrée 12.4 du registre porte déjà la matière — les
financements de court terme, en module ultérieur — ce qui est la destination juste pour une question qui
appelle un chapitre entier et non une phrase.
<strong>À rouvrir si la relecture externe du module la fait remonter</strong>, la phrase étant écrite
ci-dessus et son gage identifié.""" ),

('Aucun <code>&lt;UAlert&gt;</code>, et la simplification qui reste', 'TRANCHÉ À LA LIVRAISON — CONFORME', """
<strong>Le recensement du déroulé, section 6, ne prévoit pas d'alerte pour ce chapitre</strong>, et le
déroulé l'emporte sur la checklist (charte, section 18). Aucune n'est ajoutée.
<strong>Une simplification existe pourtant, et elle est dite en une phrase du corps</strong>, comme la
charte l'exige dans ce cas~: «~le calcul du chapitre ne retient que ces trois postes de l'exploitation
courante, alors qu'un banquier en regarde quelques autres~». Le besoin en fonds de roulement réel ajoute
les dettes sociales, les deux comptes de taxe et les charges et produits constatés d'avance, tous présents
au Bilan du module.
<strong>Ce que la simplification coûte, chiffré~:</strong> le besoin en fonds de roulement complet vaudrait
sensiblement moins que 69~000~€, les postes omis étant tous au Passif. <strong>Le chiffre exact n'est pas
écrit</strong>, ni au corps ni ici comme valeur à retenir, parce que la formule qui le produit varie d'un
analyste à l'autre et qu'il n'y a pas de version unique à enseigner.
<strong>Tranché à la livraison du 26~août 2026~: la phrase du corps reste seule.</strong> Le déroulé,
maître du fond, n'a pas recensé d'alerte ici, et une alerte ajoutée par le rédacteur contre le recensement
est exactement ce que la charte, section 18, lui interdit. L'entrée 12.2 du registre porte la formulation
complète, avec les quatre lignes du Bilan que le calcul omet.
<strong>Se rouvre par le déroulé, pas par le chapitre</strong>~: si l'alerte est décidée, elle entre au
recensement de la section 6 et le chapitre la reçoit à sa forme imposée.""" ),

('La piste N et N–1 de la fiche', 'TRANCHÉE AVANT RÉDACTION', """
<strong>La fiche du Chapitre 12 ouvrait une piste et interdisait de la découvrir au Chapitre 13.</strong>
Un vrai Bilan porte deux colonnes, l'exercice qui se termine et le précédent~; celui du module n'en porte
qu'une, et c'est l'entrée 1.5 du registre.
<strong>Tranchée avec Pascal avant d'écrire une ligne~: elle devient la précision de ce chapitre.</strong>
<strong>Les deux autres voies ont été pesées.</strong> Laisser 1.5 candidate à l'aside final revenait à
faire exactement ce que la fiche voulait éviter. En faire une matière du corps supposait d'inventer une
colonne de chiffres pour un exercice antérieur que Latitude Café n'a pas, hors du scénario verrouillé de la
section 3.
<strong>Ce que la voie retenue coûte~:</strong> rien au corps. L'ancre est une réserve que le texte posait
déjà, et le corollaire de la charte, section 18, ne se paie que sur un nombre venu du décor.
<strong>Ce qu'elle rapporte~:</strong> l'écart cesse d'en être un à l'endroit exact où le lecteur lit un
Bilan pour décider, et les entrées 1.3 et 1.6, qui sont sur le même terrain, restent seules à arbitrer au
Chapitre 13.""" ),

('La précision', 'NEUVE — ANCRÉE SUR «~TOUT SEUL~»', """
<strong>Ancre~: «~tout seul~», au troisième sous-titre</strong>, sur la réserve que le corps pose en
écrivant qu'un ratio ne dit rien seul. <strong>Quatrième fois du module que l'ancre est une réserve du
corps</strong>, après «~le plus souvent~» au Chapitre 7, «~probable~» au Chapitre 10 et «~perte~» au
Chapitre 11. Le patron annoncé au Chapitre 11 comme premier endroit où chercher a donc tenu au premier
essai suivant.
<strong>Elle vient de l'entrée 1.5 du registre, qui sort par le haut</strong> — première fois du module
qu'une entrée remonte dans un autre chapitre que celui qui l'a produite.
<strong>Le test de la charte, section 20~:</strong> une phrase et un repère dans un champ restreint, donc
elle remonte. Le lecteur peut l'ignorer sans que la suite devienne fausse, et elle n'explique l'origine
d'aucun nombre du corps. <strong>L'exception absolue a été vérifiée et écartée</strong>~: la note n'apprend
à personne que le chapitre ne le concerne pas.
<strong>Elle est placée là où le lecteur a la chose sous les yeux</strong>, au moment où il vient de lire
deux pourcentages, et non au Chapitre 1 où il regardait une grille vierge.""" ),

('L\'illustration et la famille du chapitre', 'ÉCART À LA FICHE — DÉCISION', """
<strong>La section 14 du déroulé range le Chapitre 12 dans les méthodes</strong> et laisse sa légende à
trancher en l'écrivant. <strong>Il y reste.</strong> Sa thèse n'est pas qu'une chose se lit deux fois,
c'est qu'un même Bilan répond à trois questions différentes selon la manière dont on l'interroge.
<strong>Le test des axes passe.</strong> Le composant travaille sur les leviers, de combien faudrait-il
bouger le stock, les créances ou le délai fournisseur. L'illustration travaille sur la taille~: où l'argent
se trouve au 31~décembre, et combien chaque poste pèse par rapport aux autres. Le premier fait bouger, la
seconde fait comparer.
<strong>La fiche ne prévoyait pas d'illustration</strong>, et celle-ci est un ajout de la rédaction. Le
motif est que la thèse du chapitre est une affaire de proportions, 63~000~€ contre 17~310~€, et qu'une
proportion se montre mieux qu'elle ne se décrit. <strong>Elle ne rejoint pas pour autant la famille des
dualités</strong>~: elle ne montre pas une chose lue à deux endroits, elle met quatre postes du Bilan à la
même échelle.
<strong>Sa légende dit «~stock~» et non «~café en stock~»</strong>, comme le corps, depuis la correction de
Pascal. <strong>Elle porte cinq sommes, toutes déjà écrites au corps</strong>, et toutes vérifiées par
script.""" ),

('Le composant et ce que sa légende promet', 'POINT DE VIGILANCE', """
<strong><code>&lt;SimulateurBfr /&gt;</code>, pris à la table de nommage du déroulé, section 5.</strong>
Placé en fin de sous-titre 2, après la déclaration et avant le paragraphe qui nomme les trois leviers~:
l'activité prépare, le texte commente (charte, section 14).
<strong>Sa légende promet trois curseurs et un objectif</strong>, «~chercher ce qui financerait la
machine~». <strong>C'est une promesse sur un écran qui n'existe pas encore</strong>, et c'est le seul
endroit du chapitre où le texte engage le produit. La fiche du déroulé dit la même chose.
<strong>Le mot «~encours~» de la fiche n'est pas repris.</strong> Il n'a jamais été présenté à
l'apprenant, et «~créances clients~» dit la même chose avec le mot du Chapitre 4.
<strong>Aucune légende ne demande de regarder un total bouger pendant qu'une ligne s'inscrit</strong>
(charte, section 16)~: le chapitre ne passe aucune écriture, la case est sans objet.""" ),

('Le dosage narratif', 'AU-DESSUS — ASSUMÉ', """
<strong>Cinq occurrences de «~Latitude Café~» dans le corps, pour trois ou quatre prescrites</strong> par
la règle de dosage du déroulé, section 1.
<strong>La règle attache le fil rouge à l'accroche puis à chaque bloc d'écritures.</strong> Ce chapitre n'en
a aucun, et il n'a pas non plus de notion générale à exposer~: chacun de ses paragraphes lit un chiffre du
Bilan de cette entreprise-là. Le nom revient donc à chaque chiffrage, ce que la règle demande, sans le
point d'ancrage qu'elle prévoyait.
<strong>Le tour de relecture n'a pas fait bouger ce compte</strong>, la correction sur «~Ceux de Latitude
Café~» ayant supprimé un pronom et non le nom.""" ),

('Le refrain', 'REPRIS — FORME SÈCHE', """
<strong>Le déroulé prévoit une reprise du refrain ici</strong>, après les Chapitres 4, 5, 7 et 10.
<strong>Elle est au troisième paragraphe</strong>, «~deux chiffres disent donc deux choses différentes~»,
suivie du renvoi au Chapitre 4.
<strong>La correction de Pascal l'a rendue vérifiable.</strong> La v1 écrivait «~deux nombres exacts~» sans
dire lesquels, après un paragraphe qui en portait cinq. Les deux chiffres sont maintenant nommés et
chiffrés, 27~200~€ et 17~310~€, chacun avec le document qui le porte.
<strong>La forme reste sèche, comme le déroulé l'autorise</strong> depuis que l'encadrement du Chapitre 4
est posé. <strong>Le renvoi au Chapitre 4 porte la substance et le nom</strong> (charte, section 12)~: la
facture de 1~450~€, le compte qui ne bouge pas, et le mot «~créance client~».""" ),

('Déclaration en gras', 'DOUZIÈME FORME', """
<strong>«~Ces 69~000~€, l'entreprise ne les a pas perdus, elle les a rangés dans son stock et dans les
factures que ses clients n'ont pas encore payées.~»</strong>
<strong>C'est une mise en relief par détachement</strong>, avec reprise pronominale. Elle ne ressemble ni à
celle du Chapitre 11, une subordonnée causale, ni à celle du Chapitre 10, une hypothétique à sujet
infinitif. La règle ne vise que le voisinage (charte, section 9).
<strong>«~son café en stock~» est devenu «~son stock~»</strong> à la relecture, pour la même raison que le
sous-titre~: l'image doit se transposer à un autre métier que celui du fil rouge.
<strong>À consigner au journal de rédaction</strong>, qui tient la liste des formes déjà employées.""" ),

('Les deux points ouverts de la section 14', 'TOUCHENT CE CHAPITRE — ÉTAT', """
<strong>Les 808~€ de TVA versée.</strong> Le déroulé note qu'aucune combinaison de versements ne laisse
4~400~€ dus au 31~décembre, et que ces 4~400~€ portent le total du Bilan, donc les ratios de ce
chapitre. <strong>Le chapitre les écrit deux fois</strong>, à la ligne de TVA à décaisser et dans les
9~200~€ dus à l'État. <strong>Rien n'est à changer si la voie la moins chère est retenue</strong> — tenir
les 808~€ pour un paramètre du scénario et l'écrire à la section 3. Refaire le calendrier des versements
déplacerait les 4~400~€, donc les 130~410~€, donc l'autonomie financière.
<strong>Les trente centimes de l'échéancier.</strong> Sans effet ici~: ils portent sur l'emprunt et la
trésorerie, dont ce chapitre lit les valeurs arrondies de la section 3. La réparation proposée — écrire
l'arrondi à la section 3 — ne touche aucun chiffre de ce texte.""" ),

('Registre des écarts', 'CINQ ENTRÉES NEUVES, ET UNE SORTIE', """
<strong>12.1 les autres outils de lecture</strong> — rentabilité des capitaux, rotation du stock, capacité
de remboursement~; silencieuse, candidate.
<strong>12.2 le besoin en fonds de roulement réduit à trois postes</strong>, signalée en une phrase du
corps.
<strong>12.3 le fonds de roulement et la trésorerie nette</strong> — comment le besoin est financé~;
silencieuse, candidate.
<strong>12.4 les financements de court terme</strong> — découvert autorisé, escompte, affacturage~;
silencieuse, en module ultérieur.
<strong>12.5 les repères sectoriels</strong> — le corps dit de comparer à d'autres entreprises de la même
taille sans dire où l'on trouve ces repères~; signalée, candidate.
<strong>Et l'entrée 1.5 du Chapitre 1 sort par le haut, dans ce chapitre-ci.</strong> C'est le premier cas
du module, et il produit une règle que le registre porte désormais~: <strong>une entrée peut remonter dans
un autre chapitre que celui qui l'a produite</strong>, parce que la note ne vaut que là où le lecteur a la
chose sous les yeux. Corollaire~: une entrée refusée comme précision de son propre chapitre n'est pas
condamnée à l'aside, elle attend le chapitre où son ancre existe.
<strong>Le registre passe de 57 à 62 entrées</strong>, recomptées par script, et les onze sorties par le
haut sont listées.
<strong>Un quatorzième nombre annoncé a été pris en défaut au passage.</strong> Le décompte de fin du
registre annonçait cinquante-quatre candidates et deux remontées en précision quand le fichier en portait
déjà dix. Le total tombait juste, ce qui est ce qui l'a rendu invisible. Les trois sous-totaux se
recomptent désormais par script, à la même passe que le total.
<strong>Le tour de relecture n'a pas produit d'entrée neuve</strong>, ses vingt corrections portant toutes
sur la lisibilité et non sur un contenu écarté.""" ),

('Les outils', 'UN SCRIPT NEUF, UN DÉFAUT TROUVÉ', """
<strong><code>outils/verif_ratios.py</code></strong> reconstruit le Bilan et le Compte de Résultat depuis
les panneaux des onze chapitres, recalcule les trois outils de lecture et la décision, puis
<strong>confronte une à une toutes les sommes et tous les pourcentages du texte</strong> à ce
recalcul. Il ne porte aucun nombre en dur venu d'un document~: le prix de la machine se déduit du
torréfacteur du Chapitre 8 par le taux de taxe du module, et le seul paramètre écrit est ce taux.
<strong>Il a servi~:</strong> les 1~450~€ du renvoi au Chapitre 4 sont ressortis comme la seule somme non
reconstructible depuis le Bilan de clôture, et le script la retrouve sur une ligne d'écriture des
Chapitres 4 et 5. C'est ce que le contrôle devait faire. <strong>Il a été relancé après les vingt
corrections</strong>, et rien n'a bougé.
<strong><code>controle_checklist.py</code> a levé à tort</strong> sur la glose (emploi) et (ressource),
qu'il exigeait une fois chacune. <strong>Le Chapitre 12 est le premier du module sans aucune
écriture</strong>, donc sans première occurrence à gloser~: la case est sans objet, pas en défaut. C'est la
loi des défauts d'outil — un script ne se trompe que sur ce qu'aucun chapitre antérieur ne lui avait
présenté. Corrigé, la case se déclare sans objet quand le chapitre ne porte aucune ligne d'écriture.
<strong><code>rejeu.py</code> et <code>verif_cloture.py</code> sont inchangés</strong>, ce chapitre
n'ajoutant aucune ligne. Le total de contrôle du module reste 1~294~694,00~€ au débit comme au crédit.""" ),

('Ce qui reste à faire', 'AVANT LIVRAISON', """
<strong>Rien avant la livraison. Le chapitre est livré le 26~août 2026</strong>, un tour de relecture
profane passé, vingt corrections appliquées, et les trois points laissés ouverts tranchés en faveur du
texte, chacun à sa ligne ci-dessus avec sa rechange.
<strong>Répercussions passées le même jour</strong>~: registre des écarts (cinq entrées et la sortie de
1.5)~; déroulé v22 → v23, sections 6 (la précision, ancre «~tout seul~»), 10 (la fiche reçoit ses
arbitrages et la piste N et N–1 se ferme), 11 (le sigle BFR au lexique, et la définition de «~ratio~»
alignée sur celle du corps), 12 (trois vigilances de vocabulaire neuves), 13 (la ligne du Chapitre 12) et
14 (l'illustration du Chapitre 12)~; journal de rédaction (la douzième forme de déclaration, l'illustration,
et les vingt corrections à la table «~Relectures profanes~»).
<strong>À la charte~: rien.</strong> Deux candidats à une seule attestation partent au journal, où vivent
déjà les six autres. <strong>Le premier est le plus sérieux~:</strong> définir un terme ne suffit pas à
l'introduire, il faut dire ce que l'opération fait et à quoi elle sert — sept corrections de ce tour en
relèvent, mais toutes sur le même chapitre, et la charte grossit par attestation et jamais par soupçon.
<strong>Le second~:</strong> «~nombres~» ne s'emploie pas pour des montants.
<strong>Ce qui pourrait toucher la charte plus tard</strong>, et qui n'est pas une famille de jargon~: la
section 12 déclare que le rédacteur ne peut pas trouver ces défauts seul. Le contrôle par script de la
ligne «~Relecture profane~» en trouve une partie, et c'est une nuance à porter à la limite du dispositif si
un second chapitre le confirme.
<strong>Reste hors de ce chapitre~:</strong> le découpage en deux, qui est une décision de module et non de
rédaction, et le Chapitre 13, dernier du parcours.""" ),
]

CONTROLES = [

('Recalcul des chiffres', 'FAIT — AUCUN ÉCART', """
Le chapitre ne passe aucune écriture~: tous ses chiffres sont des lectures du Bilan et du Compte de
Résultat que les onze chapitres précédents ont construits. <strong>Aucun n'a été écrit de mémoire</strong>,
et tous sont ressortis de <code>outils/verif_ratios.py</code>.
<strong>Vérifiés à l'euro~:</strong> 27~200~€ de résultat net et 17~310~€ de trésorerie au 31~décembre~;
4~400~€ de TVA à décaisser et 4~800~€ d'impôt sur les sociétés, soit 9~200~€ dus à l'État~; 43~200~€ pour
la machine, qui sont les 36~000~€ hors taxes du torréfacteur du Chapitre 8 majorés du taux de 20~% de la
section 3~; 17~310~€ moins 43~200~€ font bien −~25~890~€.
<strong>Le besoin en fonds de roulement~:</strong> 15~000~€ de stock, 63~000~€ de créances clients,
9~000~€ de dettes fournisseurs, tous lus au Bilan de clôture, et leur combinaison vaut 69~000~€.
<strong>Les deux ratios~:</strong> 268~000~€ de ventes, qui sont les comptes 701 et 707 additionnés et ne
comprennent pas la variation de stock~; 27~200~€ sur 268~000~€ font 10,149~%, arrondis à 10,1~%. Les
capitaux propres valent 57~200~€, les comptes 101 et 120, et le compte courant d'associé en est exclu~;
57~200~€ sur 130~410~€ font 43,862~%, arrondis à 43,9~%.
<strong>Le seul nombre non reconstructible depuis le Bilan de clôture est celui du renvoi au
Chapitre 4, 1~450~€</strong>, et le script le retrouve sur une ligne d'écriture des Chapitres 4 et 5.
<strong>Total de contrôle du module, inchangé~: 1~294~694,00~€</strong> au débit comme au crédit.""" ),

('Checklist de relecture', 'QUARANTE-DEUX CASES — AUCUNE EN DÉFAUT', """
Charte, section 21. <strong>Vingt-trois cases sont passées par script</strong>, le reste à la lecture~; une
vingt-quatrième est sans objet, ce chapitre ne portant aucune écriture.
<strong>Ce que le script vérifie et qui est vert~:</strong> aucun mot de la liste des interdits~;
«~toucher~» absent~; aucun tiret cadratin~; une seule déclaration en gras, sans terme de lexique dedans~;
les quatre termes du lexique colorés une seule fois, aucun coloré dans un titre~; une précision, son ancre
hors lexique, sa note présente et son <code>aria-describedby</code> résolu~; Bilan et Compte de Résultat
jamais en minuscules~; toutes les sommes avec leurs insécables et leur unité~; zéro ligne manuelle sur un
plafond de huit~; aucun <code>&lt;UAlert&gt;</code>~; trois sous-titres et aucun niveau 3~; un seul nom
propre de personne à l'accroche~; «~bloc~» jamais nu et «~la grille~» absente~; le bloc de clôture à trois
points.
<strong>Les cases de jugement</strong> sont détaillées aux lignes ci-dessus~: volume, budget de
deux-points, précision, illustration, composant, déclaration, refrain, renvois aux Chapitres 2, 4, 5, 7
et 8 avec leur substance et leur nom.
<strong>Les cases sans objet</strong>~: rattachement des blocs d'écritures, panneau automatique, glose
débit et crédit, écritures automatiques et leur renvoi, légendes de bloc. Le chapitre ne passe aucune
écriture, ce qui est ce que la fiche prévoit.""" ),

('Production du fichier', 'CONFORME', """
Fichier produit sous la charte, section 22. <strong>Le fichier de livraison ne portera que ce qui
s'affichera à l'apprenant</strong>~: le chapo de version et cette annexe en sortent et vivent au PDF. Les
deux fichiers portent le même texte au caractère près, contrôlé sur le source dépouillé de ses balises par
expression régulière — jamais par un parseur.
La précision est écrite en dur. Il n'y a pas d'<code>&lt;UAlert&gt;</code> à convertir.
<strong>Le PDF de livraison revient au pointillé sur l'ancre</strong>, qui est la forme réelle~; les PDF de
relecture la portent en souligné plein.""" ),
]

_COMPLETE = len(sys.argv) > 1 and sys.argv[1] == 'complete'
if _COMPLETE:
    ROWS = ROWS + CONTROLES

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
print('annexe ajoutée à', F, '—', annexe.count(NB), 'insécables,', len(ROWS), 'lignes')
