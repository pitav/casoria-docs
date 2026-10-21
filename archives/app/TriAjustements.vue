<script setup>
import { ref, computed } from 'vue'

/* <TriAjustements /> — Chapitre 10, en fin du dernier sous-titre, après les
   deux blocs d'écritures qui se touchent.
   Six situations de fin d'année, quatre issues. L'apprenant range chacune là
   où elle va au 31 décembre. Aucune des six n'est l'un des trois faits du
   chapitre : les ranger serait se souvenir, pas reconnaître.

   Même geste que le <TriActifPassif /> : glisser-déposer, ou deux appuis
   (saisir, puis « Placer ici »), qui sont aussi le chemin du clavier. Un
   dépôt n'est pas une réponse à une question : pas de verdict, une ligne
   `text-error-500` par geste refusé, un `.panneau-final` à la fin.

   Palette : amber pour les situations à ranger, slate pour les quatre
   issues, lime pour ce qui est rangé. Rien n'est porté par la couleur seule.

   Les textes s'écrivent avec `~` là où il faut une espace insécable ; `nb()`
   la pose en une passe. Ne jamais taper l'insécable au clavier. */
const nb = s => s.replaceAll('~', ' ')

/* Les quatre issues. Dans l'ordre de la grille 2 × 2 : le miroir du chapitre
   sur la première ligne, la prudence et l'absence de correction sur la
   seconde. Le nom est celui du chapitre, écrit en toutes lettres — jamais de
   sigle pour les charges constatées d'avance (déroulé, vigilance du
   Chapitre 10). */
const zones = [
  { cle: 'chargeAvance', titre: "Charges constatées d'avance", mouvement: "Quitte les charges, rejoint l'Actif" },
  { cle: 'produitAvance', titre: "Produits constatés d'avance", mouvement: 'Quitte les produits, rejoint le Passif' },
  { cle: 'provision', titre: 'Provision', mouvement: "Entre dans les charges, s'inscrit au Passif" },
  { cle: 'rien', titre: 'Rien à corriger', mouvement: "L'année dit déjà ce qu'elle a fait" },
]

/* Les six situations. `retour` est la phrase d'un dépôt refusé : elle dit
   pourquoi la situation va ailleurs. Aucune ne demande une notion que le
   Chapitre 10 ou le Chapitre 9 n'a pas donnée.
   Les parts sur 2027, pour la relecture, ne s'affichent pas :
   loyer 5 mois × 300 € = 1 500 € ; logiciel 8 mois × 40 € = 320 € ;
   abonnement 11 paquets × 20 € = 220 €. */
const situations = [
  /* La paire de la prudence : même phrase, même avocat, sens opposé. */
  {
    id: 'penalites',
    titre: 'Des pénalités réclamées par un fournisseur',
    detail: nb("Une commande annulée en octobre. Le fournisseur réclame 4~000~€, et l'avocat de Latitude Café juge probable qu'il obtienne gain de cause."),
    zone: 'provision',
    retour: nb("La perte n'est pas encore certaine, et rien n'est payé. Mais elle est probable, son montant est estimé, et la comptabilité n'attend pas la certitude pour l'inscrire."),
  },
  {
    id: 'transporteur',
    titre: 'Une indemnité réclamée à un transporteur',
    detail: nb("Un colis cassé en novembre. Latitude Café réclame 1~500~€ au transporteur, et son avocat juge probable qu'elle obtienne gain de cause."),
    zone: 'rien',
    retour: nb("Même probable, un gain espéré ne s'inscrit jamais. La prudence ne joue que dans un sens, et ces 1~500~€ n'entreront dans les comptes qu'une fois acquis."),
  },
  /* Deux charges payées d'avance, sur deux durées : l'une presque entière
     sur 2027, l'autre aux deux tiers. */
  {
    id: 'loyer',
    titre: "Le loyer d'un entrepôt",
    detail: nb('1~800~€ payés en décembre pour six mois, de décembre à mai.'),
    zone: 'chargeAvance',
    retour: "Un seul mois de ce loyer concerne 2026. Les cinq autres concernent 2027, et leur part quitte les charges de l'année.",
  },
  {
    id: 'logiciel',
    titre: "L'abonnement au logiciel de caisse",
    detail: nb('480~€ payés en septembre pour douze mois, de septembre à août.'),
    zone: 'chargeAvance',
    retour: "Quatre mois de cet abonnement concernent 2026. Les huit autres concernent 2027, et leur part quitte les charges de l'année.",
  },
  {
    id: 'abonnementClient',
    titre: "L'abonnement d'un client",
    detail: nb('240~€ encaissés en décembre pour douze paquets de café, un par mois de décembre à novembre.'),
    zone: 'produitAvance',
    retour: "Un seul paquet est livré en 2026. Les onze autres le seront en 2027, et leur part quitte les produits de l'année.",
  },
  {
    id: 'salaires',
    titre: 'Les salaires de décembre',
    detail: "Versés à l'équipe le 31 décembre, pour le travail de décembre.",
    zone: 'rien',
    retour: "Ces salaires concernent décembre, et ils sont déjà inscrits en décembre. Rien n'est à déplacer.",
  },
]

/* Le miroir se trompe d'une façon à lui : le bon mouvement, le mauvais
   côté. La phrase le dit plutôt que de redire la durée. */
const retourMiroir = {
  chargeAvance: "Latitude Café a payé cette somme, elle ne l'a pas encaissée. Ce qui quitte l'année est une charge.",
  produitAvance: "Cette fois, c'est Latitude Café qui a encaissé. Ce qui quitte l'année est un produit.",
}

