<script setup lang="ts">
/**
 * Le Bilan et le Compte de Résultat du module, en saisie (déroulé v28, sections 2 et 4).
 *
 * - Deux tableaux par document, un par côté : caption, en-têtes de colonne lus par le lecteur
 *   d'écran, nom du compte en <th scope="row">, total en <tfoot>.
 * - Saisie à la ligne : un clic sur la ligne (ou sur son bouton, au clavier) ouvre un UPopover qui ne
 *   demande que le montant. Ni débit ni crédit dans la grille. Une saisie fausse est refusée.
 * - Les totaux se calculent, ils ne se saisissent jamais. Seuls ceux du Bilan portent une couleur
 *   (slate tant qu'ils diffèrent, lime quand ils sont égaux, signe ≠ / =).
 * - Un nombre qui change est chassé par le nouveau ; jamais de compteur.
 *
 * Le grand journal n'est pas ici : une ligne de consigne sur 4456 ou 4457 est ignorée par ce
 * composant (ces deux comptes n'ont pas de case dans la grille).
 */

type Col = 'débit' | 'crédit'
/** Une ligne de consigne, au format de gdJal : montant positif, colonne du journal. */
interface LigneConsigne { id?: string, cpt: string, somme: number, col: Col }
/** Une écriture enregistrée : `somme` est l'effet sur la case, positif si la case monte. */
interface Ecriture { cpt: string, somme: number, timestamp: number }
type Cote = 'actif' | 'passif' | 'charges' | 'produits'

const props = withDefaults(defineProps<{
  /** Les lignes du bloc en cours. Vide : rien à saisir, les lignes remplies restent consultables. */
  consigne?: LigneConsigne[]
}>(), { consigne: () => [] })

const emit = defineEmits<{ termine: [] }>()

// ─── La grille (déroulé, section 2) ─────────────────────────────────────────
const grille: Record<Cote, { cpt: string, nom: string, prec?: string }[]> = {
  actif: [
    { cpt: '215', nom: 'Immobilisations corporelles', prec: 'Torréfacteur' },
    { cpt: '2815', nom: 'Amortissements des immobilisations', prec: 'Torréfacteur' },
    { cpt: '355', nom: 'Stocks', prec: 'Café torréfié' },
    { cpt: '411', nom: 'Créances clients' },
    { cpt: '486', nom: 'Charges constatées d\'avance' },
    { cpt: '512', nom: 'Banque', prec: 'Trésorerie' }
  ],
  passif: [
    { cpt: '101', nom: 'Capital social' },
    { cpt: '120', nom: 'Résultat de l\'exercice' },
    { cpt: '455', nom: 'Compte courant d\'associé' },
    { cpt: '164', nom: 'Emprunt bancaire' },
    { cpt: '151', nom: 'Provisions pour risques', prec: 'Risque client' },
    { cpt: '401', nom: 'Dettes fournisseurs' },
    { cpt: '431', nom: 'Dettes sociales' },
    { cpt: '4455', nom: 'État — TVA à décaisser' },
    { cpt: '444', nom: 'État — IS à payer' },
    { cpt: '487', nom: 'Produits constatés d\'avance' }
  ],
  charges: [
    { cpt: '601', nom: 'Achats de matières premières', prec: 'Café vert' },
    { cpt: '615', nom: 'Autres charges externes' },
    { cpt: '641', nom: 'Salaires bruts' },
    { cpt: '645', nom: 'Charges sociales patronales' },
    { cpt: '6811', nom: 'Dotation aux amortissements' },
    { cpt: '6815', nom: 'Dotation aux provisions' },
    { cpt: '661', nom: 'Charges d\'intérêts' }
  ],
  produits: [
    { cpt: '701', nom: 'Ventes de produits finis', prec: 'Ventes aux professionnels' },
    { cpt: '707', nom: 'Ventes de marchandises', prec: 'Ventes au comptoir' },
    { cpt: '7135', nom: 'Variation des stocks', prec: 'Café torréfié' }
  ]
}

