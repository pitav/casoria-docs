#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute l'annexe de relecture au fichier de travail du Chapitre 10.

Annexe RÉDUITE aux points de vigilance : charte v13, section 22.
"""
import re

F = 'ch10-travail.html'
s = open(F, encoding='utf-8').read()
NB = '\u00a0'
assert NB == chr(160), 'NB doit être un insécable, pas un espace ordinaire'

ROWS = [
('Volume du texte', 'DÉPASSEMENT MOTIVÉ — 701', """
<strong>v4 —</strong> 662 mots au périmètre déclaré, 701 avec les sous-titres. Le seuil de vigilance de la
charte, section 19, est de 680. Le premier jet tombait exactement dessus, avec 641 et 680.
<strong>Les 21 mots de dépassement viennent tous des deux tours de relecture</strong>, et la charte les
prévoit : «~une relecture qui porte sur des manques allonge, et il n'y a rien à en conclure sur la qualité
du premier jet~». Six des sept corrections portaient sur des informations absentes ou sur un mot que
l'apprenant ne pouvait pas comprendre, pas sur des tournures.
<strong>Une coupe a été appliquée au second tour, et c'est le cinquième point du premier qui l'a rendue
nécessaire :</strong> «~Ce que l'entreprise détient ce jour-là est bien réel, neuf mois de couverture déjà
payés~», quinze mots au troisième sous-titre, que le bloc de clôture reprend désormais presque mot pour mot
depuis sa réécriture. La charte, section 2, demande à ce bloc de reformuler et non de recopier ; c'était
au corps de céder, le résumé étant le seul des deux à devoir se lire seul.
<strong>Une seconde coupe reste proposée et non appliquée</strong>, la charte, section 19, demandant de
gager un ajout plutôt que de le constater : «~C'est lui qui explique pourquoi des comptes annoncent
rarement une bonne nouvelle avant qu'elle n'arrive~», seize mots de couleur au deuxième sous-titre, qui
n'ajoutent aucun mécanisme. Elle ramènerait le chapitre à 685. <strong>Le chapitre resterait au-dessus du
seuil de cinq mots</strong>, ce qui est désormais acquis : la clarté demandée coûte plus que la marge
disponible, et c'est exactement le cas que la section 19 prévoit.
<strong>Périmètre déclaré, mesuré par script :</strong> l'accroche et le corps. En sortent la vidéo, les
sous-titres, les blocs d'écritures, leurs légendes, le composant, l'<code>&lt;UAlert&gt;</code>, la
précision et le bloc « Ce que vous avez appris », qui pèse 100 mots à lui seul, la limite haute de la charte.
<strong>Il n'y a donc aucune marge.</strong> Le chapitre porte six termes de lexique, trois cas et trois
blocs pour trente minutes annoncées, et toute demande de contenu se paiera par une coupe — la règle de
conduite de la charte, section 19, dernier paragraphe.
<strong>Ce que le chapitre délègue :</strong> le tri à quatre issues porte la reconnaissance du mécanisme
sur six situations que le texte ne décrit pas, et le contact des deux derniers blocs porte la symétrie que
le texte ne réexplique pas.""" ),

('Budget de deux-points', '1 → 1', """
<strong>Notation : premier jet → état soumis.</strong> Six sections comptées, un seul deux-points en
prose, à l'accroche.
<strong>Il est motivé.</strong> C'est un dénombrement suivi immédiatement de ses trois éléments, la forme
que la charte, section 12, huitième famille, exige quand on annonce un compte : les trois faits de
l'automne sont nommés dans la même phrase que le mot « trois ».
<strong>Hors compte :</strong> aucun dans les quatre légendes de bloc d'écritures.""" ),

('Écritures manuelles', '6 LIGNES', """
Trois blocs de deux lignes, répartis 0~/~1~/~2 sur les trois sous-titres, comme la fiche du déroulé le
prévoit. Le premier sous-titre ne porte aucun bloc, ce qui est normal : il expose le principe et ne fait
passer aucune opération.
<strong>Le mécanisme que chaque bloc introduit</strong>, contrôle imposé par la section 4 du déroulé :
bloc 1, une charge inscrite pour un fait qui n'a pas encore eu lieu ; bloc 2, une charge déjà écrite qui
sort du Compte de Résultat pour devenir un élément d'actif ; bloc 3, le même geste sur un produit, et
c'est le seul du module qui débite un compte de produit. Trois mécanismes distincts, aucune répétition.
<strong>Les blocs 2 et 3 se touchent</strong>, sans texte entre eux, comme la fiche l'impose. C'est le
seul endroit du module où deux blocs sont volontairement collés, et chacun garde sa propre légende, qui
vit à l'intérieur du bloc.""" ),

