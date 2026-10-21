#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Écrit le fichier de travail du Chapitre 10 — Fin d'exercice.

Le texte est écrit avec « ~ » partout où un insécable est requis, et la
substitution se fait ici. Piège 2 du LISEZ-MOI : ne jamais taper l'insécable
au clavier.
"""
NB = '\u00a0'
assert NB == chr(160), 'NB doit être un insécable, pas un espace ordinaire'

CORPS = r"""<p class="kicker">Casoria • Comprendre la comptabilité • Chapitre 10</p>
<h1>Fin d'exercice</h1>

<div class="video"><span class="t">Vidéo d'ouverture — ~2 min</span>
<p>Une année de comptes ne s'arrête pas le soir du 31~décembre comme on ferme une caisse. Avant de figer
les deux documents, l'entreprise reprend certaines opérations et les remet dans l'année qu'elles
concernent. La vidéo pose la question du chapitre, celle de ce qui sépare une photo exacte d'une photo
seulement à jour, et montre les trois faits de l'automne qui vont demander une correction.</p></div>

<p class="accroche">31~décembre. L'année de Latitude Café est finie, et trois faits de l'automne ne sont
pas rangés dans l'année qu'ils concernent~: un client conteste un lot de café pour 3~500~€, une assurance a
été payée pour des mois qui n'ont pas commencé, un contrat a été encaissé pour l'année prochaine. Le Compte
de Résultat n'en porte encore aucun, et reste à remettre chacun à sa place avant d'arrêter les
comptes.</p>

<h2 class="nu">Une opération appartient à la période qu'elle concerne, pas à celle où l'argent bouge</h2>
<p>Les comptes d'une année ne s'arrêtent pas d'eux-mêmes. Avant de les figer, l'entreprise passe une série
d'écritures qui remettent chaque opération dans la période à laquelle elle appartient. Ce moment porte un
nom, la <span class="lex">clôture</span>. Ces écritures-là ne ressemblent à aucune de celles que vous avez
passées jusqu'ici, puisqu'elles ne constatent pas une opération nouvelle mais corrigent la place d'une
opération déjà écrite.</p>
<p>La règle qui les commande tient en une phrase. Une charge ou un produit se rattache à la période qu'il
concerne, et non à celle où l'argent a bougé. C'est le <span class="lex">rattachement à la période</span>,
et tout le reste de ce chapitre en découle.</p>
<p>Vous connaissez déjà la moitié de cette idée. Au Chapitre 4, une facture inscrivait une vente le jour où
elle était émise, sans attendre que le client règle. Le rattachement va un cran plus loin. Inscrire une
opération au bon moment ne suffit pas. Une fois l'année finie, il faut vérifier que chacune concerne bien
l'année qui s'achève, et corriger celles qui ne la concernent pas.</p>
<p class="declaration">Laisser ces montants où ils sont ferait dire à l'année autre chose que ce qu'elle a
fait.</p>
<div class="composant"><code>&lt;TriAjustements /&gt;</code>
<span class="cap">Tri à quatre issues, six situations de fin d'exercice</span></div>
<p>Une chose doit être faite avant ces corrections. Les ventes et les achats d'octobre, novembre et
décembre ne sont pas encore inscrits, ni au Bilan ni au Compte de Résultat. Deux des trois corrections
portent sur des sommes qui s'y trouvent, et ce dernier trimestre s'enregistre donc en premier.</p>
<div class="panneau panneau--auto">
<span class="t">Enregistré automatiquement — 9 lignes</span>
<p class="op">Écriture de période — quatrième trimestre</p>
<ul class="lignes">
<li>Bilan — 411 Créances clients — « Ventes professionnelles T4 » — 96~000~€ au débit</li>
<li>CR — 701 Ventes aux professionnels — « Ventes professionnelles T4 » — 80~000~€ au crédit</li>
<li>GdJal seul — 4457 TVA collectée — « TVA sur ventes T4 » — 20~800~€ au crédit</li>
<li>Bilan — 512 Trésorerie — « Ventes au comptoir T4 » — 28~800~€ au débit</li>
<li>CR — 707 Ventes au comptoir — « Ventes au comptoir T4 » — 24~000~€ au crédit</li>
<li>CR — 601 Achats de café vert — « Achats café vert T4 » — 45~000~€ au débit</li>
<li>CR — 615 Autres charges externes — « Charges externes T4 » — 26~960~€ au débit</li>
<li>GdJal seul — 4456 TVA déductible — « TVA déductible T4 » — 14~392~€ au débit</li>
<li>Bilan — 401 Dettes fournisseurs — « Fournisseurs T4 » — 86~352~€ au crédit</li>
</ul>
<p class="legende">Ce mécanisme a été passé à la main au Chapitre 5, sur le premier trimestre. Il se répète
ici sans apporter de notion nouvelle. Il porte les ventes et les achats du dernier trimestre, et les 26~960~€ de charges externes
du trimestre contiennent la prime d'assurance payée le 1<sup>er</sup>~octobre, et les ventes aux
professionnels contiennent le contrat de l'Hôtel Bellevue encaissé le 1<sup>er</sup>~novembre. Le compte en
banque finit le trimestre à 99~435,10~€, et le total des charges à 227~551,50~€.</p>
</div>