const placements = ref({}) // id de la situation -> zone où elle est rangée
const selection = ref(null) // id de la situation saisie, à la souris comme au doigt
const survol = ref(null)
const message = ref('')

const enAttente = computed(() => situations.filter(s => !placements.value[s.id]))
const nbRangees = computed(() => Object.keys(placements.value).length)
const termine = computed(() => nbRangees.value === situations.length)
const contenuDe = cle => situations.filter(s => placements.value[s.id] === cle)

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
  const situation = situations.find(s => s.id === selection.value)
  if (!situation) return

  if (situation.zone === zoneVisee) {
    placements.value[situation.id] = zoneVisee
    message.value = ''
  } else {
    Reflect.deleteProperty(placements.value, situation.id)
    const miroir = ['chargeAvance', 'produitAvance']
    message.value = miroir.includes(situation.zone) && miroir.includes(zoneVisee)
      ? retourMiroir[situation.zone]
      : situation.retour
  }
  selection.value = null
}

function toutReprendre() {
  placements.value = {}
  selection.value = null
  message.value = ''
}
</script>

<template>
  <M1ActiviteSection class="tri-ajustements">
    <template #activite>
      Rangez chaque situation selon ce que Latitude Café doit faire au 31 décembre
    </template>
    <template #info>
      Rien n'est chronométré ou noté. Une situation mal rangée revient parmi les autres.
    </template>

    <!-- les situations à ranger, collées en haut tant qu'il en reste — à
         partir de 640 px seulement. En étroit, les six cartes font plus haut
         qu'un écran de téléphone : collées, elles recouvriraient les zones. -->
    <div
      v-if="!termine"
      class="sm:sticky sm:top-0 z-10 backdrop-blur bg-activite"
    >
      <div class="flex justify-between items-center mb-3">
        <h3 class="titre-panneau color-activite">
          À ranger
        </h3>
        <div class="places">
          {{ nbRangees }} rangées sur {{ situations.length }}
        </div>
      </div>
      <!-- deux colonnes : six cartes sur une seule en prendraient le double en
           hauteur, dans la moitié d'écran dont le composant dispose -->
      <ul class="grid gap-2 sm:grid-cols-2 list-none! list-outside! pl-0!">
        <li
          v-for="situation in enAttente"
          :key="situation.id"
        >
          <button
            type="button"
            draggable="true"
            class="btn-drag h-full w-full flex-col items-start! gap-0.5"
            :class="selection === situation.id
              ? 'btn-drag-selected'
              : 'btn-drag-color'"
            :aria-pressed="selection === situation.id"
            @dragstart="commencerGlisser(situation.id)"
            @dragend="selection = null"
            @click="basculerSelection(situation.id)"
          >
            <span class="font-bold">{{ situation.titre }}</span>
            <span class="text-xs leading-snug opacity-90">{{ situation.detail }}</span>
          </button>
        </li>
      </ul>
    </div>

    <!-- la phrase de clôture prend la place des situations -->
    <p
      v-else
      class="panneau-final"
    >
      Les six situations sont rangées. Quatre demandaient une correction au 31 décembre, deux n'en demandaient aucune.
    </p>

    <!-- Le retour d'un dépôt refusé. Rendu en permanence, hauteur réservée
         sur deux lignes : les phrases de ce composant en font souvent deux,
         et les quatre zones ne doivent pas sauter sous le curseur. -->
    <p
      role="status"
      aria-live="polite"
      class="min-h-[2.5rem] mt-2 text-sm font-medium text-error-500"
    >
      {{ message }}
    </p>

    <!-- les quatre issues, en 2 × 2 dès 640 px -->
    <div class="panneau-depot mt-2 grid gap-3 sm:grid-cols-2">
      <div
        v-for="zone in zones"
        :key="zone.cle"
        class="zone-depot min-h-[6.5rem] flex flex-col transition"
        :class="survol === zone.cle
          ? 'zone-depot-hover'
          : 'zone-depot-nue'"
        @dragover.prevent="survol = zone.cle"
        @dragleave.self="survol = null"
        @drop.prevent="deposer(zone.cle)"
      >
        <h3 class="flex justify-between gap-2 titre-panneau color-neutral">
          <span>{{ zone.titre }}</span>
          <span>{{ contenuDe(zone.cle).length }}</span>
        </h3>
        <p class="mt-0.5! mb-2! text-xs text-slate-500">
          {{ zone.mouvement }}
        </p>

        <!-- une situation rangée ne garde que son titre : le détail a servi -->
        <ul class="list-none! list-outside! pl-0!">
          <li
            v-for="situation in contenuDe(zone.cle)"
            :key="situation.id"
            class="mb-2"
          >
            <button
              type="button"
              draggable="false"
              class="item-place"
              @click="reprendre(situation.id)"
            >
              {{ situation.titre }}
            </button>
          </li>
        </ul>

        <!-- le geste en deux appuis, qui est aussi le chemin du clavier -->
        <button
          v-if="selection"
          type="button"
          class="btn-placer-ici mt-auto"
          :aria-label="`Ranger dans ${zone.titre}`"
          @click="deposer(zone.cle)"
        >
          Placer ici
        </button>
      </div>
    </div>

    <!-- toujours à sa place, invisible tant qu'il n'y a rien à reprendre :
         il ne saute pas sous le doigt -->
    <div class="mt-4">
      <UButton
        type="button"
        size="sm"
        color="neutral"
        :class="nbRangees ? '' : 'invisible'"
        :tabindex="nbRangees ? 0 : -1"
        @click="toutReprendre"
      >
        Tout reprendre
      </UButton>
    </div>
  </M1ActiviteSection>
</template>
