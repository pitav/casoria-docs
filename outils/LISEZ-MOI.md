# Outils de la passe de reprise — Casoria

Les scripts de la passe ordonnancée au déroulé, section 13. Ils vivent ici parce que l'environnement de
travail est jeté à la fin de chaque session : sans ce dossier, ils se réécrivent entièrement à chaque
chapitre, ce qui a coûté le quart du temps de la reprise du Chapitre 4.

Dépendances : `python3`, `beautifulsoup4`, `weasyprint`, la police Carlito, `pdftoppm` (poppler).

## La chaîne, dans l'ordre

Se lancer depuis un dossier de travail contenant les `.corps.html` des chapitres, `casoria.css`, le
registre et le déroulé.

```
cp chapitre-NN-….corps.html vNN-original.html      # ← indispensable, voir le piège 1
python3 compter.py vNN-original.html               # état avant : deux-points par section, mots
python3 rejeu.py NN                                # soldes de la grille, bloc par bloc
python3 patch_chNN.py                              # la passe → chNN-travail.html
python3 annexe_chNN.py                             # chapo + lignes d'annexe
python3 livrer.py chNN-travail.html chapitre-NN-….corps.html "Chapitre N — Titre"
weasyprint pdf-livraison.html chapitre-NN-livraison-vV.pdf
pdftoppm -png -r 90 chapitre-NN-livraison-vV.pdf page   # relire en images, toujours
# puis, une seule fois à la fin de la passe et non par chapitre :
python3 repercuter_final.py                        # registre + déroulé + charte
```

## Ce que fait chacun

| Script | Rôle | Générique ? |
|---|---|---|
| `compter.py <fichier>` | Deux-points par section, en prose et hors compte, avec l'extrait de chaque phrase. Compte aussi les mots au périmètre déclaré. | oui |
| `rejeu.py [NN]` | Rejoue le journal du module depuis les panneaux des `.corps.html`, jusqu'au chapitre NN. Solde de chaque compte avant et après chaque ligne, et équilibre débit/crédit de chaque écriture. | oui |
| `livrer.py <travail> <livrable> "<titre>"` | Dérive le `.corps.html` livrable, convertit les `.alert` en `<UAlert>`, fabrique le HTML du PDF **depuis le fichier de travail**, et lève sur **quatre contrôles** (ci-dessous). | oui |
| `patch_ch08.py` | La passe elle-même. Chaque substitution est assertée unique, donc rien d'autre ne peut bouger. **Modèle de référence** — le Chapitre 8 est le cas le plus chargé, 26 deux-points en prose. `patch_ch05.py` et `patch_ch04.py` sont les mêmes en plus léger. | non |
| `annexe_ch08.py` | Réécrit le chapo et les lignes d'annexe, puis pose les insécables de l'annexe. **Modèle.** | non |
| `repercuter_final.py` | Registre, déroulé et charte, en une fois à la fin d'une passe. **Modèle**, et c'est la forme retenue : la répercussion ne se fait plus chapitre par chapitre. | non |

## Les quatre contrôles de `livrer.py`

1. **Budget de deux-points.** Il lève si une section porte plus d'un deux-points en prose.
2. **Nombres annoncés.** Il recompte les mots, les mots avec sous-titres, les deux-points et les lignes
   d'écritures manuelles, et refuse d'écrire si l'annexe en annonce d'autres. Dix nombres annoncés ont été
   pris en défaut sur les documents du module avant que ce contrôle existe, dont le total de contrôle du
   module lui-même.
3. **Typographie des sommes.** Chaque somme du corps doit porter ses insécables **et son unité**. Le second
   point vient du Chapitre 5 : couper une phrase à deux-points isole une somme dont l'unité était en
   ellipse dans la phrase d'origine. Les insécables manquants se voyaient au PDF, l'unité manquante non.
4. **Même texte au caractère près** entre le fichier de travail et le livrable. Le contrôle se fait sur le
   source dépouillé de ses balises par regex, **jamais par un parseur** : `html.parser` avale le contenu
   d'un `<template>`, donc celui d'un `<UAlert>`, ce qui masquerait une perte réelle.

## Le périmètre de comptage des mots

Fixé et reproductible depuis le Chapitre 4 : **l'accroche et le corps**. En sortent la vidéo, les
sous-titres, les blocs d'écritures, les légendes de bloc, la légende d'illustration, le composant,
l'`<UAlert>`, la précision et le bloc « Ce que vous avez appris ». C'est celui des Chapitres 1, 2, 3 et 7.

## Cinq pièges, tous rencontrés

