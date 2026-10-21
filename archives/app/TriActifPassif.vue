<script setup>
import { ref, computed } from 'vue'

/* Les quatre zones, dans l'ordre des deux documents. */
const documents = [
  { cle: 'bilan', titre: 'Le Bilan', question: "Où est l'argent, et d'où vient-il ?" },
  { cle: 'resultat', titre: 'Le Compte de Résultat', question: "Ce que l'activité a consommé, et qu'a-t-elle gagné ?" },
]

const zones = [
  { cle: 'actif', titre: 'Actif', doc: 'bilan' },
  { cle: 'passif', titre: 'Passif', doc: 'bilan' },
  { cle: 'charges', titre: 'Charges', doc: 'resultat' },
  { cle: 'produits', titre: 'Produits', doc: 'resultat' },
]

/* Les huit éléments. Aucun ne demande une notion postérieure au Chapitre 1. */
const elements = [
  { id: 'banque', libelle: "L'argent sur le compte en banque", zone: 'actif' },
  { id: 'materiel', libelle: "Le matériel de l'atelier", zone: 'actif' },
  { id: 'apport', libelle: "L'argent que les fondateurs ont mis dans l'entreprise", zone: 'passif' },
  { id: 'pret', libelle: 'Le prêt accordé par la banque', zone: 'passif' },
  { id: 'electricite', libelle: "L'électricité de l'atelier", zone: 'charges' },
  { id: 'salaires', libelle: "Les salaires de l'équipe", zone: 'charges' },
  { id: 'ventesPro', libelle: 'Le café vendu aux restaurants', zone: 'produits' },
  { id: 'ventesComptoir', libelle: "Le café vendu au comptoir de l'atelier", zone: 'produits' },
]

const placements = ref({}) // id de l'élément -> zone où il est posé
const selection = ref(null) // id de l'élément saisi, à la souris comme au doigt
const survol = ref(null)
const message = ref('')

const enAttente = computed(() => elements.filter(e => !placements.value[e.id]))
const nbPlaces = computed(() => Object.keys(placements.value).length)
const termine = computed(() => nbPlaces.value === elements.length)

const zonesDe = cle => zones.filter(z => z.doc === cle)
const contenuDe = cle => elements.filter(e => placements.value[e.id] === cle)
const documentDe = cle => zones.find(z => z.cle === cle).doc

function basculerSelection(id) {
  selection.value = selection.value === id ? null : id
  message.value = ''
}

function commencerGlisser(id) {
  selection.value = id
  message.value = ''
}

function reprendre(id) {
  Reflect.deleteProperty(placements.value, id)
  selection.value = id
  message.value = ''
}

function deposer(zoneVisee) {
  survol.value = null
  const element = elements.find(e => e.id === selection.value)
  if (!element) return

  if (element.zone === zoneVisee) {
    placements.value[element.id] = zoneVisee
    message.value = ''
  } else {
    Reflect.deleteProperty(placements.value, element.id)
    message.value = phraseDeRetour(element.zone, zoneVisee)
  }
  selection.value = null
}

function toutReprendre() {
  placements.value = {}
  selection.value = null
  message.value = ''
}

/* La règle du document passe avant celle de la colonne : se tromper de document
   est l'erreur qui compte, se tromper de colonne dans le bon document en est
   une plus petite. */
function phraseDeRetour(attendue, visee) {
  if (documentDe(attendue) !== documentDe(visee)) {
    return documentDe(attendue) === 'bilan'
      ? "Celui-ci est encore là le 31 décembre au soir. Le film raconte ce qui s'est passé pendant l'année ; celui-ci fait partie de ce qui reste."
      : "Celui-ci s'est passé pendant l'année. La photo ne montre pas ce qui s'est passé, elle montre ce qui reste."
  }
  return {
    actif: "Vous venez de répondre à « d'où vient l'argent ? ». Celui-ci répond à l'autre moitié de la question : où est-il ?",
    passif: "Celui-ci ne dit pas ce que l'entreprise détient. Il dit d'où vient ce qu'elle détient.",
    charges: "L'activité ne l'a pas gagné, elle l'a consommé.",
    produits: "L'activité ne l'a pas consommé, elle l'a gagné.",
  }[attendue]
}
</script>

