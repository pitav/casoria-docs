#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Répercute la livraison de l'avant-propos aux documents de référence.

Modèle : repercuter_ch0910.py (classe Doc, motif tolérant les trois formes
d'espace) et repercuter_ch13.py (assertion sur chaque substitution, écriture à
la toute fin).

  charte v15 → v16   la forme courte de la promesse (section 1) et l'avant-propos
                     d'un module (section 2). Les deux par décision du décideur.
  déroulé v24 → v25  la clause du terme employé avant son chapitre (section 11),
                     l'avant-propos au tableau de la section 9, à l'ordre de
                     rédaction et aux points ouverts, bloc « Changements v25 ».
  journal            tables cumulatives : avancement et déclarations en gras.

Aucune écriture, aucun montant, aucun composant ne bouge : le total de contrôle
du module est inchangé.
"""
import re

NB = chr(0xA0)
assert NB == chr(160)


class Doc:
    """Un document de référence. Les motifs tolèrent les trois formes d'espace
    — ordinaire, insécable littéral, entité &nbsp; — et les retours à la ligne
    du source, le découpage se faisant sur split() et non sur split(' ')."""

    def __init__(self, chemin):
        self.chemin = chemin
        self.s = open(chemin, encoding='utf-8').read()
        self.n = 0

    def _motif(self, txt):
        return r'(?:\s|&nbsp;)+'.join(re.escape(m) for m in txt.split())

    def rep(self, old, new, label):
        m = list(re.finditer(self._motif(old), self.s))
        assert len(m) == 1, f'{label} : {len(m)} occurrence(s), 1 attendue'
        self.s = self.s[:m[0].start()] + new + self.s[m[0].end():]
        self.n += 1
        return self

    def rep_bloc(self, debut, fin, new, label):
        """Remplace de `debut` jusqu'au début de `fin`, `fin` exclu."""
        a = list(re.finditer(self._motif(debut), self.s))
        assert len(a) == 1, f'{label} (début) : {len(a)} occurrence(s)'
        b = list(re.finditer(self._motif(fin), self.s[a[0].start():]))
        assert b, f'{label} (fin) : introuvable'
        j = a[0].start() + b[0].start()
        self.s = self.s[:a[0].start()] + new + self.s[j:]
        self.n += 1
        return self

    def ecrire(self, chemin=None):
        open(chemin or self.chemin, 'w', encoding='utf-8').write(self.s)
        print(f'   écrit : {chemin or self.chemin} — {self.n} substitution(s), '
              f'{len(self.s)} caractères')


# ═══════════════════════════════════════════════════════════════════════════
#  1.  La charte — v15 → v16
# ═══════════════════════════════════════════════════════════════════════════
C = Doc('charte-redaction-casoria-v15.corps.html')

C.rep('<p class="kicker">Casoria • Document de référence • v15</p>',
      '<p class="kicker">Casoria • Document de référence • v16</p>',
      'charte : kicker')

C.rep_bloc('<p class="chapo">Règles de rédaction des textes de chapitre',
           '<h2 class="nu">1 — La promesse</h2>',
           '''<p class="chapo">Règles de rédaction des textes de chapitre, applicables à tous les modules
de la plateforme. <strong>Cette v16 ne déplace aucune section et n'en crée aucune</strong>&nbsp;: elle
ajoute la forme courte de la promesse à la section 1 — «&nbsp;Simulez, Visualisez, Comprenez&nbsp;» — et
une clause à la section 2, sur l'avant-propos d'un module, qui n'a pas de gabarit. <strong>Les deux
entrent par décision du décideur et non par attestation</strong>, et elles sont écrites comme telles.
Toute la numérotation est inchangée, et tous les renvois faits depuis les déroulés de module restent
valides. Cette charte fait autorité sur la forme. Le déroulé de chaque module reste seul maître du fond,
du scénario aux chiffres, de la séquence au lexique. Une règle de forme ne se répète pas dans un déroulé,
elle s'y cite.</p>

''', 'charte : chapo')

