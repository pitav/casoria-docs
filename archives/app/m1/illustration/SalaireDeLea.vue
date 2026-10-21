<script setup>
/* m1/illustration/SalaireDeLea.vue — Chapitre 9, « Les salariés ».
   Portée depuis illustration-cout-employeur.html.

   C'est une illustration, pas une activité : aucun geste, aucun amber,
   slate seul. Les styles vivent dans illustrations.css, sous .illustration.
   (Le composant <CoutEmployeur /> a été écarté par la règle 0 : les nombres
   sont tous dans le texte. D'où un autre nom ici.)

   Une seule barre à l'échelle, trois accolades qui la lisent à trois
   endroits. Les charges salariales sont sous deux accolades à la fois,
   dans le contrat et chez les organismes : c'est ce que l'image montre et
   que la prose ne montre pas. */

/* Les données de la scène, en un seul endroit. Si elles doivent un jour venir
   d'un store, c'est cet objet seul qui change. Les trois totaux se calculent. */
const scene = {
  quand: 'Le salaire de Léa, pour un mois',
  net: 1716, // ce que Léa reçoit
  salariales: 484,
  patronales: 924,
}
const brut = scene.net + scene.salariales // 2 200, au contrat
const total = brut + scene.patronales // 3 124, le coût employeur
const organismes = scene.salariales + scene.patronales // 1 408

/* Les trois pistes portent les montants eux-mêmes : la proportion est
   exacte, en colonnes en large, en rangées en étroit. */
const parts = { '--parts': `${scene.net}fr ${scene.salariales}fr ${scene.patronales}fr` }

/* formatEuros() : shared/utils/formatEuros.ts, auto-importé par Nuxt. */
const m = {
  net: formatEuros(scene.net),
  salariales: formatEuros(scene.salariales),
  patronales: formatEuros(scene.patronales),
  brut: formatEuros(brut),
  total: formatEuros(total),
  organismes: formatEuros(organismes),
}

/* L'équivalent du « alt » : il décrit ce qu'on voit, la légende du chapitre
   tire la leçon. */
const alt = `${scene.quand} : une barre à l'échelle en trois parts. `
  + `${m.net}, le salaire net, ce que Léa reçoit ; ${m.salariales} de charges salariales ; `
  + `${m.patronales} de charges patronales. Au-dessus, une accolade sur toute la barre : `
  + `${m.total}, le coût total employeur, ce que Latitude Café paie ; une autre sur les deux `
  + `premières parts : ${m.brut}, le salaire brut, écrit au contrat. En dessous, une accolade `
  + `sur les deux dernières : ${m.organismes} partent aux organismes sociaux ; `
  + `l'entreprise n'en garde rien.`
</script>

<template>
  <div
    class="illustration salaire-de-lea"
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
        <div class="acc acc-haut acc-total">
          <div class="acc-txt">
            <b>{{ m.total }}</b>
            <span>le coût total employeur, ce que Latitude Café paie</span>
          </div>
          <div class="acc-trait" />
        </div>

        <div class="acc acc-haut acc-contrat">
          <div class="acc-txt">
            <b>{{ m.brut }}</b>
            <span>le salaire brut, écrit au contrat</span>
          </div>
          <div class="acc-trait" />
        </div>

        <div class="seg seg-net">
          <div class="seg-m">
            {{ m.net }}
          </div>
          <div class="seg-lab">
            <strong>salaire net</strong><br>ce que Léa reçoit
          </div>
        </div>
        <div class="seg seg-sal">
          <div class="seg-m">
            {{ m.salariales }}
          </div>
          <div class="seg-lab">
            <strong>charges salariales</strong>
          </div>
        </div>
        <div class="seg seg-pat">
          <div class="seg-m">
            {{ m.patronales }}
          </div>
          <div class="seg-lab">
            <strong>charges patronales</strong>
          </div>
        </div>

        <div class="acc acc-bas acc-org">
          <div class="acc-trait" />
          <div class="acc-txt">
            <b>{{ m.organismes }}</b>
            <span>partent aux organismes sociaux</span>
            <em>L’entreprise n’en garde rien.</em>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
