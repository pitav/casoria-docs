#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Répercussion de la livraison du Chapitre 12 — 26 août 2026.

Déroulé v22 → v23, et journal de rédaction. La charte v14 est inchangée : les
deux candidats du chapitre n'ont qu'une attestation et vivent au journal.
Le registre a été répercuté à part, le jour de la rédaction, sa propre règle
l'imposant.

Ce script rattrape aussi ce que la répercussion du Chapitre 11 avait laissé
au journal : le tableau d'avancement, la table des déclarations, la table des
relectures profanes et la section des illustrations s'étaient arrêtés au
Chapitre 10, alors que ce journal est le seul document qui permette de
vérifier les règles cumulatives.

Chaque substitution est assertée unique et l'écriture se fait à la toute fin :
une assertion qui saute laisse les fichiers intacts.
"""
import os
import re

NB = '\u00a0'
assert NB == chr(160), 'NB doit être un insécable, pas un espace ordinaire'


class Doc:
    def __init__(self, chemin):
        self.chemin = chemin
        self.s = open(chemin, encoding='utf-8').read()
        self.n = 0

    def rep(self, old, new, label, n=1, brut=False):
        # brut : le fragment porte un « ~ » littéral et non le marqueur d'insécable.
        if not brut:
            old, new = old.replace('~', NB), new.replace('~', NB)
        trouves = self.s.count(old)
        assert trouves == n, f'{self.chemin} · {label} : {trouves} occurrence(s), {n} attendue(s)'
        self.s = self.s.replace(old, new, n)
        self.n += 1

    def ecrire(self):
        open(self.chemin, 'w', encoding='utf-8').write(self.s)
        print(f'   {self.chemin} — {self.n} substitutions')


d = Doc('deroule-comprendre-la-comptabilite-v22.corps.html')
j = Doc('journalderedactioncomprendrelacomptabilite.md')

# ═══════════════════════════════════════════════════════════════════════════
# DÉROULÉ v22 → v23
# ═══════════════════════════════════════════════════════════════════════════

d.rep('<p class="kicker">Casoria • Document de référence • v22</p>',
      '<p class="kicker">Casoria • Document de référence • v23</p>', 'kicker')

d.rep("""<strong>Cette v22 enregistre la livraison du Chapitre 11 et la reprise du Chapitre 10 en v5</strong>,
et ne touche ni au plan ni au scénario chiffré. <strong>L'écart de 22&nbsp;648,50&nbsp;€ ouvert par la v21
est fermé</strong>, et le Bilan de l'exercice avec lui&nbsp;: la grille boucle sur 130&nbsp;410&nbsp;€ des
deux côtés au terme du Chapitre 11, poste par poste. Le prix en est un panneau automatique de vingt-sept
lignes au Chapitre 10, en trois écritures, et l'encadré «&nbsp;Ce qu'aucun des deux régimes ne
montre&nbsp;» de la section 4, devenu faux, est réécrit. <strong>Onze chapitres sont écrits sur
treize.</strong></p>""",
      """<strong>Cette v23 enregistre la livraison du Chapitre 12</strong>, et ne touche ni au plan, ni au
scénario chiffré, ni à une ligne d'écriture — ce chapitre n'en passe aucune. <strong>La piste des colonnes
N et N–1, que la fiche du Chapitre 12 imposait de trancher avant rédaction, est fermée</strong>&nbsp;:
l'entrée 1.5 du registre sort par le haut et devient la précision du chapitre, première du module à
remonter dans un autre chapitre que celui qui l'a produite. Trois vigilances de vocabulaire entrent à la
section 12, et le sigle BFR au lexique. <strong>Douze chapitres sont écrits sur treize, et il ne reste que
le 13.</strong></p>""", 'chapo')

# ─── section 6 : recensement des précisions ─────────────────────────────────
d.rep("""écrit</strong>, comme au Chapitre 9 et pour la même raison — le plafond
annuel d'imputation d'un déficit bouge d'une loi de finances à l'autre.</td></tr>

</tbody>""",
      """écrit</strong>, comme au Chapitre 9 et pour la même raison — le plafond
