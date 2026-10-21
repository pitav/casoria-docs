<script setup>
/* m1/illustration/ArgentAu31Decembre.vue — Chapitre 12, « Piloter ».
   Portée depuis illustration-argent-au-31-decembre.html.

   C'est une illustration, pas une activité : aucun geste, aucun amber,
   slate seul. Les styles vivent dans illustrations.css, sous .illustration.

   Quatre lignes du Bilan et la machine, à une seule échelle. Le niveau de la
   trésorerie est prolongé sur toute la hauteur : c'est le bout de sa barre,
   pas un second élément, il ne porte donc pas de nombre. */

/* Les données de la scène, en un seul endroit. Si elles doivent un jour venir
   d'un store, c'est cet objet seul qui change. Soldes du Bilan au 31/12. */
const scene = {
  date: '31 décembre',
  stock: 15000, // 355
  creances: 63000, // 411
  tresorerie: 17310, // 512
  fournisseurs: 9000, // 401
  machine: 43200, // TTC, pas achetée
}

/* sorte : actif = barre pleine ; passif = trait plein, il joue en sens
   inverse ; projet = trait pointillé, pas encore (règle du Chapitre 4). */
const groupes = [
  { nom: 'Actif', sorte: 'actif', lignes: [
    { lib: 'Stock', montant: scene.stock },
    { lib: 'Créances clients', montant: scene.creances },
    { lib: 'Trésorerie', montant: scene.tresorerie },
  ] },
  { nom: 'Passif', sorte: 'passif', lignes: [
    { lib: 'Dettes fournisseurs', montant: scene.fournisseurs },
  ] },
  { nom: 'À côté', sorte: 'projet', lignes: [
    { lib: 'Machine à torréfier', montant: scene.machine },
  ] },
]

/* L'échelle : la plus longue barre prend la piste entière. */
const echelle = {
  '--max': Math.max(...groupes.flatMap(g => g.lignes.map(l => l.montant))),
  '--niveau': scene.tresorerie,
}

/* formatEuros() : shared/utils/formatEuros.ts, auto-importé par Nuxt. */
/* L'équivalent du « alt » : il décrit ce qu'on voit, la légende du chapitre
   tire la leçon. */
const alt = `Au ${scene.date}, quatre lignes du Bilan de Latitude Café à la même échelle. `
  + `À l'Actif : Stock, ${formatEuros(scene.stock)} ; Créances clients, ${formatEuros(scene.creances)} ; `
  + `Trésorerie, ${formatEuros(scene.tresorerie)}. `
  + `Au Passif : Dettes fournisseurs, ${formatEuros(scene.fournisseurs)}. `
  + `Un trait pointillé prolonge la trésorerie sur toute la hauteur ; seules les créances `
  + `clients le dépassent, le stock s'arrête un peu avant. En dessous, à la même échelle `
  + `et en pointillé, la machine à torréfier, ${formatEuros(scene.machine)}, bien au-delà du trait.`
</script>

<template>
  <div
    class="illustration argent-au-31-decembre"
    role="img"
    :aria-label="alt"
  >
    <div aria-hidden="true">
      <div class="quand">
        Au {{ scene.date }}
      </div>

      <!-- une grille à plat : intitulé, piste, montant -->
      <div
        class="graphe"
        :style="echelle"
      >
        <span class="niveau"><span>la trésorerie</span></span>

        <template
          v-for="(g, i) in groupes"
          :key="g.nom"
        >
          <div
            class="groupe"
            :class="{ premier: i === 0, projet: g.sorte === 'projet' }"
          >
            {{ g.nom }}
          </div>

          <template
            v-for="l in g.lignes"
            :key="l.lib"
          >
            <div class="lib">
              <span>{{ l.lib }}</span>
            </div>
            <div
              class="piste"
              :class="g.sorte"
            >
              <span
                class="barre"
                :style="{ '--m': l.montant }"
              />
            </div>
            <div class="val">
              {{ formatEuros(l.montant) }}
            </div>
          </template>
        </template>
      </div>
    </div>
  </div>
</template>
