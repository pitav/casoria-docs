import asyncio
from playwright.async_api import async_playwright
Q="['#l-ventes .val','#tt-pr','#l-achats .val','#tt-ch','#l-creances .val','#l-banque .val','#tt-ac','#tt-pa','#l-dettes .val'].map(s=>document.querySelector(s).textContent).join(' | ')"
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1920,'height':1080})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///tmp/vid/video.html'); await pg.wait_for_function('window.PRET===true')
        marks=[39.9,40.4,64,92.9,93.4,126.9,127.7,133]; t=0.0
        while t<=134:
            await pg.evaluate(f'void tl.seek({t},false)')
            for m in marks:
                if abs(t-m)<0.01: print(m, await pg.evaluate(Q))
            t=round(t+0.1,2)
        print('erreurs',errs); await b.close()
asyncio.run(main())
