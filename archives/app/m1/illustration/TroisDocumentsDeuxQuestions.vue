<script setup>
/* m1/illustration/TroisDocumentsDeuxQuestions.vue — Chapitre 3, « Lire un
   document ». Portée depuis illustration-trois-documents.html (v2).

   C'est une illustration, pas une activité : aucun geste, aucun amber,
   slate seul. Les styles vivent dans illustrations.css, sous .illustration.

   Trois papiers de formes différentes, deux questions écrites une seule
   fois, en tête de rangée. Sous chaque papier, la réponse seule, en trois ou
   quatre mots : « Sur le compte » face à « Du compte » montre le sens qui
   s'inverse sans le dire. Ni débit, ni crédit, ni Bilan : le Chapitre 3 lit
   un document, <EcritureDragDrop /> choisit une colonne. */

/* Les données de la scène, en un seul endroit. Si elles doivent un jour venir
   d'un store, c'est cet objet seul qui change. Les montants sont ceux des
   écritures du chapitre qui suivent l'image. */
const scene = {
  ticket: {
    enseigne: 'Latitude Café',
    lieu: 'Comptoir',
    date: 'samedi 17\u00a0janvier',
    montant: 320, // ventes du samedi 17 janvier
    va: 'Sur le compte',
    vient: 'Des ventes du jour',
  },
  cafeVert: {
    emetteur: 'Verdecafé',
    destinataire: 'à Latitude Café · janvier',
    article: 'Café vert', // suivi de « 1er lot » dans le dessin
    montant: 1800, // premier lot de café vert
    va: 'Dans le café vert',
    vient: 'Du compte',
  },
  electricite: {
    periode: 'Consommation · janvier',
    montant: 240, // électricité de janvier
    va: 'Dans l’électricité',
    vient: 'Du compte',
  },
}

/* Le dessin seul : longueur des lignes muettes du ticket et de la facture,
   hauteur des barres de consommation (la dernière est le mois facturé). */
const dessin = {
  ticket: [86, 70, 80, 60],
  facture: [74, 52],
  consommation: [40, 55, 35, 60, 45, 85],
}

/* formatEuros() : shared/utils/formatEuros.ts, auto-importé par Nuxt. */
/* L'équivalent du « alt » : il décrit ce qu'on voit, la légende du chapitre
   tire la leçon. */
const { ticket, cafeVert, electricite } = scene
const alt = `Un ticket de caisse de ${formatEuros(ticket.montant)}, une facture de café vert `
  + `de ${formatEuros(cafeVert.montant)} et une facture d'électricité de `
  + `${formatEuros(electricite.montant)}. Pour le ticket, la valeur va sur le compte et `
  + `vient des ventes du jour. Pour les deux factures, elle va dans le café vert ou dans `
  + `l'électricité, et vient du compte.`
</script>

<template>
  <div
    class="illustration trois-documents-deux-questions"
    role="img"
    :aria-label="alt"
  >
    <!-- une grille : les questions en tête de rangée (en tête de colonne en
         étroit), un papier et ses deux réponses par colonne (par rangée) -->
    <div
      class="tableau"
      aria-hidden="true"
    >
      <div class="question question-va">
        <span>Où va la<br> valeur&nbsp;?</span>
      </div>
      <div class="question question-vient">
        <span>D’où<br> vient-elle&nbsp;?</span>
      </div>

      <!-- le ticket : étroit, bord bas dentelé -->
      <div class="document-col p1">
        <div class="zone">
          <div class="papier ticket">
            <div class="ticket-enseigne">
              {{ ticket.enseigne }}
            </div>
            <div class="ticket-type">
              Ticket de caisse
            </div>
            <div class="ticket-sous">
              {{ ticket.lieu }}<br>{{ ticket.date }}
            </div>
            <div class="pointilles" />
            <span
              v-for="(l, k) in dessin.ticket"
              :key="k"
              class="fantome"
              :style="{ width: `${l}%` }"
            />
            <div class="pointilles" />
            <div class="ticket-total">
              <span>Total</span>
              <span class="montant">{{ formatEuros(ticket.montant, 2) }}</span>
            </div>
          </div>
        </div>
        <div class="reponse va">
          {{ ticket.va }}
        </div>
        <div class="reponse vient">
          {{ ticket.vient }}
        </div>
      </div>

      <!-- la facture du grossiste : un en-tête, un tableau -->
      <div class="document-col p2">
        <div class="zone">
          <div class="papier facture">
            <div class="facture-haut">
              <span class="facture-emet">{{ cafeVert.emetteur }}</span>
              <span class="facture-type">Facture</span>
            </div>
            <div class="facture-dest">
              {{ cafeVert.destinataire }}
            </div>
            <div class="facture-ligne">
              <span>{{ cafeVert.article }}, 1<sup>er</sup> lot</span>
              <span class="montant">{{ formatEuros(cafeVert.montant, 2) }}</span>
            </div>
            <span
              v-for="(l, k) in dessin.facture"
              :key="k"
              class="fantome"
              :style="{ width: `${l}%` }"
            />
            <div class="papier-total">
              <span>Total</span>
              <b class="montant">{{ formatEuros(cafeVert.montant, 2) }}</b>
            </div>
          </div>
        </div>
        <div class="reponse va">
          {{ cafeVert.va }}
        </div>
        <div class="reponse vient">
          {{ cafeVert.vient }}
        </div>
      </div>

      <!-- la facture d'électricité : un bandeau, un graphique -->
      <div class="document-col p3">
        <div class="zone">
          <div class="papier electricite">
            <div class="electricite-bandeau">
              Facture d’électricité
            </div>
            <div class="electricite-corps">
              <div class="electricite-periode">
                {{ electricite.periode }}
              </div>
              <div class="barres">
                <i
                  v-for="(h, k) in dessin.consommation"
                  :key="k"
                  :style="{ height: `${h}%` }"
                />
              </div>
              <div class="papier-total">
                <span>À payer</span>
                <b class="montant">{{ formatEuros(electricite.montant, 2) }}</b>
              </div>
            </div>
          </div>
        </div>
        <div class="reponse va">
          {{ electricite.va }}
        </div>
        <div class="reponse vient">
          {{ electricite.vient }}
        </div>
      </div>
    </div>
  </div>
</template>
