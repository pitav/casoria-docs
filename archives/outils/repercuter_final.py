#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Répercussion groupée de la passe des huit chapitres, 24 août 2026.
Registre des écarts, déroulé v19 → v20, charte v12 → v13.
Chaque substitution est assertée unique.
"""
import re
NB = '\u00a0'
assert NB == chr(160)

def sub(s, old, new, n=1, quoi=''):
    c = s.count(old)
    assert c == n, f'{quoi} : {c} occurrence(s) au lieu de {n} pour {old[:70]!r}'
    return s.replace(old, new)

# ══════════════════════ 1. REGISTRE DES ÉCARTS ══════════════════════════════
F = 'registredesecartscomprendrelacomptabilite.md'
r = open(F, encoding='utf-8').read()

# 6.4 sort par le haut
r = sub(r, "| 6.4 | Ce que le stock coûte à garder | notion non traitée | silencieux | candidat |",
        "| 6.4 | Ce que le stock coûte à garder | notion non traitée | signalé (précision) | **précision** |",
        quoi='registre 6.4')

# 7.5 sort par le haut
r = sub(r, "| 7.5 | Taux fixe uniquement | simplification de la simulation | silencieux | candidat |",
        "| 7.5 | Taux fixe uniquement | simplification de la simulation | signalé (précision) | **précision** |",
        quoi='registre 7.5')

# la table du Chapitre 7 était coupée en deux par une ligne vide
r = sub(r, """Deux lectures très différentes de la même machine. |

| 7.5 | Taux fixe uniquement""",
        """Deux lectures très différentes de la même machine. |
| 7.5 | Taux fixe uniquement""", quoi='registre table Ch. 7')

# notes de sortie par le haut
r = sub(r, """garder les deux apprendrait au lecteur qu'on se répète. Même configuration que 4.2 contre le Chapitre 10.""",
        """garder les deux apprendrait au lecteur qu'on se répète. Même configuration que 4.2 contre le Chapitre 10.

**Sortie par le haut de 6.4 — 24 août 2026, écrite.** Ancrée sur « sur""" + NB + """les""" + NB + """étagères », au troisième
sous-titre, sur la phrase qui dit qu'un stock trop gros fait dormir de l'argent. La note dit que ce café ne
fait pas que dormir, qu'il coûte — local, assurance, place, café qui vieillit — et qu'il représente chaque
année entre 15 et 25 % de sa valeur dans beaucoup de métiers.

**C'est un ordre de grandeur, ce que la charte, section 20, donne en exemple de ce qui remonte.** Et il se
vérifie sur le chapitre : le lecteur a 15 000 € sous les yeux, donc deux à quatre mille euros par an.
Elle n'a rien coûté au corps.

**Ce que le tri de 6.2 a produit, et qui vaut d'être gardé.** L'entrée « comment on met un prix sur un
stock » est **disqualifiée comme précision par le corollaire de la section 18** : son contenu *est*
l'origine des 15 000 €. Or sa formulation commence par « le chapitre donne 15 000 € sans dire d'où vient ce
nombre », ce qui est le constat d'un manque au corps et non le résumé d'un écart. **Question posée à la
passe, laissée ouverte** : faut-il écrire au corps du Chapitre 6 qu'un stock se valorise à ce qu'il a coûté
à produire, ou le nombre a-t-il le droit de rester un donné de la simulation ? La passe est une passe de
style et ne l'a pas tranché.""", quoi='registre note 6.4')