const documents = [
  { cle: 'bilan', titre: 'Bilan', cotes: [
    { cle: 'actif' as Cote, titre: 'Actif', total: 'Total actif' },
    { cle: 'passif' as Cote, titre: 'Passif', total: 'Total passif' }
  ] },
  { cle: 'cr', titre: 'Compte de Résultat', cotes: [
    { cle: 'charges' as Cote, titre: 'Charges', total: 'Total charges' },
    { cle: 'produits' as Cote, titre: 'Produits', total: 'Total produits' }
  ] }
]

const COTES: Cote[] = ['actif', 'passif', 'charges', 'produits']
const coteDe: Record<string, Cote> = {}
for (const k of COTES) for (const l of grille[k]) coteDe[l.cpt] = k

// ─── Les écritures enregistrées ─────────────────────────────────────────────
const bilanCr = reactive<Ecriture[]>([])

function enregistrer(cpt: string, somme: number) {
  bilanCr.push({ cpt, somme, timestamp: Date.now() })
}

/** Ce qu'une ligne de consigne fait à sa case : l'actif et les charges montent au débit, le passif et les produits au crédit. */
function effet(l: LigneConsigne) {
  const cote = coteDe[l.cpt]
  const monteAuDebit = cote === 'actif' || cote === 'charges'
  return (monteAuDebit === (l.col === 'débit')) ? l.somme : -l.somme
}

const cents = (m: number) => Math.round(m * 100) / 100
const decimales = (m: number) => (Number.isInteger(cents(m)) ? 0 : 2)
const euros = (m: number) => formatEuros(m, decimales(m))
/** Une hausse porte son « + » ; une baisse, le « − » de formatEuros. */
const signe = (m: number) => (m > 0 ? '+\u00a0' + euros(m) : euros(m))

const soldes = computed(() => {
  const s: Record<string, number> = {}
  for (const e of bilanCr) s[e.cpt] = cents((s[e.cpt] ?? 0) + e.somme)
  return s
})
const inscrit = (cpt: string) => cpt in soldes.value

const totaux = computed(() => {
  const t = { actif: 0, passif: 0, charges: 0, produits: 0 } as Record<Cote, number>
  for (const k of COTES) for (const l of grille[k]) t[k] = cents(t[k] + (soldes.value[l.cpt] ?? 0))
  return t
})

/** vide : rien d'inscrit au Bilan ; egal : Actif = Passif ; ecart : le déséquilibre normal du module. */
const etatBilan = computed(() => {
  const { actif, passif } = totaux.value
  if (actif === 0 && passif === 0) return 'vide'
  return actif === passif ? 'egal' : 'ecart'
})
const annonce = ref('')
watch(etatBilan, (n, o) => {
  if (o !== 'vide' || n === 'egal') annonce.value = n === 'egal' ? 'Le Bilan est équilibré.' : n === 'ecart' ? 'Le Bilan n\'est plus équilibré.' : ''
})

// ─── Le sens du dernier changement, et l'écart affiché un instant ───────────
const sensLigne = reactive<Record<string, 'haut' | 'bas'>>({})
const sensTotal = reactive<Record<Cote, 'haut' | 'bas'>>({ actif: 'haut', passif: 'haut', charges: 'haut', produits: 'haut' })
const ecarts = reactive<Partial<Record<Cote, { v: number, cle: number }>>>({})
let numero = 0

watch(soldes, (n, o) => {
  for (const cpt in n) if (n[cpt] !== o[cpt]) sensLigne[cpt] = n[cpt]! >= (o[cpt] ?? 0) ? 'haut' : 'bas'
})
watch(totaux, (n, o) => {
  for (const k of COTES) {
    if (n[k] === o[k]) continue
    sensTotal[k] = n[k] > o[k] ? 'haut' : 'bas'
    const cle = ++numero
    ecarts[k] = { v: cents(n[k] - o[k]), cle }
    setTimeout(() => { if (ecarts[k]?.cle === cle) delete ecarts[k] }, 2200)
  }
})

// ─── La consigne en cours ────────────────────────────────────────────────────
const faites = ref(new Set<number>())
watch(() => props.consigne, () => { faites.value = new Set() })

/** Les lignes de la consigne qui restent à saisir dans la grille (les comptes « journal seul » n'y sont pas). */
const restantes = computed(() => props.consigne
  .map((l, i) => ({ ...l, i }))
  .filter(l => !faites.value.has(l.i) && l.cpt in coteDe))