annuel d'imputation d'un déficit bouge d'une loi de finances à l'autre.</td></tr>

<tr><td class="ch">12</td><td class="cle">«~tout seul~»</td><td><strong>Écrite.</strong> Que le Bilan et le
Compte de Résultat de ce module portent une seule colonne de chiffres, alors que ceux qu'une entreprise
publie en portent deux, l'exercice qui vient de se terminer et le précédent, côte à côte&nbsp;; que
Latitude Café n'a rien à côté de quoi se ranger, étant à son premier exercice&nbsp;; et que sur de vrais
comptes la comparaison des deux colonnes est souvent ce qu'on regarde avant les montants eux-mêmes. Ancrée
au troisième sous-titre, sur la réserve que le corps pose en écrivant qu'un ratio ne dit rien seul.
<strong>Vient de l'entrée 1.5 du registre, née au Chapitre 1 et sortie par le haut ici</strong> — premier
cas du module où une entrée remonte dans un autre chapitre que celui qui l'a produite. La fiche du
Chapitre 12 avait ouvert la piste et interdisait de la découvrir au Chapitre 13. <strong>Quatrième fois du
module que l'ancre est une réserve que le corps posait déjà</strong>, après «~le plus souvent~» au
Chapitre 7, «~probable~» au Chapitre 10 et «~perte~» au Chapitre 11&nbsp;: le patron annoncé comme premier
endroit où chercher a tenu au premier essai suivant. Elle ne coûte rien au corps, l'ancre n'étant pas un
nombre venu du décor.</td></tr>

</tbody>""", 'recensement des précisions, ligne 12')

d.rep("""<strong>État~: onze chapitres écrits, onze précisions écrites, au 25~août 2026.</strong>
Les chapitres 12 et 13, non encore écrits, n'en portent aucune~; chacun posera la sienne à sa rédaction, en confrontant ses entrées du registre des écarts au test de la charte,
section 20 — une phrase remonte au texte, un paragraphe reste au registre. <strong>Neuf des onze viennent
d'une entrée du registre sortie par le haut</strong>&nbsp;; celle du Chapitre 8 a fait naître le dispositif,
et celles des Chapitres 9 et 11 sont nées de l'écriture.""",
      """<strong>État~: douze chapitres écrits, douze précisions écrites, au 26~août 2026.</strong>
Le Chapitre 13, non encore écrit, n'en porte aucune~; il posera la sienne à sa rédaction, en confrontant ses entrées du registre des écarts au test de la charte,
section 20 — une phrase remonte au texte, un paragraphe reste au registre. <strong>Dix des douze viennent
d'une entrée du registre sortie par le haut</strong>&nbsp;; celle du Chapitre 8 a fait naître le dispositif,
et celles des Chapitres 9 et 11 sont nées de l'écriture.
<strong>Ce que le Chapitre 12 ajoute&nbsp;: une entrée peut remonter dans un autre chapitre que celui qui
l'a produite.</strong> L'entrée 1.5 est née au Chapitre 1 et n'y avait pas d'ancre, le lecteur y regardant
une grille vierge&nbsp;; elle en a une au Chapitre 12, où il lit un Bilan chiffré pour décider. Le
corollaire est un ordre de travail pour le Chapitre 13&nbsp;: une entrée refusée comme précision de son
propre chapitre n'est pas pour autant condamnée à l'aside, elle attend le chapitre où son ancre existe.""",
      'état du recensement des précisions')

# ─── section 10 : fiche du Chapitre 12 ──────────────────────────────────────
d.rep('<h3 class="saut">Chapitre 12 — Piloter : la décision et les 3 ratios · 30 min</h3>',
      '<h3 class="saut">Chapitre 12 — Piloter : la décision et les trois ratios · 30 min</h3>',
      'titre de la fiche 12')

