#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Répercute la livraison du Chapitre 13 au déroulé (v24) et à la charte (v15).

Le registre a déjà été répercuté par repercuter_ch13.py, au fil de la rédaction.
Le journal l'est par repercuter_journal13.py.

Chaque substitution est assertée unique. Les fichiers sont écrits à la toute
fin : une assertion qui saute les laisse intacts (règle 4 des documents de
référence).

Règle 1 des documents de référence : une version ne garde que son propre bloc
« Changements ». Celui de la v22 saute.
"""
import re

NB = chr(0xA0)
assert NB == ' '

DER_IN = 'deroule-comprendre-la-comptabilite-v23.corps.html'
DER_OUT = 'deroule-comprendre-la-comptabilite-v24.corps.html'
CHA_IN = 'charte-redaction-casoria-v14.corps.html'
CHA_OUT = 'charte-redaction-casoria-v15.corps.html'


class Doc:
    def __init__(self, path):
        self.path = path
        self.s = open(path, encoding='utf-8').read()
        self.n = 0

    def rep(self, old, new, label, n=1):
        c = self.s.count(old)
        assert c == n, f'{self.path} — {label} : {c} occurrence(s), {n} attendue(s)'
        self.s = self.s.replace(old, new, n)
        self.n += 1

    def rep_bloc(self, debut, fin, new, label):
        i = self.s.find(debut)
        assert i >= 0, f'{self.path} — {label} : début introuvable'
        j = self.s.find(fin, i)
        assert j >= 0, f'{self.path} — {label} : fin introuvable'
        assert self.s.count(debut) == 1, f'{self.path} — {label} : début non unique'
        self.s = self.s[:i] + new + self.s[j + len(fin):]
        self.n += 1

    def compte(self, motif, n, label):
        c = self.s.count(motif)
        assert c == n, f'{self.path} — {label} : {c} occurrence(s) de « {motif} », {n} attendue(s)'

    def write(self, path):
        open(path, 'w', encoding='utf-8').write(self.s)
        print(f'   {path} — {self.n} substitutions')


# ═══════════════════════════════════════════════════════════════════════════
#  LE DÉROULÉ — v23 → v24
# ═══════════════════════════════════════════════════════════════════════════
d = Doc(DER_IN)

# ── en-tête ────────────────────────────────────────────────────────────────
d.rep('<p class="kicker">Casoria • Document de référence • v23</p>',
      '<p class="kicker">Casoria • Document de référence • v24</p>', 'kicker')

d.rep_bloc('<p class="chapo">Déroulé annoté', '</p>',
           '''<p class="chapo">Déroulé annoté de la formation. Treize chapitres, un exercice complet simulé de la création
à la clôture, sur le fil rouge d'une PME fictive. <strong>Cette v24 enregistre la livraison du
Chapitre 13, et le module est complet</strong>&nbsp;: treize chapitres écrits, relus et livrés. Elle ne
touche ni au plan, ni au scénario chiffré, ni à une ligne d'écriture — ce chapitre n'en passe aucune.
<strong>Le tri du registre des écarts est fait</strong>, ce que la fiche du Chapitre 13 imposait de faire
en une fois sur la matière complète&nbsp;: onze entrées sur quarante-neuf sont retenues, une remonte en
précision et trois partent en module ultérieur. <strong>Trois décisions du décideur entrent ici</strong>&nbsp;:
le composant du Chapitre 13 est retiré, le glossaire et la liste des écarts passent après le bloc de
clôture, et trois mots rejoignent les vigilances de la section 12.</p>''',
           'chapo')

d.rep('Charte de rédaction Casoria v14 — règles de forme, applicables à tous les modules. '
      'Ce déroulé ne les répète pas. La v14 ajoute trois règles à la section 12, toutes de la '
      'même espèce\xa0: ce que le rédacteur ne peut pas voir parce qu\'il connaît déjà la réponse. '
      'Le vocabulaire de fabrication qui passe dans le texte, le nom propre qui entre sans son '
      'rôle, et le renvoi qui rappelle la substance d\'une notion sans en rendre le nom. La '
      'section 21 passe à quarante-deux cases. Toute la numérotation est inchangée, et tous les '
      'renvois faits d\'ici restent valides.',
      'Charte de rédaction Casoria v15 — règles de forme, applicables à tous les modules. '
      'Ce déroulé ne les répète pas. La v15 ajoute une seule clause, à la section 2\xa0: le dernier '
      'chapitre d\'un module peut porter, après le bloc «\xa0Ce que vous avez appris\xa0», les blocs de '
      'référence qu\'il rend au lecteur. Toute la numérotation est inchangée, et tous les renvois '
      'faits d\'ici restent valides.',
      'documents liés')

# ── le bloc « Changements » ────────────────────────────────────────────────
d.rep_bloc('<h2>Changements v22</h2>', '</ul>\n', '''<h2>Changements v24</h2>
<p>Le Chapitre 13 est écrit, relu et livré. <strong>Le module est complet.</strong> Le plan et le scénario
chiffré de la section 3 sont intacts, et ce chapitre ne passe aucune écriture&nbsp;: le total de contrôle
du module reste à 1&nbsp;294&nbsp;694,00&nbsp;€ au débit comme au crédit.</p>
<ul>
<li><strong>Le tri du registre des écarts est fait</strong>, en une fois et sur la matière complète, comme
cette fiche l'exigeait. Quarante-neuf candidates, <strong>onze retenues</strong> — 1.1, 2.3, 3.2, 3.4,
5.2, 6.2, 7.4, 8.3, 10.3, 11.6 et 12.5. Une remonte en précision, trois partent en module ultérieur,
trente-quatre restent écrites au registre. Le motif de chaque écartée est à l'annexe du chapitre.</li>
<li><strong>Le composant <code>&lt;FlashDecision /&gt;</code> est retiré</strong>, sections 5, 7 et 10.
Décision du décideur&nbsp;: l'activité fera l'objet du module suivant, et le Chapitre 13 n'a pas besoin
d'elle pour basculer. <strong>Le Chapitre 13 devient le seul du module sans écriture, sans composant et
sans illustration</strong>, ce qui est cohérent avec ce qu'il est — il ne démontre rien, il reprend et il
oriente. Les 15&nbsp;minutes de la section 9 tiennent sans lui.</li>
<li><strong>Le glossaire et la liste des écarts passent après le bloc «&nbsp;Ce que vous avez
appris&nbsp;»</strong>, en annexe de chapitre. Décision du décideur, prise au tour de relecture. Le corps
garde son sous-titre, son paragraphe et un renvoi. <strong>C'est un écart au gabarit de la charte,
section 2</strong>, et la v15 de la charte le régularise par une clause propre au dernier chapitre d'un
module.</li>
<li><strong>Une précision entre au recensement</strong>, section 6. «&nbsp;la même allure&nbsp;» au
Chapitre 13, et c'est <strong>le second cas du module où une entrée du registre remonte dans un autre
chapitre que celui qui l'a produite</strong> — l'entrée 1.4 est née au Chapitre 1. Les deux cas viennent
du même chapitre, celui qui montre les documents avant que le lecteur n'ait de raison de les comparer à
d'autres. <strong>Treize chapitres sur treize portent désormais une précision.</strong></li>
<li><strong>Trois vigilances de vocabulaire entrent à la section 12</strong>, «&nbsp;parcours&nbsp;»,
«&nbsp;lexique&nbsp;» et «&nbsp;aside&nbsp;», <strong>toutes trois trouvées par script avant d'être
écrites</strong>. Le contrôle né au Chapitre 12 est désormais un outil, <code>outils/verif_ch13.py</code>,
et il porte son seuil&nbsp;: un mot que ce document emploie au moins huit fois et qu'aucun chapitre livré
ne porte est un candidat.</li>
<li><strong>Deux définitions de la section 11 sont corrigées</strong>, «&nbsp;Capitaux propres&nbsp;» et
«&nbsp;Immobilisation&nbsp;», qui écrivaient «&nbsp;au passif&nbsp;» et «&nbsp;à l'actif&nbsp;» en
minuscules contre la charte, section 9. Le défaut a été trouvé en construisant le glossaire du
Chapitre 13, qui reprend cette table telle quelle.</li>
<li><strong>Trois définitions de la section 11 restent en l'état et sont signalées</strong>, section 14&nbsp;:
«&nbsp;marge nette&nbsp;» et «&nbsp;autonomie financière&nbsp;» reproduisent la tournure que la relecture
profane du Chapitre 12 a déclarée illisible, et «&nbsp;impôt assis sur le bénéfice&nbsp;» est une tournure
de métier. Leurs rechanges sont écrites à l'annexe du Chapitre 13.</li>
</ul>
''', 'bloc Changements')

# ── section 5 : le composant du Chapitre 13 sort ───────────────────────────
d.rep('<tr><td class="ch">13</td><td><code>&lt;FlashDecision /&gt;</code></td>'
      '<td>Situation en 3 lignes, 3 décisions, pas de bonne réponse unique</td></tr>\n', '',
      'composant FlashDecision')
# ne reste que la mention du bloc « Changements », qui dit son retrait
d.compte('FlashDecision', 1, 'FlashDecision')

# ── section 6 : la précision du Chapitre 13 ────────────────────────────────
d.rep('\n</tbody>\n</table>\n<p class="legende"><strong>État\xa0: douze chapitres écrits',
      '''
<tr><td class="ch">13</td><td class="cle">«\xa0la même allure\xa0»</td><td><strong>Écrite.</strong> Que le
Bilan et le Compte de Résultat de ce module ont une forme unique&nbsp;; qu'une entreprise présente les
siens en modèle abrégé, de base ou développé selon sa taille, et qu'une société cotée les publie dans un
référentiel international dont la présentation ne ressemble à aucun des trois&nbsp;; et que d'une
présentation à l'autre, les lignes changent de nom, de place et de quantité. Ancrée au premier sous-titre,
sur la réserve que le corps pose en écrivant que les comptes que le lecteur ouvrira ne se ressembleront
pas tous. <strong>Vient de l'entrée 1.4 du registre, née au Chapitre 1 et sortie par le haut
ici</strong> — second cas du module où une entrée remonte dans un autre chapitre que celui qui l'a
produite, après 1.5 au Chapitre 12, <strong>et les deux viennent du Chapitre 1</strong>. Le corollaire que
la fiche du Chapitre 12 posait comme ordre de travail est donc vérifié. <strong>Cinquième fois du module
que l'ancre est une réserve que le corps posait déjà.</strong> Elle ne coûte rien au corps, l'ancre
n'étant pas un nombre venu du décor. <strong>La dernière phrase de la formulation est restée au
corps</strong> et n'est pas dans la note&nbsp;: «\xa0ce qui ne change pas d'un format à l'autre, c'est la
question à laquelle chaque colonne répond\xa0» est la thèse du sous-titre, et elle porte trop pour dépendre
d'un clic.</td></tr>

</tbody>
</table>
<p class="legende"><strong>État\xa0: treize chapitres écrits''', 'précision du Chapitre 13')

d.rep('''treize chapitres écrits, douze précisions écrites, au 26\xa0août 2026.</strong>
Le Chapitre 13, non encore écrit, n\'en porte aucune\xa0; il posera la sienne à sa rédaction, en confrontant ses entrées du registre des écarts au test de la charte,
section 20 — une phrase remonte au texte, un paragraphe reste au registre. <strong>Dix des douze viennent''',
      '''treize chapitres écrits, treize précisions écrites, au 27\xa0août 2026.</strong>
Le recensement est complet. <strong>Onze des treize viennent''', 'état du recensement')

d.rep('''Le\ncorollaire est un ordre de travail pour le Chapitre 13&nbsp;: une entrée refusée comme précision de son\npropre chapitre n\'est pas pour autant condamnée à l\'aside, elle attend le chapitre où son ancre existe.''',
      '''<strong>Le Chapitre 13 l\'a vérifié</strong>&nbsp;: l\'entrée 1.4, née elle aussi au Chapitre 1, y
remonte sur «\xa0la même allure\xa0». Le corollaire tient donc, et il vaut pour les modules à venir&nbsp;:
une entrée refusée comme précision de son propre chapitre n\'est pas pour autant condamnée à l\'aside, elle
attend le chapitre où son ancre existe.''', 'corollaire du Chapitre 12')

d.rep('''<strong>Ce que la passe a appris sur le choix de l\'ancre</strong>, et qui vaut pour
les cinq chapitres restants&nbsp;:''',
      '''<strong>Ce que la passe a appris sur le choix de l\'ancre</strong>, et qui a tenu jusqu\'au
dernier chapitre&nbsp;:''', 'leçon de la passe')

# ── section 7 : l'activité du Chapitre 13 sort ─────────────────────────────
d.rep('<tr><td class="ch">13</td><td class="cle">Flash Décision [JDC 4]</td>'
      '<td>Pas de bonne réponse unique. Bascule vers le pilotage et amorce le module suivant.</td></tr>',
      '<tr><td class="ch">13</td><td class="cle">—</td><td>Chapitre de synthèse. Retiré à la livraison, '
      'le 27\xa0août 2026&nbsp;: la bascule vers la décision se fait en une phrase, et l\'activité appartient '
      'au module de pilotage. Un chapitre qui ne démontre rien n\'a rien à faire prendre position.</td></tr>',
      'activité Flash Décision')
# ne reste que la mention de la fiche, qui dit son retrait
d.compte('Flash Décision', 1, 'Flash Décision')

# ── section 10 : la fiche du Chapitre 13 ───────────────────────────────────
d.rep('''<h4>Activité</h4>
<p>Flash Décision — bascule vers le pilotage, amorce du module suivant.</p>
<h4>Écritures</h4>
<p>Aucune.</p>''', '''<h4>Activité</h4>
<p>Aucune. La fiche en prévoyait une, <em>Flash Décision</em>&nbsp;; elle est retirée à la livraison, le
27&nbsp;août 2026.</p>
<h4>Écritures</h4>
<p>Aucune.</p>
<div class="note"><span class="t">Ce que la rédaction a tranché, à la livraison du 27 août 2026</span>
<p><strong>Le tri du registre, qui est le travail principal du chapitre, a retenu onze entrées sur
quarante-neuf.</strong> Trois arbitrages que le registre demandait de trancher ici le sont&nbsp;: 10.3
l'emporte sur 4.2 et 6.3, les trois portant le même réflexe de prudence sur trois objets&nbsp;; 7.4
l'emporte sur 7.3, parce qu'elle change la lecture d'un document là où l'autre décrit un engagement qui n'y
figure pas&nbsp;; et ni 8.1 ni 8.4 ne passent, 8.3 représentant déjà le Chapitre 8. <strong>Deux écartées
le sont contre ce que le registre prévoyait</strong>, et ce sont elles qu'une relecture doit regarder&nbsp;:
10.4, que la note du Chapitre 10 favorisait, l'activité de ce chapitre ayant déjà fait manipuler la
symétrie&nbsp;; et 1.3, <strong>la première à rouvrir</strong> si la place paraît trop chère payée.</p>
<p><strong>Deux règles se contredisaient sur les deux blocs repris, et l'arbitrage est écrit.</strong> Cette
fiche exige que la liste des écarts «&nbsp;assemble et enchaîne des phrases déjà écrites&nbsp;» et
«&nbsp;n'en rédige aucune&nbsp;»&nbsp;; la charte, section 10, plafonne le deux-points à un par section. Les
deux blocs en portent quatorze. <strong>Ils sortent du compte</strong>, comme en sortent les légendes et
les listes&nbsp;: ce n'est pas de la prose du corps, et le lecteur ne les lit pas dans le fil. Tenir le
budget aurait imposé de réécrire ce que cette fiche interdit de réécrire.</p>
<p><strong>La grille complète «&nbsp;affichée une dernière fois&nbsp;» n'a pas de composant</strong>, et la
charte, section 18, interdit au rédacteur d'en inventer un. Le chapitre fait la preuve sur les deux
documents que l'écran affiche déjà&nbsp;: son premier sous-titre remonte quatre lignes du Bilan à leur
opération d'origine. <strong>Si un affichage dédié est voulu</strong>, en pleine largeur et hors du flux du
texte, c'est un composant à ajouter à la section 5 avant que le chapitre ne le porte.</p>
<p><strong>Le lexique de la section 11 est repris tel quel dans le glossaire</strong>, aux consignes de
fabrication près et à deux capitales près. <strong>Trois de ses définitions posent problème et sont
signalées à la section 14</strong> plutôt que corrigées de la main du rédacteur&nbsp;: une définition de
référence se change ici, pas dans un chapitre.</p>
<p><strong>Volume&nbsp;: 584 mots au périmètre déclaré, 618 avec les sous-titres</strong>, sous le seuil de
680. La charte, section 19, demande alors à quoi le texte a délégué, et la réponse est au glossaire, à la
liste des écarts et aux deux documents eux-mêmes, que le chapitre fait regarder plutôt qu'il ne les décrit.
<strong>Un tour de relecture profane, sept corrections, toutes appliquées</strong>, et le premier jet en
faisait 549.</p></div>''', 'fiche du Chapitre 13')

# ── section 11 : deux capitales ────────────────────────────────────────────
d.rep('Capital et résultats accumulés, au passif',
      'Capital et résultats accumulés, au Passif', 'capitale de Capitaux propres')
d.rep("Ce bien, inscrit à l'actif du Bilan",
      "Ce bien, inscrit à l'Actif du Bilan", 'capitale d\'Immobilisation')

# ── section 12 : trois vigilances neuves ───────────────────────────────────
d.rep('''<tr><td class="cle">«\xa0Partie double\xa0»</td>''',
      '''<tr><td class="cle">«\xa0Parcours\xa0», «\xa0lexique\xa0», «\xa0aside\xa0»</td>
<td>Ne s'emploient dans aucun texte de chapitre. Ce sont des mots de fabrication au sens de la charte,
section 12&nbsp;: ce déroulé et la charte les écrivent partout, et aucun des douze chapitres livrés ne les
porte, recompté par script. Écrire «&nbsp;ce module&nbsp;» — que huit des douze chapitres livrés emploient
déjà —, «&nbsp;les mots de ce module&nbsp;» et «&nbsp;ce que ce module a écarté&nbsp;».
<strong>Trouvés au Chapitre 13, le 27&nbsp;août 2026, avant d'avoir été écrits</strong>&nbsp;: c'est la
première fois qu'un mot de fabrication est arrêté par le contrôle plutôt que par une relecture.
<strong>Le contrôle est désormais un outil</strong>, <code>outils/verif_ch13.py</code>, et il porte son
seuil&nbsp;: un mot que ce déroulé emploie <strong>au moins huit fois</strong> et qu'aucun chapitre livré
ne porte est un candidat. Sans le seuil, il rend cent mots de français ordinaire&nbsp;; avec lui, il isole
ceux par lesquels ce document <em>désigne</em> les objets du module. <strong>Il rend des candidats, pas des
verdicts</strong>&nbsp;: huit autres ont été jugés licites au Chapitre 13, dont «&nbsp;registre&nbsp;» et
«&nbsp;entrée&nbsp;», parce qu'ils y ont un sens que ce document ne leur donne pas.</td></tr>
<tr><td class="cle">«\xa0Partie double\xa0»</td>''', 'vigilances parcours/lexique/aside')

# ── section 13 : le Chapitre 13 à l'ordre de rédaction ─────────────────────
d.rep('''<li><strong>Chapitre 13</strong> ensuite, dernier du parcours, avec le vocabulaire réellement employé
désormais connu et le registre à 62 entrées.</li>''',
      '''<li><strong>Chapitre 13 — livré.</strong> 584 mots, 618 avec les sous-titres, le plus court du module
après le Chapitre 7. Trois sous-titres, <strong>aucune écriture, aucun composant, aucune
illustration</strong> — le seul du module dans ce cas. Un tour de relecture profane, sept corrections.
<strong>Son travail principal n'est pas son texte, c'est le tri du registre des écarts</strong>, fait en une
fois sur la matière complète&nbsp;: onze retenues sur quarante-neuf.
<strong>Ce que son tour de relecture enseigne, et qui est propre à un chapitre de synthèse&nbsp;:</strong>
en fin de parcours, un pronom ou une image ne suffisent plus à désigner ce dont on parle. Quatre des sept
corrections portent cela. «&nbsp;Au bas du film&nbsp;» et «&nbsp;sur la photo&nbsp;» sont redevenus
«&nbsp;au bas du Compte de Résultat, le film&nbsp;» et «&nbsp;au Bilan, la photo&nbsp;» — le lecteur vient
de traverser douze chapitres de chiffres, et une image posée au Chapitre 1 ne porte plus seule à cette
distance. <strong>Une cinquième correction est du même ordre et coûte un paragraphe&nbsp;:</strong> l'écart
entre résultat et trésorerie s'y ré-explique une dernière fois, le décideur l'ayant déclaré
«&nbsp;déjà lointain&nbsp;».
<strong>Et un mot proscrit est entré par une correction de relecture et non par le premier jet</strong>,
«&nbsp;toucher&nbsp;», attrapé par le script. Les corrections repassent les contrôles comme le premier jet.
<strong>C'est aussi le chapitre qui a fait du contrôle de vocabulaire un outil</strong>, et qui a montré
qu'un bloc en <code>&lt;dl&gt;</code> ou en <code>&lt;table&gt;</code> passe les quatre contrôles de
<code>livrer.py</code> sans être vu.</li>''', 'ordre de rédaction')

# ── section 14 : le pied de page ───────────────────────────────────────────
d.rep_bloc('<p class="fin">Document de référence — Casoria, v23',
           'Ce qui suit est le bilan de la v20, gardé\npour son raisonnement.',
           '''<p class="fin">Document de référence — Casoria, v24 du 27 août 2026. Livraison du Chapitre 13.
<strong>Treize chapitres écrits sur treize&nbsp;: le module est complet.</strong> Le scénario chiffré de la
section 3 est inchangé et reste vérifié&nbsp;: le Bilan de l'exercice boucle sur 130&nbsp;410&nbsp;€ des
deux côtés, le Compte de Résultat sur 283&nbsp;000&nbsp;€ de produits, et le total de contrôle du module
vaut 1&nbsp;294&nbsp;694,00&nbsp;€ au débit comme au crédit — ce chapitre ne passe aucune écriture et ne
pouvait donc rien y changer. <strong>Tous les chiffres du Chapitre 13 ont été recalculés depuis les
panneaux des onze chapitres qui les produisent</strong>, par <code>outils/verif_ratios.py</code> et
<code>outils/verif_cloture.py</code>, et confrontés un à un au texte.
<strong>Le recensement des précisions, section 6, est complet</strong>&nbsp;: treize chapitres, treize
précisions, dont onze issues d'une entrée du registre sortie par le haut.
<strong>Le registre des écarts porte 63 entrées et son tri est fait</strong>&nbsp;: onze retenues, douze
remontées en précision, six en module ultérieur, trente-quatre non retenues. Les quatre sous-totaux se
recomptent par script à chaque écriture du fichier.
<strong>Trois définitions de la section 11 restent à trancher</strong>, et elles sont le seul point de fond
que cette version laisse ouvert. «&nbsp;Marge nette — Résultat net rapporté au chiffre d'affaires&nbsp;» et
«&nbsp;Autonomie financière — Capitaux propres rapportés au total du Bilan&nbsp;» sont exactement les
tournures que la relecture profane du Chapitre 12 a déclarées illisibles, et que le corps de ce chapitre a
dû réécrire. Le glossaire du Chapitre 13 les reproduit telles quelles, une définition de référence se
changeant ici et pas dans un chapitre. <strong>Leurs rechanges sont écrites à l'annexe du
Chapitre 13</strong>, prises au corps du Chapitre 12 lui-même&nbsp;: «&nbsp;ce qui reste à l'entreprise sur
ce qu'elle a vendu&nbsp;» et «&nbsp;la part de ce que l'entreprise détient qu'elle gardera tant qu'elle
vivra, par opposition à ce qu'elle devra rendre&nbsp;». Un troisième cas, plus léger&nbsp;: «&nbsp;Impôt
assis sur le bénéfice&nbsp;», où «&nbsp;assis sur&nbsp;» est une tournure de métier que le Chapitre 11
n'emploie pas.
<strong>La charte passe en v15</strong> et reçoit une seule clause, à la section 2&nbsp;: le dernier
chapitre d'un module peut porter ses blocs de référence après le bloc «&nbsp;Ce que vous avez appris&nbsp;».
Les deux autres candidats du chapitre n'ont qu'une attestation et vivent au journal de rédaction — et la
seconde ne viendra pas de ce module, qui est fini.
Ce qui suit est le bilan de la v20, gardé
pour son raisonnement.''', 'pied de page')

# ── section 14 : les illustrations ─────────────────────────────────────────
d.rep("""À trancher chapitre par chapitre, en écrivant la
légende, jamais après.</p>
<p><strong>Le Chapitre 12 reste aux méthodes""",
      """À trancher chapitre par chapitre, en écrivant la