r = sub(r, """La consigne « au fil de la rédaction, jamais après » est confirmée par l'exception**, et le coût du
rattrapage est réel même sur trois phrases.""",
        """La consigne « au fil de la rédaction, jamais après » est confirmée par l'exception**, et le coût du
rattrapage est réel même sur trois phrases.

**Sortie par le haut de 7.5 — 24 août 2026, écrite.** Ancrée sur « le""" + NB + """plus""" + NB + """souvent », au deuxième
sous-titre, sur la phrase qui dit que la mensualité est constante. La note dit que le taux de Latitude Café
est fixe, qu'une banque peut aussi prêter à taux variable, et qu'alors la mensualité et son partage entre
intérêts et capital changent en cours de route.

**L'ancre est la réserve que le corps posait déjà.** Le texte écrivait « le plus souvent constante » sans
jamais dire ce qui arrive dans l'autre cas : une porte entrouverte et laissée telle quelle. C'est la forme
la plus nette de *ce que le corps ferme, la précision l'ouvre*, et **la première fois du module que
l'ancre est une concession du texte** plutôt qu'un nom ou un nombre. À chercher en priorité aux chapitres
suivants : un « le plus souvent », un « en général », un « presque toujours » est une précision qui
s'ignore.

**7.3, les garanties, était le second candidat** et son fait central est fort — l'engagement qui décide de
l'accord ne figure pas au Bilan. Écartée pour deux raisons : deux termes de métier à poser, et rien qui se
vérifie sur les écritures du chapitre.""", quoi='registre note 7.5')

# le compte des sorties par le haut
r = sub(r, """**Cinq entrées sont sorties par le haut et sont écrites**, au 24 août 2026 :""",
        """**Sept entrées sont sorties par le haut et sont écrites**, au 24 août 2026 :""",
        quoi='registre compte, tête')

r = sub(r, """« due""" + NB + """à""" + NB + """l'État » au Chapitre 5. **Cinq enseignements, un par cas.**""",
        """« due""" + NB + """à""" + NB + """l'État » au Chapitre 5 ; 6.4, ce que le stock coûte à garder, ancrée sur
« sur""" + NB + """les""" + NB + """étagères » au Chapitre 6 ; 7.5, le taux fixe, ancrée sur « le""" + NB + """plus""" + NB + """souvent » au
Chapitre 7. Le Chapitre 8 portait déjà la sienne, « cinq""" + NB + """ans », et la charte n'en autorise qu'une.
**Les huit chapitres écrits en portent donc chacun une, et la passe est close.**""",
        quoi='registre compte, liste')

open(F, 'w', encoding='utf-8').write(r)
print('registre mis à jour')

# ══════════════════════ 2. DÉROULÉ v19 → v20 ════════════════════════════════
G = 'deroule-comprendre-la-comptabilite-v19.corps.html'
d = open(G, encoding='utf-8').read()

d = d.replace('v19', 'v20').replace('v19'.upper(), 'v20'.upper())

d = sub(d, """<h2>Changements v20</h2>""", """<h2>Changements v20</h2>""", quoi='titre bloc')

# le bloc « Changements » ne garde que le sien
i = d.index('<h2>Changements v20</h2>')
j = d.index('<div class="note">', i)
nouveau = """<h2>Changements v20</h2>
<p>La passe de reprise des huit chapitres est faite. Le plan, le scénario chiffré et les écritures sont
intacts : aucune ligne n'a bougé, aucun montant, aucun libellé. Ce qui change est la ponctuation du corps,
le recensement des précisions et deux nombres annoncés.</p>
<ul>
<li><strong>Les huit chapitres sont repris sous le budget de deux-points</strong>, charte, section 10.
Mesure faite par script sur les huit fichiers livrés : ils portaient 191 deux-points dans leur corps, dont
123 en prose courante et jusqu'à 26 pour le seul Chapitre 8. Ils en portent <strong>34 en prose et 43 en
tout</strong>, soit trois à cinq par chapitre, et pas un chapitre au-dessus du budget. Le coût en mots est
nul : trois chapitres en ont gagné, trois en ont perdu deux ou moins, deux n'ont pas bougé.</li>
<li><strong>Le recensement des précisions, section 6, est complet.</strong> Les huit chapitres écrits en
portent chacun une. Trois sont nées de cette passe — « sur les étagères » au 6, « le plus souvent » au 7,
et avant elles « trente jours » au 4 et « due à l'État » au 5. Le Chapitre 8 portait déjà la sienne.</li>
<li><strong>Deux nombres annoncés sont corrigés.</strong> Le total de contrôle du Chapitre 7 passe de
300 258,60 € à <strong>341 528,90 €</strong>, faux depuis sa v11. Et les volumes des huit chapitres sont
recomptés au périmètre déclaré, dix d'entre eux ayant été pris en défaut. Voir la section 13.</li>
<li><strong>Le périmètre de comptage des mots est fixé et reproductible</strong> : l'accroche et le corps ;
en sortent la vidéo, les sous-titres, les blocs d'écritures, les légendes, l'illustration, le composant,
l'alerte, la précision et le bloc « Ce que vous avez appris ». Mesuré par script à chaque livraison, qui
refuse d'écrire si un nombre annoncé ne correspond pas.</li>
<li><strong>Un point de fond reste ouvert, au Chapitre 5</strong>, et la passe ne l'a pas tranché : la
légende du panneau automatique demande de regarder un total bouger <em>pendant</em> qu'une ligne s'inscrit,
ce qui est faux sur un écran étroit. Les deux réparations sont écrites à l'annexe du chapitre, l'une
rédactionnelle et l'autre à la charge du produit. Voir la section 4.</li>
<li><strong>Le module suit la charte v13.</strong> Toute la numérotation est inchangée, aucun renvoi à
corriger.</li>
</ul>
"""
d = d[:i] + nouveau + d[j:]

