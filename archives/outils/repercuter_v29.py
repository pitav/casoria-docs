#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reporte au déroulé la passe de clarification du texte (v28 → v29).

La passe du 13 octobre 2026 a été faite dans les pages .vue de l'application :
titres à l'écran, renvois par titre, alertes et précisions retouchées, deux mots
au glossaire, deux illustrations déplacées. Cette version reporte ce qui touche
une décision du déroulé, écrit le rôle des vidéos et la correspondance des
numérotations, et pose à la section 14 les quatre points où la passe contredit
une décision antérieure. Aucune écriture ne bouge.

Chaque substitution est assertée unique. Le fichier est écrit à la toute fin.
Règle 1 : le bloc « Changements » de la v28 saute. Règle 2 : pas de numéro de
version dans un renvoi interne.
"""
import re

DER_IN = 'deroule-comprendre-la-comptabilite-v28.corps.html'
DER_OUT = 'deroule-comprendre-la-comptabilite-v29.corps.html'


class Doc:
    def __init__(self, path):
        self.s = open(path, encoding='utf-8').read()
        self.n = 0

    def rep(self, old, new, label, n=1):
        c = self.s.count(old)
        assert c == n, f'{label} : {c} occurrence(s), {n} attendue(s)'
        self.s = self.s.replace(old, new, n)
        self.n += 1

    def rep_s(self, old, new, label):
        motif = r'(?:\s|&nbsp;)+'.join(re.escape(p) for p in old.split())
        m = list(re.finditer(motif, self.s))
        assert len(m) == 1, f'{label} : {len(m)} occurrence(s), 1 attendue'
        a, b = m[0].span()
        self.s = self.s[:a] + new + self.s[b:]
        self.n += 1

    def rep_bloc(self, debut, fin, new, label):
        assert self.s.count(debut) == 1, f'{label} : début non unique'
        i = self.s.find(debut)
        j = self.s.find(fin, i)
        assert j >= 0, f'{label} : fin introuvable'
        self.s = self.s[:i] + new + self.s[j + len(fin):]
        self.n += 1

    def compte(self, motif, n, label):
        c = self.s.count(motif)
        assert c == n, f'{label} : {c} occurrence(s) de « {motif} », {n} attendue(s)'

    def write(self, path):
        open(path, 'w', encoding='utf-8').write(self.s)
        print(f'   {path} — {self.n} substitutions, {len(self.s)} caractères')


d = Doc(DER_IN)

# ═══════════════════════════════════════════════════════════════════════════
#  EN-TÊTE
# ═══════════════════════════════════════════════════════════════════════════
d.rep('<p class="kicker">Casoria • Document de référence • v28</p>',
      '<p class="kicker">Casoria • Document de référence • v29</p>', 'kicker')

d.rep_bloc('<p class="chapo">Déroulé annoté', '</p>', """<p class="chapo">Déroulé annoté de la formation. Treize chapitres, un exercice complet
simulé de la création à la clôture, sur le fil rouge d'une PME fictive. <strong>Cette v29 reporte la passe
de clarification du texte</strong>, faite le 13&nbsp;octobre 2026 dans les pages de l'application&nbsp;:
titres à l'écran, renvois entre chapitres, alertes et précisions retouchées, deux mots de plus au lexique. Elle
écrit le rôle des vidéos d'ouverture, et la correspondance entre la numérotation de ce document et celle de
l'application. <strong>Aucune écriture ne bouge</strong>&nbsp;: le total de contrôle du module reste à
1&nbsp;294&nbsp;694,00&nbsp;€ au débit comme au crédit, et le Bilan de l'exercice sur 130&nbsp;410&nbsp;€. La
charte reste en v16.</p>""", 'chapo')

d.rep('<tr><td class="cle">Format</td><td>13 chapitres numérotés de 1 à 13 — séance unique, ou 4 séances fractionnées</td></tr>',
      """<tr><td class="cle">Format</td><td>13 chapitres numérotés de 1 à 13, précédés d'une introduction — séance
unique, ou 4 séances fractionnées. L'application compte l'introduction comme premier chapitre&nbsp;: le
Chapitre N de ce document y est le N+1 sur 14 (section 10).</td></tr>""", 'format')

d.rep_s("""La charte est inchangée, et tous les renvois faits d'ici restent valides.</td></tr>""",
        """La charte est inchangée, et tous les renvois faits d'ici restent valides. Deux règles
nées de la passe de clarification valent pour tous les modules et l'attendent (section 14).</td></tr>""",
        'documents liés')

