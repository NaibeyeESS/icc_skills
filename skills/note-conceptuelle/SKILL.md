---
name: note-conceptuelle
description: Utiliser quand un promoteur ICC doit rédiger une note conceptuelle, un dossier de candidature, un formulaire d'appel, une lettre de soutien ou de motivation, un CV, un portfolio ou un cadre logique (concept note, « répondre à un appel », « monter le dossier de subvention »). Produit la note conceptuelle dans projet/dossiers/, au format de l'appel.
---

# /icc:note-conceptuelle — Note conceptuelle et pièces d'accompagnement conformes au bailleur

## Objectif

Rédiger une note conceptuelle (= document de 2 à 5 pages qui présente le projet à un bailleur,
souvent demandé avant ou avec le dossier complet pour une présélection) strictement conforme au
format imposé par l'appel ciblé, à partir des informations déjà réunies dans `projet/` :
`projet/fiche-projet.md`, `projet/budget/budget.md` et `projet/financements/matching-<appel>.md`.

Le skill produit aussi, à la demande, les pièces d'accompagnement courantes : cadre logique
simplifié, lettre de soutien ou de partenariat (FR/EN), lettre de motivation ou courrier
d'accompagnement (FR/EN), CV une page, structure de portfolio, et une relecture notée du dossier.

Livrable canonique : `projet/dossiers/<slug-bailleur>/note-conceptuelle.md` (slug = nom court du
bailleur ou de l'appel en minuscules sans accents, ex. `oif-fonds-image`, `if-tchad-2027`). Les pièces
vont dans le même dossier (`lettre-soutien-<partenaire>.md`, `cv-<nom>.md`, `cadre-logique.md`,
`relecture.md`).

Ce skill est porté par l'agent `icc-redaction`. Principe directeur : le format du bailleur prime
toujours sur les gabarits de ce fichier. Quand les deux divergent, suivre le bailleur.

## Quand l'utiliser / ne pas l'utiliser

Utiliser ce skill :
- quand un appel à projets précis a été identifié (idéalement après `/icc:matching-appel`) et que
  le promoteur doit déposer une note conceptuelle, un formulaire ou un dossier ;
- quand un partenaire ou un bailleur demande « une présentation du projet en quelques pages » ;
- quand il faut produire une lettre de soutien, une lettre de motivation, un CV ou un portfolio pour
  accompagner un dossier.

Ne pas l'utiliser :
- si `projet/fiche-projet.md` n'existe pas : lancer d'abord `/icc:fiche-projet` (agent
  `icc-diagnostic`) ; une note conceptuelle sans fiche repose sur du vide ;
- pour chiffrer le budget : la note reprend le budget résumé produit par `/icc:budget-cofinancement`
  (agent `icc-budget`) ; si ce budget n'existe pas, le signaler et proposer de le produire avant ou en
  parallèle ;
- pour choisir l'appel : c'est `/icc:cartographie-bailleurs` et `/icc:matching-appel` (agent
  `icc-financements`) ;
- pour rendre le texte plus naturel une fois la note conforme : `/icc:reecriture-humanisee` ;
- pour un pitch oral ou un dossier de presse : `/icc:pitch-dossier-presse` (agent
  `icc-communication`).

## Prérequis (fichiers projet/ à lire si présents, informations nécessaires)

1. `projet/ETAT.md` — lire en premier ; reprendre à l'étape indiquée si une note est en cours.
2. `projet/fiche-projet.md` — obligatoire ; source de toutes les rubriques descriptives. Ne jamais
   reposer les questions auxquelles elle répond.
3. `projet/budget/budget.md` (+ `budget.csv`) — budget par postes, cofinancement, devises.
4. `projet/financements/matching-<slug-appel>.md` — analyse d'éligibilité, points forts/faibles
   face à l'appel, pièces exigées.
5. `projet/dossiers/<slug-bailleur>/lignes-directrices.md` ou le texte de l'appel — à demander au
   promoteur (copier-coller, PDF déposé dans `projet/pieces/`) ou à récupérer par WebFetch si une
   URL officielle est fournie. Sans lignes directrices, utiliser le gabarit générique en le marquant
   « format générique — à mettre en conformité dès réception des lignes directrices ».
6. `projet/juridique/statut.md`, `projet/mise-en-oeuvre/plan.md`, `projet/communication/pitch.md`
   — si présents, réutiliser (capacité du porteur, chronogramme, formulation du pitch).
7. `projet/pieces/` — CV, statuts, lettres déjà disponibles.

Informations nécessaires non couvertes par la fiche : texte de l'appel, langue et devise exigées,
date limite, mode de dépôt (plateforme, courriel, papier), nombre de pages ou de mots, pièces
obligatoires, personne signataire.

## Procédure étape par étape

Étape 0 — Reprise. Lire `projet/ETAT.md`. Créer `projet/dossiers/<slug-bailleur>/` si besoin.
Noter dans `ETAT.md` : « Skill en cours : /icc:note-conceptuelle — étape 1 ».

Étape 1 — Obtenir les lignes directrices. Demander au promoteur le texte de l'appel (ou l'URL
officielle ; WebFetch si disponible). L'enregistrer dans
`projet/dossiers/<slug-bailleur>/lignes-directrices.md` avec la date de consultation. Si le texte
manque, poser les questions de la section « Questions à poser » et travailler avec le gabarit
générique, en le signalant.

