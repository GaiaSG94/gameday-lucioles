"""Generate the 3 V1 planches (page Jeu) for Lucioles. Output: standalone HTML."""
import sys, pathlib

OUT = pathlib.Path(sys.argv[1])

# ---------- shared demo data ----------
NIGHT, DATE, PLAYERS, STREAK = "12", "Tue 18 Nov", "1,284", 6
RULE = "Three fireflies. One will fade. Catch it."
# firefly positions (% of field): two steady, one fading
FF = [(24, 40), (63, 26), (71, 64)]
TRAILS = [  # path d in 0..100 space, ending at firefly
    "M6 74 C 12 60, 30 66, 24 40",
    "M38 8 C 46 18, 52 34, 63 26",
    "M94 88 C 86 92, 78 80, 71 64",
]
BOKEH = [  # x, y, size px, opacity
    (8, 18, 90, .10), (36, 70, 140, .07), (82, 14, 70, .09), (90, 46, 120, .06),
    (52, 52, 46, .12), (14, 88, 60, .08), (66, 90, 100, .06), (46, 14, 34, .14),
    (30, 30, 22, .18), (78, 36, 18, .2), (58, 78, 26, .15),
]

SHEET_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#d8d7d3}
body{font-family:"Helvetica Neue","Liberation Sans",Arial,sans-serif;color:#1b1b1d;overflow-x:hidden}
.sheet{width:1980px;padding:40px 48px 56px}
.sh-head{display:grid;grid-template-columns:420px 1fr 440px;gap:40px;align-items:start;margin-bottom:32px}
.k{font:400 11px/1 "DejaVu Sans Mono",Menlo,monospace;letter-spacing:.14em;text-transform:uppercase;color:#6b6a66}
.sh-id h1{font:400 44px/1.05 "Noto Serif",Georgia,serif;margin-top:10px;letter-spacing:-.01em}
.sh-id p{margin-top:10px;font-size:14px;color:#4a4945}
.sh-why{font-size:15px;line-height:1.55;max-width:760px;color:#2a2a2c}
.sh-why p+p{margin-top:8px}
.sh-spec{display:flex;flex-direction:column;gap:10px}
.sw{display:flex;gap:8px}
.sw span{flex:1;height:48px;border-radius:4px;padding:6px;font:10px/1.2 "DejaVu Sans Mono",monospace;display:flex;align-items:flex-end;border:1px solid rgba(0,0,0,.1)}
.ty{font-size:12px;color:#4a4945;line-height:1.55}
.frames{display:flex;gap:48px;align-items:flex-start}
.fr-l{font:400 11px/1 "DejaVu Sans Mono",monospace;letter-spacing:.12em;text-transform:uppercase;color:#6b6a66;margin-bottom:12px}
.states{margin-top:44px}
.st-row{display:flex;gap:24px;align-items:flex-start;flex-wrap:wrap;margin-top:12px}
.st{display:flex;flex-direction:column;gap:8px;width:220px}
.st i{font:normal 11px/1.4 "DejaVu Sans Mono",monospace;color:#5d5c58}
.note{margin-top:28px;font-size:13px;line-height:1.55;color:#4a4945;max-width:1100px}
/* ---- neutral host chrome: light desktop feed, dark mobile feed (no logo, no mascot) ---- */
.desk{width:1440px;height:900px;background:#f5f6f7;border-radius:10px;overflow:hidden;box-shadow:0 30px 60px -30px rgba(0,0,0,.35)}
.d-top{height:56px;background:#fff;border-bottom:1px solid #e4e6e8;display:flex;align-items:center;gap:24px;padding:0 24px}
.d-logo{width:96px;height:22px;border-radius:6px;background:#dfe2e5}
.d-search{flex:0 0 560px;margin:0 auto;height:38px;border-radius:19px;background:#eef0f2;color:#8a9096;font-size:14px;display:flex;align-items:center;padding:0 18px}
.d-user{width:34px;height:34px;border-radius:50%;background:#dfe2e5}
.d-body{display:grid;grid-template-columns:240px 768px 320px;gap:28px;padding:20px 24px 0;justify-content:center}
.d-nav{display:flex;flex-direction:column;gap:14px;padding-top:8px}
.d-nav span{height:12px;border-radius:6px;background:#e3e6e9}
.d-nav span:nth-child(3n){width:70%}.d-nav span:nth-child(4n){width:55%}
.post{background:#fff;border:1px solid #e4e6e8;border-radius:12px;padding:12px 16px 4px}
.post-h{display:flex;align-items:center;gap:8px;font-size:12px;color:#6b7176;height:26px}
.post-h .av{width:22px;height:22px;border-radius:50%;background:#0a1020}
.post-h b{color:#1f2326;font-weight:600}
.post-t{font-size:18px;font-weight:600;color:#1f2326;margin:2px 0 10px;letter-spacing:-.01em}
.post-f{display:flex;gap:10px;height:42px;align-items:center;font-size:12px;font-weight:600;color:#53595e}
.post-f span{background:#eef0f2;border-radius:16px;padding:7px 12px}
.d-side .card{background:#fff;border:1px solid #e4e6e8;border-radius:12px;padding:16px;font-size:13px;color:#3b4146;line-height:1.5}
.d-side .card h4{font-size:14px;color:#1f2326;margin-bottom:6px}
.d-side .card+.card{margin-top:16px}
.d-side .ph{height:10px;border-radius:5px;background:#eceef0;margin-top:10px}
.d-side .ph.s{width:60%}
.post.stub{margin-top:16px;height:150px;padding:16px}.post.stub .ph{height:12px;border-radius:6px;background:#eceef0;margin-bottom:12px;width:40%}.post.stub .ph.l{width:75%;height:16px}
.mob{width:390px;height:844px;background:#0e0f11;border-radius:44px;overflow:hidden;box-shadow:0 30px 60px -30px rgba(0,0,0,.45);outline:10px solid #111;display:flex;flex-direction:column;color:#d7dadc}
.m-status{height:44px;display:flex;justify-content:space-between;align-items:center;padding:0 30px;font-size:14px;font-weight:600}
.m-bar{height:44px;display:flex;align-items:center;gap:12px;padding:0 14px;border-bottom:1px solid #222428;font-size:14px;font-weight:600}
.m-bar .bk{margin:0 4px 0 6px;width:10px;height:10px;border-left:2px solid #8b9095;border-bottom:2px solid #8b9095;transform:rotate(45deg)}
.m-post{padding:8px 12px 10px}
.m-post .post-h{color:#8b9095}.m-post .post-h b{color:#d7dadc}
.m-post .post-t{font-size:15px;margin:0;color:#e8eaec}
.m-game{flex:1;margin:0 0;position:relative}
.m-foot{height:50px;display:flex;gap:8px;align-items:center;padding:0 12px;font-size:12px;font-weight:600;color:#a4a9ad}
.m-foot span{background:#1d1f23;border-radius:16px;padding:7px 11px}
/* ---- field primitives ---- */
.field{position:absolute;inset:0;overflow:hidden}
.ff{position:absolute;width:0;height:0}
.ff::before,.ff::after{content:"";position:absolute;border-radius:50%;transform:translate(-50%,-50%)}
.bk{position:absolute;border-radius:50%;transform:translate(-50%,-50%)}
.trails{position:absolute;inset:0;width:100%;height:100%}
.trails path{fill:none;vector-effect:non-scaling-stroke}
.tap{position:absolute;width:0;height:0}
.tap::before{content:"";position:absolute;border-radius:50%;transform:translate(-50%,-50%)}
.ghost{position:absolute;width:0;height:0}
.ghost::before{content:"";position:absolute;border-radius:50%;transform:translate(-50%,-50%)}
.drift{animation:drift 7s ease-in-out infinite alternate}
.drift.b{animation-duration:9s;animation-delay:-3s}
.drift.c{animation-duration:8s;animation-delay:-5s}
@keyframes drift{from{translate:0 0}50%{translate:10px -8px}to{translate:-6px 6px}}
.fade::before,.fade::after{animation:dim 4s ease-in-out infinite alternate}
@keyframes dim{from{opacity:1}to{opacity:.45}}
@media (prefers-reduced-motion:reduce){.drift,.fade::before,.fade::after{animation:none}}
"""


def field(d, ffs=FF, fade_idx=2, gone=False, tap=None, ghost=None, caught=False, trails=False):
    """Field markup. d = direction key. ffs = positions; fade_idx = index of fading one."""
    h = ['<div class="field">']
    if d["bokeh"]:
        for x, y, s, o in BOKEH:
            h.append(f'<div class="bk" style="left:{x}%;top:{y}%;width:{s}px;height:{s}px;opacity:{o}"></div>')
    if d.get("scenery"):
        h.append(d["scenery"])
    if (trails or d.get("always_trails")) and d.get("trails"):
        h.append(d["trails"](fade_idx, gone))
    for i, (x, y) in enumerate(ffs):
        if i == fade_idx and gone:
            continue
        cls = "ff drift " + "abc"[i] + (" fade" if i == fade_idx else "")
        h.append(f'<div class="{cls}" style="left:{x}%;top:{y}%"></div>')
    if ghost:
        h.append(f'<div class="ghost" style="left:{ghost[0]}%;top:{ghost[1]}%"></div>')
    if tap:
        h.append(f'<div class="tap{" ok" if caught else ""}" style="left:{tap[0]}%;top:{tap[1]}%"></div>')
    h.append("</div>")
    return "".join(h)


def desk(d):
    return f"""
<div class="desk"><div class="d-top"><div class="d-logo"></div><div class="d-search">Search</div><div class="d-user"></div></div>
<div class="d-body"><div class="d-nav">{'<span></span>' * 12}</div>
<div><div class="post"><div class="post-h"><span class="av"></span><b>r/lucioles</b> · u/lucioles-app · 2h</div>
<div class="post-t">Lucioles · Night {NIGHT} · {DATE}</div>
<div class="game g-d {d['key']}" style="position:relative;height:560px;border-radius:10px;overflow:hidden">{d['game']('d')}</div>
<div class="post-f"><span>412 comments</span><span>Share</span></div></div><div class="post stub"><div class="ph"></div><div class="ph l"></div><div class="ph"></div></div></div>
<div class="d-side"><div class="card"><h4>r/lucioles</h4>One flight a night. Same sky for everyone.<div class="ph"></div><div class="ph s"></div></div>
<div class="card"><h4>Rules</h4><div class="ph"></div><div class="ph s"></div><div class="ph"></div></div></div></div></div>"""


def mob(d):
    return f"""
<div class="mob"><div class="m-status"><span>21:47</span><span>5G</span></div>
<div class="m-bar"><span class="bk"></span>r/lucioles</div>
<div class="m-post"><div class="post-h"><span class="av"></span><b>r/lucioles</b> · 2h</div><div class="post-t">Lucioles · Night {NIGHT} · {DATE}</div></div>
<div class="m-game game g-m {d['key']}">{d['game']('m')}</div>
<div class="m-foot"><span>412 comments</span><span>Share</span></div></div>"""


def states(d):
    tiles = [
        ("1 · Watch", "Les trois brillent. Rien à faire qu'à suivre.", dict(fade_idx=-1)),
        ("2 · Fading", "L'une baisse lentement, sans signal.", dict(trails=True)),
        ("3 · Gone · tap", "Le vol s'arrête. Toucher où elle est.", dict(gone=True, trails=True)),
        ("4 · Caught", "Toucher juste : elle se rallume sous le doigt.", dict(tap=FF[2], caught=True)),
        ("5 · Missed", "Toucher à côté : son vrai point réapparaît.", dict(gone=True, tap=(50, 50), ghost=FF[2])),
    ]
    out = []
    for name, cap, kw in tiles:
        msg = d["msg"].get(name[0], "")
        out.append(f'<div class="st"><div class="game tile {d["key"]}" style="position:relative;width:220px;height:170px;border-radius:8px;overflow:hidden">'
                   f'{d.get("wrap", lambda f, s: f)(field(d, **kw), "t")}{msg}</div><i>{name}<br>{cap}</i></div>')
    out.append(f'<div class="st"><div class="game tile {d["key"]}" style="position:relative;width:220px;height:170px;border-radius:8px;overflow:hidden">{d["loading"]}</div>'
               '<i>6 · Loading<br>Le ciel du jour se prépare.</i></div>')
    return "".join(out)


def page(d):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lucioles · {d.get('ver', 'V1')} · {d['num']} {d['name']}</title>
<style>{SHEET_CSS}{d['css']}</style></head><body><div class="sheet">
<div class="sh-head"><div class="sh-id"><div class="k">Lucioles · {d.get('ver', 'V1')} · page Jeu · direction {d['num']}</div><h1>{d['name']}</h1><p>{d['tagline']}</p></div>
<div class="sh-why">{d['why']}</div>
<div class="sh-spec"><div class="sw">{d['swatches']}</div><div class="ty">{d['type']}</div></div></div>
<div class="frames"><div><div class="fr-l">Desktop · 1440 × 900 · post déplié dans le feed (clair)</div>{desk(d)}</div>
<div><div class="fr-l">Mobile · 390 × 844 · feed sombre</div>{mob(d)}</div></div>
<div class="states"><div class="fr-l">États du jeu · même vol, du début à la fin</div><div class="st-row">{states(d)}</div>
<p class="note">{d['note']}</p></div>
</div></body></html>"""


def build(directions):
    OUT.mkdir(parents=True, exist_ok=True)
    for d in directions:
        (OUT / f"{d['num']}-{d['slug']}.html").write_text(page(d), encoding="utf-8")
        print("wrote", d["slug"])
