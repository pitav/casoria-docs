import json,base64,re,sys
B='/tmp/vid/'; nm=B+'node_modules/'
s=open(B+'gabarit-ch08.html',encoding='utf-8').read()
def ff(fam,path,w):
    d=base64.b64encode(open(nm+path,'rb').read()).decode()
    return f"@font-face{{font-family:{fam};font-weight:{w};font-style:normal;src:url(data:font/woff2;base64,{d}) format('woff2')}}"
fonts=[ff('Poppins',f'@fontsource/poppins/files/poppins-latin-{w}-normal.woff2',w) for w in (400,500,600,700,800)]
s=s.replace('/*__FONTS__*/','\n'.join(fonts))
logo=open('/mnt/user-data/uploads/casoria-docs/logo-casoria.svg').read()
i1=logo.find('<path'); i2=logo.find('<path',i1+5); i3=logo.find('<defs')
logo=logo[:i1]+'<g class="lg-mot">'+logo[i1:i2]+'</g><g class="lg-sym">'+logo[i2:i3]+'</g>'+logo[i3:]
s=s.replace('/*__LOGO__*/',logo)
icons=json.load(open(nm+'@iconify-json/mdi/icons.json'))
def icon(n):
    i=icons['icons'][n]; w=i.get('width',icons.get('width',24)); h=i.get('height',icons.get('height',24))
    return f'<svg viewBox="0 0 {w} {h}" fill="currentColor" aria-hidden="true">{i["body"]}</svg>'
s=re.sub(r'/\*__I:([a-z0-9-]+)__\*/',lambda m:icon(m.group(1)).replace("'","\\'"),s)
s=s.replace('/*__GSAP__*/',open(nm+'gsap/dist/gsap.min.js').read())
V=json.load(open('/tmp/voix/ch08/voixoff-mesure.json')); V['jingle_fin']=round(V['duree_totale']-5.6,2)
s=s.replace('/*__VOIX__*/',json.dumps(V,ensure_ascii=False))
if len(sys.argv)>2:
    a=base64.b64encode(open('/tmp/voix/ch08/mix-ch08.mp3','rb').read()).decode()
    s=s.replace('<!--__APERCU__-->',f'''<audio id="son" src="data:audio/mpeg;base64,{a}"></audio>
<div id="ctl" style="position:fixed;left:0;right:0;bottom:0;padding:10px 20px;background:#0f172acc;display:flex;gap:16px;align-items:center;font:16px Poppins;color:#fff;z-index:9">
<button id="lp" style="font:inherit;padding:6px 16px;border-radius:8px;border:0;cursor:pointer">Lecture</button>
<input id="pos" type="range" min="0" max="{V['duree_totale']}" step="0.01" value="0" style="flex:1">
<span id="tc">0:00</span></div>
<script>
const son=document.getElementById('son'),lp=document.getElementById('lp'),pos=document.getElementById('pos'),tc=document.getElementById('tc');
function fit(){{const k=Math.min(innerWidth/1920,innerHeight/1080);const st=document.getElementById('stage');document.documentElement.style.cssText='width:auto;height:auto;overflow:hidden;background:#fff';document.body.style.cssText='width:auto;height:auto';st.style.transformOrigin='0 0';st.style.transform='scale('+k+')';}}
addEventListener('resize',fit);fit();
lp.onclick=()=>{{son.paused?son.play():son.pause();}};
son.onplay=()=>lp.textContent='Pause';son.onpause=()=>lp.textContent='Lecture';
pos.oninput=()=>{{son.currentTime=+pos.value;tl.seek(+pos.value,false);}};
(function loop(){{if(!son.paused){{tl.seek(son.currentTime,false);pos.value=son.currentTime;}}const t=+pos.value;tc.textContent=Math.floor(t/60)+':'+String(Math.floor(t%60)).padStart(2,'0');requestAnimationFrame(loop);}})();
tl.seek(0,false);
</script>''')
open(sys.argv[1],'w',encoding='utf-8').write(s)
print(sys.argv[1], len(s)//1024,'Ko')