Étape 2 — Extraire le plan imposé. Remplir le tableau « Plan imposé par l'appel » (gabarit A) :
rubriques dans l'ordre du bailleur, limite par rubrique (pages, mots, caractères), langue, devise,
police/interligne si précisés, pièces jointes, mode de dépôt, date limite (heure et fuseau horaire).
Chaque élément absent du texte de l'appel est marqué « non précisé — demander au bailleur ».

Étape 3 — Mapper rubriques → informations disponibles. Pour chaque rubrique du bailleur, indiquer
dans le tableau de mappage (gabarit A) la section de `projet/` qui la nourrit (fiche §4, budget §2…).
Identifier les trous : informations absentes partout dans `projet/`.

Étape 4 — Combler les trous. Poser au promoteur uniquement les questions correspondant aux trous
(jamais celles déjà couvertes). Si une réponse exige un travail d'un autre skill (budget, statut),
l'indiquer et, soit l'appeler, soit noter « [À COMPLÉTER après /icc:…] » dans la note.

Étape 5 — Rédiger la note. Suivre l'ordre et les intitulés exacts du bailleur. Pour chaque rubrique,
s'appuyer sur le texte-type du gabarit B, adapté aux données du projet. Règles d'écriture :
- une idée par paragraphe ; phrases courtes ; chiffres sourcés (fiche ou budget) ;
- reprendre les mots-clés de l'appel (ses priorités, ses termes) sans les plaquer artificiellement ;
- genre, inclusion (handicap, jeunes, zones rurales, langues nationales) et impact social
  apparaissent dans les rubriques bénéficiaires, résultats et méthodologie, avec des données
  ventilées et des mesures concrètes ;
- budgets toujours en FCFA et dans la devise du bailleur au taux fixe 1 EUR = 655,957 XAF/XOF ;
- aucune promesse ; parler de résultats visés et d'hypothèses.
Écrire la note rubrique par rubrique dans le fichier au fur et à mesure (reprise possible).

Étape 6 — Cadre logique si demandé. Si le bailleur exige un cadre logique (« logframe »),
produire `cadre-logique.md` avec le gabarit C, cohérent avec la fiche §5 et §8.

Étape 7 — Vérifier la conformité. Compter pages/mots par rubrique ; vérifier la langue, la devise,
les intitulés, la présence de chaque pièce exigée ; comparer avec le tableau du gabarit A. Toute
non-conformité est corrigée avant d'aller plus loin.

