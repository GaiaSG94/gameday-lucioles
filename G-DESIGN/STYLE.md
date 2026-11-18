# STYLE — Lucioles

> **VERROUILLÉ le 2026-11-18 (`/lock`)** : fin des explorations. Toute modification passe par un `/delta` daté dans `DESIGN.md`.
> **V4 (2026-11-18) : la couche d'interface passe en style « univers », voir §9 ; §9 prime sur §2 et §5 en cas de conflit.**
> Style validé par Gaia le 2026-11-18 : direction 06 « L'île · ciel profond » (V3, `planches/v3/06-ile-ciel-profond.html`).
> Source de vérité pour toutes les planches de déclinaison et pour l'intégration dans l'app. Code de référence : `G-DESIGN/gen/directions_v3.py` et `pages_v3.py`.

## 1. Idée
Une île flottante dans un ciel profond, éclairée par une étoile froide. Trois lucioles dorées volent autour. **L'or n'appartient qu'aux lucioles** et à ce qui parle d'elles ; tout le reste est froid.

## 2. Palette

| Rôle | Hex | Usage |
|---|---|---|
| Vide | `#03040a` | Fond le plus sombre, bords du ciel |
| Ciel | `#0b1022` | Centre du ciel (dégradé radial vers Vide) |
| Nébuleuse bleue | `rgba(60,100,140,.48)` | Tache floue (flou 40 px), jamais nette |
| Nébuleuse violette | `rgba(100,54,104,.36)` | Idem |
| Étoile | `#dfe8ff` | Étoiles, étoile principale, liseré de lumière sur l'île |
| Herbe éclairée → ombre | `#4b6b52` → `#0c140f` | Dessus de l'île, de gauche (lumière) à droite |
| Roche éclairée / mi-teinte / ombre | `#6a5d50` / `#3a332c` / `#1a1715` | Trois faces du dessous de l'île |
| Texte fort | `#eef1f6` | Titres, règle |
| Texte courant | `#a9b2c4` | Métadonnées, texte secondaire |
| Texte éteint | `#6f7889` | Étapes à venir, désactivé |
| Filet | `rgba(169,178,196,.18)` | Bords de pastilles, de panneaux |
| Panneau verre | `rgba(8,11,24,.72)` + flou 10 px | Cartes posées sur le ciel |
| **Luciole (accent unique)** | `#ffd27a` | Lucioles, traînées, étape en cours, bouton principal, chiffres clés |
| Cœur de luciole | `#fff6df` | Point central |

Règle : une seule couleur d'accent. Pas d'autre couleur vive, pas de dégradé coloré dans l'interface (les dégradés sont réservés au ciel et à l'île).

## 3. Typographie
Deux voix, aucune graisse forte.

| Rôle | Police | Taille / interligne | Remarques |
|---|---|---|---|
| Règle, titres de carte | Ubuntu Sans 300 | 34 / 1.02 desktop, 26 mobile | Approche −0.02em, 2 lignes max |
| Gros chiffre (série) | Ubuntu Sans 300 | 64 / 1 | Toujours en or |
| Nom du jeu | Ubuntu Sans 400 | 16 | « Lucioles », jamais en capitales |
| Corps | Ubuntu Sans 300 | 15 / 1.4 | Phrases courtes |
| Étapes, métadonnées, étiquettes | DejaVu Sans Mono 400 | 11 (10 mobile) / 1.6 | Capitales, espacement .08–.14em |

Polices à embarquer dans l'app (pas de requête externe, CSP Devvit) : Ubuntu Sans (licence UFL) et une mono libre (DejaVu Sans Mono ou JetBrains Mono, OFL).

## 4. Grille et cadre
- Le jeu occupe tout le cadre du post. Marges intérieures : 26 px desktop, 18 px mobile.
- Haut : nom du jeu à gauche, n° de nuit à droite (ligne à 20 px du haut). Sous elle, à 52 px, la frise d'étapes centrée.
- Centre : la scène (île à 56 % de la largeur desktop, 88 % mobile, posée à 20–25 % du bas).
- Bas : règle en grand à gauche, métadonnées mono à droite (empilées sur mobile). Barre de progression de 2 px collée au bas du cadre.
- Panneaux (carte de fin, séries) : centrés, largeur max 440 px desktop, pleine largeur moins 2 × 14 px sur mobile. La scène reste visible autour, assombrie.

