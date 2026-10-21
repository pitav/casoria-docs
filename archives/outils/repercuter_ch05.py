#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Répercute la passe du Chapitre 5 sur le registre des écarts et le déroulé.
Le déroulé reste en v19 pendant toute la passe ; il basculera en v20 à la fin.
"""
import re
NB = '\u00a0'

def sub(s, old, new, n=1, quoi=''):
    c = s.count(old)
    assert c == n, f'{quoi} : {c} occurrence(s) au lieu de {n} pour {old[:60]!r}'
    return s.replace(old, new)

# ══════════════════════ registre des écarts ═════════════════════════════════
F = 'registredesecartscomprendrelacomptabilite.md'
r = open(F, encoding='utf-8').read()

r = sub(r,
    '| 5.5 | TVA due à la facture ou à l\'encaissement | cas particulier ignoré | silencieux | candidat |',
    '| 5.5 | TVA due à la facture ou à l\'encaissement | cas particulier ignoré | signalé (précision) | **précision** |',
    quoi='registre 5.5')

r = sub(r,
    """Hors d'Europe, c'est la douane qui l'encaisse à l'entrée. |

### Chapitre 6 — Produire et stocker""",
    """Hors d'Europe, c'est la douane qui l'encaisse à l'entrée. |

**Sortie par le haut de 5.5 — 24 août 2026, écrite.** Ancrée sur « due""" + NB + """à""" + NB + """l'État », au deuxième
sous-titre, sur la phrase qui définit la TVA à décaisser. La note dit que l'entreprise doit la taxe dès
qu'elle facture, sans attendre d'être payée, et que la règle s'inverse pour qui vend des services.

**Elle ne coûte rien au corps, et c'est l'inverse du Chapitre 4.** Le corollaire de la charte, section 18,
interdit à une précision de porter d'où sort un nombre ; ici les trois nombres qu'elle entoure — 7 800,
6 600 et 1 200 — ont tous leur origine écrite au corps, le chapitre entier étant construit pour la
produire. **Ce que les deux cas apprennent ensemble :** le corollaire ne coûte quelque chose que sur un
nombre venu du décor, jamais sur un nombre que le chapitre démontre. Les trente jours du Chapitre 4
étaient du décor.

**Pourquoi elle plutôt que les cinq autres.** 5.2 tombe sous l'exception absolue et ne peut dépendre d'un
clic. 5.4 emploierait le vocabulaire du Chapitre 8. 5.3 décrit une situation où Latitude Café n'est pas,
donc rien ne s'y vérifie sur les écritures du chapitre — critère posé au Chapitre 3 — et le corps la
signale déjà. 5.1 répéterait l'`<UAlert>` qui est trois paragraphes plus bas. 5.6 demande deux régimes,
donc deux paragraphes.

**L'exception absolue a été vérifiée pour 5.5 elle-même, et elle ne s'applique pas.** Le mécanisme du
chapitre vaut à l'identique pour qui vend des services : seule la date de naissance de la dette change.
C'est une variante, pas une disqualification. **La distinction mérite d'être gardée pour le tri du
Chapitre 13** : l'exception vise ce qui dit *ce chapitre ne vous concerne pas*, pas ce qui dit *chez vous
le calendrier diffère*.

**Effet sur 5.3.** Le chapitre dit maintenant quand la dette naît. 5.3 porte ce que le remboursement
coûte en temps, ce qui reste entier et sans recoupement.

### Chapitre 6 — Produire et stocker""", quoi='registre note 5.5')

r = sub(r,
    """**Quatre entrées sont sorties par le haut et sont écrites**, au 24 août 2026 : 1.2, l'ordre de classement
des lignes du Bilan, ancrée sur « leur ordre » au Chapitre 1 ; 2.2, la libération partielle du capital,
ancrée sur « dès sa création » au Chapitre 2 ; 3.5, la logique des numéros du plan comptable, ancrée sur
« Ces numéros » au Chapitre 3 ; 4.1, le plafond légal des délais de paiement, ancrée sur
« trente""" + NB + """jours » au Chapitre 4. **Quatre enseignements, un par cas.**""",
    """**Cinq entrées sont sorties par le haut et sont écrites**, au 24 août 2026 : 1.2, l'ordre de classement
des lignes du Bilan, ancrée sur « leur ordre » au Chapitre 1 ; 2.2, la libération partielle du capital,
ancrée sur « dès sa création » au Chapitre 2 ; 3.5, la logique des numéros du plan comptable, ancrée sur
« Ces numéros » au Chapitre 3 ; 4.1, le plafond légal des délais de paiement, ancrée sur
« trente""" + NB + """jours » au Chapitre 4 ; 5.5, le moment où la TVA devient due, ancrée sur
« due""" + NB + """à""" + NB + """l'État » au Chapitre 5. **Cinq enseignements, un par cas.**""",
    quoi='registre compte des sorties')

