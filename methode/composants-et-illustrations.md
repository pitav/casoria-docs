# Composants et illustrations

**Statut.** Document vivant, valable pour tous les modules de Casoria. Il rassemble des règles posées pendant la fabrication du module 1 (septembre 2026) et qui n'étaient jusqu'ici écrites que dans les notes de travail de Claude. La charte de rédaction (`charte-redaction.md`, § 18) fixe ce que le *texte* dit des composants ; ce document fixe leur *conception*.

**Changements (20 octobre 2026).** Première version.

---

## L'essentiel

1. **Un composant doit faire faire ce que le texte ne peut pas faire à la place de l'apprenant.** Sinon, c'est une illustration, ou rien (règle 0).
2. **Une activité n'emploie que ce que l'apprenant a déjà vu**, dans le chapitre présent ou le précédent ; à défaut, du générique compréhensible sans rien savoir (règle 1).
3. **Trois couleurs, trois rôles** : amber pour l'activité, slate pour les documents, lime pour ce qui est acquis. Rien n'est dit par la couleur seule (règle 2).
4. **Un composant dispose d'environ 700 px de large**, pas de l'écran : on maquette à 720 px (règle 3).
5. **La réponse arrive à un seul endroit, juste sous l'activité**, avec un verdict écrit en toutes lettres quand il y a une question à réponse unique.
6. **On peut toujours tout reprendre**, et rien ne compte : pas de score, pas de chronomètre.
7. **Une illustration montre, elle n'explique pas** : peu de texte, pas de couleur, slate seul, accessible en contraste élevé.

---

## Composant ou illustration ?

| | Composant (activité) | Illustration |
|---|---|---|
| Ce qu'il demande | Un geste : trier, reconstituer, calculer, prendre position | Rien : on regarde |
| Ce qu'il fait | Faire pratiquer ce que le texte ne peut pas faire à la place de l'apprenant | Montrer une structure, une proportion, une relation |
| Couleur | amber, slate, lime | slate seul |
| Réponse | Oui, dans un panneau de verdict | Non |

Le mot « illustration » s'emploie pour l'image, jamais « composant » ni « widget », même quand elle est codée en `.vue` : la règle 0 repose sur la différence entre geste et absence de geste. (En accessibilité, un widget est interactif ; une illustration est une image, `role="img"`.)

## Règle 0 — un composant fait faire ce que le texte ne peut pas faire

> « Notre but est que les gens comprennent rapidement. Le côté interactif du composant est peut-être inutile, et ce d'autant plus que la réponse est écrite noir sur blanc juste après. » (consigne du décideur, 16 septembre 2026)

**Le test se pose avant d'écrire la fiche du composant.** Trier huit éléments, reconstituer une écriture, poser une soustraction : le texte ne peut pas le faire à la place de l'apprenant, et l'activité est la pratique elle-même. Annoncer un nombre ou une direction que le texte donne trois lignes plus bas : le texte le fait, et plus vite. Un composant de ce second genre est un détour, pas un apprentissage.

**Corollaire.** Quand une fiche a besoin d'une section entière pour prévenir de ce que son composant ne montre pas, c'est l'axe du composant qu'il faut changer.

**Contrôle.** Chercher l'objectif du chapitre dans le déroulé, et vérifier que le geste demandé y touche.

> **Attestation (M1).** Le composant de décomposition d'une mensualité (*Se financer*) a été écrit deux fois et retiré deux fois, puis remplacé par une illustration. À l'inverse, l'activité avant/après sur le stock (*Produire et stocker*) passe de justesse : sa sortie est une direction que le texte donne aussi, mais elle fait bouger un document, ce que la prose ne peut pas faire, et tout le chapitre est bâti sur la prise de position.

## Règle 1 — la matière ne sort pas du chapitre présent et du précédent

> « N'aborde que les notions déjà vues dans le chapitre précédent et présent. Si ça n'est pas possible, utilise des choses génériques compréhensibles par tout le monde sans connaissance. » (consigne du décideur)

Un élément qui suppose une notion non encore donnée ne mesure pas la compréhension : il mesure ce que l'apprenant devine.

1. **Avant de choisir la matière**, lister les notions des deux chapitres concernés, et la liste de ce qu'on écarte avec son motif. Les deux listes vont dans la fiche.
2. **Ce que le chapitre présent n'a pas encore dit, à l'endroit où l'activité se place, est aussi hors matière.**
3. **Une activité ne prend jamais au chapitre ce qu'il se réserve** : elle ne dévoile pas sa déclaration.
4. Quand la règle ne laisse rien, du générique, que l'on comprend sans rien savoir.
5. Quand elle ne laisse qu'un candidat, c'est une bonne nouvelle : elle a désigné la matière.

