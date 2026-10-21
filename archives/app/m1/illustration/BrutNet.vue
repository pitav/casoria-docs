<script setup>
/* m1/illustration/BrutNet.vue — Chapitre 8, « Investir ».
   Portée depuis illustration-brut-net.html.

   C'est une illustration, pas une activité : aucun geste, aucun amber,
   slate seul. Les styles vivent dans illustrations.css, sous .illustration.

   Le torréfacteur écrit de deux façons, deux panneaux empilés (la légende
   dit « en haut / en bas »). En haut, la présentation de cette formation :
   deux lignes, et le net en pointillé à pleine encre — il existe mais n'est
   pas écrit (règle du Chapitre 4). En bas, un vrai bilan : une ligne en
   trois colonnes, le net encadré, le nombre qu'on va chercher.
   « Dans cette formation », jamais « la grille » (mot de fabrication). */

/* Les données de la scène, en un seul endroit. Si elles doivent un jour venir
   d'un store, c'est cet objet seul qui change. Le net se calcule. */
const scene = {
  bien: 'Torréfacteur',
  brut: 36000, // inv-torref-215d
  amortissements: 3600, // inv-amort-2815c
}
const net = scene.brut - scene.amortissements // 32 400

/* formatEuros() : shared/utils/formatEuros.ts, auto-importé par Nuxt. */
const m = {
  brut: formatEuros(scene.brut),
  amortissements: formatEuros(scene.amortissements),
  // le signe moins que le Bilan de la formation affiche
  moins: formatEuros(-scene.amortissements),
  net: formatEuros(net),
}
const libAmortissements = `Amortissements du ${scene.bien.toLowerCase()}`

/* L'équivalent du « alt » : il décrit ce qu'on voit, la légende du chapitre
   tire la leçon. */
const alt = `Le ${scene.bien.toLowerCase()} écrit de deux façons. `
  + `Dans cette formation, à l'Actif, deux lignes : ${scene.bien}, ${m.brut} ; `
  + `${libAmortissements}, moins ${m.amortissements} ; une accolade les réunit vers `
  + `${m.net}, en pointillé, à calculer. `
  + `Dans un vrai bilan, une ligne en trois colonnes : ${scene.bien}, brut ${m.brut}, `
  + `amortissements ${m.amortissements}, net ${m.net}, encadré.`
</script>

<template>
  <div
    class="illustration brut-net"
    role="img"
    :aria-label="alt"
  >
    <div aria-hidden="true">
      <!-- en haut : deux lignes, la soustraction à faire -->
      <div class="pan">
        <div class="pan-t">
          Dans cette formation
        </div>
        <div class="pan-actif">
          Actif
        </div>
        <div class="deux">
          <div class="rangees">
            <div class="rangee">
              <span class="rangee-lib">{{ scene.bien }}</span>
              <span class="rangee-val">{{ m.brut }}</span>
            </div>
            <div class="rangee">
              <span class="rangee-lib">{{ libAmortissements }}</span>
              <span class="rangee-val">{{ m.moins }}</span>
            </div>
          </div>
          <span class="acc" />
          <div class="calc">
            <div class="calc-val">
              {{ m.net }}
            </div>
            <div class="calc-n">
              à calculer
            </div>
          </div>
        </div>
      </div>

      <!-- en bas : une ligne, trois colonnes -->
      <div class="pan">
        <div class="pan-t">
          Dans un vrai bilan
        </div>
        <div class="trois">
          <div class="th th-actif">
            Actif
          </div>
          <div class="th">
            Brut
          </div>
          <div class="th">
            Amortissements
          </div>
          <div class="th th-net">
            Net
          </div>
          <div class="td td-lib">
            {{ scene.bien }}
          </div>
          <div class="td">
            {{ m.brut }}
          </div>
          <div class="td">
            {{ m.amortissements }}
          </div>
          <div class="td td-net">
            {{ m.net }}
          </div>
          <!-- une ligne parmi d'autres -->
          <div class="suite">
            <i class="fantome demi" />
            <i class="fantome d" />
            <i class="fantome d" />
            <i class="fantome d" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
