import json,re,subprocess
segs=json.load(open('voixoff.json'))
OUV=6.0; G_SEG=0.8; G_PLAN=1.4; FIN=6.0
def pauses(f):
    o=subprocess.run(['ffmpeg','-i',f,'-af','silencedetect=n=-35dB:d=0.2','-f','null','-'],capture_output=True,text=True).stderr
    st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',o)]; en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',o)]
    return list(zip(st,en))
t=OUV; prev=None
for s in segs:
    if prev is not None: t+= G_PLAN if s['plan']!=prev else G_SEG
    prev=s['plan']; s['debut']=round(t,3); t+=s['duree']; s['fin']=round(t,3)
    txt=s['texte']; ps=pauses(s['fichier'])
    voice_on=ps[0][1] if ps and ps[0][0]<0.05 else 0.0
    idx=[0]+[m.end() for m in re.finditer(r'[.?!:]\s+',txt)]
    used=0 if ps and ps[0][0]<0.05 else -1; phr=[]
    for k,i in enumerate(idx):
        est=s['duree']*i/len(txt)
        if k==0: real=voice_on
        else:
            c=[(abs(e-est),j,e) for j,(a,e) in enumerate(ps) if j>used and e-a>=0.2]
            if not c: real=est
            else: _,j,real=min(c); used=j
        phr.append({'i':i,'t':round(real,3)})
    s['phrases']=phr
    print(s['id'],s['debut'],[(txt[p['i']:p['i']+14],round(s['duree']*p['i']/len(txt),2),p['t']) for p in phr])
total=round(t+FIN,2)
J={"voix":"voice_dur676prxpls","modele":"gemini-3.8-flash-tts","duree_totale":total,"segments":segs}
json.dump(J,open('voixoff-mesure.json','w'),ensure_ascii=False,indent=1)
# mix
jfin=round(total-5.6,2)
cmd=['ffmpeg','-y','-loglevel','error','-f','lavfi','-t',str(total),'-i','anullsrc=r=44100:cl=stereo']
flt=[]
for i,s in enumerate(segs):
    cmd+=['-i',s['fichier']]; flt.append(f"[{i+1}]adelay={int(s['debut']*1000)}:all=1[v{i}]")
J1=len(segs)+1
cmd+=['-i','/mnt/user-data/uploads/casoria-docs/jingle-logo-casoria.mp3','-i','/mnt/user-data/uploads/casoria-docs/jingle-logo-casoria.mp3']
flt.append(f"[{J1}]volume=0.4[j0]"); flt.append(f"[{J1+1}]volume=0.4,adelay={int(jfin*1000)}:all=1[j1]")
flt.append('[0]'+''.join(f'[v{i}]' for i in range(len(segs)))+'[j0][j1]'+f'amix=inputs={len(segs)+3}:normalize=0:duration=first[o]')
cmd+=['-filter_complex',';'.join(flt),'-map','[o]','-b:a','160k','mix-ch08.mp3']
subprocess.run(cmd,check=True); print('total',total,'jingle fin',jfin)