d.rep("""<div class="alert"><span class="t">Piste à examiner avant d'écrire ce chapitre</span>""",
      """<div class="note"><span class="t">Trois arbitrages de la rédaction, tranchés à la livraison du
26~août 2026</span>
<p><strong>Le titre du déroulé est conservé, et il annonce trois ratios dont l'un n'en est pas
un.</strong> Le besoin en fonds de roulement est une somme en euros, pas une division. Le corps porte la
distinction en toutes lettres — il écrit que le besoin en fonds de roulement est une somme, puis définit le
ratio comme une division qui donne un pourcentage — et c'est ce qui rendait le titre inoffensif. Deux
rechanges restent écrites à l'annexe du chapitre&nbsp;: «~Piloter~: une décision et trois chiffres~» et
«~Piloter~: lire ses comptes pour décider~».</p>
<p><strong>Le chapitre ne dit rien d'un second emprunt</strong>, alors que le lecteur sort du Chapitre 7 et
posera la question. La réponse du chapitre reste juste, la question posée étant celle de la trésorerie
disponible. La matière part à l'entrée 12.4 du registre, en module ultérieur&nbsp;: elle appelle un
chapitre entier et non une phrase.</p>
<p><strong>La simplification du besoin en fonds de roulement est dite en une phrase du corps</strong>, la
section 6 ne recensant pas d'alerte pour ce chapitre et la charte, section 18, interdisant au rédacteur
d'en ajouter une contre le recensement. Le calcul ne retient que le stock, les créances clients et les
dettes fournisseurs&nbsp;; l'entrée 12.2 du registre porte les quatre lignes du Bilan qu'il omet. Si
l'alerte est décidée, elle entre par la section 6 et non par le chapitre.</p></div>
<div class="note"><span class="t">Volume et forme, à la livraison</span>
<p><strong>833 mots au périmètre déclaré, 865 avec les sous-titres</strong>, pour un seuil de vigilance de
680. <strong>Le dépassement est motivé</strong>, comme la charte, section 19, l'exige&nbsp;: le chapitre
porte quatre termes de lexique neufs et trois outils de lecture qu'aucun schéma ni aucun geste ne peut
définir à la place du texte. Il reste le deuxième du module, le Chapitre 8 en faisant 858. Trois
sous-titres, aucune écriture, un composant, une illustration, une précision, aucun
<code>&lt;UAlert&gt;</code>, deux deux-points en prose et un par section.
<strong>Le premier jet en faisait 668, et le tour de relecture profane a ajouté 165 mots</strong> pour une
seule raison, qui vaut pour le Chapitre 13&nbsp;: définir un terme ne suffit pas à l'introduire, il faut
dire ce que l'opération fait et à quoi elle sert.</p></div>
<div class="note"><span class="t">La piste des colonnes N et N–1 — tranchée avant rédaction</span>""",
      'fiche 12 : arbitrages et volume')

d.rep("""ce qu'un lecteur fait devant de vrais comptes. <strong>À trancher avant rédaction</strong> : ou bien l'écart
reste candidat à l'aside final du Chapitre 13, ou bien il devient une matière de ce chapitre. Les deux se
défendent ; ce qu'il faut éviter, c'est de le découvrir au Chapitre 13, quand il sera trop tard pour en faire
autre chose qu'une phrase de regret.</p></div>""",
      """ce qu'un lecteur fait devant de vrais comptes. <strong>Tranchée le 25~août 2026, avant d'écrire une
ligne&nbsp;: l'entrée 1.5 sort par le haut et devient la précision de ce chapitre</strong>, ancrée sur
«~tout seul~». Les deux autres voies ont été pesées et écartées. La laisser candidate à l'aside final
revenait à faire exactement ce que cette fiche voulait éviter&nbsp;; en faire une matière du corps
supposait d'inventer une colonne de chiffres pour un exercice antérieur que Latitude Café n'a pas, hors du
scénario verrouillé de la section 3. <strong>La voie retenue ne coûte rien au corps</strong>, l'ancre étant
une réserve que le texte posait déjà. Les entrées 1.3 et 1.6, qui sont sur le même terrain, restent seules
à arbitrer au Chapitre 13.</p></div>""", 'fiche 12 : piste tranchée')