const enSaisie = computed(() => restantes.value.length > 0)
const cible = computed(() => restantes.value[0]?.cpt ?? null)
const cliquable = (_cpt: string) => true

// ─── Le popover ──────────────────────────────────────────────────────────────
const ouvert = ref<string | null>(null)
const montant = ref<number>()
const erreur = ref('')

function ouvrir(cpt: string) {
  if (!cliquable(cpt)) return
  ouvert.value = cpt
  montant.value = undefined
  erreur.value = ''
}
function fermer() {
  ouvert.value = null
}
function basculer(cpt: string, ouvre: boolean) {
  if (ouvre) ouvrir(cpt)
  else if (ouvert.value === cpt) fermer()
}
/** Le clic sur la ligne entière ouvre aussi ; le bouton, lui, passe par UPopover. */
function clicLigne(e: MouseEvent, cpt: string) {
  if ((e.target as HTMLElement).closest('button')) return
  ouvrir(cpt)
}

const historique = (cpt: string) => bilanCr.filter(e => e.cpt === cpt)

function valider(cpt: string) {
  const m = montant.value
  if (m == null || !(m > 0)) { erreur.value = 'Indiquez un montant.'; return }
  const candidates = restantes.value.filter(l => l.cpt === cpt)
  if (!candidates.length) { erreur.value = 'Ce compte n\'est pas dans l\'écriture en cours.'; return }
  const juste = candidates.find(l => Math.round(l.somme * 100) === Math.round(m * 100))
  if (!juste) { erreur.value = 'Ce montant n\'est pas celui de la consigne.'; return }

  faites.value = new Set(faites.value).add(juste.i)
  enregistrer(cpt, effet(juste))
  fermer()
  if (!enSaisie.value) emit('termine')
}

defineExpose({ bilanCr, enregistrer })
</script>

