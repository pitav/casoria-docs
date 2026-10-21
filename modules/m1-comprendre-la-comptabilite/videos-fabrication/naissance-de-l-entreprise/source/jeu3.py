import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])
        pg=await b.new_page(viewport={'width':1440,'height':810})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///tmp/vid/apercu.html'); await pg.wait_for_timeout(1500)
        for start,att in [(46,4),(60,4),(80,3),(134,3)]:
            await pg.evaluate(f"document.getElementById('son').currentTime={start}")
            if await pg.evaluate("document.getElementById('son').paused"): await pg.click('#lp')
            await pg.wait_for_timeout(att*1000)
            t=await pg.evaluate("document.getElementById('son').currentTime")
            v=await pg.evaluate("['#v-banque','#tt-ac','#tt-pa','#l-banque .val'].map(s=>document.querySelector(s).textContent)")
            print(round(t,1),v)
        await pg.screenshot(path='jeu2.png'); print('erreurs',errs); await b.close()
asyncio.run(main())