## 5. Composants
- **Luciole** : cœur 9 px `#fff6df` + halo radial 96 px or (55 % → 0). En train de s'éteindre : opacité .42, traînée en pointillés.
- **Traînée** : courbe de 2.4 px, dégradé or de 0 à 80 % d'opacité vers la luciole.
- **Étape** : pastille 16 px de rayon, mono 11 px, pictogramme 30 × 10. À venir : texte éteint, filet. Faite : texte courant. En cours : fond or, texte Vide, halo or.
- **Étiquette d'état** : pastille mono 10 px sur verre sombre, filet or 35 %. Version pleine or pour une réussite.
- **Bouton principal** : pilule or, texte Vide, Ubuntu 400 15 px, 12 × 22 px. Un seul par écran.
- **Bouton secondaire** : pilule à filet, texte fort, fond transparent.
- **Panneau verre** : rayon 18 px, filet, fond verre, flou 10 px.
- **Cercle de toucher** : anneau or 1.5 px, 46 px, pulsation. Attrapée : couronne d'étincelles or. Manquée : pointillé or vers le vrai point + anneau pointillé.
- **Nuits (calendrier)** : point or plein = attrapée ; anneau or = jouée, manquée ; point gris = pas jouée.

## 6. Mouvement
- Lucioles : dérive lente 7–9 s, aller-retour, jamais de saut.
- Extinction : baisse d'opacité continue sur 4 s.
- Cercle de toucher : pulsation 1.6 s.
- Apparition des panneaux : fondu + montée de 8 px, 300 ms.
- `prefers-reduced-motion` : tout s'arrête, les états restent lisibles à l'arrêt.

## 7. États
Chaque écran a ses états dessinés : chargement (« Waiting for dark », scène sans lucioles), en cours, réussite, échec, déjà joué aujourd'hui. Aucun écran vide, aucun composant non stylé.

## 8. Interdits propres à ce style
Pas de Snoo, pas de karma, pas d'emoji, pas d'or ailleurs que sur ce qui concerne les lucioles, pas de grosse étoile qui pourrait passer pour une luciole (les étoiles restent froides et immobiles).

## 9. V4 — couche d'interface « univers » (prime sur §2 et §5)

Retour de Gaia : « pas assez moderne, la couleur or des étiquettes change-la, il faut un style univers ».

**Deux lumières, deux rôles :**
- **Or `#ffd27a` = les lucioles, et seulement elles** : lucioles, leurs traînées, la couronne d'étincelles quand on en attrape une. C'est ce qu'on suit dans le jeu.
- **Lumière d'étoile = toute l'interface** : cyan `#6fd6ff` → violet `#8f86ff`, en dégradé horizontal ; texte clair `#e8f6ff`.

| Élément | Traitement |
|---|---|
| Panneau | Verre fumé `linear-gradient(160deg, rgba(24,30,64,.62), rgba(6,8,20,.78))`, rayon 22 px, **bord lumineux 1 px en dégradé** (cyan 75 % → violet 28 % → presque transparent → violet 50 %), halo cyan diffus |
| Bouton principal | Pilule pleine en dégradé cyan → violet, texte `#050714`, halo cyan, reflet blanc en haut |
| Bouton secondaire | Verre fumé + même bord lumineux, texte clair |
| Étape | À venir : verre fumé, texte `#6f7a96`. Faite : `#aab6d4`. En cours : fond dégradé à 22 %, bord lumineux, halo, texte blanc, pictogramme cyan |
| Étiquette d'état | Verre fumé, filet cyan 35 %. Réussite : pleine en dégradé |
| Mot clé de la règle (« fade », « now ») | Texte en dégradé cyan → violet |
| Gros chiffre | Dégradé vertical blanc → cyan → violet, halo cyan |
| Progression | 2–4 px, dégradé cyan → violet, halo |
| Cercle de toucher | Anneau cyan pulsant. Manqué : anneau et pointillé violets |
| Série (nuits) | **Constellation** : chaque nuit est une étoile blanche ; les nuits attrapées consécutives sont reliées par un trait en dégradé ; nuit manquée = anneau violet ; nuit pas jouée = poussière grise ; la nuit du jour est entourée |
| Nom du jeu | Ubuntu Sans 400, texte en dégradé blanc → bleu glacé |

Le ciel, l'île, la typographie, la grille et le mouvement de §1–§7 ne changent pas.
