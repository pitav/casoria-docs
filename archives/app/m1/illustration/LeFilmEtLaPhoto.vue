<script setup>
/* m1/illustration/LeFilmEtLaPhoto.vue — Chapitre 1, « Le Bilan et le Compte
   de Résultat ». Portée depuis illustration-film-photo-b.html (version B).

   C'est une illustration, pas une activité : aucun geste, aucun amber,
   slate seul. Les styles vivent dans illustrations.css, sous .illustration.

   La même année, deux règles de douze mois : le film la remplit, la photo
   n'en garde que le dernier soir. Les documents restent des squelettes —
   aucun élément, aucun montant : ranger des exemples donnerait les réponses
   de <TriActifPassif />, plus loin dans le chapitre. L'axe de l'image est le
   temps. */

/* Les données de la scène, en un seul endroit. Si elles doivent un jour venir
   d'un store, c'est cet objet seul qui change. */
const scene = {
  mois: ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'],
  vise: { index: 5, nom: 'juin' }, // le mois qu'on suit d'un panneau à l'autre
  film: {
    sur: 'Le film',
    nom: 'Le Compte de Résultat',
    date: 'du 5\u00a0janvier au 31\u00a0décembre',
    colonnes: ['Charges', 'Produits'],
  },
  photo: {
    sur: 'La photo',
    nom: 'Le Bilan',
    date: 'le 31\u00a0décembre, le soir',
    colonnes: ['Actif', 'Passif'],
  },
}

/* sorte : plein = toute la règle est remplie ; vide = seul un trait au bout.
   fantomes : largeur des lignes muettes de chaque colonne (la seconde est plus
   courte, comme dans la source). */
const panneaux = [
  { ...scene.film, sorte: 'plein',
    dit: 'Toute l’année est filmée', note: `${scene.vise.nom} en fait partie` },
  { ...scene.photo, sorte: 'vide',
    dit: 'Seul le dernier soir', note: `${scene.vise.nom} n’y figure pas` },
]
const fantomes = [
  ['', 'court', 'l65', 'l90'],
  ['', 'court', 'l65'],
]

/* L'équivalent du « alt » : il décrit ce qu'on voit, la légende du chapitre
   tire la leçon. */
const [film, photo] = panneaux
const alt = `Deux panneaux. ${film.sur}, ${film.nom}, ${film.date} : une règle de douze mois `
  + `entièrement remplie, ${scene.vise.nom} plus foncé. ${film.dit}, ${film.note}. `
  + `En dessous, deux colonnes vides, ${film.colonnes.join(' et ')}. `
  + `${photo.sur}, ${photo.nom}, ${photo.date} : la même règle de douze mois, vide, `
  + `${scene.vise.nom} en pointillé, un seul trait au bout de décembre. `
  + `${photo.dit}, ${photo.note}. En dessous, deux colonnes vides, ${photo.colonnes.join(' et ')}.`
</script>

<template>
  <div
    class="illustration le-film-et-la-photo"
    role="img"
    :aria-label="alt"
  >
    <div
      class="panneaux"
      aria-hidden="true"
    >
      <div
        v-for="p in panneaux"
        :key="p.sorte"
        class="pan"
      >
        <div class="pan-sur">
          {{ p.sur }}
        </div>
        <div class="pan-nom">
          {{ p.nom }}
        </div>
        <div class="pan-date">
          {{ p.date }}
        </div>

        <!-- la règle de douze mois ; sur la photo, l'instant est un trait au bout -->
        <div
          class="regle"
          :class="p.sorte"
        >
          <span
            v-for="(m, i) in scene.mois"
            :key="i"
            class="mois"
            :class="{ vise: i === scene.vise.index }"
          />
          <span
            v-if="p.sorte === 'vide'"
            class="instant"
          />
        </div>
        <div class="lettres">
          <span
            v-for="(m, i) in scene.mois"
            :key="i"
            :class="{ vise: i === scene.vise.index }"
          >{{ m }}</span>
        </div>

        <div class="dit">
          <b>{{ p.dit }}</b>
          <span>{{ p.note }}</span>
        </div>

        <!-- le squelette du document : deux colonnes, aucun contenu -->
        <div class="colonnes">
          <div
            v-for="(c, j) in p.colonnes"
            :key="c"
            class="colonne"
          >
            <div class="colonne-titre">
              {{ c }}
            </div>
            <span
              v-for="(f, k) in fantomes[j]"
              :key="k"
              class="fantome"
              :class="f"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
