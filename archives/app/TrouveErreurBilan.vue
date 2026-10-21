<script setup>
import { ref, computed } from 'vue'

/* <TrouveErreurBilan /> — Chapitre 8, point d'étape.
   Le Bilan de l'apprenant tel qu'il est à la fin du chapitre, avec UNE ligne
   en trop : les achats de café vert, rangés à l'Actif. L'apprenant clique sur
   la ligne qu'il croit fausse.

   Palette : amber pour la question, slate pour le Bilan, lime pour ce qui est
   acquis (une ligne vérifiée, la ligne trouvée). Le verdict prend les trois
   teintes du module. Aucune information n'est portée par la couleur seule —
   le verdict est écrit, une ligne vérifiée porte sa coche, la ligne trouvée
   est barrée et dit où elle va. */

/* Les onze lignes, dans l'ordre de la grille. Montants en euros, tels que le
   rejeu du journal les donne à la fin du Chapitre 8. `retour` est la remarque
   affichée quand l'apprenant clique une ligne juste : elle dit pourquoi la
   ligne est à sa place, sans désigner la bonne. */
const colonnes = [
  {
    cle: 'actif',
    nom: 'Actif',
    mention: "ce que l'entreprise détient",
    total: 'Total actif',
    lignes: [
      { compte: '215', intitule: 'Torréfacteur', montant: 36000,
        retour: "La machine servira cinq ans. L'entreprise la détient, à son prix hors taxes." },
      /* Le signe moins est la fausse piste la plus honorable du lot : le
         chapitre vient de dire qu'aucun montant négatif n'est écrit nulle part.
         La remarque commence par lui donner raison de s'étonner. */
      { compte: '2815', intitule: 'Amortissements du torréfacteur', montant: -3600,
        retour: 'Le signe moins surprend, et il est juste. Cette ligne se retranche de la machine, qui vaut encore 32 400 € dans les comptes.' },
      /* Le seul « Presque » : c'est le bon raisonnement — le café consommé n'a
         rien à faire au Bilan — appliqué au mauvais café. */
      { compte: '355', intitule: 'Stock de café torréfié', montant: 15000, presque: true,
        retour: "Vous êtes sur la bonne piste, c'est une affaire de café. Mais celui-ci attend sur les étagères, torréfié et pas encore vendu. L'entreprise le détient." },
      { compte: '411', intitule: 'Créances clients', montant: 90000,
        retour: "Des clients doivent encore ces factures. Cet argent reviendra à l'entreprise." },
      { compte: '512', intitule: 'Trésorerie', montant: 61371.10,
        retour: "C'est l'argent sur le compte en banque, une fois le torréfacteur payé." },
      /* L'INTRUSE. Numéro et intitulé de la grille, montant du Compte de
         Résultat au même instant (25 000 € au Chapitre 6, plus 30 000 € au
         deuxième trimestre). */
      { compte: '601', intitule: 'Achats de café vert', montant: 55000, intruse: true },
    ],
  },
  {
    cle: 'passif',
    nom: 'Passif',
    mention: "d'où vient l'argent",
    total: 'Total passif',
    lignes: [
      { compte: '101', intitule: 'Capital social', montant: 30000,
        retour: "C'est l'argent que les associés ont apporté à la création." },
      { compte: '455', intitule: "Compte courant d'associé", montant: 15000,
        retour: "C'est ce que l'entreprise doit encore à Thomas, après lui avoir rendu 5 000 €." },
      { compte: '164', intitule: 'Emprunt bancaire', montant: 34458.60,
        retour: "C'est ce que l'entreprise doit encore à la banque, une fois la première échéance payée." },
      { compte: '401', intitule: 'Dettes fournisseurs', montant: 97200,
        retour: "Ce sont des factures de fournisseurs que l'entreprise n'a pas encore payées." },
      { compte: '4455', intitule: 'État — TVA à décaisser', montant: 1200,
        retour: "C'est de la TVA que l'entreprise doit encore à l'État." },
    ],
  },
]