# ═══════════════════════════════════════════════════════════════════════════
#  CHANGEMENTS — le bloc v28 saute (règle 1)
# ═══════════════════════════════════════════════════════════════════════════
d.rep_bloc('<h2>Changements v28</h2>', '<h2 class="saut">1 — Le fil rouge', """<h2>Changements v29</h2>
<p>Le 13&nbsp;octobre 2026, le texte des quatorze pages et de la liste des cas écartés a été repris dans
l'application, sur le retour de lecteurs de confiance&nbsp;: module bien reçu, texte parfois alambiqué,
renvois peu clairs aux chapitres précédents. Cette version reporte ce que la passe change dans ce que le
déroulé décide. <strong>Rien de ce qui suit ne touche une écriture ni un montant.</strong></p>
<ul>
<li><strong>Le texte vu par l'apprenant ne nomme plus aucun chapitre par son numéro.</strong> Il renvoie
par le titre, en italique, par la notion ou par le moment de l'année. Les autres règles de la passe sont
écrites avec celle-ci à la section 12, la correspondance des numéros et des titres à la section 10.</li>
<li><strong>Quatre titres changent de nom dans ce document</strong>, alignés sur l'écran&nbsp;:
<em>Naissance de l'entreprise</em>, <em>Fin de l'exercice</em>, <em>Clôture de l'exercice</em>, et
<em>Décider avec trois chiffres</em>, qui remplace «&nbsp;Piloter&nbsp;» parce que le besoin en fonds de
roulement est une somme et non un ratio. Sections 9 et 10.</li>
<li><strong>Le recensement des alertes suit l'application</strong>&nbsp;: deux alertes de plus, les
documents allégés au Chapitre 1 et le débit du relevé bancaire au Chapitre 2, et celles des Chapitres 7, 8,
10 et 11 réécrites. Section 6 et fiches. La fiche du Chapitre 8 portait encore «&nbsp;presque au centime
près&nbsp;», la formulation que le recensement interdit.</li>
<li><strong>Une créance douteuse se déprécie, elle ne se provisionne pas.</strong> Le Chapitre 10 ne cite
plus les créances parmi les usages d'une provision, et la liste des cas écartés traite la dépréciation à
part. Sections 6, 10 et 12.</li>
<li><strong>Deux mots entrent au lexique</strong>, crédit de TVA au Chapitre 5 et reprise de provision au
Chapitre 10, déjà au glossaire de l'application. <strong>Le besoin en fonds de roulement est désormais
nommé avant son sigle</strong>, comme la SAS et l'IS. Section 11.</li>
<li><strong>Deux illustrations ont changé de place</strong>, chacune présentée désormais par une
phrase&nbsp;: le brut et le net après la valeur nette comptable, au Chapitre 8&nbsp;; l'argent au
31&nbsp;décembre juste après la définition du besoin en fonds de roulement, au Chapitre 12. La légende du
Chapitre 12 qui disait le stock plus lourd que la trésorerie a disparu, et le point est fermé.</li>
<li><strong>Le rôle des vidéos d'ouverture est écrit</strong> à la section 9, et le point ouvert de la
section 14 est réduit à ce qui reste à faire.</li>
<li><strong>La suite du parcours ne nomme aucun module</strong>&nbsp;: fiches des Chapitres 12 et 13.</li>
<li><strong>Quatre retouches de la passe contredisent une décision antérieure.</strong> Elles sont posées à
la section 14, pas tranchées ici.</li>
</ul>

<h2 class="saut">1 — Le fil rouge""", 'changements')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 6 — ALERTES ET PRÉCISIONS
# ═══════════════════════════════════════════════════════════════════════════
d.rep_s("""Placement : après le dernier sous-titre,
avant le panneau automatique.</p>""", """Placement : après le dernier sous-titre,
avant le panneau automatique. Une exception, au Chapitre 2&nbsp;: l'alerte du relevé bancaire se place là où
l'objection naît, juste après la définition de débit et crédit.</p>""", 's6 placement')

d.rep_bloc('<tr><td class="ch">2</td><td class="cle">Le Bilan va cesser de s\'équilibrer</td>', '</tr>',
           """<tr><td class="ch">1</td><td class="cle">Deux documents allégés</td><td>Le Bilan et le Compte de Résultat du module sont volontairement allégés&nbsp;: un Bilan réel porte davantage de lignes, et celles qui restent sont celles que Latitude Café utilise vraiment. C'était la dernière phrase du corps, «&nbsp;Un dernier mot, et un seul&nbsp;»&nbsp;; la passe de clarification en a fait une alerte.</td></tr>
<tr><td class="ch">2</td><td class="cle">Le débit du relevé bancaire</td><td>Sur un relevé, «&nbsp;débit&nbsp;» désigne l'argent qui sort, parce que le relevé est écrit du point de vue de la banque. Vu de l'entreprise, un débit sur le compte en banque est de l'argent qui entre, et l'image ne vaut que pour la trésorerie. C'est la phrase de désamorçage que la fiche demandait, sortie du corps à la passe de clarification.</td></tr>
<tr><td class="ch">2</td><td class="cle">Le Bilan va cesser de s'équilibrer</td><td>Au terme des quatre écritures du chapitre, les deux totaux sont égaux. Ils cesseront de l'être dès les premières ventes et les premiers achats, et ne redeviendront égaux qu'au Chapitre 11, parce que le résultat de l'année ne se calcule qu'à la fin. L'alerte annonce, elle ne constate pas. Ce ne sera pas une erreur de saisie. Le mot «&nbsp;clôture&nbsp;» y était proscrit, appartenant au Chapitre 10&nbsp;; depuis la passe, l'alerte renvoie à la <em>Clôture de l'exercice</em> par son titre. À trancher, section 14.</td></tr>""",
           's6 ch1-2')