Étape 8 — Pièces d'accompagnement. Produire ce qui est exigé ou utile : lettres de soutien
(gabarit D, FR/EN), lettre de motivation ou courrier d'accompagnement (gabarit E), CV une page
(gabarit F), portfolio (gabarit G). Signaler les pièces qui exigent un tiers (signature d'un
partenaire, attestation d'un expert-comptable, statuts enregistrés) et le délai réaliste.

Étape 9 — Relecture notée. Appliquer la grille du gabarit H ; écrire le résultat dans
`relecture.md` ; corriger tout critère sous 3/5. Proposer `/icc:reecriture-humanisee` pour
naturaliser le texte sans toucher aux faits ni au format.

Étape 10 — Dépôt. Rappeler au promoteur : date et heure limite, format de fichier (PDF, Word,
formulaire en ligne), nommage des fichiers, signature et cachet si requis, accusé de réception à
conserver dans `projet/dossiers/<slug-bailleur>/`.

Étape 11 — Mise à jour de `projet/ETAT.md` (voir « Passage de relais »).

Mode faible connectivité : la note se rédige entièrement hors ligne à partir de la fiche et du
budget ; seules la récupération des lignes directrices et la vérification de l'appel exigent une
connexion. Enregistrer après chaque rubrique.

## Questions à poser au promoteur

À poser uniquement si la réponse n'est pas dans `projet/` :
1. Avez-vous le texte complet de l'appel (lignes directrices, formulaire, FAQ) ? Pouvez-vous le
   coller ou le déposer ? (Sinon : URL officielle ?)
2. Quelle est la date limite exacte, avec l'heure et le fuseau horaire ? Par quel canal dépose-t-on ?
3. Dans quelle langue et quelle devise le dossier doit-il être rédigé ?
4. Qui signera le dossier (représentant légal de la structure, vous-même, la structure de portage) ?
5. Le bailleur demande-t-il un cadre logique, des lettres de soutien, des CV, un portfolio, des
   devis, des états financiers ? Lesquels avez-vous déjà ?
6. Avez-vous déjà déposé un dossier auprès de ce bailleur ? Quel retour ?
7. Y a-t-il une information que vous ne souhaitez pas voir figurer dans le dossier (sécurité des
   personnes filmées, données personnelles, montant d'un contrat) ?
8. Pour les lettres de soutien : quels partenaires acceptent de signer, à quel titre, sous quel
   délai ?

## Gabarits complets

### Gabarit A — Plan imposé par l'appel et mappage (à copier dans `projet/dossiers/<slug>/plan-impose.md`)

```markdown
# Plan imposé — <nom de l'appel> — consulté le AAAA-MM-JJ (source : <URL officielle ou document>)
| Élément de forme | Exigence du bailleur | Source (page/section) |
|---|---|---|
| Langue | | |
| Devise | | |
| Longueur totale (pages/mots) | | |
| Police, taille, interligne, marges | | |
| Format de fichier et nommage | | |
| Mode de dépôt et date limite (heure, fuseau) | | |
| Pièces obligatoires | | |
| Pièces facultatives | | |
| Critères de sélection annoncés (et pondération) | | |

| N° | Rubrique du bailleur (intitulé exact) | Limite | Source dans projet/ | Trou à combler |
|---|---|---|---|---|
| 1 | | | fiche-projet.md §… | |
| 2 | | | budget.md §… | |
| … | | | | |
```

### Gabarit B — Note conceptuelle générique (3 pages, ~1 200 mots) avec texte-type par rubrique

À n'utiliser tel quel qu'en l'absence de lignes directrices ; sinon, réordonner et renommer selon
le bailleur. Les passages entre chevrons sont à remplacer ; les phrases-types sont à adapter avec les
mots du promoteur.

```markdown
# NOTE CONCEPTUELLE — <Titre du projet>
Porteur : <structure ou personne> — <ville, pays> — Contact : <courriel, téléphone>
Appel : <nom de l'appel / bailleur> — Montant demandé : <X FCFA = Y EUR> — Durée : <n mois>

## 1. Contexte et justification (≈ 200 mots)
<Situation de départ en 3-4 phrases : lieu, personnes concernées, fait marquant avec source.>
Texte-type : « À <lieu>, <groupe concerné> <fait observable, chiffre sourcé si disponible>. Pourtant,
<manque ou absence constaté>. <Le porteur> a constaté ce décalage lors de <expérience concrète :
repérage, édition précédente, atelier>. Le présent projet répond à <priorité de l'appel, reprise
avec ses mots> en <ce que le projet apporte de spécifique>. »

## 2. Objectifs (≈ 100 mots)
Objectif général : <changement large — fiche §5>.
Objectifs spécifiques :
- OS1 — <formulation SMART — fiche §5>
- OS2 — <…>
- OS3 — <…>

## 3. Résultats attendus et indicateurs (≈ 150 mots)
| Résultat | Indicateur | Valeur de départ | Cible | Moyen de vérification |
|---|---|---|---|---|
| R1 <ce qui existera> | <nombre, taux> | <0 ou valeur connue> | <fiche §8> | <liste, photo, rapport, lien> |
| R2 | | | | |
| R3 | | | | |
Texte-type : « Les indicateurs seront ventilés par sexe, âge (15-35 ans), situation de handicap et
zone (urbaine/rurale), collectés par <méthode simple> et consolidés dans le rapport final. »

## 4. Activités (≈ 150 mots)
| Activité | Résultat visé | Période | Responsable |
|---|---|---|---|
| A1 <fiche §6> | R1 | | |
| A2 | | | |
| A3 | | | |

## 5. Méthodologie et approche (≈ 150 mots)
Texte-type : « Le projet est conduit en <n> phases : <phase 1>, <phase 2>, <phase 3>. Les
<bénéficiaires> participent à <décision concrète : choix des sujets, programmation, test des
produits> par <mécanisme : comité, atelier, restitution>. Les contenus sont produits en <langues>
et <mesure d'accessibilité>. La qualité artistique est garantie par <personne, méthode, référence
vérifiable>. »

## 6. Bénéficiaires, genre et inclusion (≈ 120 mots)
| Catégorie | Nombre | dont femmes | dont jeunes | dont pers. handicapées | dont zone rurale |
|---|---|---|---|---|---|
| Directs | | | | | |
| Indirects | | | | | |
Texte-type : « <n> bénéficiaires directs, dont <x> % de femmes, sont identifiés via <méthode>.
Les obstacles connus à leur participation (<prix, distance, horaires, langue, accès physique>) sont
levés par <mesure concrète et chiffrée si possible>. L'équipe compte <x> femmes sur <n>. »

## 7. Partenariats (≈ 80 mots)
| Partenaire | Rôle | Statut | Lettre jointe |
|---|---|---|---|
| | | acquis / pressenti | oui / non |

## 8. Durabilité (≈ 100 mots)
Texte-type : « Après le financement, <ce qui continue : diffusion, ventes, éditions suivantes,
compétences acquises par l'équipe, matériel conservé par la structure>. Les recettes propres
attendues (<billetterie, ventes, droits>) couvrent <x> % des coûts récurrents à partir de <année>.
Les contenus restent accessibles via <canal>. »

## 9. Budget résumé (≈ 80 mots)
| Poste | FCFA | <Devise bailleur> | % |
|---|---|---|---|
| <reprendre les grandes masses de budget.md> | | | |
| TOTAL | | | 100 % |
Montant demandé au bailleur : <X FCFA = Y devise> soit <z> % du total. Cofinancement (= part du
budget apportée par d'autres sources ou en nature) : <sources et statut>.

## 10. Calendrier (≈ 60 mots)
| Mois | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | x | x | | | | | | | | | | |
| A2 | | | x | x | x | | | | | | | |
| A3 | | | | | | x | x | x | | | | |
| Rapports | | | | | | x | | | | | | x |

## 11. Capacité du porteur (≈ 100 mots)
Texte-type : « <Structure> existe depuis <année> (<forme juridique, récépissé n° …>). Elle a réalisé
<2-3 réalisations datées et vérifiables>. L'équipe clé : <nom, rôle, expérience en une ligne> ;
<nom, rôle>. La gestion financière est assurée par <personne/outil> ; <expert-comptable si
pertinent>. Pièces jointes : <liste>. »
```

### Gabarit C — Cadre logique simplifié (`cadre-logique.md`)

Cadre logique (en anglais « logframe ») = tableau qui relie, du haut vers le bas, l'objectif général,
les objectifs spécifiques, les résultats et les activités, et indique pour chacun comment on le
mesure et ce qu'on suppose vrai pour réussir.

```markdown
# Cadre logique — <Titre du projet>
| Niveau | Logique d'intervention | Indicateurs objectivement vérifiables | Sources de vérification | Hypothèses (ce qui doit rester vrai, hors de votre contrôle) |
|---|---|---|---|---|
| Objectif général | <changement large> | <indicateur de contribution> | <étude, presse, rapport sectoriel> | — |
| Objectif spécifique 1 | <OS1> | <indicateur, cible, échéance, ventilé F/H/jeunes> | <rapport, liste, fichier> | <ex. : accès au terrain maintenu> |
| Résultat 1.1 | <ce qui existe> | <nombre> | <preuve> | <ex. : prestataires disponibles> |
| Résultat 1.2 | | | | |
| Activités 1.1.1 … | <liste> | Moyens : <RH, matériel> | Coûts : <FCFA / devise> | <ex. : saison favorable> |
| Objectif spécifique 2 | | | | |
| Résultat 2.1 | | | | |
```

### Gabarit D — Lettre de soutien / de partenariat (FR puis EN)

```markdown
<En-tête du partenaire : nom, adresse, téléphone, courriel, logo si disponible>
<Lieu>, le <date>

Objet : Lettre de soutien au projet « <titre> » porté par <porteur>

Madame, Monsieur,

<Nom du partenaire>, <description en une ligne : nature, date de création, activité>, confirme son
soutien au projet « <titre> », présenté par <porteur> dans le cadre de <nom de l'appel>.

Nous connaissons <porteur> depuis <année / contexte précis>. <Une phrase sur une collaboration
passée ou sur ce que le partenaire a observé du projet>.

Dans le cadre de ce projet, nous nous engageons à : <engagement 1 concret — ex. : mettre à
disposition la salle X pendant Y jours> ; <engagement 2 — ex. : relayer les projections auprès de
nos membres> ; <engagement 3 facultatif, chiffré si apport en nature : valeur estimée Z FCFA>.

Ce projet rejoint nos priorités en matière de <genre, jeunesse, inclusion, patrimoine, etc.> parce
que <raison spécifique>.

Nous restons à votre disposition pour toute information complémentaire.

<Nom, fonction, signature, cachet>
```

```markdown
<Partner letterhead>
<Place>, <date>

Subject: Letter of support for the project "<title>" led by <applicant>

Dear Sir or Madam,

<Partner name>, <one-line description: nature, year founded, activity>, confirms its support for the
project "<title>" submitted by <applicant> under <call name>.

We have worked with <applicant> since <year / context>. <One sentence on a past collaboration or on
what the partner has seen of the project>.

Within this project, we commit to: <commitment 1 — e.g. provide venue X for Y days>; <commitment 2
— e.g. promote the screenings to our members>; <commitment 3, valued at Z FCFA / EUR if in kind>.

This project matches our priorities on <gender, youth, inclusion, heritage> because <specific reason>.

We remain available for any further information.

<Name, position, signature, stamp>
```

### Gabarit E — Lettre de motivation / courrier d'accompagnement (FR puis EN)

```markdown
<En-tête du porteur>
<Lieu>, le <date>
À l'attention de <service / comité de sélection>, <bailleur>

Objet : Candidature de <porteur> à <nom de l'appel> — projet « <titre> »

Madame, Monsieur,

Je vous adresse, au nom de <structure> (ou : en mon nom propre, avec le portage administratif de
<structure>), le dossier de candidature du projet « <titre> » à <nom de l'appel>.

<Paragraphe 1 — ce que le projet est, en deux phrases concrètes, et pourquoi il répond à l'appel.>

<Paragraphe 2 — ce qui légitime le porteur : une réalisation vérifiable, un lien avec le terrain, une
équipe ; une phrase sur la place des femmes, des jeunes ou des personnes éloignées de l'offre
culturelle.>

<Paragraphe 3 — le montant demandé en FCFA et dans la devise du bailleur, la part de cofinancement,
la durée, et la liste des pièces jointes.>

Je me tiens à votre disposition pour tout complément et vous prie d'agréer, Madame, Monsieur,
l'expression de ma considération distinguée.

<Nom, fonction, signature>
Pièces jointes : <liste numérotée>
```

```markdown
<Applicant letterhead>
<Place>, <date>
To: <selection committee / department>, <funder>

Subject: Application by <applicant> to <call name> — project "<title>"

Dear Sir or Madam,

On behalf of <organisation> (or: in my own name, with administrative hosting by <organisation>), I
am submitting the application of the project "<title>" to <call name>.

<Paragraph 1 — what the project is, in two concrete sentences, and why it fits the call.>

<Paragraph 2 — why the applicant is credible: one verifiable achievement, a link to the field, the
team; one sentence on women, young people or audiences far from cultural provision.>

<Paragraph 3 — amount requested in FCFA and in the funder's currency, co-funding share, duration,
and the list of attachments.>

I remain available for any further information.

Yours faithfully,
<Name, position, signature>
Attachments: <numbered list>
```

### Gabarit F — CV type artiste / porteur (1 page)

```markdown
# <Prénom NOM>
<Rôle principal : réalisatrice, musicien, créatrice de mode> — <ville, pays>
<Téléphone> · <courriel> · <lien portfolio / réseaux professionnels>

## Profil (3 lignes)
<Qui vous êtes, votre pratique, ce qui vous caractérise, un fait vérifiable.>

## Réalisations principales (les plus récentes d'abord, 4 à 6 lignes)
| Année | Œuvre / projet | Rôle | Diffusion / résultat vérifiable |
|---|---|---|---|
| | | | |

## Expérience professionnelle (3 à 5 lignes)
| Période | Structure | Fonction | Responsabilités en une ligne |
|---|---|---|---|
| | | | |

## Formation
| Année | Diplôme ou formation | Établissement, ville |
|---|---|---|

## Compétences
Techniques : <…> · Gestion : <budget, coordination, reporting> · Langues : <avec niveau>

## Distinctions, sélections, résidences, bourses
<Année — intitulé — organisme>
```

### Gabarit G — Structure d'un portfolio / dossier artistique (8 à 15 pages)

| Page | Contenu | Conseils |
|---|---|---|
| 1 | Couverture : nom, discipline, titre du projet, contact, une image forte | une seule image, lisible en petit |
| 2 | Démarche artistique (200 mots) | à la première personne, concret, pas de superlatifs |
| 3-8 | Œuvres ou réalisations : 1 page par œuvre (image/lien, titre, année, format/durée, contexte de diffusion, 3 lignes) | privilégier la qualité des visuels ; liens vers vidéos privées avec mot de passe |
| 9 | Presse et retours (extraits datés, sources) | citer la source exacte, pas « la presse a salué » |
| 10 | Collaborations et partenaires | logos ou noms, rôles |
| 11 | Le projet présenté : images de repérage, maquette, échantillons | lien avec la note conceptuelle |
| 12 | CV résumé (gabarit F) | |
| Fin | Annexes : liens, fiches techniques | |
Formats : PDF unique ≤ 10 Mo si envoi par courriel (vérifier la limite du bailleur), nommé
`Portfolio_<Nom>_<Projet>_<année>.pdf`.

### Gabarit H — Grille de relecture notée (`relecture.md`)

Noter chaque critère de 1 à 5 ; total sur 40 ; viser ≥ 32 et aucun critère < 3.
| Critère | Question de contrôle | Note /5 | Correction à faire |
|---|---|---|---|
| Clarté | Un lecteur pressé comprend-il en 1 minute qui fait quoi, pour qui, où, combien ? | | |
| Cohérence objectifs-activités-budget | Chaque activité sert un objectif ; chaque poste budgétaire correspond à une activité ; les cibles sont atteignables avec ce budget ? | | |
| Conformité au format | Intitulés, ordre, longueur, langue, devise, pièces exigées respectés ? | | |
| Genre et inclusion | Données ventilées, obstacles nommés, mesures concrètes, équipe mixte ? | | |
| Impact social et durabilité | Changement durable décrit, ce qui continue après le financement, recettes propres ? | | |
| Faisabilité | Calendrier réaliste (saisons, délais administratifs), équipe disponible, hypothèses explicites ? | | |
| Originalité et point de vue | Ce que seul ce porteur peut faire ; absence de généralités ? | | |
| Preuves et crédibilité | Chaque chiffre sourcé (fiche, budget, document), réalisations vérifiables, lettres jointes ? | | |
| **TOTAL /40** | | | |

### Gabarit I — Exemple rempli : extrait de note conceptuelle, scénario 1 (documentaire, Tchad)

Extrait des rubriques 1, 3 et 6 d'une note générique de 3 pages (noms fictifs ; chiffres repris de
`projet/fiche-projet.md`, estimations marquées « (est.) »).

```markdown
# NOTE CONCEPTUELLE — « Les filets du lac » (documentaire, 26 min)
Porteur : Achta M., réalisatrice (portage administratif : <société de production tchadienne, à
confirmer>) — N'Djamena, Tchad
Appel : <nom exact de l'appel — à reporter des lignes directrices> — Montant demandé : à fixer
selon le plafond de l'appel [À VÉRIFIER], sur un budget total de 16 398 925 FCFA (25 000 EUR) —
Durée : 24 mois

## 1. Contexte et justification
Sur la rive tchadienne du lac Tchad, les femmes fument et vendent une grande part du poisson pêché ;
ce travail fait vivre des villages entiers. Pourtant, les images du lac qui circulent parlent de
sécurité ou de climat, presque jamais d'elles. En 2025, pendant trois semaines de repérage auprès
d'un groupement de fumeuses de poisson, la réalisatrice a filmé un teaser de 3 minutes : les femmes
y racontent leur journée en arabe tchadien et en kanembou, et demandent à se voir à l'écran. Les
données chiffrées sur la place des femmes dans la filière seront documentées à partir des sources
officielles (ministère en charge de la pêche, FAO) [À VÉRIFIER]. « Les filets du lac » répond à la
priorité de l'appel sur <priorité citée avec les mots de l'appel> en donnant à ces femmes la
maîtrise du récit : ce sont leurs voix qui structurent le film.

## 3. Résultats attendus et indicateurs
| Résultat | Indicateur | Départ | Cible | Vérification |
|---|---|---|---|---|
| R1 Un documentaire de 26 min sous-titré FR/EN est terminé | master livré | 0 | 1 (déc. 2027, est.) | fichier master, visa si requis |
| R2 Les communautés filmées voient le film | projections ; spectateurs ventilés F/H, jeunes | 0 | 10 projections ; 2 000 spectateurs dont 50 % de femmes (est.) | feuilles de présence, photos |
| R3 Le film circule au-delà du lac | sélections festivals ; diffusion TV | 0 | 3 sélections, 1 diffusion (est.) | courriels de sélection, contrat |
Les indicateurs seront ventilés par sexe, tranche d'âge et zone, comptés par feuilles de présence
tenues par deux personnes du groupement partenaire.

## 6. Bénéficiaires, genre et inclusion
| Catégorie | Nombre | dont femmes | dont jeunes | dont pers. handicapées | dont rural |
|---|---|---|---|---|---|
| Directs (femmes filmées et familles) | 40 (est.) | 30 | 15 (est.) | à documenter | 40 |
| Indirects (spectateurs) | 2 000 (est.) | 1 000 visé | 800 (est.) | accès prévu | 1 500 (est.) |
Les projections sont gratuites, en plein air, en langues nationales, programmées après l'heure de
vente du poisson pour que les femmes puissent y assister ; un espace est réservé aux personnes à
mobilité réduite. L'équipe technique de six personnes (est.) comptera au moins trois femmes, dont
deux stagiaires formées pendant le tournage.
```

## Critères de qualité du livrable

- Le plan, les intitulés, l'ordre, la longueur, la langue et la devise sont ceux du bailleur (gabarit A
  rempli et vérifié) ; en l'absence de lignes directrices, le fichier porte la mention « format
  générique — à mettre en conformité ».
