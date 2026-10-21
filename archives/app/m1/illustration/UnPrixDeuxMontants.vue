<script setup>
/* m1/illustration/UnPrixDeuxMontants.vue — Chapitre 5, « La TVA ».
   Portée depuis illustration-prix-ttc.html.

   C'est une illustration, pas une activité : aucun geste, aucun amber,
   slate seul. Les styles vivent dans illustrations.css, sous .illustration.

   Deux lectures du même prix, sur la même longueur et à l'échelle : le client
   voit 12 € d'un bloc, Latitude Café y lit 10 € + 2 €. Ici le partage est le
   sujet — avec le Chapitre 7, le seul cas où couper un montant est juste.
   Ni « TVA collectée », ni taux, ni document : le texte ne les a pas encore
   posés à cet endroit. */

/* Les données de la scène, en un seul endroit. Si elles doivent un jour venir
   d'un store, c'est cet objet seul qui change. */
const scene = {
  quand: 'Un sachet de café, au comptoir',
  ht: 10, // le prix du café
  taxe: 2, // reçue pour l'État
}
const ttc = scene.ht + scene.taxe

/* Les deux pistes de la grille portent les montants eux-mêmes : la
   proportion est exacte. */
const parts = { '--parts': `${scene.ht}fr ${scene.taxe}fr` }

/* formatEuros() : shared/utils/formatEuros.ts, auto-importé par Nuxt. */
const montants = {
  ttc: formatEuros(ttc),
  ht: formatEuros(scene.ht),
  taxe: formatEuros(scene.taxe),
}

/* L'équivalent du « alt » : il décrit ce qu'on voit, la légende du chapitre
   tire la leçon. */
const alt = `${scene.quand}. Le client voit un prix : une barre de ${montants.ttc} `
  + `toutes taxes comprises. Latitude Café lit deux montants sur la même longueur : `
  + `${montants.ht} hors taxes, le prix de son café, qui vont pour Latitude Café, `
  + `et ${montants.taxe} de taxe, qui vont pour l'État.`
</script>

<template>
  <div
    class="illustration un-prix-deux-montants"
    role="img"
    :aria-label="alt"
  >
    <div aria-hidden="true">
      <div class="quand">
        {{ scene.quand }}
      </div>

      <div
        class="schema"
        :style="parts"
      >
        <div class="qui q1">
          Le client<span>voit un prix</span>
        </div>
        <div class="barre ttc">
          <div class="barre-m">
            {{ montants.ttc }}
          </div>
          <div class="barre-n">
            toutes taxes comprises
          </div>
        </div>

        <!-- entre les deux barres : même longueur, rien d'ajouté -->
        <div class="meme">
          <i /><i />
        </div>

        <div class="qui q2">
          Latitude Café<span>lit deux montants</span>
        </div>
        <div class="barre ht">
          <div class="barre-m">
            {{ montants.ht }}
          </div>
          <div class="barre-n">
            hors taxes, le prix de son café
          </div>
        </div>
        <div class="barre taxe">
          <div class="barre-m">
            {{ montants.taxe }}
          </div>
          <div class="barre-n">
            de taxe
          </div>
        </div>

        <!-- sous la seconde barre, où va chaque part -->
        <div class="dest d-ht">
          <span>pour Latitude Café</span>
        </div>
        <div class="dest d-taxe">
          <span>pour l’État</span>
        </div>
      </div>
    </div>
  </div>
</template>
