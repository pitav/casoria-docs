#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Réécrit le chapo et l'annexe de contrôle du fichier de travail du Chapitre 8."""
import re

F = 'ch08-travail.html'
s = open(F, encoding='utf-8').read()
NB = '\u00a0'
assert NB == chr(160), 'NB doit être un insécable, pas un espace ordinaire'

old_chapo = re.search(r'<p class="chapo">.*?</p>', s, re.S).group(0)
new_chapo = ("""<p class="chapo">Version v5, passe de reprise sous la charte v12. Trois sous-titres, deux blocs
manuels répartis 3 / 2 / 0, une activité, une illustration, un <code>&lt;UAlert&gt;</code>, aucun panneau
automatique, et la précision « cinq""" + NB + """ans » que ce chapitre a inventée pour le module. La passe a fait
redescendre les deux-points de vingt-six à cinq, le plus gros écart des huit chapitres. Aucune écriture n'a
bougé, et le texte a gagné deux mots. <strong>Aucune précision nouvelle</strong> : la charte n'en autorise
qu'une par chapitre et celle-ci était déjà posée. <strong>Le registre et le déroulé ne sont pas
répercutés</strong> : ils le seront en une fois à la fin de la passe, qui s'achève avec ce chapitre. Ce
fichier est le fichier de travail. Il porte le chapo et l'annexe de contrôle, que le fichier de livraison ne
porte pas.</p>""")
s = s.replace(old_chapo, new_chapo)

ROWS = {}

ROWS['Volume du texte'] = ('DÉPASSEMENT MOTIVÉ', """
<strong>v5 —</strong> 858 mots au périmètre déclaré ci-dessous, 898 avec les sous-titres. Au-dessus du
seuil de 680, sous la limite de 900, et <strong>toujours le plus long du module</strong>.
<strong>Périmètre déclaré, et mesuré par script :</strong> l'accroche et le corps. En sortent la vidéo,
les sous-titres, les blocs d'écritures, leurs légendes, la légende d'illustration, le composant,
l'<code>&lt;UAlert&gt;</code>, la précision et le bloc « Ce que vous avez appris », qui pèse 98 mots à lui
seul.
<strong>Le recompte du fichier v4 à ce périmètre donne 856 et non 854.</strong> Dixième nombre annoncé
pris en défaut sur les documents du module, et le dernier de la passe — le script de livraison les
recompte tous désormais.
<strong>Ce que la passe coûte : deux mots.</strong> Deux phrases de la démonstration de l'amortissement
sont devenues autonomes et ont demandé un sujet. <strong>Le chapitre n'a plus que quarante-deux mots de
marge avant la limite de 900</strong>, sous-titres compris, ce qui est la situation la plus tendue du
module. Toute demande de contenu se paiera par une coupe.""")

ROWS['Budget de deux-points'] = ('26 → 5', """
Objet principal de la passe. Charte v12, section 10, budget d'un par section de niveau 2, l'accroche et le
bloc de clôture comptant chacun pour une section.
<strong>Six sections, cinq deux-points employés.</strong> Vidéo 2 → 1, accroche 2 → 1, premier
sous-titre 5 → 1, deuxième sous-titre 9 → 1, troisième sous-titre 8 → 1, bloc de clôture 1 → 0.
<strong>C'est le plus gros écart des huit chapitres</strong>, vingt-et-un signes retirés à la prose, et
c'est aussi le seul chapitre dont <em>trois</em> sections en portaient plus de quatre. Le total, corps et
légendes confondus, passe de trente-trois à six.
<strong>Ce que le chapitre avait de particulier :</strong> il porte sept termes de lexique, le maximum du
module après le Chapitre 2, et chacun était glosé par un deux-points. <strong>Cinq gloses de lexique de
suite, c'est exactement ce que la section 10 appelle « une manière de parler »</strong> — la
recommandation sans plafond devenue un style. Une seule est gardée, la dernière.
<strong>Hors compte, repris quand même.</strong> Les légendes passent de sept à un, le seul restant étant
le « Légende&nbsp;: » de format que la charte, section 18, impose.
<strong>Corrections employées.</strong> Dix-huit points, sept virgules, aucun tiret cadratin ajouté.""")

