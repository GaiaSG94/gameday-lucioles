"""Étape C — déclinaison du style V3 sur les pages restantes : Post, Carte de fin, Séries & classement."""
import sys
import pathlib
import gen
import directions_v3 as v3
from gen import field, NIGHT, DATE, STREAK, FF

OUT = pathlib.Path(sys.argv[1])
CALM = dict(v3.D, always_trails=False)
PLAYERS, CAUGHT_PCT = "1,284", 61

COMP_CSS = v3.css("""
.v3 .dim{position:absolute;inset:0;background:rgba(3,4,10,.55)}
.v3 .gl{background:rgba(8,11,24,.72);border:1px solid rgba(169,178,196,.16);border-radius:18px;backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.v3 .btn{display:inline-flex;align-items:center;gap:10px;background:GOLD;color:#03040a;border-radius:24px;padding:12px 22px;font:400 15px/1 UBU;box-shadow:0 0 22px rgba(255,210,122,.3)}
.v3 .btn2{display:inline-flex;align-items:center;background:transparent;color:#eef1f6;border:1px solid rgba(169,178,196,.35);border-radius:24px;padding:11px 20px;font:400 15px/1 UBU}
.v3 .mono{font:400 11px/1.6 MONO;letter-spacing:.1em;text-transform:uppercase}
.v3 .mono b{font-weight:400;color:GOLD}
.v3 .big{font:300 64px/1 UBU;color:GOLD;letter-spacing:-.02em}
.v3 .h{font:300 34px/1.05 UBU;color:#eef1f6;letter-spacing:-.02em}
.v3 .p{font-size:15px;line-height:1.4;color:#a9b2c4}
.v3 .split{height:6px;border-radius:3px;background:rgba(169,178,196,.18);overflow:hidden}.v3 .split span{display:block;height:100%;background:GOLD}
.v3 .dots{display:flex;gap:6px}.v3 .dots i{width:9px;height:9px;border-radius:50%;background:GOLD;box-shadow:0 0 6px rgba(255,210,122,.6)}
.v3 .dots i.m{background:none;border:1.5px solid GOLD;box-shadow:none}.v3 .dots i.n{background:rgba(169,178,196,.22);box-shadow:none}
.v3 .dots i.new{animation:ripple 1.6s ease-out infinite}
.v3 .quote{border-left:2px solid GOLD;padding:6px 0 6px 12px;font:400 14px/1.4 UBU;color:#eef1f6}
.v3 .row{display:flex;justify-content:space-between;align-items:center;gap:12px}
.cmp{display:flex;gap:24px;flex-wrap:wrap;margin-top:12px}
.cmp .c{width:340px;display:flex;flex-direction:column;gap:8px}
.cmp .c .box{position:relative;height:200px;border-radius:10px;overflow:hidden;display:flex;align-items:center;justify-content:center;padding:16px}
.cmp .c i{font:normal 11px/1.4 "DejaVu Sans Mono",monospace;color:#5d5c58}
""")


def head(page_name):
    return (f'<div class="ht"><span class="wm">Lucioles</span><span>Night {NIGHT} · {DATE}</span></div>')


# ---------------- Post ----------------
def post_game(size):
    m = size == "m"
    return (field(CALM, fade_idx=-1) + head("post") + v3.steps(-1) +
            '<div class="hb"><div><p class="rule">Three fireflies.<br>One will <em>fade</em>. Catch it.</p>'
            '<div style="margin-top:18px;display:flex;gap:14px;align-items:center;flex-wrap:wrap"><span class="btn">Start tonight\'s flight</span>'
            f'<span class="mono">20 s · one try</span></div></div>'
            f'<p class="meta"><b>{PLAYERS}</b> flew tonight<br>Your streak <b>{STREAK}</b> nights</p></div>')


def post_states():
    played = (f'<div class="gl" style="padding:16px 18px;width:100%"><div class="mono">You flew tonight</div>'
              f'<div class="row" style="margin-top:8px"><span class="h" style="font-size:24px">Caught it.</span><span class="mono">Streak <b>7</b></span></div>'
              '<div class="row" style="margin-top:12px"><span class="btn2" style="padding:8px 14px;font-size:13px">See tonight\'s results</span><span class="mono">Next in 05:12</span></div></div>')
    return [("Bouton principal · repos", '<span class="btn">Start tonight\'s flight</span>', "Un seul bouton plein par écran."),
            ("Bouton principal · appuyé", '<span class="btn" style="transform:scale(.97);box-shadow:0 0 34px rgba(255,210,122,.55)">Start tonight\'s flight</span>', "Halo plus fort, échelle .97."),
            ("Déjà joué ce soir", played, "Le post montre le résultat du joueur au lieu du bouton."),
            ("Chargement", '<span class="mono">Waiting for dark</span>', "Scène sans lucioles, mot d'attente en mono.")]


