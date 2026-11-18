"""V3 — direction 06 L'île retravaillée : ciel profond réaliste, île éclairée par une étoile, règle rendue visuelle."""
import random
import gen
from gen import field, NIGHT, DATE, STREAK, FF

UBU = '"Ubuntu Sans","Helvetica Neue","Liberation Sans",Arial,sans-serif'
MONO = '"DejaVu Sans Mono",Menlo,monospace'
GOLD = "#ffd27a"
TINTS = ["#ffffff", "#dfe8ff", "#c9d8ff", "#fff1dc", "#ffd9bd"]


def css(s):
    return s.replace("UBU", UBU).replace("MONO", MONO).replace("GOLD", GOLD)


def stars():
    """Champ d'étoiles déterministe : fond diffus + densité dans la bande de la Voie lactée."""
    r = random.Random(12)
    out = []
    for i in range(420):
        if i < 240:
            x, y = r.uniform(0, 1000), r.uniform(0, 760)
        else:  # concentrées le long de la bande (diagonale haut-droite -> bas-gauche)
            t = r.uniform(0, 1)
            x, y = 1000 * t + r.gauss(0, 40), 120 + 420 * t + r.gauss(0, 55)
        rad = r.choice([.45, .55, .6, .7, .8, .9, 1.1, 1.4]) if r.random() > .04 else 1.9
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rad}" fill="{r.choice(TINTS)}" opacity="{r.uniform(.25, .95):.2f}"/>')
    return "".join(out)


def spike(x, y, s, o):
    return (f'<g opacity="{o}"><circle cx="{x}" cy="{y}" r="{s * .18}" fill="#fff"/>'
            f'<path d="M{x - s} {y} L{x + s} {y} M{x} {y - s} L{x} {y + s}" stroke="#dfe8ff" stroke-width=".6"/></g>')


SKY = ('<div class="neb n1"></div><div class="neb n2"></div><div class="neb n3"></div>'
       '<svg class="sky" viewBox="0 0 1000 760" preserveAspectRatio="xMidYMid slice"><defs>'
       '<filter id="dust" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".008 .02" numOctaves="5" seed="7"/>'
       '<feColorMatrix values="0 0 0 0 .78  0 0 0 0 .8  0 0 0 0 .92  0 0 0 1.6 -.75"/></filter>'
       '<radialGradient id="band"><stop offset="0" stop-color="#fff" stop-opacity="1"/><stop offset=".55" stop-color="#fff" stop-opacity=".45"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>'
       '<mask id="bm"><ellipse cx="500" cy="330" rx="640" ry="120" fill="url(#band)" transform="rotate(25 500 330)"/></mask>'
       '<radialGradient id="key"><stop offset="0" stop-color="#eef3ff" stop-opacity=".95"/><stop offset=".08" stop-color="#cfdcff" stop-opacity=".45"/>'
       '<stop offset=".35" stop-color="#8fa6e0" stop-opacity=".1"/><stop offset="1" stop-color="#8fa6e0" stop-opacity="0"/></radialGradient></defs>'
       '<rect width="1000" height="760" filter="url(#dust)" mask="url(#bm)" opacity=".9"/>'
       '<ellipse cx="520" cy="345" rx="560" ry="16" fill="#03040a" opacity=".55" transform="rotate(25 500 330)" style="filter:blur(6px)"/>'
       + stars() + spike(830, 120, 9, .8) + spike(610, 60, 6, .6) + spike(930, 520, 7, .55) +
       '<circle cx="120" cy="150" r="300" fill="url(#key)"/>' + spike(120, 150, 34, 1) +
       '<circle cx="120" cy="150" r="3.2" fill="#fff"/></svg>')

ROCKS = "".join(f'<polygon points="{p}" fill="url(#rl)"/>' for p in [
    "40,150 52,142 60,152 50,160", "350,150 362,146 368,156 356,162", "300,236 308,230 316,238 306,244"])

