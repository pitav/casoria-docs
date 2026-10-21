#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Réécrit le chapo et l'annexe de contrôle du fichier de travail du Chapitre 4."""
import re

F = 'ch04-travail.html'
s = open(F, encoding='utf-8').read()
NB = '\u00a0'

# ─── chapo ───────────────────────────────────────────────────────────────────
old_chapo = re.search(r'<p class="chapo">.*?</p>', s, re.S).group(0)
new_chapo = """<p class="chapo">Version v6, passe de reprise sous la charte v12. Trois sous-titres, trois blocs
d'écritures manuelles répartis 1 / 1 / 1, une illustration en fin de premier sous-titre, l'activité placée
avant le dernier bloc, une précision ancrée sur « trente""" + NB + """jours » au premier sous-titre. Aucun panneau
automatique, ce chapitre n'en porte pas. La passe a fait redescendre les deux-points de treize à cinq et a
fait sortir l'entrée 4.1 du registre par le haut. Aucune écriture n'a bougé. Ce fichier est le fichier de
travail. Il porte le chapo et l'annexe de contrôle, que le fichier de livraison ne porte pas.</p>"""
s = s.replace(old_chapo, new_chapo)

ROWS = {}

ROWS['Volume du texte'] = ('DÉPASSEMENT MOTIVÉ', """
<strong>v6 —</strong> 724 mots au périmètre déclaré ci-dessous, 760 avec les sous-titres. Au-dessus du
seuil de 680, loin de la limite de 900. Trajectoire annoncée par les versions antérieures : 663 en v1,
724 en v2, 722 en v3, 718 en v4, 722 en v5.
<strong>Périmètre déclaré, et mesuré par script :</strong> l'accroche et le corps. En sortent la vidéo,
les sous-titres, les blocs d'écritures, les légendes de bloc, la légende d'illustration, le composant, la
précision et le bloc « Ce que vous avez appris », qui pèse 105 mots à lui seul. C'est le périmètre des
Chapitres 1, 2, 3 et 7, rendu reproductible.
<strong>Le recompte du fichier v5 à ce périmètre donne 717 et non 722.</strong> Sixième nombre annoncé
pris en défaut sur les documents du module, toujours du même type — un compte non remis à jour après une
correction. Les nombres de cette annexe sont désormais recomptés par le script de livraison, qui refuse
d'écrire si l'un d'eux ne correspond pas.
<strong>Ce que la passe coûte :</strong> +7 mots. La coupe des deux-points, seule, en rend 1 ; les 8
autres sont l'origine du délai portée au corps, que la précision exigeait (charte, section 18). Le
chapitre n'a toujours pas de marge, et le motif du dépassement est inchangé — deux raisonnements que rien
ne peut porter à la place du texte, <em>pourquoi</em> le produit se compte à la facture et <em>ce que
devient le Bilan</em> le jour du règlement.""")

ROWS['Budget de deux-points'] = ('13 → 5', """
Objet principal de la passe. Charte v12, section 10, budget d'un par section de niveau 2, l'accroche et le
bloc de clôture comptant chacun pour une section.
<strong>Six sections, cinq deux-points employés.</strong> Vidéo 2 → 1, accroche 1 → 1, premier
sous-titre 4 → 1, deuxième sous-titre 3 → 1, troisième sous-titre 3 → 1, bloc de clôture 2 → 0. Le
chapitre en portait treize en prose et vingt en tout, ce qui le plaçait dans la moyenne haute des huit
chapitres mesurés le 23 août.
<strong>Hors compte, repris quand même.</strong> Les légendes et la légende d'illustration passent de
sept à un. Le seul restant est le « Légende&nbsp;: » de format que la charte, section 18, impose.
<strong>Corrections employées.</strong> Onze points, deux virgules, aucun tiret cadratin ajouté. Le
chapitre en compte toujours un seul, celui de la chute, au troisième point du bloc de clôture.
<strong>Profil obtenu identique à celui du Chapitre 3 repris</strong>, cinq en prose et un hors compte.""")

