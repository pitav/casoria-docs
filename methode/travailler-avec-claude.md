# Travailler avec Claude

**Statut.** Document vivant, pour toute personne qui participe à la fabrication de Casoria, quelle que soit son expérience de l'IA. Il dit comment se répartit le travail, comment se déroule une séance, ce qu'il faut vérifier, et ce qu'il ne faut jamais déléguer.

**Changements (20 octobre 2026).** Première version.

---

## L'essentiel

1. **Claude rédige, un humain décide.** Claude ne valide jamais son propre travail.
2. **Claude ne se souvient de rien d'une conversation à l'autre**, sauf de ce qui est écrit dans le dossier ou dans ses notes de projet. Ce qui n'est pas écrit est perdu.
3. **Une séance = un objectif.** On dit ce qu'on veut obtenir à la fin, et on lui donne les documents qui comptent.
4. **Claude peut se tromper avec assurance**, surtout sur les chiffres et sur ce que l'écran affiche. Tout chiffre se revérifie par un script ou à l'écran, jamais sur parole.
5. **Rien ne change dans le texte de l'apprenant sans un « avant / après / pourquoi »**, et sans accord.
6. **Les secrets (clés d'API, mots de passe) ne se donnent jamais à Claude dans la conversation et ne vont jamais dans le dossier partagé.**

---

## Qui fait quoi

Les rôles sont tenus au sein de l'équipe, qui a les compétences pour décider. Une même personne peut en tenir plusieurs, à une exception près : on ne peut pas être à la fois relecteur profane et relecteur de fond d'une même matière.

| Rôle | Tenu par | Ce qu'il fait |
|---|---|---|
| Rédacteur | Claude | Écrit les chapitres, les fiches de composants, les scripts de vidéo, les documents de référence ; fabrique les PDF, les illustrations, les vidéos ; vérifie par script ; signale ce qui demande une décision. |
| Décideur | L'équipe | Tranche, valide, intègre dans l'application. Ce que la charte et le déroulé ne tranchent pas lui revient. |
| Relecteur profane | Quelqu'un qui ne connaît pas la matière | Lit chaque chapitre et dit ce qu'il ne comprend pas. C'est le seul contrôle qui attrape le jargon déguisé (charte, § 12). |
| Relecteur de fond | Quelqu'un qui connaît la matière | Vérifie que ce qui est enseigné est juste, que les situations d'entreprise sont crédibles, et que le parcours tient. |

### La relecture de fond

Claude peut se tromper sur la matière avec assurance. La relecture de fond, faite par quelqu'un qui connaît la comptabilité et l'entreprise, est ce qui l'attrape. Elle vérifie :

- **l'exactitude** : chaque définition, chaque écriture, chaque montant, chaque règle fiscale ou sociale citée ;
- **le réalisme** : les situations du fil rouge (une machine achetée, un client qui paie en retard, une embauche) sont-elles crédibles pour une petite entreprise ? Les ordres de grandeur sont-ils plausibles ?
- **la progression** : chaque notion arrive-t-elle au bon moment ? Manque-t-il une étape que des apprenants réclameraient ?
- **les quiz et les activités** : la bonne réponse est-elle incontestable, et les mauvaises réponses sont-elles des erreurs que de vrais apprenants commettent ?
- **ce que le module a écarté** (le registre des écarts) : un écart est-il acceptable, ou fausse-t-il la compréhension ?

**Deux précautions.**

1. **Qui connaît la matière ne peut pas en être le relecteur profane.** On ne voit pas qu'une phrase est obscure quand on connaît déjà la réponse. L'expérience de l'enseignement aide à prévoir où les apprenants butent, mais elle ne remplace pas la lecture de quelqu'un qui ne sait pas.
2. **Une simplification assumée n'est pas une erreur.** Casoria promet de faire comprendre, pas de rendre compétent (charte, § 1). Un module allège volontairement certaines choses, et le dit (alertes, registre des écarts). La question à se poser devant une simplification n'est pas « est-ce complet ? » mais « est-ce que cela fait comprendre quelque chose de faux ? ». Si oui, c'est une erreur à signaler ; sinon, c'est un choix, qui se discute avec le décideur.

**Certains choix d'interface sont délibérés** (texte et saisie sur le même écran, erreurs de saisie refusées plutôt que corrigées) : ils sont expliqués dans `composants-et-illustrations.md`. Un retour d'usage qui les met en cause est bienvenu, à condition de partir de leur motif.

## Premiers pas

**Quelques mots du vocabulaire.**

| Mot | Ce que c'est |
|---|---|
| Claude | L'IA d'Anthropic avec laquelle on travaille, dans l'application de bureau Claude. |
| Conversation, séance | Un échange avec Claude, du premier message au dernier. Claude n'en garde rien après, sauf ce qui a été écrit dans un fichier. |
| Contexte | Tout ce que Claude a sous les yeux pendant une séance : vos messages, ses réponses, les fichiers qu'il a lus. Il est limité : sur une très longue séance, le début s'efface. |
| Dossier connecté | Un dossier de votre ordinateur que Claude peut lire et dans lequel il peut écrire pendant la séance (ici, `casoria-docs`). Il ne voit rien d'autre. |
| Notes de projet | Des fiches que Claude écrit lui-même pour se souvenir d'une séance à l'autre. |
| Modèle | La « version » de Claude utilisée. Les plus puissants sont plus lents et plus coûteux ; on les réserve au travail de fond. |
| Points de vigilance | La courte liste, en annexe des PDF de relecture, des questions qui demandent une décision humaine. |

**Une bonne première séance.** Ne pas commencer par produire. Ouvrir une conversation avec le dossier connecté et demander : « Lis `methode/travailler-avec-claude.md` et `methode/charte-redaction.md` (l'essentiel), puis fais-moi une relecture de fond du chapitre *Facturé n'est pas encaissé* : ce qui est faux, ce qui est discutable, ce qui manque. » Puis comparer ses remarques avec votre propre lecture. C'est la meilleure façon de voir ce qu'il sait faire, et où il se trompe.

**Trois réflexes à prendre.**

- **Demander comment il sait.** « D'où vient ce chiffre ? », « tu l'as vérifié comment ? ». Une réponse vague est un signal.
- **Demander l'avis contraire.** « Qu'est-ce qui ne va pas dans ce que je propose ? » Il a tendance à aller dans votre sens si on ne le lui demande pas.
- **Faire écrire les décisions.** Ce qui n'est pas dans un fichier est oublié à la séance suivante.

## Ce que Claude fait bien, et moins bien

**Bien** : rédiger vite dans un style contraint ; appliquer une charte de quarante règles sans en oublier ; écrire et lancer des scripts de vérification ; tenir des documents longs à jour ; proposer des variantes ; fabriquer des illustrations et des vidéos à partir d'un gabarit ; expliquer une notion à plusieurs niveaux.

**Moins bien, et il faut le savoir** :

- **Il voit mal ses propres tournures obscures**, pour la même raison qu'un expert : il connaît la réponse. D'où la relecture profane.
- **Il peut affirmer un chiffre faux avec assurance.** Dans le M1, un total de contrôle repris d'un document à l'autre était faux de 41 270,30 €, alors que tous les soldes étaient justes. La parade : tout nombre se recalcule par script, et toute phrase qui décrit ce que l'écran affiche se vérifie en rejouant les écritures.
- **Il a tendance à aller dans votre sens.** Demandez-lui explicitement de contester ce que vous proposez, et méfiez-vous d'un accord trop rapide.
- **Sur une très longue conversation, il perd en précision** : les premiers échanges sortent de sa mémoire de travail. Il vaut mieux plusieurs séances courtes, chacune avec son objectif.
- **Il ne connaît pas votre application** tant qu'on ne lui donne pas accès aux fichiers, et il ne voit que ce qu'on lui donne.

## La mémoire : ce qui reste et ce qui se perd

Claude ne garde rien d'une conversation à l'autre, sauf trois choses :

1. **Le dossier `casoria-docs`**, connecté à la session dans l'application de bureau. C'est la mémoire officielle : chartes, déroulés, registres, outils.
2. **Les notes de projet de Claude**, qu'il écrit lui-même au fil du travail (décisions, pièges rencontrés, état d'avancement). Elles sont attachées au projet dans l'application de bureau. Elles sont utiles, mais **une règle qui n'existe que là n'est pas partageable** : tout ce qui doit valoir pour d'autres personnes remonte dans `methode/`.
3. **Ce que vous lui redonnez** en début de séance.

**Conséquence pratique** : une décision prise en conversation et non écrite sera oubliée. À la fin d'une séance qui a tranché quelque chose, demandez : « Écris cette décision dans le document qui convient. »

## Une séance type

**1. Ouvrir.** Une conversation dans l'application de bureau, avec le dossier `casoria-docs` connecté. Pour travailler sur le texte des chapitres, connecter aussi le dossier de l'application.

**2. Donner le cadre** en quelques lignes :

> On travaille sur le module « … », chapitre « … ». Objectif de la séance : … À la fin, je veux : … Lis d'abord `methode/charte-redaction.md` (l'essentiel), puis la fiche du chapitre dans le déroulé.