légende, jamais après.</p>
<p><strong>Le Chapitre 13 n'entre dans aucune des deux familles, et il ne porte aucune
illustration.</strong> C'est le seul du module dans ce cas, et le principe n'y est pour rien&nbsp;: il ne
démontre rien, il reprend, il nomme et il oriente. <strong>Surtout, l'axe est déjà pris.</strong> Le seul
geste qu'une illustration pourrait faire ici est de montrer les deux documents complets, ce que sa fiche
confie précisément à leur affichage&nbsp;; le test des axes l'interdit donc. <strong>Treize chapitres, dix
illustrations</strong>, et le principe de la chose lue deux fois n'a plus servi depuis le Chapitre 8 — les
cinq derniers sont des méthodes ou des synthèses, et ni l'une ni l'autre ne se montre deux fois.</p>
<p><strong>Le Chapitre 12 reste aux méthodes""",
      'illustrations')

# ── ce qui reste en attente ────────────────────────────────────────────────
d.rep('''<strong>Ce qui reste en attente.</strong> Au Chapitre 5,''',
      '''<strong>Ce qui reste en attente, et qui ne dépend plus de la rédaction des chapitres.</strong>
Au Chapitre 5,''', 'ce qui reste en attente')

d.rep('Le module suit la charte v14\xa0; toute la numérotation des sections est inchangée, ici comme à la charte.',
      'Le module suit la charte v15\xa0; toute la numérotation des sections est inchangée, ici comme à la charte.',
      'mention de la charte au pied de page')

d.compte('v23', 0, 'mention de version périmée')
d.compte('v14', 0, 'mention de la charte périmée')

# ═══════════════════════════════════════════════════════════════════════════
#  LA CHARTE — v14 → v15
# ═══════════════════════════════════════════════════════════════════════════
c = Doc(CHA_IN)

VRAI_ANCRE = "Il n'y a pas non plus de bloc\n«\xa0Pour aller plus loin\xa0» : ce qu'il porterait migre vers un aside unique en fin de module, alimenté par le\nregistre des écarts (section 20).</p></div>"
NEUF_CLAUSE = 'Il n\'y a pas non plus de bloc\n«\xa0Pour aller plus loin\xa0» : ce qu\'il porterait migre vers un aside unique en fin de module, alimenté par le\nregistre des écarts (section 20).</p>\n\n<div class="note"><span class="t">Le dernier chapitre d\'un module, et ce qu\'il peut porter après le bloc de clôture</span>\n<p><strong>Règle.</strong> Le dernier chapitre d\'un module peut porter, <strong>après</strong> le bloc\n«&nbsp;Ce que vous avez appris&nbsp;», les blocs de référence qu\'il rend au lecteur&nbsp;: le glossaire du\nmodule et la liste de ce que le module a écarté. Le corps garde le sous-titre et le paragraphe qui les\nannoncent, et y renvoie.</p>\n<p><strong>Le motif est que ce ne sont pas des textes de chapitre.</strong> Ce sont deux documents rendus au\nlecteur, faits pour être consultés et non lus dans le fil. Placés dans le corps, ils coupent la lecture en\nson milieu — quatre pages de tableau entre deux sous-titres — et repoussent le bloc de clôture loin de\nl\'endroit où le lecteur l\'attend. Placés après lui, ils ne coûtent rien à personne.</p>\n<p><strong>Ce que la règle ne fait pas.</strong> Elle n\'autorise aucun autre chapitre à porter quoi que ce\nsoit après son bloc de clôture, et elle n\'autorise pas le dernier chapitre à y porter du texte de chapitre.\nLe bloc «&nbsp;Ce que vous avez appris&nbsp;» reste la dernière chose que le lecteur <em>lit</em>&nbsp;;\nce qui le suit est ce qu\'il <em>consulte</em>.</p>\n<div class="note"><span class="t">Attesté</span>\n<p>Chapitre 13 de «&nbsp;Comprendre la comptabilité&nbsp;», 27 août 2026. <strong>La clause vient d\'une\ndécision du décideur et non d\'une attestation de relecture</strong>, et c\'est pourquoi elle entre avec un\nseul cas là où la section 12 en exige deux&nbsp;: une décision de structure n\'est pas une vigilance\ndéduite. La v1 du chapitre portait les deux blocs dans le corps, entre le deuxième et le troisième\nsous-titre&nbsp;; le corps du chapitre y perdait sa continuité sur quatre pages.</p></div></div></div>'

c.rep('<p class="kicker">Casoria • Document de référence • v14</p>',
      '<p class="kicker">Casoria • Document de référence • v15</p>', 'kicker')

c.rep_bloc('<p class="chapo">Règles de rédaction', '</p>',
           '''<p class="chapo">Règles de rédaction des textes de chapitre, applicables à tous les modules de la plateforme.
<strong>Cette v15 ne déplace aucune section, n'en crée aucune, et n'ajoute qu'une clause</strong>&nbsp;: à
la section 2, le dernier chapitre d'un module peut porter ses blocs de référence après le bloc
«&nbsp;Ce que vous avez appris&nbsp;». La clause vient d'une décision de décideur et non d'une attestation,
et elle est écrite comme telle. Toute la numérotation est inchangée, et tous les renvois faits depuis les
déroulés de module restent valides. Cette charte fait autorité sur la forme. Le déroulé de chaque module
reste seul maître du fond, du scénario aux chiffres, de la séquence au lexique. Une règle de forme ne se
répète pas dans un déroulé, elle s'y cite.</p>''', 'chapo')

c.rep(VRAI_ANCRE, NEUF_CLAUSE,
      'clause du dernier chapitre')

c.rep_bloc('<p class="fin">Charte de rédaction Casoria — v13', '</p>',
           '''<p class="fin">Charte de rédaction Casoria — v15 du 27 août 2026. Aucun dispositif nouveau, aucune
section déplacée, une seule clause ajoutée, à la section 2.
<strong>Elle entre par décision et non par attestation</strong>, ce qui est le premier cas de cette charte.
Le motif est écrit à la section&nbsp;: une décision de structure prise par le décideur d'un module n'est pas
une vigilance déduite d'une relecture, et la règle des deux attestations ne la vise pas. Elle reste bornée
au dernier chapitre d'un module et aux blocs de référence.
<strong>Toute la numérotation est inchangée</strong>, et les renvois faits depuis les déroulés de module
restent valides.
<strong>Ce qui n'entre pas.</strong> Huit candidats à une seule attestation vivent au journal de rédaction
du module «&nbsp;Comprendre la comptabilité&nbsp;»&nbsp;: le seuil de longueur de la déclaration en gras,
section 9&nbsp;; <em>la simplification dite trop tard</em>, <em>la périphrase née d'une contrainte de
coloration</em>, <em>le sigle d'usage courant qui précède son développement</em>&nbsp;; <em>la notion posée
avant l'obligation qui la fonde</em>, <em>la phrase exacte sur l'écran et fausse sur ce qui est
enregistré</em>&nbsp;; et deux produits par le Chapitre 13 — <em>en fin de parcours, un pronom ou une image
ne suffisent plus à désigner ce dont on parle</em>, et <em>une notion ancienne se ré-explique dans le
chapitre de synthèse</em>. <strong>Ces deux-là n'auront pas de seconde attestation dans ce module, qui est
fini&nbsp;; elles attendent le module suivant.</strong> La section 12 grossit par attestation et jamais par
soupçon.</p>''', 'pied de page')

c.compte('v14', 0, 'mention de version périmée à la charte')

# ── écriture, à la toute fin ────────────────────────────────────────────────
print('── répercussion v24 / v15')
d.write(DER_OUT)
c.write(CHA_OUT)