ROWS['Les cinq deux-points conservés'] = ('MOTIVÉS', """
Chacun répond à une question posée juste au-dessus, ou présente une formule que le texte va installer.
Aucun n'est une simple annonce d'énumération.
<strong>Vidéo</strong>, les deux faits posés côte à côte, qui sont le sujet même du chapitre.
<strong>Accroche</strong>, le contenu du premier lot, qui chiffre l'achat que la phrase vient d'annoncer.
<strong>Premier sous-titre</strong>, « Le Chapitre 1 a déjà donné la réponse », deux lignes après la
question « Reste à savoir quand la vente compte ».
<strong>Deuxième sous-titre</strong>, la conséquence de la livraison sur le moment où la charge se compte,
qui porte la démonstration du sous-titre.
<strong>Troisième sous-titre</strong>, l'installation du refrain du module. Celui-là ne pouvait pas
partir&nbsp;: la formule est située avant d'être énoncée, et c'est le signe deux-points qui fait la
présentation.""")

ROWS['Précision'] = ('POSÉE — ENTRÉE 4.1', """
Ancre <strong>« trente""" + NB + """jours »</strong>, au premier sous-titre, dans le paragraphe qui pose le délai.
Vient de l'entrée 4.1 du registre, qui sort par le haut. Quatrième précision écrite du module.
<strong>Ce qu'elle porte.</strong> Le plafond légal de soixante jours entre professionnels, l'amende
encourue au-delà, et les pénalités dues dès le lendemain de l'échéance même si personne ne les réclame.
Cinquante-quatre mots, trois phrases, aucun deux-points.
<strong>Le corps a reçu l'origine du nombre</strong>, comme le corollaire non négociable de la charte,
section 18, l'exige. « Le délai est convenu entre les deux entreprises et figure sur la facture. Ici,
c'est trente""" + NB + """jours. » Sans cette phrase, la précision aurait porté d'où sortent les trente jours, ce
qu'une précision ne fait jamais. C'est ce qui explique les huit mots ajoutés au corps.
<strong>Le point d'ancrage est celui où le lecteur a la chose sous les yeux</strong>, leçon du Chapitre 1.
Le mot « trente""" + NB + """jours » revient six fois dans le chapitre&nbsp;; l'ancre est posée sur la seule
occurrence qui dit que ce délai est un choix, et non sur l'accroche, qui le subit.
<strong>Ce qui a été écarté de la note, et c'est un arbitrage.</strong> La variante des quarante-cinq
jours fin de mois. Elle est exacte et elle figure au registre. Elle ajoute un second nombre et une
locution de métier à une note de trois lignes, et un seul repère retenu vaut mieux que deux confondus.
<strong>Ce qui a été corrigé au passage.</strong> La formulation du registre mettait l'amende sur le
fournisseur seul. La sanction porte sur la clause et sur le retard, donc sur les deux parties. Vérifié
sur une source à jour d'août 2026, plafond de soixante jours à compter de la facture inchangé.
<strong>L'ancre n'est pas un terme du lexique</strong> et n'est pas colorée, comme la charte, section 18,
l'impose. L'espace entre les deux mots est insécable, le bouton ne pouvant pas se couper en fin de ligne.""")

ROWS['Les trois autres entrées du registre'] = ('RESTENT', """
Confrontées au test de la charte, section 20, en même temps que 4.1.
<strong>4.2, le client qui ne paie jamais.</strong> La plus utile des quatre, et une extension. Le doute
constaté avant la perte, puis la perte, demandent un paragraphe et un mécanisme que le Chapitre 10
enseigne sur un autre cas. Reste au registre, et l'arbitrage contre l'entrée du Chapitre 10 reste ouvert.
<strong>4.3, l'escompte de règlement et les pénalités de retard.</strong> Porte deux clauses, donc deux
notions. La moitié la plus utile des deux, les pénalités, vient d'être emportée par 4.1. Reste au
registre avec un handicap nouveau, à consigner au tri.
<strong>4.4, vendre ses créances.</strong> Extension, et elle chiffre une créance de soixante-trois mille
euros que le module n'affiche nulle part. Un nombre invérifiable dans une note ouvrante est exactement ce
que la neuvième famille de la section 12 interdit. Reste au registre.""")