# section 6 : la ligne du Chapitre 8 gagne sa mention « Écrite. »
d = sub(d, '<tr><td class="ch">8</td><td class="cle">« cinq ans »</td><td>Que la durée',
        '<tr><td class="ch">8</td><td class="cle">«&nbsp;cinq&nbsp;ans&nbsp;»</td><td><strong>Écrite.</strong> Que la durée',
        quoi='déroulé ligne Ch. 8')

# le recensement gagne les Chapitres 6 et 7, en ordre
ancre_8 = '<tr><td class="ch">8</td><td class="cle">«&nbsp;cinq&nbsp;ans&nbsp;»</td>'
lignes_67 = (
 '<tr><td class="ch">6</td><td class="cle">«&nbsp;sur&nbsp;les&nbsp;étagères&nbsp;»</td>'
 '<td><strong>Écrite.</strong> Qu\'un stock ne fait pas que dormir, qu\'il coûte — un local à chauffer ou '
 'à refroidir, une assurance, de la place prise, du café qui vieillit — et qu\'il représente chaque année '
 'entre 15 et 25&nbsp;% de sa valeur dans beaucoup de métiers, ce qui change l\'arbitrage entre acheter en '
 'gros et acheter souvent. Ancrée au troisième sous-titre, sur la phrase de l\'argent qui dort. Vient de '
 'l\'entrée 6.4 du registre. <strong>C\'est un ordre de grandeur</strong>, ce que la charte, section 20, '
 'donne en exemple de ce qui remonte, et il se vérifie sur le chapitre — le lecteur a 15&nbsp;000&nbsp;€ '
 'sous les yeux.</td></tr>\n'
 '<tr><td class="ch">7</td><td class="cle">«&nbsp;le&nbsp;plus&nbsp;souvent&nbsp;»</td>'
 '<td><strong>Écrite.</strong> Que le taux de Latitude Café est fixe et sa mensualité constante, qu\'une '
 'banque peut aussi prêter à taux variable, et qu\'alors la mensualité et son partage entre intérêts et '
 'capital changent en cours de route — l\'échéancier signé n\'étant plus qu\'une prévision. Ancrée au '
 'deuxième sous-titre. Vient de l\'entrée 7.5 du registre. <strong>L\'ancre est la réserve que le corps '
 'posait déjà</strong>, « le plus souvent constante », sans jamais dire ce qui arrive dans l\'autre cas. '
 'Première fois du module que l\'ancre est une concession du texte plutôt qu\'un nom ou un nombre : à '
 'chercher en priorité aux chapitres suivants.</td></tr>\n')
d = sub(d, ancre_8, lignes_67 + ancre_8, quoi='déroulé recensement 6 et 7')

