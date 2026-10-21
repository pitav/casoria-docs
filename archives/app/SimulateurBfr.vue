<script setup>
import { ref, computed, watch } from 'vue'

/* <SimulateurBfr /> — Chapitre 12, juste après la déclaration sur les 69 000 €.
   Les trois lignes du besoin en fonds de roulement deviennent trois curseurs.
   L'apprenant les fait bouger et regarde ce que devient le compte en banque,
   une fois la machine achetée et l'État payé.

   Ce que le texte ne peut pas faire à sa place (règle 0) : chercher DE COMBIEN
   il faudrait bouger chaque ligne. Le paragraphe suivant nomme les trois
   leviers ; aucune phrase du chapitre ne donne un montant.

   Palette : amber pour les curseurs, qui sont ce que l'apprenant fait ; slate
   pour le compte en banque, qui est le document ; lime quand la machine passe.
   Aucune information n'est portée par la couleur seule — l'état est écrit en
   toutes lettres, avec son montant. */

/* Les trois lignes, avec les intitulés d'une ligne du module et les mots du
   chapitre pour la mention. Chaque curseur va de zéro au double de sa valeur
   de départ : une seule règle pour les trois, et le point de départ tombe
   toujours au milieu, où un repère le marque. */
const lignes = [
  { cle: 'stock', compte: '355', intitule: 'Stock de café torréfié', signe: 1,
    mention: 'du café acheté, payé et torréfié, pas encore vendu', depart: 15000 },
  { cle: 'creances', compte: '411', intitule: 'Créances clients', signe: 1,
    mention: 'des ventes livrées et facturées, pas encore payées', depart: 63000 },
  /* Le seul curseur qui joue à l'envers : le monter fait BAISSER le besoin.
     C'est la découverte la moins évidente des trois, et le signe « − » de sa
     gouttière la prépare sans la dire. */
  { cle: 'dettes', compte: '401', intitule: 'Dettes fournisseurs', signe: -1,
    mention: 'des marchandises reçues, pas encore réglées', depart: 9000 },
]
const PAS = 1000

/* Les trois nombres fixes, ceux du chapitre. 9 200 € = 4 400 € de TVA à
   décaisser + 4 800 € d'impôt sur les sociétés, les deux dettes envers l'État
   que le premier sous-titre met de côté. */
const TRESORERIE = 17310
const MACHINE = 43200
const ETAT = 9200

const depart = () => Object.fromEntries(lignes.map(l => [l.cle, l.depart]))
const valeurs = ref(depart())

const bfrDe = v => lignes.reduce((s, l) => s + l.signe * v[l.cle], 0)
const BFR_DEPART = bfrDe(depart()) // 69 000 €

const bfr = computed(() => bfrDe(valeurs.value))
/* Ce que le besoin rend au compte en banque quand il baisse — ou lui prend
   quand il monte. C'est toute la mécanique du composant, en une soustraction. */
const libere = computed(() => BFR_DEPART - bfr.value)
const reste = computed(() => TRESORERIE + libere.value - MACHINE - ETAT) // − 35 090 € au départ
const passe = computed(() => reste.value >= 0)
const bouge = computed(() => lignes.some(l => valeurs.value[l.cle] !== l.depart))

/* Sommes entières : le chapitre n'écrit aucun centime. Le signe moins est le
   vrai (U+2212), suivi d'une insécable, comme dans le corps. */
const euros = n => (n < 0 ? '− ' : '')
  + Math.abs(n).toLocaleString('fr-FR', { maximumFractionDigits: 0 }) + ' €'
const signe = n => (n < 0 ? '− ' : '+ ')
  + Math.abs(n).toLocaleString('fr-FR', { maximumFractionDigits: 0 }) + ' €'

/* Le compte en banque, posé. La deuxième ligne change de nom selon le sens :
   un besoin qui monte prend de l'argent au compte, il ne lui en rend pas. */
const compte = computed(() => [
  { cle: 'tresorerie', libelle: 'Trésorerie', numero: '512', mention: 'au 31 décembre', montant: euros(TRESORERIE) },
  { cle: 'bfr', numero: '',
    libelle: libere.value < 0 ? 'Hausse du besoin en fonds de roulement' : 'Baisse du besoin en fonds de roulement',
    mention: libere.value < 0 ? 'ce que les trois lignes prennent au compte' : 'ce que les trois lignes rendent au compte',
    montant: signe(libere.value), vivant: true },
  { cle: 'machine', numero: '', libelle: 'La machine à torréfier', mention: 'prix TTC', montant: signe(-MACHINE) },
  { cle: 'etat', numero: '', libelle: 'Dû à l\'État', mention: 'TVA et impôt sur les sociétés', montant: signe(-ETAT) },
])

