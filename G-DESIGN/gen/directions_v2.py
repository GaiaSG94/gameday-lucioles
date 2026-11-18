"""V2 — 3 directions repensées de zéro à partir des refs narratif-jeu + 3d-matiere."""
import gen
from gen import field, RULE, NIGHT, DATE, STREAK

UBU = '"Ubuntu Sans","Helvetica Neue","Liberation Sans",Arial,sans-serif'
MONO = '"DejaVu Sans Mono",Menlo,monospace'
SERIF = '"Noto Serif","DejaVu Serif",Georgia,serif'


def sw(hexes):
    return "".join(f'<span style="background:{h};color:{c}">{n}<br>{h}</span>' for n, h, c in hexes)


def msgs():
    return {"3": '<div class="msg">Tap where it is</div>', "4": '<div class="msg">Caught</div>',
            "5": '<div class="msg">Missed</div>'}


def css(s):
    return s.replace("UBU", UBU).replace("MONO", MONO).replace("SERIF", SERIF)


# ======================= 04 · LE BOCAL =======================
def jar(inner, size):
    return f'<div class="pool"></div><div class="table"></div><div class="jar"><div class="lid"></div><div class="neck"></div>{inner}</div>'


D4 = dict(key="v2a", num="04", slug="bocal", name="Le bocal", ver="V2",
    tagline="Le jeu est un objet : un bocal de verre posé sur une table, dans le noir, et les lucioles volent dedans.",
    why="<p>Attraper des lucioles dans un bocal, tout le monde l'a fait ou rêvé : le décor raconte la règle avant qu'on lise une ligne.</p>"
        "<p>Le bocal donne aussi une limite claire au champ de jeu, ce qui rend le suivi lisible sur un petit écran.</p>"
        "<p>Les informations sont posées autour de l'objet, en petites étiquettes reliées par un trait, comme des annotations sur une scène 3D.</p>",
    swatches=sw([("Nuit chaude", "#0c0a08", "#b9ab95"), ("Table", "#17120d", "#b9ab95"), ("Verre", "#efe4d0", "#0c0a08"), ("Luciole", "#ffbe5a", "#0c0a08")]),
    type="Sans légère (Ubuntu Sans 300) pour la règle, monospace pour les étiquettes. Tailles : 11 / 13 / 20 px. Aucun gras.<br>"
         "Refs : MemoryQuest (un objet de jeu qui brille seul dans le noir), Dairy Food (un monde miniature contenu), Igloo (étiquettes reliées à l'objet), DFY (reflets sur une matière lisse).",
    bokeh=False, wrap=jar,
    note="Le bocal est un décor, pas une fonction : rien ne change dans la règle. Hypothèses de produit inchangées (voir <code>PAGES.md</code>).",
    loading='<div class="pool"></div><div class="table"></div><div class="jar"><div class="lid"></div><div class="neck"></div></div><div class="msg">Waiting for dark</div>',
    msg=msgs(),
    css=css("""
.v2a{background:radial-gradient(55% 50% at 50% 46%,rgba(255,170,60,.15),transparent 72%),linear-gradient(#0d0b09,#060505);color:#b9ab95;font-family:UBU;font-weight:300}
.v2a .table{position:absolute;left:0;right:0;bottom:0;height:20%;background:linear-gradient(#18130e,#0a0807);border-top:1px solid rgba(255,200,120,.1)}
.v2a .pool{position:absolute;left:50%;bottom:10%;width:56%;height:12%;transform:translateX(-50%);background:radial-gradient(closest-side,rgba(255,180,80,.22),transparent);z-index:1}
.v2a .jar{position:absolute;left:50%;bottom:14%;width:44%;height:64%;transform:translateX(-50%);z-index:2;border-radius:28px 28px 44px 44px/36px 36px 56px 56px;border:1px solid rgba(255,240,220,.17);
  background:linear-gradient(90deg,rgba(255,255,255,.08),rgba(255,255,255,.015) 22%,transparent 50%,rgba(255,255,255,.02) 80%,rgba(255,255,255,.09));box-shadow:inset 0 -40px 50px rgba(255,180,80,.07),0 40px 60px -24px rgba(0,0,0,.9)}
.v2a .jar::before{content:"";position:absolute;left:10%;top:12%;width:6%;height:66%;border-radius:20px;background:linear-gradient(rgba(255,255,255,.2),rgba(255,255,255,.02));filter:blur(1px)}
.v2a .jar::after{content:"";position:absolute;right:13%;top:22%;width:2%;height:46%;border-radius:10px;background:rgba(255,255,255,.1)}
.v2a .lid{position:absolute;top:-22px;left:9%;right:9%;height:22px;border-radius:6px 6px 3px 3px;background:repeating-linear-gradient(90deg,#3d362d 0 3px,#29241e 3px 7px);box-shadow:inset 0 2px 0 rgba(255,255,255,.14)}
.v2a .neck{position:absolute;top:0;left:6%;right:6%;height:16px;border-bottom:1px solid rgba(255,240,220,.14)}
.v2a .field{inset:20px 8px 8px 8px;overflow:visible}
.v2a.tile .lid{top:-10px;height:10px}.v2a.tile .neck{height:8px}.v2a.tile .field{inset:10px 4px 4px}
.v2a .ff::before{width:84px;height:84px;background:radial-gradient(circle,rgba(255,190,90,.48) 0,rgba(255,190,90,.14) 34%,transparent 68%)}
.v2a .ff::after{width:7px;height:7px;background:#fff2d6;box-shadow:0 0 9px 3px rgba(255,190,90,.9)}
.v2a .ff.fade{opacity:.45}
.v2a.tile .ff::before{width:44px;height:44px}.v2a.tile .ff::after{width:5px;height:5px}
.v2a .tap::before{width:40px;height:40px;border:1px solid rgba(255,190,90,.85)}.v2a .tap.ok::before{box-shadow:0 0 22px rgba(255,190,90,.5)}
.v2a .ghost::before{width:12px;height:12px;border:1px dashed #ffbe5a}
.v2a .msg{position:absolute;left:0;right:0;bottom:8px;text-align:center;font:400 10px/1 MONO;letter-spacing:.14em;text-transform:uppercase;color:#efe4d0;z-index:3}
.v2a .ttl{position:absolute;top:22px;left:26px;font-size:13px;letter-spacing:.3em;text-transform:uppercase;color:#efe4d0}
.v2a .ann{position:absolute;font:400 11px/1.6 MONO;letter-spacing:.08em;text-transform:uppercase;display:flex;align-items:center;gap:12px;z-index:3}
.v2a .ann b{font-weight:400;color:#efe4d0}.v2a .ann .ln{width:64px;height:1px;background:#5a5146}
.v2a .ann.l{left:5%;top:32%}.v2a .ann.r{right:5%;top:32%;text-align:right}.v2a .ann.r2{right:5%;top:52%;text-align:right}
.v2a .hb{position:absolute;left:26px;right:26px;bottom:20px;z-index:3;text-align:center}
.v2a .rule{font-size:20px;color:#efe4d0;margin-bottom:14px}
.v2a .bar{height:1px;background:rgba(239,228,208,.16);max-width:420px;margin:0 auto}.v2a .bar span{display:block;width:45%;height:1px;background:#ffbe5a;box-shadow:0 0 6px #ffbe5a}
.v2a.g-m .jar{width:60%;height:56%;bottom:18%}.v2a.g-m .table{height:24%}
.v2a.g-m .ann{top:62px;font-size:10px}.v2a.g-m .ann .ln{display:none}.v2a.g-m .ann.l{left:18px}.v2a.g-m .ann.r{right:18px}.v2a.g-m .ann.r2{display:none}
.v2a.g-m .ttl{left:18px;top:18px;font-size:12px}.v2a.g-m .rule{font-size:16px}.v2a.g-m .hb{left:18px;right:18px}
"""))