d = sub(d, 'État de la passe&nbsp;: Chapitres 1 à 5 faits, Chapitres 6 à 8 à traiter.',
        'État de la passe&nbsp;: les huit chapitres écrits sont repris, et chacun porte sa précision.',
        quoi='déroulé état de la passe')

# section 13 : les volumes recomptés et la passe close
d = sub(d, """Passe de reprise des huit chapitres écrits — à faire avant le Chapitre 9.""",
        """Passe de reprise des huit chapitres écrits — faite le 24 août 2026.""",
        quoi='déroulé s.13 titre')

d = sub(d, """Le Chapitre 1, rédigé et non livré, suit la même passe mais reste
en attente de sa relecture.""",
        """Le Chapitre 1, rédigé et non livré, a suivi la même passe mais reste
en attente de sa relecture. <strong>Résultat mesuré :</strong> 123 deux-points en prose ramenés à 34, de
trois à cinq par chapitre, à coût nul en mots. <strong>Sept entrées du registre sont sorties par le
haut</strong>, une par chapitre, la huitième précision étant celle que le Chapitre 8 portait déjà.
<strong>Ce que la passe a trouvé et qui n'était pas son objet :</strong> dix nombres annoncés faux, dont
le total de contrôle du Chapitre 7 ; un € manquant au Chapitre 5 que la coupe a rendu visible ; et deux
défauts des outils de vérification eux-mêmes, un compte à quatre chiffres et des centimes que le script de
rejeu ne savait pas lire.""", quoi='déroulé s.13 résultat')

for old, new in [
    ("822 mots", "822 mots"),
    ("Chapitre 4 — livré.</strong> 724 mots après la passe du 24 août, 717 avant elle — le nombre de 722 qu'il annonçait était faux.",
     "Chapitre 4 — livré.</strong> 724 mots, le nombre de 722 qu'il annonçait étant faux."),
]:
    if old in d and old != new:
        d = d.replace(old, new)

d = sub(d, 'Chapitre 6 — livré.</strong> 737 mots.',
        'Chapitre 6 — livré.</strong> 721 mots après la passe, le nombre de 737 qu\'il annonçait étant faux.',
        quoi='déroulé volume Ch. 6')

d = sub(d, 'Chapitre 8 — livré. 854 mots</strong>',
        'Chapitre 8 — livré. 858 mots après la passe</strong>, le nombre de 854 qu\'il annonçait étant faux,',
        quoi='déroulé volume Ch. 8')

open('deroule-comprendre-la-comptabilite-v20.corps.html', 'w', encoding='utf-8').write(d)
print('déroulé v20 écrit')

# ══════════════════════ 3. CHARTE v12 → v13 ═════════════════════════════════
H = 'charte-redaction-casoria-v12.corps.html'
c = open(H, encoding='utf-8').read()
c = c.replace('v12', 'v13')

c = sub(c, """<div class="oui"><span class="t">Écrire</span><p>Un associé peut prêter à sa propre société : c'est le compte courant d'associé, ouvert au Chapitre 2. Cette source est souple, elle se rembourse quand l'entreprise le peut.</p></div>""",
        """<div class="oui"><span class="t">Écrire</span><p>Un associé peut prêter à sa propre société. C'est le compte courant d'associé, ouvert au Chapitre 2. Cette source est souple, elle se rembourse quand l'entreprise le peut.</p></div>""",
        quoi='charte exemple s.10')

c = sub(c, """Les légendes de bloc,
les légendes d'illustration et les listes sortent du compte, ce qui ne les autorise pas à en porter un dont
on peut se passer.""",
        """Les légendes de bloc,
les légendes d'illustration et les listes sortent du compte, ce qui ne les autorise pas à en porter un dont
on peut se passer. <strong>Une note de précision, en revanche, est de la prose et compte dans sa
section</strong> : elle n'est pas toujours visible, mais quand elle l'est, elle se lit dans le fil.""",
        quoi='charte budget, note de précision')

open('charte-redaction-casoria-v13.corps.html', 'w', encoding='utf-8').write(c)
print('charte v13 écrite')
