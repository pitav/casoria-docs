#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Répercute la passe du Chapitre 4 sur le registre des écarts et le déroulé.
Le déroulé reste en v19 pendant toute la passe ; il basculera en v20 à la fin.
"""
import re
NB = ' '

def sub(s, old, new, n=1, quoi=''):
    c = s.count(old)
    assert c == n, f'{quoi} : {c} occurrence(s) au lieu de {n} pour {old[:60]!r}'
    return s.replace(old, new)

# ══════════════════════ registre des écarts ═════════════════════════════════
F = 'registredesecartscomprendrelacomptabilite.md'
r = open(F, encoding='utf-8').read()

# 1 — la ligne 4.1 change de statut et de destination
r = sub(r,
    '| 4.1 | Les délais de paiement sont encadrés par la loi | notion non traitée | silencieux | candidat |',
    '| 4.1 | Les délais de paiement sont encadrés par la loi | notion non traitée | signalé (précision) | **précision** |',
    quoi='registre 4.1')

# 2 — la note de sortie par le haut, après les notes du Chapitre 4
r = sub(r,
    """lues sur ses propres factures sans savoir ce qu'elles coûtent. Si une seule doit sortir, c'est 4.1 :
l'ignorance du plafond légal a des conséquences, celle de l'escompte n'en a pas.
""",
    """lues sur ses propres factures sans savoir ce qu'elles coûtent. Si une seule doit sortir, c'est 4.1 :
l'ignorance du plafond légal a des conséquences, celle de l'escompte n'en a pas.

**Sortie par le haut de 4.1 — 24 août 2026, écrite.** Ancrée sur « trente""" + NB + """jours », au premier
sous-titre, dans le paragraphe qui pose le délai. La note porte le plafond de soixante jours, l'amende
encourue au-delà et les pénalités dues dès le lendemain de l'échéance. Le pronostic de la note ci-dessus
est donc tenu, et c'est la première fois que le registre le vérifie.

**Ce que le corps a dû recevoir.** Le corollaire de la charte, section 18, interdit à une précision de
porter d'où sort un nombre. Le chapitre écrivait « Le délai figure sur la facture, ici c'est trente jours »,
ce qui ne disait pas que ces trente jours sont un accord entre deux entreprises. Il écrit désormais
« Le délai est convenu entre les deux entreprises et figure sur la facture », et la précision se contente
des limites. **Huit mots au corps pour qu'une note de trois lignes reste licite** : c'est le prix du
corollaire, mesuré pour la première fois.

**Ce que la formulation du registre avait de faux.** Elle mettait l'amende sur le fournisseur seul. La
sanction porte sur la clause et sur le retard, donc sur les deux parties. Corrigé dans la note du
chapitre ; la formulation ci-dessus reste telle quelle, l'entrée étant sortie et n'ayant plus à servir
l'aside.

**Ce qui a été écarté de la note, et qui reste ici.** La variante des quarante-cinq jours fin de mois. Une
note de trois lignes ne porte pas deux nombres et une locution de métier, et un seul repère retenu vaut
mieux que deux confondus.

**Effet sur 4.3.** Les pénalités de retard sont désormais dites au lecteur. L'entrée 4.3 garde l'escompte
de règlement, qui est la moitié la moins utile des deux, et part au tri avec un handicap nouveau.
""", quoi='registre note 4.1')

# 3 — le compte des sorties par le haut
r = sub(r,
    """**Trois entrées sont sorties par le haut et sont écrites**, au 23 août 2026 : 1.2, l'ordre de classement des
lignes du Bilan, ancrée sur « leur ordre » au Chapitre 1 ; 2.2, la libération partielle du capital, ancrée
sur « dès sa création » au Chapitre 2 ; 3.5, la logique des numéros du plan comptable, ancrée sur « Ces
numéros » au Chapitre 3. **Trois enseignements, un par cas.**""",
    """**Quatre entrées sont sorties par le haut et sont écrites**, au 24 août 2026 : 1.2, l'ordre de classement
des lignes du Bilan, ancrée sur « leur ordre » au Chapitre 1 ; 2.2, la libération partielle du capital,
ancrée sur « dès sa création » au Chapitre 2 ; 3.5, la logique des numéros du plan comptable, ancrée sur
« Ces numéros » au Chapitre 3 ; 4.1, le plafond légal des délais de paiement, ancrée sur
« trente""" + NB + """jours » au Chapitre 4. **Quatre enseignements, un par cas.**""",
    quoi='registre compte des sorties')

r = sub(r,
    """été confrontées au même test et sont restées — trois demandaient un paragraphe, deux parlaient de comparer