d.rep_s("""Formulation imposée : ne pas écrire « tableau d'amortissement ».</td></tr>""",
        """Formulation imposée : ne pas écrire « tableau d'amortissement ». L'alerte signale aussi le
regroupement des ventes et des achats du deuxième trimestre en une écriture automatique.</td></tr>""", 's6 ch7')

d.rep_bloc('<tr><td class="ch">8</td><td class="cle">Financement ajusté, colonne unique</td>', '</tr>',
           """<tr><td class="ch">8</td><td class="cle">Financement ajusté</td><td>Les 35&nbsp;000&nbsp;€ prêtés le 1<sup>er</sup>&nbsp;juin couvrent presque exactement les 36&nbsp;000&nbsp;€ hors taxes de la machine, ce qui n'arrive jamais en pratique&nbsp;: une entreprise apporte une part et emprunte le reste. <em>Formulation imposée : « presque exactement », jamais « au centime près » — l'écart est d'un millier d'euros.</em> La colonne unique d'actif n'y est plus signalée depuis la passe de clarification&nbsp;: l'illustration du brut et du net la montre.</td></tr>""",
           's6 ch8')

d.rep_bloc('<tr><td class="ch">10</td><td class="cle">Une seule provision, et les règlements de l\'année groupés</td>', '</tr>',
           """<tr><td class="ch">10</td><td class="cle">Une seule provision</td><td>Le chapitre ne suit qu'une provision, pour un litige&nbsp;; une entreprise en constitue aussi pour les garanties données à ses clients. <strong>Les créances douteuses n'y figurent plus</strong>&nbsp;: une créance qu'on risque de ne pas encaisser se déprécie, elle ne se provisionne pas (section 12). Le regroupement des opérations du dernier trimestre est dit par la légende du panneau automatique, et non plus par l'alerte.</td></tr>""",
           's6 ch10')

d.rep("dans l'ordre où le module les allume", "dans l'ordre où le module les remplit", 's6 précision 1')

d.rep_bloc('La dernière phrase de la formulation', "d'un clic.",
           """La thèse du sous-titre est restée au corps</strong> et n'est pas dans la note. Depuis la passe de
clarification, elle s'écrit «&nbsp;La question posée au tout début, devant deux pages vides, s'y pose de la
même façon&nbsp;: où est l'argent, et d'où vient-il&nbsp;?&nbsp;», et elle porte trop pour dépendre
d'un clic.""", 's6 précision 13')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 9 — VUE D'ENSEMBLE, ET LES VIDÉOS
# ═══════════════════════════════════════════════════════════════════════════
d.rep("<td>Avant-propos — mot d'accueil, hors gabarit et hors compte</td>",
      "<td>Introduction — mot d'accueil, hors gabarit. Sans numéro ici, premier des quatorze chapitres dans l'application («&nbsp;1/14&nbsp;»)</td>",
      's9 intro')
d.rep("<td class=\"ch\">2</td><td>Naître en tant qu'entreprise</td>",
      "<td class=\"ch\">2</td><td>Naissance de l'entreprise</td>", 's9 ch2')
d.rep("<td>Fin d'exercice</td>", "<td>Fin de l'exercice</td>", 's9 ch10')
d.rep("<td>La clôture (avec l'impôt sur les sociétés)</td>",
      "<td>Clôture de l'exercice (avec l'impôt sur les sociétés)</td>", 's9 ch11')
d.rep("<td>Piloter : la décision et les 3 ratios</td>", "<td>Décider avec trois chiffres</td>", 's9 ch12')

