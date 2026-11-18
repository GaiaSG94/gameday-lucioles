import gen
from gen import field, RULE, NIGHT, DATE, STREAK, TRAILS, FF

SANS = '"Helvetica Neue","Liberation Sans",Arial,sans-serif'
MONO = '"DejaVu Sans Mono",Menlo,monospace'
SERIF = '"Noto Serif","DejaVu Serif",Georgia,serif'


def sw(hexes):
    return "".join(f'<span style="background:{h};color:{c}">{n}<br>{h}</span>' for n, h, c in hexes)


def msgs(cls):
    return {"3": f'<div class="{cls}">Tap where it is</div>',
            "4": f'<div class="{cls}">Caught</div>',
            "5": f'<div class="{cls}">Missed</div>'}


# ======================= 01 · BOKEH (direction de départ) =======================
D1 = dict(key="d01", num="01", slug="bokeh", name="Bokeh",
    tagline="Direction de départ poussée au bout : nuit d'encre, une seule lumière citron, le flou comme décor.",
    why="<p>La nuit est un champ de taches floues ; seules les trois lucioles sont nettes. L'œil sait tout de suite quoi suivre : ce qui est net.</p>"
        "<p>Le texte est léger et large, posé dans les coins, pour laisser le centre au vol. Une seule ligne de règle, un fil de progression, une série en points.</p>"
        "<p>Risque : le flou de fond peut se confondre avec la luciole qui s'éteint ; le contraste net / flou doit rester franc.</p>",
    swatches=sw([("Nuit", "#0a1020", "#c9cdb8"), ("Ombre", "#161e33", "#c9cdb8"), ("Luciole", "#e9f27a", "#0a1020"), ("Brume", "#c9cdb8", "#0a1020")]),
    type=f"Une seule famille sans, graisse 300, capitales espacées (.32em) pour le nom, bas de casse pour la règle. Tailles : 11 / 13 / 17 / 22 px. Aucun gras.<br>Mouvement : dérive lente (7–9 s), baisse de lumière sur 4 s.",
    bokeh=True,
    note="Hypothèses de produit visibles sur la planche (voir <code>PAGES.md</code>) : la luciole éteinte continue de voler ; on touche l'endroit où on la croit ; résultat attrapée / manquée seulement ; vol de 20 s.",
    loading='<div class="field"><div class="ff drift a" style="left:50%;top:46%;opacity:.6"></div></div><div class="msg">Waiting for dark</div>',
    msg=msgs("msg"),
    css=f"""
.d01{{background:radial-gradient(120% 90% at 50% 112%,#161e33 0%,#0a1020 64%);color:#c9cdb8;font-family:{SANS};font-weight:300}}
.d01 .bk{{background:radial-gradient(circle,rgba(233,242,122,.55) 0%,rgba(233,242,122,.4) 58%,rgba(233,242,122,.6) 64%,transparent 69%);filter:blur(2.5px)}}
.d01 .ff::before{{width:120px;height:120px;background:radial-gradient(circle,rgba(233,242,122,.42) 0,rgba(233,242,122,.13) 32%,transparent 68%)}}
.d01 .ff::after{{width:9px;height:9px;background:#f7fbd0;box-shadow:0 0 10px 3px rgba(233,242,122,.85)}}
.d01 .ff.fade{{opacity:.5}}
.d01.tile .ff::before{{width:64px;height:64px}}.d01.tile .ff::after{{width:6px;height:6px}}
.d01 .tap::before{{width:46px;height:46px;border:1px solid rgba(233,242,122,.75)}}
.d01 .tap.ok::before{{box-shadow:0 0 28px rgba(233,242,122,.45),inset 0 0 18px rgba(233,242,122,.25)}}
.d01 .ghost::before{{width:14px;height:14px;border:1px dashed rgba(233,242,122,.7)}}
.d01 .msg{{position:absolute;left:0;right:0;bottom:12px;text-align:center;font-size:12px;letter-spacing:.08em;color:#c9cdb8}}
.d01 .ht{{position:absolute;top:22px;left:26px;right:26px;display:flex;justify-content:space-between;font-size:12px;letter-spacing:.32em;text-transform:uppercase}}
.d01 .ht .r{{letter-spacing:.12em}}
.d01 .hb{{position:absolute;left:26px;right:26px;bottom:22px}}
.d01 .rule{{font-size:22px;letter-spacing:.02em;color:#eef1d8;text-align:center;margin-bottom:22px}}
.d01 .bar{{height:1px;background:rgba(201,205,184,.22)}}.d01 .bar span{{display:block;height:1px;width:45%;background:#e9f27a;box-shadow:0 0 6px #e9f27a}}
.d01 .row{{display:flex;justify-content:space-between;align-items:center;margin-top:12px;font-size:12px;letter-spacing:.1em}}
.d01 .dots{{display:flex;gap:6px;align-items:center}}.d01 .dots i{{width:5px;height:5px;border-radius:50%;background:#e9f27a;opacity:.85}}
.d01 .dots i.o{{background:none;border:1px solid #e9f27a;opacity:.6}}.d01 .dots em{{font-style:normal;margin-left:8px}}
.d01.g-m .ht{{top:16px;left:18px;right:18px;font-size:11px}}.d01.g-m .hb{{left:18px;right:18px;bottom:18px}}
.d01.g-m .rule{{font-size:17px;margin-bottom:18px;padding:0 10px}}
""")