# ─── section 11 : lexique cumulatif ─────────────────────────────────────────
d.rep("""<tr><td class="cle">Ratio</td><td class="ch">12</td><td>Rapport entre deux grandeurs comptables</td></tr>
<tr><td class="cle">Besoin en fonds de roulement</td><td class="ch">12</td><td>Stock + créances clients – dettes fournisseurs</td></tr>""",
      """<tr><td class="cle">Ratio</td><td class="ch">12</td><td>Division d'un chiffre du Bilan ou du Compte de Résultat par un autre, qui donne un pourcentage. Le corps dit aussi à quoi elle sert&nbsp;: un pourcentage se compare d'une année sur l'autre, et d'une entreprise à une autre, même si elles n'ont pas la même taille</td></tr>
<tr><td class="cle">Besoin en fonds de roulement</td><td class="ch">12</td><td>Stock + créances clients – dettes fournisseurs. <strong>Le sigle BFR précède le nom complet à la première occurrence</strong>, «~le BFR~: le besoin en fonds de roulement~», et non l'inverse comme pour la SAS au Chapitre 2 et l'IS au Chapitre 11. Le motif est que BFR est le sigle que le lecteur rencontrera avant le nom, chez son banquier comme chez son expert-comptable&nbsp;; personne ne dit «~IS~» avant d'avoir dit «~impôt~». Ce n'est pas une convention maison, à la différence de «~CCA~» et «~PCA~» que la section 12 refuse</td></tr>""",
      'lexique : ratio et BFR')

# ─── section 12 : vigilances de vocabulaire ─────────────────────────────────
d.rep("""<tr><td class="cle">«~Partie double~»</td>""",
      """<tr><td class="cle">«~Exploitation~», «~poste~»</td><td>Ne s'emploient dans aucun texte de chapitre.
Ce sont des mots de fabrication au sens de la charte, section 12&nbsp;: le déroulé les écrit partout et
<strong>aucun des onze chapitres livrés ne les porte</strong>, recompté par script. Écrire
«~l'activité~» et «~une ligne~», que le lecteur a déjà lus. Attestés au Chapitre 12, le 26~août 2026, où le
premier jet les employait trois fois.
<strong>Le contrôle qui les a trouvés est reproductible et vaut pour le Chapitre 13&nbsp;:</strong> un mot
que ce déroulé emploie et qu'aucun chapitre livré ne porte est un candidat au vocabulaire de fabrication.
C'est la première famille de ce type trouvée sans relecteur, après «~la grille~» et «~bloc~».</td></tr>
<tr><td class="cle">«~Nombre~»</td><td>Ne désigne jamais un montant. Écrire «~chiffre~» ou «~somme~». Un
nombre est abstrait&nbsp;; ce que le lecteur regarde est inscrit sur un document. Attesté au Chapitre 12 par
la relecture profane, où «~deux nombres exacts~» ouvrait la reprise du refrain. Le mot reste employable
dans les documents de fabrication, celui-ci compris.</td></tr>
<tr><td class="cle">«~Torréfacteur~»</td><td>Désigne la machine du Chapitre 8, et rien d'autre dans les
textes. Le mot nomme aussi le métier, et le Chapitre 12 l'employait en ce second sens pour dire à qui
comparer les ratios&nbsp;; il écrit «~d'autres entreprises de la même taille~». C'est le corollaire du mot
à deux sens, posé au Chapitre 9 sur «~bloc~», appliqué cette fois à deux sens séparés par quatre
chapitres&nbsp;: <strong>c'est le second sens qui cède, même quand le premier est loin.</strong></td></tr>
<tr><td class="cle">«~Partie double~»</td>""", 'vigilances de vocabulaire')

