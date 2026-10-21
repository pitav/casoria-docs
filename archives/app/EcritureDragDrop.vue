<script setup>
import { ref, computed } from 'vue'

/* Palette : le amber pour la surface de l'activité — « À placer », qui est ce
   que l'apprenant manipule —, le slate pour le relevé et pour tout le grand
   journal, et le lime pour ce qui est acquis, c'est-à-dire une ligne posée et
   la phrase de clôture. Aucune autre couleur, et la couleur ne porte jamais
   seule une information : la zone visée se marque d'abord par son trait, qui
   passe du pointillé au plein. */

/* Les deux opérations du 5 janvier. Aucune notion hors des Chapitres 2 et 3 :
   l'apprenant a passé ces deux écritures de sa main au chapitre précédent.
   Le libellé au journal est porté par l'opération, pas répété sur ses lignes. */
const operations = [
  { cle: 'capital', titre: 'Apport en capital', releve: 'Virement reçu — les associés', montant: 30000 },
  { cle: 'courant', titre: 'Apport en compte courant', releve: 'Virement reçu — T. Vasseur', montant: 20000 },
]

const zones = [
  { cle: 'debit', nom: 'Débit', question: 'où va la valeur' },
  { cle: 'credit', nom: 'Crédit', question: "d'où elle vient" },
]

const lignes = [
  { id: 'treso-capital', op: 'capital', compte: '512', intitule: 'Trésorerie', montant: 30000, zone: 'debit' },
  { id: 'capital-social', op: 'capital', compte: '101', intitule: 'Capital social', montant: 30000, zone: 'credit' },
  { id: 'treso-courant', op: 'courant', compte: '512', intitule: 'Trésorerie', montant: 20000, zone: 'debit' },
  { id: 'compte-courant', op: 'courant', compte: '455', intitule: "Compte courant d'associé", montant: 20000, zone: 'credit' },
]

const placements = ref({}) // id de la ligne -> zone où elle est posée
const tenue = ref(null) // id de la ligne saisie, à la souris comme au doigt
const visee = ref(null)
const message = ref('')

const euros = n => n.toLocaleString('fr-FR', { minimumFractionDigits: 2 })

const nbPosees = computed(() => Object.keys(placements.value).length)
const termine = computed(() => nbPosees.value === lignes.length)
const ligneTenue = computed(() => lignes.find(l => l.id === tenue.value) || null)

/* « À placer » ne porte que les lignes de l'opération en cours : l'opération est
   l'unité de l'activité, puisque son sujet est « une opération, deux lignes ». */
const opCourante = computed(() =>
  operations.find(o => lignes.some(l => l.op === o.cle && !placements.value[l.id])) || null)
const enAttente = computed(() =>
  lignes.filter(l => l.op === opCourante.value?.cle && !placements.value[l.id]))

const operationsOuvertes = computed(() => {
  const rang = opCourante.value ? operations.indexOf(opCourante.value) : operations.length - 1
  return operations.slice(0, rang + 1)
})

const posee = (op, zone) =>
  lignes.find(l => l.op === op && placements.value[l.id] === zone) || null

const total = zone => lignes
  .filter(l => placements.value[l.id] === zone)
  .reduce((s, l) => s + l.montant, 0)

function basculer(id) {
  tenue.value = tenue.value === id ? null : id
  message.value = ''
}

function tenir(id) {
  tenue.value = id
  message.value = ''
}

/* Reprendre une ligne posée est toujours possible, y compris après la fin. */
function reprendre(id) {
  placements.value = Object.fromEntries(
    Object.entries(placements.value).filter(([cle]) => cle !== id),
  )
  tenue.value = id
  message.value = ''
}

function deposer(zone) {
  visee.value = null
  const ligne = ligneTenue.value
  if (!ligne) return

  if (ligne.zone === zone) {
    placements.value[ligne.id] = zone
    message.value = ''
  } else {
    message.value = phraseDeRetour(ligne.zone)
  }
  tenue.value = null
}

function toutReprendre() {
  placements.value = {}
  tenue.value = null
  message.value = ''
}

/* La réponse porte sur la question à laquelle la zone répond, jamais sur le
   compte déposé : c'est ce qui empêche l'apprenant d'en tirer qu'un compte
   appartient à une colonne. */
function phraseDeRetour(attendue) {
  return attendue === 'debit'
    ? "Cette ligne ne dit pas d'où vient la valeur. Elle dit où elle va."
    : "Cette ligne ne dit pas où va la valeur. Elle dit d'où elle vient."
}
</script>

