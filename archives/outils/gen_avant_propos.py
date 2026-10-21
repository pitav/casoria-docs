#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Écrit le fichier de travail de l'avant-propos du module
« Comprendre la comptabilité sans être comptable ».

Modèle : gen_ch13.py pour le corps, annexe_ch13.py pour l'annexe de contrôle.
Le texte est écrit avec « ~ » partout où un insécable est requis, et la
substitution se fait ici, en une passe (piège 2 du LISEZ-MOI).

Ce n'est pas un chapitre : forme libre, pas de sous-titre, pas de bloc
« Ce que vous avez appris », pas d'écriture, pas de composant. Le gabarit de la
charte, section 2, ne s'y applique donc pas ; le ton, le vocabulaire, la
ponctuation et la typographie, si.

v5 — 27 août 2026, VALIDÉE. Le texte de la v4 est inchangé, au mot près. Ce
qui change ici : le chapo passe en livraison, et l'annexe réduite devient
l'annexe de contrôle complète, en trois colonnes, avec les nombres que
livrer.py recompte.
"""
NB = '\u00a0'
assert NB == chr(160), 'NB doit être un insécable, pas un espace ordinaire'

CORPS = r"""<p class="kicker">Casoria • Comprendre la comptabilité • Avant-propos</p>
<h1>Comprendre la comptabilité sans être comptable</h1>

<p class="accroche">Bienvenue dans ce module. En treize chapitres et un peu plus de six heures, vous allez
apprendre à lire les deux documents principaux qui résument la vie d'une entreprise, le Bilan et le Compte
de Résultat, et à comprendre comment ils se remplissent. Savoir les lire change ce que vous pouvez
décider. C'est ce qui permet de dire si une entreprise gagne de l'argent, si elle peut payer ce qu'elle
doit, et si elle passera l'année~— la vôtre comme celle d'un client, d'un fournisseur ou d'une société que
votre banque va financer.</p>

<p>La façon d'y arriver est spécifique à la pédagogie de Casoria~: Simulez, Visualisez, Comprenez. Ce
module ne pose pas une définition, puis un exemple qui l'illustre. Vous allez remplir ces deux documents
sur une année entière d'entreprise, et enregistrer vous-même les opérations qui vous apprennent quelque
chose. Les autres opérations, comme les centaines de factures d'une année ordinaire, l'application s'en
charge. Chaque enregistrement arrive au moment où vous venez de comprendre pourquoi il a lieu.</p>

<p>Pour cela, vous allez suivre l'entreprise Latitude Café, qui torréfie du café et le vend en sachets.
Elle naît le 5~janvier 2026, elle achète, vend, emprunte, s'équipe, embauche, se trompe une fois sur une
livraison, et le 31~décembre elle arrête ses comptes. Chaque notion arrive au moment où une situation la
rend nécessaire, jamais avant.</p>

<p>À la fin de ce module, c'est ce que vous vous direz.</p>

<p class="declaration">«~Je comprends enfin ce que je regarde quand j'ai les comptes d'une entreprise sous
les yeux.~»</p>