/* L'état, en un seul endroit, sous les curseurs. Ce n'est pas un verdict : il
   n'y a pas une réponse, il y en a beaucoup, et l'état est vrai à chaque
   position. La seconde phrase du cas favorable est la même pour tous les
   réglages : c'est elle, la réponse à la question. */
const etat = computed(() => passe.value
  ? {
      mot: 'La machine passe',
      classe: '',
      texte: `${reste.value > 0 ? `Il reste ${euros(reste.value)}` : 'Il ne reste rien'} une fois l'État payé. `
        + `Le besoin en fonds de roulement est descendu de ${euros(BFR_DEPART)} à ${euros(bfr.value)}, `
        + `et ces ${euros(libere.value)} sont revenus sur le compte en banque.`,
    }
  : {
      mot: `Il manque ${euros(-reste.value)}`,
      classe: 'panneau-final-attente',
      texte: 'Avec ce réglage, le compte en banque ne suffit pas à payer à la fois la machine et l\'État.',
    })

/* Au lecteur d'écran, chaque cran du curseur dit sa valeur ET l'état : c'est
   ce que l'œil voit d'un seul regard. La région annoncée, elle, ne parle que
   quand l'état bascule — sinon elle bavarderait à chaque cran. */
const texteValeur = l => `${euros(valeurs.value[l.cle])}. `
  + (passe.value ? 'La machine passe.' : `Il manque ${euros(-reste.value)}.`)

const annonce = ref('')
watch(passe, p => {
  annonce.value = p
    ? `La machine passe. Besoin en fonds de roulement ${euros(bfr.value)}.`
    : `La machine ne passe plus. Il manque ${euros(-reste.value)}.`
})

/* Mesure : le PREMIER réglage qui fait passer la machine part à l'événement,
   avec les trois valeurs. « Tout reprendre » remet l'écran à zéro, pas la
   mesure. Rien d'autre n'est compté. */
const emit = defineEmits(['premiere-reussite'])
let premiere = false
watch(passe, p => {
  if (p && !premiere) {
    premiere = true
    emit('premiere-reussite', { ...valeurs.value, bfr: bfr.value })
  }
})

function toutReprendre() {
  valeurs.value = depart()
}

const idCurseur = l => `sbfr-${l.cle}`
</script>