def g1(size):
    dots = "<i></i>" * STREAK + '<i class="o"></i>'
    return (field(D1) +
            f'<div class="ht"><span>Lucioles</span><span class="r">Night {NIGHT}</span></div>'
            f'<div class="hb"><p class="rule">{RULE}</p><div class="bar"><span></span></div>'
            f'<div class="row"><span class="dots">{dots}<em>{STREAK}-night streak</em></span><span>0:09 / 0:20</span></div></div>')


D1["game"] = g1


# ======================= 02 · LONGUE POSE =======================
def trails02(fade_idx, gone):
    defs, paths = [], []
    for i, dpath in enumerate(TRAILS):
        nums = dpath.replace("M", "").replace("C", "").replace(",", " ").split()
        x1, y1, x2, y2 = nums[0], nums[1], nums[-2], nums[-1]
        defs.append(f'<linearGradient id="t{i}" gradientUnits="userSpaceOnUse" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">'
                    f'<stop offset="0" stop-color="#ffb547" stop-opacity="0"/><stop offset="1" stop-color="#ffb547" stop-opacity=".9"/></linearGradient>')
        extra = ' stroke-dasharray="1 6" stroke-linecap="round" opacity=".7"' if i == fade_idx else ""
        if i == fade_idx and gone:
            extra = ' stroke-dasharray="1 9" stroke-linecap="round" opacity=".45"'
        paths.append(f'<path d="{dpath}" stroke="url(#t{i})" stroke-width="2"{extra}/>')
    return (f'<svg class="trails" viewBox="0 0 100 100" preserveAspectRatio="none"><defs>{"".join(defs)}</defs>{"".join(paths)}</svg>')


