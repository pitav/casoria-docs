import json,re,subprocess,sys
V='/mnt/user-data/uploads/casoria-docs/Claude outputs/video-ch04/voix/'
d=json.load(open('/tmp/voix/ch04/voixoff.json'))
def pauses(f):
    o=subprocess.run(['ffmpeg','-i',V+f,'-af','silencedetect=n=-35dB:d=0.2','-f','null','-'],capture_output=True,text=True).stderr
    st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',o)]; en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',o)]
    return list(zip(st,en))
for s in d['segments']:
    t=s['texte']; ps=pauses(s['fichier'])
    voice_on=ps[0][1] if ps and ps[0][0]<0.05 else 0.0
    # sentence starts (char idx)
    idx=[0]+[m.end() for m in re.finditer(r'[.?!:]\s+',t)]
    phr=[]
    used=0 if ps and ps[0][0]<0.05 else -1
    for k,i in enumerate(idx):
        est=s['duree']*i/len(t)
        if k==0: real=voice_on
        else:
            cands=[(abs(e-est),j,e) for j,(a,e) in enumerate(ps) if j>used and e-a>=0.2]
            _,j,real=min(cands); used=j
        phr.append({'i':i,'t':round(real,3)})
    s['phrases']=phr
    print(s['id'],[(t[p['i']:p['i']+18],round(s['duree']*p['i']/len(t),2),p['t']) for p in phr])
json.dump(d,open('/tmp/voix/ch04/voixoff-mesure.json','w'),ensure_ascii=False,indent=1)
