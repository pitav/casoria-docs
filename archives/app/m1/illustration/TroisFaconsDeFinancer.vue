<script setup>
/* m1/illustration/TroisFaconsDeFinancer.vue — Chapitre 7, « Se financer »,
   premier emplacement (« Trois sources d'argent, et trois seulement »).
   Portée depuis illustration-trois-sources.html.

   C'est une illustration, pas une activité : aucun geste, aucun amber,
   slate seul. Les styles vivent dans illustrations.css, sous .illustration.

   Trois sources en colonnes, trois lectures en rangées, les intitulés de
   rangée écrits une seule fois. Les jauges n'ont pas de chiffre : c'est un
   ordre, pas une mesure — et elles montent ensemble sur les deux rangées,
   comme le dit la légende. Aucun montant : la trésorerie disponible serait un
   nombre neuf, et les 35 000 € arrivent au paragraphe suivant.

   Icônes : Material Design Icons (licence Apache 2.0), par <UIcon /> de
   Nuxt UI. Leur taille suit la taille de police (1em). */

/* Les données de la scène, en un seul endroit. Si elles doivent un jour venir
   d'un store, c'est cet objet seul qui change. recoit et engage : nombre de
   marches allumées sur trois. */
const scene = {
  titre: 'Trois façons de financer le torréfacteur',
  marches: 3,
  sources: [
    { nom: 'Sa trésorerie', icone: 'i-mdi-cash-multiple', recoit: 1, engage: 1, rembourse: 'jamais' },
    { nom: 'Un associé', icone: 'i-mdi-account-tie', recoit: 2, engage: 2, rembourse: 'quand elle le peut' },
    { nom: 'Une banque', icone: 'i-mdi-bank', recoit: 3, engage: 3, rembourse: 'à dates fixes, avec intérêts' },
  ],
}

/* Les rangées : un intitulé en deux morceaux (deux lignes en large, une en
   étroit), et ce que chaque cellule montre. */
const rangees = [
  { lib: ['Ce qu’elle', 'reçoit'], cle: 'recoit', jauge: true },
  { lib: ['Ce qui', 'l’engage'], cle: 'engage', jauge: true },
  { lib: ['Se', 'rembourse'], cle: 'rembourse', jauge: false },
]

/* L'équivalent du « alt » : il décrit ce qu'on voit, la légende du chapitre
   tire la leçon. */
const [tresorerie, associe, banque] = scene.sources
const marches = n => (n === 1 ? 'une marche' : n === 2 ? 'deux marches' : 'trois marches')
const alt = `${scene.titre}, en trois colonnes : ${scene.sources.map(s => s.nom.toLowerCase()).join(', ')}. `
  + `Ce qu'elle reçoit et ce qui l'engage, en jauges de ${scene.marches} marches sans chiffre, `
  + `identiques sur les deux rangées : ${marches(tresorerie.recoit)} pour la trésorerie, `
  + `${marches(associe.recoit)} pour l'associé, ${marches(banque.recoit)} pour la banque. `
  + `Se rembourse : ${scene.sources.map(s => s.rembourse).join(' ; ')}. `
  + `Une flèche, sous les trois colonnes, va de gauche à droite.`
</script>

<template>
  <div
    class="illustration trois-facons-de-financer"
    role="img"
    :aria-label="alt"
  >
    <div aria-hidden="true">
      <div class="quand">
        {{ scene.titre }}
      </div>

      <div class="tableau">
        <!-- en tête : les trois sources -->
        <div
          v-for="(s, i) in scene.sources"
          :key="s.nom"
          class="source"
          :class="`c${i + 1}`"
        >
          <UIcon
            :name="s.icone"
            class="source-icone"
          />
          <div class="source-nom">
            {{ s.nom }}
          </div>
        </div>

        <!-- les trois rangées -->
        <template
          v-for="(r, j) in rangees"
          :key="r.cle"
        >
          <div
            class="intitule"
            :class="`r${j + 1}`"
          >
            <span>{{ r.lib[0] }}</span> <span>{{ r.lib[1] }}</span>
          </div>
          <div
            v-for="(s, i) in scene.sources"
            :key="s.nom"
            class="cellule"
            :class="[`c${i + 1}`, `r${j + 1}`]"
          >
            <span
              v-if="r.jauge"
              class="jauge"
            >
              <i
                v-for="m in scene.marches"
                :key="m"
                :class="{ allumee: m <= s[r.cle] }"
              />
            </span>
            <span
              v-else
              class="reponse"
            >{{ s[r.cle] }}</span>
          </div>
        </template>

        <!-- sous le tout, le sens de lecture -->
        <div class="sens fleche droite" />
      </div>
    </div>
  </div>
</template>
