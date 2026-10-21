<script setup>
import { ref, computed } from 'vue'

/* Palette : le amber pour la surface de l'activité — la question et les trois
   réponses, qui sont ce que l'apprenant fait — et le slate pour le Compte de
   Résultat, qui est le document. Le panneau de verdict prend les trois teintes
   du module : lime pour la bonne réponse, amber pour « presque », error pour la
   mauvaise. Aucune information n'est portée par la couleur seule — le verdict
   est écrit en toutes lettres, la réponse choisie se marque d'abord par sa
   pastille, le document qui bouge par son trait. */

/* Les cinq nombres du composant, écrits une seule fois. Les deux totaux et les
   deux résultats s'en déduisent, la phrase de clôture comprise : un montant du
   scénario qui bougerait n'a qu'un endroit à changer. Les intitulés sont ceux
   du <FriseEncaissement /> et du module, pas les noms de classe de la grille. */
const colonnes = [
  {
    cle: 'charges',
    nom: 'Charges',
    total: 'Total charges',
    lignes: [
      { compte: '601', intitule: 'Achats de café vert', montant: 25000 },
      { compte: '615', intitule: 'Autres charges externes', montant: 8000 },
    ],
  },
  {
    cle: 'produits',
    nom: 'Produits',
    total: 'Total produits',
    lignes: [
      { compte: '701', intitule: 'Ventes aux professionnels', montant: 30000 },
      { compte: '707', intitule: 'Ventes au comptoir', montant: 9000 },
    ],
  },
]

/* La ligne qui arrive ne porte pas de numéro de compte. À la grille elle
   s'appelle « 7135 Variation des stocks », mais le terme appartient au
   sous-titre suivant et le numéro au panneau qui le clôt : le composant produit
   le mouvement, le texte le nomme. */
const stock = {
  nom: 'Le café invendu',
  mention: 'ce que l\'atelier a produit et pas encore vendu',
  montant: 15000,
}

/* Les trois réponses reprennent les mots du corps au caractère près — « faire
   baisser le résultat, le laisser où il est, ou le faire monter ». Aucune n'est
   refusée : les trois mènent au même écran, seule la phrase change. Et aucune
   des trois ne donne la raison, qui est la matière du sous-titre suivant. */
const reponses = [
  {
    cle: 'baisse',
    libelle: 'Il baisse',
    verdict: 'Mauvaise réponse',
    variante: 'panneau-final-faux',
    retour: "Regardez la colonne des charges : elle n'a pas bougé, et rien ne s'y est ajouté.",
  },
  {
    cle: 'stable',
    libelle: 'Il reste où il est',
    /* Ni juste ni faux, et c'est la raison d'être du troisième verdict : posée
       sur l'événement, cette réponse EST la bonne, la fiche du chapitre l'a
       reconnu. Ce qu'elle rectifie n'est pas le raisonnement mais l'objet de la
       question, qui porte sur les deux totaux affichés. La peindre en rouge
       dirait faux à un raisonnement vrai. */
    verdict: 'Presque',
    variante: 'panneau-final-presque',
    retour: "Latitude Café n'a ni encaissé ni dépensé un euro de plus, et c'est vrai. Mais la question porte sur les deux totaux affichés, et eux ne sont pas restés en place.",
  },
  {
    cle: 'monte',
    libelle: 'Il monte',
    /* Pas de félicitation au-delà du verdict : un constat, et le signalement
       que l'apprenant vient de répondre contre l'intuition commune. */
    verdict: 'Bonne réponse',
    variante: '',
    retour: "C'est bien ce que font les deux totaux, et c'est la réponse qui vient le moins spontanément des trois.",
  },
]

const choix = ref(null) // la case cochée, tant qu'elle n'est pas validée
const reponse = ref(null) // la position prise : l'état entier s'en déduit
const ligneVisible = ref(false)
const revele = ref(false)

/* La prise de position ne se rejoue pas — mais c'est une règle de mesure, pas
   une règle d'écran. « Tout reprendre » remet l'activité à zéro comme aux trois
   composants précédents ; seule la PREMIÈRE réponse part à l'événement, et les
   suivantes, données en connaissant le résultat, ne comptent pas. */
const premiereReponse = ref(null)

const somme = cle => colonnes.find(c => c.cle === cle).lignes.reduce((s, l) => s + l.montant, 0)

const totalCharges = somme('charges')
const totalProduits = somme('produits')
const totalProduitsApres = totalProduits + stock.montant
const resultat = totalProduits - totalCharges
const resultatApres = totalProduitsApres - totalCharges

const euros = (n, d = 2) => n.toLocaleString('fr-FR', { minimumFractionDigits: d }) + ' €'

const reponseChoisie = computed(() => reponses.find(r => r.cle === reponse.value))

/* Ce qui s'est passé, en une phrase et avec ses nombres. Elle suit le retour
   propre à la réponse donnée, dans le MÊME panneau : la réponse arrivait
   auparavant à deux endroits, et on ne savait plus laquelle était la bonne. */