1. **Copier le fichier source sous un autre nom avant de commencer.** `livrer.py` écrit le `.corps.html`
   livrable à l'emplacement du fichier d'origine, et `patch_chNN.py` ne retrouve plus sa source si on
   relance la chaîne.
2. **Écrire `NB = '\u00a0'`, avec la séquence d'échappement, jamais l'insécable au clavier**, et faire
   suivre de `assert NB == chr(160)`. Un insécable tapé littéralement se dégrade en espace ordinaire au
   fil des copies, sans que rien ne le signale : les substitutions s'appliquent alors sans rien changer,
   ou ne trouvent plus leur motif. **Le piège a été rencontré quatre fois** sur cinq chapitres, dont deux
   après avoir écrit l'avertissement ci-dessus dans sa version faible. L'assertion est la seule parade
   qui tienne.
3. **L'annexe porte ses insécables elle aussi.** Elle ne sort jamais du PDF, mais elle est pleine de
   sommes et de guillemets, et WeasyPrint coupe volontiers un `»` ou un `€` en début de ligne. Les quatre
   substitutions de fin d'`annexe_chNN.py` s'occupent des deux.
4. **`rejeu.py` ne cherche le numéro de compte qu'après « Bilan — », « CR — » ou « GdJal seul — »**, et
   compte en centimes entiers. Deux défauts trouvés à la passe, et ils suivent la même loi : **un script
   ne se trompe que sur ce qu'aucun chapitre antérieur ne lui avait présenté.** Le numéro était cherché
   n'importe où sur trois chiffres, ce qui lisait les milliers des montants — invisible jusqu'au
   Chapitre 5, premier à porter des comptes à quatre chiffres. Et les centimes n'étaient pas lus,
   « 628,90 » valant 90 — invisible jusqu'au Chapitre 7, premier à en porter.
5. **Relire le PDF en images.** Les coupures de ligne fautives ne se voient nulle part ailleurs, et
   `pdftotext` rend les insécables en espaces ordinaires : un contrôle sur le texte extrait ne prouve
   rien.

## Ce que les scripts ne font pas

Ils ne décident rien. Le choix des deux-points à garder, l'entrée du registre qui sort par le haut et le
point d'ancrage de la précision se tranchent à la lecture, pas au comptage. `compter.py` dit où regarder,
`rejeu.py` dit si une phrase de mécanisme est vraie, `livrer.py` dit si un nombre annoncé est faux. Le
reste est de la rédaction.

**Et ils ne tranchent surtout pas un point de fond.** Deux sont restés ouverts à la passe des huit
chapitres, laissés intacts dans le texte et documentés à leur annexe. Au Chapitre 5, la légende du panneau
automatique demande de regarder un total bouger *pendant* qu'une ligne s'inscrit, ce qui est faux sur un
écran étroit. Au Chapitre 6, l'origine des 15 000 € de stock n'est écrite nulle part, ce qui interdit d'en
faire une précision. La passe coupe les deux-points et ne touche à rien d'autre.

## Ce que la passe des huit chapitres a donné

123 deux-points en prose courante ramenés à 34, trois à cinq par chapitre, **à coût nul en mots sur
l'ensemble**. Sept entrées du registre sorties par le haut, une précision par chapitre. Dix nombres
annoncés pris en défaut, dont le total de contrôle du module. Le détail est aux annexes des chapitres, et
le bilan aux blocs « Changements » du déroulé v20 et de la charte v13.

## Écrire un chapitre neuf — ajouté le 24 août 2026, Chapitres 9 et 10

La chaîne ci-dessus est celle d'une reprise. Pour un chapitre qui n'existe pas encore, l'ordre est
celui-ci, et il ne produit **pas** de `.corps.html` : la charte, section 22, réserve ce fichier à la
livraison.

```
python3 gen_chNN.py                                # texte + chapo → chNN-travail.html
python3 compter.py chNN-travail.html               # mots et deux-points, avant d'écrire l'annexe
cp chNN-travail.html chapitre-NN-....corps.html    # copie de rejeu SEULEMENT, jamais livrée
python3 rejeu.py NN                                # vérifie chaque nombre des légendes
python3 annexe_chNN.py                             # annexe RÉDUITE aux points de vigilance
python3 livrer.py chNN-travail.html /tmp/jeter.html "Chapitre N — Titre"   # les 4 contrôles
python3 pdf_relecture.py chNN-travail.html chapitre-NN-relecture-vV.pdf "Chapitre N — Titre"
pdftoppm -png -r 90 chapitre-NN-relecture-vV.pdf page   # relire en images, toujours
```