ROWS['Les cinq deux-points conservés'] = ('MOTIVÉS', """
<strong>Vidéo</strong>, « deux achats peuvent se ressembler en tout point », dénombrement suivi de ses
trois éléments. Forme que la charte, section 12, huitième famille, exige.
<strong>Accroche</strong>, le torréfacteur payé puis les 43&nbsp;200&nbsp;€ qui partent. C'est le chiffre
qui ouvre la tension avec le total des charges, deux phrases plus bas.
<strong>Premier sous-titre</strong>, « un bien qui servira plusieurs années n'est pas une charge&nbsp;:
c'est un investissement ». <strong>Celui-là est intouchable</strong>&nbsp;: c'est la formulation arrêtée
mot pour mot à la relecture du 22 août, en remplacement d'une correction qui cassait la définition de
lexique. La reprendre reviendrait à rouvrir un arbitrage déjà rendu.
<strong>Deuxième sous-titre</strong>, la glose de la valeur nette comptable, « ce qu'elle vaut encore dans
les comptes ». Quatre mots, dernier terme du chapitre, et la seule des cinq gloses de lexique qui survit.
<strong>Troisième sous-titre</strong>, la chute du point d'étape — « le Bilan n'est pas un second document
que quelqu'un remplirait à côté du journal&nbsp;: c'est le journal résumé, compte par compte ». C'est la
phrase que tout le sous-titre construit, et le signe est ce qui fait la bascule.""")

ROWS['La précision — premier emploi du module'] = ('CONSERVÉE — NOTE REPRISE', """
Ancre « cinq""" + NB + """ans », au deuxième sous-titre. C'est la première précision écrite du module, celle qui a
fait naître le dispositif à la relecture du 22 août, et elle est conservée telle quelle quant au fond.
<strong>Aucune précision nouvelle n'a été posée</strong>, la charte, section 18, n'en autorisant qu'une
par chapitre. C'est le seul des six chapitres repris dans ce cas. Les quatre entrées du registre restent
donc toutes candidates, et 8.1 comme 8.4 gardent le handicap que la note leur inflige déjà en disant que
la durée est estimée par l'entreprise.
<strong>Sa note a perdu ses deux deux-points.</strong> Elle en portait deux pour cinq lignes, dont un
d'annonce devant la liste des repères d'usage. <strong>Décision de méthode, valable pour tout le
module :</strong> une note de précision est de la prose et entre au budget de sa section comme le reste.
La charte, section 10, ne l'écrit pas — elle n'exclut que les légendes et les listes — et le silence se
lisait dans les deux sens. Les six chapitres repris l'ont tous traitée ainsi ; c'est à consigner.
<strong>L'espace de l'ancre est passé en insécable</strong> au passage, « cinq""" + NB + """ans » ne pouvant pas se
couper en fin de ligne. Les cinq autres précisions du module l'avaient d'origine ; celle-ci est
antérieure à la règle.""")

ROWS['Rejeu du journal'] = ('FAIT — AUCUN ÉCART', """
Toutes les phrases touchées qui décrivent un mouvement dans la grille ont été rejouées par script, bloc
par bloc, depuis la première écriture du Chapitre 2. Ce chapitre en portait plus qu'aucun autre, son
troisième sous-titre étant un point d'étape qui ne fait que décrire la grille.
<strong>Vérifiés au centime :</strong> le compte en banque descend bien de 104&nbsp;571,10&nbsp;€ à
61&nbsp;371,10&nbsp;€ à l'achat&nbsp;; le total des charges reste bien à 81&nbsp;087,50&nbsp;€ après le
bloc 1, puis monte bien à 84&nbsp;687,50&nbsp;€ après le bloc 2&nbsp;; la ligne Torréfacteur porte bien
36&nbsp;000&nbsp;€ et les amortissements 3&nbsp;600&nbsp;€, soit 32&nbsp;400&nbsp;€ de valeur nette
comptable.
<strong>Le contrôle du compte 512 est exact :</strong> treize lignes, 112&nbsp;240&nbsp;€ au débit,
50&nbsp;868,90&nbsp;€ au crédit, différence 61&nbsp;371,10&nbsp;€, qui est bien ce qu'affiche la ligne
Trésorerie. Les trois nombres du corps sont vérifiés un par un, et le compte de treize lignes aussi.
<strong>Total de contrôle du module au terme du Chapitre 8 : 388&nbsp;328,90&nbsp;€</strong> au débit
comme au crédit. Le script le recalcule à chaque exécution et lève si les deux colonnes diffèrent.
<strong>Aucune écriture n'a bougé</strong> : montants, comptes et libellés sont ceux de la v4.""")

ROWS['Un total de contrôle du Chapitre 7 ne se reproduit pas'] = ('RÉSOLU', """
Ce chapitre avait trouvé, le 22 août, que le total de contrôle annoncé par l'annexe du Chapitre 7 était
faux alors que tous ses soldes étaient exacts. Le nombre est resté faux jusqu'à la reprise du Chapitre 7,
le 24 août, qui l'a corrigé&nbsp;: <strong>341&nbsp;528,90&nbsp;€ et non 300&nbsp;258,60&nbsp;€</strong>.
<strong>Ce qui a changé depuis, et qui règle la famille entière :</strong> le script de livraison
recompte désormais tout ce qu'une annexe annonce et refuse d'écrire si un nombre ne correspond pas, et le
script de rejeu recalcule le total de contrôle du module à chaque exécution. <strong>Dix nombres annoncés
ont été pris en défaut sur les huit chapitres</strong>, tous du même type — un compte non remis à jour
après une correction. C'était le défaut le plus régulier des documents du module, et c'est le seul que la
passe a éteint pour de bon.""")