const cloture = computed(() => `Les ${euros(stock.montant, 0)} se sont rangés du côté des produits, `
  + `et le total des charges n'a pas bougé d'un euro : `
  + `le résultat passe de ${euros(resultat, 0)} à ${euros(resultatApres, 0)}.`)
const totalDe = cle => cle === 'charges'
  ? totalCharges
  : revele.value ? totalProduitsApres : totalProduits

/* L'annonce doit dire qu'un nombre N'A PAS bougé : c'est la moitié de la leçon,
   et c'est le seul endroit du module dans ce cas. */
const annonce = computed(() => revele.value
  ? `${stock.nom}, ${euros(stock.montant, 0)}, s'inscrit du côté des produits. `
  + `Le total des produits passe de ${euros(totalProduits, 0)} à ${euros(totalProduitsApres, 0)}. `
  + `Le total des charges ne change pas, il reste à ${euros(totalCharges, 0)}. `
  + `Le résultat passe de ${euros(resultat, 0)} à ${euros(resultatApres, 0)}.`
  : '')

const sansMouvement = () => typeof window !== 'undefined'
  && window.matchMedia?.('(prefers-reduced-motion: reduce)').matches

/* La révélation, dans l'ordre : la ligne s'inscrit, puis les deux nombres
   changent, en un peu plus d'une demi-seconde — le verdict s'affiche au même
   instant, juste au-dessus, et les deux ne doivent pas se contredire longtemps.
   Sous prefers-reduced-motion, les deux
   états basculent d'un coup — rien n'est perdu, le composant porte l'avant et
   l'après à l'écrit.
   Les nombres ne défilent pas de l'ancienne valeur à la nouvelle : un compteur
   ferait passer sous les yeux une suite de nombres faux, ce que la règle de la
   <CalculetteTva /> interdit déjà à un résultat. */
function animer() {
  ligneVisible.value = true
  if (sansMouvement()) {
    revele.value = true
    return
  }
  setTimeout(() => { revele.value = true }, 450)
}

/* Deux temps, et c'est voulu : on coche, puis on valide. Une position qu'on
   prend d'un seul clic est trop facile à prendre par mégarde, et le temps entre
   les deux gestes est celui où l'apprenant relit les deux totaux. */
function valider() {
  if (!choix.value || reponse.value) return
  reponse.value = choix.value
  if (!premiereReponse.value) premiereReponse.value = choix.value
  animer()
}

function toutReprendre() {
  reponse.value = null
  choix.value = null
  ligneVisible.value = false
  revele.value = false
}
</script>