ROWS['Rejeu du journal'] = ('FAIT — AUCUN ÉCART', """
Toutes les phrases touchées qui décrivent un mouvement dans la grille ont été rejouées par script, bloc
par bloc, depuis la première écriture du Chapitre 2. Charte v12, section 12, neuvième famille.
Les 320""" + NB + """€ du Chapitre 3 arrivent bien sur le compte le soir même, le 512 passant de 50""" + NB + """000 à
50""" + NB + """320""" + NB + """€. Au bloc 3, les deux lignes sont bien toutes les deux à l'Actif, 512 et 411. La créance tombe
bien de 1""" + NB + """450""" + NB + """€ à zéro, et rien ne l'a touchée entre le bloc 1 et le bloc 3. La banque monte bien de
48""" + NB + """280 à 49""" + NB + """730""" + NB + """€, soit exactement 1""" + NB + """450""" + NB + """€.
<strong>Le total de l'Actif est identique avant et après le règlement</strong>, 49""" + NB + """730""" + NB + """€ dans les deux
cas, ce qui vérifie la phrase « l'entreprise ne détient ni plus ni moins qu'avant » — devenue une phrase
autonome par la passe, et donc à revérifier. Le bloc 2 ne touche pas le 512, ce qui vérifie « n'a rien
sorti de son compte ». Les trois écritures sont équilibrées, débit contre crédit.
<strong>Aucune écriture n'a bougé</strong>&nbsp;: montants, comptes et libellés sont ceux de la v5.""")

ROWS['Paragraphes scindés'] = ('2', """
La coupe des deux-points laisse deux paragraphes à sept phrases, ce qui est le seuil retenu aux
Chapitres 1 à 3.
<strong>Premier sous-titre</strong>, scindé après « c'est aussi l'exception ». Effet de bord utile&nbsp;:
la note de précision se retrouve juste sous son ancre, au lieu d'être repoussée de quatre phrases.
<strong>Troisième sous-titre</strong>, scindé après « l'argent en banque monte de 1""" + NB + """450""" + NB + """€ ». Les deux
phrases de conclusion forment désormais un paragraphe court, juste avant « C'est le point clé du
chapitre ».""")

ROWS['Un parallèle rétabli'] = ('V6', """
« C'est une créance client&nbsp;: une somme facturée à un client et pas encore reçue » portait un
deux-points là où la définition symétrique du sous-titre suivant portait déjà une virgule, « une dette
fournisseur, une somme facturée par un fournisseur et pas encore payée ». Les deux gloses de lexique sont
désormais ponctuées de la même façon.
<strong>C'est le seul cas des quatre chapitres repris où la coupe rend une symétrie au lieu d'en
coûter une.</strong> Ailleurs elle en coûte, et le remède retenu reste le parallèle lexical — ici « À
gauche / À droite » dans la légende d'illustration, dont les deux deux-points ont sauté sans que la
structure bouge.""")

ROWS['Registre des écarts'] = ('4 ENTRÉES, DONT UNE SORTIE PAR LE HAUT', """
Délais de paiement encadrés par la loi (4.1, destination <strong>précision</strong>), client qui ne paie
jamais (4.2), escompte de règlement et pénalités de retard (4.3), mobilisation des créances (4.4). Le
registre garde ses vingt-sept entrées et en compte une de moins au tri du Chapitre 13.""")

ROWS['Incises'] = ('CONFORME', """
Aucun tiret cadratin en usage de parenthèse, et la passe n'en a ajouté aucun — c'est la correction que la
charte, section 10, interdit expressément. Un seul tiret de chute dans tout le chapitre, au troisième
point du bloc « Ce que vous avez appris ».""")