`livrer.py` est lancé sur une destination jetable : on ne veut que ses quatre contrôles, pas son
livrable. Il écrit aussi `pdf-livraison.html`, à supprimer.

| Script | Rôle | Générique ? |
|---|---|---|
| `pdf_relecture.py <travail> <sortie.pdf> "<titre>"` | Le PDF de relecture : texte, chapo et annexe, `body.relecture`, donc ancre de précision en souligné plein. Pendant de `livrer.py`, qui ne fabrique que le PDF de livraison. | oui |
| `gen_ch09.py`, `gen_ch10.py` | Le texte du chapitre, écrit avec `~` partout où un insécable est requis, substitué en une fois. **Modèles** pour les Chapitres 11 à 13. | non |
| `annexe_ch09.py`, `annexe_ch10.py` | L'annexe de relecture, réduite aux points de vigilance. **Modèles** — `annexe_ch08.py` reste le modèle de l'annexe de contrôle complète. | non |

**Le `~` plutôt que l'insécable littéral.** Le piège 2 s'est reproduit une fois de plus, à la première
écriture de `gen_ch10.py` : l'assertion l'a attrapé. Écrire le texte avec `~` et substituer en une passe
supprime la classe entière — il n'y a plus qu'un seul endroit où l'insécable puisse se dégrader, et
l'assertion le garde.

**Deux nombres que `livrer.py` recompte n'ont pas de « avant » sur un chapitre neuf.** Le budget de
deux-points s'écrit `0 → 0` ou `1 → 1`, et l'annexe explique que la notation vaut *premier jet → état
soumis*. C'est ce qui permet au contrôle 2 de rester armé.

## Chapitres 10 v5 et 11 — ajouté le 25 août 2026

L'écart de 22 648,50 € est tranché : les lignes manquantes vont à l'écriture de période du Chapitre 10,
et le Bilan y est réparé dans le même panneau. La chaîne des deux chapitres, dans l'ordre :

```
python3 patch_ch10.py                                # v4 livrée → ch10-travail.html
python3 gen_ch11.py                                  # ch11-travail.html
cp ch10-travail.html <dossier>/chapitre-10-….corps.html   # copies de rejeu SEULEMENT
cp ch11-travail.html <dossier>/chapitre-11-la-cloture.corps.html
python3 rejeu.py 11                                  # soldes, bloc par bloc
python3 verif_ecart.py                               # écart au scénario : doit tomber à 0
python3 verif_cloture.py                             # le Bilan boucle-t-il sur 130 410 €
python3 annexe_ch10r.py ; python3 annexe_ch11.py
python3 controle_checklist.py chNN-travail.html
python3 livrer.py chNN-travail.html /tmp/jeter.html "…"   # les 4 contrôles seuls
python3 pdf_relecture.py … ; pdftoppm -png -r 90 …
python3 repercuter_ch11.py                           # le registre SEUL, avant validation
```

| Script | Rôle | Générique ? |
|---|---|---|
| `verif_cloture.py` | Reconstruit le Bilan et le Compte de Résultat au terme du dernier chapitre et les compare au scénario du déroulé, section 3. **Il existe parce que `rejeu.py` ne sait pas lire une ligne « Bilan seul »**, la destination que la charte, section 17, réserve à un report calculé par l'application. C'est lui qui a fourni tous les nombres des légendes des deux chapitres. | oui |
| `patch_ch10.py` | La reprise du 10. Son `rep()` tolère les trois formes d'espace **et découpe le motif sur `split()` et non sur `split(' ')`**, ce qui le rend insensible aux retours à la ligne du source. À reprendre comme modèle plutôt que `patch_ch08.py`. | non |
| `gen_ch11.py`, `annexe_ch11.py`, `annexe_ch10r.py` | Modèles pour les Chapitres 12 et 13. | non |
| `repercuter_ch11.py` | Le registre des écarts seul. Le déroulé, la charte et le journal attendent la validation. | non |

**Trois défauts d'outil trouvés, et ils suivent la même loi qu'avant** — un script ne se trompe que sur
ce qu'aucun chapitre antérieur ne lui avait présenté.

1. **`rejeu.py` ne lit pas « Bilan seul »**, première destination de ce type du module. Il l'annonce en
   ligne non lue et son contrôle d'équilibre reste vrai, le bloc ne portant aucune écriture de journal.
   **Le script n'a pas été modifié** ; `verif_cloture.py` a été écrit à côté.
2. **`rejeu.py` vérifie l'équilibre du panneau entier**, pas de chaque écriture qu'il contient. Le
   panneau du Chapitre 10 en porte trois : l'équilibre de chacune se vérifie à part.