C.rep('''<p>Cette phrase est le critère d'arbitrage de toutes les décisions de rédaction. Devant un choix
qui ne se tranche pas autrement, écrire ce qui sert la reconnaissance et la lecture, jamais ce qui sert la
restitution.</p>''',
      '''<p>Cette phrase est le critère d'arbitrage de toutes les décisions de rédaction. Devant un choix
qui ne se tranche pas autrement, écrire ce qui sert la reconnaissance et la lecture, jamais ce qui sert la
restitution.</p>

<div class="note"><span class="t">La forme courte de la promesse</span>
<p><strong>«&nbsp;Simulez, Visualisez, Comprenez.&nbsp;»</strong> C'est la promesse ci-dessus en trois
verbes, dans l'ordre où l'apprenant les vit. Elle se cite telle quelle, avec son deux-points d'annonce,
partout où la méthode se présente&nbsp;; elle ne se paraphrase pas.</p>
<p><strong>Le troisième verbe porte la promesse, et c'est ce qui l'a fait choisir.</strong> La formule
initiale était «&nbsp;Simulez, Visualisez, Apprenez autrement&nbsp;», et elle est écartée pour trois
raisons&nbsp;: elle est moins dynamique&nbsp;; «&nbsp;apprendre autrement&nbsp;» est trop neutre et ne dit
pas grand-chose&nbsp;; et ce que veut le lecteur, c'est comprendre. <strong>«&nbsp;Autrement&nbsp;» était
de surcroît déjà contenu dans «&nbsp;Simulez, Visualisez&nbsp;»</strong>, qui dit en quoi consiste la
différence au lieu de l'annoncer.</p>
<p><strong>Ce qu'elle coûte.</strong> Le deux-points fait partie de la formule. Dans un texte qui ne
compte qu'une section, il consomme à lui seul le budget de la section 10, et plus aucune phrase ne peut en
porter.</p>
<p class="legende"><strong>Décidé</strong> par le décideur le 27&nbsp;août 2026, à la relecture de
l'avant-propos de «&nbsp;Comprendre la comptabilité&nbsp;», qui est le premier texte à la porter.</p>
</div>''',
      'charte : section 1, la forme courte de la promesse')

C.rep("""<h2>3 — L'accroche</h2>""",
      '''<div class="note"><span class="t">L'avant-propos d'un module, et pourquoi il n'a pas de
gabarit</span>
<p><strong>Règle.</strong> Un module peut porter un avant-propos, lu avant son premier chapitre.
<strong>Ce n'est pas un chapitre</strong>&nbsp;: ni sous-titre, ni vidéo, ni écriture, ni composant, ni
bloc «&nbsp;Ce que vous avez appris&nbsp;», ni quiz. Le tableau ci-dessus ne s'y applique pas. Tout le
reste de cette charte s'y applique — l'adresse et la personne, le point de vue narratif, le marquage, la
ponctuation et son budget, les conventions d'écriture, les interdits.</p>
<p><strong>Ce qu'il fait, et ce qu'il ne fait pas.</strong> Il accueille quelqu'un qui a déjà choisi le
module. Il dit ce qu'on va y apprendre, pourquoi savoir le lire change ce qu'on peut décider, par quelle
méthode, sur quel fil rouge, et il lance le lecteur. <strong>Il ne dit rien du public visé et
n'argumente pas</strong>&nbsp;: ce travail est celui d'une page de présentation, qui s'adresse à quelqu'un
qui n'a pas encore choisi et qui n'est pas un texte de formation.</p>
<p><strong>Il suit le cycle de production d'un chapitre</strong> (section 22)&nbsp;: PDF de relecture avec
ses seuls points de vigilance, puis fichier de livraison et annexe de contrôle complète. Deux cases de la
checklist de la section 21 ne s'y appliquent pas, celle des sous-titres et celle du bloc de clôture, et
l'annexe les déclare.</p>
<div class="note"><span class="t">Attesté</span>
<p>Avant-propos de «&nbsp;Comprendre la comptabilité&nbsp;», 27&nbsp;août 2026. <strong>Comme la clause
qui précède, celle-ci entre par décision et non par attestation de relecture.</strong> Quatre tours ont
été nécessaires, et les deux premiers ont produit un texte de présentation que le décideur a reconnu comme
celui de la page de vente&nbsp;: c'est ce qui a rendu la distinction visible, et c'est pourquoi elle est
écrite ici plutôt que laissée au jugement.</p></div></div>

<h2>3 — L'accroche</h2>''',
      "charte : section 2, l'avant-propos")