<template>
  <!-- Le composant vit dans la colonne de droite, à côté du texte : la largeur
       utile est d'environ 700 px, pas celle du conteneur. Il occupe la place du
       Compte de Résultat — il ne peut donc pas y renvoyer, il doit le porter. -->
  <M1ActiviteSection class="avant-apres-stock">
    <template #activite>
      Le café torréfié qui attend sur les étagères ne figure pas encore au Compte de Résultat.
    </template>
    <template #info>
      Rien n'est noté. Vous répondez, et la suite s'affiche.
    </template>

    <!-- la question et les trois réponses. Une seule réponse est possible, donc
         un groupe de boutons radio et non trois boutons d'action : les trois
         restent à l'écran après le choix, celui qui a été fait marqué d'une
         pastille, et l'apprenant voit ce qu'il n'a pas choisi. -->
    <div class="mt-3 bg-activite">
      <h3 class="titre-panneau color-activite">
        {{ reponse ? 'Votre réponse' : 'La question' }}
      </h3>

      <p
        id="aas-question"
        class="mt-3 text-[0.95rem] font-semibold text-amber-900"
      >
        Une fois ces {{ euros(stock.montant, 0) }} pris en compte, que devient le résultat&nbsp;?
      </p>

      <div
        role="radiogroup"
        aria-labelledby="aas-question"
        class="mt-3 flex flex-wrap gap-2"
      >
        <label
          v-for="r in reponses"
          :key="r.cle"
          class="option-activite"
        >
          <input
            v-model="choix"
            type="radio"
            name="avant-apres-stock"
            :value="r.cle"
            :disabled="!!reponse"
          >
          <span>{{ r.libelle }}</span>
        </label>
      </div>

      <div
        v-if="!reponse"
        class="mt-3"
      >
        <button
          type="button"
          class="btn-activite btn-activite-color justify-center"
          :disabled="!choix"
          @click="valider"
        >
          Valider ma réponse
        </button>
      </div>

    </div>

    <!-- LE VERDICT, et il est le seul endroit où la réponse arrive. Il se place
         juste sous le panneau d'activité, là où l'apprenant vient de cliquer :
         la réponse était auparavant à deux endroits — une phrase ici, une autre
         sous le document — et on ne savait plus laquelle était la bonne.
         Le mot porte l'information, la teinte ne fait que la doubler. -->
    <p
      v-if="reponse"
      role="status"
      aria-live="polite"
      class="panneau-final mt-3"
      :class="reponseChoisie.variante"
    >
      <span class="titre-panneau block">{{ reponseChoisie.verdict }}</span>
      {{ reponseChoisie.retour }} {{ cloture }}
    </p>

    <!-- le document. Deux colonnes, jamais quatre : l'avant et l'après sont deux
         instants du même document, pas deux objets. Il se marque pendant qu'il
         change, par son trait qui passe au plein. -->
    <div
      class="zone-resultat mt-4 transition"
      :class="revele ? 'zone-resultat-remplie' : 'zone-resultat-nue'"
    >
      <h3 class="titre-panneau color-neutral">
        Compte de Résultat
      </h3>
      <p class="mt-px text-[0.63rem] leading-snug text-slate-500">
        ce que l'activité a gagné ou consommé
      </p>

      <div class="mt-3 grid gap-3 sm:grid-cols-2">
        <div
          v-for="col in colonnes"
          :key="col.cle"
          class="flex flex-col"
        >
          <p class="mb-1.5 text-[0.56rem] font-bold uppercase tracking-[0.11em] text-slate-400">
            {{ col.nom }}
          </p>

          <div
            v-for="l in col.lignes"
            :key="l.compte"
            class="ligne-doc"
          >
            <span class="text-[0.72rem]! leading-tight text-slate-800">
              <b class="mr-1 font-bold text-slate-700">{{ l.compte }}</b>{{ l.intitule }}
            </span>
            <span class="text-[0.72rem]! font-semibold tabular-nums whitespace-nowrap">
              {{ euros(l.montant) }}
            </span>
          </div>

          <!-- la case qui s'allume. Elle ne porte pas de numéro de compte : le
               chapitre ne l'a pas encore donné, et les quatre autres en portent
               un — l'asymétrie est lisible et elle est juste. -->
          <Transition
            enter-active-class="transition duration-500 ease-out"
            enter-from-class="-translate-y-1 opacity-0"
            enter-to-class="translate-y-0 opacity-100"
            leave-active-class="transition duration-200 ease-in"
            leave-from-class="opacity-100"
            leave-to-class="-translate-y-1 opacity-0"
          >
            <div
              v-if="col.cle === 'produits' && ligneVisible"
              class="item-place mt-2"
            >
              <p class="flex items-baseline justify-between gap-2">
                <span class="text-[0.72rem]! leading-tight text-slate-800">{{ stock.nom }}</span>
                <span class="text-[0.72rem]! font-semibold tabular-nums whitespace-nowrap">{{ euros(stock.montant) }}</span>
              </p>
              <p class="mt-px text-[0.56rem]! leading-snug text-slate-500">
                {{ stock.mention }}
              </p>
            </div>
          </Transition>

          <!-- les deux totaux sont à la même hauteur, comme à la grille depuis
               le déroulé v26 : c'est ce qui rend l'écart lisible d'un regard. -->
          <p class="total-doc">
            <span class="text-[0.6rem] font-bold uppercase tracking-[0.1em] text-slate-600">
              {{ col.total }}
            </span>
            <span class="text-[0.85rem] font-bold tabular-nums whitespace-nowrap text-slate-800">
              <span
                v-if="col.cle === 'produits' && revele"
                class="valeur-avant"
              >{{ euros(totalProduits) }} →</span>
              {{ euros(totalDe(col.cle)) }}
            </span>
          </p>
        </div>
      </div>
    </div>

    <!-- le résultat vit SOUS le document et non dedans : la grille n'affiche
         aucune ligne de résultat avant le Chapitre 11. C'est la lecture que le
         composant fait du document, pas une ligne du document. Il est affiché
         dès le premier écran, parce qu'il est vrai à chaque instant. -->
    <div class="mt-3 flex items-center justify-between gap-3 border-t-[1.5px] border-slate-700 pt-2.5">
      <p class="text-[0.72rem] font-bold uppercase tracking-[0.06em] text-slate-700">
        Le résultat
        <span class="mt-0.5 block text-[0.68rem] font-normal normal-case tracking-normal tabular-nums text-slate-500">
          {{ euros(revele ? totalProduitsApres : totalProduits) }} − {{ euros(totalCharges) }}
        </span>
      </p>
      <p class="text-xl font-bold tabular-nums whitespace-nowrap text-slate-800">
        <span
          v-if="revele"
          class="valeur-avant text-[0.8rem]!"
        >{{ euros(resultat, 0) }} →</span>
        {{ euros(revele ? resultatApres : resultat, 0) }}
      </p>
    </div>

    <div
      v-if="reponse"
      class="mt-4"
    >
      <UButton
        type="button"
        size="sm"
        color="neutral"
        @click="toutReprendre"
      >
        Tout reprendre
      </UButton>
    </div>

    <p
      role="status"
      aria-live="polite"
      class="sr-only"
    >
      {{ annonce }}
    </p>
  </M1ActiviteSection>
</template>
