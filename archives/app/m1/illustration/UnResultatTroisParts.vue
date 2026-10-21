<script setup>
/* m1/illustration/UnResultatTroisParts.vue — Chapitre 11, « La clôture ».
   Portée depuis illustration-affectation.html (v2).

   C'est une illustration, pas une activité : aucun geste, aucun amber,
   slate seul. Les styles vivent dans illustrations.css, sous .illustration.

   Les associés décident ce que devient le résultat net. Le résultat est
   montré tel que le Bilan arrêté le porte (un seul panneau, qui dit à la
   fois le montant et sa provenance), puis une fourche à trois branches :
   le partage est le sujet. Aucun montant par part — ni le chapitre ni le
   déroulé n'en donnent ; en inventer serait un nombre neuf.

   Icônes : Material Design Icons (licence Apache 2.0), par <UIcon /> de
   Nuxt UI. Leur taille suit la taille de police (1em). */

/* Les données de la scène, en un seul endroit. Si elles doivent un jour venir
   d'un store, c'est cet objet seul qui change. */
const scene = {
  associes: [
    { nom: 'Thomas Vasseur', icone: 'i-mdi-account-tie' },
    { nom: 'Claire Berthier', icone: 'i-mdi-account-tie-woman' },
  ],
  bilan: 'Bilan au 31\u00a0décembre',
  resultat: 27200, // 120, résultat de l'exercice
  parts: [
    { nom: 'Réserve légale', dit: 'reste, la loi l’exige' },
    { nom: 'Dividende', dit: 'versé aux associés' },
    { nom: 'Report à nouveau', dit: 'attend l’année suivante' },
  ],
}

/* formatEuros() : shared/utils/formatEuros.ts, auto-importé par Nuxt. */
/* L'équivalent du « alt » : il décrit ce qu'on voit, la légende du chapitre
   tire la leçon. */
const alt = `Les deux associés décident ce que devient le résultat net. `
  + `${scene.bilan}, arrêté, marqué d'un cadenas : résultat de l'exercice, `
  + `${formatEuros(scene.resultat)}. Il se partage en trois : `
  + scene.parts.map(p => `${p.nom.toLowerCase()}, ${p.dit}`).join(' ; ')
  + `.`
</script>

<template>
  <div
    class="illustration un-resultat-trois-parts"
    role="img"
    :aria-label="alt"
  >
    <div
      class="scene"
      aria-hidden="true"
    >
      <!-- la décision -->
      <div class="qui">
        <span class="qui-icones">
          <UIcon
            v-for="a in scene.associes"
            :key="a.nom"
            :name="a.icone"
            class="qui-icone"
          />
        </span>
        <div class="qui-texte">
          <b>Les associés décident</b>
          <span>ce que devient le résultat net</span>
        </div>
      </div>

      <!-- le résultat, tel que le Bilan arrêté le porte -->
      <div class="micro">
        <div class="micro-titre">
          {{ scene.bilan }}
        </div>
        <div class="micro-lib">
          <UIcon
            name="i-mdi-lock-outline"
            class="micro-icone"
          />
          Résultat de l’exercice
        </div>
        <div class="micro-val">
          {{ formatEuros(scene.resultat) }}
        </div>
      </div>

      <!-- la fourche : un tronc, trois branches -->
      <div class="fourche">
        <span class="tronc" />
        <span class="branches" />
        <span class="milieu" />
      </div>

      <div class="parts">
        <div
          v-for="p in scene.parts"
          :key="p.nom"
          class="part"
        >
          <b>{{ p.nom }}</b>
          <span>{{ p.dit }}</span>
        </div>
      </div>
    </div>
  </div>
</template>
