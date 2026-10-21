# casoria-docs

Le dossier de fabrication de Casoria. Rangé le 20 octobre 2026 (phase 1 : tri).

## Ce qui est où

| Dossier | Contenu | État |
|---|---|---|
| `methode/` | Ce qui vaut pour tous les modules. **Commencer par `travailler-avec-claude.md`.** Puis `charte-redaction.md` (écrire un chapitre), `composants-et-illustrations.md`, `charte-videos.md`, `process-de-fabrication.md` (les étapes), et `gabarits/` (fiche composant, fiche vidéo, entrée de registre). | Phase 2 faite le 20 oct. 2026, à valider. |
| `modules/m1-comprendre-la-comptabilite/` | Tout ce qui est propre au module 1. | Voir ci-dessous. |
| `outils/` | Scripts Python génériques (contrôles, PDF, voix off, rendu vidéo) + leur `LISEZ-MOI.md`. | Phase 4 : un seul répercuteur et un seul contrôle génériques, modèles dans `outils/modeles/`. |
| `marque/` | Logo (`logo-casoria.svg`) et jingle des vidéos (`jingle-logo-casoria.mp3`). | Stable. |
| `archives/` | Ce qui ne sert plus mais qu'on garde comme mémoire : copies des fichiers livrés à l'appli, maquettes, bancs d'essai, scripts ponctuels, essais de voix. `MANIFESTE-rangement-2026-10-20.csv` dit d'où vient chaque fichier. | Figé. |

## Module 1

| Fichier ou dossier | Rôle |
|---|---|
| `deroule-comprendre-la-comptabilite-v30.corps.html` + `.pdf` | La spécification du module. Phase 3 : réduite à la spécification seule. |
| `registre-des-ecarts.md` | Les écarts assumés au savoir comptable, et leur traitement. |
| `journal-de-redaction.md` | Les arbitrages. Phase 3 : réduit aux décisions durables (`decisions.md`). |
| `composants/` | Fiches de conception des composants interactifs (dernière version de chacune). |
| `illustrations/sources/` | Sources HTML des douze illustrations. |
| `specs/` | Plans techniques (ordre des écritures). |
| `videos/comprendre_la_comptabilite/` | Les 14 vidéos définitives, nommées par le slug de la page : `<slug>.html`, `.mp4`, `.jpg` (convention dans `methode/charte-videos.md`). |
| `videos-fabrication/<slug>/` | De quoi corriger une vidéo : `source/` (gabarit, build) et `voix/` (voix off phrase par phrase). |

## Règles

- **Le texte des chapitres a pour source de vérité les pages `.vue` de l'application.** Il n'y a plus de `.corps.html` de chapitre.
- **Aucun secret dans ce dossier.** La clé d'API Gemini vit hors du dossier partagé.
- **Versions** (pas de git) : un document vivant n'a pas de numéro dans son nom ; il porte en tête un court bloc « Changements » daté ; avant une refonte, une copie datée va dans `archives/`.
- Méthode en Markdown ; les PDF de relecture se génèrent par script.