ISLAND = ('<svg class="isl" viewBox="0 0 400 270"><defs>'
          '<linearGradient id="g3" x1="0" y1="0" x2="1" y2=".3"><stop offset="0" stop-color="#4b6b52"/><stop offset=".45" stop-color="#22362a"/><stop offset="1" stop-color="#0c140f"/></linearGradient>'
          '<linearGradient id="fa" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6a5d50"/><stop offset="1" stop-color="#2a241f"/></linearGradient>'
          '<linearGradient id="fb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a332c"/><stop offset="1" stop-color="#141211"/></linearGradient>'
          '<linearGradient id="fc" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a1715"/><stop offset="1" stop-color="#070708"/></linearGradient>'
          '<linearGradient id="rl" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7a6c5e"/><stop offset="1" stop-color="#1d1916"/></linearGradient>'
          '<radialGradient id="w3"><stop offset="0" stop-color="#ffd27a" stop-opacity=".5"/><stop offset="1" stop-color="#ffd27a" stop-opacity="0"/></radialGradient></defs>'
          + ROCKS +
          '<polygon points="24,94 150,112 212,262 182,210 132,190 90,152" fill="url(#fa)"/>'
          '<polygon points="150,112 262,112 254,218 212,262" fill="url(#fb)"/>'
          '<polygon points="262,112 382,92 336,142 304,192 254,218" fill="url(#fc)"/>'
          '<path d="M60 128 L 150 136 M 96 160 L 170 168 M 150 190 L 196 200" stroke="rgba(255,240,220,.12)" fill="none"/>'
          '<path d="M212 262 C 214 270, 208 274, 210 282 M 182 210 C 178 226, 186 234, 180 248" stroke="#2a2620" fill="none"/>'
          '<path d="M20 90 C 60 62, 340 56, 386 88 C 362 112, 52 118, 20 90Z" fill="url(#g3)"/>'
          '<path d="M20 90 C 60 62, 200 56, 260 60" stroke="rgba(220,232,255,.55)" stroke-width="1.2" fill="none"/>'
          '<ellipse cx="300" cy="94" rx="80" ry="15" fill="url(#w3)"/><ellipse cx="128" cy="84" rx="66" ry="12" fill="url(#w3)" opacity=".7"/>'
          '<ellipse cx="342" cy="82" rx="30" ry="6" fill="#050806" opacity=".6"/>'
          '<path d="M318 86 L 320 52 M 320 60 L 308 48 M 320 56 L 332 44" stroke="#2a2016" stroke-width="3" fill="none"/>'
          '<ellipse cx="320" cy="42" rx="22" ry="16" fill="#1b2a1f"/><ellipse cx="312" cy="38" rx="12" ry="8" fill="#3c5a43"/><ellipse cx="306" cy="50" rx="14" ry="10" fill="#16241a"/>'
          '<path d="M40 88 l2 -7 l2 7 M70 80 l2 -6 l2 6 M110 74 l2 -7 l2 7 M200 72 l2 -7 l2 7 M250 76 l2 -6 l2 6 M360 86 l2 -6 l2 6" stroke="#6f9177" fill="none"/></svg>')


def trails(fade_idx, gone):
    tails = [((14, 52), FF[0]), ((52, 18), FF[1]), ((84, 76), FF[2])]
    out = []
    for i, ((x1, y1), (x2, y2)) in enumerate(tails):
        if i == fade_idx and gone:
            continue
        dash = ' stroke-dasharray="1 5"' if i == fade_idx else ""
        out.append(f'<linearGradient id="c{i}" gradientUnits="userSpaceOnUse" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">'
                   f'<stop offset="0" stop-color="{GOLD}" stop-opacity="0"/><stop offset="1" stop-color="{GOLD}" stop-opacity=".8"/></linearGradient>'
                   f'<path d="M{x1} {y1} Q {(x1 + x2) / 2 + 4} {(y1 + y2) / 2 - 6} {x2} {y2}" stroke="url(#c{i})" stroke-width="2.4" stroke-linecap="round"{dash}/>')
    return f'<svg class="trails" viewBox="0 0 100 100" preserveAspectRatio="none">{"".join(out)}</svg>'