# ---------------- Carte de fin ----------------
def end_card(caught, m):
    title = "Caught it." if caught else "Missed.<br>It was right there."
    dots = '<i></i>' * (7 if caught else 6) + ('' if caught else '<i class="m"></i>')
    if caught:
        dots = '<i></i>' * 6 + '<i class="new"></i>'
    streak = "7" if caught else "6"
    sub = "nights in a row · +1 tonight" if caught else "nights in a row"
    quote = f"Night {NIGHT} · {'caught it' if caught else 'missed it'} · {streak} nights"
    w = "calc(100% - 28px)" if m else "440px"
    return (f'<div class="gl card" style="position:absolute;left:{"14px" if m else "26px"};top:{"112px" if m else "64px"};width:{w};padding:{"20px" if m else "26px 28px"}">'
            f'<div class="row"><span class="mono">Night {NIGHT} · {DATE}</span><span class="tm{" ok" if caught else ""}" style="position:static">{"Caught" if caught else "Missed"}</span></div>'
            f'<p class="h" style="margin-top:14px">{title}</p>'
            f'<div class="row" style="margin-top:18px;align-items:flex-end"><div><span class="big">{streak}</span><div class="mono">{sub}</div></div><div class="dots">{dots}</div></div>'
            f'<div style="margin-top:20px"><div class="row mono"><span><b>{CAUGHT_PCT}%</b> caught it</span><span>{PLAYERS} flew</span></div>'
            f'<div class="split" style="margin-top:8px"><span style="width:{CAUGHT_PCT}%"></span></div></div>'
            f'<div style="margin-top:20px"><div class="mono">Tell the others</div><p class="quote" style="margin-top:8px">{quote}</p></div>'
            '<div class="row" style="margin-top:18px;justify-content:flex-start;gap:10px"><span class="btn">Post as comment</span><span class="btn2">Streaks</span></div>'
            '<div class="mono" style="margin-top:16px">Next flight in <b>05:12:40</b></div></div>')


def end_game(size):
    m = size == "m"
    if m:
        sc = field(v3.D, gone=True, tap=(50, 50), ghost=FF[2])
    else:
        sc = field(v3.D, tap=FF[2], caught=True)
    return sc + '<div class="dim" style="background:rgba(3,4,10,.32)"></div>' + head("end") + end_card(not m, m)


def end_states():
    first = ('<div class="gl" style="padding:16px 18px;width:100%"><div class="mono">Night 1</div><p class="h" style="font-size:24px;margin-top:6px">Caught it.</p>'
             '<div class="row" style="margin-top:10px"><span class="mono">First night · come back tomorrow</span><span class="dots"><i class="new"></i></span></div></div>')
    posted = ('<div class="gl" style="padding:16px 18px;width:100%"><p class="quote">Night 12 · caught it · 7 nights</p>'
              '<div class="mono" style="margin-top:12px">Posted to the thread</div></div>')
    return [("Première nuit", first, "Série à 1, invitation à revenir."),
            ("Commentaire publié", posted, "Le bouton disparaît, le texte publié reste visible."),
            ("Bouton · Post as comment", '<span class="btn">Post as comment</span>', "Commentaire pré-rempli, un seul toucher."),
            ("Compte à rebours", '<span class="mono" style="font-size:13px">Next flight in <b>05:12:40</b></span>', "Toujours visible en bas de la carte.")]


# ---------------- Séries & classement ----------------
NIGHTS = "ccncmcccccnccccmccccm" + "c" * 7  # 28 dernières nuits, la plus récente à la fin
TOP = [("u/nightowl_", 41), ("u/mothlight", 38), ("u/quietfield", 33), ("u/lanternjaw", 29), ("u/pebble_", 27)]


def cal(n):
    cls = {"c": "", "m": "m", "n": "n"}
    return "".join(f'<i class="{cls[k]}"></i>' for k in NIGHTS[-n:])


def board(n):
    rows = "".join(f'<div class="row lb"><span class="mono">{i + 1:02d}</span><span style="flex:1;color:#eef1f6">{u}</span><span class="mono"><b>{s}</b></span></div>'
                   for i, (u, s) in enumerate(TOP[:n]))
    return rows + f'<div class="row lb me"><span class="mono">212</span><span style="flex:1;color:#eef1f6">You</span><span class="mono"><b>{STREAK + 1}</b></span></div>'


def streak_game(size):
    m = size == "m"
    you = (f'<div class="gl" style="padding:20px"><div class="mono">Your nights</div>'
           f'<div class="row" style="margin-top:8px;align-items:flex-end"><div><span class="big">{STREAK + 1}</span><div class="mono">in a row · best <b>11</b></div></div></div>'
           f'<div class="dots cal" style="margin-top:16px">{cal(14 if m else 28)}</div>'
           '<div class="mono" style="margin-top:10px;color:#6f7889">Gold caught · ring missed · grey not played</div></div>')
    com = (f'<div class="gl" style="padding:20px"><div class="mono">Tonight · Night {NIGHT}</div>'
           f'<div class="row" style="margin-top:8px"><span class="h" style="font-size:26px">{CAUGHT_PCT}% caught it</span><span class="mono"><b>{PLAYERS}</b> flew</span></div>'
           f'<div class="split" style="margin-top:10px"><span style="width:{CAUGHT_PCT}%"></span></div>'
           f'<div class="mono" style="margin-top:18px">Longest streaks</div><div style="margin-top:6px">{board(3 if m else 5)}</div></div>')
    grid = "display:flex;flex-direction:column;gap:12px" if m else "display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start"
    pos = "left:14px;right:14px;top:56px" if m else "left:26px;right:26px;top:64px"
    return (field(CALM, fade_idx=-1) + '<div class="dim" style="background:rgba(3,4,10,.62)"></div>' + head("streaks") +
            f'<div style="position:absolute;{pos};{grid}">{you}{com}</div>')