3. **`pdf_relecture.py` portait la date en dur**, « 24 août 2026 », et un PDF produit un autre jour la
   portait quand même. Elle se prend désormais à l'horloge.

**Le contrôle 2 de `livrer.py` a levé une fois, et à raison** : l'annexe du Chapitre 10 annonçait
« 9 → 27 LIGNES » dans une cellule d'état, et le motif `(\d+)\s*LIGNES` y lisait le nombre d'écritures
manuelles. **Ne jamais écrire « LIGNES » en capitales ailleurs que dans la cellule des écritures
manuelles.**

## La livraison des Chapitres 10 v5 et 11 — 25 août 2026

```
python3 annexe_chNN.py complete          # l'annexe passe de « relecture » à « contrôle »
python3 livrer.py chNN-travail.html chapitre-NN-….corps.html "Chapitre N — Titre"
weasyprint pdf-livraison.html chapitre-NN-livraison-vV.pdf
python3 repercuter_v22.py                # déroulé v21 → v22, et journal
python3 verif_comptes.py ; python3 balise.py *.corps.html
pdftoppm -png -r 90 …                    # relire en images, toujours
```

**`annexe_chNN.py complete` est la forme retenue** — un seul script par chapitre, deux modes. L'argument
ajoute les lignes de contrôle aux lignes de vigilance et change le titre de l'annexe. La v4 du Chapitre 10
avait deux scripts pour ça, c'est un de trop.

**`repercuter_v22.py` est le modèle d'une répercussion groupée**, et il ajoute une leçon à celles de
`repercuter_ch0910.py` : **le `~` du marqueur d'insécable entre en collision avec le `~` de
l'approximatif**, « ~6h10 » au tableau de la section 9. La méthode `rep()` prend donc un paramètre
`brut=True` qui laisse le fragment intact. L'assertion l'a attrapé, et les fichiers étaient intacts —
l'écriture à la toute fin fait son travail.

**Trois nombres annoncés ont encore été pris en défaut**, ce qui porte à treize le compte du module :
le décompte de fin du registre, resté à 51 quand l'en-tête passait à 57 ; et deux constantes de
`verif_comptes.py` lui-même.

**`verif_comptes.py` portait deux noms de fichier en dur et un compte en dur**, et cassait donc à chaque
répercussion. Corrigé le 25 août 2026 : le déroulé et la charte se prennent par `glob` sur la version la
plus récente, la liste des documents contrôlés en typographie se prend au dossier, et **le compte des
précisions se lit dans la phrase d'état que le déroulé porte lui-même** plutôt que d'être écrit dans le
script. La règle qui en sort : *un script de contrôle ne porte jamais un nombre qu'un document annonce —
il compare deux endroits du même document.*

**`verif_ecart.py` a fait son travail et n'en a plus.** Il compare l'état de la grille au scénario en
supposant que le Chapitre 11 n'est pas écrit ; depuis qu'il l'est, ses deux lignes d'impôt entrent dans
son total de charges et le script annonce un écart qui n'en est pas un. **C'est `verif_cloture.py` qui
prend le relais** — il sépare les comptes par leur destination et reconstruit les deux documents.

## Le Chapitre 12 — ajouté le 25 août 2026

Premier chapitre du module **sans aucune écriture**. La chaîne perd donc `rejeu.py` et `verif_cloture.py`,
qui n'ont rien de neuf à rejouer, et gagne un contrôle qui leur correspond.

```
python3 gen_ch12.py                                  # texte + chapo → ch12-travail.html
python3 compter.py ch12-travail.html                 # mots et deux-points, AVANT l'annexe
python3 verif_ratios.py                              # tous les nombres, recalculés depuis les panneaux
python3 annexe_ch12.py                               # annexe réduite aux points de vigilance
python3 controle_checklist.py ch12-travail.html
python3 balise.py ch12-travail.html
python3 livrer.py ch12-travail.html /tmp/jeter.html "Chapitre 12 — …"   # les 4 contrôles seuls
python3 pdf_relecture.py ch12-travail.html chapitre-12-relecture-vV.pdf "…" vV
pdftoppm -png -r 90 …                                # relire en images, toujours
python3 repercuter_ch12.py                           # le registre SEUL, avant validation
```

