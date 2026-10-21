import sys,asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1920,'height':1080})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
        await pg.goto('file:///tmp/vid/video.html'); await pg.wait_for_function('window.PRET===true')
        import time
        for t in sys.argv[1:]:
            t0=time.time()
            await pg.evaluate(f'void tl.seek({t},false)'); await pg.screenshot(path=f'snap-{t}.png'); print(t,round(time.time()-t0,2),flush=True)
        print('erreurs:',errs); await b.close()
asyncio.run(main())
