import asyncio,json
from playwright.async_api import async_playwright
V=json.load(open('/tmp/voix/ch07/voixoff-mesure.json'));S={s['id']:s for s in V['segments']}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])
        pg=await b.new_page(viewport={'width':1440,'height':810})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///tmp/vid/apercu.html'); await pg.wait_for_timeout(1500)
        st=S['p6-1']['debut']-1
        await pg.evaluate(f"document.getElementById('son').currentTime={st}")
        await pg.click('#lp')
        for k in range(14):
            await pg.wait_for_timeout(1500)
            t=await pg.evaluate("document.getElementById('son').currentTime")
            v=await pg.evaluate("['#tt-pr','#v-res'].map(s=>document.querySelector(s).textContent)")
            print(round(t,1),v)
        await pg.evaluate("document.getElementById('son').currentTime=%f"%(S['p8-1']['debut']+1)); await pg.wait_for_timeout(800)
        print('croix au refrain', await pg.evaluate("getComputedStyle(document.getElementById('croix')).opacity"))
        print('erreurs',errs); await b.close()
asyncio.run(main())
