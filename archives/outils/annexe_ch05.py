#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Réécrit le chapo et l'annexe de contrôle du fichier de travail du Chapitre 5."""
import re

F = 'ch05-travail.html'
s = open(F, encoding='utf-8').read()
NB = ' '

# ─── chapo ───────────────────────────────────────────────────────────────────
old_chapo = re.search(r'<p class="chapo">.*?</p>', s, re.S).group(0)
new_chapo = ("""<p class="chapo">Version v8, passe de reprise sous la charte v12. Trois sous-titres, deux blocs
d'écritures manuelles répartis 1 / 1 / 0, une illustration en fin de premier sous-titre, la calculette
placée avant le second bloc, un <code>&lt;UAlert&gt;</code>, le panneau automatique entre les deux blocs
manuels, et une précision ancrée sur « due""" + NB + """à""" + NB + """l'État » au deuxième sous-titre. La passe a fait
redescendre les deux-points de vingt-et-un à quatre et a fait sortir l'entrée 5.5 du registre par le haut.
Aucune écriture n'a bougé. <strong>Un point de fond non tranché reste dans le texte</strong>, la légende
qui demande de regarder un total bouger <em>pendant</em> qu'une ligne s'inscrit — voir l'annexe. Ce fichier
est le fichier de travail. Il porte le chapo et l'annexe de contrôle, que le fichier de livraison ne porte
pas.</p>""")
s = s.replace(old_chapo, new_chapo)

ROWS = {}

ROWS['Volume du texte'] = ('DÉPASSEMENT MOTIVÉ', """
<strong>v8 —</strong> 797 mots au périmètre déclaré ci-dessous, 832 avec les sous-titres. Au-dessus du
seuil de 680, loin de la limite de 900. Trajectoire annoncée par les versions antérieures : 715 en v1,
770 en v2, 802 en v3, 802 en v4, 804 en v5, 802 en v7.
<strong>Périmètre déclaré, et mesuré par script :</strong> l'accroche et le corps. En sortent la vidéo,
les sous-titres, les blocs d'écritures, les légendes de bloc, la légende d'illustration, le composant,
l'<code>&lt;UAlert&gt;</code>, la précision et le bloc « Ce que vous avez appris », qui pèse 101 mots à
lui seul. C'est le périmètre fixé à la reprise du Chapitre 4.
<strong>Le recompte du fichier v7 à ce périmètre donne 797 et non 802.</strong> Septième nombre annoncé
pris en défaut sur les documents du module, toujours du même type.
<strong>Ce que la passe coûte : zéro mot.</strong> C'est le premier chapitre repris où la coupe et la
précision s'annulent exactement. La coupe rend quelques mots, la précision n'en demande aucun au corps —
contrairement au Chapitre 4, dont la précision a exigé huit mots d'origine. <strong>Le motif de l'écart
entre les deux cas mérite d'être retenu :</strong> ici, les trois nombres que la note entoure
(7 800, 6 600, 1 200) ont tous leur origine écrite au corps, le chapitre entier étant construit pour ça.
Les deux coupes de réserve chiffrées en v7 restent disponibles et non employées, 53 mots au paragraphe du
crédit de TVA et 28 au dernier paragraphe du troisième sous-titre.""")

ROWS['Budget de deux-points'] = ('21 → 4', """
Objet principal de la passe. Charte v12, section 10, budget d'un par section de niveau 2, l'accroche et le
bloc de clôture comptant chacun pour une section.
<strong>Six sections, quatre deux-points employés.</strong> Vidéo 3 → 1, accroche 2 → 1, premier
sous-titre 9 → 1, deuxième sous-titre 3 → 0, troisième sous-titre 4 → 1, bloc de clôture 1 → 0.
<strong>C'est le chapitre le plus chargé des cinq repris</strong>, et de loin : vingt-et-un en prose et
trente-cinq en tout, contre treize et vingt au Chapitre 4. Le seul premier sous-titre en portait neuf en
prose et douze en légendes.
<strong>Hors compte, repris quand même.</strong> Les cinq légendes passent de quatorze à un. Le seul
restant est le « Légende&nbsp;: » de format que la charte, section 18, impose. La légende du bloc 1 en
portait quatre à elle seule, celle du panneau automatique six sur ses deux sous-blocs.
<strong>Corrections employées.</strong> Quatorze points, trois virgules, aucun tiret cadratin ajouté. Le
chapitre n'en porte toujours qu'un seul, dans le libellé de compte « État — TVA à décaisser », qui est le
nom porté par la grille et non une incise.
<strong>Le deuxième sous-titre descend à zéro, et c'est volontaire.</strong> Le budget est un plafond, pas
un quota. C'est la section qui porte l'arithmétique de la compensation, et ses trois phrases se lisent
mieux coupées qu'annoncées.""")

