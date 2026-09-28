"""Build original, dependency-free SVG artwork for the GitHub profile."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)

INK = '#101526'
WHITE = '#f4f1ff'
MINT = '#9affce'
PURPLE = '#b6a1ff'
PEACH = '#ffce92'
MUTED = '#a7abc6'

FONT = {
 'A':['01110','10001','10001','11111','10001','10001','10001'],
 'B':['11110','10001','10001','11110','10001','10001','11110'],
 'C':['01111','10000','10000','10000','10000','10000','01111'],
 'D':['11110','10001','10001','10001','10001','10001','11110'],
 'E':['11111','10000','10000','11110','10000','10000','11111'],
 'F':['11111','10000','10000','11110','10000','10000','10000'],
 'G':['01111','10000','10000','10111','10001','10001','01111'],
 'H':['10001','10001','10001','11111','10001','10001','10001'],
 'I':['11111','00100','00100','00100','00100','00100','11111'],
 'J':['00111','00010','00010','00010','10010','10010','01100'],
 'K':['10001','10010','10100','11000','10100','10010','10001'],
 'L':['10000','10000','10000','10000','10000','10000','11111'],
 'M':['10001','11011','10101','10101','10001','10001','10001'],
 'N':['10001','11001','10101','10011','10001','10001','10001'],
 'O':['01110','10001','10001','10001','10001','10001','01110'],
 'P':['11110','10001','10001','11110','10000','10000','10000'],
 'Q':['01110','10001','10001','10001','10101','10010','01101'],
 'R':['11110','10001','10001','11110','10100','10010','10001'],
 'S':['01111','10000','10000','01110','00001','00001','11110'],
 'T':['11111','00100','00100','00100','00100','00100','00100'],
 'U':['10001','10001','10001','10001','10001','10001','01110'],
 'V':['10001','10001','10001','10001','10001','01010','00100'],
 'W':['10001','10001','10001','10101','10101','10101','01010'],
 'X':['10001','10001','01010','00100','01010','10001','10001'],
 'Y':['10001','10001','01010','00100','00100','00100','00100'],
 'Z':['11111','00001','00010','00100','01000','10000','11111'],
 '.':['00000','00000','00000','00000','00000','00110','00110'],
 ' ':['00000']*7,
}

def rect(x,y,w,h,c,extra=''):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}" {extra}/>'

def text(x,y,value,size=18,c=WHITE,weight=400,extra=''):
 return f'<text x="{x}" y="{y}" fill="{c}" font-family="ui-monospace, SFMono-Regular, Consolas, monospace" font-size="{size}" font-weight="{weight}" {extra}>{escape(value)}</text>'

def pixel_text(x,y,value,scale=6,c=WHITE):
 d=[]
 for n,char in enumerate(value.upper()):
  for row,line in enumerate(FONT[char]):
   for col,bit in enumerate(line):
    if bit=='1':
     xx=x+(n*6+col)*scale; yy=y+row*scale
     d.append(f'M{xx} {yy}h{scale}v{scale}h-{scale}z')
 return f'<path fill="{c}" shape-rendering="crispEdges" d="{"".join(d)}"/>'

def star(x,y,c=MINT,size=4,delay=0):
 return f'<g class="spark" style="animation-delay:{delay}s">'+rect(x+size,y,size,size,c)+rect(x,y+size,size*3,size,c)+rect(x+size,y+size*2,size,size,c)+'</g>'

def start(w,h,title,desc):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<style>
@keyframes sparkle {{ 0%,65%,100% {{opacity:1}} 75%,90% {{opacity:.35}} }}
@keyframes hover {{ 0%,100% {{transform:translateY(0)}} 50% {{transform:translateY(-6px)}} }}
.spark {{animation:sparkle 4.8s steps(1,end) infinite}}
.buddy {{animation:hover 3.6s steps(3,end) infinite}}
@media (prefers-reduced-motion: reduce) {{ .spark,.buddy {{animation:none}} }}
</style>'''

def scene(tx=0,ty=0,scale=1):
 a=[f'<g transform="translate({tx} {ty}) scale({scale})" shape-rendering="crispEdges">']
 # Layered pixel hills and platform.
 a += [rect(0,248,392,12,'#222940'),rect(16,260,360,16,'#191f35')]
 for x,y,w,h in [(12,208,48,40),(40,192,36,56),(334,206,44,42)]:
  a.append(rect(x,y,w,h,'#26233e'))
 # E-commerce shop.
 a += [rect(95,96,212,152,'#49425f'),rect(103,104,196,144,'#c1a9c9'),
       rect(111,148,180,100,'#f4d9c7'),rect(119,164,72,64,'#444058'),
       rect(127,172,56,48,'#262d42'),rect(199,164,76,84,'#444058'),
       rect(207,172,60,76,'#292f47'),rect(251,204,8,8,PEACH)]
 # Shop window shelf, little parcels and plant.
 a += [rect(127,204,56,8,'#9b7a99'),rect(135,184,24,20,PEACH),
       rect(144,184,5,10,'#ab7183'),rect(167,180,8,24,MINT),rect(159,188,24,8,MINT)]
 # Purple striped awning and sign.
 a += [rect(83,122,236,16,'#7763a9'),rect(87,138,228,12,'#3a335b')]
 for n in range(8): a.append(rect(87+n*28,122,28,28, PURPLE if n%2==0 else '#f1dfff'))
 a += [rect(119,70,164,44,'#51456f'),rect(123,74,156,36,'#28253f'),pixel_text(138,82,'VIRALDY',3,MINT)]
 # Roof antenna: ideas becoming products.
 a += [rect(197,48,8,22,'#726292'),rect(189,32,24,20,PEACH),rect(193,24,16,8,PEACH),rect(197,36,8,8,WHITE)]
 # Delivery boxes.
 a += [rect(292,220,44,28,'#ab7385'),rect(288,208,40,36,PEACH),rect(304,208,8,15,'#bd8d83'),
       rect(330,224,28,24,'#d9a275'),rect(341,224,6,10,'#956b76')]
 # Friendly original pixel robot.
 a.append('<g class="buddy">')
 a += [rect(38,190,40,8,'#8aa7bb'),rect(30,198,56,34,MINT),rect(22,206,8,18,'#51b7af'),
       rect(86,206,8,18,'#51b7af'),rect(38,206,40,18,'#18354b'),rect(44,210,8,8,WHITE),
       rect(64,210,8,8,WHITE),rect(45,232,26,10,'#6cc9b5'),rect(37,242,12,8,MINT),
       rect(67,242,12,8,MINT),rect(54,180,8,10,'#648aab'),rect(50,172,16,8,PEACH)]
 a.append('</g>')
 # Plant and pixel flower.
 a += [rect(347,200,12,24,'#538d88'),rect(337,200,10,8,MINT),rect(359,192,10,8,MINT),
       rect(347,186,12,12,'#e9a0d5'),rect(351,190,4,4,PEACH)]
 a += [star(48,120,PEACH,4,1),star(328,68,PURPLE,4,2),star(302,28,MINT,3,3)]
 a.append('</g>')
 return ''.join(a)

def hero(mobile=False):
 w,h=(680,790) if mobile else (1280,480)
 a=[start(w,h,'Phu — Software Engineer & Founder','Original pixel-art storefront and robot. Building Viraldy. E-commerce, digital transformation, and AI integration.'),rect(0,0,w,h,INK)]
 # A pixel-cut frame and subtle night-sky grid.
 a.append('<defs><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><rect x="24" y="24" width="2" height="2" fill="#242b43"/></pattern></defs>')
 a.append(rect(0,0,w,h,'url(#grid)'))
 a += [rect(0,0,w,5,PURPLE),rect(0,0,18,18,INK),rect(w-18,0,18,18,INK),rect(0,h-18,18,18,INK),rect(w-18,h-18,18,18,INK)]
 if mobile:
  a += [rect(40,37,9,9,MINT),text(61,47,'BUILD MODE: ON',15,MINT),text(40,98,'SOFTWARE ENGINEER + FOUNDER',19,MUTED),
        pixel_text(40,132,'PHU.',12,WHITE),pixel_text(40,242,'BUILDS.',11,MINT),
        text(40,356,'Real problems. Useful products.',24,WHITE),
        text(40,398,'E-COMMERCE / DIGITAL TRANSFORMATION',15,PURPLE),text(40,423,'AI INTEGRATION',15,PURPLE),
        scene(155,454,1.14),text(40,468,'CURRENT QUEST: BUILDING VIRALDY',16,MINT)]
 else:
  a += [rect(52,43,9,9,MINT),text(74,53,'BUILD MODE: ON',15,MINT),text(1187,53,'01',16,MUTED,extra='text-anchor="end"'),
        text(52,108,'SOFTWARE ENGINEER + FOUNDER',18,MUTED),
        pixel_text(56,144,'PHU.',12,'#373b60'),pixel_text(52,140,'PHU.',12,WHITE),
        pixel_text(52,248,'BUILDS.',10,MINT),
        text(52,362,'Real problems. Useful products.',26,WHITE),
        text(52,406,'E-COMMERCE / DIGITAL TRANSFORMATION / AI',14,PURPLE),
        scene(761,131,1.1),star(682,142,MINT,5),star(730,319,PEACH,3,1)]
 a += ['</svg>']
 return ''.join(a)

(ASSETS/'hero.svg').write_text(hero(),encoding='utf-8')
(ASSETS/'hero-mobile.svg').write_text(hero(True),encoding='utf-8')

BADGES=[('nodejs','Node.js',118,MINT),('python','Python',114,PEACH),('fastapi','FastAPI',126,MINT),('nestjs','NestJS',114,'#ffacc4'),('react','React',104,'#99deff'),('nextjs','Next.js',126,WHITE),('openai','OpenAI',114,MINT),('llm','LLM integrations',226,PURPLE),('notebooks','Notebooks',150,PEACH)]
for filename,label,width,color in BADGES:
 svg=start(width,38,label,label)+f'<path d="M4 0H{width-4}V4H{width}V34H{width-4}V38H4V34H0V4H4Z" fill="#20263b"/>'
 svg+=rect(11,15,7,7,color)+text(27,24,label,14,color)+ '</svg>'
 (ASSETS/f'{filename}.svg').write_text(svg,encoding='utf-8')

footer=start(1280,98,'Keep building useful things.','Pixel trail with a flag.')+rect(0,0,1280,98,INK)
footer+=pixel_text(44,29,'KEEP BUILDING USEFUL THINGS.',5,MINT)
footer+=rect(1120,36,6,36,PURPLE)+rect(1126,36,30,18,PEACH)+rect(1100,72,66,6,'#4a4265')
footer+=star(1183,30,MINT,4,1)+'</svg>'
(ASSETS/'footer.svg').write_text(footer,encoding='utf-8')
print(f'Built {len(list(ASSETS.glob("*.svg")))} original SVG assets.')
