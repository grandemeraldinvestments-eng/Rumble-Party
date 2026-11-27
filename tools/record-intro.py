#!/usr/bin/env python3
"""Record the opening of a board's introduction as a film, from the game itself.

    python3 tools/record-intro.py island            # 1280x720, 30 frames a second
    python3 tools/record-intro.py island 1920 1080 30

The game must be served on http://localhost:8765 (PORT=8765 node server.js). Needs Python Playwright, Chrome and ffmpeg.
The film covers the flight in and the board's special rule, and stops before the camera turns to the pearl, because the pearl is in a
different place every game and is always shown live. No words are recorded: the title and the rule card are drawn over the film by the
game. Every frame is stepped by hand, so the same command always gives the same film.
Writes assets/intro/<board>.mp4 and assets/intro/<board>.jpg. To use them, add to that board's entry in INTRO.boards (index.html):
    video:{src:'assets/intro/<board>.mp4',poster:'assets/intro/<board>.jpg',until:<the number this script prints>}
"""
import asyncio, os, subprocess, sys, tempfile
from playwright.async_api import async_playwright
board=sys.argv[1]; W=int(sys.argv[2]) if len(sys.argv)>2 else 1280; H=int(sys.argv[3]) if len(sys.argv)>3 else 720; FPS=int(sys.argv[4]) if len(sys.argv)>4 else 30
URL=os.environ.get('RUMBLE_URL','http://localhost:8765/index.html'); CHROME=os.environ.get('CHROME','/usr/bin/google-chrome')
ARGS=['--use-gl=angle','--ignore-gpu-blocklist','--no-sandbox']+(['--use-angle=swiftshader','--enable-unsafe-swiftshader'] if os.environ.get('SOFTWARE_GL','1')=='1' else [])
async def main():
    out=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','assets','intro'); os.makedirs(out,exist_ok=True); tmp=tempfile.mkdtemp()
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=CHROME,args=ARGS); pg=await (await b.new_context(viewport={'width':W,'height':H},device_scale_factor=1,service_workers='block')).new_page()
        await pg.goto(URL); await pg.wait_for_timeout(3500)
        await pg.evaluate("localStorage.setItem('rumble-intro','full'); document.querySelector('#soloBtn').click()"); await pg.wait_for_timeout(600)
        for i in range(14):
            if await pg.evaluate("document.querySelector('#guide').hidden"): break
            await pg.evaluate("[...document.querySelectorAll('#gBtns button')].pop().click()"); await pg.wait_for_timeout(200)
        await pg.evaluate(f"document.querySelector('#m{board[0].upper()+board[1:]}').click()"); await pg.wait_for_timeout(800)
        await pg.evaluate("document.querySelector('#startBtn').click()"); await pg.wait_for_function("IN&&IN.gid===V.gid"); await pg.wait_for_timeout(300)
        # no words, no buttons, and time stepped by hand
        until=await pg.evaluate("""(()=>{window.requestAnimationFrame=()=>0; for(const q of ['#titleCard','#introCard','#introSkip','#introWait','#game'])document.querySelector(q).style.visibility='hidden';
          INTRO.LIMIT=1e9; pearl.visible=false; pawns.forEach(g=>{g.visible=false;}); IN.from=introPose(IN.seq[0][0],0,IN);   /* nothing that changes from game to game may be in the film: no pieces, no pearl */
           const a=IN.seq[0][1]+IN.seq[1][1], B=Math.min(.95,IN.seq[1][1]*.42); window.__rec=t=>{INTRO.seek(t); frame(last+1000/%d);}; return +(a-B).toFixed(2);})()"""%FPS)
        n=int(until*FPS)+1
        for k in range(n):
            await pg.evaluate(f"__rec({k/FPS})"); await pg.screenshot(path=f'{tmp}/f{k:04d}.jpg',type='jpeg',quality=95)
            if k%30==0: print(f'frame {k}/{n}',flush=True)
        await b.close()
    mp4=os.path.join(out,board+'.mp4'); jpg=os.path.join(out,board+'.jpg')
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',f'{tmp}/f%04d.jpg','-c:v','libx264','-preset','slow','-crf','23','-pix_fmt','yuv420p','-movflags','+faststart','-an',mp4],check=True)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{tmp}/f0000.jpg','-q:v','4',jpg],check=True)
    print(f'wrote {mp4} ({os.path.getsize(mp4)//1024} KB) and {jpg}; until:{until}')
asyncio.run(main())