<p>Ouvrez le premier chapitre. Les deux documents vous y attendent.</p>
"""

CHAPO = r"""<p class="chapo"><strong>Avant-propos du module, v5, livré.</strong> Rédigé le 27~août 2026,
après la livraison des treize chapitres, et validé le jour même au quatrième tour de relecture.
<strong>Le texte est celui de la v4, au mot près~</strong>: cette version ne change que le chapo et
l'annexe, qui passe en annexe de contrôle complète. <strong>[[MOTS]]~mots.</strong> Forme libre, ni
sous-titre, ni bloc «~Ce que vous avez appris~», ni écriture, ni composant, ni illustration. Un
deux-points en prose, un tiret cadratin. <strong>Deux décisions de cette relecture sortent du
texte~</strong>: «~Simulez, Visualisez, Comprenez~» va à la charte, et la clause du terme nommé avant son
chapitre va au déroulé. Ce fichier est le fichier de travail~: il porte le chapo et l'annexe, que le
fichier de livraison ne porte pas.</p>"""

# ═══════════════════════════════════════════════════════════════════════════
#  Annexe de contrôle complète — gabarit d'annexe_ch13.py, trois colonnes
# ═══════════════════════════════════════════════════════════════════════════
_TITRE = 'Annexe de contrôle'
_INTRO = (
    "Annexe de contrôle complète, produite à la livraison. Elle reste détaillée, y compris sur les "
    "arbitrages écartés~: c'est elle qui permet de revérifier ce texte plus tard, et c'est le seul "
    "endroit où le raisonnement d'un texte hors gabarit est écrit. Les premières lignes portent ce qui a "
    "été décidé pendant les quatre tours de relecture~; les dernières portent les contrôles. Charte, "
    "section 22.")

ROWS = [

('Nature du texte', 'HORS GABARIT — DÉCLARÉ', """
<strong>Ce n'est pas un chapitre, et le gabarit de la charte, section 2, ne s'y applique pas.</strong> Ni
sous-titre, ni bloc «~Ce que vous avez appris~», ni écriture, ni composant, ni illustration, ni quiz. Ce
qui s'y applique et qui a été vérifié~: l'adresse et la personne (section 5), le point de vue narratif
(section 6), le marquage typographique (section 9), la ponctuation et le budget de deux-points
(section 10), les conventions d'écriture (section 11), les interdits (section 12).
<strong>Conséquence sur les contrôles~:</strong> deux cases de
<code>controle_checklist.py</code> lèvent et ne se corrigent pas — «~deux à trois sous-titres~» et
«~le bloc de clôture porte trois points~». Elles supposent le gabarit d'un chapitre. Aucune autre ne lève.
<strong>Le fichier vit dans le dossier comme un chapitre</strong>, avec son fichier de travail, son
livrable et ses PDF.""" ),

('Ce que le texte est devenu, en quatre tours', 'v1 545 → v5 [[MOTS]]', """
<strong>La v1 et la v2 n'étaient pas le bon texte</strong>, et c'est le principal enseignement de la
séance. Elles répondaient à cinq points demandés — pourquoi, le thème, pour qui, l'angle pédagogique,
comment — et s'adressaient à quelqu'un qui n'a pas encore choisi le module. C'est le travail de la page de
vente, pas celui de l'écran d'ouverture~: celui qui lit un avant-propos a déjà choisi.
<strong>Le décideur l'a formulé en relisant la v2~:</strong> «~ce texte se rapproche plus du texte de
promo qui sera affiché dans la page de vente~». <strong>Les PDF des v1 et v2 restent déposés</strong> et
servent de matière à cette page.
<strong>La v3 a changé de nature</strong> — un mot d'accueil de 243~mots, ouvrant sur «~Bienvenue~» — et
la v4 l'a corrigée en huit points, dont six formulations écrites par le décideur et reprises telles
quelles. <strong>La v5 ne touche pas au texte de la v4.</strong>""" ),

('Le motif, à la fin du premier paragraphe', 'DEMANDÉ — ARBITRÉ, À VÉRIFIER', """
<strong>Demandé en relecture de la v3~:</strong> «~il manque l'explication du pourquoi c'est important de
savoir lire ces deux documents~». <strong>Écrit en nommant trois questions plutôt qu'en affirmant que
c'est important~:</strong> l'entreprise gagne-t-elle de l'argent, peut-elle payer ce qu'elle doit,
passera-t-elle l'année. Une affirmation d'importance ne se vérifie pas~; une question que le lecteur se
pose déjà, si.
<strong>À vérifier, et c'est le seul point que cette livraison laisse ouvert~:</strong> ces trois questions
engagent la fin du module. La première et la troisième sont tenues par le Chapitre~12 et ses trois
ratios~; la deuxième l'est par le Chapitre~11 et par le besoin en fonds de roulement du 12. Si l'une des
trois n'est pas tenue, c'est ici qu'on la retire.
<strong>Il coûte une quarantaine de mots</strong>, et c'est ce qui explique l'écart entre les 250 visés et
les [[MOTS]] livrés. Les suppressions demandées au même tour en rendent une dizaine.""" ),

('«~Simulez, Visualisez, Comprenez~»', 'DÉCIDÉ — VA À LA CHARTE', """
<strong>Donné par le décideur en relecture de la v3</strong>, et confirmé avec son motif à la v5.
<strong>La formule initiale était «~Simulez, Visualisez, Apprenez autrement~»</strong>, et elle est
écartée pour trois raisons, les siennes~: elle est moins dynamique, elle est trop neutre, et
«~apprendre autrement~» ne dit pas grand-chose. <strong>Ce que veut le lecteur, c'est comprendre</strong>,
et le troisième verbe doit donc porter la promesse du module. <strong>«~Autrement~» est de surcroît déjà
contenu dans «~Simulez, Visualisez~»</strong>, qui dit en quoi consiste la différence au lieu de
l'annoncer.
<strong>Ce n'est pas une tournure de ce texte, c'est la signature de la marque~:</strong> elle vaut pour
les modules suivants, et elle est portée à la charte, section 1, à côté de la promesse dont elle est la
forme courte.
<strong>Elle consomme le seul deux-points que ce texte peut porter</strong>, une seule section étant
comptée. C'est un bon emploi du signe, l'énumération après annonce que le tableau de la section 10
reconnaît. Rien d'autre n'en porte, et rien ne doit en porter tant que la triade est là.""" ),

('Le Bilan et le Compte de Résultat sont nommés', 'DÉCIDÉ — VA AU DÉROULÉ', """
<strong>Décidé en relecture de la v1</strong>, contre l'arbitrage du rédacteur. <strong>Motif du
décideur~:</strong> les deux noms sont employés de manière générique et sans explication, et ils plantent
le décor. <strong>La v1 les évitait</strong> au nom du lexique cumulatif du déroulé, section 11, «~aucun
terme ne doit être employé avant son chapitre~», et parce que l'accroche du Chapitre~1 tient sa
révélation sur «~Il s'appelle le Bilan~». Elle écrivait «~deux documents d'une page~» et «~les deux
colonnes du premier~».
<strong>La règle se reformule, et c'est ce qui part au déroulé~:</strong> elle vise l'emploi qui définit,
ou qui suppose la définition acquise, et non la mention qui pose le sujet.
<strong>Effet de bord, et il compte~:</strong> le mot «~Bilan~» capitalisé dans le texte a obligé à
réécrire la fin de la v1, qui disait «~le bilan d'une petite entreprise ordinaire~», minuscule et
générique. Les deux graphies se seraient touchées à deux lignes d'intervalle, ce que la charte,
section 9, veut précisément éviter. <strong>Autoriser un terme, c'est s'obliger à sa graphie
partout.</strong>""" ),

('«~écriture~» reste dehors', 'CONFORME', """
<strong>Le terme appartient au Chapitre~3, et la décision prise sur les deux documents ne le couvre
pas~:</strong> il ne planterait aucun décor, il demanderait une explication. C'est le test qui sépare les
deux emplois, et il est écrit au déroulé avec la clause.
<strong>Le texte écrit «~opération après opération~» puis «~enregistrer vous-même les
opérations~».</strong> «~Enregistrer~» entre dans le vocabulaire des textes par une correction du
décideur, et il est cohérent avec ce que l'apprenant lit à l'écran, «~Enregistré automatiquement~».""" ),

('La promesse, affichée en direct', 'DEMANDÉ — APPLIQUÉ', """
<strong>La v3 finissait sur une déclaration qui tombait de nulle part~:</strong> «~Aucune connaissance
préalable n'est nécessaire, et vous ne sortirez pas d'ici comptable~». Le décideur l'a lue «~comme un
cheveu dans la soupe~» — elle répondait à une objection que le texte n'avait pas posée. <strong>Sur un
texte court, chaque phrase doit être appelée par la précédente</strong>, et c'est une attestation de la
famille de la charte, section 12, sur la réponse donnée à une question non posée.
<strong>La promesse est désormais la déclaration en gras du texte</strong>, une phrase autonome entre
guillemets, et non plus une citation rapportée. Une seule déclaration, comme dans un chapitre
(section 9). <strong>La ligne qui la précède, «~À la fin de ce module, c'est ce que vous vous direz~»,
est le minimum qui l'attribue~</strong>: sans elle, le lecteur ne sait pas qui parle.
<strong>Arbitrage écarté, et il peut revenir~:</strong> cette ligne saute si l'écran met la citation en
évidence par sa mise en page. C'est alors la mise en page qui fait le travail, et il faut le vérifier
avant de la retirer. <strong>La moitié négative de la promesse — «~je connais la comptabilité~» — n'est
pas citée~:</strong> à ce volume, les deux moitiés ne tenaient pas.""" ),

('La métaphore du jeu', 'RETIRÉE PAR LE DÉCIDEUR', """
<strong>La v3 écrivait «~Chaque ligne y est une case à allumer, et chaque case s'allume au moment où vous
venez de comprendre pourquoi~».</strong> C'est la métaphore personnelle du décideur, et il l'a retirée
lui-même~: «~ça ne veut pas dire grand-chose lâché comme ça~». Elle vit dans sa tête et dans l'écran, pas
dans la prose d'un texte de 250~mots qui n'a pas la place de l'installer.
<strong>La phrase de remplacement garde ce qu'elle visait</strong>, l'ordre entre la compréhension et le
geste~: «~Chaque enregistrement arrive au moment où vous venez de comprendre pourquoi il a lieu~».
<strong>Deux mots ont été ajoutés à la phrase du décideur, «~il a lieu~»~:</strong> un verbe sans
complément est une ellipse de métier (section 12, cinquième famille).""" ),

('Le fil rouge', 'CONFORME', """
<strong>Latitude Café porte son rôle à sa première occurrence</strong>, comme la section 12 l'exige, en
cinq mots — «~qui torréfie du café et le vend en sachets~». La clientèle et le comptoir de l'atelier sont
sortis à la v3~; le Chapitre~1 les donne.
<strong>Le lot non conforme du Chapitre~10 est annoncé en trois mots</strong>, «~se trompe une fois sur
une livraison~», pour que la première année ne paraisse pas sans accroc.
<strong>Aucun nom propre de personne</strong>~: ni Thomas Vasseur, ni Claire Berthier, ni Léa Ferrand. Un
avant-propos n'a pas de quoi porter leur rôle, et la règle du nom propre l'exigerait.
<strong>Le «~vous~» désigne l'apprenant partout</strong>, jamais le dirigeant de Latitude Café
(section 6). Le test de l'annexe A a été repassé sur les quatre paragraphes~: aucune occurrence
ambiguë.""" ),

('Budget de deux-points', '0 → 1', """
<strong>Notation~: premier jet → état livré.</strong> Les v1, v2 et v3 n'en portaient aucun. Le seul
deux-points du texte est celui de la triade, entré à la v4 par décision, et il est expliqué à la ligne qui
lui est consacrée.
<strong>Le texte ne compte qu'une section</strong>, l'accroche, faute de sous-titre~; le budget de la
charte, section 10, en autorise donc un seul et il est consommé. <strong>Conséquence pour toute reprise
future~: aucune phrase ajoutée à ce texte ne peut porter de deux-points</strong> tant que la triade y est.
<strong>Un tiret cadratin</strong>, en chute du premier paragraphe, sur «~la vôtre comme celle d'un
client~». La charte en autorise un de chute. Il est précédé d'un insécable, pour qu'il ne tombe jamais en
tête de ligne.""" ),

('Volume du texte', 'HORS SEUIL DE CHAPITRE — [[MOTS]]', """
<strong>[[MOTS]]~mots au périmètre déclaré, [[MOTS_ST]] avec les sous-titres</strong>, le texte n'en
portant aucun. <strong>Le seuil de 680 de la charte, section 19, ne s'applique pas~:</strong> il vise un
chapitre, qui doit installer des notions. La cible de ce texte a été fixée par le décideur, à 550 puis 350
puis 250~mots.
<strong>Les [[MOTS]] livrés dépassent la dernière cible de douze</strong>, et le motif ajouté au premier
paragraphe les explique à lui seul. <strong>Ce que la coupe à 250 a fait sortir</strong>, et qui rentrerait
pour une trentaine de mots si le besoin s'en faisait sentir~: le vocabulaire jamais remplacé par un
équivalent plus doux, les exercices qui font prendre position avant l'explication, la nature des questions
posées — reconnaître et situer, jamais restituer — et le détail du bilan final.
<strong>Ce qui a été gardé contre tout cela~:</strong> rien du fil conducteur n'est resté. Les deux
questions du module — où est l'argent et d'où vient-il, qu'est-ce que l'activité a consommé et gagné — sont
sorties à la v4 avec le changement de nature. <strong>Elles sont au Chapitre~1</strong>, qui les pose et
les tient, et un mot d'accueil qui les récite les use avant leur chapitre.""" ),

