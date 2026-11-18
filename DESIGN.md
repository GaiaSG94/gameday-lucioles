# DESIGN — Lucioles (gameday-lucioles)

> Journal de design. Versions datées, jamais écrasées. Tenu par Claude (directeur artistique), à partir de `PROMPT-DESIGN.md`.

## V1 — 2026-11-18 · Exploration de la page principale (« Jeu »)

**Statut : en attente de validation de Gaia (étape B du process, on s'arrête ici).**

### Fait
- `G-DESIGN/REFS.md` : Raben Rifaie et Igloo ouverts et décodés. Raben Rifaie : une seule lumière dans le noir, deux voix typographiques légères, mouvement lent. Igloo : la scène 3D ne s'est pas chargée (WebGL) ; seuls l'écran de chargement et l'image de partage ont été vus (profondeur par la brume, monospace comme voix technique). Limite notée dans le fichier.
- `G-DESIGN/PAGES.md` : 4 pages proposées (Post, Jeu, Carte de fin, Séries & classement), à valider. 5 questions produit ouvertes listées.
- 3 planches de la page **Jeu**, chacune avec le cadre desktop 1440 × 900 (post déplié dans un feed clair neutre) et le cadre mobile 390 × 844 (feed sombre), plus une bande de 6 états (watch, fading, gone/tap, caught, missed, loading) :
  - `G-DESIGN/planches/v1/01-bokeh.html` : direction de départ poussée au bout. Nuit `#0a1020`, luciole `#e9f27a`, fond de taches floues, seules les lucioles sont nettes.
  - `G-DESIGN/planches/v1/02-longue-pose.html` : photo de nuit en pose longue. Noir neutre, ambre unique, chaque luciole traîne sa trace ; celle qui s'éteint laisse des pointillés. Voix monospace de viseur.
  - `G-DESIGN/planches/v1/03-heure-bleue.html` : s'écarte du brief. Ciel d'heure bleue, collines en trois plans de brume, luciole chaude, serif italique + sans légère.
- Planches générées par `G-DESIGN/gen/` (`python3 G-DESIGN/gen/directions.py G-DESIGN/planches/v1`) : même feed, mêmes données de démo pour les trois, pour comparer le style seul. Les fichiers HTML restent autonomes (double-clic, sans serveur).

### Données de démo communes
Night 12, Tue 18 Nov. Trois lucioles, la troisième (bas droite) en train de s'éteindre. Vol à 0:09 sur 0:20. Série de 6 nuits. 412 commentaires sur le post. Règle affichée : « Three fireflies. One will fade. Catch it. »

### Décisions
- Feed hôte dessiné en gris neutre, sans logo, sans Snoo, sans karma (critère Reddit-y « pas on the nose »). Desktop en feed clair, mobile en feed sombre : chaque direction est jugée dans les deux contextes.
- Zéro dépendance réseau : polices système en pile (sans / serif / mono). Les polices définitives seront embarquées dans l'app à l'étape C.
- UI en anglais ; planches annotées en français. Aucun gras dans l'UI du jeu.
- Une seule couleur d'accent par direction, réservée à la lumière (lucioles, progression, toucher).

### Choix recommandé
**02 — Longue pose.** C'est la seule direction où la règle se voit sans la lire : la traînée qui se casse en pointillés désigne la luciole qui s'éteint, et c'est un signe propre au jeu, pas un effet de décor. La longueur de traînée devient aussi un réglage de difficulté que la graine du jour peut faire varier, ce qui sert la rejouabilité. La réserve : elle quitte la palette de départ (ambre au lieu de citron) et des traînées trop longues rendraient le suivi trop facile, à régler en jeu.
01 est la plus fidèle au brief et la plus douce, mais le flou de fond risque de se confondre avec la luciole qui s'éteint. 03 est la plus visible dans un feed sombre, mais le contraste réduit rend le suivi plus dur.

### Questions ouvertes (bloquantes pour l'étape C)
Voir `G-DESIGN/PAGES.md` §« Questions produit ouvertes » : ce que devient la luciole éteinte, présence de leurres, mesure du résultat, durée du vol, un seul essai par jour.

## V2 — 2026-11-18 · Repartir de zéro (page « Jeu »)

**Statut : en attente de validation de Gaia (étape B, on s'arrête ici).**

### Retour de Gaia sur V1
« Aucun des trois, repars de zéro », en s'appuyant sur les refs des catégories **narratif-jeu** et **3d-matiere** du catalogue `hackatons-pipeline/REFERENCES-DESIGN.md`. Les planches V1 restent dans `G-DESIGN/planches/v1/`, écartées, non modifiées.

### Fait
- `G-DESIGN/REFS.md` : section V2 ajoutée, refs lues sur les captures `REFERENCES-CAPTURES/narratif-jeu` et `3d-matiere`, avec ce qui est retenu, et pour quelle direction.
- 3 planches de la page **Jeu**, même cadre que V1 (desktop 1440 × 900 en feed clair, mobile 390 × 844 en feed sombre, bande de 6 états) :
  - `G-DESIGN/planches/v2/04-bocal.html` : le jeu est un objet. Un bocal de verre sur une table dans le noir, les lucioles volent dedans ; nuit, vol et série en étiquettes monospace reliées au bocal. Refs : MemoryQuest, Dairy Food, Igloo, DFY.
  - `G-DESIGN/planches/v2/05-carnet.html` : une nuit d'été dessinée à l'encre dans un carnet, lucioles au surligneur jaune, grand titre condensé, série en bâtons, chrono en étiquette à ombre portée. Refs : Don't Look Up, Gapsy, Gemeos.
  - `G-DESIGN/planches/v2/06-ile.html` : un jardin flottant dans la brume ; la lumière des lucioles tombe sur l'herbe. Grand texte léger en bas à gauche. Refs : Dairy Food, Noddal, Yogi Suria, Primal Instinct.
- Générateur : `G-DESIGN/gen/directions_v2.py` (V1 conservé dans `directions_v1.py`).

### Décisions
- Mêmes données de démo et mêmes hypothèses de produit qu'en V1, pour juger le style seul.
- Une seule couleur d'accent par direction, toujours la lumière des lucioles.
- 05 s'écarte du brief (fond clair, titre gras) : écart assumé, signalé sur la planche.
- 06 soulève une idée hors `IDEE.md` (une île différente chaque nuit, tirée de la graine) : notée comme question, pas dessinée.

### Choix recommandé
**04 — Le bocal.** C'est la direction qui réunit le mieux les deux familles de refs demandées : le récit (attraper des lucioles dans un bocal, tout le monde le comprend sans lire) et la matière (verre, reflets, lumière sur la table). Le bocal borne aussi le champ de jeu, ce qui aide le suivi sur mobile. La réserve : le champ est plus petit qu'en plein écran ; si le suivi devient trop serré sur mobile, on élargira le bocal plutôt que de le retirer.
05 est l'option la plus singulière dans un feed Reddit (fond clair, humour du dessin) mais la plus pauvre en matière 3D. 06 est la plus spectaculaire mais la plus proche des sites 3D « vitrines », avec un risque d'effet générique.

## V3 — 2026-11-18 · Direction 06 « L'île » retenue et retravaillée

**Statut : en attente de validation de Gaia (étape B, style pas encore verrouillé).**

### Retour de Gaia sur V2
Direction 06 retenue. Trois demandes : un fond qui ressemble à l'univers de façon réaliste ; l'île mieux éclairée, par une étoile par exemple, pour qu'on la voie mieux ; « visuellement je ne comprends pas le jeu » : le rendre plus visuel et plus ludique.

### Fait
- `G-DESIGN/planches/v3/06-ile-ciel-profond.html` (générateur `G-DESIGN/gen/directions_v3.py`) :
  - **Ciel profond** : Voie lactée en diagonale (poussière en bruit SVG masqué, bande sombre au milieu), trois nébuleuses froides floues, 420 étoiles de tailles et teintes variées (plus denses dans la bande), quelques étoiles à aigrettes.
  - **Lumière principale** : une étoile bleutée en haut à gauche, avec halo. L'île est éclairée par elle : liseré clair sur le bord gauche de l'herbe, roche en trois faces (gauche éclairée, centre en demi-teinte, droite dans l'ombre), arbre éclairé à gauche, petits rochers flottants. Les tâches dorées des lucioles restent sur l'herbe.
  - **Règle visuelle** : une frise de 3 étapes en haut (1 Watch, 2 One fades, 3 Tap it), l'étape en cours en or, chacune avec son pictogramme (trois points, deux points et un pointillé, une cible). Chaque luciole a une traînée qui montre qu'elle vole ; celle qui s'éteint a une traînée en pointillés.
  - Desktop montre l'étape 2 (l'une s'éteint), mobile l'étape 3 (elle a disparu, cercle pulsant « Tap where it is », texte « It went dark. Where is it now? ») : les deux cadres racontent deux moments du même vol.
  - **États** : chaque vignette a son étiquette (Watch all three, One is fading, Where is it now? Tap, Caught · streak 7, Missed · it was here, Waiting for dark). Attrapée : couronne d'étincelles. Manquée : trait pointillé du toucher vers le vrai point.

### Décisions
- L'or reste réservé aux lucioles et à ce qui les concerne (étapes, traînées, toucher) ; tout le ciel est froid, pour que les lucioles ne se confondent pas avec les étoiles.
- Toujours en CSS/SVG inline, sans image ni WebGL (budget léger, portable dans Devvit).

### Points à surveiller
- Les étoiles proches des lucioles peuvent gêner le suivi : en jeu, garder les étoiles petites et immobiles, les lucioles plus grosses et en mouvement.
- « Caught · streak 7 » suppose qu'une partie gagnée fait monter la série ; à confirmer (question ouverte n°3 de `PAGES.md`).
- Le texte d'étape suppose l'hypothèse n°1 (la luciole éteinte continue de voler et on touche où on la croit).

## V3 · déclinaison — 2026-11-18 · Étape C

**Statut : style validé par Gaia (« Oui, décline »). Pages déclinées en attente de revue ; pas de `/lock` tant que les 4 pages ne sont pas validées.**

### Fait
- `G-DESIGN/STYLE.md` : palette (hex), typographie, grille, composants, mouvement, états, interdits propres au style.
- `G-DESIGN/planches/v3/` (générateur `G-DESIGN/gen/pages_v3.py`, réutilise la scène et le CSS de `directions_v3.py`) :
  - `01-post.html` : la scène calme, la frise des 3 étapes en aperçu, la règle, un seul bouton or « Start tonight's flight » ; à droite, joueurs du soir et série. États : bouton repos / appuyé, « déjà joué ce soir », chargement.
  - `03-carte-de-fin.html` : panneau verre posé à gauche sur la scène assombrie, pour garder visible l'endroit de la luciole (couronne si attrapée, pointillé si manquée). Résultat, série en gros chiffre or + points des nuits, part de la communauté qui l'a attrapée, commentaire pré-rempli sans indice de position, « Post as comment », compte à rebours. Desktop attrapée, mobile manquée. États : première nuit, commentaire publié, bouton, compte à rebours.
  - `04-series-classement.html` : ses nuits (gros chiffre, meilleure série, calendrier de 28 nuits en points or / anneau / gris) et la communauté du soir (part attrapée, plus longues séries, ligne « You » toujours visible).
- La page Jeu validée reste `planches/v3/06-ile-ciel-profond.html`.

### Décisions
- Un seul bouton plein par écran (or) ; les autres actions en pilule à filet.
- Le commentaire pré-rempli ne dit que la nuit, le résultat et la série : rien qui aide les autres à trouver la luciole.
- Panneaux en verre sombre, la scène reste visible autour.

### Questions ouvertes ajoutées
`PAGES.md` n°6 (série après un échec) et n°7 (critère du classement).

## V4 — 2026-11-18 · Couche d'interface « univers »

**Statut : en attente de validation de Gaia.**

### Retour de Gaia sur la déclinaison V3
« Non ça va pas, c'est pas assez moderne, la couleur or des étiquettes change-la, il faut un style univers. »

### Fait
- `G-DESIGN/planches/v4/` (générateur `G-DESIGN/gen/v4.py`, surcouche CSS sur V3) : les 4 pages refaites avec la nouvelle couche : `02-jeu`, `01-post`, `03-carte-de-fin`, `04-series-classement`.
- `G-DESIGN/STYLE.md` §9 : règles de la couche univers (prime sur la palette et les composants de §2/§5).

### Décisions
- L'or reste uniquement sur les lucioles (ce qu'on suit en jeu) ; toute l'interface passe en lumière d'étoile cyan → violet. Deux couleurs, deux rôles qui ne se mélangent jamais.
- Verre fumé à bord lumineux en dégradé pour tous les panneaux, pastilles et boutons secondaires : une seule matière d'interface.
- La série devient une constellation : les nuits attrapées d'affilée sont reliées. C'est la métaphore « univers » appliquée à la donnée.
- Les pages V3 restent dans `planches/v3/`, inchangées.

### Validation — 2026-11-18
Gaia valide V4 (« Oui, valide ») : les 4 pages (Post, Jeu, Carte de fin, Séries & classement) sont validées dans `planches/v4/`. Le style n'est pas encore verrouillé (`/lock`) ; les questions produit n°1 à 7 de `PAGES.md` restent à trancher avant l'intégration.

## LOCK — 2026-11-18

Style verrouillé à la demande de Gaia (`/lock`). Référence : `G-DESIGN/STYLE.md` (§1–§7 + §9 V4) et les 4 planches validées de `G-DESIGN/planches/v4/`. Fin des explorations ; les versions V1 à V3 restent archivées dans `planches/v1` à `v3`. Toute évolution passe désormais par un `/delta` daté ici.

À trancher avant l'intégration dans l'app : questions produit n°1 à 7 de `G-DESIGN/PAGES.md`.