ICONS = {
    "watch": '<svg viewBox="0 0 30 10"><circle cx="5" cy="5" r="3" fill="GOLD"/><circle cx="15" cy="5" r="3" fill="GOLD"/><circle cx="25" cy="5" r="3" fill="GOLD"/></svg>',
    "fade": '<svg viewBox="0 0 30 10"><circle cx="5" cy="5" r="3" fill="GOLD"/><circle cx="15" cy="5" r="3" fill="GOLD"/><circle cx="25" cy="5" r="2.6" fill="none" stroke="GOLD" stroke-dasharray="1.5 1.5"/></svg>',
    "catch": '<svg viewBox="0 0 30 10"><circle cx="15" cy="5" r="4" fill="none" stroke="GOLD"/><circle cx="15" cy="5" r="1.2" fill="GOLD"/></svg>',
}


def steps(active):
    names = [("watch", "1 · Watch"), ("fade", "2 · One fades"), ("catch", "3 · Tap it")]
    out = []
    for i, (k, label) in enumerate(names):
        st = "on" if i == active else ("done" if i < active else "")
        out.append(f'<span class="stp {st}">{css(ICONS[k])}<em>{label}</em></span>')
    return '<div class="steps">' + '<i class="sl"></i>'.join(out) + '</div>'


TILE_MSG = {
    "1": '<div class="tm">Watch all three</div>',
    "2": '<div class="tm">One is fading</div>',
    "3": '<div class="tm">Where is it now? Tap</div>',
    "4": '<div class="tm ok">Caught · streak 7</div>',
    "5": ('<svg class="miss" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M50 50 L71 64" stroke="GOLD" stroke-dasharray="2 2" vector-effect="non-scaling-stroke"/></svg>'
          '<div class="tm">Missed · it was here</div>').replace("GOLD", GOLD),
}