- Chaque chiffre de la note existe dans `projet/fiche-projet.md`, `projet/budget/budget.md` ou une
  pièce ; les estimations sont marquées ; aucun montant, date ou critère de bailleur n'est inventé
  (« [À VÉRIFIER — source : …] »).
- Objectifs, résultats, activités, budget et calendrier se répondent ligne à ligne.
- Genre, inclusion (handicap, jeunes, rural, langues nationales) et impact social sont traités avec
  des données ventilées et des mesures concrètes, pas une phrase de principe.
- Les termes techniques sont expliqués à leur première apparition (note conceptuelle, cadre
  logique, cofinancement, indicateur, moyen de vérification).
- Les pièces exigées sont listées avec leur statut (prête / à signer / à produire par un tiers) et
  les professionnels humains nécessaires sont nommés (expert-comptable pour états financiers
  certifiés, juriste pour statuts, avocat pour contrat de portage ou de coproduction).
- La grille de relecture (gabarit H) atteint ≥ 32/40 sans critère < 3.
- Le texte est au vouvoiement dans les parties adressées au promoteur, sans emoji, sans anglicisme
  non traduit ; les lettres sont prêtes à signer.
- `projet/ETAT.md` est à jour.

## Erreurs fréquentes à éviter

- Imposer le gabarit générique alors que le bailleur a son propre formulaire : refus administratif
  immédiat.