ROWS['Répercussion différée'] = ('CE QUE LA PASSE FINALE DOIT RECEVOIR', """
<strong>Décidé le 24 août 2026 : le registre et le déroulé ne se répercutent plus chapitre par
chapitre</strong>, mais en une fois maintenant que les huit sont repris.
<strong>Au registre des écarts : rien pour ce chapitre.</strong> Aucune entrée du Chapitre 8 ne sort par
le haut, la précision étant déjà prise. C'est le seul des six chapitres repris à ne rien devoir au
registre.
<strong>Au déroulé, section 6 :</strong> la ligne du Chapitre 8 au recensement des précisions est la
seule à ne pas porter la mention <strong>Écrite.</strong> que les cinq autres portent, alors qu'elle
l'est depuis le 22 août. À rétablir. Et l'état de la passe passe à <em>huit chapitres faits</em>.
<strong>Au déroulé, section 13 :</strong> le volume du Chapitre 8 passe de 854 à 858 mots, et la passe
est close.
<strong>À la charte, section 10 :</strong> deux choses. L'exemple « Un associé peut prêter à sa propre
société » à remettre en deux phrases, voir l'annexe du Chapitre 7. Et <strong>une phrase à ajouter au
budget : une note de précision est de la prose et compte dans sa section</strong>, ce que le silence
actuel laissait ambigu.
<strong>Ce que la passe a mesuré, et qui vaut d'être écrit quelque part :</strong> les huit chapitres
portaient 191 deux-points dans leur corps, dont 123 en prose courante. <strong>Ils en portent 34 en prose
après la passe, et 43 en tout</strong>, soit de trois à cinq par chapitre, et pas un chapitre au-dessus du
budget. Le comptage est refait par script sur les huit fichiers livrés, au même périmètre.""")

ROWS['Production du fichier'] = ('CONFORME', """
Fichier repris sous la charte v12, section 22. <strong>Le fichier de livraison ne porte que ce qui
s'affichera à l'apprenant</strong> : le chapo de version et cette annexe en sortent, et vivent au PDF de
livraison. Les deux fichiers portent le même texte, au caractère près, contrôlé par le script de livraison
sur le source dépouillé de ses balises.
La précision y est écrite en dur, et l'<code>&lt;UAlert&gt;</code> est converti depuis la classe
<code>.alert</code> du fichier de travail. Le PDF de livraison revient au pointillé sur l'ancre.
<strong>C'est le dernier fichier de la passe des huit chapitres.</strong>""")

INSERT = [None]

def maj(cle, etat, detail):
    global s
    pat = re.compile(r'<tr><td class="cle">' + re.escape(cle) +
                     r'</td>\s*<td>.*?</td>\s*<td>.*?</td></tr>', re.S)
    new = (f'<tr><td class="cle">{cle}</td><td>{etat}</td><td>'
           + ' '.join(detail.split()) + '</td></tr>')
    if pat.search(s):
        s = pat.sub(lambda m: new, s, count=1)
    else:
        anc = INSERT[0]
        assert anc in s, f'ancre absente pour insérer « {cle} »'
        s = s.replace(anc, anc + '\n' + new, 1)
    INSERT[0] = new

ORDRE = ['Volume du texte', 'Budget de deux-points', 'Les cinq deux-points conservés',
         'La précision — premier emploi du module', 'Rejeu du journal',
         'Un total de contrôle du Chapitre 7 ne se reproduit pas',
         'Répercussion différée', 'Production du fichier']
for cle in ORDRE:
    maj(cle, *ROWS[cle])

s = re.sub(r'<td class="cle">Relecture profane</td><td>(FAITE[^<]*)</td>',
           lambda m: f'<td class="cle">Relecture profane</td><td>{m.group(1)} + PASSE</td>', s, count=1)

tete, sep, annexe = s.partition('<h2 class="saut">')
annexe = re.sub(r'«\s+', '«' + NB, annexe)
annexe = re.sub(r'\s+»', NB + '»', annexe)
for _ in range(3):
    annexe = re.sub(r'(?<=\d)[ ](?=\d{3}\b)', NB, annexe)
annexe = re.sub(r'(?<=\d)[ ](?=[€%])', NB, annexe)
s = tete + sep + annexe

open(F, 'w', encoding='utf-8').write(s)
print('annexe réécrite dans', F)