<template>
  <div class="bilan-cr">
    <section
      v-for="doc in documents"
      :key="doc.cle"
      class="document"
      :aria-labelledby="`titre-${doc.cle}`"
    >
      <div :id="`titre-${doc.cle}`" class="document-titre">
        {{ doc.titre }}
      </div>

      <div class="cotes" :class="doc.cle === 'bilan' && `equilibre-${etatBilan}`">
        <template v-for="(cote, n) in doc.cotes" :key="cote.cle">
          <div v-if="n === 1" class="signe-col" aria-hidden="true">
            <span v-if="doc.cle === 'bilan' && etatBilan !== 'vide'" class="signe">{{ etatBilan === 'egal' ? '=' : '≠' }}</span>
          </div>

          <table class="cote">
            <caption>{{ cote.titre }}</caption>
            <thead>
              <tr>
                <th scope="col"><span class="sr-only">Compte</span></th>
                <th scope="col"><span class="sr-only">Montant</span></th>
              </tr>
            </thead>

            <tbody>
              <tr
                v-for="l in grille[cote.cle]"
                :key="l.cpt"
                class="ligne"
                :class="{ vide: !inscrit(l.cpt), cible: cible === l.cpt, ouverte: ouvert === l.cpt, cliquable: cliquable(l.cpt) }"
                @click="clicLigne($event, l.cpt)"
              >
                <th scope="row">
                  <UPopover
                    :open="ouvert === l.cpt"
                    :content="{ side: 'bottom', align: 'start', sideOffset: 6, collisionPadding: 8 }"
                    @update:open="basculer(l.cpt, $event)"
                  >
                    <button type="button" class="compte" :aria-disabled="!cliquable(l.cpt)">
                      <span class="nom">{{ l.cpt }} {{ l.nom }}</span>
                      <span v-if="l.prec" class="prec">{{ l.prec }}</span>
                    </button>

                    <template #content>
                      <div class="pop">
                        <div class="pop-compte">
                          {{ l.cpt }} {{ l.nom }}
                        </div>

                        <div v-if="historique(l.cpt).length" class="pop-histo">
                          <div class="pop-histo-titre">
                            Déjà inscrit sur cette ligne
                          </div>
                          <ul>
                            <li v-for="(e, k) in historique(l.cpt)" :key="k">
                              {{ signe(e.somme) }}
                            </li>
                          </ul>
                        </div>
                        <div v-else-if="!enSaisie">Rien à inscrire sur cette ligne pour l'instant.</div>

                        <form v-if="enSaisie" class="pop-saisie" @submit.prevent="valider(l.cpt)">
                          <UFormField label="Montant" :error="erreur || false">
                            <UInputNumber
                              v-model="montant"
                              color="neutral"
                              locale="fr-FR"
                              :min="0"
                              :step="0.01"
                              :format-options="{ style: 'currency', currency: 'EUR', minimumFractionDigits: 0, maximumFractionDigits: 2 }"
                              :increment="false"
                              :decrement="false"
                              autofocus
                              class="w-full"
                            />
                          </UFormField>
                          <div class="pop-actions">
                            <UButton color="neutral" variant="ghost" label="Annuler" @click="fermer" />
                            <UButton type="submit" color="neutral" label="Inscrire" />
                          </div>
                        </form>

                        <div v-else class="pop-actions">
                          <UButton color="neutral" variant="ghost" label="Fermer" @click="fermer" />
                        </div>
                      </div>
                    </template>
                  </UPopover>
                </th>

                <td class="montant">
                  <span class="chiffre">
                    <Transition :name="`chasse-${sensLigne[l.cpt] ?? 'haut'}`">
                      <span :key="inscrit(l.cpt) ? soldes[l.cpt] : 'vide'">{{ inscrit(l.cpt) ? euros(soldes[l.cpt]!) : '' }}</span>
                    </Transition>
                  </span>
                  <UBadge
                    v-if="cible === l.cpt"
                    label="À saisir"
                    color="neutral"
                    variant="solid"
                    size="sm"
                    class="badge-cible"
                  />
                </td>
              </tr>

              <!-- Pousse le total en bas : le côté le plus court s'aligne sur l'autre. -->
              <tr class="bourrage" aria-hidden="true">
                <td colspan="2" />
              </tr>
            </tbody>

            <tfoot>
              <tr class="total">
                <th scope="row">
                  {{ cote.total }}
                </th>
                <td class="montant">
                  <span class="chiffre">
                    <Transition :name="`chasse-${sensTotal[cote.cle]}`">
                      <span :key="totaux[cote.cle]">{{ euros(totaux[cote.cle]) }}</span>
                    </Transition>
                  </span>
                  <Transition name="ecart">
                    <span
                      v-if="ecarts[cote.cle]"
                      :key="ecarts[cote.cle]!.cle"
                      class="ecart"
                      :class="{ baisse: ecarts[cote.cle]!.v < 0 }"
                      aria-hidden="true"
                    >{{ ecarts[cote.cle]!.v > 0 ? '▲' : '▼' }} {{ signe(ecarts[cote.cle]!.v) }}</span>
                  </Transition>
                </td>
              </tr>
            </tfoot>
          </table>
        </template>
      </div>
    </section>

    <div class="sr-only" aria-live="polite">
      {{ annonce }}
    </div>
  </div>
</template>

<style scoped>
.bilan-cr {
  container-type: inline-size;
  color: var(--ui-text);
}

/* ─── Documents et côtés ──────────────────────────────────────────────── */
.document + .document {
  margin-top: calc(var(--spacing, .25rem) * 4);
}
.document-titre {
  margin-bottom: calc(var(--spacing, .25rem) * 2);
  font-size: var(--text-sm, .875rem);
  font-weight: 600;
  color: var(--ui-text-highlighted);
}
.cotes {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 2.25rem minmax(0, 1fr);
  /* place pour l'écart affiché sous les totaux */
  padding-bottom: calc(var(--spacing, .25rem) * 6);
}
/* Pas de height: 100% : il s'appliquerait sans la caption, qui déborderait de la grille.
   Le tableau, élément de grille, s'étire seul. */
