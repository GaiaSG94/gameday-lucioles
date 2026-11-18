# REFS — Lucioles

> Références ouvertes le 2026-11-18 dans le navigateur (page d'accueil + défilement). On prend des **principes**, jamais un layout, un texte, un asset ou une marque.

## Raben Rifaie — rabenrifaie.com

Observé :
- Écran d'entrée quasi noir (≈ `#0a0a0a`), plein cadre, avec un seul élément centré : le nom du studio en petit et un bouton pilule à filet fin. Un compteur de chargement en serif italique fin dans le coin bas droit.
- Typo en deux voix seulement : une serif italique légère pour le mot qui porte l'émotion, une sans légère pour le reste. Corps petits (≈ 13–15 px), aucune graisse forte, beaucoup de vide autour.
- Après l'entrée, une scène 3D sombre (collines en clair-obscur) où **une seule source de lumière** pâle et chaude, une sphère lumineuse, attire l'œil. Elle bouge lentement avec le défilement.
- Interface minimale posée sur la scène : boutons ronds à filet, une pilule pleine claire, rien d'autre.

À retenir pour Lucioles :
1. **Une seule lumière** dans un fond sombre : l'œil va où est la lumière, ce qui est exactement la règle du jeu.
2. **Le vide est la mise en page** : un écran de jeu n'a besoin que du champ, d'une ligne de règle et d'un compteur.
3. **Deux voix typographiques, toutes deux légères** ; jamais de gras.
4. **Mouvement lent** : la lumière dérive, elle ne saute pas.

## Igloo — igloo.inc

Observé :
- La scène 3D ne s'est pas chargée dans le navigateur de travail (WebGL). Seuls visibles : l'écran de chargement et l'image de partage du site. **La profondeur et les sources lumineuses citées dans le brief n'ont donc pas pu être vérifiées en direct.** À revoir sur une machine où la scène tourne si cette ref devient décisive.
- Écran de chargement : fond gris bleuté uni (≈ `#a3a7b2`), un indicateur en caractères de texte (tirets, signes égal et plus) qui défilent, en monospace blanc. Le chargement est un motif, pas une barre.
- Image de partage : un seul objet au centre d'un paysage enneigé monochrome ; la profondeur vient uniquement de la **brume** (les plans lointains montent vers le gris clair) et non de la couleur. Texte d'accompagnement en monospace petit, interligne large.

À retenir pour Lucioles :
1. **La profondeur par la valeur** : plusieurs plans du même ton, du plus sombre devant au plus voilé derrière. Utile pour poser les lucioles « dans » une nuit plutôt que sur un aplat.
2. **Le monospace comme voix technique** : compteurs, minutage, n° de nuit. Il cadre sans décorer.
3. **Un état d'attente qui fait partie de l'identité** (motif de texte animé) plutôt qu'un spinner générique.

---

## V2 — 2026-11-18 · Refs du catalogue `hackatons-pipeline/REFERENCES-DESIGN.md` (catégories `narratif-jeu` + `3d-matiere`)

> Demande de Gaia : repartir de zéro en s'appuyant sur les refs « narratif jeu » et « 3D matière » du catalogue. Lues sur les captures 1440 de `REFERENCES-CAPTURES/` (branche `main` du dépôt hackatons-pipeline), pas sur les sites en ligne. Seules les refs effectivement utilisées sont détaillées.

### narratif-jeu

- **MemoryQuest** : une borne d'arcade seule au centre, dans le noir, entourée d'un halo coloré flou. Le jeu est **un objet** qu'on regarde avant d'être un écran. Retenu pour 04 (le bocal comme objet de jeu).
- **Dairy Food Bulgaria** : un monde miniature complet posé sur une île flottante au milieu des nuages. **Un monde contenu, vu d'un peu au-dessus.** Retenu pour 04 (le bocal contient la scène) et 06 (l'île).
- **Don't Look Up (jeu)** : dessin au trait noir sur fond blanc cassé, très grand titre noir et gras, boutons pilule à contour épais et ombre portée nette, une phrase de mise en situation sous le titre. **Le dessin à la main donne le ton et l'humour.** Retenu pour 05.
- **Gapsy Studio** : lettres en relief dans une salle 3D, avec des griffonnages à la main (bulle, flèche) par-dessus. **Le trait à main levée commente la scène.** Retenu pour 05.
- **Gemeos** : autocollants et dessins à la main autour d'un grand titre. Confirme le ton dessiné de 05.
- **Raben Rifaie** (capture) : une fenêtre dans une pièce claire qui ouvre sur un paysage, titre en serif italique. Confirme l'idée de « scène dans un cadre ». Non utilisé directement en V2.
- Vus, non retenus : Experience Funtech (néon saturé, trop chargé pour une règle à lire en 5 s), Matchball (objets alignés, jeu de quiz proche du trivia à éviter), Merci Studio (formes 3D décoratives), Sponge (créature photoréaliste, hors ton).

### 3d-matiere

- **Igloo** (capture, la scène se voit enfin) : un objet en blocs au centre d'un paysage gris dans la brume, avec de **petites étiquettes monospace reliées à l'objet par un trait**. Retenu pour 04 (étiquettes de nuit, vol et série autour du bocal).
- **Noddal** : un cube lumineux d'où part un faisceau, dans des nuages sombres ; **grand titre léger sur deux lignes en bas à gauche**, une ligne de métadonnées en bas. Retenu pour 06 (mise en page du texte).
- **Yogi Suria** : rochers en suspension autour d'une croix de lumière rouge, poussière de particules. **La lumière fait exister la matière autour d'elle.** Retenu pour 06 (poussière, lumière qui tombe sur l'herbe).
- **Primal Instinct** : un disque de pierre gravé éclairé en lumière rasante, presque noir. **La matière se lit par une lumière rasante faible.** Retenu pour 06 (dessous rocheux de l'île).
- **Defy the Current** : un téléphone en verre poli avec reflets nets sur fond noir. **Les reflets suffisent à dire « verre ».** Retenu pour 04 (reflets verticaux du bocal).
- **Giallo Studio** : vue aérienne d'une ville de nuit, titre « une seule fenêtre encore allumée ». Même idée que Lucioles (une lumière qui compte dans le noir) ; confirme la direction, sans élément repris.
- Vus, non retenus : Framer (interface produit), Köm (tissu irisé), Noon (vagues lumineuses), Psychoactive (fluide coloré), Shutabug (galerie en couloir).

### Reproductibilité (budget léger)
Les trois directions V2 sont en HTML/CSS/SVG inline, sans WebGL ni image : le bocal est fait de dégradés et de bordures, l'île et le dessin sont des tracés SVG. Elles se portent telles quelles dans l'app Devvit.
