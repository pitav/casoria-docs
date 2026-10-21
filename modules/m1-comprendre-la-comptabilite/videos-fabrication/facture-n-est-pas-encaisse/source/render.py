import sys,asyncio,subprocess
from playwright.async_api import async_playwright
FPS=30; a,b,out=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
async def main():
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-',
        '-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p',out],stdin=subprocess.PIPE)
    async with async_playwright() as p:
        br=await p.chromium.launch()
        pg=await br.new_page(viewport={'width':1920,'height':1080})
        await pg.goto('file:///tmp/vid/video.html'); await pg.wait_for_function('window.PRET===true')
        await pg.evaluate('void tl.seek(0,false)')
        for f in range(a,b):
            await pg.evaluate(f'void tl.seek({f/FPS},false)')
            ff.stdin.write(await pg.screenshot(type='jpeg',quality=92))
        await br.close()
    ff.stdin.close(); ff.wait()
asyncio.run(main())
