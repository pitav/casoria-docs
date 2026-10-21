# Process de fabrication d'un module

**Statut.** Document vivant. Il décrit, dans l'ordre, comment un module de Casoria se fabrique, tel que le module 1 l'a été (août – octobre 2026), avec ce qu'on referait autrement. Chaque étape dit qui fait quoi, ce qu'elle produit, et ce qui la clôt. Les règles de forme sont dans les chartes ; ce document ne les répète pas.

**Changements (20 octobre 2026).** Première version. À éprouver sur le module 2 : chaque fois qu'il faudra aller chercher une règle ailleurs que dans `methode/`, c'est un trou à boucher ici.

---

## Vue d'ensemble

| # | Étape | Produit | Clôturée par |
|---|---|---|---|
| 1 | Concevoir le module | Le déroulé | Validation du déroulé par le décideur |
| 2 | Rédiger un chapitre | Le texte, en PDF de relecture | Relecture profane + validation |
| 3 | Concevoir un composant ou une illustration | Une fiche, puis le `.vue` | Validation dans l'application |
| 4 | Faire la vidéo du chapitre | HTML, puis MP4 et affiche | Validation du HTML, puis livraison |
| 5 | Intégrer dans l'application | La page `.vue` du chapitre | Le chapitre fonctionne dans l'application |
| 6 | Clore le module | Dernier chapitre, tri du registre, relecture externe | Le module est publiable |
| — | Corriger un module livré | Une passe de correction | Décisions reportées dans le déroulé |

Les étapes 2 à 5 se répètent pour chaque chapitre. Elles ne sont pas strictement séquentielles : une illustration peut se faire pendant la relecture du texte. Mais **le texte d'un chapitre se valide avant sa vidéo**, puisque la vidéo en reprend le bloc « Ce que vous avez appris ».

---

## 1 — Concevoir le module : le déroulé

**Qui.** Le rédacteur écrit, le décideur tranche, le relecteur de fond vérifie le scénario : exactitude des écritures, réalisme des situations, plausibilité des montants, progression des notions. Plusieurs séances.

**Le déroulé est le document maître du fond.** La charte dit comment écrire ; le déroulé dit quoi écrire. Il contient, dans cet ordre :

1. **La promesse du module** : ce que l'apprenant saura lire à la fin, en une phrase.
2. **Le fil rouge** : l'entreprise suivie tout au long du module, ses personnes, ses clients et fournisseurs, avec leur rôle.
3. **Les documents de la simulation** (si le module en a) : les lignes affichées, leur intitulé exact, l'ordre d'apparition.
4. **Le scénario chiffré** : toutes les opérations de l'exercice, avec leurs montants, **vérifié par script** (le Bilan boucle, les totaux du journal sont égaux).
5. **Les écritures** : pour chaque chapitre, ce qui se passe à la main et ce qui est automatique, et où se place le panneau automatique.
6. **La table des composants** et le recensement des alertes, chapitre par chapitre.
7. **Les activités et les quiz.**
8. **La vue d'ensemble** : une ligne par chapitre (titre, notion, déclaration, refrain).
9. **Les fiches de chapitre** : pour chacun, l'objectif, les notions, l'accroche visée, les écritures, le composant, l'illustration, ce qu'on écarte.
10. **Le lexique cumulatif** : chaque terme, le chapitre qui l'introduit, sa définition.
11. **Les vigilances de vocabulaire propres au module**, dont le vocabulaire de fabrication.
12. **L'ordre de rédaction** des chapitres (qui n'est pas forcément l'ordre de lecture).
13. **Les points ouverts**, chacun avec sa question au décideur.

**Ce qu'on referait autrement.** Dans le M1, le déroulé a fini par contenir une copie du texte des chapitres et l'historique de ses trente versions. Il doit rester une spécification : il décrit le chapitre, il ne le contient pas. Le texte vit dans l'application.

**Le titre du module** suit la règle : « [Verbe] + [le / la / les + objet] + sans être + [identité experte] », article défini, jamais de possessif (*Comprendre la comptabilité sans être comptable*).

**Clôture.** Le relecteur de fond a relu le scénario chiffré et les fiches, et le décideur valide le déroulé. Les chapitres peuvent commencer ; le déroulé continue d'évoluer, mais par décision, jamais en silence.

---

## 2 — Rédiger un chapitre

**Qui.** Le rédacteur ; puis le relecteur profane et le relecteur de fond, en parallèle ; puis le décideur.

**Ce que le rédacteur relit avant d'écrire** : la page « L'essentiel » de la charte, la fiche du chapitre et celle du chapitre précédent dans le déroulé, le lexique, les vigilances du module, le registre des écarts, et le texte des chapitres cités par un renvoi.

**Les étapes** (charte, § 22) :