('Écritures', 'AUCUNE — 0 LIGNES', """
<strong>Aucune écriture, ni manuelle ni automatique</strong>, et c'est normal~: le texte précède le
Chapitre~1 et le lecteur n'a encore rien vu de la simulation. <strong>Aucun composant, aucune
illustration, aucune précision, aucun <code>&lt;UAlert&gt;</code>.</strong> Le texte n'appelle aucune
classe de <code>casoria.css</code> qui n'y soit déjà~: <code>kicker</code>, <code>chapo</code>,
<code>accroche</code>, <code>declaration</code> et <code>saut</code>.
<strong>Rien n'est donc à ajouter à la feuille de style</strong>, et rien du scénario chiffré n'est
touché. Le total de contrôle du module est inchangé.""" ),

('Vocabulaire et marquage', 'CONFORMES', """
<strong>Vocabulaire de fabrication — vérifié par <code>verif_ch13.py</code> et à la main~:</strong> ni
«~grille~», ni «~bloc~», ni «~exploitation~», ni «~poste~», ni «~parcours~», ni «~lexique~», ni
«~aside~», ni «~nombre~» au sens d'un montant. «~Module~» est employé, et c'est le mot que huit des treize
chapitres livrés emploient déjà.
<strong>Vigilances du module~:</strong> «~clôture~» et «~encaisser~» sont évités, le texte écrivant
«~elle arrête ses comptes~». «~Dépense~», «~recette~», «~s'éteindre~» et «~toucher~» sont absents.
<strong>Mots interdits de la section 12~:</strong> aucun.
<strong>Capitales~:</strong> Bilan et Compte de Résultat portent la leur à chacune de leurs occurrences,
et aucun bilan minuscule ne subsiste. Actif et Passif ne sont pas employés.
<strong>Gras~:</strong> une seule déclaration, et elle ne porte aucun terme du lexique. <strong>Aucune
couleur de lexique~:</strong> le texte précède le Chapitre~1, et la couleur dit «~défini ici~», ce qui
serait faux partout dans ce texte.""" ),