d.rep_s("""Les coupes sont placées à des fins de cycle narratif, jamais au milieu d'une notion.</p>""",
        """Les coupes sont placées à des fins de cycle narratif, jamais au milieu d'une notion.</p>
<div class="note"><span class="t">Les vidéos d'ouverture — rôle décidé le 12&nbsp;octobre 2026</span>
<p>Chaque chapitre s'ouvre sur une vidéo qui enseigne les mêmes notions que le texte, mais de manière
générique, sans les détails ni les chiffres de Latitude Café. On peut la regarder seule et comprendre le
cours&nbsp;; le texte et la simulation sont la mise en pratique. Deux angles, pas un doublon. <strong>Le
texte se suffit à lui-même et reste prioritaire</strong>&nbsp;: rien n'en est retiré au motif que la vidéo
le couvre, et chaque accroche fonctionne que la vidéo ait été vue ou non.</p>
<p><strong>Le cahier des charges d'une vidéo est le bloc «&nbsp;Ce que vous avez appris&nbsp;» de son
chapitre</strong>, ni plus ni moins. Promesse honnête aux lecteurs pressés&nbsp;: la vidéo seule fait
comprendre, elle ne fait pas savoir faire. Une vidéo sans chiffres ne casse pas quand un montant bouge.</p>
<p class="legende">Suggéré, non tranché&nbsp;: garder Latitude Café au niveau du récit, montants ronds ou
absents&nbsp;; plafonner la durée tôt, les Chapitres 5 et 10 étant denses.</p></div>""", 's9 vidéos')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 10 — CORRESPONDANCE, PUIS LES FICHES
# ═══════════════════════════════════════════════════════════════════════════
LIGNES = [
    ('—', '1', 'Introduction', 'index.vue'),
    ('1', '2', 'Le Bilan et le Compte de Résultat', 'bilan-et-compte-de-resultat.vue'),
    ('2', '3', "Naissance de l'entreprise", 'naissance-de-l-entreprise.vue'),
    ('3', '4', "Du document à l'écriture", 'du-document-a-l-ecriture.vue'),
    ('4', '5', "Facturé n'est pas encaissé", 'facture-n-est-pas-encaisse.vue'),
    ('5', '6', 'La TVA', 'la-tva.vue'),
    ('6', '7', 'Produire et stocker', 'produire-et-stocker.vue'),
    ('7', '8', 'Se financer', 'se-financer.vue'),
    ('8', '9', 'Investir', 'investir.vue'),
    ('9', '10', 'Les salariés', 'les-salaries.vue'),
    ('10', '11', "Fin de l'exercice", 'fin-de-l-exercice.vue'),
    ('11', '12', "Clôture de l'exercice", 'cloture-de-l-exercice.vue'),
    ('12', '13', 'Décider avec trois chiffres', 'decider-avec-trois-chiffres.vue'),
    ('13', '14', 'Synthèse et feuille de route', 'ce-que-vous-avez-appris.vue'),
]
assert len(LIGNES) == 14
tableau = '\n'.join(
    f'<tr><td class="ch">{a}</td><td class="ch">{b}</td><td>{t}</td><td><code>{f}</code></td></tr>'
    for a, b, t, f in LIGNES)

d.rep_s("""rattachement des blocs manuels. Les règles de rédaction ne figurent pas ici : voir la charte.</p>""",
        """rattachement des blocs manuels. Les règles de rédaction ne figurent pas ici : voir la charte.</p>
<div class="note"><span class="t">Ce document et l'application — numéros, titres, pages</span>
<p>Les fiches gardent la numérotation de ce document, de 1 à 13, et les renvois de la charte et du registre
la suivent. <strong>L'application compte l'introduction comme premier chapitre</strong> et affiche
«&nbsp;N/14&nbsp;»&nbsp;: le Chapitre N d'ici y est le N+1, et la colonne «&nbsp;Ch.&nbsp;» du glossaire
suit l'application. Le texte vu par l'apprenant n'emploie aucun des deux numéros (section 12). Le titre à
l'écran est le <code>titre:</code> de la page, que son <code>&lt;h1&gt;</code> reprend.</p></div>
<table class="serree">
<thead><tr><th class="ch">Ici</th><th class="ch">Appli</th><th>Titre à l'écran</th><th>Page</th></tr></thead>
<tbody>
""" + tableau + """
</tbody>
</table>
<p class="legende">Pages dans <code>app/pages/apprendre/comprendre-la-comptabilite/</code>. Le renommage de
la dernière en <code>synthese-et-feuille-de-route.vue</code> est laissé au décideur.</p>""", 's10 correspondance')

d.rep('<h3 class="saut">Chapitre 2 — Naître en tant qu\'entreprise · 35 min</h3>',
      '<h3 class="saut">Chapitre 2 — Naissance de l\'entreprise · 35 min</h3>', 'h3 ch2')
d.rep('<h3 class="saut">Chapitre 10 — Fin d\'exercice · 30 min</h3>',
      '<h3 class="saut">Chapitre 10 — Fin de l\'exercice · 30 min</h3>', 'h3 ch10')
d.rep('<h3 class="saut">Chapitre 11 — La clôture (avec l\'impôt sur les sociétés) · 35 min</h3>',
      '<h3 class="saut">Chapitre 11 — Clôture de l\'exercice (avec l\'impôt sur les sociétés) · 35 min</h3>', 'h3 ch11')