## Règle 2 — la palette

Trois familles de Tailwind, chacune avec un rôle, et la coupure passe entre l'activité et le document.

| Couleur | Rôle | Exemples |
|---|---|---|
| amber | La surface de l'activité : là où l'on agit | fond du panneau, boutons d'action, options |
| slate | Les documents : ce qu'on lit | zones de dépôt, lignes de compte, montants, totaux |
| lime | Ce qui est acquis | élément bien placé, panneau de fin |
| `text-error-500` | La phrase de retour d'un geste refusé, et elle seule | — |

**Aucune information portée par la couleur seule.** Une zone de dépôt visée se marque d'abord par son trait, qui passe du pointillé au plein. Un verdict s'écrit en toutes lettres.

La feuille `activite.css` (classe `.activite`) est le vocabulaire de référence. Elle n'est pas figée : on y ajoute plutôt qu'on ne la contourne. Elle évolue dans l'application plus vite que toute copie : on livre le bloc à ajouter, jamais la feuille entière.

## Règle 3 — la moitié droite de l'écran

> « La plupart du temps l'écran est divisé en deux verticalement. Le texte à gauche, le Bilan et le Compte de Résultat à droite. Il faut économiser de la place. » (consigne du décideur)

**La largeur utile est d'environ 700 px, et la hauteur compte autant.**

1. **Maquetter directement à 720 px.** Une maquette large ment sur ce qui tient.
2. **Schématiser plutôt qu'écrire** : remplacer un tableau par une géographie.
3. **Sortir des lignes ce qui se répète.**
4. **Un état se montre avant de se dire.**
5. **Une ligne de compte tient sur une seule ligne**, numéro et libellé : « 601 Achats de café vert ».
6. **L'ordre à l'écran** : panneau d'activité (la consigne), verdict, documents, bouton neutre au pied. Dans le M1, le patron est le composant `M1ActiviteSection`, avec ses créneaux `#activite` (la consigne) et `#info`.

## Comment une activité rend sa réponse

### Un seul endroit

> « La réponse arrive à deux endroits différents. Du coup on se demande qui est la bonne réponse. » (consigne du décideur, 15 septembre 2026)

1. **Un seul panneau de verdict, immédiatement sous le panneau d'activité.**
2. **Il porte, dans cet ordre** : le mot du verdict, la remarque adressée à la réponse donnée, puis ce qui s'est passé, avec ses chiffres.
3. **La seconde moitié est la même pour toutes les réponses.** C'est elle, la réponse à la question ; seule la remarque change.
4. **Il s'affiche à l'instant de la validation**, en même temps que l'animation du document, qui est donc courte (une demi-seconde).

### Trois verdicts, pas deux

**« Bonne réponse »** (lime), **« Mauvaise réponse »** (rouge), et **« Presque »** (amber). Une réponse peut être juste et hors sujet : un raisonnement exact appliqué au mauvais objet. La peindre en rouge dirait faux à quelque chose de vrai. **Avant de peindre une réponse en rouge, vérifier qu'elle est fausse et pas seulement hors sujet.**

**Un verdict n'est pas une note.** Le composant nomme la réponse, il ne compte rien : pas de score, pas de série, pas de chronomètre, et tout se reprend. C'est la frontière avec un quiz.

### Le verdict est réservé aux questions à réponse unique

- **Une question (une seule réponse vraie)** reçoit un verdict.
- **Un dépôt (trier, glisser, reconstituer) n'est pas une question.** L'apprenant corrige geste par geste, une pièce mal placée revient, avec une phrase en `text-error-500`. À la fin, un panneau de clôture lime, sans mot de verdict. Un gros panneau rouge à chaque geste faux rendrait l'activité punitive, alors qu'on veut qu'on se trompe sans frais.
- **Cas mixte** (plusieurs questions enchaînées) : une réponse fausse reçoit « Mauvaise réponse » ; une réponse juste n'en reçoit aucun, c'est l'avancée elle-même qui récompense.

### La forme des réponses dit la nature de la question

Trois boutons d'action disent *faites l'une de ces trois choses* ; trois boutons radio disent *une seule de ces trois est vraie*. **Une question qui demande une croyance veut des radios ; une question qui demande un geste veut des boutons.**