# ─── section 13 : ordre de rédaction ────────────────────────────────────────
d.rep("""<li><strong>Chapitres 12 et 13</strong> ensuite, quand le vocabulaire réellement employé est connu.</li>""",
      """<li><strong>Chapitre 12 — livré.</strong> 833 mots, 865 avec les sous-titres, <strong>dépassement
motivé et le second du module</strong> derrière le Chapitre 8. Trois sous-titres, aucune écriture, un
composant, une illustration, une précision. <strong>Un tour de relecture profane, vingt corrections, le
tour le plus lourd du module en volume&nbsp;:</strong> le premier jet faisait 668 mots et sept des vingt
corrections portaient la même chose. <strong>Ce qu'il enseigne, et qui vaut pour le Chapitre 13&nbsp;:
définir un terme ne suffit pas à l'introduire, il faut dire ce que l'opération fait et à quoi elle
sert.</strong> «~L'autonomie financière rapporte les capitaux propres au total du Bilan~» était exacte,
tenait dans la définition du lexique, et était illisible. Le mot «~ratio~» était employé sans qu'on dise
jamais que c'est une division ni pourquoi on la fait, et les deux pourcentages étaient calculés sans qu'on
dise ce qu'ils signifient. C'est aussi le premier chapitre du module <strong>sans aucune écriture</strong>,
ce qui rend cinq cases de la checklist sans objet et a révélé un défaut du script qui les passe. Et le
premier à faire remonter une entrée du registre née dans un autre chapitre.</li>
<li><strong>Chapitre 13</strong> ensuite, dernier du parcours, avec le vocabulaire réellement employé
désormais connu et le registre à 62 entrées.</li>""", 'ordre de rédaction, ligne 12')

# ─── section 14 : familles d'illustration ───────────────────────────────────
d.rep("""Sont des méthodes : les Chapitres 3 ✓, 7 ✓, 11 ✓, 10 et 12.""",
      """Sont des méthodes : les Chapitres 3 ✓, 7 ✓, 11 ✓, 12 ✓ et 10.""", 'familles, 12 coché')

d.rep("""<p><strong>Le Chapitre 11 est sorti des dualités en s'écrivant, comme le Chapitre 7, et pour le même
motif.</strong>""",
      """<p><strong>Le Chapitre 12 reste aux méthodes, et son illustration est un ajout de la
rédaction.</strong> Sa fiche n'en prévoyait pas. Sa thèse n'est pas qu'une chose se lit deux fois, c'est
qu'un même Bilan répond à trois questions différentes selon la manière dont on l'interroge&nbsp;; elle
n'entre donc pas aux dualités. <strong>Le motif de l'ajout est que cette thèse est une affaire de
proportions</strong> — 63~000~€ de créances clients contre 17~310~€ de trésorerie — et qu'une proportion se
montre mieux qu'elle ne se décrit. L'illustration met quatre lignes du Bilan à la même échelle, et le prix
de la machine à côté. <strong>Le test des axes passe&nbsp;:</strong> le composant fait bouger des curseurs,
l'illustration fait comparer des tailles. Le premier demande «~de combien faudrait-il~», la seconde répond
«~voilà où c'est~».</p>
<p><strong>Le Chapitre 11 est sorti des dualités en s'écrivant, comme le Chapitre 7, et pour le même
motif.</strong>""", 'illustration du Chapitre 12')

# ─── pied de document ───────────────────────────────────────────────────────
d.rep("""<p class="fin">Document de référence — Casoria, v22 du 25 août 2026. Livraison du Chapitre 11 et
reprise du Chapitre 10 en v5. Le Bilan de l'exercice boucle sur 130~410~€ des deux côtés, et le total de
contrôle du module vaut 1~294~694,00~€ au débit comme au crédit. Ce qui suit est le bilan de la v20, gardé
pour son raisonnement.""",
      """<p class="fin">Document de référence — Casoria, v23 du 26 août 2026. Livraison du Chapitre 12.
Douze chapitres écrits sur treize. Le scénario chiffré de la section 3 est inchangé et reste vérifié&nbsp;:
le Bilan de l'exercice boucle sur 130~410~€ des deux côtés, et le total de contrôle du module vaut
1~294~694,00~€ au débit comme au crédit — ce chapitre ne passe aucune écriture et ne pouvait donc rien y
changer. <strong>Tous les chiffres du Chapitre 12 ont été recalculés depuis les panneaux des onze
chapitres précédents</strong>, par <code>outils/verif_ratios.py</code>, et confrontés un à un au texte.
Le recensement des précisions, section 6, couvre douze chapitres sur treize. Trois vigilances de vocabulaire
entrent à la section 12, dont deux trouvées par script et non par un relecteur. <strong>La charte v14 est
inchangée</strong>&nbsp;: les deux candidats du chapitre n'ont qu'une attestation et vivent au journal de
rédaction. Ce qui suit est le bilan de la v20, gardé
pour son raisonnement.""", 'pied de document')

