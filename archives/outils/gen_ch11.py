#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Écrit le fichier de travail du Chapitre 11 — La clôture.

Le texte est écrit avec « ~ » partout où un insécable est requis, et la
substitution se fait ici, en une passe. Piège 2 du LISEZ-MOI : ne jamais
taper l'insécable au clavier.
"""
NB = ' '
assert NB == chr(160), 'NB doit être un insécable, pas un espace ordinaire'

CORPS = r"""<p class="kicker">Casoria • Comprendre la comptabilité • Chapitre 11</p>
<h1>La clôture</h1>

<div class="video"><span class="t">Vidéo d'ouverture — ~2 min</span>
<p>Une année de comptes finit sur la question du premier chapitre. L'entreprise a-t-elle gagné de l'argent,
et où le voit-on~? La vidéo suit le dernier trajet du module, celui qui va du film à la photo. Ce que le
Compte de Résultat a mesuré pendant douze mois vient se poser sur le Bilan, qui retrouve alors son
équilibre. Elle rappelle au passage qu'un tiers se sert avant les associés.</p></div>

<p class="accroche">31~décembre au soir. Les comptes de Latitude Café sont arrêtés, et le Compte de
Résultat annonce 32~000~€ de bénéfice pour une première année. Le Bilan, lui, ne tombe pas juste~:
130~410~€ à l'Actif, 98~410~€ au Passif, et exactement la même somme d'écart entre les deux. Reste à
comprendre pourquoi c'est la même, et ce qu'il en restera une fois l'État servi.</p>

<h2>L'État prend sa part du bénéfice avant les associés</h2>
<p>Une société paie un impôt sur ce qu'elle a gagné dans l'année, et cet impôt est une charge de cette
année-là. Il porte un nom, l'<span class="lex">impôt sur les sociétés</span> (IS). Il se calcule sur le
bénéfice que le Compte de Résultat vient d'établir, et ce bénéfice porte lui aussi un nom, le
<span class="lex">résultat avant impôt</span>. Il vaut 32~000~€ pour Latitude Café.</p>
<p>Le taux dépend de la somme gagnée. Jusqu'à 42~500~€ de bénéfice, une société est imposée à
15~%. Au-delà, la part qui dépasse ce seuil l'est à 25~%. Latitude Café reste en dessous, comme la
plupart des entreprises de sa taille, et son impôt tient donc en une seule ligne de calcul. 32~000~€ à
15~% font 4~800~€.</p>
<p>Cet impôt est lui-même une charge de l'année qui s'achève, et il fait donc baisser le résultat de cette
année. Il ne se recalcule pas pour autant sur le résultat qu'il vient de faire baisser. Le calcul se fait
une fois, sur le bénéfice avant impôt, c'est-à-dire sur les 32~000~€ et non sur les 27~200~€ qui restent
une fois l'impôt inscrit.</p>
<p>L'impôt ne se calcule que sur un bénéfice, jamais sur une
<button aria-describedby="p11-deficit" class="prec" type="button">perte</button>. Ce qui reste une fois
l'État servi est le <span class="lex">résultat net</span>, 4~800~€ plus bas, soit 27~200~€.</p>
<p class="prec-note" id="p11-deficit" role="note">Une année qui se termine sur une perte ne donne lieu à
aucun impôt sur les sociétés. La perte n'est pas perdue pour autant. Elle vient en déduction des bénéfices
des années suivantes, et réduit l'impôt de ces années-là. Une entreprise qui perd de l'argent sa première
année et en gagne la deuxième ne paie donc pas sur la totalité de ce second bénéfice.</p>
<div class="panneau">
<span class="t">À passer — Impôt sur les sociétés de l'exercice · 2 lignes</span>
<ul class="lignes">
<li>CR — 695 Impôt sur les sociétés — « Impôt sur les sociétés 2026 » — 4~800~€ au débit (emploi)</li>
<li>Bilan — 444 État — IS à payer — « Impôt sur les sociétés 2026 » — 4~800~€ au crédit (ressource)</li>
</ul>
<p class="legende">Regardez les deux documents avant de passer le bloc d'écritures, puis après. Au Compte
de Résultat, une ligne s'ouvre du côté des charges et le total monte de 251~000~€ à 255~800~€. Le résultat
de l'année descend de 32~000~€ à 27~200~€. Au Bilan, une ligne s'ouvre au Passif, État — IS à payer, pour
4~800~€, et le total du Passif monte de 98~410~€ à 103~210~€. Le compte en banque ne bouge pas, cet impôt
étant versé au printemps suivant.</p>
</div>