def g4(size):
    return (jar(field(D4), size) + '<div class="ttl">Lucioles</div>'
            f'<div class="ann l"><span>Night <b>{NIGHT}</b><br>{DATE}</span><span class="ln"></span></div>'
            '<div class="ann r"><span class="ln"></span><span>Flight<br><b>0:09</b> / 0:20</span></div>'
            f'<div class="ann r2"><span class="ln"></span><span>Streak<br><b>{STREAK}</b> nights</span></div>'
            f'<div class="hb"><p class="rule">{RULE}</p><div class="bar"><span></span></div></div>')


D4["game"] = g4


# ======================= 05 · CARNET DE NUIT =======================
def sketch():
    tufts = "".join(f"M{x} 440 q 3 -13 7 -21 M{x + 5} 440 q 0 -9 -3 -15 " for x in range(0, 760, 13))
    posts = "".join(f"M{x} 440 L{x} 380 L{x + 7} 371 L{x + 14} 380 L{x + 14} 440 " for x in range(24, 300, 40))
    return ('<svg class="sk" viewBox="0 0 740 560" preserveAspectRatio="xMidYMax slice">'
            '<g fill="none" stroke="#1d1b18" stroke-linecap="round" stroke-linejoin="round">'
            '<circle cx="420" cy="78" r="24" stroke-width="1.6"/><circle cx="422" cy="77" r="25.5" stroke-width=".8" opacity=".6"/>'
            f'<path d="{posts}" stroke-width="1.6"/><path d="M10 396 L310 391 M10 420 L310 417" stroke-width="1.4"/>'
            '<path d="M640 440 C 636 400, 646 360, 640 320 M641 360 L 620 340 M641 350 L 662 330" stroke-width="1.8"/>'
            '<path d="M600 330 C 580 300, 600 262, 632 266 C 646 236, 690 244, 690 274 C 716 282, 712 324, 680 330 C 666 344, 620 344, 600 330Z" stroke-width="1.5"/>'
            f'<path d="{tufts}" stroke-width="1.2"/><path d="M0 441 L740 439" stroke-width="1.6"/>'
            '<path d="M520 470 l14 -6 M540 474 l14 -6 M560 470 l14 -6 M120 478 l12 -5 M138 482 l12 -5" stroke-width="1" opacity=".5"/></g></svg>')