D = dict(key="v3", num="06", slug="ile-ciel-profond", name="L'île · ciel profond", ver="V3",
    tagline="Direction 06 retenue et retravaillée : un vrai ciel profond, une étoile qui éclaire l'île, et la règle qui se lit en trois étapes.",
    why="<p>Le fond devient un ciel d'univers : Voie lactée en diagonale avec sa poussière sombre, nébuleuses froides, étoiles de tailles et de teintes différentes. Les lucioles restent les seules lumières dorées.</p>"
        "<p>Une étoile bleutée en haut à gauche sert de lumière principale : l'herbe et la face gauche de la roche sont éclairées, la droite tombe dans l'ombre. L'île a du volume et se voit au premier coup d'œil.</p>"
        "<p>La règle devient visuelle : trois étapes en haut (regarder, l'une s'éteint, toucher), des traînées qui montrent que les lucioles volent, une traînée en pointillés pour celle qui s'éteint, et un retour clair quand on touche.</p>",
    swatches=('<span style="background:#03040a;color:#c7cdd9">Vide<br>#03040a</span><span style="background:#dfe8ff;color:#03040a">Étoile<br>#dfe8ff</span>'
              '<span style="background:#4b6b52;color:#fff">Herbe éclairée<br>#4b6b52</span><span style="background:#ffd27a;color:#03040a">Luciole<br>#ffd27a</span>'),
    type="Ubuntu Sans 300 pour la règle (34 px), monospace 11 px pour les étapes et métadonnées. Aucun gras.<br>"
         "L'or est réservé aux lucioles et à ce qui les concerne (étapes, traînées, toucher). Le reste du ciel est froid.",
    bokeh=False, scenery=SKY + '<div class="isl-w">' + ISLAND + '</div>', always_trails=True, trails=trails,
    note="Desktop : étape 2, l'une s'éteint (sa traînée devient pointillée). Mobile : étape 3, elle a disparu, on touche où on la croit. "
         "Le texte « streak 7 » sur Attrapée suppose qu'une partie gagnée fait monter la série (à confirmer). Ciel et île en CSS/SVG inline, sans image ni WebGL.",
    loading=f'<div class="field">{SKY}<div class="isl-w">{ISLAND}</div></div><div class="tm">Waiting for dark</div>',
    msg=TILE_MSG,
    css=css("""
.v3{background:radial-gradient(90% 70% at 60% 40%,#0b1022,#03040a 70%);color:#a9b2c4;font-family:UBU;font-weight:300}
.v3 .sky{position:absolute;inset:0;width:100%;height:100%}
.v3 .neb{position:absolute;border-radius:50%;filter:blur(40px)}
.v3 .n1{left:40%;top:8%;width:60%;height:46%;background:radial-gradient(closest-side,rgba(60,100,140,.48),transparent)}
.v3 .n2{left:-10%;top:48%;width:56%;height:44%;background:radial-gradient(closest-side,rgba(100,54,104,.36),transparent)}
.v3 .n3{left:62%;top:58%;width:44%;height:40%;background:radial-gradient(closest-side,rgba(40,90,98,.22),transparent)}
.v3 .isl-w{position:absolute;left:50%;bottom:20%;width:56%;transform:translateX(-50%)}
.v3 .isl{display:block;width:100%;filter:drop-shadow(-6px -4px 18px rgba(170,195,255,.16))}
.v3 .trails path{fill:none}
.v3 .ff::before{width:96px;height:96px;background:radial-gradient(circle,rgba(255,210,122,.55) 0,rgba(255,210,122,.15) 34%,transparent 68%)}
.v3 .ff::after{width:9px;height:9px;background:#fff6df;box-shadow:0 0 12px 4px rgba(255,210,122,.95)}
.v3 .ff.fade{opacity:.42}
.v3.tile .ff::before{width:48px;height:48px}.v3.tile .ff::after{width:5px;height:5px}.v3.tile .isl-w{bottom:10%;width:60%}
.v3 .tap::before{width:46px;height:46px;border:1.5px solid GOLD;animation:ripple 1.6s ease-out infinite}
.v3 .tap.ok::before{animation:none;box-shadow:0 0 26px rgba(255,210,122,.6)}
.v3 .tap.ok::after{content:"";position:absolute;width:96px;height:96px;transform:translate(-50%,-50%);border-radius:50%;
  background:repeating-conic-gradient(rgba(255,210,122,.95) 0 4deg,transparent 4deg 30deg);
  -webkit-mask:radial-gradient(circle,transparent 46%,#000 48%,#000 62%,transparent 64%);mask:radial-gradient(circle,transparent 46%,#000 48%,#000 62%,transparent 64%)}
.v3.tile .tap.ok::after{width:64px;height:64px}
.v3 .ghost::before{width:14px;height:14px;border:1.5px dashed GOLD}
@keyframes ripple{from{box-shadow:0 0 0 0 rgba(255,210,122,.5)}to{box-shadow:0 0 0 18px rgba(255,210,122,0)}}
.v3 .miss{position:absolute;inset:0;width:100%;height:100%}
.v3 .tm{position:absolute;left:10px;top:10px;font:400 10px/1 MONO;letter-spacing:.12em;text-transform:uppercase;color:#e6e9ef;background:rgba(3,4,10,.55);border:1px solid rgba(255,210,122,.35);border-radius:12px;padding:5px 8px}
.v3 .tm.ok{color:#03040a;background:GOLD;border-color:GOLD}
.v3 .ht{position:absolute;top:20px;left:26px;right:26px;display:flex;justify-content:space-between;font:400 11px/1 MONO;letter-spacing:.14em;text-transform:uppercase}
.v3 .ht .wm{font:400 16px/1 UBU;letter-spacing:.02em;text-transform:none;color:#eef1f6}
.v3 .steps{position:absolute;top:52px;left:50%;transform:translateX(-50%);display:flex;align-items:center;gap:8px;white-space:nowrap}
.v3 .stp{display:flex;align-items:center;gap:8px;font:400 11px/1 MONO;letter-spacing:.08em;text-transform:uppercase;color:#6f7889;padding:7px 12px;border-radius:16px;border:1px solid rgba(169,178,196,.18);background:rgba(3,4,10,.45)}
.v3 .stp svg{width:30px;height:10px;opacity:.45}
.v3 .stp.done{color:#a9b2c4}.v3 .stp.done svg{opacity:.8}
.v3 .stp.on{color:#03040a;background:GOLD;border-color:GOLD;box-shadow:0 0 18px rgba(255,210,122,.35)}
.v3 .stp.on svg{opacity:1;filter:brightness(.15)}
.v3 .sl{width:16px;height:1px;background:rgba(169,178,196,.3)}
.v3 .hb{position:absolute;left:26px;right:26px;bottom:22px;display:flex;justify-content:space-between;align-items:flex-end}
.v3 .rule{font-size:34px;line-height:1.02;letter-spacing:-.02em;color:#eef1f6}.v3 .rule em{font-style:normal;color:GOLD}
.v3 .meta{font:400 11px/1.7 MONO;letter-spacing:.08em;text-transform:uppercase;text-align:right}.v3 .meta b{font-weight:400;color:GOLD}
.v3 .bar{position:absolute;left:0;right:0;bottom:0;height:2px;background:rgba(199,205,217,.1)}.v3 .bar span{display:block;width:45%;height:2px;background:GOLD}
.v3 .hint{position:absolute;font:400 12px/1.3 MONO;letter-spacing:.06em;text-transform:uppercase;color:GOLD;text-align:center;transform:translate(-50%,0)}
.v3.g-m .isl-w{width:88%;bottom:25%}.v3.g-m .ht{left:18px;right:18px;top:16px}
.v3.g-m .steps{top:46px;left:12px;right:12px;transform:none;justify-content:space-between;gap:4px}
.v3.g-m .stp{padding:6px 9px;font-size:10px;gap:6px;letter-spacing:.04em}.v3.g-m .stp svg{width:20px}.v3.g-m .sl{display:none}
.v3 .stp em{font-style:normal}
.v3.g-m .hb{left:18px;right:18px;bottom:20px;flex-direction:column;align-items:flex-start;gap:14px}.v3.g-m .rule{font-size:26px}.v3.g-m .meta{text-align:left}
"""))


def game(size):
    if size == "m":  # mobile : étape 3, elle a disparu, on touche
        return (field(D, gone=True, tap=(60, 50)) + '<div class="hint" style="left:60%;top:calc(50% + 34px)">Tap where it is</div>'
                + f'<div class="ht"><span class="wm">Lucioles</span><span>Night {NIGHT}</span></div>' + steps(2) +
                '<div class="hb"><p class="rule">It went dark.<br>Where is it <em>now</em>?</p>'
                f'<p class="meta">Flight <b>0:20</b> / 0:20<br>Streak {STREAK} nights</p></div><div class="bar"><span style="width:100%"></span></div>')
    return (field(D) + f'<div class="ht"><span class="wm">Lucioles</span><span>Night {NIGHT} · {DATE}</span></div>' + steps(1) +
            '<div class="hb"><p class="rule">Three fireflies.<br>One will <em>fade</em>. Catch it.</p>'
            f'<p class="meta">Flight <b>0:09</b> / 0:20<br>Streak {STREAK} nights</p></div><div class="bar"><span></span></div>')


D["game"] = game

if __name__ == "__main__":
    gen.build([D])