.cote {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
}
.cote caption {
  caption-side: top;
  padding-bottom: calc(var(--spacing, .25rem) * 1);
  margin-bottom: 2px;
  border-bottom: 1px solid var(--ui-border-accented);
  text-align: left;
  font-size: var(--text-xs, .75rem);
  font-weight: 500;
  letter-spacing: .04em;
  text-transform: uppercase;
  color: var(--ui-text-muted);
}
.cote thead th {
  height: 0;
  padding: 0;
  line-height: 0;
}
.bourrage {
  height: 100%;
}
.bourrage td {
  padding: 0;
}

/* ─── Les lignes : trois niveaux, aucune couleur ──────────────────────── */
.ligne > th,
.ligne > td {
  padding: calc(var(--spacing, .25rem) * 1);
  vertical-align: baseline;
  font-weight: 400;
  text-align: left;
}
.ligne > th {
  border-radius: var(--ui-radius, .25rem) 0 0 var(--ui-radius, .25rem);
}
.ligne > td {
  border-radius: 0 var(--ui-radius, .25rem) var(--ui-radius, .25rem) 0;
}
.ligne.cliquable {
  cursor: pointer;
}
.ligne.cliquable:hover > *,
.ligne.ouverte > * {
  background: var(--ui-bg-muted);
}

.compte {
  display: block;
  width: 100%;
  padding: 0;
  border: 0;
  border-radius: calc(var(--ui-radius, .25rem) * .75);
  background: none;
  color: inherit;
  font: inherit;
  text-align: left;
  cursor: inherit;
}
.compte:focus-visible {
  outline: 2px solid var(--ui-text-highlighted);
  outline-offset: 3px;
}
.compte[aria-disabled="true"] {
  cursor: default;
}

/* La hauteur de ligne ne change pas entre vide et remplie : rien ne se décale. */
.nom {
  display: block;
  font-size: var(--text-sm, .875rem);
  line-height: 1.25rem;
  color: var(--ui-text-highlighted);
  transition: font-size .3s, color .3s;
}
.prec {
  display: block;
  font-size: var(--text-xs, .75rem);
  line-height: 1rem;
  color: var(--ui-text-muted);
  transition: font-size .3s, color .3s;
}
.ligne.vide .nom {
  font-size: var(--text-xs, .75rem);
  color: var(--ui-text-muted);
}
.ligne.vide .prec {
  font-size: .625rem;
  color: var(--ui-text-dimmed);
}

/* La ligne à saisir : un cadre posé sur les cellules (une <tr> ne porte pas d'ombre fiable). */
.ligne.cible > th {
  box-shadow:
    inset 1.5px 0 0 var(--ui-text-muted),
    inset 0 1.5px 0 var(--ui-text-muted),
    inset 0 -1.5px 0 var(--ui-text-muted);
}
.ligne.cible > td {
  box-shadow:
    inset -1.5px 0 0 var(--ui-text-muted),
    inset 0 1.5px 0 var(--ui-text-muted),
    inset 0 -1.5px 0 var(--ui-text-muted);
}
.badge-cible {
  position: absolute;
  top: -.6rem;
  right: -.4rem;
  z-index: 1;
  white-space: nowrap;
  pointer-events: none;
}

/* ─── Montants ────────────────────────────────────────────────────────── */
.montant {
  position: relative;
  text-align: right !important;
  white-space: nowrap;
  font-size: var(--text-sm, .875rem);
  line-height: 1.25rem;
  font-variant-numeric: tabular-nums;
  font-weight: 500 !important;
}
/* Le chiffre qui chasse l'autre : l'ancien sort, le nouveau entre. Découpe verticale seulement. */
.chiffre {
  position: relative;
  display: inline-block;
  vertical-align: bottom;
  clip-path: inset(0 -100vw);
}
.chasse-haut-enter-active,
.chasse-haut-leave-active,
.chasse-bas-enter-active,
.chasse-bas-leave-active {
  transition: transform .3s ease, opacity .3s ease;
}
.chasse-haut-leave-active,
.chasse-bas-leave-active {
  position: absolute;
  top: 0;
  right: 0;
}
.chasse-haut-enter-from,
.chasse-bas-leave-to {
  opacity: 0;
  transform: translateY(100%);
}
.chasse-haut-leave-to,
.chasse-bas-enter-from {
  opacity: 0;
  transform: translateY(-100%);
}

