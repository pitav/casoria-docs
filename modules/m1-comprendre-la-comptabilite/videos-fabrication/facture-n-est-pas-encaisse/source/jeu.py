import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])
        pg=await b.new_page(viewport={'width':1440,'height':810})
        await pg.goto('file:///tmp/vid/apercu.html'); await pg.wait_for_timeout(1500)
        await pg.evaluate("document.getElementById('son').currentTime=124")
        await pg.click('#lp'); await pg.wait_for_timeout(5000)
        print(await pg.evaluate("document.getElementById('son').currentTime"))
        print(await pg.evaluate("['#l-ventes .val','#tt-pr','#tt-ch','#l-creances .val','#l-banque .val','#tt-ac'].map(s=>document.querySelector(s).textContent+' / '+getComputedStyle(document.querySelector(s).closest('.ligne,.tot-col')).opacity)"))
        await pg.screenshot(path='jeu.png'); await b.close()
asyncio.run(main())