<h2>Une perte encore incertaine s'inscrit dès qu'elle est probable</h2>
<p>Fin novembre, Le Comptoir des Halles a reçu un lot de café trop torréfié. Le client réclame, la
discussion n'est pas tranchée, et Latitude Café estime à 3~500~€ ce que l'affaire lui coûtera. Rien n'est
encore certain, et rien n'a encore été versé.</p>
<p>La comptabilité n'attend pas la certitude pour inscrire une perte. Dès qu'un risque est
<button aria-describedby="p10-reprise" class="prec" type="button">probable</button> et que son montant peut
être estimé, l'entreprise en compte la charge sur l'année où le risque est né. Cette charge anticipée
s'appelle une <span class="lex">provision</span>.</p>
<p class="prec-note" id="p10-reprise" role="note">Une provision n'est pas définitive. Si le litige se règle
l'année suivante pour moins que prévu, ou s'il finit par ne rien coûter, l'entreprise reprend sa provision.
La charge inscrite aujourd'hui redevient alors un produit de l'année suivante, à hauteur de ce qui n'a pas
été payé. Compter prudemment ne fait donc rien perdre à l'entreprise. Cela décale seulement l'année où
son résultat en tient compte.</p>
<p>Ce qui vaut pour les pertes ne vaut pas pour les gains. Une entreprise anticipe une perte probable,
jamais un gain espéré. Ce déséquilibre est voulu et porte un nom, le <span class="lex">principe de
prudence</span>. C'est lui qui explique pourquoi des comptes annoncent rarement une bonne nouvelle avant
qu'elle n'arrive.</p>
<p>Le résultat de l'année baisse donc de 3~500~€ aujourd'hui, sans qu'un euro ne quitte le compte en
banque. L'argent partira peut-être l'an prochain, peut-être jamais. Vous avez rencontré le même écart au
Chapitre 8, avec l'amortissement du torréfacteur, cette part d'usure que le Compte de Résultat inscrivait
sans rien décaisser. La provision fait de même, sur un risque au lieu d'une machine.</p>
<div class="panneau">
<span class="t">À passer — Provision pour la réclamation du Comptoir des Halles · 2 lignes</span>
<ul class="lignes">
<li>CR — 6815 Dotation à la provision — « Provision réclamation client » — 3~500~€ au débit (emploi)</li>
<li>Bilan — 151 Provision pour risque client — « Provision réclamation client » — 3~500~€ au crédit (ressource)</li>
</ul>
<p class="legende">Regardez les deux documents avant de passer le bloc d'écritures, puis après. Au Compte
de Résultat, le total des charges monte de 227~551,50~€ à 231~051,50~€. Au Bilan, le compte en banque ne bouge pas et
reste à 99~435,10~€, tandis qu'une ligne s'ouvre au Passif, Provision pour risque client, pour
3~500~€.</p>
</div>