- Réponse unique parmi n : un groupe de radios (`role="radiogroup"`) nommé par la question. Les options restent à l'écran après le choix, figées, la réponse donnée marquée.
- Quand la réponse engage : deux temps, cocher puis valider. Entre les deux, l'apprenant relit le document.
- Quand la réponse est une tentative qu'on recommence : un seul clic suffit.
- Au clavier, les flèches parcourent le groupe et l'espace coche, sans rien déclencher : c'est le bouton de validation qui engage.

### Un résultat ne s'affiche pas tant qu'il est faux

Dans une activité de calcul, un résultat faux ne s'inscrit pas. Pour la même raison, **un total qui change se remplace (le chiffre chasse l'autre, environ 300 ms), il ne défile pas comme un compteur** : un compteur fait passer à l'écran des nombres faux.

### Le pied de l'activité

- **Le pied porte « Tout reprendre »**, au même endroit et sous le même nom dans tous les composants.
- **Une règle qui interdit de refaire une activité n'a rien à faire dans un bouton.** Elle vit dans l'événement : ne retenir que la première réponse.
- **Tout changement déclenché par un bouton doit être visible depuis ce bouton.**
- **Toute région de retour est rendue en permanence, avec sa hauteur réservée.** Un panneau qui apparaît et disparaît fait sauter les éléments sous le doigt.
- Sous `prefers-reduced-motion`, un rejeu qui n'est qu'une bascule d'état devient un clignotement : prévoir un changement lisible.

> **Attestation (M1).** Le bouton « Revoir » d'une activité « ne marchait pas ». Il marchait : la révélation bougeait trois éléments à 400 pixels du curseur, le panneau se démontait et se remontait, et rien ne changeait dans la zone où l'on venait de cliquer.

## Ce qu'un composant peut montrer en mouvement

**Un total ne bouge sous les yeux de l'apprenant que dans un composant, jamais dans les documents de la simulation.** Le texte et les documents sont sur le même écran, mais pas dans le même champ de vision : sur un téléphone, un défilement les sépare (charte, § 16). Un composant tient son propre cadre : la ligne qui s'inscrit et le total qu'elle déplace sont à deux centimètres l'un de l'autre, à toutes les largeurs.

**L'ancienne valeur reste affichée à côté de la nouvelle.** C'est gratuit dans un composant, et cela affranchit le texte de toute mise en page.

**Limite.** Ce qu'un empilement fait sortir du champ de vision doit être dit par une phrase. *(M1 : sous 480 px, le total des charges sort de l'écran au moment où celui des produits bouge ; c'est la phrase de clôture qui dit qu'il n'a pas bougé.)*

**Un comportement d'interface se déclare avant d'être écrit.** Avant qu'une légende s'appuie sur ce que fait un écran, ce comportement doit être décrit dans le déroulé. Dans le M1, trois légendes se sont appuyées sur des comportements qui n'étaient écrits nulle part (grand journal, panneau automatique, bloc manuel).

## La saisie des écritures (modules avec simulation)

Décisions prises pour le M1, à reprendre telles quelles sauf raison contraire :

- **Le texte et la saisie sont toujours sur le même écran**, à toutes les tailles : deux colonnes en large, empilées en étroit. On ne navigue jamais entre lire et saisir. Séparer la lecture et la saisie sur deux écrans coûte des clics et des allers-retours ; c'est ce que ce choix évite.
- **Le bloc d'écritures dans le texte n'est qu'une consigne.** La saisie se fait dans les documents (grand journal, Bilan, Compte de Résultat).
- **Saisie à la ligne, par popover, jamais par modale** (tiroir sur téléphone). Le popover ne demande que le montant ; le sens vient de la consigne. Pas de débit ni de crédit au Bilan.
- **Une saisie fausse est refusée**, signalée, non validable. L'historique de la ligne s'affiche donc en lecture seule : il n'y a rien à corriger.
- **Les totaux sont calculés, jamais saisis.** Ils changent par remplacement, avec l'écart affiché un instant. Sur le Bilan, slate quand Actif et Passif diffèrent, lime quand ils sont égaux, jamais rouge (le déséquilibre en cours d'année n'est pas une erreur).
- **Le panneau automatique se déclenche à la main, d'un clic, ne se rejoue pas**, et ses lignes s'inscrivent une à une, avec « Tout afficher ».
- **Toutes les lignes des documents sont visibles dès le début**, comme une grille de mots croisés. La ligne à saisir se signale par un cadre et un badge « À saisir », jamais à la place du montant.

## Illustrations

### Ce qu'une illustration fait