def streak_states():
    return [("Nuit attrapée", '<div class="dots"><i></i><i></i><i class="new"></i></div>', "Point or plein ; la dernière pulse."),
            ("Nuit manquée", '<div class="dots"><i class="m"></i></div>', "Anneau or : jouée mais manquée."),
            ("Nuit non jouée", '<div class="dots"><i class="n"></i></div>', "Point gris."),
            ("Ligne « You »", f'<div style="width:100%">{board(0)}</div>', "Toujours visible, même hors du top.")]


STREAK_CSS = v3.css("""
.v3 .cal{flex-wrap:wrap;gap:7px}.v3 .cal i{width:12px;height:12px}
.v3 .lb{padding:8px 0;border-top:1px solid rgba(169,178,196,.12);font-size:15px}
.v3 .lb.me{border-top:1px dashed rgba(255,210,122,.4)}
""")

PAGES = [
    dict(num="01", slug="post", name="Post", title="Post · dans le feed",
         tagline="Le post tel qu'il apparaît dans le feed : la scène calme, la règle, un seul bouton.",
         why="<p>Avant de jouer, le post montre déjà la scène de la nuit et les trois étapes : on sait ce qu'on va faire avant de toucher.</p>"
             "<p>Le bouton or est la seule action. À droite, la preuve sociale (combien ont joué ce soir) et la série du joueur.</p>",
         game=post_game, states=post_states, note="« 20 s · one try » reprend les hypothèses n°4 et n°5 de PAGES.md."),
    dict(num="03", slug="carte-de-fin", name="Carte de fin", title="Carte de fin",
         tagline="Résultat, série, part de la communauté et commentaire en un toucher, posés sur la scène assombrie.",
         why="<p>La carte reste posée sur la scène : on voit encore où était la luciole (couronne si attrapée, pointillé si manquée).</p>"
             "<p>Le commentaire est pré-rempli sans rien dévoiler de la position : le fil du post devient le tableau des résultats de la nuit.</p>",
         game=end_game, states=end_states,
         note="Desktop : attrapée. Mobile : manquée. Ce que devient la série après un échec n'est pas tranché (question n°6 de PAGES.md) : la planche garde 6 et l'écrit."),
    dict(num="04", slug="series-classement", name="Séries & classement", title="Séries & classement",
         tagline="Ses propres nuits à gauche, la communauté du soir à droite.",
         why="<p>La série se lit comme un ciel : chaque nuit est un point, or si attrapée, anneau si manquée, gris si pas jouée.</p>"
             "<p>Côté communauté : la part de joueurs qui l'ont attrapée ce soir et les plus longues séries, avec la ligne du joueur toujours visible.</p>",
         game=streak_game, states=streak_states,
         note="Classement par longueur de série, faute d'un score chiffré (question n°3). Pseudos de démo."),
]


def comp_band(items):
    return "".join(f'<div class="c"><div class="box v3">{html}</div><i>{t}<br>{cap}</i></div>' for t, html, cap in items)


def page(p):
    d = dict(v3.D, key="v3", game=p["game"])
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lucioles · V3 · {p['num']} {p['name']}</title>
<style>{gen.SHEET_CSS}{v3.D['css']}{COMP_CSS}{STREAK_CSS}</style></head><body><div class="sheet">
<div class="sh-head"><div class="sh-id"><div class="k">Lucioles · V3 · déclinaison · page {p['num']}</div><h1>{p['title']}</h1><p>{p['tagline']}</p></div>
<div class="sh-why">{p['why']}</div><div class="sh-spec"><div class="sw">{v3.D['swatches']}</div><div class="ty">Style : <code>STYLE.md</code> (V3 validée).</div></div></div>
<div class="frames"><div><div class="fr-l">Desktop · 1440 × 900 · feed clair</div>{gen.desk(d)}</div>
<div><div class="fr-l">Mobile · 390 × 844 · feed sombre</div>{gen.mob(d)}</div></div>
<div class="states"><div class="fr-l">Composants et états de la page</div><div class="cmp">{comp_band(p['states']())}</div>
<p class="note">{p['note']}</p></div></div></body></html>"""


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for p in PAGES:
        (OUT / f"{p['num']}-{p['slug']}.html").write_text(page(p), encoding="utf-8")
        print("wrote", p["slug"])
