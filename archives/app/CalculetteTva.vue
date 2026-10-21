<script setup>
import { ref, computed } from 'vue'

/* Les deux zones de la calculette. Chacune porte son nom, son numéro de compte
   et la question à laquelle elle répond — ce sont ces deux questions, et non les
   comptes, que les phrases de retour reprennent.
   Le composant ne dit pas « TVA à décaisser » : le terme, le compte 4455 et la
   ligne au Bilan arrivent après lui, dans le texte du chapitre. */
const zones = [
  { cle: 'collectee', titre: 'TVA collectée', compte: '4457', signe: '+', question: 'la taxe facturée aux clients' },
  { cle: 'deductible', titre: 'TVA déductible', compte: '4456', signe: '−', question: 'la taxe payée aux fournisseurs' },
]

/* Les trois lignes de taxe du premier trimestre, telles qu'elles sont au journal
   du module : deux au compte 4457, une au 4456. Aucune notion hors de ce que le
   Chapitre 5 a dit au-dessus du composant.
   La ligne porte son opération, jamais son numéro de compte : la décision
   demandée EST le compte, la ligne ne peut donc pas le donner.
   Les montants ne sont écrits qu'ici ; sous-totaux et résultat s'en déduisent. */
const lignes = [
  { id: 'tvaVentesPro', libelle: 'Ventes aux professionnels', periode: 'T1', montant: 6000, zone: 'collectee' },
  { id: 'tvaVentesComptoir', libelle: 'Ventes au comptoir', periode: 'T1', montant: 1800, zone: 'collectee' },
  { id: 'tvaAchats', libelle: 'Achats et charges externes', periode: 'T1', montant: 6600, zone: 'deductible' },
]

const placements = ref({}) // id de la ligne -> zone où elle est posée
const selection = ref(null) // id de la ligne saisie, à la souris comme au doigt
const survol = ref(null)
const message = ref('')

const enAttente = computed(() => lignes.filter(l => !placements.value[l.id]))
const nbPlacees = computed(() => Object.keys(placements.value).length)
const termine = computed(() => nbPlacees.value === lignes.length)
const ligneSaisie = computed(() => lignes.find(l => l.id === selection.value) || null)

const contenuDe = cle => lignes.filter(l => placements.value[l.id] === cle)
const sousTotal = cle => contenuDe(cle).reduce((somme, l) => somme + l.montant, 0)

/* Le résultat ne se lit que terminé : une différence partielle serait un nombre
   faux présenté comme la somme due à l'État. Les deux sous-totaux, eux, sont
   vrais à chaque instant et s'affichent toujours. */
const resultat = computed(() => sousTotal('collectee') - sousTotal('deductible'))

const euros = n => n.toLocaleString('fr-FR', { minimumFractionDigits: 2 })
const eurosRonds = n => `${n.toLocaleString('fr-FR')} €`

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
  const ligne = ligneSaisie.value
  if (!ligne) return

  if (ligne.zone === zoneVisee) {
    placements.value[ligne.id] = zoneVisee
    message.value = ''
  } else {
    Reflect.deleteProperty(placements.value, ligne.id)
    message.value = phraseDeRetour(ligne.zone)
  }
  selection.value = null
}

function toutReprendre() {
  placements.value = {}
  selection.value = null
  message.value = ''
}

/* Deux phrases pour les trois dépôts faux. Chacune porte sur la question à
   laquelle la zone répond, jamais sur l'opération déposée ni sur son montant :
   c'est ce qui empêche l'apprenant d'en tirer qu'une opération appartient à un
   compte, quand ce qui décide est le sens de la taxe. */
function phraseDeRetour(attendue) {
  return attendue === 'collectee'
    ? "Cette taxe n'a pas été payée à un fournisseur. Elle a été facturée à un client."
    : "Cette taxe n'a pas été facturée à un client. Elle a été payée à un fournisseur."
}
</script>

