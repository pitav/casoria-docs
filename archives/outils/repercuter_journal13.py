#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Répercute la livraison du Chapitre 13 au journal de rédaction.

Le journal est le seul document qui permette de vérifier les règles
cumulatives — refrain non recopié, terme coloré une seule fois, déclarations qui
ne se ressemblent pas. Une table en retard rend ce contrôle faux sans le
signaler : la leçon du Chapitre 12 est qu'une répercussion se vérifie table par
table, et non au souvenir de l'avoir faite.

Règle 3 des documents de référence : ce qui est porté à la charte ou au déroulé
sort du journal. Les tables cumulatives et les candidats non portés restent.

Chaque substitution est assertée unique. Le fichier est écrit à la toute fin.
"""
import re

F = 'journalderedactioncomprendrelacomptabilite.md'
s = open(F, encoding='utf-8').read()
_n = 0


def rep(old, new, label, n=1):
    global s, _n
    c = s.count(old)
    assert c == n, f'{label} : {c} occurrence(s), {n} attendue(s)'
    s = s.replace(old, new, n)
    _n += 1


# ═══════════════════════════════════════════════════════════════════════════
#  1.  Avancement
# ═══════════════════════════════════════════════════════════════════════════
rep('| 13 | Synthèse | à écrire — **suivant** | — | — | — |',
    '| 13 | Synthèse et feuille de route | **livré** (v2, 27 août) | 584 | — | — |',
    'ligne 13 de l\'avancement')

rep('''Ordre de rédaction (déroulé, section 13) : 7 ✓, 2 ✓, 1 ✓, 3 ✓, 4 ✓, 5 ✓, 6 ✓, 8 ✓, 9 ✓, 10 ✓, 11 ✓,
12 ✓, puis **13**.

**Douze chapitres écrits, douze livrés. Aucun en attente.** Les Chapitres 10 v5, 11 et 12 ont été livrés
les 25 et 26 août ; les volumes du 10 et du 11 sont ceux du déroulé, section 13.''',
    '''Ordre de rédaction (déroulé, section 13) : 7 ✓, 2 ✓, 1 ✓, 3 ✓, 4 ✓, 5 ✓, 6 ✓, 8 ✓, 9 ✓, 10 ✓, 11 ✓,
12 ✓, 13 ✓.

**Treize chapitres écrits, treize livrés. Le module est complet.** Le Chapitre 13 a été livré le
27 août 2026, en deux versions : 549 mots au premier jet, 584 après un tour de relecture profane de sept
corrections. **C'est le plus court du module après le Chapitre 7**, et le seul sans écriture, sans
composant et sans illustration.''',
    'bilan de l\'avancement')

# ═══════════════════════════════════════════════════════════════════════════
#  2.  Le refrain — quatrième reprise écrite
# ═══════════════════════════════════════════════════════════════════════════
rep('''| 7 | « Le résultat et le solde bancaire ne mesurent pas la même chose, et ils ne bougent pas aux mêmes moments. » |''',
    '''| 7 | « Le résultat et le solde bancaire ne mesurent pas la même chose, et ils ne bougent pas aux mêmes moments. » |
| 13 | **Reprise par le lieu**, ce qu'aucune des trois précédentes n'avait fait. « C'est pourquoi le bénéfice et le compte en banque ne se lisent pas au même endroit. Le bénéfice de 27 200 € est au bas du Compte de Résultat, le film. Les 17 310 € du compte en banque sont au Bilan, la photo. » Puis l'écart lui-même est rejoué en un paragraphe, sur la vente de 1 450 € du Chapitre 4. |''',
    'ligne 13 du refrain')

rep('''Reprises prévues au déroulé : chapitres 4 ✓ (installation), 5 ✓, 7 ✓, 10 et 12.''',
    '''**Ce que la reprise du Chapitre 13 a coûté, et qui est propre à un chapitre de synthèse.** Elle était
sèche au premier jet — une subordonnée en fin de phrase — et Pascal l'a refusée : *« au sujet de l'écart il
faut le ré-expliquer une dernière fois sinon la phrase est un peu compliquée à comprendre. Car en cette fin
de formation on a vu beaucoup de chiffres et de notions et la notion d'écart est déjà lointaine. »*
**La règle qui en sort, et qui contredit en partie ce que le Chapitre 5 avait établi :** une reprise peut
être sèche tant que la notion est fraîche ; au dernier chapitre elle ne le peut plus, parce que douze
chapitres de chiffres se sont interposés. La reprise finale d'un module se paie un paragraphe.

Reprises prévues au déroulé : chapitres 4 ✓ (installation), 5 ✓, 7 ✓, 10 et 12.''',
    'leçon du refrain au Chapitre 13')

# ═══════════════════════════════════════════════════════════════════════════
#  3.  Termes du lexique déjà colorés
# ═══════════════════════════════════════════════════════════════════════════
rep('''**Actif et Passif ne sont pas recolorés au Chapitre 2.**''',
    '''**Les Chapitres 9 à 13 n'en colorent aucun**, tous les termes du lexique ayant été introduits au
Chapitre 8. **Le Chapitre 13 non plus, et c'est une décision de plus qu'il a fallu prendre :** son
glossaire reprend les soixante-dix entrées du lexique, et il ne les colore pas. La couleur dit *où la
notion est définie*, et ce n'est pas là ; la colorer ferait du glossaire un second lieu de définition et
contredirait la case de la checklist qui veut un terme coloré une seule fois. Le glossaire les distingue
par la structure de sa table, pas par la couleur.

**Actif et Passif ne sont pas recolorés au Chapitre 2.**''',
    'note sur les termes colorés au Chapitre 13')

# ═══════════════════════════════════════════════════════════════════════════
#  4.  Déclarations en gras — la douzième forme
# ═══════════════════════════════════════════════════════════════════════════
rep('''| 12 | **Ces 69 000 €, l'entreprise ne les a pas perdus, elle les a rangés dans son stock et dans les factures que ses clients n'ont pas encore payées.** |''',
    '''| 12 | **Ces 69 000 €, l'entreprise ne les a pas perdus, elle les a rangés dans son stock et dans les factures que ses clients n'ont pas encore payées.** |
| 13 | **Désormais, ce que vous savez lire n'est pas le Bilan de Latitude Café, c'est n'importe quel bilan !** |''',
    'ligne 13 des déclarations')

rep('''**Le 11 est une subordonnée causale, le 12 une mise en relief par détachement avec reprise pronominale.**
Onze tournures distinctes sur douze chapitres — le détachement du 12 reprend la forme du Chapitre 3, neuf
chapitres plus tôt, ce que la règle de voisinage autorise largement. Les deux voisines immédiates du 12 ne
lui ressemblent pas : hypothétique à sujet infinitif au 10, causale au 11. **Une seule forme reste à
trouver, pour le Chapitre 13.**''',
    '''**Le 11 est une subordonnée causale, le 12 une mise en relief par détachement avec reprise pronominale.**
Onze tournures distinctes sur douze chapitres — le détachement du 12 reprend la forme du Chapitre 3, neuf
chapitres plus tôt, ce que la règle de voisinage autorise largement. Les deux voisines immédiates du 12 ne
lui ressemblent pas : hypothétique à sujet infinitif au 10, causale au 11.

**Le 13 est une pseudo-clivée en « ce que… c'est… », et la prédiction écrite ici est tenue : c'était la
douzième forme, et il en restait une à trouver.** Elle se distingue de l'extraction « c'est… que » du
Chapitre 6, sept chapitres plus tôt, et de ses deux voisines immédiates. **Quinze mots**, sous le seuil que
ce journal garde en candidat depuis le Chapitre 4. Elle déclare l'idée que le chapitre ajoute, comme la
leçon du Chapitre 10 l'impose : la compétence est transférable.

**Deux choses lui sont propres, et toutes deux viennent de la relecture.** Elle porte le seul point
d'exclamation du module, et elle commence par « Désormais » — Pascal a demandé les deux. Le mot situe la
déclaration dans le temps du lecteur plutôt que dans celui de l'entreprise, ce qu'aucune des douze autres
n'avait à faire. **Et elle fait lever un contrôle par script sans être fautive** : la case « bilan jamais
en minuscules » de `controle_checklist.py` ignore le cas du bilan réel et générique, que la charte,
section 9, autorise. Le Chapitre 8 livré la fait lever deux fois pour le même motif — **seconde
attestation, la case est à affiner et non le texte.**''',
    'note sur la douzième forme')

# ═══════════════════════════════════════════════════════════════════════════
#  5.  Relectures profanes — le tour du Chapitre 13
# ═══════════════════════════════════════════════════════════════════════════
rep('''| 3 | « C'est le principe de la partie double », dans le sous-titre et dans le corps.''',
    '''| 13 | « **Ils** ne racontent pourtant pas la même chose » ; « la photo prise le dernier soir » ; « au bas du **film** », « sur la **photo** ». Trois corrections de la même famille, attestées par Pascal en fin de parcours : un pronom ou une image ne suffisent plus à désigner ce dont on parle après douze chapitres de chiffres et de notions. | « **Le Bilan et le Compte de Résultat** ne racontent pourtant pas… » ; « la photo **de l'entreprise au dernier soir de l'exercice** » ; « au bas **du Compte de Résultat, le film** » et « **au Bilan, la photo** ». **Famille candidate, une seule attestation** : *en fin de parcours, une image se rattache à son document à chaque emploi*. |
| 13 | « … et le Chapitre 4 avait fait naître **l'écart** le jour où une facture de 1 450 € devenait une créance client. » Subordonnée en fin de phrase. Attestée par Pascal : « il faut le ré-expliquer une dernière fois, la notion d'écart est déjà lointaine ». | Un paragraphe entier, où le mécanisme est rejoué : « Cet écart entre ce que l'entreprise a gagné et ce qu'elle a sur son compte… le Compte de Résultat comptait la vente le jour même quand le compte en banque, lui, n'avait encore rien reçu. » **Trente mots de coût.** Seconde attestation de la même famille : une notion ancienne se ré-explique dans le chapitre de synthèse. |
| 13 | « Treize chapitres suivent une entreprise sur une année, et une entreprise sur une année ne rencontre pas tout. » Formule d'auteur : elle fait un effet de style là où le lecteur attend ce qui a été écarté et pourquoi. | « Les treize chapitres de ce module suivent Latitude Café sur une année sans évoquer certains cas, pour les besoins de la formation. Ils ont été écartés à dessein, parce qu'ils ne servaient que de loin ce que ce module voulait vous apprendre à lire. » |
| 13 | « Ce que vous savez lire n'est pas le Bilan de Latitude Café, c'est n'importe quel bilan. » Déclaration en gras. | « **Désormais**, ce que vous savez lire … c'est n'importe quel bilan **!** » Le seul point d'exclamation du module, et le seul « désormais » d'une déclaration. Demandé par Pascal. |
| 13 | « … parce qu'ils **touchent** de trop loin à ce que ce module voulait vous apprendre. » **Entré par une correction de relecture et non par le premier jet**, et attrapé par `verif_ch13.py` et non par un relecteur. Le verbe est une vigilance du module depuis le Chapitre 6. | « … parce qu'ils **ne servaient que de loin** ce que ce module voulait vous apprendre à lire. » **Premier cas du module où un mot proscrit entre par une correction : les corrections repassent les contrôles comme le premier jet.** |
| 3 | « C'est le principe de la partie double », dans le sous-titre et dans le corps.''',
    'tour de relecture du Chapitre 13')

# ═══════════════════════════════════════════════════════════════════════════
#  6.  Illustrations
# ═══════════════════════════════════════════════════════════════════════════
rep('''**Douze chapitres, dix
illustrations, et le principe de la chose lue deux fois n'a plus servi depuis le Chapitre 8.** Ce n'est pas
qu'il s'use : les quatre derniers chapitres sont des méthodes, et une méthode ne se montre pas deux fois.''',
    '''**Treize chapitres, dix
illustrations, et le principe de la chose lue deux fois n'a plus servi depuis le Chapitre 8.** Ce n'est pas
qu'il s'use : les cinq derniers chapitres sont des méthodes ou une synthèse, et ni l'une ni l'autre ne se
montre deux fois.

**Le Chapitre 13 n'en porte aucune, et c'est le seul du module.** Il n'entre dans aucune des deux familles
de la section 14 du déroulé : il ne démontre rien, il reprend, il nomme et il oriente. **Surtout, l'axe est
déjà pris** — le seul geste qu'une illustration pourrait faire ici est de montrer les deux documents
complets, ce que sa fiche confie précisément à leur affichage, et le test des axes l'interdit. Le motif est
porté au déroulé v24, section 14.''',
    'illustrations du Chapitre 13')

# ═══════════════════════════════════════════════════════════════════════════
#  7.  Registre des écarts — état
# ═══════════════════════════════════════════════════════════════════════════
rep('''**62 entrées après le Chapitre 12, toutes formulées, recomptées par script. Le contrôle bloquant
d'avant-Chapitre 13 reste vert.** Quarante-neuf candidates à l'aside, onze remontées en précision, deux en
module ultérieur.''',
    '''**63 entrées après le Chapitre 13, toutes formulées, recomptées par script. Le tri est fait, et il ne se
refera pas.** Onze retenues à l'aside, douze remontées en précision, six en module ultérieur, trente-quatre
non retenues et conservées. **Le contrôle d'avant-tri est passé**, sa troisième case par défaut : les six
entrées `module ultérieur` restent écrites au registre tant qu'aucun des déroulés qui doivent les recevoir
n'existe. **Le registre a gagné une quatrième valeur de destination, `aside`** — sans elle, le tri n'était
plus vérifiable par script, et les quatre sous-totaux se recomptent désormais à chaque écriture du fichier.''',
    'état du registre')

rep('''- **Entrée 1.5 — fermée le 25 août 2026, et elle produit une règle.**''',
    '''- **Entrée 1.4 — fermée le 27 août 2026, et elle vérifie la règle que 1.5 avait produite.** Les formats
  de présentation d'un état financier sont sortis par le haut et sont devenus la précision du
  **Chapitre 13**, ancrée sur « la même allure ». **Second cas du module où une entrée remonte dans un
  autre chapitre que celui qui l'a produite, et les deux viennent du Chapitre 1** — celui qui montre les
  documents avant que le lecteur n'ait de raison de les comparer à d'autres. Le corollaire que la fiche du
  Chapitre 12 posait comme ordre de travail est donc tenu. Porté au registre et au déroulé v24.
- **Le tri du Chapitre 13 — fait le 27 août 2026.** Quarante-neuf candidates, onze retenues, et le motif
  de chacune est à l'annexe du chapitre. **Deux écartées le sont contre ce que le registre prévoyait**, et
  ce sont elles qu'une relecture doit regarder : 10.4, que la note du Chapitre 10 favorisait par le
  critère 4, écartée parce que l'activité de ce chapitre fait déjà manipuler la symétrie ; et 1.3, **la
  première à rouvrir** si la place paraît trop chère payée. **Trois candidates passent en module
  ultérieur** — 2.4 et 9.1 vers « choisir sa forme juridique », comme la note sur 2.4 le demandait, et 4.4
  vers le module qui reçoit déjà 12.4.
- **L'entrée propre du Chapitre 13 est la seule, et elle ne va pas à l'aside.** 13.1, qui tient les comptes
  et avec quoi. **Un chapitre de synthèse n'alimente pas le registre, il le vide** : le contrôle qui exige
  au moins une entrée par chapitre est tenu de justesse, et le cas vaut d'être noté pour les modules à
  venir.
- **Entrée 1.5 — fermée le 25 août 2026, et elle produit une règle.**''',
    'entrées 1.4 et tri au registre')

# ═══════════════════════════════════════════════════════════════════════════
#  8.  Ce qu'il faut redonner — les versions en vigueur
# ═══════════════════════════════════════════════════════════════════════════
rep('- **La charte de rédaction — v11** depuis le 22 août. La v10 ne fait plus autorité.',
    '- **La charte de rédaction — v15** depuis le 27 août. Les versions antérieures ne font plus autorité.',
    'version de la charte')
rep('- **Le déroulé du module — v18** depuis le 22 août. La v17 ne fait plus autorité.',
    '- **Le déroulé du module — v24** depuis le 27 août. Les versions antérieures ne font plus autorité.',
    'version du déroulé')

# ── la prédiction sur les formes de déclaration est close ───────────────────
rep('''**Neuf formes employées sur treize chapitres, et trois restent à écrire.** Les formes disponibles sont en
nombre fini, et la charte ne vise que le voisinage pour cette raison. La prédiction écrite ici s'est
vérifiée dès le chapitre annoncé.''',
    '''**Douze formes employées sur treize chapitres, et il n'en reste aucune à écrire.** Les formes
disponibles sont en nombre fini, et la charte ne vise que le voisinage pour cette raison. **Les deux
prédictions écrites ici sont tenues** : celle qui annonçait la forme du Chapitre 10 s'est vérifiée dès le
chapitre annoncé, et celle qui disait qu'une seule forme restait à trouver pour le 13 aussi. Une seule
forme se répète sur les treize, les deux propositions parallèles des Chapitres 1 et 8, à sept chapitres
d'écart — ce que la règle de voisinage autorise largement.''',
    'clôture de la prédiction sur les formes')

assert '<' not in s.split('## Avancement')[0][:0] + ''  # garde-fou muet
open(F, 'w', encoding='utf-8').write(s)
print(f'journal répercuté — {_n} substitutions')