d.rep('<h3 class="saut">Chapitre 12 — Piloter : la décision et les trois ratios · 30 min</h3>',
      '<h3 class="saut">Chapitre 12 — Décider avec trois chiffres · 30 min</h3>', 'h3 ch12')

# ── Chapitre 2 ──────────────────────────────────────────────────────────────
d.rep_s("""Ici, on tient les comptes du point de vue de l'entreprise.</li>""",
        """Ici, on tient les comptes du point de vue de l'entreprise. <strong>Depuis la passe de
clarification</strong>, cette phrase est sortie du corps pour devenir une alerte, placée juste après la
définition de débit et crédit (section 6).</li>""", 'ch2 relevé')

d.rep_bloc('<div class="alert"><span class="t">UAlert</span><p>Ce soir, les deux totaux du Bilan sont', '</p></div>',
           """<div class="alert"><span class="t">UAlert</span><p>Ce soir, les deux totaux du Bilan sont égaux.
L'Actif affiche 50&nbsp;000&nbsp;€, le Passif aussi. Ils cesseront de l'être dès les premières ventes et les
premiers achats, et ne redeviendront égaux qu'à la <em>Clôture de l'exercice</em>. Entre-temps, il manquera
au Passif le résultat de l'année, qui ne se calcule qu'à la fin. Ce ne sera pas une erreur de saisie, c'est
le déroulement normal d'un exercice.</p></div>""", 'ch2 alerte')

d.rep_s("""l'employer huit chapitres trop tôt sans annonce explicite.""",
        """l'employer huit chapitres trop tôt sans annonce explicite. <strong>La passe de clarification l'y a
remis</strong>, par le titre du Chapitre 11, en renvoi&nbsp;: à trancher, section 14.""", 'ch2 légende clôture')

# ── Chapitre 8 ──────────────────────────────────────────────────────────────
d.rep("""<li>Mention unique de la présentation réelle — brut / amortissements / net — en illustration, avec le même bilan dans les deux formats.</li>""",
      """<li>Mention unique de la présentation réelle — brut / amortissements / net — en illustration, avec le même bilan dans les deux formats. Placée après la valeur nette comptable et présentée par une phrase, «&nbsp;En haut…&nbsp;», «&nbsp;En bas…&nbsp;», depuis la passe de clarification.</li>""",
      'ch8 illustration')

d.rep_bloc('<div class="alert"><span class="t">UAlert</span><p>L\'emprunt couvre le torréfacteur', '</p></div>',
           """<div class="alert"><span class="t">UAlert</span><p>Les 35&nbsp;000&nbsp;€ prêtés le
1<sup>er</sup>&nbsp;juin par la Banque du Centre couvrent presque exactement le prix de la machine,
36&nbsp;000&nbsp;€ hors taxes. Dans la réalité, une entreprise apporte une part et emprunte le reste, et les
deux montants ne tombent jamais aussi juste.</p></div>""", 'ch8 alerte')

# ── Chapitre 10 ─────────────────────────────────────────────────────────────
d.rep_bloc('<div class="alert"><span class="t">UAlert</span><p>Écritures de période regroupées. Une seule provision est',
           '</p></div>', """<div class="alert"><span class="t">UAlert</span><p>Ce chapitre ne suit qu'une provision, pour un
litige. Une entreprise en constitue aussi pour les garanties données à ses clients.</p></div>
<p class="legende">Les créances douteuses en sont sorties à la passe de clarification&nbsp;: une créance
qu'on risque de ne pas encaisser se déprécie, elle ne se provisionne pas (section 12). La liste des cas
écartés, au Chapitre 13, en parle à part.</p>""", 'ch10 alerte')

# ── Chapitre 11 ─────────────────────────────────────────────────────────────
d.rep_s("""le texte et la légende disent tous deux qu'elle se prend « plus tard, quelques mois après ».""",
        """le texte dit qu'elle se prend «&nbsp;quelques mois plus tard&nbsp;», formule resserrée à la passe de
clarification.""", 'ch11 plus tard')

d.rep_bloc('<div class="alert"><span class="t">UAlert</span><p>Pas d\'acomptes trimestriels', '</p></div>',
           """<div class="alert"><span class="t">UAlert</span><p>Ce chapitre simplifie l'impôt sur trois points.
Il est calculé et inscrit en une fois, à la fin de l'année, alors qu'une entreprise en verse des acomptes en
cours de route dès sa deuxième année. Les conditions qui ouvrent le taux de 15&nbsp;% sont supposées remplies.
Et le calcul part du bénéfice que le Compte de Résultat affiche, alors qu'une entreprise le corrige d'abord de
quelques charges que la loi n'admet pas en déduction.</p></div>""", 'ch11 alerte')