('Place du panneau automatique', 'ARBITRÉ — LA FICHE DISAIT « À TRANCHER »', """
<strong>Décision : le panneau est placé en fin du premier sous-titre, après l'activité, et non en fin de
texte.</strong> La fiche du Chapitre 10 au tableau de la section 4 du déroulé laissait le point ouvert.
<strong>Le critère de la charte, section 15, ne suffit pas à trancher ici.</strong> Il dit que le panneau
précède quand un montant à saisir se forme à partir d'un compte qu'il alimente. Les trois montants
ajustés — 3~500~€, 2~700~€ et 2~000~€ — sont fixes et ne se forment d'aucun solde, ce qui renverrait le
panneau à sa place par défaut, la fin de texte.
<strong>Trois raisons l'emportent sur le critère.</strong> La première est chronologique : les ajustements
de fin d'exercice sont, par définition, les dernières opérations de l'année, et les faire passer avant
l'activité du dernier trimestre enseignerait l'inverse de ce que le chapitre démontre. La deuxième est
arithmétique dans son effet pédagogique : le bloc 2 sort 2~700~€ des charges externes, et cette prime
d'assurance n'entre dans la grille qu'avec les 26~960~€ du quatrième trimestre. Panneau en fin de texte,
l'apprenant retirerait d'un compte une somme qui n'y est pas encore, et la légende du bloc ne pourrait
décrire aucun avant ni aucun après honnête. La troisième est que le corps doit écrire d'où sortent les
3~600~€ d'assurance et les 2~400~€ du contrat, la charte, section 18, interdisant à une précision de
porter l'origine d'un nombre — et cette origine est une phrase sur ce que la grille affiche, donc
vérifiable seulement une fois le panneau passé.
<strong>C'est la situation que la charte, section 15, décrit :</strong> une règle de forme qui rendrait un
contenu impossible se réexamine avant que le contenu ne se déforme. La charte autorise d'ailleurs
explicitement les trois places, « avant les écritures manuelles, après elles, ou entre deux blocs ».
<strong>Conséquence de forme à valider :</strong> l'<code>&lt;UAlert&gt;</code> reste après le dernier
sous-titre, comme la charte, section 18, l'impose, mais il n'est plus « avant le panneau automatique »
puisque celui-ci a bougé. La clause de placement de la section 18 suppose un panneau en fin de texte, ce
qui n'est plus toujours vrai depuis le Chapitre 5. À reformuler à la charte.""" ),

('La précision — arbitrée sans consigne', 'À VALIDER', """
Ancre «~probable~», au deuxième sous-titre. Elle porte le fait qu'une provision se reprend l'année
suivante si le risque ne se réalise pas ou coûte moins que prévu, et que la charge d'aujourd'hui redevient
alors un produit.
<strong>Le déroulé ne l'avait pas prévue</strong>, son recensement de la section 6 renvoyant la décision à
la rédaction pour les chapitres 9 à 13.
<strong>Le point d'ancrage suit ce que la passe du 24~août a appris :</strong> le bon point n'est pas
celui qui parle du sujet, c'est celui où le lecteur a la chose sous les yeux. Le mot « probable » est la
condition même qui déclenche l'écriture, et il est à trois lignes du bloc qui la passe.
<strong>C'est aussi une réserve que le corps posait déjà</strong> sans dire ce qui arrive dans l'autre
cas, la forme que le Chapitre 7 avait identifiée comme la meilleure candidate.
<strong>Ce qu'elle coûte au corps : rien.</strong> Le nombre qu'elle entoure, 3~500~€, est celui que le
chapitre démontre, et non un nombre venu du décor.
<strong>Écarté :</strong> ancrer sur « douze mois » au troisième sous-titre pour porter les autres charges
qui se répartissent ainsi. La charte n'en autorise qu'une par chapitre, et celle de la provision sert le
cas principal.""" ),