# ═══════════════════════════════════════════════════════════════════════════
# JOURNAL DE RÉDACTION
#   rattrape aussi ce que la répercussion du Chapitre 11 n'avait pas passé
# ═══════════════════════════════════════════════════════════════════════════

j.rep("""**Dernière mise à jour : 22 août 2026, livraison du Chapitre 8.**""",
      """**Dernière mise à jour : 26 août 2026, livraison du Chapitre 12.**""", 'date du journal')

# ─── avancement ─────────────────────────────────────────────────────────────
j.rep("""| 11 | La clôture | à écrire — **suivant** | — | 2 | — |
| 12 | Piloter | à écrire | — | — | — |
| 13 | Synthèse | à écrire | — | — | — |

Ordre de rédaction (déroulé, section 13) : 7 ✓, 2 ✓, 1 ✓, 3 ✓, 4 ✓, 5 ✓, 6 ✓, 8 ✓, puis **9**, puis 10,
11, puis 12 et 13.

**Huit chapitres écrits, huit livrés. Aucun en attente.**""",
      """| 11 | La clôture | **livré** (v2, 25 août) | 666 | 2 (2/1) | — |
| 12 | Piloter | **livré** (v2, 26 août) | 833 | — | — |
| 13 | Synthèse | à écrire — **suivant** | — | — | — |

Ordre de rédaction (déroulé, section 13) : 7 ✓, 2 ✓, 1 ✓, 3 ✓, 4 ✓, 5 ✓, 6 ✓, 8 ✓, 9 ✓, 10 ✓, 11 ✓,
12 ✓, puis **13**.

**Douze chapitres écrits, douze livrés. Aucun en attente.** Les Chapitres 10 v5, 11 et 12 ont été livrés
les 25 et 26 août ; les volumes du 10 et du 11 sont ceux du déroulé, section 13.

**Ce tableau était en retard d'un chapitre, et il faut le dire.** La répercussion du Chapitre 11 n'a touché
que la section du refrain de ce journal, laissant l'avancement, les déclarations, les relectures profanes
et les illustrations arrêtés au Chapitre 10. **Ce journal est le seul document qui permette de vérifier les
règles cumulatives** — refrain non recopié, terme coloré une seule fois, déclarations qui ne se ressemblent
pas — et une table en retard rend ce contrôle faux sans le signaler. Rattrapé le 26 août 2026, avec le
Chapitre 12. La leçon est celle des nombres annoncés : **une répercussion se vérifie table par table, pas
au souvenir de l'avoir faite.**""", 'avancement')

# ─── déclarations en gras ───────────────────────────────────────────────────
j.rep("""| 10 | **Laisser ces montants où ils sont ferait dire à l'année autre chose que ce qu'elle a fait.** |""",
      """| 10 | **Laisser ces montants où ils sont ferait dire à l'année autre chose que ce qu'elle a fait.** |
| 11 | **Le résultat figure au Passif parce qu'il appartient à quelqu'un d'autre que l'entreprise qui l'a gagné.** |
| 12 | **Ces 69 000 €, l'entreprise ne les a pas perdus, elle les a rangés dans son stock et dans les factures que ses clients n'ont pas encore payées.** |

**Le 11 est une subordonnée causale, le 12 une mise en relief par détachement avec reprise pronominale.**
Onze tournures distinctes sur douze chapitres — le détachement du 12 reprend la forme du Chapitre 3, neuf
chapitres plus tôt, ce que la règle de voisinage autorise largement. Les deux voisines immédiates du 12 ne
lui ressemblent pas : hypothétique à sujet infinitif au 10, causale au 11. **Une seule forme reste à
trouver, pour le Chapitre 13.**

**Ce que la déclaration du 12 a coûté à la relecture.** Elle disait « dans son café en stock » ; Pascal a
demandé « son stock », pour que l'image se transpose au métier du lecteur. Le fil rouge illustre, il ne
borne pas — et une déclaration en gras est l'endroit du chapitre où cela compte le plus, puisque c'est la
phrase que le lecteur emportera.""", 'déclarations 11 et 12')