deux exercices, ce que ce chapitre ne fait pas.""",
    """été confrontées au même test et sont restées — trois demandaient un paragraphe, deux parlaient de comparer
deux exercices, ce que ce chapitre ne fait pas. **Et ce que le Chapitre 4 ajoute : une précision se paie au
corps.** Le corollaire qui interdit de lui confier l'origine d'un nombre oblige à écrire cette origine
là où elle manquait, et le chapitre l'ignorait sans que personne l'ait vu. Chercher une précision est donc
aussi une relecture du corps, et le premier des quatre cas où elle a coûté des mots.""",
    quoi='registre leçon du Ch. 4')

open(F, 'w', encoding='utf-8').write(r)
print('registre mis à jour')

# ══════════════════════ déroulé, v19 inchangée ══════════════════════════════
G = 'deroule-comprendre-la-comptabilite-v19.corps.html'
d = open(G, encoding='utf-8').read()

# 1 — une ligne au recensement des précisions, à sa place dans l'ordre
ancre_8 = '<tr><td class="ch">8</td><td class="cle">« cinq ans »</td>'
ligne_4 = ('<tr><td class="ch">4</td><td class="cle">«&nbsp;trente&nbsp;jours&nbsp;»</td>'
           '<td><strong>Écrite.</strong> Que la liberté des deux entreprises n\'est pas entière — entre '
           'professionnels, la loi plafonne le délai de paiement à soixante jours à compter de la facture, '
           'un délai plus long les expose à une amende, et un client qui paie en retard doit des pénalités '
           'dès le lendemain de l\'échéance même si personne ne les lui réclame. Ancrée au premier '
           'sous-titre, dans le paragraphe qui pose le délai. Vient de l\'entrée 4.1 du registre, qui sort '
           'par le haut. <strong>Le corps a reçu l\'origine du nombre</strong> — «&nbsp;Le délai est convenu '
           'entre les deux entreprises et figure sur la facture&nbsp;» — la charte, section 18, interdisant '
           'à une précision de porter d\'où sort un nombre. Huit mots ajoutés au corps pour trois lignes de '
           'note, et c\'est la première fois que le corollaire se chiffre. La variante des quarante-cinq '
           'jours fin de mois est écartée de la note et reste au registre.</td></tr>\n')
d = sub(d, ancre_8, ligne_4 + ancre_8, quoi='déroulé recensement')

# 2 — l'état de la passe
d = sub(d,
    'État de la passe&nbsp;: Chapitres 1, 2 et 3 faits, Chapitres 4 à 8 à traiter.',
    'État de la passe&nbsp;: Chapitres 1, 2, 3 et 4 faits, Chapitres 5 à 8 à traiter.',
    quoi='déroulé état de la passe')

# 3 — la ligne du Chapitre 4 à l'ordre de rédaction
d = sub(d,
    '722 mots. Cinq tours de relecture, vingt-trois corrections, sept tournures illisibles.',
    '724 mots après la passe du 24 août, 717 avant elle — le nombre de 722 qu\'il annonçait était faux. '
    'Cinq tours de relecture, vingt-trois corrections, sept tournures illisibles.',
    quoi='déroulé section 13, volume')

d = sub(d,
    'Il a aussi changé le libellé du refrain central et fait entrer « s\'éteindre » aux vigilances de vocabulaire.',
    'Il a aussi changé le libellé du refrain central et fait entrer « s\'éteindre » aux vigilances de '
    'vocabulaire. <strong>Repris le 24 août&nbsp;:</strong> treize deux-points en prose ramenés à cinq, '
    'sans qu\'aucune écriture bouge, et l\'entrée 4.1 du registre sortie par le haut. C\'est le chapitre '
    'de la passe qui a montré que <strong>chercher une précision oblige à relire le corps</strong>, le '
    'corollaire de la charte, section 18, imposant d\'y écrire l\'origine du nombre que la note vient '
    'entourer.',
    quoi='déroulé section 13, passe')

open(G, 'w', encoding='utf-8').write(d)
print('déroulé mis à jour (reste en v19 jusqu\'à la fin de la passe)')