('Les produits constatés d\'avance en une phrase', 'ÉCART À LA FICHE — MOTIVÉ', """
<strong>La fiche demande une phrase et un renvoi visuel, pas un développement autonome. Le chapitre en
prend cinq.</strong>
<strong>La cinquième vient de la relecture</strong>, et elle n'était pas négociable : l'Hôtel Bellevue
apparaissait ici pour la première fois de tout le module, sans qu'aucune phrase ne dise que c'est un
client.
<strong>Le reste du motif est le corollaire de la charte, section 18 :</strong> l'origine d'un nombre reste au
corps. Écrire les 2~000~€ sans dire d'où ils sortent en ferait un nombre magique. Il faut donc le contrat,
les 2~400~€ pour douze mois, les dix mois qui débordent, la destination au Passif et la raison de cette
destination — l'entreprise doit encore des livraisons. Cela ne tient pas en une phrase.
<strong>Ce que le chapitre respecte, en revanche :</strong> aucun raisonnement autonome n'est refait. Le
cas est présenté comme le trajet inverse du précédent et rien de la mécanique n'est réexpliqué.
<strong>Le renvoi visuel demandé par la fiche est le contact des deux blocs</strong>, et non une
illustration. Le chapitre n'en porte aucune, la fiche n'en prévoyant pas.""" ),

('Vigilance de vocabulaire du module', 'VÉRIFIÉ', """
<strong>Le sigle CCA n'apparaît nulle part</strong>, ni pour les charges constatées d'avance, ni pour les
produits constatés d'avance. PCA non plus. Les deux notions sont écrites en toutes lettres à chacune de
leurs occurrences, comme la section 12 du déroulé l'impose en propre pour ce chapitre.
<strong>« Clôture » est employé pour la première fois du module</strong>, et c'est ce chapitre qui
l'introduit. Vérifié : aucun des huit chapitres antérieurs ne le porte, y compris dans un
<code>&lt;UAlert&gt;</code>.
<strong>Aucun numéro de compte n'apparaît dans le corps</strong>, seulement dans les blocs, où la notation
les accompagne de leur intitulé.
<strong>« Toucher », « s'éteindre », « dépense » et « recette » :</strong> absents.""" ),

('Rejeu du journal', 'FAIT — AUCUN ÉCART', """
Toutes les phrases du chapitre qui décrivent un mouvement dans la grille ont été rejouées par script,
bloc par bloc, depuis la première écriture du Chapitre 2.
<strong>Vérifiés au centime :</strong> le compte en banque monte bien de 70~635,10~€ à 99~435,10~€ à
l'écriture de période, puis ne bouge plus d'un euro sur les trois blocs ; le total des charges passe bien
de 155~591,50~€ à 227~551,50~€, puis à 231~051,50~€, puis à 228~351,50~€ ; les charges externes
redescendent bien de 72~960~€ à 70~260~€ et les ventes aux professionnels de 210~000~€ à 208~000~€ ; le
total des produits tombe bien à 283~000~€.
<strong>Les trois lignes que les ajustements ferment sont conformes au scénario chiffré</strong> du
déroulé, section 3 : 70~260~€ de charges externes, 208~000~€ de ventes aux professionnels, et les trois
comptes ouverts au Bilan portent 3~500~€, 2~700~€ et 2~000~€.
<strong>L'accroche est vraie au moment où elle se lit :</strong> aucun des trois faits n'est au Compte de
Résultat quand le lecteur l'ouvre, l'écriture de période n'ayant pas encore été jouée. C'est le contrôle
de la neuvième famille de la charte, section 12, et c'est lui qui a fait réécrire l'accroche — sa
première version annonçait un total de charges que la grille n'affichait pas encore à cet instant.
<strong>Total de contrôle du module au terme du Chapitre 10 : 773~584,90~€</strong> au débit comme au
crédit.
<strong>Ce que les scripts n'avaient jamais vu :</strong> un compte de produit débité, au bloc 3. Le
script de rejeu l'a lu correctement, sa lecture du sens ne dépendant pas de la classe du compte.""" ),