D5 = dict(key="v2b", num="05", slug="carnet", name="Carnet de nuit", ver="V2",
    tagline="Une nuit d'été dessinée à l'encre dans un carnet ; les lucioles sont les seules taches de couleur, au surligneur.",
    why="<p>Le dessin au trait raconte une histoire (la clôture, l'arbre, la lune) et donne au jeu un ton à lui, chaleureux et un peu drôle, loin du jeu sombre générique.</p>"
        "<p>Sur un fond clair, le jaune du surligneur est la seule couleur : l'œil ne peut suivre que les lucioles. Celle qui s'éteint perd sa couleur et redevient un trait.</p>"
        "<p>La série se compte en bâtons, comme sur un mur ; le chrono est une étiquette épaisse à ombre portée. Risque : on quitte la nuit du brief.</p>",
    swatches=sw([("Papier", "#f2ecdf", "#1d1b18"), ("Encre", "#1d1b18", "#f2ecdf"), ("Crayon", "#8c857a", "#f2ecdf"), ("Surligneur", "#ffd23f", "#1d1b18")]),
    type="Titre en linéale condensée très grasse (Ubuntu Sans Condensed 800), le reste en Ubuntu Sans 400. Tailles : 12 / 15 / 19 / 64 px. "
         "Le titre est la seule graisse forte (écart assumé au brief).<br>"
         "Refs : Don't Look Up (dessin au trait sur fond clair, grand titre noir, boutons à ombre portée), Gapsy (griffonnages par-dessus la scène), Gemeos (dessin à la main comme ton).",
    bokeh=False, scenery=sketch(),
    note="Écart assumé au brief : fond clair et titre gras. Le grain papier est un bruit SVG inline (aucune image externe). Hypothèses de produit inchangées (voir <code>PAGES.md</code>).",
    loading=f'<div class="field">{sketch()}</div><div class="msg">Drawing tonight\'s sky</div>',
    msg=msgs(),
    css=css("""
.v2b{background-color:#f2ecdf;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0.1 0 0 0 0 0.09 0 0 0 0 0.08 0 0 0 .09 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");color:#1d1b18;font-family:UBU}
.v2b .sk{position:absolute;inset:0;width:100%;height:100%}
.v2b .ff::before{width:46px;height:42px;border-radius:48% 52% 45% 55%/55% 45% 52% 48%;background:radial-gradient(circle,#ffd23f 0 42%,rgba(255,210,63,.5) 58%,transparent 72%);mix-blend-mode:multiply}
.v2b .ff::after{width:7px;height:7px;background:#1d1b18}
.v2b .ff.fade::before{background:radial-gradient(circle,rgba(255,210,63,.4) 0 36%,transparent 64%)}
.v2b .ff.fade::after{background:transparent;border:1.4px solid #1d1b18;width:8px;height:8px}
.v2b.tile .ff::before{width:30px;height:28px}.v2b.tile .ff::after{width:5px;height:5px}
.v2b .tap::before{width:50px;height:44px;border:2px solid #1d1b18;border-radius:52% 48% 55% 45%/50% 55% 45% 50%;transform:translate(-50%,-50%) rotate(-8deg)}
.v2b .tap.ok::before{background:rgba(255,210,63,.35)}
.v2b .ghost::before{width:14px;height:14px;border:1.4px dashed #1d1b18}
.v2b .msg{position:absolute;left:0;right:0;bottom:8px;text-align:center;font-size:12px;color:#1d1b18}
.v2b .ttl{position:absolute;top:20px;left:26px}
.v2b .ttl h3{font:800 64px/.86 UBU;font-stretch:condensed;letter-spacing:-.01em;text-transform:uppercase}
.v2b .ttl p{font-size:13px;margin-top:8px;color:#5f594f}
.v2b .chip{position:absolute;top:24px;right:26px;border:2px solid #1d1b18;border-radius:20px;padding:7px 14px;font-size:14px;background:#f2ecdf;box-shadow:3px 3px 0 #1d1b18}
.v2b .hb{position:absolute;left:26px;right:26px;bottom:18px}
.v2b .rule{font-size:19px;text-align:center;margin-bottom:14px}
.v2b .row{display:flex;justify-content:space-between;align-items:center;font-size:13px;color:#5f594f}
.v2b .bar{flex:0 0 46%;height:2px;background:#8c857a;position:relative}.v2b .bar span{position:absolute;left:0;top:-4px;width:45%;height:9px;background:#ffd23f;mix-blend-mode:multiply;border-radius:3px;transform:rotate(-.6deg)}
.v2b .tally{display:flex;align-items:center;gap:10px}.v2b .tally svg{width:40px;height:20px}
.v2b.g-m .ttl{left:18px;top:16px}.v2b.g-m .ttl h3{font-size:44px}.v2b.g-m .chip{right:18px;top:20px;font-size:13px}
.v2b.g-m .hb{left:18px;right:18px}.v2b.g-m .rule{font-size:16px}.v2b.g-m .bar{flex-basis:34%}
"""))