| Script | Rôle | Générique ? |
|---|---|---|
| `verif_ratios.py [travail]` | Reconstruit le Bilan et le Compte de Résultat depuis les panneaux, recalcule les outils de lecture et la décision, puis **confronte une à une toutes les sommes et tous les pourcentages du texte** à ce recalcul. Une somme qui ne se recalcule pas mais figure sur une ligne d'écriture d'un chapitre est signalée comme *renvoi*, avec le chapitre. Il ne porte **aucun nombre en dur venu d'un document** : le prix TTC de la machine se déduit du torréfacteur du Chapitre 8 par le taux de taxe, seul paramètre écrit. | oui, pour un chapitre de lecture |
| `gen_ch12.py`, `annexe_ch12.py`, `repercuter_ch12.py` | Modèles pour le Chapitre 13, qui est lui aussi sans écriture. | non |

**Un défaut d'outil, et il suit la même loi que les précédents.** `controle_checklist.py` exigeait la glose
(emploi) et (ressource) une fois chacune, et levait donc sur un chapitre qui ne passe aucune écriture et
n'a pas de première occurrence à gloser. **Corrigé** : la case se déclare *sans objet* quand le fichier ne
porte aucune ligne d'écriture. Elle reste armée dès qu'il en porte une.

**Ce que `livrer.py` annonce et qu'il faut lire comme normal sur un tel chapitre** : `(\d+)\s*LIGNES` en
annonce non trouvée, l'annexe n'ayant pas de cellule d'écritures manuelles. Son contrôle 2 reste armé sur
les mots, les mots avec sous-titres et les deux-points.

**Le décompte de fin du registre était faux**, quatorzième nombre annoncé pris en défaut dans le module :
il annonçait cinquante-quatre candidates et deux précisions quand le fichier en portait dix. Le total
tombait juste, ce qui l'a rendu invisible. `repercuter_ch12.py` recompte désormais **les trois sous-totaux
par script**, à la même passe que le total, et `verif_comptes.py` les revoit.

## Chapitre 13 — ajouté le 26 août 2026

Dernier chapitre du module. Sa chaîne est celle d'un chapitre neuf, avec **deux blocs qu'aucun chapitre
antérieur n'avait présentés aux scripts** : un glossaire de 70 termes en `<table>` et une liste de onze
écarts en `<dl>`.

```
python3 gen_ch13.py                  # texte + les deux blocs assemblés depuis leurs sources
python3 compter.py ch13-travail.html
python3 annexe_ch13.py               # annexe réduite aux points de vigilance
python3 livrer.py ch13-travail.html /tmp/jeter.html "Chapitre 13 — …"   # les 4 contrôles
python3 verif_ch13.py ch13-travail.html                                 # ce que les 4 ne voient pas
python3 controle_checklist.py ch13-travail.html
python3 balise.py ch13-travail.html
python3 repercuter_ch13.py           # registre seul, avant validation
python3 pdf_relecture.py ch13-travail.html chapitre-13-relecture-vV.pdf "…" vV
pdftoppm -png -r 90 …
rm -f /tmp/jeter.html pdf-livraison.html
```

**Les deux blocs ne sont pas rédigés dans `gen_ch13.py`, ils y sont assemblés.** Le glossaire vient de la
section 11 du déroulé, la liste des écarts du registre. Chaque retouche est déclarée dans le script avec une
assertion sur son motif : si la source change, le script s'arrête au lieu de produire un texte divergent.
C'est ce que la fiche exige — « l'aside assemble et enchaîne des phrases déjà écrites, il n'en rédige
aucune ».

**Nouveau piège, et il complète le piège 4.** Les quatre contrôles de `livrer.py` ne regardent que les
`<p>` et les `<li>`. Un bloc en `<dl>` ou en `<table>` **passe les quatre sans être vu** : ni budget de
deux-points, ni typographie des sommes. `verif_ch13.py` est écrit à côté pour cela, comme `verif_cloture.py`
l'avait été à côté de `rejeu.py`.

**Et le piège 4 lui-même s'est reproduit dans `verif_ch13.py` en l'écrivant** : `'' in '€%'` est vrai, donc
le contrôle d'unité levait sur chaque chiffre du glossaire. Troisième apparition du cas dans le module.
Écrire `if suite[:1] and suite[:1] in '€%'`.

**Le contrôle du vocabulaire de fabrication est dans `verif_ch13.py`** et il est reproductible sur
n'importe quel chapitre : un mot que le déroulé emploie au moins huit fois et qu'aucun chapitre livré ne
porte est un candidat. Le seuil sépare les mots par lesquels le déroulé *désigne* les objets du module du
français ordinaire. Il a évité trois mots au Chapitre 13 : « parcours », « lexique » et « aside ».

**`repercuter_ch13.py` ajoute une quatrième valeur de destination au registre, `aside`**, et recompte les
quatre sous-totaux à chaque exécution avec une assertion. Sans elle, le tri n'est plus vérifiable.
