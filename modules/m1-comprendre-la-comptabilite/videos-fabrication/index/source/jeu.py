import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])
        pg=await b.new_page(viewport={'width':1440,'height':810})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///tmp/vid/apercu.html'); await pg.wait_for_timeout(1500)
        for start,attente,sel in [(9,3,['#ap-b','#ap-c']),(40,3,['#pluie','#repere']),(66,4,['.etape','#repere']),(84,1,['#promesse'])]:
            await pg.evaluate(f"document.getElementById('son').currentTime={start}")
            if await pg.evaluate("document.getElementById('son').paused"): await pg.click('#lp')
            await pg.wait_for_timeout(attente*1000)
            t=await pg.evaluate("document.getElementById('son').currentTime")
            info=await pg.evaluate(f"{sel}.map(s=>{{const e=document.querySelector(s);return s+' op='+getComputedStyle(e).opacity+' left='+e.style.left}})")
            vis=await pg.evaluate("[...document.querySelectorAll('.goutte')].filter(g=>+getComputedStyle(g).opacity>0).length")
            print(round(t,2),info,'gouttes visibles',vis)
            await pg.screenshot(path=f'jeu-{start}.png')
        print('erreurs',errs); await b.close()
asyncio.run(main())