**3. Laisser Claude poser ses questions.** Il en pose quand une consigne est ambiguë. Une réponse courte et concrète suffit.

**4. Relire ce qu'il produit, sur pièce.** Un PDF ou une page, pas un résumé de ce qu'il a fait. Ses PDF de relecture portent une annexe de **points de vigilance** : ce sont les deux ou trois questions qui méritent votre décision. Le reste est vérifié.

**5. Corriger par consignes précises.** « Dans le deuxième paragraphe, “consolidé” n'est pas clair » vaut mieux que « c'est un peu lourd ». Une retouche que vous écrivez vous-même s'applique telle quelle.

**6. Clore.** Demander que les décisions soient écrites, que les fichiers soient enregistrés à leur place dans le dossier, et vérifier qu'ils y sont.

## Les consignes de travail en vigueur

Ces règles valent pour toutes les séances. On peut les lui rappeler en début de séance.

- **Avant / après / pourquoi.** Claude ne modifie pas le texte de l'apprenant sans montrer l'avant, l'après et la raison, et sans accord. « Vas-y » vaut accord pour toutes les propositions présentées.
- **Questions claires et concrètes**, une décision à la fois.
- **Pas de complaisance.** Il dit quand il n'est pas d'accord, et pourquoi.
- **Il signale quand la conversation devient trop chargée** pour rester fiable, et propose de repartir sur une séance neuve.
- **Il ne produit pas de version validée de sa propre initiative** (charte, § 22).
- **Il joint chaque fichier livré**, et dit où il l'a rangé. Un fichier modifié par un script peut arriver périmé dans la conversation : en cas de doute, demander la version du dossier.