# ── Chapitre 12 ─────────────────────────────────────────────────────────────
d.rep("L'aboutissement direct des briques posées aux Chapitres 4 à 6.</li>",
      "L'aboutissement direct des briques posées aux Chapitres 4 à 6. L'illustration de l'argent au 31&nbsp;décembre suit la définition, présentée par une phrase, et précède le composant.</li>",
      'ch12 illustration')
d.rep('<li>Teasing explicite vers la formation dédiée au pilotage.</li>',
      "<li>Une ouverture vers la suite, sans nommer de module&nbsp;: manier les trois chiffres ensemble pour décider «&nbsp;est l'objet d'une formation à part&nbsp;».</li>",
      'ch12 teasing')
d.rep_bloc('<p><strong>Le titre du déroulé est conservé', '</p>',
           """<p><strong>Le titre a changé le 13&nbsp;octobre 2026&nbsp;: «&nbsp;Décider avec trois
chiffres&nbsp;».</strong> L'ancien, «&nbsp;Piloter&nbsp;: la décision et les trois ratios&nbsp;», annonçait trois
ratios dont l'un n'en est pas un — le besoin en fonds de roulement est une somme en euros, pas une division.
Le corps tenait la distinction, ce qui rendait l'ancien titre inoffensif&nbsp;; le nouveau n'a plus besoin du
corps pour être exact. La page a été renommée avec lui.</p>""", 'ch12 titre')

# ── Chapitre 13 ─────────────────────────────────────────────────────────────
d.rep_s("""donner des pistes pour aller plus loin, dont la formation dédiée au pilotage.</p>""",
        """donner des pistes pour aller plus loin, vers «&nbsp;les modules suivants&nbsp;», sans en nommer
aucun.</p>""", 'ch13 objectif')

d.rep_s("""<p><strong>Le lexique de la section 11 est repris tel quel dans le glossaire</strong>, aux consignes de
fabrication près et à deux capitales près.""", """<p><strong>Passe de clarification, 13&nbsp;octobre 2026.</strong> Le titre à l'écran est revenu à
«&nbsp;Synthèse et feuille de route&nbsp;», qui était déjà celui du <code>&lt;h1&gt;</code>&nbsp;:
«&nbsp;Ce que vous avez appris&nbsp;» entrait en collision avec l'encadré du même nom que porte chaque
chapitre. La feuille de route est la seconde moitié de la page, les cas écartés puis la suite du
parcours. La liste des cas écartés a été reprise sans changer d'entrée&nbsp;: renvois par titre, «&nbsp;un
ticket de caisse perdu&nbsp;» au lieu d'une allusion à un fait que le module ne raconte pas, le crédit-bail
nommé et sa charge placée au Compte de Résultat, la créance douteuse dépréciée et comparée à la provision de
<em>Fin de l'exercice</em>, la réserve légale nommée.</p>
<p><strong>Le lexique de la section 11 est repris tel quel dans le glossaire</strong>, aux consignes de
fabrication près et à deux capitales près. Depuis la passe, le glossaire numérote les chapitres comme
l'application, et il porte deux mots de plus, reportés à la section 11.""", 'ch13 passe')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 11 — LEXIQUE
# ═══════════════════════════════════════════════════════════════════════════
d.rep_s("""sert de garde-fou pendant la rédaction et devient le glossaire du Chapitre 13.</p>""",
        """sert de garde-fou pendant la rédaction et devient le glossaire du Chapitre 13. Le glossaire de
l'application numérote les chapitres comme elle&nbsp;: sa colonne «&nbsp;Ch.&nbsp;» vaut celle-ci plus un
(section 10).</p>""", 's11 intro')

d.rep('<tr><td class="cle">TVA à décaisser</td><td class="ch">5</td><td>Différence due à l\'État</td></tr>',
      """<tr><td class="cle">TVA à décaisser</td><td class="ch">5</td><td>Différence due à l'État</td></tr>
<tr><td class="cle">Crédit de TVA</td><td class="ch">5</td><td>Différence due par l'État, quand la TVA payée dépasse la TVA facturée. Entré à la passe de clarification&nbsp;: le corps le nommait sans que le glossaire le porte</td></tr>""",
      's11 crédit de TVA')
d.rep('<tr><td class="cle">Provision</td><td class="ch">10</td><td>Charge anticipée pour un risque probable mais non encore réalisé</td></tr>',
      """<tr><td class="cle">Provision</td><td class="ch">10</td><td>Charge anticipée pour un risque probable mais non encore réalisé</td></tr>
<tr><td class="cle">Reprise de provision</td><td class="ch">10</td><td>Annulation de tout ou partie d'une provision devenue inutile, qui redevient un produit. Entré à la passe de clarification, depuis la précision du chapitre</td></tr>""",
      's11 reprise')