('Le Compte de Résultat ne bouclera pas au Chapitre 11',
 'DÉCISION DEMANDÉE — 22 648,50 € MANQUANTS', """
<strong>C'est le point le plus important de cette relecture, et il ne vient pas de ces deux chapitres : il
vient du déroulé.</strong> Au terme du Chapitre 10, la grille affichera un résultat de 54~648,50~€. Le
Chapitre 11 calcule l'impôt sur 32~000~€ et met en scène un Bilan qui s'équilibre à 130~410~€. Les deux ne
peuvent pas être vrais ensemble.
<strong>L'écart est de 22~648,50~€ exactement, et il tient en trois lignes :</strong> 15~600~€ de
salaires bruts du quatrième trimestre, 6~552~€ de charges patronales correspondantes, et 496,50~€
d'intérêts sur les échéances d'emprunt de juillet à décembre. Aucune des trois n'est prévue par une fiche
— ni celle du Chapitre 9, dont le bloc s'arrête au troisième trimestre, ni celle du Chapitre 10, dont
l'écriture de période ne porte que les ventes, les achats et les charges externes, ni celle du
Chapitre 11, qui ne prévoit aucun panneau automatique.
<strong>Tous les autres postes du Compte de Résultat sont conformes</strong> au scénario chiffré :
135~000~€ d'achats de café vert, 70~260~€ de charges externes, 3~600~€ de dotation aux amortissements,
3~500~€ de dotation à la provision, 208~000~€ et 60~000~€ de ventes, 15~000~€ de variation de stock.
Recompté par script sur les dix chapitres.
<strong>Les trois voies possibles.</strong> Porter les trois lignes à l'écriture de période du
Chapitre 10, qui passerait de neuf à douze lignes — le moins cher, chronologiquement juste, et cohérent
avec ce qu'est une écriture de période ; c'est la voie que je recommande. Donner un panneau automatique au
Chapitre 11, ce qui alourdit le chapitre le plus dense du module. Ou faire passer les salaires du
quatrième trimestre à la main au Chapitre 9, ce que la charte, section 16, interdit — le mécanisme y a
déjà été passé une fois.
<strong>Le Bilan pose la même question, en plus large.</strong> La grille finit le Chapitre 10 avec
99~435,10~€ en banque contre 17~310~€ attendus, 252~000~€ de créances clients contre 63~000~€, et
249~552~€ de dettes fournisseurs contre 9~000~€. Aucun règlement de client, aucun paiement de
fournisseur, aucun versement de TVA et aucune échéance d'emprunt postérieurs au premier trimestre ne sont
inscrits. <strong>C'est une question de déroulé, pas de chapitre</strong>, et elle se pose entière avant
d'écrire le Chapitre 11. Les trois lignes ci-dessus sont seulement la part qui touche le résultat, donc
l'impôt.
<strong>Ces deux chapitres n'ont rien fait pour l'éviter</strong>, et rien non plus pour l'aggraver : ils
passent exactement les écritures que leurs fiches prévoient, aux montants qu'elles donnent.""" ),