<template>
  <!-- Le composant vit dans la moitié droite de l'écran, à la place du Bilan :
       largeur utile d'environ 700 px. Il n'a pas besoin du Bilan entier, trois
       de ses lignes et le compte en banque suffisent. -->
  <M1ActiviteSection class="simulateur-bfr">
    <template #activite>
      Faites bouger les trois lignes du besoin en fonds de roulement. Le compte en banque suit.
    </template>
    <template #info>
      Rien n'est noté. Plusieurs réglages conviennent.
    </template>

    <!-- la question et les trois curseurs. Ils sont posés comme le calcul du
         chapitre, un signe dans la gouttière, le total au pied. -->
    <div class="mt-3 bg-activite">
      <h3 class="titre-panneau color-activite">
        La question
      </h3>
      <p
        id="sbfr-question"
        class="mt-3 text-[0.95rem] font-semibold text-amber-900"
      >
        La machine coûte {{ euros(MACHINE) }}. Jusqu'où faudrait-il faire bouger ces trois lignes pour
        la payer sans toucher à l'argent dû à l'État&nbsp;?
      </p>

      <div
        role="group"
        aria-labelledby="sbfr-question"
        class="mt-3 space-y-3"
      >
        <div
          v-for="(l, i) in lignes"
          :key="l.cle"
          class="rang-operation"
        >
          <span
            class="signe-operation pt-0!"
            aria-hidden="true"
          >{{ i === 0 ? '' : l.signe > 0 ? '+' : '−' }}</span>

          <div>
            <div class="flex items-baseline justify-between gap-2">
              <label
                :for="idCurseur(l)"
                class="text-[0.78rem] leading-tight text-slate-800"
              >
                <b class="mr-1 font-bold text-slate-700">{{ l.compte }}</b>{{ l.intitule }}
              </label>
              <span class="somme text-[0.85rem] text-slate-800">
                <span
                  v-if="valeurs[l.cle] !== l.depart"
                  class="valeur-avant"
                >{{ euros(l.depart) }} →</span>{{ euros(valeurs[l.cle]) }}
              </span>
            </div>
            <p class="mt-px text-[0.63rem] leading-snug text-amber-800">
              {{ l.mention }}
            </p>

            <div class="mt-1 flex items-center gap-2">
              <span
                class="w-10 shrink-0 text-[0.6rem] tabular-nums text-slate-500"
                aria-hidden="true"
              >0&nbsp;€</span>
              <div class="relative flex-1">
                <input
                  :id="idCurseur(l)"
                  v-model.number="valeurs[l.cle]"
                  type="range"
                  class="curseur-activite"
                  min="0"
                  :max="l.depart * 2"
                  :step="PAS"
                  :aria-valuetext="texteValeur(l)"
                >
                <!-- le point de départ : toujours au milieu, puisque chaque
                     curseur va jusqu'au double -->
                <span
                  class="repere-depart"
                  aria-hidden="true"
                />
              </div>
              <span
                class="w-14 shrink-0 text-right text-[0.6rem] tabular-nums text-slate-500"
                aria-hidden="true"
              >{{ euros(l.depart * 2) }}</span>
            </div>
          </div>
        </div>
      </div>

      <div class="rang-operation mt-3">
        <span
          class="signe-operation pt-1.5!"
          aria-hidden="true"
        >=</span>
        <p class="sous-total mt-0!">
          <!-- le sigle en étroit : le nom entier y prendrait trois lignes, et le
               chapitre vient de donner les deux -->
          <span class="sous-total-libelle">
            <span class="hidden sm:inline">Besoin en fonds de roulement</span>
            <abbr
              class="no-underline sm:hidden"
              title="Besoin en fonds de roulement"
            >BFR</abbr>
          </span>
          <span class="somme text-base text-slate-900">
            <span
              v-if="bfr !== BFR_DEPART"
              class="valeur-avant"
            >{{ euros(BFR_DEPART) }} →</span>{{ euros(bfr) }}
          </span>
        </p>
      </div>
    </div>

    <!-- L'ÉTAT, juste sous les curseurs : le seul endroit où la réponse arrive.
         Toujours rendu, hauteur réservée, il change de mot et de teinte mais ne
         se démonte jamais : rien ne saute sous le curseur. -->
    <div
      class="mt-3 min-h-[8.75rem] sm:min-h-[6.5rem]"
    >
      <p
        class="panneau-final mt-0!"
        :class="etat.classe"
      >
        <span class="titre-panneau">{{ etat.mot }}</span>
        {{ etat.texte }}
      </p>
    </div>

    <!-- le document : le compte en banque, posé comme une soustraction. Il se
         marque par son trait dès qu'une ligne a bougé. -->
    <div
      class="zone-resultat mt-3 transition"
      :class="bouge ? 'zone-resultat-remplie' : 'zone-resultat-nue'"
    >
      <h3 class="titre-panneau color-neutral">
        Le compte en banque
      </h3>
      <p class="mt-px text-[0.63rem] leading-snug text-slate-500">
        si Latitude Café achète la machine
      </p>

      <div class="mt-3 flex flex-col">
        <div
          v-for="c in compte"
          :key="c.cle"
          class="ligne-doc"
        >
          <span class="text-[0.72rem] leading-tight text-slate-800">
            <b
              v-if="c.numero"
              class="mr-1 font-bold text-slate-700"
            >{{ c.numero }}</b>{{ c.libelle }}<span class="text-[0.6rem] text-slate-500"> · {{ c.mention }}</span>
          </span>
          <span
            class="somme text-[0.72rem]"
            :class="c.vivant && libere !== 0 ? 'text-slate-900' : 'text-slate-700'"
          >{{ c.montant }}</span>
        </div>

        <p class="total-doc">
          <span class="text-[0.6rem] font-bold uppercase tracking-[0.1em] text-slate-600">
            Ce qui reste
          </span>
          <span class="somme text-[0.95rem] font-bold text-slate-900">
            {{ euros(reste) }}
          </span>
        </p>
      </div>
    </div>

    <!-- toujours à sa place, invisible tant que rien n'a bougé -->
    <div
      class="mt-3"
      :class="{ invisible: !bouge }"
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
