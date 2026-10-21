#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Écrit le fichier de travail du Chapitre 9 — Les salariés.

Le texte est écrit avec « ~ » partout où un insécable est requis, et la
substitution se fait ici. Piège 2 du LISEZ-MOI : ne jamais taper l'insécable
au clavier.
"""
NB = '\u00a0'
assert NB == chr(160), 'NB doit être un insécable, pas un espace ordinaire'

CORPS = r"""<p class="kicker">Casoria • Comprendre la comptabilité • Chapitre 9</p>
<h1>Les salariés</h1>

<div class="video"><span class="t">Vidéo d'ouverture — ~2 min</span>
<p>Un contrat de travail porte un seul montant, et ce montant n'est celui de personne. Ni celui que le
salarié verra arriver sur son compte en banque, ni celui que l'entreprise sortira du sien. La vidéo pose la
question du chapitre, celle de ce qu'un salarié coûte réellement, et prévient que la réponse tient dans
l'écart entre deux nombres que personne n'affiche côte à côte.</p></div>

<p class="accroche">1<sup>er</sup>~septembre. Latitude Café embauche Léa Ferrand, assistante torréfaction et
vente, à 2~200~€ brut par mois. Ce montant est le seul que le contrat porte, mais il n'est ni celui que Léa
recevra, ni celui que l'entreprise paiera. Le compte en banque affiche 61~371,10~€ ; reste à savoir de
combien ce salaire le fera baisser, et ce qu'il coûte vraiment.</p>

<h2 class="nu">Le salarié ne reçoit pas la somme écrite sur son contrat</h2>
<p>Depuis le 1<sup>er</sup>~juillet, Thomas et Claire se versent chacun une rémunération de 1~500~€ par
mois. Léa les rejoint le 1<sup>er</sup>~septembre, et son contrat porte 2~200~€. Ces trois montants sont des
salaires bruts. Le <span class="lex">salaire brut</span> est la rémunération convenue, celle qui figure au
contrat, avant toute retenue.</p>
<p>Chaque mois, une partie de ce brut ne part pas chez Léa. Elle est retenue sur sa rémunération et versée
aux organismes qui financent la retraite, la maladie et le chômage. Ces cotisations retenues portent un
nom, les <span class="lex">charges salariales</span>. Elles valent 22~% du brut dans cette formation, soit
484~€ sur les 2~200~€ de Léa.</p>
<p>Ce qui reste est le <span class="lex">salaire net</span>, et c'est le seul montant du bulletin que Léa
verra arriver sur son compte en banque. Il s'élève à 1~716~€.</p>

<h2>À côté du brut, l'entreprise paie une seconde somme</h2>
<p>Latitude Café ne s'arrête pas là. En plus des 2~200~€ de brut, elle verse ses propres cotisations, qui
ne sont retenues sur rien et s'ajoutent au salaire. Ce sont les <span class="lex">charges patronales</span>.
Elles valent <button aria-describedby="p9-taux" class="prec" type="button">42~% du brut</button> dans cette
formation, soit 924~€ pour Léa.</p>
<p class="prec-note" id="p9-taux" role="note">Ce taux n'est pas le même pour tous les salaires. L'État
allège les cotisations patronales sur les rémunérations proches du salaire minimum, où elles descendent
très au-dessous de ce niveau, et l'allègement diminue à mesure que la rémunération monte. Deux entreprises
qui versent le même brut total ne paient donc pas les mêmes charges patronales si leurs salaires ne sont
pas au même niveau.</p>
<p>Le brut et ces cotisations forment ensemble ce que le salarié coûte, le <span class="lex">coût total
employeur</span>. Pour Léa, il atteint 3~124~€, quand elle-même en perçoit 1~716~€. L'écart n'est pas gardé
par l'entreprise. Il part aux organismes sociaux, qui financent les retraites, les soins et les allocations
de tout le monde.</p>
<p class="declaration">Le coût d'un salarié est toujours plus élevé que la rémunération qu'il perçoit.</p>
<div class="composant"><code>&lt;CoutEmployeur /&gt;</code>
<span class="cap">Révélateur coût employeur / net perçu, en trois parts</span></div>
<p>Reste à savoir quand cet argent part du compte en banque. Le net part le mois même. Les cotisations, en
revanche, se versent aux organismes à date fixe, le plus souvent le mois suivant. Tant qu'elles sont dues
et pas encore versées, elles s'inscrivent au Passif du Bilan sous le nom de <span class="lex">dettes
sociales</span>.</p>
<p>Le Compte de Résultat, lui, n'attend pas ce versement. Il enregistre la rémunération du mois où le
travail a été fait, cotisations comprises. Vous avez déjà rencontré ce décalage au Chapitre 4, où une
facture inscrivait une vente avant que l'argent n'arrive. Il joue ici dans l'autre sens, sur une charge.</p>
<p>Le bloc d'écritures ci-dessous regroupe les bulletins du troisième trimestre. Thomas et Claire ont été rémunérés en
juillet, août et septembre, soit 9~000~€ de brut à eux deux. Léa n'a été payée qu'en septembre, pour
2~200~€. Le brut du trimestre atteint donc 11~200~€.</p>
<div class="panneau">
<span class="t">À passer — Bulletins du trimestre · 4 lignes</span>
<ul class="lignes">
<li>CR — 641 Salaires bruts — « Salaires bruts T3 » — 11~200~€ au débit (emploi)</li>
<li>CR — 645 Charges sociales patronales — « Charges patronales T3 » — 4~704~€ au débit</li>
<li>Bilan — 512 Trésorerie — « Nets versés T3 » — 8~736~€ au crédit (ressource)</li>
<li>Bilan — 431 Dettes sociales — « Cotisations à verser T3 » — 7~168~€ au crédit</li>
</ul>
<p class="legende">Regardez les deux documents avant de passer le bloc d'écritures, puis après. Au Compte
de Résultat, le total des charges monte de 84~687,50~€ à 100~591,50~€. Au Bilan, le compte en banque ne descend que de
61~371,10~€ à 52~635,10~€, et une ligne s'ouvre au Passif, Dettes sociales, pour 7~168~€. Le bloc d'écritures se lit
de haut en bas comme une démonstration. 11~200~€ de brut coûtent 15~904~€ à l'entreprise, dont 8~736~€
seulement arrivent sur les comptes en banque des trois intéressés. Le reste ne disparaît pas, il change de
destinataire.</p>
</div>