<template>
  <M1ActiviteSection class="ecritures-drag-drop">
    <template #activite>
      Vous avez déjà passé ces écritures. Remettez chaque ligne dans sa colonne
    </template>
    <template #info>
      Rien n'est chronométré ou noté. Un élément mal placé reste à sa place.
    </template>

    <!-- Le retour d'un dépôt faux, au-dessus de « À placer », d'où la ligne
         vient et où elle retourne. Hauteur réservée : sans cela tout le
         composant saute d'une ligne à chaque erreur. -->
    <p
      role="status"
      aria-live="polite"
      class="min-h-[1.25rem] text-sm font-medium text-error-500"
    >
      {{ message }}
    </p>

    <!-- première ligne : le relevé de compte et les lignes à placer -->
    <div class="mt-3 grid gap-3 sm:grid-cols-2">
      <div class="clip-path-releve">
        <h3 class="titre-panneau titre-spacing mb-2!">
          Relevé de compte
        </h3>
        <div
          v-for="op in operations"
          :key="op.cle"
          class="flex justify-between gap-2 border-b border-slate-200 px-1.5 py-1.5 text-xs"
          :class="op.cle === opCourante?.cle && !termine ? 'border-l-[3px] border-l-slate-500 bg-white pl-0.5' : ''"
        >
          <span>
            {{ op.releve }}
            <span class="block text-[0.65rem] text-slate-700">5 janvier</span>
          </span>
          <span class="font-semibold tabular-nums whitespace-nowrap">+ {{ euros(op.montant) }}</span>
        </div>
        <p class="mt-2 flex justify-between border-t border-slate-300 pt-1.5 text-[0.7rem] text-slate-800">
          <span>Solde au 5 janvier</span><b class="tabular-nums">{{ euros(50000) }}</b>
        </p>
      </div>

      <div
        v-if="!termine"
        class="backdrop-blur bg-activite"
      >
        <div class="flex justify-between items-center mb-4">
          <h3 class="titre-panneau titre-spacing color-activite">
            À placer
          </h3>
          <div class="places">
            {{ nbPosees }} placés sur {{ lignes.length }}
          </div>
        </div>
        <div class="space-y-2.5">
          <button
            v-for="ligne in enAttente"
            :key="ligne.id"
            type="button"
            draggable="true"
            class="btn-drag w-full"
            :class="tenue === ligne.id
              ? 'btn-drag-selected'
              : 'btn-drag-color'"
            :aria-pressed="tenue === ligne.id"
            @dragstart="tenir(ligne.id)"
            @dragend="tenue = null"
            @click="basculer(ligne.id)"
          >
            <span><span class="mr-1.5 font-bold">{{ ligne.compte }}</span>{{ ligne.intitule }}</span>
            <span class="font-semibold tabular-nums whitespace-nowrap ml-1.5">{{ euros(ligne.montant) }}</span>
          </button>
        </div>
      </div>

      <p
        v-else
        class="panneau-final"
      >
        Deux virements, quatre lignes, et les deux colonnes portent le même total.
      </p>
    </div>

    <!-- le grand journal, schématisé en deux zones -->
    <p class="mt-5 mb-1! text-base font-bold text-slate-700 text-center">
      Le grand journal
    </p>
    <div class="grid gap-3 sm:grid-cols-2">
      <div
        v-for="zone in zones"
        :key="zone.cle"
        role="group"
        :aria-label="`${zone.nom} — ${zone.question}`"
        class="flex min-h-[12rem] flex-col rounded-xl zone-depot transition"
        :class="visee === zone.cle
          ? 'zone-depot-hover'
          : 'zone-depot-nue'"
        @dragover.prevent="visee = zone.cle"
        @dragleave.self="visee = null"
        @drop.prevent="deposer(zone.cle)"
        @click="ligneTenue && deposer(zone.cle)"
      >
        <p class="mb-0! titre-panneau color-neutral">
          {{ zone.nom }}
        </p>
        <p class="mb-2 mt-px text-sm! font-medium text-slate-600">
          {{ zone.question }}
        </p>

        <template
          v-for="op in operationsOuvertes"
          :key="op.cle"
        >
          <div
            v-if="posee(op.cle, zone.cle) || (visee === zone.cle && ligneTenue?.op === op.cle)"
            class="mb-1.5 mt-1.5 text-xs! font-bold uppercase tracking-[0.11em] text-slate-500 first:mt-0"
          >
            {{ op.titre }}
          </div>

          <div
            v-if="posee(op.cle, zone.cle)"
            class="flex items-baseline justify-between gap-2 item-place mb-3"
          >
            <button
              type="button"
              class="text-left hover:underline hover:underline-offset-2"
              :aria-label="`Reprendre la ligne ${posee(op.cle, zone.cle).intitule}`"
              @click.stop="reprendre(posee(op.cle, zone.cle).id)"
            >
              <span class="mr-1.5 font-bold text-slate-700">{{ posee(op.cle, zone.cle).compte }}</span>{{ posee(op.cle, zone.cle).intitule }}
            </button>
            <span class="font-semibold tabular-nums whitespace-nowrap">{{ euros(posee(op.cle, zone.cle).montant) }}</span>
          </div>

          <!-- l'emplacement que la ligne tenue occuperait, en creux, dans la zone visée -->
          <div
            v-else-if="visee === zone.cle && ligneTenue?.op === op.cle"
            class="flex items-baseline justify-between gap-2 border-l-[3px] border-dashed border-slate-400 px-2 py-1.5 text-xs italic text-slate-500"
          >
            <span><span class="mr-1.5 font-bold">{{ ligneTenue.compte }}</span>{{ ligneTenue.intitule }}</span>
            <span class="font-semibold tabular-nums whitespace-nowrap">{{ euros(ligneTenue.montant) }}</span>
          </div>
        </template>

        <p class="mt-auto flex items-baseline justify-between border-t-[1.5px] border-slate-800 pt-2">
          <span class="text-[0.55rem] font-bold uppercase tracking-[0.12em] text-slate-600">Total</span>
          <b class="text-sm tabular-nums">{{ euros(total(zone.cle)) }}</b>
        </p>
      </div>
    </div>

    <div
      v-if="nbPosees"
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
  </M1ActiviteSection>
</template>