<template>
  <M1ActiviteSection class="tri-actif-passif">
    <template #activite>
      Placez chaque élément dans la colonne où il apparaîtra
    </template>
    <template #info>
      Rien n'est chronométré ou noté. Un élément mal placé reste à sa place.
    </template>

    <!-- la réserve, collée en haut tant qu'il reste des éléments -->
    <div
      v-if="!termine"
      class="sticky top-0 z-10 backdrop-blur bg-activite"
    >
      <div class="flex justify-between items-center mb-4">
        <h3 class="titre-panneau color-activite">
          À placer
        </h3>
        <div class="places">
          {{ nbPlaces }} placés sur {{ elements.length }}
        </div>
      </div>
      <ul class="flex flex-wrap gap-3 list-none! list-outside! pl-0!">
        <li
          v-for="element in enAttente"
          :key="element.id"
        >
          <button
            type="button"
            draggable="true"
            class="btn-drag min-h-[3.25rem] w-[15rem]"
            :class="selection === element.id
              ? 'btn-drag-selected'
              : 'btn-drag-color'"
            :aria-pressed="selection === element.id"
            @dragstart="commencerGlisser(element.id)"
            @dragend="selection = null"
            @click="basculerSelection(element.id)"
          >
            {{ element.libelle }}
          </button>
        </li>
      </ul>
    </div>

    <!-- la phrase de clôture prend la place de la réserve -->
    <p
      v-else
      class="panneau-final"
    >
      Voilà les quatre colonnes. Tout ce que Latitude Café fera cette année ira dans l'une d'elles.
    </p>

    <!-- Le retour d'un dépôt faux. La région est rendue en permanence et sa
         hauteur réservée : sans cela, les quatre zones sautent d'une ligne à
         chaque erreur, sous le curseur qui vient de déposer. -->
    <p
      role="status"
      aria-live="polite"
      class="min-h-[1.25rem] text-sm font-medium text-error-500"
    >
      {{ message }}
    </p>

    <!-- les deux documents -->
    <!-- CL — subgrid : les lignes (titre / question / dépôt) s'alignent entre les deux
           colonnes même si le titre ou la question fait plus ou moins de lignes. -->
    <div class="panneau-depot mt-6 grid gap-x-6 gap-y-6 lg:gap-y-0 lg:grid-cols-2 lg:grid-rows-[auto_auto_1fr]">
      <div
        v-for="doc in documents"
        :key="doc.cle"
        class="lg:grid lg:grid-rows-subgrid lg:row-span-3"
      >
        <p class="mb-1! text-base font-bold text-slate-700">
          {{ doc.titre }}
        </p>
        <p class="mb-2! text-sm! text-slate-500">
          {{ doc.question }}
        </p>

        <div class="grid gap-3 sm:grid-cols-2">
          <div
            v-for="zone in zonesDe(doc.cle)"
            :key="zone.cle"
            class="zone-depot min-h-[6rem] transition"
            :class="survol === zone.cle
              ? 'zone-depot-hover'
              : 'zone-depot-nue'"
            @dragover.prevent="survol = zone.cle"
            @dragleave.self="survol = null"
            @drop.prevent="deposer(zone.cle)"
          >
            <h3 class="mb-2! flex justify-between titre-panneau color-neutral">
              <span>{{ zone.titre }}</span>
              <span>{{ contenuDe(zone.cle).length }}</span>
            </h3>

            <ul class="list-none! list-outside! pl-0!">
              <li
                v-for="element in contenuDe(zone.cle)"
                :key="element.id"
                class="mb-2"
              >
                <button
                  type="button"
                  draggable="false"
                  class="item-place"
                  @dragstart="commencerGlisser(element.id)"
                  @dragend="selection = null"
                  @click="reprendre(element.id)"
                >
                  {{ element.libelle }}
                </button>
              </li>
            </ul>

            <!-- le geste en deux appuis, qui est aussi le chemin du clavier -->
            <button
              v-if="selection"
              type="button"
              class="btn-placer-ici"
              :aria-label="`Placer dans ${zone.titre}`"
              @click="deposer(zone.cle)"
            >
              Placer ici
            </button>
          </div>
        </div>
      </div>
    </div>

    <div
      v-if="nbPlaces"
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