('Checklist de relecture', '22 CASES APPLICABLES — 20 CONFORMES, 2 SANS OBJET', """
<strong>Passée par <code>controle_checklist.py</code>.</strong> Vingt cases conformes. Les deux qui lèvent
sont sans objet sur un texte hors gabarit~: «~deux à trois sous-titres~» et «~le bloc de clôture porte
trois points~».
<strong>Le faux positif connu sur «~bilan~» en minuscules ne lève plus~:</strong> la fin de la v1 qui le
produisait a été réécrite. C'est le premier texte du module où cette case passe sans réserve.
<strong><code>verif_ch13.py</code> ne lève rien</strong> sur ses cinq contrôles. Deux pièges de ce script,
consignés pour la prochaine fois~: il lit le fichier entier, annexe comprise, et il a donné «~vocabulaire~»
en candidat au vocabulaire de fabrication alors que le mot n'est que dans l'annexe~; et il ouvre le déroulé
sous son nom de version en dur.""" ),

('Les quatre contrôles de livrer.py', 'CONFORMES', """
<strong>Budget de deux-points~:</strong> la seule section comptée en porte un, et pas deux.
<strong>Nombres annoncés~:</strong> les mots au périmètre, les mots avec les sous-titres, le budget et les
lignes d'écriture sont relus dans cette annexe et concordent — [[MOTS]]~mots au périmètre, [[MOTS_ST]]
avec les sous-titres, 1 deux-points en prose, 0~LIGNES d'écriture manuelle.
<strong>Typographie des sommes~:</strong> sans objet, le texte n'en porte aucune. Les insécables du texte
portent sur les dates et sur les guillemets.
<strong>Même texte au caractère près</strong> entre le fichier de travail et le livrable.""" ),