D2 = dict(key="d02", num="02", slug="longue-pose", name="Longue pose",
    tagline="Comme une photo de nuit en pose longue : chaque luciole laisse sa traînée, celle qui s'éteint laisse des pointillés.",
    why="<p>Le vol se lit après coup : les traînées gardent le chemin des dernières secondes, ce qui aide à suivre sans rendre le jeu trivial.</p>"
        "<p>La luciole qui s'éteint se trahit par sa traînée qui se casse en pointillés ; c'est le seul signe, et il est visuel, pas textuel.</p>"
        "<p>Voix monospace de viseur (n° de nuit, temps de pose, série) : précis et calme, très loin du template de jeu mobile.</p>",
    swatches=sw([("Noir", "#050607", "#7b7f88"), ("Gris viseur", "#7b7f88", "#050607"), ("Ambre", "#ffb547", "#050607"), ("Papier", "#e6e1d6", "#050607")]),
    type=f"Une seule famille monospace, graisse normale, capitales espacées pour les métadonnées, bas de casse pour la règle. Tailles : 10 / 12 / 15 / 20 px.<br>Mouvement : la traînée s'efface sur 3 s derrière chaque lumière.",
    bokeh=False, always_trails=True, trails=trails02,
    scenery='<div class="vf tl"></div><div class="vf tr"></div><div class="vf bl"></div><div class="vf br"></div>',
    note="S'écarte de la palette de départ (ambre au lieu de citron, noir neutre au lieu de bleu nuit) pour que la lumière tire vers la flamme et la photo. Mêmes hypothèses de produit que les autres planches (voir <code>PAGES.md</code>).",
    loading='<div class="field"><div class="vf tl"></div><div class="vf tr"></div><div class="vf bl"></div><div class="vf br"></div></div><div class="msg c">Exposing 06 / 20</div>',
    msg=msgs("msg"),
    css=f"""
.d02{{background:#050607;color:#7b7f88;font-family:{MONO}}}
.d02 .ff::before{{width:30px;height:30px;background:radial-gradient(circle,rgba(255,181,71,.55) 0,rgba(255,181,71,.12) 45%,transparent 70%)}}
.d02 .ff::after{{width:6px;height:6px;background:#fff4dc;box-shadow:0 0 8px 2px #ffb547}}
.d02 .ff.fade{{opacity:.45}}
.d02 .vf{{position:absolute;width:18px;height:18px;border-color:#3a3d44;border-style:solid;border-width:0}}
.d02 .vf.tl{{top:14px;left:14px;border-top-width:1px;border-left-width:1px}}.d02 .vf.tr{{top:14px;right:14px;border-top-width:1px;border-right-width:1px}}
.d02 .vf.bl{{bottom:14px;left:14px;border-bottom-width:1px;border-left-width:1px}}.d02 .vf.br{{bottom:14px;right:14px;border-bottom-width:1px;border-right-width:1px}}
.d02 .tap::before{{width:30px;height:30px;border:1px solid #ffb547;border-radius:0}}
.d02 .tap.ok::before{{box-shadow:0 0 18px rgba(255,181,71,.45)}}
.d02 .ghost::before{{width:10px;height:10px;border:1px dashed #ffb547;border-radius:0}}
.d02 .msg{{position:absolute;left:0;right:0;bottom:24px;text-align:center;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#e6e1d6}}
.d02 .msg.c{{bottom:auto;top:46%;color:#7b7f88}}
.d02 .ht{{position:absolute;top:30px;left:42px;right:42px;display:flex;justify-content:space-between;font-size:11px;letter-spacing:.16em;text-transform:uppercase}}
.d02 .ht b{{font-weight:400;color:#e6e1d6}}.d02 .ht .rec::before{{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:#ffb547;margin-right:8px;vertical-align:1px}}
.d02 .hb{{position:absolute;left:42px;right:42px;bottom:30px}}
.d02 .rule{{font-size:15px;color:#e6e1d6;margin-bottom:16px}}
.d02 .ticks{{display:flex;gap:4px}}.d02 .ticks i{{flex:1;height:8px;border-left:1px solid #2c2f35}}.d02 .ticks i.on{{border-color:#ffb547}}
.d02 .row{{display:flex;justify-content:space-between;margin-top:10px;font-size:10px;letter-spacing:.16em;text-transform:uppercase}}
.d02 .row b{{font-weight:400;color:#e6e1d6}}
.d02.g-m .ht{{top:24px;left:30px;right:30px;font-size:10px;flex-wrap:wrap;gap:6px}}.d02.g-m .hb{{left:30px;right:30px;bottom:26px}}
.d02.g-m .rule{{font-size:13px;line-height:1.4}}
""")


def g2(size):
    ticks = "".join('<i class="on"></i>' if i < 9 else "<i></i>" for i in range(20))
    return (field(D2, trails=True) +
            f'<div class="ht"><span>Lucioles <b>N°0{NIGHT}</b></span><span class="rec">Exp <b>00:09.4</b> / 00:20.0</span></div>'
            f'<div class="hb"><p class="rule">{RULE}</p><div class="ticks">{ticks}</div>'
            f'<div class="row"><span>{DATE}</span><span>Streak <b>0{STREAK}</b></span></div></div>')


D2["game"] = g2


# ======================= 03 · HEURE BLEUE (s'écarte du brief) =======================
HILLS = ('<svg class="hills" viewBox="0 0 100 100" preserveAspectRatio="none">'
         '<path d="M0 38 C 18 22, 34 30, 52 24 C 70 18, 86 30, 100 22 L100 100 L0 100Z" fill="#5d6787" opacity=".75"/>'
         '<path d="M0 58 C 22 44, 40 56, 60 46 C 76 38, 90 50, 100 44 L100 100 L0 100Z" fill="#3a4462"/>'
         '<path d="M0 78 C 20 70, 44 80, 66 70 C 82 64, 94 72, 100 68 L100 100 L0 100Z" fill="#1a2034"/></svg>'
         '<div class="haze"></div>')