TALLY = ('<svg viewBox="0 0 40 20"><g stroke="#1d1b18" stroke-width="1.6" stroke-linecap="round" fill="none">'
         '<path d="M4 2 L4 18 M10 2 L10 18 M16 2 L16 18 M22 2 L22 18 M1 15 L25 5 M34 2 L34 18"/></g></svg>')


def g5(size):
    return (field(D5) + f'<div class="ttl"><h3>Lucioles</h3><p>Night {NIGHT} · {DATE}</p></div><div class="chip">0:09 / 0:20</div>'
            f'<div class="hb"><p class="rule">{RULE}</p><div class="row"><span class="tally">{TALLY}{STREAK} nights</span>'
            '<span class="bar"><span></span></span><span>9 of 20 s</span></div></div>')


D5["game"] = g5


# ======================= 06 · L'ÎLE =======================
DUST = "".join(f'<i style="left:{(i * 37) % 100}%;top:{(i * 53) % 70}%;opacity:{.25 + (i % 4) * .12}"></i>' for i in range(34))
ISLAND = ('<div class="dust">' + DUST + '</div>'
          '<svg class="isl" viewBox="0 0 400 260"><defs>'
          '<linearGradient id="gr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1d2b22"/><stop offset="1" stop-color="#0b120e"/></linearGradient>'
          '<linearGradient id="rk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#26221f"/><stop offset="1" stop-color="#070709"/></linearGradient>'
          '<radialGradient id="wm"><stop offset="0" stop-color="#ffd27a" stop-opacity=".42"/><stop offset="1" stop-color="#ffd27a" stop-opacity="0"/></radialGradient></defs>'
          '<path d="M24 94 C 60 118, 340 116, 382 92 L 334 140 L 302 188 L 252 214 L 212 252 L 182 206 L 132 186 L 90 150 Z" fill="url(#rk)"/>'
          '<path d="M130 120 L 182 206 M 252 214 L 300 130 M 90 150 L 120 112" stroke="rgba(255,255,255,.05)" fill="none"/>'
          '<path d="M210 250 C 212 258, 206 262, 208 270 M 182 206 C 178 222, 186 230, 180 244 M 300 188 C 304 200, 298 210, 302 222" stroke="#2a2620" fill="none"/>'
          '<path d="M20 90 C 60 62, 340 56, 386 88 C 362 112, 52 118, 20 90Z" fill="url(#gr)"/>'
          '<ellipse cx="292" cy="92" rx="96" ry="18" fill="url(#wm)"/><ellipse cx="120" cy="84" rx="70" ry="12" fill="url(#wm)" opacity=".6"/>'
          '<path d="M318 86 L 320 52 M 320 60 L 308 48 M 320 56 L 332 44" stroke="#0d1611" stroke-width="3" fill="none"/>'
          '<ellipse cx="320" cy="42" rx="22" ry="16" fill="#0f1a13"/><ellipse cx="306" cy="50" rx="14" ry="10" fill="#0f1a13"/>'
          '<path d="M40 88 l2 -7 l2 7 M70 80 l2 -6 l2 6 M200 74 l2 -7 l2 7 M250 76 l2 -6 l2 6 M360 86 l2 -6 l2 6" stroke="#2c3d31" fill="none"/></svg>')

