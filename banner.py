# writes assets/banner-dark.svg and assets/banner-light.svg
T = {
 'dark':  dict(bg='#0b0b0d', fg='#f2f2f4', mu='#9d9da8', ln='#2a2a31', ac='#c9c9d2'),
 'light': dict(bg='#f6f6f4', fg='#141416', mu='#5d5d66', ln='#d4d4d8', ac='#3a3a42'),
}
def svg(c):
    ticks = ''.join(f'<line x1="{x}" y1="0" x2="{x-60}" y2="300" />' for x in range(0, 1300, 26))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300" role="img" aria-label="Josh Lucem, plugins for Minecraft">
<style>
  .t{{font-family:'Outfit','Segoe UI',Helvetica,Arial,sans-serif}}
  .s{{font-family:Georgia,'Times New Roman',serif;font-style:italic}}
  .m{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}
  @keyframes spin{{to{{transform:rotate(360deg)}}}}
  @keyframes spin2{{to{{transform:rotate(-360deg)}}}}
  @keyframes rise{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:none}}}}
  .o1{{transform-origin:960px 150px;animation:spin 26s linear infinite}}
  .o2{{transform-origin:960px 150px;animation:spin2 38s linear infinite}}
  .o3{{transform-origin:960px 150px;animation:spin 17s linear infinite}}
  .r{{animation:rise .9s ease both}} .r2{{animation:rise .9s .25s ease both}} .r3{{animation:rise .9s .5s ease both}}
</style>
<rect width="1200" height="300" fill="{c['bg']}"/>
<g stroke="{c['ln']}" stroke-width="1" opacity=".55">{ticks}</g>
<rect x=".5" y=".5" width="1199" height="299" fill="none" stroke="{c['ln']}"/>
<g stroke="{c['ac']}" fill="none">
  <g class="o1"><ellipse cx="960" cy="150" rx="150" ry="52" transform="rotate(-28 960 150)" stroke-width="2.4"/><circle cx="1103" cy="106" r="5" fill="{c['fg']}" stroke="none"/></g>
  <g class="o2"><ellipse cx="960" cy="150" rx="150" ry="52" transform="rotate(34 960 150)" stroke-width="1.2"/><circle cx="1090" cy="224" r="4" fill="{c['mu']}" stroke="none"/></g>
  <g class="o3"><ellipse cx="960" cy="150" rx="150" ry="52" transform="rotate(97 960 150)" stroke-width="1" stroke-dasharray="4 6"/><circle cx="947" cy="2" r="3.5" fill="{c['fg']}" stroke="none"/></g>
</g>
<circle cx="960" cy="150" r="26" fill="{c['bg']}" stroke="{c['ac']}" stroke-width="1.5"/>
<text x="960" y="159" text-anchor="middle" class="t" font-size="24" font-weight="600" fill="{c['fg']}">Ag</text>
<text x="946" y="138" class="m" font-size="9" fill="{c['mu']}">47</text>
<g class="r"><text x="64" y="64" class="m" font-size="14" fill="{c['mu']}" letter-spacing="2">LIMA · 12.05° S</text></g>
<g class="r2"><text x="60" y="150" class="t" font-size="76" font-weight="600" fill="{c['fg']}" letter-spacing="-2">Josh Lucem</text></g>
<g class="r3"><text x="64" y="204" class="s" font-size="30" fill="{c['mu']}">plugins for Minecraft, and a bit of law.</text></g>
<text x="64" y="262" class="m" font-size="13" fill="{c['mu']}">Java · Paper · Node.js</text>
</svg>'''
import os
os.makedirs('assets', exist_ok=True)
for k, c in T.items():
    open(f'assets/banner-{k}.svg', 'w').write(svg(c))