- Dépasser la limite de pages ou de mots « de peu » : beaucoup de bailleurs écartent sans lire.
- Reposer au promoteur des questions auxquelles la fiche-projet répond déjà.
- Rédiger sans budget : la note contient alors des chiffres inventés ou incohérents.
- Copier les priorités de l'appel mot pour mot sans les relier au projet.
- Traiter le genre en une phrase (« le projet est ouvert aux femmes ») sans données ni mesures.
- Confondre activités, résultats et objectifs dans le cadre logique.
- Omettre les hypothèses (sécurité, saison, délais administratifs) : le comité les voit, lui.
- Lettres de soutien génériques et non datées, ou signées par le porteur lui-même.
- Oublier la devise du bailleur ou utiliser un taux de change approximatif.
- Déposer à la dernière heure sans tenir compte du fuseau horaire indiqué.
- Laisser passer un texte générique : après conformité, passer par `/icc:reecriture-humanisee`.

## Références et sources à vérifier

- `references/rubriques-bailleurs.md` (dans ce dossier de skill) : rubriques et exigences de forme
  habituellement rencontrées par famille de bailleurs — chaque ligne est d'« usage général — vérifier
  dans les lignes directrices de l'appel en cours ».
- Lignes directrices de l'appel : toujours le texte officiel du bailleur (site officiel, plateforme
  de dépôt). Si WebSearch est disponible : « <nom bailleur> appel à projets <année> lignes
  directrices ».