# ─── relectures profanes ────────────────────────────────────────────────────
j.rep("""**Qui relit.** Pascal, qui ne connaît pas la matière enseignée.""",
      """**Ce que le Chapitre 12 change à cette table, et c'est le tour le plus lourd du module en volume.**
Vingt corrections, 165 mots ajoutés, un texte qui passe de 668 à 833. **Sept des vingt relèvent d'une seule
famille**, et elle est candidate à la charte avec une seule attestation : *définir un terme ne suffit pas à
l'introduire, il faut dire ce que l'opération fait et à quoi elle sert.* « L'autonomie financière rapporte
les capitaux propres au total du Bilan » est exacte, tient dans la définition du lexique, et Pascal l'a
déclarée incompréhensible. Le mot « ratio » était employé sans qu'on dise jamais que c'est une division ni
pourquoi on la fait ; les deux pourcentages étaient calculés sans qu'on dise ce qu'ils signifient — Pascal
demande explicitement « s'agit-il d'un simple constat, ou est-ce que ce ratio a une valeur et une
signification particulière ? ». **Une seconde attestation la porterait à la charte, section 12.**

**Trois corrections de la même série valent d'être notées à part.** « La réponse est non » répondait à une
question que l'accroche ne posait pas : une réponse ne se donne pas à une question qui n'a pas été posée,
et l'accroche pose désormais la question. « Ceux de Latitude Café » ne renvoyait à rien de nommé. « Trois
manières de le réduire » ne disait pas quoi. Les trois sont des ellipses de rédacteur, qui connaît le
référent.

**Une correction est une vigilance de module et est sortie à la section 12 du déroulé :** « nombres » ne
s'emploie pas pour des montants, écrire « chiffres » ou « sommes ». Candidate à la charte avec une seule
attestation, elle aussi.

**Et deux mots de fabrication ont été trouvés sans relecteur, ce qui est une première.** « exploitation »
et « poste » n'apparaissent dans aucun des onze chapitres livrés et le déroulé les écrit partout ; le
premier jet du 12 les employait trois fois. **Le contrôle est un `grep` et il est reproductible :** un mot
que le déroulé emploie et qu'aucun chapitre livré ne porte est un candidat au vocabulaire de fabrication.
**Cela nuance la limite que la charte, section 12, pose au dispositif** — « le rédacteur ne peut pas
trouver ces tournures seul » reste vrai des tournures, et devient partiellement faux des mots. À porter à
la charte si un second chapitre le confirme.

**Le Chapitre 11 en avait produit six**, toutes appliquées le 25 août 2026 : « le bénéfice d'avant impôt »
devenu « le bénéfice avant impôt » ; le renvoi au Chapitre 2 rendu explicite ; « le même nombre » accordé en
« la même somme » ; l'adjectif « petite » retiré du barème d'impôt, qui laissait supposer qu'une société
plus grosse est imposée autrement sur la première tranche ; la fin vague du troisième paragraphe refaite
sur les deux nombres ; et le sigle IS ajouté à la première occurrence de l'impôt sur les sociétés, seule
des six à être sortie au déroulé.

**Qui relit.** Pascal, qui ne connaît pas la matière enseignée.""", 'relectures profanes 11 et 12')