r = sub(r,
    """aussi une relecture du corps, et le premier des quatre cas où elle a coûté des mots.""",
    """aussi une relecture du corps, et le premier des cinq cas où elle a coûté des mots. **Le Chapitre 5 a
donné la limite de cette leçon** : sa précision n'a rien coûté au corps, parce que les nombres qu'elle
entoure sont ceux que le chapitre démontre. Le corollaire se paie sur un nombre venu du décor, jamais
sur un nombre démontré.""",
    quoi='registre leçon du Ch. 5')

open(F, 'w', encoding='utf-8').write(r)
print('registre mis à jour')

# ══════════════════════ déroulé, v19 inchangée ══════════════════════════════
G = 'deroule-comprendre-la-comptabilite-v19.corps.html'
d = open(G, encoding='utf-8').read()

ancre_8 = '<tr><td class="ch">8</td><td class="cle">« cinq ans »</td>'
ligne_5 = ('<tr><td class="ch">5</td><td class="cle">«&nbsp;due&nbsp;à&nbsp;l\'État&nbsp;»</td>'
           '<td><strong>Écrite.</strong> Que l\'entreprise doit la taxe dès qu\'elle facture, sans '
           'attendre d\'être payée — les 1&nbsp;200&nbsp;€ du trimestre partent au Trésor public même si '
           'les clients n\'ont pas encore réglé — et que la règle s\'inverse avec le métier, qui vend des '
           'services ne devant sa taxe qu\'une fois encaissé. Ancrée au deuxième sous-titre, sur la phrase '
           'qui définit la TVA à décaisser. Vient de l\'entrée 5.5 du registre, qui sort par le haut. '
           '<strong>Elle ne coûte rien au corps</strong>, à l\'inverse de celle du Chapitre 4 : les trois '
           'nombres qu\'elle entoure sont ceux que le chapitre démontre, et le corollaire de la charte, '
           'section 18, ne se paie que sur un nombre venu du décor. <strong>L\'exception absolue de la '
           'section 20 a été vérifiée et écartée</strong> : le mécanisme du chapitre vaut à l\'identique '
           'pour qui vend des services, seule la date de naissance de la dette change. C\'est une '
           'variante, pas une disqualification — à distinguer de 5.2, la franchise en base, qui reste au '
           'registre pour ce motif exact.</td></tr>\n')
d = sub(d, ancre_8, ligne_5 + ancre_8, quoi='déroulé recensement')

d = sub(d,
    'État de la passe&nbsp;: Chapitres 1, 2, 3 et 4 faits, Chapitres 5 à 8 à traiter.',
    'État de la passe&nbsp;: Chapitres 1 à 5 faits, Chapitres 6 à 8 à traiter.',
    quoi='déroulé état de la passe')

d = sub(d,
    'Chapitre 5 — livré.</strong> 802 mots.',
    'Chapitre 5 — livré.</strong> 797 mots après la passe du 24 août, et 797 avant elle — le nombre de '
    '802 qu\'il annonçait était faux, et la passe n\'a rien coûté.',
    quoi='déroulé section 13, volume')

d = sub(d,
    'rejouer le journal du module écriture\npar écriture, plutôt que raisonner sur la comptabilité générale. Une phrase qui décrit ce que la grille\naffiche ne se vérifie pas autrement.',
    'rejouer le journal du module écriture\npar écriture, plutôt que raisonner sur la comptabilité générale. Une phrase qui décrit ce que la grille\naffiche ne se vérifie pas autrement. <strong>Repris le 24 août&nbsp;:</strong> vingt-et-un deux-points en '
    'prose ramenés à quatre, le plus lourd des cinq chapitres repris, et l\'entrée 5.5 du registre sortie '
    'par le haut. <strong>Le point de fond signalé le 21 août reste ouvert</strong> — la légende du panneau '
    'automatique demande toujours de regarder un total bouger <em>pendant</em> qu\'une ligne s\'inscrit, et '
    'la passe n\'a pas le droit de trancher entre la réparation rédactionnelle et le pied de bloc. Les deux '
    'versions sont écrites à l\'annexe du chapitre.',
    quoi='déroulé section 13, passe')

open(G, 'w', encoding='utf-8').write(d)
print('déroulé mis à jour (reste en v19 jusqu\'à la fin de la passe)')
