<script setup>
/* m1/illustration/ApportEnCapital.vue — Chapitre 2, « L'écriture comptable ».
   Portée depuis illustration-apport-capital.html.

   C'est une illustration, pas une activité : aucun geste, aucun amber,
   slate seul. Les styles vivent dans illustrations.css, sous .illustration.

   Le grand journal réduit à son T : une seule opération, lue au Débit (où va
   la valeur) et au Crédit (d'où elle vient). Pas de flèche ni de « = » :
   l'égalité des totaux comme contrôle est la leçon du Chapitre 3.

   Icônes : Material Design Icons (licence Apache 2.0), par <UIcon /> de
   Nuxt UI. Leur taille suit la taille de police (1em). */

/* Les données de la scène, en un seul endroit. Si elles doivent un jour venir
   d'un store, c'est cet objet seul qui change. Écriture du 5 janvier. */
const scene = {
  operation: 'Apport en capital · 5\u00a0janvier',
  banque: { nom: ['Le compte en banque', 'de Latitude Café'], icone: 'i-mdi-bank' }, // 512
  associes: [ // 101
    { nom: ['Thomas', 'Vasseur'], icone: 'i-mdi-account-tie', montant: 15000 },
    { nom: ['Claire', 'Berthier'], icone: 'i-mdi-account-tie-woman', montant: 15000 },
  ],
}

/* Une seule opération : le même total au pied des deux colonnes. */
const total = scene.associes.reduce((s, a) => s + a.montant, 0)

/* formatEuros() : shared/utils/formatEuros.ts, auto-importé par Nuxt. */
/* L'équivalent du « alt » : il décrit ce qu'on voit, la légende du chapitre
   tire la leçon. */
const alt = `${scene.operation.replace(' · ', ', ')}. Un tableau en T, deux colonnes. `
  + `Au Débit, où va la valeur : ${scene.banque.nom.join(' ')} ; total ${formatEuros(total)}. `
  + `Au Crédit, d'où elle vient : `
  + scene.associes.map(a => `${a.nom.join(' ')}, ${formatEuros(a.montant)}`).join(', et ')
  + ` ; total ${formatEuros(total)}.`
</script>

<template>
  <div
    class="illustration apport-en-capital"
    role="img"
    :aria-label="alt"
  >
    <div aria-hidden="true">
      <div class="quand">
        {{ scene.operation }}
      </div>

      <!-- le T : en-têtes, corps, pieds ; un trait vertical au milieu -->
      <div class="journal">
        <div class="entete g">
          <b>Débit</b>
          <span>où va la valeur</span>
        </div>
        <div class="entete d">
          <b>Crédit</b>
          <span>d’où elle vient</span>
        </div>

        <div class="corps g">
          <div class="fig banque">
            <UIcon
              :name="scene.banque.icone"
              class="fig-icone"
            />
            <div class="fig-nom">
              <span
                v-for="l in scene.banque.nom"
                :key="l"
              >{{ l }}</span>
            </div>
          </div>
        </div>

        <div class="corps d">
          <div
            v-for="a in scene.associes"
            :key="a.icone"
            class="fig"
          >
            <UIcon
              :name="a.icone"
              class="fig-icone"
            />
            <div class="fig-nom">
              <span
                v-for="l in a.nom"
                :key="l"
              >{{ l }}</span>
            </div>
            <div class="fig-part">
              {{ formatEuros(a.montant) }}
            </div>
          </div>
        </div>

        <div class="pied g">
          {{ formatEuros(total) }}
        </div>
        <div class="pied d">
          {{ formatEuros(total) }}
        </div>
      </div>
    </div>
  </div>
</template>