('Production du fichier', 'CONFORME', """
<strong><code>outils/gen_avant_propos.py</code> écrit le fichier de travail</strong>, texte, chapo et
annexe, sur le modèle de <code>gen_ch13.py</code> et d'<code>annexe_ch13.py</code>. Les insécables sont
posés en une passe, par substitution d'un caractère marqueur, et l'assertion sur <code>NB</code> garde
le piège 2 du
LISEZ-MOI — l'outil d'écriture de fichier convertit un insécable littéral en espace ordinaire.
<strong>Le script recompte lui-même les mots qu'il annonce</strong>, au périmètre de
<code>compter.py</code>, et les écrit au chapo et à l'annexe. Sur un texte repris cinq fois en une séance,
un nombre annoncé à la main est faux dès la première coupe~: c'est la règle du nombre annoncé, appliquée
à la source plutôt qu'au contrôle.
<strong>Le livrable est dérivé par <code>livrer.py</code></strong>, et les PDF par
<code>pdf_relecture.py</code> pour la relecture, par WeasyPrint sur <code>pdf-livraison.html</code> pour la
livraison. Les PDF sont relus en images.""" ),

]

# ═══════════════════════════════════════════════════════════════════════════
#  Assemblage
# ═══════════════════════════════════════════════════════════════════════════
import re
from bs4 import BeautifulSoup