C.rep_bloc('<p class="fin">Charte de rédaction Casoria — v15 du 27 août 2026.',
           "<strong>Ce qui n'entre pas.</strong>",
           '''<p class="fin">Charte de rédaction Casoria — v16 du 27&nbsp;août 2026. Aucun dispositif
nouveau, aucune section déplacée, deux ajouts&nbsp;: la forme courte de la promesse à la section 1, et
l'avant-propos d'un module à la section 2.
<strong>Les deux entrent par décision et non par attestation</strong>, comme la clause de la v15 avant
elles. Le motif est le même&nbsp;: une décision de structure ou de marque prise par le décideur n'est pas
une vigilance déduite d'une relecture, et la règle des deux attestations ne la vise pas.
<strong>Toute la numérotation est inchangée</strong>, et les renvois faits depuis les déroulés de module
restent valides.
''', 'charte : pied de page')


# ═══════════════════════════════════════════════════════════════════════════
#  2.  Le déroulé — v24 → v25
# ═══════════════════════════════════════════════════════════════════════════
D = Doc('deroule-comprendre-la-comptabilite-v24.corps.html')

D.rep('<p class="kicker">Casoria • Document de référence • v24</p>',
      '<p class="kicker">Casoria • Document de référence • v25</p>',
      'déroulé : kicker')

D.rep_bloc('<p class="chapo">Déroulé annoté de la formation.', '<table class="serree">',
           '''<p class="chapo">Déroulé annoté de la formation. Treize chapitres, un exercice complet
simulé de la création à la clôture, sur le fil rouge d'une PME fictive. <strong>Cette v25 enregistre la
livraison de l'avant-propos du module</strong>&nbsp;: un mot d'accueil de 262&nbsp;mots, lu avant le
Chapitre 1, hors gabarit de chapitre. Elle ne touche ni au plan, ni au scénario chiffré, ni à une ligne
d'écriture — ce texte n'en porte aucune, et le total de contrôle du module reste
inchangé. <strong>Une clause entre à la section 11</strong>&nbsp;: un terme peut être nommé avant son
chapitre s'il pose le sujet sans supposer sa définition, ce qui autorise le Bilan et le Compte de Résultat
dans l'avant-propos et laisse «&nbsp;écriture&nbsp;» au Chapitre 3. <strong>La charte passe en
v16</strong>, qui porte la forme courte de la promesse et l'avant-propos d'un module.</p>

''', 'déroulé : chapo')

D.rep_bloc('<td class="cle">Documents liés</td>', '</tbody>',
           '''<td class="cle">Documents liés</td><td>Charte de rédaction Casoria v16 — règles de forme,
applicables à tous les modules. Ce déroulé ne les répète pas. La v16 ajoute deux clauses, l'une à la
section 1 — la forme courte de la promesse, «&nbsp;Simulez, Visualisez, Comprenez&nbsp;» — et l'autre à la
section 2, sur l'avant-propos d'un module, qui n'a pas de gabarit. Toute la numérotation est inchangée, et
tous les renvois faits d'ici restent valides.</td></tr>
''', 'déroulé : documents liés')