ROWS['Les quatre deux-points conservés'] = ('MOTIVÉS', """
<strong>Vidéo</strong>, la thèse du chapitre — un prix contient deux montants — posée dès la première
phrase.
<strong>Accroche</strong>, la révélation que 7 800 € des 46 800 € ne correspondent à aucune vente. C'est
la tension de l'accroche, et le signe la porte.
<strong>Premier sous-titre</strong>, l'énumération des trois montants des Chapitres 3 et 4, reprise par
« tous ces montants ». <strong>Seul cas d'énumération conservé des cinq chapitres repris</strong> : la
virgule y noie la reprise, et le point casserait la liste en deux.
<strong>Troisième sous-titre</strong>, la présentation de la reprise du refrain, exactement comme au
Chapitre 4. Les deux chapitres qui portent le refrain gardent leur deux-points au même endroit et pour le
même motif.""")

ROWS['Précision'] = ('POSÉE — ENTRÉE 5.5', """
Ancre <strong>« due""" + NB + """à""" + NB + """l'État »</strong>, au deuxième sous-titre, sur la phrase qui définit la TVA à
décaisser. Vient de l'entrée 5.5 du registre, qui sort par le haut. Cinquième précision écrite du module.
<strong>Ce qu'elle porte.</strong> Que l'entreprise doit la taxe dès qu'elle facture, sans attendre d'être
payée, et que la règle s'inverse pour qui vend des services, dus à l'encaissement. Soixante-trois mots,
quatre phrases, aucun deux-points.
<strong>Elle ne coûte rien au corps</strong>, contrairement à celle du Chapitre 4. Le corollaire de la
charte, section 18, n'est pas en cause ici : les trois nombres que la note entoure ont leur origine écrite
au corps, et la note ne porte qu'une variante de calendrier.
<strong>Le point d'ancrage est celui où le lecteur a la chose sous les yeux.</strong> Il vient de lire
1 200 €, et la grille affiche 36 000 € de créances clients au même instant. La note se vérifie donc sur
les écritures du chapitre, ce que le Chapitre 3 a posé comme critère de qualité.
<strong>Pourquoi elle plutôt que les cinq autres.</strong> 5.2, la franchise en base, tombe sous
l'exception absolue de la section 20 : elle apprend à une partie du lectorat que le chapitre entier ne le
concerne pas, et ne peut pas dépendre d'un clic. 5.4, la TVA sur le matériel, emploierait le vocabulaire
du Chapitre 8. 5.3, le remboursement d'un crédit de TVA, décrit une situation où Latitude Café n'est pas,
donc rien ne s'y vérifie ; elle est en outre déjà signalée par une phrase du corps. 5.1 répète
l'<code>&lt;UAlert&gt;</code> qui est trois paragraphes plus bas. 5.6, les achats hors de France, demande
deux régimes et donc deux paragraphes.
<strong>L'exception absolue a été vérifiée pour 5.5 elle-même</strong>, et elle ne s'applique pas : le
mécanisme du chapitre — collectée moins déductible égale à décaisser — vaut à l'identique pour qui vend
des services. Seule la date de naissance de la dette change. Ce n'est pas une disqualification, c'est une
variante.
<strong>L'ancre n'est pas un terme du lexique</strong> et n'est pas colorée. Ses trois mots sont liés par
des insécables.""")

ROWS['Rejeu du journal'] = ('FAIT — AUCUN ÉCART', """
Toutes les phrases touchées qui décrivent un mouvement dans la grille ont été rejouées par script, bloc
par bloc, depuis la première écriture du Chapitre 2. Il y en avait beaucoup plus qu'aux chapitres
précédents, les légendes de ce chapitre étant presque entièrement faites de trajectoires.
Vérifiés un par un : les créances clients sont bien à zéro avant le bloc 1 puis à 36 000 € ; les ventes
aux professionnels font bien 1 450 → 31 450 → 30 000 € ; les ventes au comptoir font bien
320 → 0 → 9 000 € ; le compte en banque fait bien 49 730 → 50 000 → 60 800 €, soit les 270 € annoncés ;
le compte 4457, celui de la TVA collectée, porte bien 6 000 € après le bloc 1 puis 7 800 € après le
panneau ; le compte 4456, celui de la TVA déductible, porte bien 6 600 € ; les deux tombent bien à zéro
après l'écriture de solde, qui laisse 1 200 € au compte 4455. Les trois écritures sont équilibrées.
<strong>Aucune écriture n'a bougé</strong> : montants, comptes et libellés sont ceux de la v7.
<strong>Un défaut du script de rejeu a été trouvé et corrigé ici</strong>, et il n'aurait pas pu se voir
avant : il cherchait le numéro de compte n'importe où dans la ligne, sur trois chiffres. Le Chapitre 5 est
le premier à porter des comptes à quatre chiffres, et le script lisait les milliers des montants à leur
place. Corrigé dans <code>outils/rejeu.py</code>, qui ancre désormais le numéro après « Bilan — »,
« CR — » ou « GdJal seul — ».""")