/* ─── Totaux ──────────────────────────────────────────────────────────── */
.total > th,
.total > td {
  padding: calc(var(--spacing, .25rem) * 1.5) calc(var(--spacing, .25rem) * 1);
  border-top: 2px solid var(--ui-text);
  font-weight: 600;
  vertical-align: baseline;
  color: var(--ui-text-highlighted);
  transition: color .4s, background-color .4s, border-color .4s;
}
.total > th {
  text-align: left;
  font-size: var(--text-xs, .75rem);
  letter-spacing: .03em;
  text-transform: uppercase;
}
.total > td {
  font-size: var(--text-sm, .875rem);
}

/* Le Bilan équilibré passe au lime ; le Compte de Résultat ne porte jamais de couleur. */
.equilibre-egal .total > * {
  border-top-color: var(--color-lime-600, #65a30d);
  background: var(--color-lime-100, #ecfccb);
  color: var(--color-lime-800, #3f6212);
}
.signe-col {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}
.signe {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 2.1rem;
  font-size: var(--text-lg, 1.125rem);
  font-weight: 600;
  color: var(--ui-text-muted);
  transition: color .4s;
}
.equilibre-egal .signe {
  color: var(--color-lime-700, #4d7c0f);
}

/* L'écart, un instant sous le total ; une baisse se distingue d'une hausse. */
.ecart {
  position: absolute;
  top: 100%;
  right: calc(var(--spacing, .25rem) * 1);
  margin-top: 2px;
  font-size: var(--text-xs, .75rem);
  font-weight: 600;
  white-space: nowrap;
  color: var(--ui-text);
  pointer-events: none;
  animation: ecart-vie 2.2s ease forwards;
}
.ecart.baisse {
  color: var(--color-amber-700, #b45309);
}
@keyframes ecart-vie {
  0% { opacity: 0; transform: translateY(-3px); }
  10%, 78% { opacity: 1; transform: none; }
  100% { opacity: 0; }
}

/* ─── Popover ─────────────────────────────────────────────────────────── */
.pop {
  width: 18rem;
  max-width: calc(100vw - 1rem);
  padding: calc(var(--spacing, .25rem) * 3);
}
.pop-compte {
  margin-bottom: calc(var(--spacing, .25rem) * 2);
  font-size: var(--text-sm, .875rem);
  font-weight: 600;
  color: var(--ui-text-highlighted);
}
.pop-histo {
  margin-bottom: calc(var(--spacing, .25rem) * 3);
}
.pop-histo-titre {
  margin-bottom: 2px;
  font-size: var(--text-xs, .75rem);
  font-weight: 500;
  letter-spacing: .04em;
  text-transform: uppercase;
  color: var(--ui-text-muted);
}
.pop-histo ul {
  max-height: 8.25rem;
  margin: 0;
  padding: 0;
  overflow: auto;
  list-style: none;
}
.pop-histo li {
  padding: 3px 0;
  border-top: 1px solid var(--ui-border);
  text-align: right;
  font-size: var(--text-sm, .875rem);
  font-weight: 500;
  font-variant-numeric: tabular-nums;
  color: var(--ui-text);
}
.pop-histo li:first-child {
  border-top: 0;
}
.pop-actions {
  display: flex;
  justify-content: flex-end;
  gap: calc(var(--spacing, .25rem) * 2);
  margin-top: calc(var(--spacing, .25rem) * 3);
}

/* ─── Étroit ──────────────────────────────────────────────────────────── */
@container (max-width: 34em) {
  .cotes {
    grid-template-columns: minmax(0, 1fr) 1.5rem minmax(0, 1fr);
  }
  .prec {
    display: none;
  }
}

/* ─── Mouvement réduit : pas de glissement, l'écart seul ──────────────── */
@media (prefers-reduced-motion: reduce) {
  .chasse-haut-enter-active,
  .chasse-haut-leave-active,
  .chasse-bas-enter-active,
  .chasse-bas-leave-active,
  .nom,
  .prec {
    transition: none;
  }
  .ecart {
    animation-name: ecart-fixe;
  }
  @keyframes ecart-fixe {
    0%, 78% { opacity: 1; }
    100% { opacity: 0; }
  }
}
</style>
