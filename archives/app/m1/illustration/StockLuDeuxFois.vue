<script setup>
/* m1/illustration/StockLuDeuxFois.vue — Chapitre 6, « Produire et stocker ».
   Portée depuis illustration-stock.html.

   C'est une illustration, pas une activité : aucun geste, aucun amber,
   slate seul. Les styles vivent dans illustrations.css, sous .illustration.

   Le miroir du Chapitre 4 : au centre, non pas un document mais l'objet
   lui-même, l'étagère de sachets ; une flèche vers chaque document. Les
   côtés sont inversés par rapport au Chapitre 4 (Bilan à gauche) : c'est la
   légende qui commande. */

/* Les données de la scène, en un seul endroit. Si elles doivent un jour venir
   d'un store, c'est cet objet seul qui change. */
const scene = {
  quand: 'Fin avril',
  montant: 15000, // stock-prod-355d / stock-prod-7135c
  planches: 2,
  sachetsParPlanche: 5,
}

/* formatEuros() : shared/utils/formatEuros.ts, auto-importé par Nuxt. */
const stock = formatEuros(scene.montant)

/* L'équivalent du « alt » : il décrit ce qu'on voit, la légende du chapitre
   tire la leçon. */
const alt = `${scene.quand}, une étagère de sachets de café torréfié pas encore vendu, `
  + `${stock}, renvoie vers deux documents. `
  + `Au Bilan, à l'actif : Stock de café torréfié, ${stock}, puis Trésorerie, plus 0 €. `
  + `Au Compte de Résultat, en produits, sous une ligne déjà présente : `
  + `Variation de stock, ${stock}.`
</script>

<template>
  <div
    class="illustration stock-lu-deux-fois"
    role="img"
    :aria-label="alt"
  >
    <div aria-hidden="true">
      <div class="quand">
        {{ scene.quand }}
      </div>

      <div class="scene">
        <div class="document">
          <div class="document-titre">
            Bilan
          </div>
          <div class="colonnes">
            <div class="colonne">
              <div class="colonne-titre">
                Actif
              </div>
              <div class="ligne">
                <div class="ligne-lib">
                  Stock de café torréfié
                </div>
                <div class="ligne-val">
                  {{ stock }}
                </div>
              </div>
              <!-- « + 0 € » est la leçon : même encre, seul le trait change -->
              <div class="ligne pas-encore">
                <div class="ligne-lib">
                  Trésorerie
                </div>
                <div class="ligne-val">
                  +&nbsp;0&nbsp;€
                </div>
              </div>
            </div>
            <div class="colonne">
              <div class="colonne-titre">
                Passif
              </div>
              <i class="fantome" />
              <i class="fantome court" />
            </div>
          </div>
        </div>

        <span class="fleche gauche" />

        <!-- le stock : une étagère de sachets, pas un document -->
        <div class="etagere">
          <div
            v-for="p in scene.planches"
            :key="p"
            class="planche"
          >
            <span
              v-for="s in scene.sachetsParPlanche"
              :key="s"
              class="sachet"
            />
          </div>
          <div class="etagere-nom">
            Café torréfié,<br>
            pas encore vendu
          </div>
          <div class="etagere-val">
            {{ stock }}
          </div>
        </div>

        <span class="fleche droite" />

        <div class="document">
          <div class="document-titre">
            Compte de Résultat
          </div>
          <div class="colonnes">
            <div class="colonne">
              <div class="colonne-titre">
                Charges
              </div>
              <i class="fantome" />
              <i class="fantome court" />
            </div>
            <div class="colonne">
              <div class="colonne-titre">
                Produits
              </div>
              <!-- les ventes déjà là -->
              <i class="fantome" />
              <div class="ligne">
                <div class="ligne-lib">
                  Variation de stock
                </div>
                <div class="ligne-val">
                  {{ stock }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