ROWS['Le « pendant » de la légende du panneau'] = ('NON TRANCHÉ — DÉCISION ATTENDUE', """
<strong>C'est le seul point de ce chapitre que la passe n'a pas le droit de régler seule, et il reste
donc dans le texte en l'état.</strong> La légende du premier sous-bloc du panneau automatique écrit
« Regardez le Compte de Résultat <em>pendant</em> que ces six lignes s'inscrivent ». Le parti pris de
conception veut que le texte et la saisie soient toujours sur le même écran, mais <strong>même écran ne
veut pas dire même champ de vision</strong> : empilée sur un téléphone, la grille est à un défilement du
texte. Demander de regarder un total bouger pendant qu'une ligne s'inscrit est vrai sur un écran large et
faux sur un téléphone.
<strong>C'est la seule phrase en défaut des huit chapitres écrits</strong>, vérifiée comme telle le
21 août 2026, et les deux réparations proposées alors ne sont toujours pas tranchées.
<strong>Réparation A, à la charge de la rédaction.</strong> Passer la légende en <em>avant / après</em>.
Texte de repli, rédigé et prêt : « Regardez le Compte de Résultat avant de passer le panneau, puis après.
Les ventes aux professionnels sont redescendues de 31 450 € à 30 000 €, le chiffre du trimestre, qui
comprend les 1 450 € de janvier. » Coût : deux mots, et la perte de la simultanéité.
<strong>Réparation B, à la charge du produit.</strong> Faire que tout bloc affiche à son pied les totaux
qu'il déplace, ancienne valeur et nouvelle. Elle affranchirait la rédaction de la mise en page pour tout
le module, et la légende actuelle deviendrait exacte sans être touchée. C'est le chantier « pied de bloc »
du journal, ordonnancé avant les tests utilisateurs.
<strong>Ce que la passe a fait, et rien de plus :</strong> couper le deux-points de la phrase. Le verbe
« pendant » est intact, et le texte livré est donc identique au texte validé sur ce point.""")

ROWS['Un symbole € rendu par la coupe'] = ('CORRIGÉ', """
La phrase « les deux comptes de taxe portent son total : Latitude Café a facturé 7 800 € de taxe à ses
clients et en a payé 6 600 à ses fournisseurs » portait une ellipse d'unité sur la seconde somme, licite
tant que les deux montants vivaient dans la même phrase.
<strong>La coupe la rend illisible</strong> : une fois le deux-points remplacé par un point, l'unité
manque à une somme isolée. Le symbole est rétabli, avec son insécable, et le chapitre porte désormais une
unité sur chacune de ses sommes.
<strong>C'est une illustration du point 3 de la charte, section 10</strong>, sous un angle nouveau. On
savait que couper une phrase à deux-points redistribue le sujet et le verbe et peut rendre fausse une
description exacte. Ici la coupe ne rend rien de faux, elle rend visible une ellipse qui tenait par la
proximité. <strong>Le contrôle qui l'attrape :</strong> après la passe, vérifier que chaque somme du corps
porte son unité, et pas seulement ses insécables.""")

ROWS['Numéros de compte dans le corps'] = ('RÈGLE TENUE APRÈS LA COUPE', """
La règle du déroulé, section 12 — aucun numéro n'apparaît seul, nulle part — a été revérifiée sur chaque
phrase touchée, la coupe étant précisément ce qui risquait de séparer un numéro de son libellé.
Deux endroits ont demandé une réécriture. « sur deux comptes séparés : le compte 4457 pour la TVA
collectée, le compte 4456 pour la TVA déductible » devient « sur deux comptes séparés. Le compte 4457
reçoit la TVA collectée, le compte 4456 la TVA déductible ». Et dans la légende du panneau, « Puis sur le
4456, celui de la TVA déductible » devient « Puis sur le compte 4456, celui de la TVA déductible », ce qui
rétablit au passage le parallèle avec le 4457 de la phrase précédente.
Recompté après la passe : <strong>aucune occurrence isolée</strong>, blocs d'écritures exceptés, où le
numéro est suivi de son libellé par le format même de la ligne.""")