## Ce qu'il faut vérifier soi-même

| Ce qu'il livre | Ce que vous vérifiez |
|---|---|
| Un chapitre | Qu'il se lit, et que ce qu'il enseigne est juste. Les points de vigilance de l'annexe. |
| Un chiffre, un total | Qu'il a été recalculé par script dans la séance, pas recopié. Demandez : « Tu l'as recompté comment ? » |
| Une phrase sur ce que l'écran affiche | Qu'elle correspond à l'écran à cet instant du parcours, en ouvrant l'application. |
| Un composant ou une illustration | Sur un vrai écran, à 720 px et sur téléphone. |
| Une vidéo | En la regardant, avec le son, jusqu'au bout. |
| Un fichier rangé | Qu'il est bien dans le dossier, à la bonne place, et que l'ancienne version a été archivée. |

## Ce qu'on ne délègue jamais

- **La décision.** Claude propose et argumente ; il ne tranche pas un choix pédagogique, éditorial ou commercial.
- **La relecture profane et la relecture de fond.** Il peut s'y préparer (lister les points délicats, proposer une première relecture), pas s'y substituer.
- **Les secrets.** Une clé d'API ne se colle pas dans la conversation et ne se range pas dans `casoria-docs`. Elle vit dans un fichier local hors du dossier partagé.
- **La suppression de fichiers.** Dans la configuration actuelle, Claude ne peut ni déplacer ni supprimer de fichiers sur votre ordinateur : il copie, vous supprimez. C'est voulu.
- **Ce qui engage Casoria envers l'extérieur** : un envoi, une publication, un achat, un contrat.

## Le coût

Chaque séance consomme des ressources, proportionnelles à la quantité de texte que Claude lit et écrit. Trois habitudes les réduisent sans rien perdre : lui indiquer quels documents lire au lieu de « tout le dossier » ; séparer les séances par objectif ; réserver le modèle le plus puissant au travail de fond (rédaction, méthode) et un modèle plus léger aux tâches mécaniques (tri de fichiers, conversions).

## Où trouver quoi

| Besoin | Document |
|---|---|
| Écrire un texte de chapitre | `methode/charte-redaction.md` |
| Concevoir un composant ou une illustration | `methode/composants-et-illustrations.md` |
| Faire une vidéo | `methode/charte-videos.md` |
| Les étapes de fabrication d'un module | `methode/process-de-fabrication.md` |
| Le fond d'un module (scénario, chiffres, lexique, fiches de chapitre) | `modules/<module>/deroule…` |
| Ce qu'un module a écarté | `modules/<module>/registre-des-ecarts.md` |
| Les arbitrages d'un module | `modules/<module>/journal-de-redaction.md` |
| Les scripts | `outils/` et son `LISEZ-MOI.md` |
