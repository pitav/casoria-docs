# Passe finale de clarification — propositions (13 octobre 2026)

Relu : les 14 pages `.vue`, le glossaire, la colonne « Ce que ce module a écarté », le texte visible des illustrations. Pas les textes internes des activités (option déjà ouverte).
**Rien n'est modifié.** Aucune proposition n'ajoute de deux-points (budget d'un « : » par section). Répondez « vas-y », ou « oui sauf n° … ».

---

## A. Erreurs et contradictions (à corriger en priorité)

**1. *La TVA* — section « Le compte en banque a porté… »**
- Avant : « Rien ne les distinguait sur la facture. »
- Après : « Rien ne les distinguait sur le compte en banque. »
- Pourquoi : une facture sépare justement le HT et la TVA, c'est ce que le chapitre vient de montrer. C'est sur le compte que les deux se mélangent, et le titre de la section le dit.

**2. *Clôture de l'exercice* et *Décider avec trois chiffres* — « ce qu'elle gardera tant qu'elle vivra »**
- Avant (Clôture) : « Il range côte à côte ce qu'elle devra rendre à sa banque et à ses fournisseurs, et ce qu'elle gardera tant qu'elle vivra. »
- Après : « Il range côte à côte ce qu'elle devra rembourser, à sa banque comme à ses fournisseurs, et ce qu'elle n'a pas à rembourser. »
- Avant (Décider) : « …la part de ce que l'entreprise détient qu'elle gardera tant qu'elle vivra, par opposition à ce qu'elle devra rendre. »
- Après : « …la part de ce que l'entreprise détient qu'elle n'a pas à rembourser, par opposition à ce qu'elle doit. »
- Pourquoi : deux paragraphes plus haut, les 27 200 € « ne sont pas une somme que Latitude Café garde pour elle », et une partie peut repartir en dividende. Dire « qu'elle n'a pas à rembourser » reste vrai dans les deux cas.

**3. *Décider avec trois chiffres* — la suite**
- Avant : « …est l'objet d'une formation à part, qui suppose des comptes déjà tenus et déjà lus. »
- Après : « …est l'objet des modules suivants. »
- Pourquoi : la *Synthèse* parle des « modules suivants », comme vous l'avez décidé. Et elle redit déjà « Ils supposent des comptes tenus et lus ».

**4. *Synthèse et feuille de route* — la machine refusée**
- Avant : « …là où *Décider avec trois chiffres* s'est arrêté, quand trois chiffres ont suffi à refuser une machine à 43 200 €, et portent… »
- Après : « …là où *Décider avec trois chiffres* s'est arrêté, devant une machine à 43 200 € que la trésorerie ne permettait pas d'acheter, et portent… »
- Pourquoi : la machine est refusée à cause de la trésorerie (17 310 €). Le BFR et les deux ratios viennent après, pour expliquer.

**5. *Naissance de l'entreprise* — le risque de l'associé**
- Avant : « …un risque pour l'associé, qui sera remboursé le dernier si les choses tournent mal. »
- Après : « …un risque pour l'associé, qui risque de ne rien récupérer si les choses tournent mal. »
- Pourquoi : en cas de faillite, c'est le capital qui passe en dernier. Le compte courant est remboursé avant lui, comme les fournisseurs. Le risque est réel, mais « le dernier » est faux.

**6. *Investir* et *Produire et stocker* — noms de lignes absents de `comptes.ts`**
- « Stock de café torréfié » → « Stocks » (le Bilan affiche « 355 Stocks », avec « Café torréfié » en précision). La même étiquette est à changer dans `StockLuDeuxFois.vue`.
- « Amortissements du torréfacteur » → « Amortissements des immobilisations ».
- Pourquoi : c'est votre règle (« une ligne <nom exact> apparaît »). « Torréfacteur », « Trésorerie » et « Ventes aux professionnels » sont des précisions affichées à l'écran : je les laisse.

**7. Illustration `DeuxColonnes.vue` (hors chapitre)**
- Le Compte de Résultat affiche « Achats 1 200 », alors que le texte et la Banque (28 520) supposent 1 800. Le `aria-label` est lui aussi périmé : il parle d'un achat de 1 200 €, d'un salaire de 450 € et d'une Trésorerie qui baisse de 450 €.
- Proposition : « Achats 1 800 », et un `aria-label` réécrit sur les trois opérations réellement dessinées (apport, achat, vente).

## B. Clarifications

**8. *Du document à l'écriture***
- Avant : « Les trois opérations de janvier remplissent les deux mêmes colonnes du journal et ne finissent pas au même endroit. »
- Après : « Chacune des trois opérations de janvier s'inscrit dans les deux colonnes du journal, mais ses deux lignes ne finissent pas dans le même document. »
- Pourquoi : la phrase actuelle laisse croire que les trois opérations finissent à trois endroits différents.

**9. *Du document à l'écriture* — légende du panneau Électricité**
- Avant : « Ce que Latitude Café consomme sans le revendre se range sous « Autres charges externes ». »
- Après : « Les services que Latitude Café consomme, et qui n'entrent pas dans le café qu'elle vend, se rangent sous « Autres charges externes ». »
- Pourquoi : le café vert n'est pas revendu non plus, et pourtant il va ailleurs.

**10. *Du document à l'écriture* — « Ce que vous avez appris »**
- « Toute opération s'inscrit deux fois, en sens contraire » → « …deux fois, une fois au débit, une fois au crédit ». « En sens contraire » n'apparaît nulle part dans le chapitre. Même correction dans la définition du glossaire (*Comptabilité en partie double*).
- « …ce qu'elle détient reste au Bilan » → « …ce que l'entreprise détient reste au Bilan ». Sans ce changement, « elle » renvoie à « l'activité ».

**11. *Le Bilan et le Compte de Résultat***
- « La plupart ne vous disent rien pour l'instant, et chacun recevra son chapitre. » → « …et chacun sera expliqué en son temps. » Toutes les lignes n'ont pas un chapitre à elles.
- « Entre-temps, il arrivera souvent qu'ils ne soient pas égaux, et ce sera normal. » → « Entre-temps, ils ne seront presque jamais égaux, et ce sera normal. » La version actuelle ne s'accorde pas avec l'alerte de *Naissance* : les totaux sont inégaux de la première vente jusqu'à la *Clôture*.

**12. *Produire et stocker* — le résultat qui monte**
- Avant : « Ce qui ne veut pas dire que Latitude Café s'est enrichie de 15 000 € en torréfiant. »
- Après : « Le résultat monte donc de 15 000 €, sans que Latitude Café se soit enrichie en torréfiant. La variation ne fait qu'annuler la charge d'un café qu'elle a encore. »
- Pourquoi : le lecteur voit le résultat monter et lit qu'elle ne s'est pas enrichie. Rien ne lui dit comment ces deux faits tiennent ensemble.

**13. *Se financer* — accroche**
- Avant : « …la somme est là, elle n'est pas disponible. »
- Après : « …la somme est là, mais une fois les fournisseurs payés, il ne resterait que 21 200 €. »
- Pourquoi : la phrase fait elle-même le calcul que le lecteur devait faire seul.

**14. *Se financer* — le compte courant**
- Avant : « …et cet argent-là dort dans l'entreprise au lieu de servir ailleurs. »
- Après : « …et cet argent, l'associé ne peut plus s'en servir ailleurs. »
- Pourquoi : dans l'entreprise, l'argent ne dort pas. C'est pour l'associé qu'il est bloqué.

**15. *Se financer* — « Elle » orphelin**
- Avant : « Elle se partage en deux parts qui n'ont rien à voir l'une avec l'autre. »
- Après : « La mensualité se partage en deux parts qui n'ont rien à voir l'une avec l'autre. »
- Pourquoi : le paragraphe sur le taux variable s'est glissé entre les deux. « Elle » renvoie maintenant à « l'échéancier signé ».

**16. *Se financer* — pourquoi les intérêts sont une charge**
- Avant : « Rien au Bilan n'en garde la trace, et c'est ce qui en fait une charge… »
- Après : « Il n'en reste rien à l'entreprise, et c'est ce qui en fait une charge… »
- Même changement dans `UneMensualiteDeuxParts.vue` (« Rien au Bilan n'en garde la trace. »).
- Pourquoi : le compte en banque, au Bilan, garde bien la trace de la sortie. La vraie raison est celle de *Du document à l'écriture* : « il n'en reste rien à l'entreprise ».

**17. *Se financer* — légende de la première échéance**
- « …le total des charges monte de 33 000 € à 33 087,50 €, et de rien d'autre. » → « …à 33 087,50 €, et rien d'autre n'y bouge. »

**18. *La TVA* — les 270 €**
- Avant : « Le solde du compte en banque se déplace de 270 € au même moment. » suivi de « Les règlements au comptant de janvier avaient été passés hors taxes, et c'est le trimestre qui les porte désormais. »
- Après : « Le compte en banque bouge lui aussi, de 270 €, parce que les règlements de janvier, passés hors taxes, sont désormais portés par le trimestre. »
- Pourquoi : le montant et sa raison étaient dans deux paragraphes séparés.

**19. *La TVA* — « on l'a vu »**
- « …et une facture professionnelle, on l'a vu, attend son échéance. » → « …et une facture professionnelle, comme dans *Facturé n'est pas encaissé*, attend son échéance. » (règle du renvoi par titre)

**20. *Les salariés* — le décalage sur une charge**
- Avant : « Vous avez déjà rencontré ce décalage dans *Facturé n'est pas encaissé*, où la vente était inscrite avant que l'argent n'arrive. Il joue ici dans l'autre sens, sur une charge. »
- Après : « Vous avez déjà rencontré ce décalage dans *Facturé n'est pas encaissé*, avec la facture de Verdecafé, dont la charge était inscrite avant que l'argent ne parte. »
- Pourquoi : ce chapitre-là avait déjà montré une charge en avance sur le paiement. Écrire « dans l'autre sens » le présente comme une nouveauté.

**21. *Fin de l'exercice* — l'Hôtel Bellevue nommé avant d'être présenté**
- « Or l'assurance et le contrat de l'Hôtel Bellevue font partie de ces opérations. » → « Or l'assurance et le contrat encaissé d'avance font partie de ces opérations. »
- Légende du panneau automatique : « …contiennent le contrat de l'Hôtel Bellevue encaissé le 1er novembre » → « …contiennent le contrat encaissé d'avance le 1er novembre ».
- Pourquoi : le lecteur ne découvre l'hôtel que plus bas (« l'Hôtel Bellevue, un client »).

**22. *Fin de l'exercice* — « écriture de période »**
- « L'écriture de période groupe un trimestre de ventes et d'achats, et le solde de TVA met… » → « Une écriture groupe le trimestre de ventes et d'achats, une autre, le solde de TVA, met… »
- Pourquoi : « écriture de période » n'est défini nulle part.

**23. *Décider avec trois chiffres***
- « Deux chiffres disent donc deux choses différentes. » → « Deux montants disent donc deux choses différentes. »
- Pourquoi : les « trois chiffres » du titre sont le BFR et les deux ratios. Appeler aussi le bénéfice et la trésorerie des « chiffres » brouille le décompte.

**24. *Synthèse et feuille de route***
- « …et le premier chapitre, *Bilan et Compte de Résultat*, l'avait posé… » → « …et *Bilan et Compte de Résultat* l'avait posé… ». Dans l'appli, ce chapitre est la page 2/14 : « le premier chapitre » est ambigu. La forme du titre dépend de la contradiction 4 en attente.
- « …certains cas, qui ne servaient que de loin ce qu'il voulait vous apprendre à lire. » → « …certains cas, qui l'auraient alourdi sans vous aider à lire les comptes. »
- « …c'est n'importe quel bilan ! » → « …c'est n'importe quel bilan. » C'est le seul point d'exclamation du module.

## C. Réductions (sans perte de fond)

**25. *Produire et stocker*** — le paragraphe « La question qui sert de repère… » redit le précédent. Proposition : « La question qui sert de repère depuis le début, où est l'argent, se lit donc au sens large. Une étagère de sachets y répond au même titre qu'un compte en banque. »

**26. *La TVA*** — supprimer « Les six opérations de janvier et février, déjà passées à la main, sont dans ces totaux, taxe comprise cette fois. Il n'y a rien à ressaisir, l'application s'en charge. » La légende du panneau de reprise dit la même chose, au moment où ça se passe.

**27. *Investir*** — légende de l'achat : supprimer « Ils réduisent d'autant ce que l'entreprise doit à l'État. », déjà dit trois lignes plus haut.

**28. *Investir*** — « Cinq ans n'est ni une règle ni un hasard. C'est la durée pendant laquelle l'entreprise pense se servir de la machine, et c'est elle qui l'estime. » → « Cinq ans n'est ni une règle ni un hasard, c'est l'entreprise qui l'estime. » La phrase précédente dit déjà « la durée est celle de l'usage que l'entreprise prévoit ».

**29. Petites retouches** — *Investir* : « sans qu'un euro ne parte » → « sans qu'un euro parte ». *Facturé n'est pas encaissé*, « Ce que vous avez appris » : « …en banque — le résultat n'est pas la trésorerie. » → « …en banque. Le résultat n'est pas la trésorerie. »

## D. Glossaire

**30.** À ajouter : **Plan comptable général** (Ch. 4 — « Liste officielle des comptes, rangés par classes numérotées ») et **Taux fixe / Taux variable** (Ch. 8 — « Taux qui ne bouge pas pendant tout le prêt / qui suit un taux de marché »). Les deux sont nommés et expliqués dans le texte, mais absents du glossaire.

## E. Une question, pas une correction

**31. « cette formation » ou « ce module » ?** Le texte emploie les deux pour la même chose. « Formation » revient environ quatorze fois (Ch. 1, 3, 4, 5, 6, 9, 13, plus l'étiquette de `BrutNet.vue`), « module » partout ailleurs. Faut-il tout aligner sur « ce module » ? Si oui, je fais la liste exacte des remplacements.

---

## Toujours en attente (déroulé v29, section 14)

1. *Naissance* : la *Clôture de l'exercice* citée dans l'alerte.
2. Ordre du sigle : « le besoin en fonds de roulement (BFR) ».
3. *Décider* : capitaux propres « vus dans *Clôture de l'exercice* » (introduits dans *Naissance*).
4. Les trois formes du titre du Ch. 1 (titre, h1, renvois). Les n° 24 et 2 en dépendent en partie.

---

## Appliqué le 13 octobre 2026 (« vas-y »)

Les points 1 à 30 sont dans les `.vue` : 13 pages, `Glossaire.vue`, `DeuxColonnes.vue`, `StockLuDeuxFois.vue`, `UneMensualiteDeuxParts.vue`. Deux retouches en cours de route :

- n° 14 : « …et cet argent, **il** ne peut plus s'en servir ailleurs », pour ne pas répéter « l'associé » deux fois dans la phrase ;
- n° 16 : le texte d'accessibilité de `UneMensualiteDeuxParts.vue` est corrigé lui aussi.

## Point 31 — liste exacte des remplacements, pas encore appliquée

| # | Fichier | Avant | Après |
|---|---|---|---|
| a | bilan-et-compte-de-resultat | à chaque chapitre de cette formation | à chaque chapitre de ce module |
| b | bilan-et-compte-de-resultat | tels que cette formation les affiche | tels que ce module les affiche |
| c | du-document-a-l-ecriture | rien dans cette formation ne vous le demandera | rien dans ce module ne vous le demandera |
| d | facture-n-est-pas-encaisse | tout le reste de la formation | tout le reste du module |
| e | la-tva | C'est un raccourci de la formation. | C'est un raccourci du module. |
| f | produire-et-stocker | Dans cette formation, Latitude Café ne compte son stock | Dans ce module, Latitude Café ne compte son stock |
| g | produire-et-stocker (alerte) | Une seule ligne de stock dans cette formation. | Une seule ligne de stock dans ce module. |
| h | les-salaries | 22 % du brut dans cette formation | 22 % du brut dans ce module |
| i | les-salaries | 42 % du brut dans cette formation | 42 % du brut dans ce module |
| j | les-salaries (alerte) | Le bulletin de paie de cette formation | Le bulletin de paie de ce module |
| k | ce-que-vous-avez-appris | n'a été inventé pour la formation | n'a été inventé pour ce module |
| l | ce-que-vous-avez-appris | Pour les besoins de la formation, ce module a laissé de côté | Pour rester simple, ce module a laissé de côté |
| m | BrutNet.vue (étiquette) | Dans cette formation | Dans ce module |

Pour la ligne l, je propose « Pour rester simple » plutôt que « ce module » : sinon, la phrase dirait deux fois « ce module ».