D6 = dict(key="v2c", num="06", slug="ile", name="L'île", ver="V2",
    tagline="Un morceau de jardin suspendu dans la brume ; les lucioles volent autour et éclairent l'herbe en dessous.",
    why="<p>Le jardin flottant est un petit monde : on comprend qu'on regarde une scène, et que ce soir il s'y passe une seule chose.</p>"
        "<p>La lumière des lucioles tombe sur l'herbe : quand l'une s'éteint, la tache chaude sous elle disparaît aussi. Le décor confirme ce que l'œil a vu.</p>"
        "<p>Grand texte léger en bas à gauche, métadonnées en monospace à droite : la scène reste au centre, rien ne la couvre.</p>",
    swatches=sw([("Brume", "#0a0f1c", "#c7cdd9"), ("Roche", "#26221f", "#c7cdd9"), ("Herbe", "#1d2b22", "#c7cdd9"), ("Luciole", "#ffd27a", "#0a0f1c")]),
    type="Ubuntu Sans 300 en grand (34 px, interligne serré) pour la règle, monospace 11 px pour les métadonnées. Aucun gras.<br>"
         "Refs : Dairy Food (monde miniature flottant), Noddal (objet lumineux dans la brume, grand texte léger en bas à gauche), "
         "Yogi Suria (poussière en suspension autour d'une source), Primal Instinct (relief de pierre éclairé en rasant).",
    bokeh=False, scenery=ISLAND,
    note="Idée à trancher, hors <code>IDEE.md</code> : une île différente chaque nuit (tirée de la graine du jour) renforcerait le contenu quotidien. Non dessiné tant que ce n'est pas validé. Hypothèses de produit inchangées (voir <code>PAGES.md</code>).",
    loading=f'<div class="field">{ISLAND}</div><div class="msg">Waiting for dark</div>',
    msg=msgs(),
    css=css("""
.v2c{background:radial-gradient(70% 45% at 50% 72%,rgba(120,140,180,.14),transparent 70%),linear-gradient(#0b1020,#06080e);color:#8f97a8;font-family:UBU;font-weight:300}
.v2c .isl{position:absolute;left:50%;bottom:20%;width:58%;transform:translateX(-50%)}
.v2c .dust i{position:absolute;width:2px;height:2px;border-radius:50%;background:#c7cdd9}
.v2c .ff::before{width:110px;height:110px;background:radial-gradient(circle,rgba(255,210,122,.46) 0,rgba(255,210,122,.13) 34%,transparent 68%)}
.v2c .ff::after{width:8px;height:8px;background:#fff6df;box-shadow:0 0 10px 3px rgba(255,210,122,.9)}
.v2c .ff.fade{opacity:.45}
.v2c.tile .ff::before{width:56px;height:56px}.v2c.tile .ff::after{width:5px;height:5px}.v2c.tile .isl{bottom:8%;width:64%}
.v2c .tap::before{width:44px;height:44px;border:1px solid rgba(255,210,122,.85)}.v2c .tap.ok::before{box-shadow:0 0 24px rgba(255,210,122,.5)}
.v2c .ghost::before{width:12px;height:12px;border:1px dashed #ffd27a}
.v2c .msg{position:absolute;left:12px;bottom:10px;font:400 10px/1 MONO;letter-spacing:.14em;text-transform:uppercase;color:#c7cdd9}
.v2c .ht{position:absolute;top:22px;left:26px;right:26px;display:flex;justify-content:space-between;font:400 11px/1 MONO;letter-spacing:.14em;text-transform:uppercase}
.v2c .ht .wm{font:400 15px/1 UBU;letter-spacing:.02em;text-transform:none;color:#e6e9ef}
.v2c .hb{position:absolute;left:26px;right:26px;bottom:22px;display:flex;justify-content:space-between;align-items:flex-end}
.v2c .rule{font-size:34px;line-height:1.02;letter-spacing:-.02em;color:#e6e9ef}
.v2c .meta{font:400 11px/1.7 MONO;letter-spacing:.08em;text-transform:uppercase;text-align:right}.v2c .meta b{font-weight:400;color:#ffd27a}
.v2c .bar{position:absolute;left:0;right:0;bottom:0;height:2px;background:rgba(199,205,217,.1)}.v2c .bar span{display:block;width:45%;height:2px;background:#ffd27a}
.v2c.g-m .isl{width:86%;bottom:24%}.v2c.g-m .ht{left:18px;right:18px;top:18px}
.v2c.g-m .hb{left:18px;right:18px;bottom:20px;flex-direction:column;align-items:flex-start;gap:14px}.v2c.g-m .rule{font-size:26px}.v2c.g-m .meta{text-align:left}
"""))


def g6(size):
    return (field(D6) + f'<div class="ht"><span class="wm">Lucioles</span><span>Night {NIGHT} · {DATE}</span></div>'
            '<div class="hb"><p class="rule">Three fireflies.<br>One will fade. Catch it.</p>'
            f'<p class="meta">Flight <b>0:09</b> / 0:20<br>Streak {STREAK} nights</p></div><div class="bar"><span></span></div>')


D6["game"] = g6

if __name__ == "__main__":
    gen.build([D4, D5, D6])
