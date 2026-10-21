# Charte des vidéos

**Statut.** Document vivant, valable pour tous les modules. Il reprend la « Charte graphique des vidéos Casoria » (document Claude Docs du 16 octobre 2026) et les décisions prises jusqu'à la livraison des quatorze vidéos du module 1, le 19 octobre 2026. **C'est désormais ce fichier qui fait foi** ; le document Claude Docs n'est plus tenu à jour.

**Changements (20 octobre 2026).** Première version en Markdown. Convention de nommage et emplacements mis à jour après le rangement du dossier. Ajout des règles de travail (HTML avant MP4, plafond de durée, espacements).

---

## L'essentiel

1. **Le texte du chapitre se suffit à lui-même ; la vidéo est un plus**, placée en ouverture.
2. **Son cahier des charges est le bloc « Ce que vous avez appris »** du chapitre, ni plus ni moins. La vidéo fait *comprendre*, pas *savoir faire*.
3. **Générique** : une entreprise, un client, un fournisseur. Ni métier, ni personnage, ni fil rouge (exception : la vidéo d'introduction du module).
4. **Le vocabulaire est exactement celui du texte**, et les chiffres sont fictifs, ronds, présentés comme un exemple.
5. **Les chiffres changent au moment où la voix les dit.**
6. **Environ 3 minutes, au plus 3 min 15** (≈ 430 mots de voix).
7. **On livre d'abord le HTML** ; le MP4 et l'affiche seulement après validation.

---

## Fond

- **Cahier des charges** : le bloc « Ce que vous avez appris » du chapitre. Pour l'introduction d'un module, la page entière.
- **Aucun métier, aucun personnage.** Les rôles seulement : « une entreprise », « un client », « un fournisseur », « un associé », « une commande ». Pas l'entreprise du fil rouge (le M1 fait une exception pour son introduction). « Entreprise » est féminin : vérifier les accords.
- **Vocabulaire** : exactement celui du texte. Les lignes des documents portent le nom qu'elles ont dans l'application, sans numéro de compte. Au Compte de Résultat : « Ventes » et « Achats ».
- **Chiffres** : fictifs et ronds (10 000, 4 000), sans continuité d'une vidéo à l'autre. Un chiffre de cas se présente comme un exemple : « Par exemple, … ».
- **Ce qui est laissé de côté** se signale au décideur, pas à l'apprenant.

## Mise en page

L'image fait 1920 × 1080 px.

- **Fond** : dégradé de gauche à droite, `#459ceb` (primary-400) → `#c084fc` (purple-400), partout, en-tête compris.
- **En-tête permanent** : bande de 90 px transparente, bordure basse `1px solid #ffffff95`, avec le logo, le nom du module et le titre du chapitre en blanc. Il reste affiché de la fin de l'ouverture jusqu'à la fermeture.
- **Panneaux** : tout panneau posé sur le fond est blanc, jamais transparent, et **sans bordure** (panneaux, documents, tuiles, cartes, lignes). Seule une ligne encore vide garde un pointillé slate-300, qui disparaît quand elle se remplit.
- **Textes et flèches posés sur le fond** : en blanc.
- **Espacements** : rien ne colle au trait de l'en-tête (environ 50 px sous l'en-tête) ni à un bandeau (70 à 90 px dessous). Un opérateur (+, −, =) entre deux cartes se centre par calcul, pas à l'œil.
- **Tuiles d'acteurs** : le nom, et une précision éventuelle (« payée tout de suite »), à l'intérieur de la tuile, sous l'icône.
- **Facture** : un ticket de caisse, fond yellow-100, traits yellow-400, bords haut et bas dentelés (5 dents de 8 px). « FACTURE » en slate-500, destinataire et échéance en slate-600, montant en slate-900. Un élément posé dans une facture est rogné par sa découpe : le mettre à côté.
- **Frise** : rail primary-700, libellés « Jour 1 » / « Jour 30 » en primary-900, repère primary-600 cerclé de blanc.
- **Titres de repère** (« Jour 1 », « À retenir ») : primary-900, capitales espacées.
- **Cartes « À retenir »** : les notions clés en gras.
- **Ouverture et fermeture** : le logo seul, au centre, avec le jingle.