<h2>Le bénéfice appartient aux associés, pas à l'entreprise qui l'a gagné</h2>
<p>Les 27~200~€ qui restent ne sont pas une somme que Latitude Café garde pour elle. Ils reviennent aux
deux associés, qui ont apporté l'argent du départ. L'entreprise les détient et ne les possède
pas.</p>
<p class="declaration">Le résultat figure au Passif parce qu'il appartient à quelqu'un d'autre que
l'entreprise qui l'a gagné.</p>
<p>Le Passif dit d'où vient ce que l'entreprise détient. Il range côte à côte ce qu'elle devra rendre à sa
banque et à ses fournisseurs, et ce qu'elle gardera tant qu'elle vivra. Le bénéfice de l'année
s'inscrit dans cette seconde part, juste à côté du capital social, ces 30~000~€
que les associés ont apportés le jour où ils ont créé la société, au Chapitre 2.</p>
<p>Cela explique l'écart que le Bilan traîne depuis le premier jour d'activité, et qui vaut 27~200~€ ce
soir. Tout ce que l'année a rapporté est déjà inscrit à l'Actif, en argent sur le compte en banque, en café
sur les étagères, en factures que les clients doivent encore. Rien au Passif ne dit d'où cette valeur est
venue. Elle n'a été ni apportée par les associés, ni prêtée par une banque, ni facturée par un fournisseur.
Elle a été gagnée, et le seul document qui l'ait mesurée est le Compte de Résultat.</p>
<p>Ce que les associés font de ces 27~200~€ se décide plus tard, quelques mois après, le jour où ils
approuvent les comptes de l'année. Cette décision porte un nom, l'<span class="lex">affectation du
résultat</span>, et elle a trois issues. Une part reste dans l'entreprise parce que la loi l'exige, la
<span class="lex">réserve légale</span>. Une part peut leur être versée, et c'est le
<span class="lex">dividende</span>. Ce qui n'est ni l'une ni l'autre attend l'année suivante sans être
affecté, sous le nom de <span class="lex">report à nouveau</span>.</p>
<div class="image-slot"><span class="t">[IMAGE]</span>
<p class="cap">Légende : Les 27~200~€ de résultat net, quelques mois après la fin de l'année, au moment
où les associés en décident. Une part reste dans l'entreprise parce que la loi l'exige, une part peut leur
être versée, une part attend sans être affectée. Le Bilan du 31~décembre, lui, ne bouge plus, puisqu'il est
déjà arrêté.</p></div>

<div class="alert"><span class="t">À savoir</span>
<p>L'impôt est calculé et inscrit ici en une fois, à la fin de l'année. Une entreprise en verse en réalité
des acomptes en cours de route, dès sa deuxième année. Les conditions qui ouvrent le taux de 15~% sont
supposées remplies. Et le calcul est fait sur le bénéfice que le Compte de Résultat affiche, alors qu'une
entreprise le fait sur un bénéfice corrigé de quelques charges que la loi n'admet pas en déduction.</p></div>

<p>Il reste un geste, et c'est le dernier du module. Le résultat net quitte le Compte de Résultat, où il a
été mesuré, pour s'inscrire au Passif du Bilan. Au Chapitre 1, le Bilan était la photo de l'entreprise à un
instant donné et le Compte de Résultat le film de son année. Ce que le film a produit vient grossir la
photo. Les deux totaux du Bilan tombent alors sur le même nombre, ce qui ne s'était plus produit depuis les
quatre premières écritures du Chapitre 2 à la création de la société.</p>
<div class="panneau">
<span class="t">À passer — Le résultat de l'exercice rejoint le Bilan · 1 ligne</span>
<ul class="lignes">
<li>Bilan seul — 120 Résultat de l'exercice — « Résultat net de l'exercice 2026 » — 27~200~€ au crédit</li>
</ul>
<p class="legende">Cette ligne est la seule du module qui ne passe pas par le grand journal. Le résultat
n'est pas une opération entre l'entreprise et quelqu'un d'autre, c'est ce que le Compte de Résultat a fini
par mesurer, et il se reporte tel quel au Passif. Regardez le Bilan avant de passer le bloc d'écritures,
puis après. L'Actif ne bouge pas et reste à 130~410~€. Le Passif monte de 103~210~€ à 130~410~€. Les deux
totaux sont égaux.</p>
</div>
<div class="appris">
<h2>Ce que vous avez appris</h2>
<ul>
<li>L'État prend sa part avant les associés. Les 32~000~€ de bénéfice de Latitude Café ont laissé
4~800~€ d'impôt sur les sociétés et 27~200~€ de résultat net.</li>
<li>Ces 27~200~€ s'inscrivent au Passif du Bilan parce qu'ils reviennent aux associés, dans la même
colonne que les 30~000~€ de capital qu'ils avaient apportés en créant la société.</li>
<li>Les deux totaux du Bilan tombent sur 130~410~€. Douze mois mesurés par le Compte de Résultat sont
venus se poser sur la photo du 31~décembre, et c'est ce qui la referme.</li>
</ul>
</div>"""

CHAPO = r"""<p class="chapo"><strong>Version v2, livrée.</strong> Rédigée le 25~août 2026 sous la
charte v14 et le déroulé v21, une fois l'écart de 22~648,50~€ de la section 14 tranché et le Chapitre 10
repris. <strong>Premier tour de relecture profane passé le même jour, six corrections</strong>, toutes
appliquées~; deux d'entre elles ouvrent un point à trancher, et l'annexe les porte. Deux sous-titres, trois lignes manuelles en deux blocs d'écritures répartis 1~/~0, le second en
fin de texte comme la fiche l'impose, aucune activité, aucun panneau automatique, un
<code>&lt;UAlert&gt;</code>, une illustration et une précision neuve ancrée sur «~perte~». Ce fichier est le
fichier de travail~: il porte le chapo et l'annexe de contrôle, que le fichier de livraison ne porte pas.
<strong>Le registre, le déroulé et le journal sont répercutés</strong> le 25~août 2026, le déroulé passant
en v22. La charte v14 est inchangée.</p>"""

out = CORPS.replace('~', NB).replace(
    '<h1>La clôture</h1>', '<h1>La clôture</h1>\n' + CHAPO.replace('~', NB), 1)
assert '<p class="chapo">' in out
open('ch11-travail.html', 'w', encoding='utf-8').write(out + '\n')
print('écrit : ch11-travail.html —', len(out), 'caractères,', out.count(NB), 'insécables')
