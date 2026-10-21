<script setup>
/* m1/illustration/VenteAEcheance.vue — Chapitre 4, « Une facture n'est pas
   un encaissement ». Portée depuis illustration-vente-a-echeance.html.

   C'est une illustration, pas une activité : aucun geste, aucun amber,
   slate seul. Les styles vivent dans illustrations.css, sous .illustration.

   La facture au milieu, une flèche vers chaque document. Pas de fourche : une
   fourche partage un montant (c'est le sens qu'elle a au Chapitre 7), ici la
   vente est lue deux fois. */

/* Les données de la scène, en un seul endroit. Si elles doivent un jour venir
   d'un store, c'est cet objet seul qui change. */
const scene = {
  date: '28 janvier',
  emetteur: 'Latitude Café',
  client: 'Le Comptoir des Halles',
  montant: 1450, // fact-vente-701c / fact-vente-411d
  delai: 30, // jours
}

/* formatEuros() : shared/utils/formatEuros.ts, auto-importé par Nuxt. */
const vente = formatEuros(scene.montant)
const facture = formatEuros(scene.montant, 2)
const creance = formatEuros(scene.montant)
const echeance = `${scene.delai} jours`

/* L'équivalent du « alt » : l'image est lue d'un bloc. Le détail interne est
   masqué, lu dans l'ordre du DOM il serait décousu.
   Il décrit ce qu'on voit, sans tirer la leçon : c'est le rôle de la légende
   du chapitre, que le lecteur d'écran lit juste après. */
const alt = `Le ${scene.date} au soir, la facture de ${scene.emetteur} `
  + `au ${scene.client.replace(/^Le /, '')}, ${facture} à payer sous ${echeance}, `
  + `renvoie vers deux documents. `
  + `Au Compte de Résultat, en produits : Ventes aux professionnels, ${vente}. `
  + `Au Bilan, à l'actif : Créances clients, ${creance}, puis, `
  + `avec la mention « dans ${echeance} », Trésorerie, plus 0 €.`
</script>

<template>
  <div
    class="illustration vente-a-echeance"
    role="img"
    :aria-label="alt"
  >
    <div aria-hidden="true">
      <div class="quand">
        Le {{ scene.date }} au soir
      </div>

      <div class="scene">
        <!-- Ordre du DOM gardé pour l'étroit : documents et facture se
             réordonneront par `order`, sans toucher au gabarit. -->
        <div class="document document-g">
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
              <div class="ligne">
                <div class="ligne-lib">
                  Ventes aux professionnels
                </div>
                <div class="ligne-val">
                  {{ vente }}
                </div>
              </div>
            </div>
          </div>
        </div>

        <span class="fleche gauche" />

        <div class="facture">
          <div class="facture-haut">
            <span class="facture-emet">{{ scene.emetteur }}</span>
            <span class="facture-type">Facture</span>
          </div>
          <div class="facture-dest">
            <b>{{ scene.client }}</b>
            {{ scene.date }}
          </div>
          <i class="fantome l90" />
          <i class="fantome l65" />
          <div class="facture-tot">
            {{ facture }}
          </div>
          <div class="facture-ech">
            à payer sous {{ echeance }}
          </div>
        </div>

        <span class="fleche droite" />

        <div class="document document-d">
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
                  Créances clients
                </div>
                <div class="ligne-val">
                  {{ creance }}
                </div>
              </div>
              <!-- ce qui n'est pas encore de l'argent : la trésorerie attend -->
              <div class="attente">
                dans {{ echeance }}
              </div>
              <!-- « + 0 € » est la leçon : même encre que la ligne du dessus,
                   seul le trait change (pointillé contre plein) -->
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
      </div>
    </div>
  </div>
</template>