# ─── illustrations ──────────────────────────────────────────────────────────
j.rep("""**Une décision de relecture à retenir sur cette illustration.** Le sachet à 12~€ ne figure dans aucun""",
      """**Le Chapitre 11 et le Chapitre 12 ferment la série, et aucun des deux n'est une dualité.**
Le 11 porte le partage des 27 200 € entre réserve légale, dividende et report à nouveau, hors Bilan et hors
Compte de Résultat : sa dualité — les mêmes 27 200 € lus au bas du Compte de Résultat puis au Passif du
Bilan — est déjà déléguée à son bloc d'écritures, et une illustration sur le même axe aurait été le doublon
que le test des axes interdit. **La règle du Chapitre 7 s'en trouve élargie d'un cran** : un chapitre
illustre autre chose que sa dualité dès lors que celle-ci est déjà déléguée à un geste manipulable, que ce
geste soit un composant ou un bloc d'écritures. Porté au déroulé v22, section 14.

**Le 12 est un ajout de la rédaction, sa fiche n'en prévoyant aucune.** Il montre où l'argent se trouve au
31 décembre : quatre lignes du Bilan à la même échelle, et le prix de la machine à côté. **Le motif de
l'ajout est que la thèse du chapitre est une affaire de proportions** — 63 000 € de créances clients contre
17 310 € de trésorerie — et qu'une proportion se montre mieux qu'elle ne se décrit. Le test des axes passe :
le composant fait bouger des curseurs, l'illustration fait comparer des tailles. **Douze chapitres, dix
illustrations, et le principe de la chose lue deux fois n'a plus servi depuis le Chapitre 8.** Ce n'est pas
qu'il s'use : les quatre derniers chapitres sont des méthodes, et une méthode ne se montre pas deux fois.

**Une décision de relecture à retenir sur cette illustration.** Le sachet à 12~€ ne figure dans aucun""",
      'illustrations 11 et 12')

# ─── registre des écarts, état ──────────────────────────────────────────────
j.rep("""**51 entrées après le Chapitre 10, toutes formulées, recomptées par script. Le contrôle bloquant
d'avant-Chapitre 13 reste vert.**""",
      """**62 entrées après le Chapitre 12, toutes formulées, recomptées par script. Le contrôle bloquant
d'avant-Chapitre 13 reste vert.** Quarante-neuf candidates à l'aside, onze remontées en précision, deux en
module ultérieur. **Le décompte de fin du registre était faux** — il annonçait cinquante-quatre candidates
et deux précisions quand le fichier en portait déjà dix, avec un total juste, ce qui l'a rendu invisible.
Quatorzième nombre annoncé pris en défaut dans le module, corrigé le 26 août 2026 : les trois sous-totaux
se recomptent désormais par script, à la même passe que le total.""", 'état du registre')

j.rep("""- **Entrée 1.5**, les deux colonnes N et N–1 d'un état financier réel. À trancher **avant** d'écrire le
  Chapitre 12, seul endroit où une seconde colonne aurait un emploi réel plutôt que décoratif. Porté au
  déroulé, fiche du Chapitre 12.""",
      """- **Entrée 1.5 — fermée le 25 août 2026, et elle produit une règle.** Les deux colonnes N et N–1 d'un
  état financier réel sont sorties par le haut et sont devenues la précision du **Chapitre 12**, ancrée sur
  « tout seul ». **C'est le premier cas du module où une entrée remonte dans un autre chapitre que celui
  qui l'a produite** : elle n'avait pas d'ancre au Chapitre 1, où le lecteur regarde une grille vierge, et
  elle en a une au 12, où il lit un Bilan chiffré pour décider. **Le corollaire est un ordre de travail pour
  le Chapitre 13** — une entrée refusée comme précision de son propre chapitre n'est pas condamnée à
  l'aside, elle attend le chapitre où son ancre existe. Tranché avec Pascal avant rédaction, la fiche
  l'imposant. Porté au registre et au déroulé v23.
- **Les cinq entrées du Chapitre 12** ouvrent la famille de la *lecture des comptes* : les autres outils de
  lecture, le besoin en fonds de roulement réduit à trois lignes, son financement, les financements de court
  terme et les repères sectoriels. **12.4 part en module ultérieur** — l'escompte et l'affacturage appellent
  un chapitre entier, et c'est là qu'ira la question du second emprunt que le chapitre ne traite pas.
  **12.2 est la plus concrète du lot** au sens du critère 4 du tri : elle nomme les quatre lignes du Bilan
  que le calcul du chapitre omet, et le lecteur les a sous les yeux.""",
      'entrée 1.5 fermée et entrées du 12')

j.ecrire()
d.ecrire()

# ─── renommage du déroulé en v23 ────────────────────────────────────────────
os.rename('deroule-comprendre-la-comptabilite-v22.corps.html',
          'deroule-comprendre-la-comptabilite-v23.corps.html')
print('   déroulé renommé en v23')