D.rep_bloc('<h2>Changements v24</h2>', '<h2 class="saut">1 — Le fil rouge',
           '''<h2>Changements v25</h2>
<p>L'avant-propos du module est écrit, relu en quatre tours et livré. <strong>Le plan et le scénario
chiffré de la section 3 sont intacts, et ce texte ne passe aucune écriture</strong>&nbsp;: le total de
contrôle du module reste à 1&nbsp;294&nbsp;694,00&nbsp;€ au débit comme au crédit.</p>
<ul>
<li><strong>Un terme peut être nommé avant son chapitre, à une condition</strong>, section 11. La règle du
lexique cumulatif visait jusqu'ici tout emploi&nbsp;; elle vise désormais l'emploi qui définit, ou qui
suppose la définition acquise, et non la mention qui pose le sujet. <strong>Décision du décideur</strong>,
prise à la relecture de la v1 de l'avant-propos&nbsp;: le Bilan et le Compte de Résultat y sont employés
«&nbsp;de manière générique sans explication&nbsp;» et «&nbsp;plantent le décor&nbsp;». Le test qui borne
la clause est écrit à la section&nbsp;: «&nbsp;écriture&nbsp;» reste au Chapitre 3, parce qu'il ne
planterait aucun décor et demanderait une explication.</li>
<li><strong>Un effet de bord de cette clause, à connaître avant de la réemployer.</strong> Autoriser un
terme, c'est s'obliger à sa graphie partout&nbsp;: le mot «&nbsp;Bilan&nbsp;» capitalisé dans
l'avant-propos a obligé à réécrire sa dernière phrase, qui portait un «&nbsp;bilan&nbsp;» minuscule et
générique deux lignes plus bas. Les deux graphies du même mot se seraient touchées sur le même écran, ce
que la charte, section 9, veut précisément éviter.</li>
<li><strong>L'avant-propos entre à la section 9</strong>, hors compte de durée, et à la section 13 avec
son état. Il n'appelle aucune classe neuve de <code>casoria.css</code>, aucun composant et aucun
<code>&lt;UAlert&gt;</code>&nbsp;: les sections 5 et 6 sont inchangées.</li>
<li><strong>La charte passe en v16</strong> et porte deux clauses nées ici&nbsp;: la forme courte de la
promesse, «&nbsp;Simulez, Visualisez, Comprenez&nbsp;», donnée par le décideur contre «&nbsp;Simulez,
Visualisez, Apprenez autrement&nbsp;»&nbsp;; et l'avant-propos d'un module, qui n'a pas de gabarit et qui
n'est pas une page de présentation.</li>
<li><strong>Un point ouvert entre à la section 14</strong>&nbsp;: les trois questions par lesquelles
l'avant-propos motive la lecture des deux documents engagent la fin du module, et il faut vérifier que les
Chapitres 11 et 12 y répondent vraiment.</li>
</ul>

''', 'déroulé : bloc Changements')

D.rep('''<p>Chaque terme est introduit une fois, au chapitre indiqué, et n'est plus redéfini ensuite.
Aucun terme ne doit être employé avant son chapitre d'introduction, sauf annonce explicite. Cette table
sert de garde-fou pendant la rédaction et devient le glossaire du Chapitre 13.</p>''',
      '''<p>Chaque terme est introduit une fois, au chapitre indiqué, et n'est plus redéfini ensuite.
Aucun terme ne doit être employé avant son chapitre d'introduction, sauf annonce explicite. Cette table
sert de garde-fou pendant la rédaction et devient le glossaire du Chapitre 13.</p>
<div class="note"><span class="t">Ce que «&nbsp;employé avant son chapitre&nbsp;» veut dire</span>
<p><strong>Règle.</strong> L'interdit vise <strong>l'emploi qui définit un terme, ou qui suppose sa
définition acquise</strong>. Il ne vise pas la mention qui pose le sujet, sans explication et sans rien
faire reposer dessus.</p>
<p><strong>Le cas qui l'a produite.</strong> L'avant-propos du module nomme le Bilan et le Compte de
Résultat avant le Chapitre 1, qui les définit. Décision du décideur, le 27&nbsp;août 2026&nbsp;: les deux
noms y sont employés de manière générique et sans explication, et ils plantent le décor. Le Chapitre 1
garde sa révélation intacte — «&nbsp;Il s'appelle le Bilan&nbsp;» — parce que l'avant-propos ne dit rien
de ce que les deux documents portent.</p>
<p><strong>Le test qui la borne, et il est vérifiable.</strong> Un terme passe si le texte reste vrai et
lisible pour qui ne sait pas ce qu'il désigne. «&nbsp;Écriture&nbsp;» ne passe pas et reste au
Chapitre 3&nbsp;: il ne plante aucun décor, il demanderait une explication. L'avant-propos écrit donc
«&nbsp;enregistrer vous-même les opérations&nbsp;».</p>
<p><strong>Le corollaire coûte, et il n'est pas facultatif.</strong> Un terme autorisé porte sa graphie
partout dès sa première mention, capitale comprise. Deux graphies du même mot sur un même écran se lisent
comme une distinction, ce que la charte, section 9, refuse.</p>
</div>''',
      'déroulé : section 11, la clause du terme nommé avant son chapitre')

