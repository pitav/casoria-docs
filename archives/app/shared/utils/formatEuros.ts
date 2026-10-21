/**
 * Un montant en euros, écrit à la française avec les insécables de la charte.
 *
 *   formatEuros(1450)      → "1 450 €"
 *   formatEuros(1450, 2)   → "1 450,00 €"
 *   formatEuros(-25890)    → "− 25 890 €"   (signe moins typographique)
 *
 * Toutes les espaces sont des insécables (U+00A0). Le formatage est fait à la
 * main : toLocaleString('fr-FR') pose une espace fine (U+202F) que Poppins ne
 * rend pas, et le résultat changerait d'un navigateur à l'autre.
 *
 * Auto-importé par Nuxt depuis shared/utils/, côté application et serveur.
 */
export function formatEuros(montant: number, decimales = 0): string {
  const absolu = Math.abs(montant).toFixed(decimales)
  const [entier = '0', cents] = absolu.split('.')
  const groupe = entier.replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
  // pas de « − 0 € » quand l'arrondi ramène un petit négatif à zéro
  const signe = montant < 0 && Number(absolu) !== 0 ? '− ' : ''
  return signe + groupe + (cents ? ',' + cents : '') + ' €'
}