const euros = n => (n < 0 ? '− ' : '')
  + Math.abs(n).toLocaleString('fr-FR', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' €'

const arrondi = n => Math.round(n * 100) / 100
const somme = (col, sansIntruse) => arrondi(col.lignes
  .filter(l => !(sansIntruse && l.intruse))
  .reduce((s, l) => s + l.montant, 0))

const actifAvant = somme(colonnes[0], false) // 253 771,10 €
const actifApres = somme(colonnes[0], true) // 198 771,10 €, celui de la grille

/* Le texte de la bonne réponse. C'est le seul endroit qui donne la raison, et
   il la donne avec ses nombres. */
const texteTrouve =`Ce café vert n'existe plus sous cette forme. Latitude Café l'a torréfié, `
  + `l'activité l'a consommé, et sa place est au Compte de Résultat, du côté des charges. `
  + `La ligne quitte l'Actif, qui passe de ${euros(actifAvant)} à ${euros(actifApres)}. `
  + `Ce qui reste de ce café sur les étagères y figure déjà, c'est le stock de café torréfié.`

const verifiees = ref([]) // les lignes justes déjà cliquées
const derniere = ref(null) // la dernière ligne cliquée : le verdict s'en déduit
const trouve = ref(false)

/* Seule la PREMIÈRE ligne cliquée part à l'événement. « Tout reprendre »
   remet l'écran à zéro, pas la mesure. */
const emit = defineEmits(['premiere-reponse'])
const premiereReponse = ref(null)

const verdict = computed(() => {
  const l = derniere.value
  if (!l) return null
  if (l.intruse) return { mot: 'Bonne réponse', classe: '', texte: texteTrouve }
  if (l.presque) return { mot: 'Presque', classe: 'panneau-final-presque', texte: l.retour }
  return { mot: 'Mauvaise réponse', classe: 'panneau-final-faux', texte: l.retour }
})

const estVerifiee = l => verifiees.value.includes(l.compte)
const inactive = l => trouve.value || estVerifiee(l)

/* Un seul clic : chercher une ligne fausse est une suite de tentatives, pas une
   position qu'on engage. Une ligne juste se coche et ne se clique plus — la
   recherche se resserre d'elle-même. */
function choisir(l) {
  if (inactive(l)) return
  if (!premiereReponse.value) {
    premiereReponse.value = l.compte
    emit('premiere-reponse', l.compte)
  }
  derniere.value = l
  if (l.intruse) trouve.value = true
  else verifiees.value.push(l.compte)
}

function toutReprendre() {
  verifiees.value = []
  derniere.value = null
  trouve.value = false
}

const totalDe = col => col.cle === 'actif'
  ? (trouve.value ? actifApres : actifAvant)
  : somme(col, false)

const libelleBouton = l => `${l.compte} ${l.intitule}, ${euros(l.montant)}`
  + (estVerifiee(l) ? ', ligne juste' : '')
  + (l.intruse && trouve.value ? ', erreur trouvée, sa place est au Compte de Résultat' : '')

const annonce = computed(() => trouve.value
  ? `Le total de l'actif passe de ${euros(actifAvant)} à ${euros(actifApres)}.`
  : '')
</script>

<template>
  <!-- Le composant occupe la moitié droite de l'écran, à la place du Bilan :
       il porte donc le Bilan lui-même. Largeur utile, environ 700 px. -->
  <M1ActiviteSection class="trouve-erreur-bilan">
    <template #activite>
      Une ligne de ce Bilan n'a rien à y faire. Trouvez-la.
    </template>
    <template #info>
      Rien n'est noté. Une ligne juste se coche, et vous continuez.
    </template>

    <!-- la question. Pas de bouton ici : les réponses sont les lignes du Bilan,
         juste en dessous. -->
    <div class="mt-3 bg-activite">
      <h3 class="titre-panneau color-activite">
        La question
      </h3>
      <p
        id="teb-question"
        class="mt-3 text-[0.95rem] font-semibold text-amber-900"
      >
        Quelle ligne ne devrait pas figurer au Bilan de Latitude Café&nbsp;?
      </p>
      <p class="mt-1 text-sm text-amber-800">
        Cliquez dessus. Les deux totaux ne sont pas égaux, et ce n'est pas l'erreur.
      </p>
    </div>

    <!-- le Bilan. Chaque ligne est un bouton. -->
    <div
      role="group"
      aria-labelledby="teb-question"
      class="zone-resultat mt-4"
      :class="trouve ? 'zone-resultat-remplie' : 'zone-resultat-nue'"
    >
      <h3 class="titre-panneau color-neutral">
        Bilan
      </h3>
      <p class="mt-px text-[0.63rem] leading-snug text-slate-500">
        où est l'argent, et d'où vient-il
      </p>

      <div class="mt-3 grid gap-4 sm:grid-cols-2">
        <div
          v-for="col in colonnes"
          :key="col.cle"
          class="flex flex-col"
        >
          <p class="mb-1 text-[0.56rem] font-bold uppercase tracking-[0.11em] text-slate-400">
            {{ col.nom }}
            <span class="font-medium normal-case tracking-normal"> · {{ col.mention }}</span>
          </p>

          <button
            v-for="l in col.lignes"
            :key="l.compte"
            type="button"
            class="ligne-choix"
            :class="{
              'ligne-juste': estVerifiee(l),
              'ligne-trouvee': l.intruse && trouve,
            }"
            :aria-disabled="inactive(l) ? 'true' : undefined"
            :aria-label="libelleBouton(l)"
            @click="choisir(l)"
          >
            <span class="ligne-choix-libelle">
              <span class="barre"><b class="mr-1 font-bold">{{ l.compte }}</b>{{ l.intitule }}</span>
              <span
                v-if="l.intruse && trouve"
                class="ligne-destination"
              >→ Compte de Résultat</span>
            </span>
            <span class="ligne-choix-montant">
              <span
                v-if="estVerifiee(l)"
                class="coche"
                aria-hidden="true"
              >✓</span>
              <span class="somme barre">{{ euros(l.montant) }}</span>
            </span>
          </button>

          <!-- les deux totaux à la même hauteur, comme à la grille -->
          <p class="total-doc">
            <span class="text-[0.6rem] font-bold uppercase tracking-[0.1em] text-slate-600">
              {{ col.total }}
            </span>
            <span class="text-[0.85rem] font-bold tabular-nums whitespace-nowrap text-slate-800">
              <span
                v-if="col.cle === 'actif' && trouve"
                class="valeur-avant"
              >{{ euros(actifAvant) }} →</span>
              {{ euros(totalDe(col)) }}
            </span>
          </p>
        </div>
      </div>
    </div>

    <!-- LE VERDICT, sous les lignes qu'on vient de cliquer. La région est
         toujours rendue, hauteur réservée : rien ne saute sous le curseur. -->
    <div
      role="status"
      aria-live="polite"
      class="mt-3 min-h-[7.5rem]"
    >
      <p
        v-if="verdict"
        :key="derniere.compte"
        class="panneau-final mt-0!"
        :class="verdict.classe"
      >
        <span class="titre-panneau">{{ verdict.mot }}</span>
        {{ verdict.texte }}
      </p>
    </div>

    <!-- toujours à sa place, invisible tant qu'il n'y a rien à reprendre -->
    <div
      class="mt-3"
      :class="{ invisible: !derniere }"
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