- Taux de change : parité fixe 1 EUR = 655,957 XAF/XOF (BEAC / BCEAO — site officiel). Pour
  l'USD ou la GBP : taux du jour de la banque centrale ou du bailleur, daté.
- Méthode du cadre logique : guides de gestion du cycle de projet de la Commission européenne et des
  agences de coopération (usage général).
- Pièces juridiques et comptables : `/icc:statut-juridique`, `/icc:budget-cofinancement`.

## Passage de relais (quel agent/skill ensuite, et mise à jour de projet/ETAT.md)

- Note conforme → `/icc:reecriture-humanisee` (agent `icc-redaction`) pour naturaliser le style
  sans changer faits ni format ; produit `note-conceptuelle.v2.md`.
- Budget manquant ou incohérent → `/icc:budget-cofinancement` puis `/icc:plan-tresorerie` (agent
  `icc-budget`), puis revenir ici pour mettre à jour la rubrique budget.
- Statut ou portage à sécuriser avant signature → `/icc:statut-juridique` (agent `icc-juridique`).
- Pitch oral ou dossier de presse demandé par le bailleur → `/icc:pitch-dossier-presse` (agent
  `icc-communication`).
- Dossier déposé → `/icc:plan-mise-en-oeuvre` (agent `icc-mise-en-oeuvre`) pour préparer le
  démarrage ; `icc-orchestrateur` programme le suivi de la réponse du bailleur.