_c = BeautifulSoup(CORPS.replace('~', NB), 'html.parser')
MOT = r"[A-Za-zÀ-ÿ0-9]+(?:[’'\-][A-Za-zÀ-ÿ0-9]+)*"
MOTS = sum(len(re.findall(MOT, p.get_text(' ', strip=True)))
           for p in _c.find_all('p')
           if not (set(p.get('class') or []) & {'kicker'}))
MOTS_ST = MOTS + sum(len(re.findall(MOT, h.get_text(' ', strip=True)))
                     for h in _c.find_all('h2'))

TETE = f"""<h2 class="saut">{_TITRE}</h2>
<p>{_INTRO}</p>
<table>
<thead><tr><th>Point</th><th>État</th><th>Détail</th></tr></thead>
<tbody>
"""
annexe = TETE + ''.join(
    f'<tr><td class="cle">{cle}</td><td>{etat}</td><td>' + ' '.join(detail.split()) + '</td></tr>\n'
    for cle, etat, detail in ROWS) + '</tbody>\n</table>\n'

out = CORPS + '\n' + annexe
out = out.replace('<h1>Comprendre la comptabilité sans être comptable</h1>',
                  '<h1>Comprendre la comptabilité sans être comptable</h1>\n' + CHAPO, 1)
out = out.replace('[[MOTS_ST]]', str(MOTS_ST)).replace('[[MOTS]]', str(MOTS))
out = out.replace('~', NB)
out = re.sub(r'«\s+', '«' + NB, out)
out = re.sub(r'\s+»', NB + '»', out)

assert '<p class="chapo">' in out
assert '<h2 class="saut">' in out
assert '[[' not in out
assert '~' not in out
open('avant-propos-travail.html', 'w', encoding='utf-8').write(out)
print('écrit : avant-propos-travail.html —', len(out), 'caractères,',
      out.count(NB), 'insécables,', MOTS, 'mots,', len(ROWS), "lignes d'annexe")
