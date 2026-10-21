<script setup>
/* m1/illustration/UneMensualiteDeuxParts.vue — Chapitre 7, « Se financer »,
   second emplacement, à la place de l'ancien <MensualiteDecomposee />.
   Portée depuis illustration-mensualite.html.

   C'est une illustration, pas une activité : aucun geste, aucun amber,
   slate seul. Les styles vivent dans illustrations.css, sous .illustration.

   Elle illustre la déclaration « Rembourser une dette n'appauvrit pas une
   entreprise ». Une sortie du compte, deux parts : les intérêts vont au
   Compte de Résultat et n'y laissent rien au Bilan ; le capital se lit au
   Bilan des deux côtés à la fois. Actif et Passif restent côte à côte à
   toutes les largeurs : les deux baisses qui se font face sont la
   démonstration. */

/* Les données de la scène, en un seul endroit. Si elles doivent un jour venir
   d'un store, c'est cet objet seul qui change. Échéance du 30 juin. */
const scene = {
  date: '30\u00a0juin',
  interets: 87.5, // charges d'intérêts
  capital: 541.4, // remboursement du capital emprunté
}

/* Une seule sortie : la somme des deux parts. */
const mensualite = scene.interets + scene.capital

/* formatEuros() : shared/utils/formatEuros.ts, auto-importé par Nuxt. */
const montants = {
  mensualite: formatEuros(mensualite, 2),
  interets: formatEuros(scene.interets, 2),
  capital: formatEuros(scene.capital, 2),
  baisse: formatEuros(-scene.capital, 2),
}

/* L'équivalent du « alt » : il décrit ce qu'on voit, la légende du chapitre
   tire la leçon. */
const alt = `${montants.mensualite}, une seule sortie du compte, le ${scene.date}, `
  + `partagée en deux. ${montants.interets}, les intérêts, vont au Compte de Résultat : `
  + `charges d'intérêts, plus ${montants.interets} ; rien au Bilan n'en garde la trace, `
  + `le service est consommé. ${montants.capital}, le remboursement du capital, va au Bilan, `
  + `des deux côtés : à l'Actif, le compte en banque, ${montants.baisse} ; au Passif, la dette `
  + `envers la banque, ${montants.baisse}. Les deux descendent du même montant. `
  + `Moins d'argent, moins de dettes : ce que l'entreprise vaut n'a pas bougé.`
</script>

<template>
  <div
    class="illustration une-mensualite-deux-parts"
    role="img"
    :aria-label="alt"
  >
    <div aria-hidden="true">
      <!-- la sortie unique -->
      <div class="sortie">
        <div class="sortie-montant">
          {{ montants.mensualite }}
        </div>
        <div class="sortie-lib">
          une seule sortie du compte, le {{ scene.date }}
        </div>
      </div>

      <!-- la fourche : un tronc, puis deux branches (le tronc seul en étroit) -->
      <div class="fourche">
        <span class="tronc" />
        <span class="branches" />
      </div>

      <div class="parts">
        <!-- les intérêts -->
        <div class="part">
          <div class="part-montant">
            {{ montants.interets }}
          </div>
          <div class="part-nom">
            les intérêts
          </div>
          <span class="fleche-bas" />
          <div class="document">
            <div class="document-titre">
              Compte de Résultat
            </div>
            <div class="cr-ligne">
              <span class="cr-lib">Charges d’intérêts</span>
              <span class="cr-val">+&nbsp;{{ montants.interets }}</span>
            </div>
            <div class="trace">
              Rien au Bilan n’en garde la trace.<br>Le service est consommé.
            </div>
          </div>
        </div>

        <!-- le capital -->
        <div class="part">
          <div class="part-montant">
            {{ montants.capital }}
          </div>
          <div class="part-nom">
            le remboursement du capital
          </div>
          <span class="fleche-bas" />
          <div class="document">
            <div class="document-titre">
              Bilan
            </div>
            <div class="colonnes">
              <div class="colonne">
                <div class="colonne-titre">
                  Actif
                </div>
                <div class="cote-lib">
                  Le compte en banque
                </div>
                <div class="cote-val">
                  {{ montants.baisse }}
                </div>
              </div>
              <div class="colonne">
                <div class="colonne-titre">
                  Passif
                </div>
                <div class="cote-lib">
                  La dette envers la banque
                </div>
                <div class="cote-val">
                  {{ montants.baisse }}
                </div>
              </div>
            </div>
            <div class="meme">
              <span>les deux descendent du même montant</span>
            </div>
            <div class="chute">
              Moins d’argent, moins de dettes.<br>Ce que l’entreprise vaut n’a pas bougé.
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