<h2>Thomas et Claire reçoivent le même bulletin de paie que Léa</h2>
<p>Une question se pose dès qu'un associé se verse une rémunération. Est-il un salarié de sa propre
société ? Thomas préside Latitude Café et Claire en est directrice générale. À ce titre, tous deux relèvent
du régime général de la Sécurité sociale, celui des salariés. On les appelle des <span class="lex">assimilés
salariés</span>.</p>
<p>Leur bulletin obéit donc à la même mécanique que celui de Léa. Un brut, des cotisations retenues, un net
versé, des cotisations patronales en plus. Il n'y a rien de nouveau à apprendre ici, et c'est exactement ce
que la réponse apporte.</p>
<p>Une différence existe pourtant, et une seule mérite d'être retenue à ce stade. Les assimilés salariés ne
cotisent pas à l'assurance chômage, et n'y ont donc aucun droit.</p>
<p>Être associé et être rémunéré sont deux choses distinctes. La rémunération paie un travail, quand le
dividende rémunère un capital. Le dividende occupera une partie du Chapitre 11, une fois qu'il y aura un
résultat à partager entre les associés, ce qui ne se sait qu'une fois l'année finie.</p>

<div class="alert"><span class="t">À savoir</span>
<p>Le bulletin de paie de cette formation est simplifié. Les cotisations y sont calculées à deux taux
forfaitaires, 22~% pour la part retenue au salarié et 42~% pour celle de l'employeur, sans détail par
caisse. Un vrai bulletin en compte une vingtaine de lignes. Les ventes et les achats du troisième trimestre
sont par ailleurs regroupés en une seule écriture, enregistrée automatiquement.</p></div>
<div class="panneau panneau--auto">
<span class="t">Enregistré automatiquement — 9 lignes</span>
<p class="op">Écriture de période — troisième trimestre</p>
<ul class="lignes">
<li>Bilan — 411 Créances clients — « Ventes professionnelles T3 » — 66~000~€ au débit</li>
<li>CR — 701 Ventes aux professionnels — « Ventes professionnelles T3 » — 55~000~€ au crédit</li>
<li>GdJal seul — 4457 TVA collectée — « TVA sur ventes T3 » — 14~000~€ au crédit</li>
<li>Bilan — 512 Trésorerie — « Ventes au comptoir T3 » — 18~000~€ au débit</li>
<li>CR — 707 Ventes au comptoir — « Ventes au comptoir T3 » — 15~000~€ au crédit</li>
<li>CR — 601 Achats de café vert — « Achats café vert T3 » — 35~000~€ au débit</li>
<li>CR — 615 Autres charges externes — « Charges externes T3 » — 20~000~€ au débit</li>
<li>GdJal seul — 4456 TVA déductible — « TVA déductible T3 » — 11~000~€ au débit</li>
<li>Bilan — 401 Dettes fournisseurs — « Fournisseurs T3 » — 66~000~€ au crédit</li>
</ul>
<p class="legende">Ce mécanisme a été passé à la main au Chapitre 5, sur le premier trimestre. Il se répète
ici sans apporter de notion nouvelle. Le compte en banque finit le trimestre à 70~635,10~€.</p>
</div>
<div class="appris">
<h2>Ce que vous avez appris</h2>
<ul>
<li>Le montant écrit sur un contrat de travail n'est celui de personne. Une part en est retenue au salarié
et une autre s'y ajoute pour l'employeur, si bien que Léa perçoit 1~716~€ quand Latitude Café en paie
3~124~€.</li>
<li>L'entreprise ne garde rien de cet écart. Elle le reverse aux organismes sociaux, et tant qu'elle ne
l'a pas fait, ce qu'elle doit figure au Passif du Bilan.</li>
<li>Un associé qui se verse une rémunération reçoit un bulletin de paie comme les autres, et dans une SAS
il relève du régime général, sans droit à l'assurance chômage.</li>
</ul>
</div>"""

CHAPO = r"""<p class="chapo">Version v4, livrée. Deux tours de relecture profane, validés le 25~août 2026. Rédigée sous la charte v13 et le déroulé v20 ; ses arbitrages sont
passés à la charte v14 et au déroulé v21. Trois sous-titres, un
bloc manuel de quatre lignes rattaché au sous-titre du coût employeur, une activité, un
<code>&lt;UAlert&gt;</code>, un panneau automatique en fin de texte, aucune illustration, et une précision
neuve ancrée sur «~42~% du brut~». Ce fichier est le fichier de travail. Il porte le chapo et l'annexe de contrôle, que le fichier de livraison ne porte pas. <strong>Le registre, le déroulé et la charte sont
répercutés</strong> en une fois, le 25 août 2026.</p>"""

out = CORPS.replace('~', NB).replace(
    '<h1>Les salariés</h1>', '<h1>Les salariés</h1>\n' + CHAPO.replace('~', NB), 1)
assert '<p class="chapo">' in out
open('ch09-travail.html', 'w', encoding='utf-8').write(out + '\n')
print('écrit : ch09-travail.html —', len(out), 'caractères,', out.count(NB), 'insécables')