## Couleurs

La couleur est réservée à ce qu'on veut souligner ; dans les panneaux, tout le reste est en slate. Vérifier le contraste à chaque usage.

| Famille | Rôle | Valeurs |
|---|---|---|
| slate | Texte, documents, traits | slate-200 à slate-900 |
| primary (bleu Casoria) | Début du dégradé, icônes, frise, titres de repère | 50 `#f1f7fe` · 100 `#e2edfc` · 200 `#bfdbf8` · 300 `#86bdf3` · 400 `#459ceb` · 500 `#1d7fda` · 600 `#1063b9` · 700 `#0e4f97` · 800 `#10447c` · 900 `#133a67` · 950 `#0c2445` |
| purple (Tailwind `purple`, pas `violet`) | Le client ; fin du dégradé ; les mots « emploi » et « ressource », partout, en purple-600 | purple-400 `#c084fc`, purple-600 `#9333ea` |
| blanc | Panneaux ; textes et flèches sur le fond | `#fff` ; bordure d'en-tête `#ffffff95` |
| yellow | Ce qui attend (créance client, dette fournisseur) ; la facture | halo yellow-500 sur yellow-50 ; facture yellow-100, traits yellow-400 |
| red et green | Ce qui joue contre ou en faveur de l'entreprise | red-700, green-700 ; trait barré red-600 |
| lime | Rarement | — |

Pas d'amber dans les vidéos (il est réservé aux activités de l'application). **Icônes en couleur** : entreprise, banque, colis, associé en primary-600 ; client en purple-600.

## Typographie

**Une seule police, Poppins**, pour toute la vidéo. L'application utilise Roboto ; la vidéo ne la reprend pas.

| Usage | Police | Couleur |
|---|---|---|
| Titrailles, textes importants, chiffres | Poppins 400 à 800 | slate-900 |
| Question d'ouverture, refrain, titres de passage | Poppins 500, `text-wrap: balance` | blanc |
| Titres de repère | Poppins, capitales espacées | primary-900 |
| Nom du module (en-tête) | Poppins 700, capitales espacées | blanc |

**Un refrain à deux phrases s'écrit une phrase par ligne**, chacune à son instant.

## Documents comptables

- **Bilan, Compte de Résultat et grand journal** : slate sur fond blanc, jamais en couleur.
- **Pas de « € »** dans le Bilan ni dans le Compte de Résultat. Les factures et la carte « Compte en banque » le gardent.
- **Les documents vivent avec le scénario** : lignes et totaux bougent avec ce qui se passe.
- **Une ligne et le total de sa colonne changent toujours ensemble**, au même instant.
- **Emphase** : la ligne en attente (créance, dette) reçoit un halo yellow, retiré quand elle est réglée.
- **Grand journal** : en-têtes « Débit (emploi) » et « Crédit (ressource) », les mots entre parenthèses en Poppins 600, purple-600.
- **Un Bilan déséquilibré en cours d'année ne se commente pas** dans la vidéo.

## Icônes et logo

- **Icônes** : MDI ou Lucide uniquement (icones.js.org). Pictogrammes neutres, sans visage.
- **Logo** : `marque/logo-casoria.svg` (325 × 84). Symbole en dégradé `#e12afb` → `#3287ff`, mot « casoria » en `#1d293d`. À l'ouverture, le symbole tourne et grandit, puis le mot entre par la gauche ; même logo, fixe, à la fermeture.

## Animation et calage sur la voix

**Les chiffres changent au moment où la voix les dit** : c'est impératif.

- **Calage** : le début de chaque phrase se mesure sur les pauses de la voix enregistrée, puis se répartit au prorata des caractères à l'intérieur de la phrase.
- **Instants donnés par le décideur** : ils priment sur le calcul et se prennent tels quels (« 2.38 » = 2 min 38 s).
- **Changement de chiffre** : quasi immédiat (0,3 s ; 0,6 s pour un transfert, par exemple de la créance vers la banque).
- **Apparitions** : fondus et glissements courts (0,3 à 0,8 s), sans effet décoratif.
- **Jamais d'écran vide entre deux plans** : le panneau suivant entre dès que le précédent sort, quitte à apparaître vide et se remplir quand la voix en parle.
- **Ne rien retirer de la scène sans accord** : on ajuste, on ne supprime pas.

