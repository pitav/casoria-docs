import sys
def R(s,a,b):
    assert s.count(a)==1,(s.count(a),a[:60]); return s.replace(a,b)
def t(s):
    s=R(s,"height:90px;background:transparent;","height:90px;background:transparent;border-bottom:1px solid #ffffff95;")
    s=R(s,".facture .type{font-size:16px;font-weight:800;letter-spacing:.12em;color:var(--s400)}",".facture .type{font-size:16px;font-weight:800;letter-spacing:.12em;color:var(--s500)}")
    s=R(s,".facture .dest{margin-top:10px;font-size:20px;color:var(--s500)}",".facture .dest{margin-top:10px;font-size:20px;color:var(--s600)}")
    s=R(s,".facture .ech{margin-top:4px;text-align:right;font-size:20px;color:var(--s500)}",".facture .ech{margin-top:4px;text-align:right;font-size:20px;color:var(--s600)}")
    s=R(s,"#question{top:800px;font-size:46px}","#question{top:800px;font-size:46px}\n#pourquoi{top:440px;font-size:58px}")
    s=R(s,'<p id="siattend" class="abs">','<p id="pourquoi" class="abs phrase">Pourquoi ne pas attendre l\'argent&nbsp;?</p>\n  <p id="siattend" class="abs">')
    s=R(s,"tl.to(['#cr', '#facture1', '#banque', '#fl-g', '#frise', '#quand'], { autoAlpha: 0, duration: .5 }, t2b - .3)",
          "tl.to(['#cr', '#facture1', '#banque', '#fl-g', '#frise', '#quand'], { autoAlpha: 0, duration: .5 }, t2b - .3)\n"
          "  /* Pascal : 0:43, le titre comble le trou, puis monte au-dessus des deux entreprises */\n"
          "  .fromTo('#pourquoi', { autoAlpha: 0, y: 14 }, { autoAlpha: 1, y: 0, duration: .7, ease: E }, 43.0)\n"
          "  .to('#pourquoi', { top: 30, fontSize: 44, duration: .8, ease: 'power2.inOut' }, at('p2-2', 'Imaginez') - .6)")
    s=R(s,"tl.to(['#jum-a', '#jum-b'], { autoAlpha: 0, duration: .5 }, t3 - .8)","tl.to(['#jum-a', '#jum-b', '#pourquoi'], { autoAlpha: 0, duration: .5 }, t3 - .8)")
    return s
for f in sys.argv[1:]:
    x=t(open(f,encoding='utf-8').read()); open(f,'w',encoding='utf-8').write(x); print('ok',f)