1. **Premier jet**, compté par script (mots, deux-points) avant toute autre chose.
2. **Vérifications mécaniques par script** : rejeu des écritures (chaque montant cité dans le texte est celui que l'écran affiche à cet instant), budget de ponctuation, insécables, vocabulaire interdit et de fabrication, checklist.
3. **PDF de relecture**, avec une annexe réduite aux points de vigilance. Relu en images, pas en texte extrait.
4. **Deux relectures, sur le même PDF.** Le relecteur profane signale ce qu'il ne comprend pas ; chaque tournure signalée se corrige et se consigne au journal de rédaction. Le relecteur de fond signale ce qui est faux, discutable ou manquant ; une simplification assumée (alerte, registre) n'est pas une erreur, sauf si elle fait comprendre quelque chose de faux.
5. **Tours de relecture** avec le décideur. Chaque proposition de modification : avant / après / pourquoi.
6. **Validation** par le décideur. Seulement alors, le texte passe dans la page `.vue` (étape 5).
7. **Report** : ce que le chapitre a décidé et qui vaut pour la suite remonte au déroulé ; ce qu'il a écarté est déjà au registre (on l'écrit au fil de la rédaction, pas après).

**Clôture.** Le chapitre est validé et ses écarts sont au registre.

---

## 3 — Concevoir un composant ou une illustration

**Qui.** Le rédacteur conçoit et code ; le décideur valide et intègre.

1. **Le test de la règle 0, avant tout** (`composants-et-illustrations.md`) : le geste demandé fait-il ce que le texte ne peut pas faire ? Si non, c'est une illustration, ou rien.
2. **La fiche**, sur le gabarit `gabarits/fiche-composant.md` : objectif, matière disponible et écartée, consigne, réponses et retours rédigés, maquettes à 720 px et en étroit.
3. **Validation de la fiche** par le décideur.
4. **Le code** (`.vue`), selon les conventions de code (`composants-et-illustrations.md`), testé à toutes les largeurs et en contraste élevé.
5. **Intégration et validation dans l'application.**

Pour une illustration : une source HTML d'abord, validée en image, puis portée en `.vue`. La source est gardée pour fabriquer les images des PDF et des vidéos.

---

## 4 — Faire la vidéo d'un chapitre

**Qui.** Le rédacteur fabrique ; le décideur valide à l'écoute.

1. **Cahier des charges** : le bloc « Ce que vous avez appris » du chapitre validé.
2. **Le script de voix**, en segments d'environ 15 secondes, environ 430 mots au plus.
3. **La voix** (quota de 100 requêtes par jour : prévoir), puis le **gabarit animé** calé sur la voix, à partir du gabarit existant le plus proche.
4. **Vérification en lecture réelle**, son compris.
5. **Livraison du HTML seul.** Le décideur retouche, souvent à des instants précis.
6. **Après validation** : MP4 et affiche, rangés dans `videos/<module>/<slug-de-la-page>.*`, à l'intérieur du dossier du module (nommage : `charte-videos.md`).

Toutes les règles sont dans `charte-videos.md`.

---

## 5 — Intégrer dans l'application

**Qui.** Le décideur, avec le rédacteur quand le dossier de l'application est connecté à la séance.

- **La page `.vue` du chapitre est la source de vérité du texte.** Toute correction ultérieure se fait dans la page, et ce qui touche une décision se reporte au déroulé.
- **Le titre affiché reprend exactement le titre de la page**, et le slug de la page nomme aussi la vidéo.
- Les composants et illustrations vont dans `components/<module>/` ; les styles d'activité dans `activite.css`, ceux des illustrations dans `illustrations.css`.
- **Vérifier dans l'application** ce que le texte dit de l'écran : chaque montant cité, chaque ligne nommée, à l'instant du parcours où le texte en parle.

---

## 6 — Clore le module

1. **Le dernier chapitre** fait la synthèse, porte le glossaire et la liste de ce que le module a écarté (charte, § 2).
2. **Le tri du registre des écarts**, selon les critères que le déroulé a fixés d'avance : ce qui va à l'encadré de fin de module, ce qui part à un module ultérieur, ce qui reste.
3. **La relecture du module achevé, d'un bout à l'autre**, par le relecteur de fond et par au moins un lecteur du public visé : non plus « cette phrase est-elle lisible », mais « ce parcours tient-il ».
4. **Les candidats de charte** : les règles qui n'ont qu'une attestation dans ce module restent au journal ; elles entreront dans la charte si le module suivant en donne une seconde.

---

## Corriger un module livré

C'est ce que le M1 a vécu le 13 octobre 2026, après les retours de premiers lecteurs (texte parfois alambiqué, renvois peu clairs aux chapitres précédents).

1. **Rassembler les retours** et les classer : lisibilité, renvois, erreurs de fond, cohérence avec le glossaire. Les erreurs de fond passent par le relecteur de fond avant toute correction.
2. **Lire chapitre par chapitre** le texte extrait des pages `.vue`.
3. **Proposer en avant / après / pourquoi**, par lot, pour validation.
4. **Appliquer par script**, avec une vérification que chaque remplacement ne touche qu'un seul endroit, puis comparer avant et après.
5. **Reporter au déroulé** ce qui touche une décision ; **remonter à la charte** ce qui est devenu une règle générale.
6. **Ne pas oublier les vidéos** : une correction de vocabulaire dans un chapitre peut rendre sa vidéo incohérente.