<h2>Ce qui est payé d'avance quitte les charges, ce qui est encaissé d'avance quitte les produits</h2>
<p>Le 1<sup>er</sup>~octobre, Latitude Café a payé 3~600~€ pour douze mois d'assurance. La somme est partie
du compte en banque en une fois, et elle figure entièrement dans les charges externes du quatrième
trimestre. Trois mois seulement concernent l'année qui s'achève. Les neuf autres concernent 2027, soit
2~700~€.</p>
<p>Ces 2~700~€ ne sont pas une charge de 2026. Ils quittent le Compte de Résultat et rejoignent l'Actif du
Bilan, sous le nom de <span class="lex">charges constatées d'avance</span>.</p>
<p>L'Hôtel Bellevue est un client. Le 1<sup>er</sup>~novembre, il a payé d'avance son contrat
d'approvisionnement annuel, 2~400~€ pour douze mois. Ce contrat fait le trajet exactement inverse,
puisque 2~000~€ concernent 2027. Ces 2~000~€ quittent les produits et rejoignent le Passif du Bilan, comme <span class="lex">produits constatés
d'avance</span>, puisque l'entreprise doit encore dix mois de livraisons à ce client. Les deux blocs d'écritures
ci-dessous se lisent ensemble, chacun étant l'image de l'autre dans un miroir.</p>
<div class="panneau">
<span class="t">À passer — Assurance payée d'avance, neuf mois sur 2027 · 2 lignes</span>
<ul class="lignes">
<li>Bilan — 486 Charges constatées d'avance — « Assurance — part 2027 » — 2~700~€ au débit</li>
<li>CR — 615 Autres charges externes — « Assurance — part 2027 » — 2~700~€ au crédit</li>
</ul>
<p class="legende">Regardez le Compte de Résultat avant de passer le bloc d'écritures, puis après. La
ligne Autres charges externes redescend de 72~960~€ à 70~260~€, et le total des charges de 231~051,50~€ à
228~351,50~€. Au Bilan, une ligne s'ouvre à l'Actif pour 2~700~€.</p>
</div>
<div class="panneau">
<span class="t">À passer — Contrat Hôtel Bellevue encaissé d'avance, dix mois sur 2027 · 2 lignes</span>
<ul class="lignes">
<li>CR — 701 Ventes aux professionnels — « Contrat Hôtel Bellevue — part 2027 » — 2~000~€ au débit</li>
<li>Bilan — 487 Produits constatés d'avance — « Contrat Hôtel Bellevue — part 2027 » — 2~000~€ au crédit</li>
</ul>
<p class="legende">Même geste, en sens inverse. La ligne Ventes aux professionnels redescend de
210~000~€ à 208~000~€, et le total des produits de 285~000~€ à 283~000~€. Au Bilan, une ligne s'ouvre cette
fois au Passif, pour 2~000~€. Aucun des deux blocs d'écritures n'a déplacé un
euro sur le compte en banque.</p>
</div>

<div class="alert"><span class="t">À savoir</span>
<p>Une seule provision est traitée ici, en profondeur, plutôt qu'un tour d'horizon des situations qui en
demandent une. Une entreprise en constitue pour des litiges, pour des garanties données à ses clients, pour
des créances qu'elle risque de ne jamais recevoir. Les ventes et les achats du quatrième trimestre sont par
ailleurs regroupés en une seule écriture, enregistrée automatiquement.</p></div>
<div class="appris">
<h2>Ce que vous avez appris</h2>
<ul>
<li>Une charge se rattache à l'année qu'elle concerne, et non à celle où l'argent a bougé. Trois
écritures ont suffi à replacer une réclamation, une assurance et un contrat dans la bonne année.</li>
<li>Une perte probable s'inscrit avant d'être certaine, un gain espéré jamais. Les 3~500~€ de la
réclamation ont baissé le résultat sans rien retirer du compte en banque.</li>
<li>Les 2~700~€ d'assurance qui couvrent 2027 ne sont plus une charge de 2026, mais neuf mois de
couverture que l'entreprise détient. Les 2~000~€ encaissés du contrat ne sont plus un produit, mais des
livraisons qu'elle doit encore.</li>
</ul>
</div>"""

CHAPO = r"""<p class="chapo">Version v4, livrée. Deux tours de relecture profane, validés le 25~août 2026. Rédigée sous la charte v13 et le déroulé v20 ; ses arbitrages sont
passés à la charte v14 et au déroulé v21. Trois sous-titres,
trois blocs manuels de deux lignes répartis 0~/~1~/~2, une activité, un <code>&lt;UAlert&gt;</code>, aucune
illustration, et une précision neuve ancrée sur «~probable~». <strong>Le panneau automatique est placé au
premier sous-titre</strong>, et non en fin de texte~: c'est le seul arbitrage de fond du chapitre, il est
motivé à l'annexe. Ce fichier est le fichier de travail. Il porte le chapo et l'annexe de contrôle, que le fichier de livraison ne porte pas. <strong>Le registre, le déroulé et la charte sont
répercutés</strong> en une fois, le 25 août 2026.</p>"""

out = CORPS.replace('~', NB).replace(
    "<h1>Fin d'exercice</h1>", "<h1>Fin d'exercice</h1>\n" + CHAPO.replace('~', NB), 1)
assert '<p class="chapo">' in out
open('ch10-travail.html', 'w', encoding='utf-8').write(out + '\n')
print('écrit : ch10-travail.html —', len(out), 'caractères,', out.count(NB), 'insécables')