ROWS['Production du fichier'] = ('CONFORME', """
Fichier repris sous la charte v12, section 22, dans sa forme nouvelle. <strong>Le fichier de livraison ne
porte que ce qui s'affichera à l'apprenant</strong>&nbsp;: le chapo de version et cette annexe en sortent,
et vivent au PDF de livraison. Les deux fichiers portent le même texte, au mot près, le livrable étant
dérivé de ce fichier de travail par script.
La précision y est écrite en dur, <code>&lt;button type="button" class="prec"
aria-describedby="…"&gt;</code> suivie de sa <code>&lt;p class="prec-note"&gt;</code>. Aucune alerte à
convertir, ce chapitre n'en porte pas.
Le PDF de livraison revient au pointillé sur l'ancre, le souligné plein étant réservé aux PDF de
relecture.""")

ROWS['Candidats à la charte, non portés'] = ('EN ATTENTE', """
Inchangé depuis la v5, et la passe n'en a produit aucun de plus. Le seuil de longueur de la déclaration en
gras attend toujours sa seconde attestation à la section 9, celle du Chapitre 7 faisant sept mots.
<strong>Ce que la passe apprend, et qui n'est pas une famille de jargon&nbsp;:</strong> couper un
deux-points en deux phrases redistribue le sujet et le verbe, et une description exacte peut devenir
fausse à cette occasion. C'est déjà écrit à la section 10, point 3. Les deux phrases concernées ici,
« Elles sont toutes les deux à l'Actif du Bilan » et « L'entreprise ne détient ni plus ni moins
qu'avant », ont été rejouées pour cette raison.""")

# ─── application ─────────────────────────────────────────────────────────────
def maj(cle, etat, detail):
    global s
    pat = re.compile(r'<tr><td class="cle">' + re.escape(cle) +
                     r'</td><td>.*?</td><td>.*?</td></tr>', re.S)
    new = (f'<tr><td class="cle">{cle}</td><td>{etat}</td><td>'
           + ' '.join(detail.split()) + '</td></tr>')
    if pat.search(s):
        s = pat.sub(lambda m: new, s, count=1)
    else:                       # ligne nouvelle : les objets de la passe viennent
        anc = INSERT[0]         # en tête, juste après « Volume du texte »
        assert anc in s, f'ancre absente pour insérer « {cle} »'
        s = s.replace(anc, anc + '\n' + new, 1)
        INSERT[0] = new

INSERT = [None]
ORDRE = ['Volume du texte', 'Budget de deux-points', 'Les cinq deux-points conservés',
         'Précision', 'Les trois autres entrées du registre', 'Rejeu du journal',
         'Paragraphes scindés', 'Un parallèle rétabli', 'Registre des écarts',
         'Incises', 'Candidats à la charte, non portés', 'Production du fichier']
for cle in ORDRE:
    maj(cle, *ROWS[cle])
    if cle == 'Volume du texte':
        import re as _re
        INSERT[0] = _re.search(r'<tr><td class="cle">Volume du texte</td>.*?</tr>',
                               s, _re.S).group(0)

# la ligne de relecture profane gagne la mention de la passe
s = s.replace('<td class="cle">Relecture profane</td><td>FAITE — 5 TOURS</td>',
              '<td class="cle">Relecture profane</td><td>FAITE — 5 TOURS + PASSE</td>')

# le décompte des paragraphes du premier sous-titre a changé
s = s.replace('Le nom apparaît quatre fois dans les cinq paragraphes du premier sous-titre',
              'Le nom apparaît quatre fois dans le premier sous-titre, désormais scindé en deux '
              'paragraphes de tête et cinq de développement')

# ─── typographie du PDF : insécables dans les guillemets de l'annexe ────────
# L'annexe ne sort jamais du PDF ; le corps garde ses espaces ordinaires, la
# charte, section 11, réservant l'insécable aux sommes et laissant le reste au
# CSS de l'application.
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
