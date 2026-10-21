import re, sys

def R(s, a, b, n=1):
    c = s.count(a)
    assert c == n, f'{c}x : {a[:70]}'
    return s.replace(a, b)

def transforme(s):
    # palette : amber -> yellow ; primary 900 ; yellow 400
    s = R(s, "--a50:#fffbeb;--a100:#fef3c7;--a500:#f59e0b;--a700:#b45309;",
             "--y50:#fefce8;--y100:#fef9c3;--y400:#facc15;--y500:#eab308;--y700:#a16207;")
    s = R(s, "--p600:#1063b9;--p700:#0e4f97;", "--p600:#1063b9;--p700:#0e4f97;--p900:#133a67;")
    s = R(s, "border:3px solid var(--a500);background:var(--a50)", "border:3px solid var(--y500);background:var(--y50)")
    # fond global partout (en-tête compris)
    s = R(s, "html,body{width:1920px;height:1080px;overflow:hidden;background:var(--p50)}",
             "html,body{width:1920px;height:1080px;overflow:hidden;background:#459ceb}")
    s = R(s, "background:linear-gradient(to right,var(--p50),var(--pu50))", "background:linear-gradient(to right,#459ceb,#c084fc)")
    s = R(s, "height:90px;background:#fff;border-bottom:2px solid var(--p100);", "height:90px;background:transparent;")
    s = R(s, "#entete .mod{font-size:16px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--p600)}",
             "#entete .mod{font-size:16px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#fff}")
    # repères de temps et titre « À retenir »
    s = R(s, "text-transform:uppercase;color:var(--p600)}\n\n/* frise", "text-transform:uppercase;color:var(--p900)}\n\n/* frise")
    s = R(s, "#retenir-t{left:0;right:0;top:150px;text-align:center;font-size:26px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--p600)}",
             "#retenir-t{left:0;right:0;top:150px;text-align:center;font-size:26px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--p900)}")
    # frise
    s = R(s, "height:3px;background:var(--p200);border-radius:2px}", "height:3px;background:var(--p700);border-radius:2px}")
    s = R(s, "font-size:20px;font-weight:600;color:var(--s500);transform:translateX(-50%)}", "font-size:20px;font-weight:600;color:var(--p900);transform:translateX(-50%)}")
    # tuiles : sans bordure, nom à l'intérieur
    s = R(s, ".acteur .tuile{width:150px;height:150px;margin:0 auto;border:3px solid var(--s300);border-radius:24px;background:#fff;display:flex;align-items:center;justify-content:center}",
             ".acteur .tuile{width:210px;height:210px;margin:0 auto;border-radius:24px;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center}")
    s = R(s, ".acteur p{margin-top:16px;font-size:28px;font-weight:600;color:var(--s700)}",
             ".acteur p{margin-top:12px;font-size:26px;font-weight:600;color:var(--s700)}")
    s = R(s, ".acteur.eteint .tuile{border-color:var(--s200);background:#fff}", ".acteur.eteint .tuile{background:#fff}")
    s = R(s, "#colis{width:64px;height:64px;", "#colis{width:64px;height:64px;margin-top:6px;")
    s = R(s, ".jumelle .tuile{width:120px;height:120px;margin:0 auto;border:3px solid var(--s300);border-radius:20px;background:#fff;display:flex;align-items:center;justify-content:center}",
             ".jumelle .tuile{width:300px;height:210px;margin:0 auto;border-radius:22px;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center}")
    s = R(s, ".jumelle h3{margin-top:14px;font-size:28px;", ".jumelle h3{margin-top:10px;font-size:28px;")
    s = re.sub(r'</svg></div><p>(Fournisseur|Entreprise|Client)</p></div>', r'</svg><p>\1</p></div></div>', s)
    s = re.sub(r'</svg></div>(<h3>[^<]*</h3><p class="quand-paie">[^<]*</p>)', r'</svg>\1</div>', s)
    s = s.replace('/*__I:warehouse__*/</div><p>Fournisseur</p></div>', '/*__I:warehouse__*/<p>Fournisseur</p></div></div>')
    s = s.replace('/*__I:domain__*/</div><p>Entreprise</p></div>', '/*__I:domain__*/<p>Entreprise</p></div></div>')
    s = s.replace('/*__I:office-building-outline__*/</div><p>Client</p></div>', '/*__I:office-building-outline__*/<p>Client</p></div></div>')
    s = re.sub(r'(/\*__I:domain__\*/)</div>(<h3>[^<]*</h3><p class="quand-paie">[^<]*</p>)', r'\1\2</div>', s)
    # facture : ticket jaune dentelé
    s = R(s, ".facture{width:330px;background:#fff;border:2.5px solid var(--s300);padding:22px 24px 22px;color:var(--s700);box-shadow:0 18px 34px -24px rgba(15,23,42,.45)}",
             ".facture{width:330px;background:var(--y100);padding:30px 24px 30px;color:var(--s700);"
             "clip-path:polygon(0 8px,10% 0,20% 8px,30% 0,40% 8px,50% 0,60% 8px,70% 0,80% 8px,90% 0,100% 8px,"
             "100% calc(100% - 8px),90% 100%,80% calc(100% - 8px),70% 100%,60% calc(100% - 8px),50% 100%,40% calc(100% - 8px),30% 100%,20% calc(100% - 8px),10% 100%,0 calc(100% - 8px))}")
    s = R(s, "border-radius:4px;background:var(--s200);margin-top:12px}", "border-radius:4px;background:var(--y400);margin-top:12px}")
    s = R(s, "padding-top:12px;border-top:2px solid var(--s200);text-align:right;", "padding-top:12px;border-top:2px solid var(--y400);text-align:right;")
    # panneaux et documents sans bordure
    s = R(s, "#banque{width:330px;border:2.5px solid var(--s300);border-radius:18px;", "#banque{width:330px;border-radius:18px;")
    s = R(s, ".doc{width:660px;height:600px;border:3px solid var(--s300);border-radius:24px;", ".doc{width:660px;height:600px;border-radius:24px;")
    s = R(s, "padding:12px 14px;background:#fff;border:3px solid var(--s700)}", "padding:12px 14px;background:#fff;border:3px solid transparent}")
    s = R(s, ".ligne.vide{border-style:dashed}", ".ligne.vide{border-style:dashed;border-color:var(--s300)}")
    s = R(s, ".set('#l-banque', { borderStyle: 'solid' }, 127.0)", ".set('#l-banque', { borderColor: 'transparent' }, 127.0)")
    s = R(s, "width:420px;background:#fff;border:3px solid var(--s300);border-radius:20px;", "width:420px;background:#fff;border-radius:20px;")
    s = R(s, ".face{width:560px;background:#fff;border:3px solid var(--s300);border-radius:24px;", ".face{width:560px;background:#fff;border-radius:24px;")
    s = R(s, "width:1300px;background:#fff;border:3px solid var(--s300);border-radius:22px;", "width:1300px;background:#fff;border-radius:22px;")
    # textes posés sur le fond
    s = R(s, "text-align:center;font-family:Gelasio,Georgia,serif;color:var(--p600)}",
             "text-align:center;font-family:Gelasio,Georgia,serif;color:#fff;font-weight:500}")
    s = R(s, "#siattend{left:0;right:0;top:880px;text-align:center;font-size:28px;font-weight:600;color:var(--s500)}",
             "#siattend{left:0;right:0;top:880px;text-align:center;font-size:28px;font-weight:600;color:#fff}")
    s = R(s, "#titre small{display:block;margin-bottom:14px;font-size:22px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:var(--p600)}",
             "#titre small{display:block;margin-bottom:14px;font-size:22px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:#fff}")
    s = R(s, ".fleche{height:4px;background:var(--s400)}", ".fleche{height:4px;background:#fff}")
    s = R(s, "border-right:14px solid var(--s400)}", "border-right:14px solid #fff}")
    s = R(s, "border-left:14px solid var(--s400)}", "border-left:14px solid #fff}")
    return s

src, dst = sys.argv[1], sys.argv[2]
out = transforme(open(src, encoding='utf-8').read())
assert 'amber' not in out and '--a5' not in out
open(dst, 'w', encoding='utf-8').write(out)
print('ok', dst)