d.rep_bloc('<strong>Le sigle BFR précède le nom complet à la première occurrence</strong>', '</td></tr>',
           """<strong>Le nom complet précède le sigle à la première occurrence</strong>, «&nbsp;le besoin en
fonds de roulement (BFR)&nbsp;», comme pour la SAS au Chapitre 2 et l'IS au Chapitre 11. La livraison
faisait l'inverse, au motif que le lecteur rencontre le sigle avant le nom chez son banquier&nbsp;; la passe
de clarification a aligné le chapitre sur les deux autres (section 14). Ce n'est pas une convention maison, à
la différence de «&nbsp;CCA&nbsp;» et «&nbsp;PCA&nbsp;» que la section 12 refuse</td></tr>""", 's11 BFR')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 12 — LES RÈGLES DE LA PASSE
# ═══════════════════════════════════════════════════════════════════════════
d.rep_s("""ne se déduisent d'aucune règle générale.</p>""", """ne se déduisent d'aucune règle générale.</p>
<div class="note"><span class="t">Le texte vu par l'apprenant — règles de la passe de clarification,
13&nbsp;octobre 2026</span>
<ul>
<li><strong>Aucun «&nbsp;Chapitre N&nbsp;».</strong> Un renvoi se fait par le titre, en italique
(<em>La TVA</em>, <em>Facturé n'est pas encaissé</em>), par la notion, ou par le moment de l'année
(«&nbsp;fin janvier&nbsp;», «&nbsp;le 1<sup>er</sup>&nbsp;juin&nbsp;», «&nbsp;au tout début&nbsp;»). Les
numéros restent permis là où l'apprenant ne les voit pas&nbsp;: commentaires de code, menu de développement,
et ce document.</li>
<li><strong>Un renvoi ne fait pas allusion à un fait jamais raconté.</strong> «&nbsp;Le ticket
perdu&nbsp;» supposait une histoire que le module ne raconte pas.</li>
<li><strong>«&nbsp;Allumer&nbsp;» est banni du texte de l'apprenant</strong>&nbsp;: une case se remplit, une
ligne apparaît. Ce document garde «&nbsp;case allumée&nbsp;» comme mot de conception, aux sections 2 et 4.</li>
<li><strong>Une ligne se nomme par son nom exact</strong>, celui du plan de comptes de l'application
(<code>app/utils/m1/comptes.ts</code>, le même qu'à la section 2)&nbsp;: «&nbsp;une ligne Provisions pour
risques apparaît au Passif&nbsp;», jamais «&nbsp;une ligne s'ouvre&nbsp;».</li>
<li><strong>Un panneau porte en général plusieurs écritures</strong>&nbsp;: «&nbsp;avant de passer ces
écritures&nbsp;», jamais «&nbsp;le bloc&nbsp;». Seul le dernier panneau de la clôture dit «&nbsp;avant de
reporter le résultat&nbsp;». Un panneau automatique dit que ses écritures «&nbsp;s'enregistrent ici d'un
clic, regroupées&nbsp;».</li>
<li><strong>Une créance qu'on risque de ne pas encaisser se déprécie</strong>, elle ne se provisionne pas.
Le module ne cite que les litiges et les garanties données aux clients comme usages d'une provision.</li>
<li><strong>Le <code>&lt;h1&gt;</code> d'une page reprend exactement son <code>titre:</code>.</strong></li>
<li><strong>Un mot nommé dans le texte et absent du glossaire y entre</strong>, sur décision, et la
section 11 le reçoit en même temps.</li>
</ul></div>""", 's12 règles')

# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 14 — POINTS OUVERTS
# ═══════════════════════════════════════════════════════════════════════════
d.rep('<h2>14 — Points encore ouverts</h2>\n<ul>\n', """<h2>14 — Points encore ouverts</h2>
<ul>
<li><strong>Quatre retouches de la passe de clarification contredisent une décision antérieure</strong>, et
ce document ne les tranche pas.
<ol>
<li><strong>Le mot «&nbsp;clôture&nbsp;» au Chapitre 2.</strong> La fiche le proscrit dans l'alerte, huit
chapitres avant sa définition&nbsp;; la passe l'y a remis par le titre du Chapitre 11, «&nbsp;à la
<em>Clôture de l'exercice</em>&nbsp;». C'est une mention et non un emploi qui définit, au sens de la
section 11, mais le mot est à l'écran. Garder le titre, ou écrire «&nbsp;qu'à la toute fin de l'année&nbsp;».</li>
<li><strong>L'ordre du sigle BFR.</strong> La livraison mettait le sigle d'abord, motif écrit&nbsp;; la passe
a mis le nom d'abord, comme la SAS et l'IS. La section 11 suit l'application en attendant.</li>
<li><strong>Les capitaux propres au Chapitre 12</strong> sont dits «&nbsp;vus dans <em>Clôture de
l'exercice</em>&nbsp;», alors que le lexique les introduit au Chapitre 2, où le corps écrit que «&nbsp;le
capital fait partie des capitaux propres&nbsp;». Renvoyer à <em>Naissance de l'entreprise</em>, ou assumer
que le terme prend son sens complet à la clôture.</li>
<li><strong>Le titre du Chapitre 1 existe sous trois formes.</strong> Le <code>titre:</code> dit «&nbsp;Le
Bilan et le Compte de Résultat&nbsp;», le <code>&lt;h1&gt;</code> ajoute «&nbsp;: deux regards sur
l'entreprise&nbsp;», contre la règle de la section 12, et les renvois de trois pages écrivent
<em>Bilan et Compte de Résultat</em>.</li>
</ol></li>
<li><strong>Deux règles de la passe valent pour tous les modules</strong> et attendent la charte&nbsp;: le
renvoi par titre et jamais par numéro, et «&nbsp;allumer&nbsp;» banni du texte de l'apprenant. La section 12
les porte en attendant une v17.</li>
<li><strong>Le texte de référence a changé de support.</strong> La passe a été faite dans les pages de
l'application, et les <code>.corps.html</code> livrés sont désormais en retard sur elles. À décider&nbsp;: les
pages <code>.vue</code> deviennent-elles la seule version du texte&nbsp;? Les volumes donnés dans les fiches
— mots, deux-points — sont ceux de la livraison et n'ont pas été recomptés pour cette version&nbsp;; les
outils de comptage lisent les <code>.corps.html</code>.</li>
<li><strong>La page de synthèse</strong> s'appelle encore <code>ce-que-vous-avez-appris.vue</code>&nbsp;;
son renommage en <code>synthese-et-feuille-de-route.vue</code> est laissé au décideur.</li>
<li><strong>Relecture de fond des textes des activités</strong> — consignes, verdicts et retours des
composants. La passe n'y a cherché que les motifs de la section 12, pas la clarté. Optionnelle.</li>
""", 's14 nouveaux points')

d.rep_s("""<li><strong>Scénarios des 13 vidéos d'ouverture</strong> — durée, format, degré de présence des personnages
à l'image.</li>""", """<li><strong>Scénarios des treize vidéos d'ouverture</strong> — leur rôle est décidé (section 9)&nbsp;;
restent la durée, le format, et le degré de présence des personnages à l'image.</li>""", 's14 vidéos')

# ═══════════════════════════════════════════════════════════════════════════
#  PIED DE PAGE
# ═══════════════════════════════════════════════════════════════════════════
d.rep_s("""<p class="fin">Document de référence — Casoria, v28 du 18 septembre 2026. La saisie des écritures
portée à l'application : totaux calculés, comportement des totaux, geste de saisie à la ligne. Les
corrections des Chapitres 7, 9, 10 et 12 sont groupées, et les lignes automatiques de la section 9 sont
recomptées depuis les fiches : 13 au Chapitre 5, 58 au module.""",
        """<p class="fin">Document de référence — Casoria, v29 du 13&nbsp;octobre 2026. La passe de
clarification du texte reportée&nbsp;: titres à l'écran, renvois par titre, alertes et précisions, deux mots
au lexique, rôle des vidéos, correspondance avec la numérotation de l'application. Quatre contradictions
avec des décisions antérieures sont posées à la section 14.""", 'pied')

d.rep_s("""<strong>Trois définitions de la section 11 restent à trancher</strong>, et elles sont le seul point de fond
que cette version laisse ouvert.""", """<strong>Trois définitions de la section 11 restent à trancher</strong>, avec les quatre points de
la passe de clarification.""", 'pied définitions')

# ═══════════════════════════════════════════════════════════════════════════
#  CONTRÔLES
# ═══════════════════════════════════════════════════════════════════════════
d.compte('v28', 0, 'mention de la v28')
d.compte('Piloter', 2, 'Piloter : ancien titre, au bloc Changements et à la fiche du 12')
d.compte('Naître en tant', 0, 'ancien titre du 2')
d.compte('au centime près', 1, 'interdit, cité au seul recensement')
d.compte('presque au centime', 1, 'au bloc Changements seulement')
d.compte('formation dédiée au pilotage', 0, 'teasing nommé')
d.compte('<td class="cle">Crédit de TVA</td>', 1, 'lexique crédit de TVA')
d.compte('<td class="cle">Reprise de provision</td>', 1, 'lexique reprise')
d.compte('<h2>Changements v29</h2>', 1, 'bloc Changements')

mauvais = re.findall(r'\d[ \t]\d{3}\b|\d[ \t]€', d.s)
assert not mauvais, f'sommes sans insécable : {mauvais[:5]}'

print('── déroulé v28 → v29')
d.write(DER_OUT)