D.rep('''<tr><td colspan="5"><h4 style="margin:6px 0 2px">Séance 1 — Les fondations (~2h00 avec
aside)</h4></td></tr>''',
      '''<tr><td class="ch">—</td><td>Avant-propos — mot d'accueil, hors gabarit et hors compte</td>
<td class="num">~1 min</td><td class="num">—</td><td class="num">—</td></tr>
<tr><td colspan="5"><h4 style="margin:6px 0 2px">Séance 1 — Les fondations (~2h00 avec
aside)</h4></td></tr>''',
      "déroulé : section 9, l'avant-propos au tableau")

D.rep_bloc('</ol>\n\n<h2>14 — Points encore ouverts</h2>\n<ul>',
           "<li><strong>Les trente centimes de l'échéancier.</strong>",
           '''<li><strong>Avant-propos — livré.</strong> 262&nbsp;mots, hors gabarit de chapitre, écrit
après les treize et relu en quatre tours. Les deux premières versions répondaient à cinq points de
présentation et se sont révélées être le texte de la page de vente&nbsp;; la troisième a changé de nature
pour devenir un mot d'accueil. Il porte la forme courte de la promesse, il nomme le Bilan et le Compte de
Résultat par la clause de la section 11, et il finit sur la promesse du module citée en direct.</li>
</ol>

<h2>14 — Points encore ouverts</h2>
<ul>
<li><strong>Les trois questions de l'avant-propos engagent la fin du module.</strong> Il motive la lecture
des deux documents en écrivant que savoir les lire permet de dire si une entreprise gagne de l'argent, si
elle peut payer ce qu'elle doit, et si elle passera l'année. <strong>La première et la troisième sont
tenues par le Chapitre 12</strong> et ses trois ratios&nbsp;; <strong>la deuxième l'est par le
Chapitre 11</strong> et par le besoin en fonds de roulement du 12. À vérifier en relisant les deux
chapitres&nbsp;: si l'une des trois n'est pas tenue, c'est l'avant-propos qui la retire, et non le
chapitre qui la rattrape.</li>
''', "déroulé : sections 13 et 14, l'avant-propos")


# ═══════════════════════════════════════════════════════════════════════════
#  3.  Le journal de rédaction — tables cumulatives seulement
# ═══════════════════════════════════════════════════════════════════════════
# La règle de purge du journal s'applique : tout ce que l'annexe de contrôle de
# l'avant-propos porte reste à l'annexe. Ne viennent ici que les deux tables
# cumulatives, qui ne se déportent nulle part.
J = Doc('journalderedactioncomprendrelacomptabilite.md')

J.rep('**Dernière mise à jour : 26 août 2026, livraison du Chapitre 12.**',
      '**Dernière mise à jour : 27 août 2026, livraison de l\'avant-propos du module.**',
      'journal : date')

J.rep('| 13 | Synthèse et feuille de route | **livré** (v2, 27 août) | 584 | — | — |',
      '| 13 | Synthèse et feuille de route | **livré** (v2, 27 août) | 584 | — | — |\n'
      "| — | Avant-propos (mot d'accueil, hors gabarit) | **livré** (v5, 27 août) | 262 | — | — |",
      'journal : table avancement')

J.rep('Ordre de rédaction (déroulé, section 13) : 7 ✓, 2 ✓, 1 ✓, 3 ✓, 4 ✓, 5 ✓, 6 ✓, 8 ✓, 9 ✓, 10 ✓, '
      '11 ✓,\n12 ✓, 13 ✓.',
      'Ordre de rédaction (déroulé, section 13) : 7 ✓, 2 ✓, 1 ✓, 3 ✓, 4 ✓, 5 ✓, 6 ✓, 8 ✓, 9 ✓, 10 ✓, '
      '11 ✓,\n12 ✓, 13 ✓, puis l\'avant-propos ✓ — écrit en dernier, une fois les treize chapitres livrés,\n'
      'ce qui est le seul ordre possible : un mot d\'accueil promet ce que le module tient.',
      'journal : ordre de rédaction')

J.ecrire()
C.ecrire('charte-redaction-casoria-v16.corps.html')
D.ecrire('deroule-comprendre-la-comptabilite-v25.corps.html')
print('   la charte v15 et le déroulé v24 restent intacts dans le dossier.')