Mise à jour obligatoire de `projet/ETAT.md` (dernière étape) :

```markdown
# ÉTAT DU PROJET — <nom du projet>
Dernière mise à jour : AAAA-MM-JJ HH:MM
Agent actif : icc-redaction | Skill en cours : /icc:note-conceptuelle (terminé pour <slug-bailleur>)
## Résumé du projet (5 lignes max)
<inchangé — copier depuis fiche-projet.md §3b>
## Étapes terminées (avec fichiers produits)
- Note conceptuelle <bailleur> : projet/dossiers/<slug>/note-conceptuelle.md (relecture <n>/40)
- Pièces : projet/dossiers/<slug>/<lettres, cv, cadre-logique, plan-impose>
## Étape en cours (où on en est précisément)
- <ex. : attente de signature de la lettre de soutien du groupement ; dépôt prévu le …>
## Prochaines étapes (ordre recommandé)
1. /icc:reecriture-humanisee sur note-conceptuelle.md — 2. dépôt — 3. <suite>
## Décisions prises / hypothèses à confirmer
- <ex. : montant demandé fixé à X en attendant confirmation du plafond de l'appel>
## Questions en attente de réponse du promoteur
- <ex. : signataire du dossier ; version anglaise nécessaire ?>
## Alertes (délais, pièces manquantes, professionnel humain requis)
- Date limite : <date, heure, fuseau> ; pièces manquantes : <liste> ; <expert-comptable / avocat requis pour …>
```