D3 = dict(key="d03", num="03", slug="heure-bleue", name="Heure bleue",
    tagline="S'écarte du brief : pas la nuit noire mais l'heure bleue juste après le coucher, avec des collines en plans de brume.",
    why="<p>Dans un feed sombre, un post noir disparaît ; un ciel d'heure bleue se repère d'un coup d'œil et reste lisible dans le feed clair comme dans le sombre.</p>"
        "<p>Les collines en trois plans de brume donnent de la profondeur : les lucioles volent <em>dans</em> un paysage, pas sur un aplat.</p>"
        "<p>Risque : moins de contraste qu'en pleine nuit, donc la luciole qui s'éteint se perd plus vite ; il faudra régler sa vitesse de baisse.</p>",
    swatches=sw([("Ciel haut", "#1f2840", "#eceae4"), ("Brume", "#7c809c", "#1a2034"), ("Colline", "#1a2034", "#eceae4"), ("Luciole", "#ffe9a8", "#1a2034")]),
    type=f"Deux voix légères : serif italique pour le nom et le mot clé de la règle, sans 300 pour le reste. Tailles : 11 / 13 / 18 / 26 px. Aucun gras.<br>Mouvement : dérive lente ; la brume respire à peine (12 s).",
    bokeh=False, scenery=HILLS,
    note="Écart volontaire à la palette de départ (ciel bleu-gris au lieu de nuit d'encre, luciole chaude au lieu de citron). Mêmes hypothèses de produit que les autres planches (voir <code>PAGES.md</code>).",
    loading=f'<div class="field">{HILLS}</div><div class="msg c">The light is going down</div>',
    msg=msgs("msg"),
    css=f"""
.d03{{background:linear-gradient(180deg,#1f2840 0%,#3b4767 52%,#7c809c 100%);color:#eceae4;font-family:{SANS};font-weight:300}}
.d03 .hills{{position:absolute;left:0;right:0;bottom:0;width:100%;height:50%}}
.d03 .haze{{position:absolute;left:0;right:0;bottom:26%;height:22%;background:linear-gradient(180deg,transparent,rgba(170,174,200,.18),transparent);animation:breathe 12s ease-in-out infinite alternate}}
@keyframes breathe{{to{{opacity:.5}}}}
.d03 .ff::before{{width:96px;height:96px;background:radial-gradient(circle,rgba(255,233,168,.5) 0,rgba(255,233,168,.15) 34%,transparent 68%)}}
.d03 .ff::after{{width:8px;height:8px;background:#fffbe8;box-shadow:0 0 10px 3px rgba(255,233,168,.9)}}
.d03 .ff.fade{{opacity:.5}}
.d03.tile .ff::before{{width:56px;height:56px}}.d03.tile .ff::after{{width:6px;height:6px}}
.d03 .tap::before{{width:44px;height:44px;border:1px solid rgba(255,233,168,.85)}}
.d03 .tap.ok::before{{box-shadow:0 0 26px rgba(255,233,168,.5)}}
.d03 .ghost::before{{width:12px;height:12px;border:1px dashed rgba(255,233,168,.8)}}
.d03 .msg{{position:absolute;left:0;right:0;bottom:14px;text-align:center;font:italic 400 15px/1.3 {SERIF}}}
.d03 .msg.c{{bottom:auto;top:30%}}
.d03 .ht{{position:absolute;top:20px;left:26px;right:26px;display:flex;justify-content:space-between;align-items:flex-start}}
.d03 .wm{{font:italic 400 26px/1 {SERIF};letter-spacing:.01em}}
.d03 .nt{{text-align:right;font-size:13px;line-height:1.4;letter-spacing:.04em}}.d03 .nt span{{opacity:.7}}
.d03 .hb{{position:absolute;left:26px;right:26px;bottom:22px}}
.d03 .rule{{font-size:21px;text-align:center;margin-bottom:20px}}.d03 .rule em{{font:italic 400 23px/1 {SERIF}}}
.d03 .bar{{height:1px;background:rgba(236,234,228,.25)}}.d03 .bar span{{display:block;height:1px;width:45%;background:#ffe9a8}}
.d03 .row{{display:flex;justify-content:space-between;margin-top:10px;font-size:12px;letter-spacing:.06em;opacity:.85}}
.d03.g-m .ht{{top:16px;left:18px;right:18px}}.d03.g-m .wm{{font-size:22px}}.d03.g-m .hb{{left:18px;right:18px;bottom:18px}}
.d03.g-m .rule{{font-size:17px;line-height:1.35}}.d03.g-m .rule em{{font-size:19px}}
""")


def g3(size):
    rule = RULE.replace("fade", "<em>fade</em>")
    return (field(D3) +
            f'<div class="ht"><span class="wm">Lucioles</span><span class="nt">Night {NIGHT}<br><span>{DATE}</span></span></div>'
            f'<div class="hb"><p class="rule">{rule}</p><div class="bar"><span></span></div>'
            f'<div class="row"><span>{STREAK} nights in a row</span><span>9 of 20 seconds</span></div></div>')


D3["game"] = g3

if __name__ == "__main__":
    gen.build([D1, D2, D3])