<template>
  <M1ActiviteSection class="calculette-tva">
    <template #activite>
      Placez chaque ligne de taxe du côté où elle compte
    </template>
    <template #info>
      Rien n'est chronométré ou noté. Une ligne mal placée reste à sa place.
    </template>

    <!-- les lignes du trimestre, collées en haut tant qu'il en reste.
         Le composant ne les appelle pas « le grand journal » : il n'en montre ni
         les colonnes ni les sens. -->
    <div
      v-if="!termine"
      class="sticky top-0 z-10 backdrop-blur bg-activite"
    >
      <div class="flex justify-between items-center mb-4">
        <h3 class="titre-panneau color-activite">
          Les lignes de taxe du trimestre
        </h3>
        <div class="places">
          {{ nbPlacees }} placée{{ nbPlacees > 1 ? 's' : '' }} sur {{ lignes.length }}
        </div>
      </div>
      <ul class="flex flex-col gap-2 list-none! list-outside! pl-0!">
        <li
          v-for="ligne in enAttente"
          :key="ligne.id"
        >
          <button
            type="button"
            draggable="true"
            class="btn-drag w-full justify-between gap-3"
            :class="selection === ligne.id
              ? 'btn-drag-selected'
              : 'btn-drag-color'"
            :aria-pressed="selection === ligne.id"
            @dragstart="commencerGlisser(ligne.id)"
            @dragend="selection = null"
            @click="basculerSelection(ligne.id)"
          >
            <span>
              {{ ligne.libelle }}
              <span class="opacity-70">{{ ligne.periode }}</span>
            </span>
            <span class="somme">{{ euros(ligne.montant) }}</span>
          </button>
        </li>
      </ul>
    </div>

    <!-- la phrase de clôture prend la place des lignes -->
    <p
      v-else
      class="panneau-final"
    >
      Sur les {{ eurosRonds(sousTotal('collectee')) }} de taxe facturés à ses clients, Latitude Café
      en avait déjà payé {{ eurosRonds(sousTotal('deductible')) }} à ses fournisseurs.
      Il en reste {{ eurosRonds(resultat) }} pour l'État.
    </p>

    <!-- le retour d'un dépôt faux. La région est rendue en permanence pour qu'un
         lecteur d'écran l'annonce, et réservée pour que rien ne saute. -->
    <p
      role="status"
      aria-live="polite"
      class="min-h-[1.25rem] text-sm font-medium text-error-500"
    >
      {{ message }}
    </p>

    <!-- la calculette : une soustraction posée. Les deux zones sont empilées,
         leurs signes dans la gouttière, et le résultat sous elles. Côte à côte,
         il aurait fallu une phrase pour dire laquelle se retranche de l'autre. -->
    <div class="mt-4 flex flex-col gap-3">
      <div
        v-for="zone in zones"
        :key="zone.cle"
        class="rang-operation"
      >
        <div
          class="signe-operation"
          aria-hidden="true"
        >
          {{ zone.signe }}
        </div>

        <div
          class="zone-depot min-h-[7rem] flex flex-col transition"
          :class="survol === zone.cle
            ? 'zone-depot-hover'
            : 'zone-depot-nue'"
          @dragover.prevent="survol = zone.cle"
          @dragleave.self="survol = null"
          @drop.prevent="deposer(zone.cle)"
        >
          <h3 class="mb-1! flex justify-between titre-panneau color-neutral">
            <span>{{ zone.titre }}</span>
            <span>{{ zone.compte }}</span>
          </h3>
          <p class="mb-2! text-sm! text-slate-500">
            {{ zone.question }}
          </p>

          <ul class="list-none! list-outside! pl-0!">
            <li
              v-for="ligne in contenuDe(zone.cle)"
              :key="ligne.id"
              class="mb-2"
            >
              <button
                type="button"
                draggable="false"
                class="item-place flex justify-between items-baseline gap-3"
                @dragstart="commencerGlisser(ligne.id)"
                @dragend="selection = null"
                @click="reprendre(ligne.id)"
              >
                <span>
                  {{ ligne.libelle }}
                  <span class="text-slate-500">{{ ligne.periode }}</span>
                </span>
                <span class="somme">{{ euros(ligne.montant) }}</span>
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

          <!-- le sous-total est vrai à chaque instant : il s'affiche toujours -->
          <p class="sous-total mb-0!">
            <span class="sous-total-libelle">Sous-total</span>
            <span class="somme">{{ euros(sousTotal(zone.cle)) }}</span>
          </p>
        </div>
      </div>

      <!-- le résultat, troisième rang de l'opération -->
      <div class="rang-operation">
        <div
          class="signe-operation"
          aria-hidden="true"
        >
          =
        </div>
        <div
          class="zone-resultat flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1"
          :class="termine ? 'zone-resultat-remplie' : 'zone-resultat-nue'"
        >
          <h3 class="titre-panneau color-neutral">
            Ce qu'elle doit remettre à l'État
            <span
              v-if="termine"
              class="block mt-0.5 text-sm font-medium! normal-case text-slate-500 somme"
            >
              {{ euros(sousTotal('collectee')) }} − {{ euros(sousTotal('deductible')) }}
            </span>
          </h3>
          <span
            v-if="termine"
            role="status"
            aria-live="polite"
            class="somme somme-resultat"
          >
            {{ euros(resultat) }}
          </span>
          <span
            v-else
            class="somme-attente"
            aria-hidden="true"
          >———</span>
        </div>
      </div>
    </div>

    <div
      v-if="nbPlacees"
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