## Voix et son

Une seule voix off, le jingle au début et à la fin, pas de musique de fond.

- **Voix** : Gemini 3.8 Flash TTS, voix « Narrateur Casoria 1 » (`voice_dur676prxpls`), qui expire le 15 octobre 2027. **Quota : 100 requêtes par jour**, en fenêtre glissante ; une vidéo en consomme 15 à 30.
- **Script** : les dates et les sommes s'écrivent en lettres dans les segments de voix.
- **Enregistrement** : un bloc par segment de script (≈ 15 s), sans découpage phrase par phrase. Les fichiers de voix se gardent : ils permettent de corriger une phrase sans tout regénérer.
- **Jingle** : `marque/jingle-logo-casoria.mp3`, à 0 s et à la fin, volume 0,4 (il dure 5,1 s).

## Nommage et emplacement

**La convention vaut pour tous les modules** (décidée le 19 octobre 2026) :

```
videos/<module>/<slug-de-la-page>.html
                               .mp4
                               .jpg   (l'affiche)
```

- **`<module>`** : le début du titre du module, jusqu'à « sans être », en minuscules, sans accents, mots séparés par des tirets bas, sans numéro. M1 : `comprendre_la_comptabilite`. *(Règle déduite du M1, à confirmer au module 2.)*
- **`<slug-de-la-page>`** : le nom du fichier `.vue` de la page du chapitre dans l'application, sans numéro ni extension. L'introduction d'un module est `index`. M1 : `index`, `bilan-et-compte-de-resultat`, `naissance-de-l-entreprise`, `du-document-a-l-ecriture`, `facture-n-est-pas-encaisse`, `la-tva`, `produire-et-stocker`, `se-financer`, `investir`, `les-salaries`, `fin-de-l-exercice`, `cloture-de-l-exercice`, `decider-avec-trois-chiffres`, `synthese-et-feuille-de-route`.
- **Trois fichiers par chapitre, même nom** : la vidéo interactive (`.html`), la vidéo (`.mp4`), l'affiche (`.jpg`).
- **Pourquoi** : l'application retrouve la vidéo d'un chapitre par le slug de sa page, et l'arborescence `videos/<module>/` se recopie telle quelle sur le stockage en ligne (`videos.casoria.io/<module>/<slug>.mp4`).

**Dans `casoria-docs`**, le dossier `videos/<module>/` vit dans le dossier du module : `modules/m1-comprendre-la-comptabilite/videos/comprendre_la_comptabilite/<slug>.*`. Le travail en cours vit à côté :

- fabrication : `modules/<dossier-du-module>/videos-fabrication/<slug>/source/` (gabarit, script de construction) et `/voix/` (segments, mixage).

## Fabrication et livraison

**Ordre de travail.** Le décideur préfère juger sur pièce : texte, voix et vidéo s'enchaînent sans script PDF préalable, puis il retouche à des instants précis. **Tant qu'il n'a pas validé, on ne livre que le HTML** (image, voix, lecteur). Le MP4 et l'affiche (`.jpg`) se fabriquent après son accord, sauf s'il demande d'emblée une vidéo définitive.


**Chaîne technique** : un gabarit HTML animé par GSAP, polices et icônes intégrées au fichier, voix et jingle mixés en un seul fichier son. Les scripts sont dans `outils/` (`tts_gemini.py`, `voixoff_reprise.py`, `rendu_mp4.py`, `affiches_videos.py`). Partir du gabarit le plus proche de ce qu'on veut montrer ; un gabarit commun est à dériver des derniers (phase 4 du rangement).

**Vérification avant envoi** : lire la version livrée, avec son lecteur, en conditions réelles et avec le son, et relever les chiffres aux instants clés. Des captures image par image ne suffisent pas, et la version muette peut marcher quand la version livrée ne se lance pas.

**La vidéo commerciale est un autre objet** : public, promesse, durée (moins de 1 min 30) et durée de vie différents. Elle peut montrer l'application et le fil rouge. Une seule, pour l'accueil et la page du module.