Elle montre une structure, une proportion, une relation, que le texte décrirait plus longuement. Sa légende, dans le chapitre, tire la leçon ; son texte de remplacement décrit ce qu'on voit. Le lecteur d'écran lit les deux à la suite : ils ne se répètent pas.

### Règles de dessin

- **Peu de texte dans une image.** Ce qui se répète s'écrit une fois ; une réponse tient en trois ou quatre mots ; la place va au dessin.
- **Pas de couleur.** Une illustration est en slate. La couleur appartient aux activités et au lexique.
- **Une absence qui est la leçon s'écrit à pleine encre.** Si ce que l'image doit apprendre est que rien ne bouge (« le compte en banque n'a pas changé »), cette absence ne se dessine pas en gris pâle.
- **Deux éléments qui portent le même nombre se fondent en un.** Deux cadres qui affichent le même montant côte à côte font chercher une différence qui n'existe pas.
- **Un intitulé de rangée écrit une seule fois se lit en slate-700**, pas en slate-400 : s'il n'est pas répété, il doit pouvoir se lire.
- **Une métaphore trop dessinée distrait de l'objectif.** Entre une version imagée et une version sobre, la sobre gagne si la première fait regarder le dessin au lieu de la notion.
- **À l'échelle quand on compare des montants** : deux barres qui représentent 12 € et 10 € sont proportionnées, et une seule échelle par illustration.

### Accessibilité

- **Aucun texte sous 0,6 rem ni plus clair que slate-500** sur fond blanc ou slate-50 (contraste 4,5:1). Sur slate-100, passer en slate-600.
- **Tout trait qui porte un sens est au moins en slate-500** (flèches, fourches, pointillés, cases éteintes). slate-300 et slate-200 sont réservés aux bords et aux éléments fantômes.
- **Pas d'opacité sur du texte.**
- **Mode contraste élevé** (`forced-colors`) : tout ce qui porte un sens par un fond (barres pleines, icônes, pointes de flèche) doit être repris en couleurs système. Les traits en bordure plutôt qu'en fond, parce que le contraste élevé garde les bordures.
- `role="img"` et `aria-label` sur l'illustration, contenu interne en `aria-hidden`. Éléments internes en `div` et `span`, jamais `p`.

### Format technique (M1)

Les illustrations sont des composants `.vue` sans interaction, dans `components/m1/illustration/`, nommées comme une scène (`StockLuDeuxFois`, `UnPrixDeuxMontants`, `LeFilmEtLaPhoto`), sans le mot « Illustration » dans le nom. Une classe `illustration` sur le conteneur, plus une classe propre. Styles dans `illustrations.css`, imbriqués sous `.illustration`. Largeur gérée par container queries (seuils en `em`), pas par media queries ; version large d'abord, puis étroite, testée à 720, 375, 360, 340 et 320 px. Les sources HTML d'origine sont gardées dans `modules/<module>/illustrations/sources/` : elles servent à produire les images des PDF et des vidéos.

## Conventions de code

Pour quiconque écrit un composant pour l'application.

- **KISS.** Le plus simple qui tienne. On ne retouche pas un élément validé pour le factoriser.
- **Pas de store** tant qu'il n'en faut pas. Les montants et textes d'un composant sont des `const` simples, regroupés dans un objet `scene` en tête du script ; ce qui ne règle que le dessin va dans un objet `dessin`. Un total se calcule, il ne se saisit pas à part.
- **Montants par `formatEuros(montant, decimales = 0)`**, fonction commune (`shared/utils/`) : insécables partout, virgule décimale, signe moins typographique. Jamais de formateur local.
- **Icônes par `<UIcon name="i-mdi-…" />`** (Nuxt UI), jamais de chemins SVG en dur.
- **Nommer un fichier comme ce qu'on voit**, pas comme un objet technique : un nom doit dire le chapitre et la scène.
- **On annonce chaque nouveau fichier livré**, avec son chapitre et son emplacement.

## Avant d'écrire un composant : la fiche

Chaque composant a une fiche dans `modules/<module>/composants/`, écrite et validée avant le code. Elle porte :

1. l'objectif du chapitre (cité du déroulé) et en quoi le geste y touche (règle 0) ;
2. les notions disponibles et celles qu'on écarte, avec leur motif (règle 1) ;
3. la consigne, les éléments, les réponses et le texte de chaque retour, rédigés comme du texte de chapitre ;
4. la maquette à 720 px et en étroit, dans chacun de ses états ;
5. ce qui reste à trancher.

Le modèle est dans `methode/gabarits/fiche-composant.md`.