('Relecture profane — deux tours', 'FAITE — 7 CORRECTIONS, DONT 3 DÉFAUTS DE MODULE', """
<strong>Pascal, 24~août 2026.</strong> Cinq corrections, toutes appliquées. Deux d'entre elles ne sont pas
des préférences de lecture et dépassent ce chapitre.
<strong>«~la grille~» n'est définie nulle part.</strong> Le mot désigne, dans le déroulé et la charte,
l'ensemble Bilan, Compte de Résultat et grand journal. Il n'a jamais été présenté à l'apprenant.
Recompté~: il apparaît quatre fois dans les huit chapitres livrés, au Chapitre 1, au Chapitre 3 dans un
autre sens, et deux fois au Chapitre 8 — dont une dans un <code>&lt;UAlert&gt;</code>. C'est un mot de
fabricant passé dans le texte. Il est retiré ici au profit de «~ni au Bilan ni au Compte de Résultat~».
<strong>Candidat à la section 12 du déroulé</strong>, les vigilances de vocabulaire propres au module, et
les trois occurrences des Chapitres 1 et 8 sont à revoir.
<strong>L'Hôtel Bellevue arrivait sans son rôle.</strong> Le contrat est nommé, le client ne l'est pas, et
c'est sa première apparition du module. Le Comptoir des Halles avait reçu la sienne au Chapitre 4.
<strong>Règle candidate, à une seule attestation :</strong> un nom propre qui entre dans le module porte
son rôle à sa première occurrence, comme un acronyme porte son développement. La charte, section 12,
première partie, l'impose déjà pour les sigles et pas pour les noms.
<strong>Les trois autres corrections relèvent de la douzième section, sixième famille</strong>, la phrase
qui empile deux notions neuves. «~On ne corrige pas la place d'opérations que les documents n'ont pas
encore reçues~» demandait au lecteur d'admettre trois abstractions pour en comprendre une, et la
formulation est remplacée par les mois eux-mêmes. L'amortissement du torréfacteur était rappelé par sa
substance mais pas par son nom, ce que la charte n'interdit pas et que la relecture a pourtant signalé —
<strong>c'est une leçon nouvelle</strong> : sur une notion nommée dans un chapitre antérieur, rappeler la
substance ne suffit pas, il faut aussi rendre le nom, sans quoi le lecteur ne peut pas relier les deux.
Le bloc de clôture, enfin, résumait deux cas en termes abstraits et les reprend maintenant par leurs
montants.
<strong>Coût du premier tour : 26 mots.</strong>
<strong>Second tour, deux corrections, et la première confirme la famille.</strong> «~bloc~» est un mot de
fabricant au même titre que «~la grille~», et c'est la <strong>deuxième attestation de la même famille en
un seul chapitre</strong>. Le mot désigne en interne une suite d'écritures et n'a jamais été présenté à
l'apprenant. Corrigé en «~bloc d'écritures~» au corps et aux trois légendes, ici et au Chapitre 9, qui
portait le même défaut sans que la relecture ait eu à le signaler. <strong>Deux attestations font une
règle, et non plus un candidat</strong> : le vocabulaire des documents de fabrication ne passe jamais dans
un chapitre sans y avoir été présenté. Les chapitres déjà livrés ne sont pas repris, Pascal l'ayant
explicitement écarté.
<strong>La seconde correction du second tour porte sur un enchaînement</strong>, non sur un mot. Le texte
passait de «~vérifier~» à «~ces corrections~» sans dire que les secondes sortent de la première. Le lien
est désormais écrit dans la phrase même qui pose la vérification, à l'endroit que la relecture désignait,
et non dans celle qui emploie le mot «~corrections~».
<strong>Coût du second tour : six mots ajoutés, quinze retirés.</strong>""" ),

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
<strong>Au registre des écarts :</strong> ouvrir la section du Chapitre 10 et y porter quatre entrées, avec
leur formulation rédigée — les autres situations qui demandent une provision, la dépréciation des créances
douteuses, les charges à payer et produits à recevoir qui sont la symétrie exacte des deux constatations
d'avance, et l'inventaire physique du stock que la fin d'exercice impose. Avec les quatre du Chapitre 9,
le compte du registre passera de 42 à 50 entrées, à recompter par script.
<strong>Au déroulé, section 4 :</strong> la ligne du Chapitre 10 au tableau des places de panneau porte
« à trancher en l'écrivant » et doit recevoir la décision et son motif.
<strong>Au déroulé, section 6 :</strong> ajouter la ligne du Chapitre 10 au recensement des précisions,
ancre «~probable~», et la mention <strong>Écrite.</strong>
<strong>Au déroulé, section 13 :</strong> créer les lignes des Chapitres 9 et 10 à l'ordre de rédaction,
629 et 641 mots.
<strong>Au déroulé, sections 3 et 4 :</strong> ce que la décision sur les 22~648,50~€ imposera.
<strong>À la charte, section 12 :</strong> deux entrées. Une règle à deux attestations, «~la grille~» et
«~bloc~» — le vocabulaire des documents de fabrication ne passe jamais dans un chapitre sans y avoir été
présenté à l'apprenant. Et une règle candidate, à une seule attestation — un nom propre
porte son rôle à sa première occurrence dans le module. Et une leçon à consigner, sur le rappel d'une
notion antérieure par sa substance seule, sans son nom.
<strong>Au déroulé, section 12 :</strong> «~la grille~» et «~bloc~» aux vigilances de vocabulaire, avec
les trois occurrences de «~la grille~» aux Chapitres 1 et 8 signalées mais non reprises, Pascal ayant
écarté la reprise des chapitres livrés.
<strong>Au déroulé, section 7 :</strong> la ligne du Chapitre 9 dit «~le brut se décompose en trois
blocs~», au sens des trois parts et non des écritures. À écrire «~en trois parts~».
<strong>À la charte, section 18 :</strong> la clause de placement de l'<code>&lt;UAlert&gt;</code>, « après
le dernier sous-titre, avant le panneau automatique », suppose un panneau en fin de texte. Deux chapitres
du module ne sont plus dans ce cas. À reformuler en « après le dernier sous-titre ».
<strong>Au journal de rédaction :</strong> la déclaration du Chapitre 10 est une hypothétique à sujet
infinitif — «~laisser ces montants où ils sont ferait dire à l'année autre chose que ce qu'elle a fait~» —
neuvième forme du module. Le journal prévoyait que les Chapitres 4, 7 et 10 porteraient tous une variante
du refrain en gras : <strong>ce n'est pas le cas ici</strong>, la déclaration portant le rattachement à la
période, et le refrain vivant dans la prose de la provision. C'est à consigner, la prédiction étant
écrite.""" ),
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
