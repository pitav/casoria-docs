import asyncio,json,sys
from playwright.async_api import async_playwright
V=json.load(open('/tmp/voix/ch07/voixoff-mesure.json'))
ts=[float(x) for x in sys.argv[1:]] or [s['fin']-0.3 for s in V['segments']]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1920,'height':1080})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///tmp/vid/apercu.html'); await pg.wait_for_timeout(1500)
        await pg.evaluate("document.getElementById('ctl').style.display='none'")
        for t in ts:
            await pg.evaluate(f"void tl.seek({t},false)"); await pg.wait_for_timeout(150)
            await pg.screenshot(path=f'cap-{t:06.1f}.png')
        print('erreurs',errs); await b.close()
asyncio.run(main())