ROWS['Les cinq autres entrées du registre'] = ('RESTENT', """
Confrontées au test de la charte, section 20, en même temps que 5.5. Le détail du tri est à la ligne
« Précision » ci-dessus.
<strong>5.2, les régimes et rythmes de déclaration.</strong> Reste, et pour un motif qui n'est pas de
forme : c'est l'entrée type de l'exception absolue de la section 20. Elle doit être lue par tout le monde
ou par personne, jamais au choix du lecteur. Sa place est l'aside de fin de module, ou le corps.
<strong>5.1</strong> répéterait l'alerte du chapitre. <strong>5.3</strong> décrit une situation où
l'entreprise du fil rouge n'est pas, et le corps la signale déjà. <strong>5.4</strong> attend son
arbitrage au Chapitre 8 et emploierait son vocabulaire. <strong>5.6</strong> demande deux paragraphes.
Le registre garde ses trente-trois entrées et en compte une de moins au tri du Chapitre 13.""")

ROWS['Registre des écarts'] = ('6 ENTRÉES, DONT UNE SORTIE PAR LE HAUT', """
Les autres taux (5.1) ; les régimes et rythmes de déclaration, dont la franchise en base (5.2) ; ce que
le remboursement d'un crédit de TVA coûte en temps (5.3) ; la TVA sur les achats de matériel (5.4) ; la
TVA due à la facture ou à l'encaissement (5.5, destination <strong>précision</strong>) ; les achats hors
de France (5.6).""")

ROWS['Incises'] = ('CONFORME', """
Aucun tiret cadratin en usage de parenthèse dans le corps, et la passe n'en a ajouté aucun — c'est la
correction que la charte, section 10, interdit expressément. Le seul tiret long du texte reste dans le
libellé de compte « État — TVA à décaisser », qui est le nom porté par la grille. Aucun tiret de chute
employé, ce qui laisse le chapitre sans sa chute autorisée, comme en v7.""")

ROWS['Production du fichier'] = ('CONFORME', """
Fichier repris sous la charte v12, section 22, dans sa forme nouvelle. <strong>Le fichier de livraison ne
porte que ce qui s'affichera à l'apprenant</strong> : le chapo de version et cette annexe en sortent, et
vivent au PDF de livraison. Les deux fichiers portent le même texte, au mot près, le livrable étant dérivé
de ce fichier de travail par script.
La précision y est écrite en dur, <code>&lt;button type="button" class="prec"
aria-describedby="…"&gt;</code> suivie de sa <code>&lt;p class="prec-note"&gt;</code>, et
l'<code>&lt;UAlert&gt;</code> est converti depuis la classe <code>.alert</code> du fichier de travail.
Le PDF de livraison revient au pointillé sur l'ancre, le souligné plein étant réservé aux PDF de
relecture.""")

# ─── application ─────────────────────────────────────────────────────────────
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

ORDRE = ['Volume du texte', 'Budget de deux-points', 'Les quatre deux-points conservés',
         'Précision', 'Les cinq autres entrées du registre', 'Rejeu du journal',
         'Le « pendant » de la légende du panneau', 'Un symbole € rendu par la coupe',
         'Numéros de compte dans le corps', 'Registre des écarts', 'Incises',
         'Production du fichier']
for cle in ORDRE:
    maj(cle, *ROWS[cle])

s = s.replace('<td class="cle">Relecture profane</td><td>FAITE — 6 TOURS</td>',
              '<td class="cle">Relecture profane</td><td>FAITE — 6 TOURS + PASSE</td>')

# ─── typographie du PDF : insécables dans les guillemets de l'annexe ─────────
tete, sep, annexe = s.partition('<h2 class="saut">')
annexe = re.sub(r'«\s+', '«' + NB, annexe)
annexe = re.sub(r'\s+»', NB + '»', annexe)
# et les sommes : séparateur de milliers, espace avant € et %
for _ in range(3):
    annexe = re.sub(r'(?<=\d)[ ](?=\d{3}\b)', NB, annexe)
annexe = re.sub(r'(?<=\d)[ ](?=[€%])', NB, annexe)
s = tete + sep + annexe

open(F, 'w', encoding='utf-8').write(s)
print('annexe réécrite dans', F)
