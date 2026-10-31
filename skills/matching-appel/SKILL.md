---
name: matching-appel
description: Utiliser quand un promoteur ICC a un appel à projets, appel à candidatures, concours, bourse ou programme précis en main et demande s'il est éligible, s'il a ses chances, quelles pièces fournir, ou dit « est-ce que je peux candidater », « analyse cet appel », « on y va ou pas ».
---

# /icc:matching-appel — Analyse d'un appel à projets et décision GO / NO-GO

## Objectif

Analyser UN appel à projets précis (texte fourni par le promoteur, ou récupéré via WebFetch /
WebSearch quand la connexion le permet) et produire une fiche de matching (= mise en
correspondance entre les exigences de l'appel et la situation du promoteur) qui contient :

1. le décorticage des critères d'éligibilité : structure, pays, secteur, âge ou ancienneté,
   montant, durée, cofinancement, langue, pièces exigées ;
2. une grille de conformité point par point avec, pour chaque critère, un verdict : éligible /
   non éligible / à vérifier / contournable (et comment) ;
3. un score de probabilité raisonné sur 100, avec pondérations explicites : éligibilité formelle
   40, adéquation thématique 20, capacité à produire les pièces 15, concurrence et sélectivité 10,
   calendrier réaliste 15 ;
4. la liste des pièces à produire, qui les produit, et quel skill `/icc:` les produit ;
5. un rétro-planning (= calendrier à rebours depuis la date limite) ;
6. une décision argumentée : GO / NO-GO / GO SOUS CONDITIONS ;
7. les questions à poser au bailleur, avec un mail-type de demande de clarification en français et
   en anglais.

Livrable canonique : `projet/financements/matching-<slug-appel>.md`, où `<slug-appel>` est un nom
court en minuscules sans accents ni espaces (par exemple `matching-fonds-image-francophonie-2027.md`).
Agent principal : `icc-financements`. Le skill ne promet jamais l'obtention du financement ; il
évalue une probabilité et la qualité du dossier.

## Quand l'utiliser / ne pas l'utiliser

Utiliser ce skill quand :
- le promoteur a identifié un appel précis (via `/icc:cartographie-bailleurs`, une newsletter, un
  groupe WhatsApp, un partenaire) et hésite à candidater ;
- l'appel est complexe (plusieurs critères, cofinancement, pièces nombreuses) et il faut vérifier
  la conformité avant d'investir des semaines de rédaction ;
- il faut organiser le travail de l'équipe jusqu'à la date limite ;
- un bailleur a répondu par une demande de compléments et il faut vérifier ce qui manque.

Ne pas l'utiliser quand :
- aucun appel précis n'est identifié : utiliser `/icc:cartographie-bailleurs` ;
- la décision GO est déjà prise et il faut rédiger : `/icc:note-conceptuelle` (agent
  `icc-redaction`) ;
- la question porte uniquement sur le budget ou le cofinancement : `/icc:budget-cofinancement` ;
- il s'agit d'un prêt bancaire ou d'un investisseur (pas d'appel formel) : voir
  `icc-budget` et `icc-juridique`.

## Prérequis

Fichiers du dossier `projet/` à lire s'ils existent :
- `projet/ETAT.md` — à lire en premier ; reprendre à l'étape indiquée ;
- `projet/fiche-projet.md` — secteur, pays, stade, équipe, publics, montant, statut ;
- `projet/financements/cartographie.md` — ligne du bailleur concerné (verdict préliminaire,
  source officielle) ;
- `projet/juridique/statut.md` — statut juridique actuel, date de création, structure porteuse ;
- `projet/budget/budget.md` — budget total et part acquise ;
- `projet/dossiers/<slug-bailleur>/` — pièces déjà produites pour ce bailleur.

Informations nécessaires sur l'appel (à obtenir dans cet ordre de préférence) :
1. le texte intégral de l'appel et ses lignes directrices (document fourni par le promoteur, copié
   dans `projet/financements/appels/<slug-appel>-texte.md` pour pouvoir travailler hors ligne) ;
2. à défaut, la page officielle récupérée par WebFetch (noter l'URL ouverte et la date) ;
3. à défaut, le résumé que fait le promoteur, en marquant alors TOUS les critères « à vérifier ».

Sans texte de l'appel, le skill ne peut produire qu'une pré-analyse : le dire explicitement dans le
livrable.

## Procédure étape par étape

Après chaque étape, noter l'étape atteinte dans `projet/ETAT.md`. Les étapes 2 à 8 sont
réalisables hors ligne dès que le texte de l'appel est enregistré localement.

### Étape 1 — Obtenir et archiver le texte de l'appel
Demander au promoteur le texte de l'appel (copier-coller, PDF, photo). Si seule une URL est
disponible et que WebFetch fonctionne, récupérer la page et les lignes directrices ; sinon, si
WebSearch est disponible, lancer « "<nom du bailleur>" "<nom de l'appel>" <année> lignes
directrices ». Enregistrer le texte dans `projet/financements/appels/<slug-appel>-texte.md` avec
l'URL réellement ouverte et la date de consultation. Ne jamais compléter de mémoire un critère
absent du texte : le marquer « non précisé dans l'appel — à demander au bailleur ».

### Étape 2 — Décortiquer les critères
Remplir le gabarit A (fiche d'identité de l'appel) puis extraire, un par un, les critères en citant
le passage exact de l'appel (colonne « ce que dit l'appel »). Catégories à examiner
systématiquement : type de structure et personnalité juridique ; pays ou zone ; secteur et
thématique ; âge du promoteur ou ancienneté de la structure ; montant minimal et maximal ; durée
du projet ; cofinancement (= part que vous devez apporter vous-même ou via d'autres sources) et
apports en nature acceptés ou non ; langue du dossier ; pièces administratives et artistiques ;
modalités de dépôt (plateforme, courriel, papier) ; priorités transversales (genre, jeunesse,
inclusion, environnement) ; dépenses éligibles et inéligibles ; calendrier (publication, date
limite, résultats, démarrage).

### Étape 3 — Grille de conformité
Pour chaque critère, confronter la situation du promoteur (lue dans la fiche-projet et le statut)
et attribuer un verdict dans le gabarit B :
- **Éligible** : la situation correspond, preuve disponible (par exemple : récépissé
  d'association).
- **Non éligible** : critère bloquant et non contournable dans le délai (par exemple : réservé aux
  structures de plus de trois ans alors que l'association a deux ans).
- **À vérifier** : l'appel est ambigu ou l'information sur le promoteur manque ; indiquer la
  question à poser au bailleur ou au promoteur.
- **Contournable** : non conforme en l'état mais une action réaliste le rend conforme avant la
  date limite ; décrire l'action (portage par une structure éligible, partenariat avec un chef de
  file, traduction du dossier, ajustement du montant demandé) et le skill `/icc:` concerné.
Un seul critère « non éligible » formel entraîne un NO-GO, sauf contournement crédible.

### Étape 4 — Score de probabilité
Remplir la grille du gabarit C. Attribuer chaque note en justifiant en une phrase, puis
additionner. Interprétation indicative : 70 et plus = GO ; 50 à 69 = GO SOUS CONDITIONS (lister
les conditions) ; moins de 50 = NO-GO ou report à une prochaine session. Le score ne remplace pas
le jugement : si un critère formel bloquant existe, la décision est NO-GO quel que soit le total.

### Étape 5 — Pièces à produire et responsables
Remplir le gabarit D : pour chaque pièce exigée, indiquer si elle existe déjà (et où), qui la
produit (promoteur, partenaire, professionnel humain), quel skill `/icc:` aide à la produire, la
date butoir interne. Signaler explicitement les pièces qui exigent un professionnel : statuts et
récépissé (greffe, notaire, avocat selon le pays), états financiers ou attestation comptable
(expert-comptable), comptes audités (commissaire aux comptes), contrats de cession de droits ou
convention de portage (avocat ou juriste), légalisation de documents (notaire, huissier).

### Étape 6 — Rétro-planning
À partir de la date limite (et de l'heure, avec le fuseau horaire indiqué dans l'appel), remplir
le gabarit E à rebours : dépôt avec marge de 48 heures (connectivité irrégulière), relecture
finale et réécriture humanisée (`/icc:reecriture-humanisee`), traduction si nécessaire, budget
validé, pièces administratives obtenues (délais des administrations et professionnels), lettres de
soutien demandées, note conceptuelle rédigée, questions envoyées au bailleur (le plus tôt possible,
car les réponses peuvent prendre deux semaines). Vérifier que la somme des délais tient dans le
temps disponible ; sinon, la note « calendrier réaliste » du score doit être basse.

### Étape 7 — Intégrer genre, inclusion et impact social
Repérer dans l'appel les priorités transversales et vérifier dans la fiche-projet ce que le projet
apporte réellement. Remplir la rubrique dédiée du gabarit B (ligne « Priorités transversales ») et
noter dans le gabarit D les preuves à rassembler (données sur l'équipe, les publics, les
territoires, les langues). Ne pas inventer d'impact : un bailleur vérifie.

### Étape 8 — Questions au bailleur
Remplir le gabarit F avec toutes les ambiguïtés relevées. Préparer le mail-type (FR ou EN selon la
langue de l'appel) prêt à envoyer par le promoteur, sans inventer d'adresse : utiliser le contact
indiqué dans l'appel ou demander au promoteur de le repérer.

### Étape 9 — Décision et livrable
Rédiger la décision GO / NO-GO / GO SOUS CONDITIONS (gabarit G) en trois à cinq phrases
argumentées, avec les conditions précises et les dates. Assembler les gabarits A à G dans
`projet/financements/matching-<slug-appel>.md`. Relire avec la grille de qualité. Mettre à jour
`projet/ETAT.md` (voir « Passage de relais »).

## Questions à poser au promoteur

Poser uniquement celles dont la réponse ne figure ni dans la fiche-projet ni dans le statut.
Regrouper en un seul message.

1. Pouvez-vous me transmettre le texte complet de l'appel et, s'il existe, le document de lignes
   directrices ou le formulaire ? Sinon, l'adresse de la page ?
2. Quelle est la date et l'heure limite de dépôt indiquées, et dans quel fuseau horaire ?
3. Au nom de qui le dossier serait-il déposé : vous-même, votre structure, une structure porteuse ?
   Date de création et numéro d'enregistrement de cette structure ?
4. Quel montant comptez-vous demander à ce bailleur, et quel est le budget total du projet (FCFA) ?
5. Quelle part de cofinancement pouvez-vous justifier, en argent (lettres d'engagement,
   conventions) et en nature ?
6. Quelles pièces avez-vous déjà : statuts, récépissé, relevé d'identité bancaire, états
   financiers, rapports d'activité, CV, portfolio, teaser, lettres de soutien, devis ?
7. Pouvez-vous rédiger ou faire relire le dossier dans la langue exigée ?
8. Avez-vous déjà candidaté à cet appel ou chez ce bailleur ? Quel retour avez-vous reçu ?
9. Combien d'heures par semaine, et quelles personnes, pouvez-vous consacrer au dossier d'ici la
   date limite ?
10. Le projet concerne-t-il particulièrement des femmes, des jeunes, des personnes en situation de
    handicap, des zones rurales, des langues nationales ? Quelles preuves (chiffres, listes,
    photos, témoignages) pouvez-vous fournir ?
11. Connaissez-vous d'autres candidats ou lauréats passés de cet appel (pour estimer la
    sélectivité) ?

## Gabarits complets

Copier les gabarits A à G dans `projet/financements/matching-<slug-appel>.md`, dans l'ordre.

### Gabarit A — Fiche d'identité de l'appel

```markdown
# Fiche de matching — <nom de l'appel> (<bailleur>)
Date de l'analyse : AAAA-MM-JJ | Rédigé avec /icc:matching-appel | Agent : icc-financements
Projet : <nom du projet> | Fiche-projet : projet/fiche-projet.md

| Élément | Valeur | Source |
|---|---|---|
| Bailleur | <nom> | <texte de l'appel> |
| Intitulé exact de l'appel / programme | <intitulé> | <texte de l'appel> |
| Texte de l'appel archivé dans | projet/financements/appels/<slug-appel>-texte.md | URL ouverte le AAAA-MM-JJ : <URL réelle> ou « document fourni par le promoteur » |
| Date de publication | <date ou « non précisée »> | |
| Date et heure limite de dépôt (fuseau) | <date, heure, fuseau> [À VÉRIFIER sur la page officielle la veille du dépôt] | |
| Résultats annoncés | <date ou « non précisée »> | |
| Démarrage prévu des projets | <date ou période> | |
| Mode de dépôt | <plateforme en ligne / courriel / papier> | |
| Contact indiqué pour les questions | <adresse ou formulaire indiqué dans l'appel, sinon « non précisé »> | |
| Langue(s) du dossier | <FR / EN / autre> | |
| Montant demandé par le projet | <montant> FCFA (≈ <montant> <devise du bailleur>, parité 1 EUR = 655,957 FCFA) | projet/budget/budget.md |
```

### Gabarit B — Grille de conformité

```markdown
## B. Grille de conformité point par point

| Critère | Ce que dit l'appel (citation) | Situation du promoteur | Verdict | Pourquoi / comment contourner | Preuve ou action | Skill /icc: |
|---|---|---|---|---|---|---|
| Type de structure / personnalité juridique | « … » | <sans statut / association depuis … / SARL …> | <Éligible / Non éligible / À vérifier / Contournable> | <raison ; si contournable : portage, partenariat, création> | <récépissé, statuts, convention de portage> | /icc:statut-juridique |
| Pays / zone d'intervention | « … » | <pays> | | | | |
| Secteur et thématique | « … » | <secteur> | | | | /icc:fiche-projet |
| Âge du promoteur / ancienneté de la structure | « … » | <âge / date de création> | | | | |
| Montant minimal / maximal | « … » | <montant demandé> | | | | /icc:budget-cofinancement |
| Durée du projet | « … » | <durée prévue> | | | | /icc:plan-mise-en-oeuvre |
| Cofinancement exigé (taux, nature acceptée) | « … » | <part justifiable> | | | | /icc:budget-cofinancement |
| Dépenses éligibles / inéligibles | « … » | <postes du budget concernés> | | | | /icc:budget-cofinancement |
| Langue du dossier | « … » | <capacité> | | | | /icc:note-conceptuelle |
| Pièces administratives exigées | « … » | <disponibles / manquantes> | | | | voir gabarit D |
| Pièces artistiques exigées (synopsis, teaser, portfolio, programme) | « … » | | | | | /icc:pitch-dossier-presse |
| Priorités transversales : genre, jeunes, handicap, zones rurales, langues nationales, environnement | « … » | <ce que le projet fait réellement> | | <les points forts à mettre en avant, les faiblesses à reconnaître> | <données, listes, témoignages> | /icc:fiche-projet |
| Modalités de dépôt (plateforme, compte à créer, format des fichiers) | « … » | | | | | |
| Exclusions explicites (déjà financé, cumul, candidature précédente) | « … » | | | | | |

Nombre de critères : <n> | Éligible : <n> | Non éligible : <n> | À vérifier : <n> | Contournable : <n>
Critère(s) bloquant(s) : <liste ou « aucun »>
```

### Gabarit C — Grille de scoring (sur 100)

```markdown
## C. Score de probabilité raisonné

| Dimension | Pondération | Note attribuée | Justification (une phrase, factuelle) |
|---|---|---|---|
| Éligibilité formelle (structure, pays, secteur, montant, durée, cofinancement) | 40 | <0-40> | <40 si tout est éligible ; 0 si un critère bloquant non contournable ; entre les deux selon le nombre de « à vérifier » et de « contournable »> |
| Adéquation thématique (le projet répond-il à ce que le bailleur veut financer, y compris ses priorités transversales ?) | 20 | <0-20> | <citer les priorités de l'appel couvertes et non couvertes> |
| Capacité à produire les pièces dans le délai (administratives, artistiques, financières) | 15 | <0-15> | <pièces existantes vs manquantes, professionnels à mobiliser> |
| Concurrence et sélectivité (nombre de lauréats, taux de sélection connu ou estimé, antécédents) | 10 | <0-10> | <information de l'appel ou estimation marquée [estimation]> |
| Calendrier réaliste (temps disponible vs charge de travail et délais administratifs) | 15 | <0-15> | <résultat du rétro-planning> |
| **Total** | **100** | **<total>** | |

Lecture indicative : 70 et plus = GO ; 50 à 69 = GO SOUS CONDITIONS ; moins de 50 = NO-GO ou
report. Un critère formel bloquant impose NO-GO quel que soit le total.
```

### Gabarit D — Tableau des pièces à produire

```markdown
## D. Pièces à produire

| Pièce exigée | Existe déjà ? (où) | Qui la produit | Professionnel humain requis ? (pourquoi) | Skill /icc: d'appui | Date butoir interne | Statut |
|---|---|---|---|---|---|---|
| Formulaire de candidature du bailleur | non | promoteur | non | /icc:note-conceptuelle | AAAA-MM-JJ | à faire |
| Note conceptuelle / description du projet (format imposé : <pages, rubriques>) | non | promoteur | non | /icc:note-conceptuelle puis /icc:reecriture-humanisee | | |
| Budget détaillé au format du bailleur (FCFA + devise du bailleur) | partiel : projet/budget/budget.md | promoteur | relecture par expert-comptable recommandée si états financiers joints | /icc:budget-cofinancement | | |
| Preuves de cofinancement (lettres d'engagement, conventions) | | partenaires | non | /icc:budget-cofinancement | | |
| Statuts et récépissé / registre du commerce | | structure | oui : greffe, notaire ou avocat selon le pays | /icc:statut-juridique | | |
| Relevé d'identité bancaire au nom de la structure | | banque | non (mais délai bancaire) | | | |
| États financiers ou rapport financier de l'année précédente | | structure | oui : expert-comptable (commissaire aux comptes si comptes audités exigés) | /icc:budget-cofinancement | | |
| Rapport d'activité | | structure | non | /icc:suivi-evaluation | | |
| CV de l'équipe | | équipe | non | /icc:note-conceptuelle | | |
| Portfolio / teaser / synopsis / programme artistique | | équipe artistique | non | /icc:pitch-dossier-presse | | |
| Lettres de soutien ou d'intention (partenaires, diffuseurs, collectivités) | | partenaires | non | /icc:note-conceptuelle | | |
| Contrats de cession de droits, autorisations (musique, images, personnes filmées) | | | oui : avocat ou juriste pour les contrats | /icc:propriete-intellectuelle | | |
| Convention de portage (si structure porteuse) | | structure porteuse | oui : avocat ou juriste | /icc:statut-juridique | | |
| Chronogramme et cadre logique (« logframe » = tableau objectifs/résultats/indicateurs) | | promoteur | non | /icc:plan-mise-en-oeuvre | | |
| Données genre / inclusion / impact (équipe, publics, territoires) | | promoteur | non | /icc:suivi-evaluation | | |
| Traduction du dossier | | traducteur | recommandé si dossier en anglais et niveau insuffisant | /icc:reecriture-humanisee (relecture) | | |
```

### Gabarit E — Rétro-planning

```markdown
## E. Rétro-planning jusqu'à la date limite

Date limite : AAAA-MM-JJ HH:MM (<fuseau>) | Aujourd'hui : AAAA-MM-JJ | Jours disponibles : <n>

| Échéance interne | Date | Tâche | Responsable | Dépend de | Faisable hors ligne ? |
|---|---|---|---|---|---|
| J-<n> (aujourd'hui) | | Décision GO ; envoi des questions au bailleur (gabarit F) | promoteur | | oui (rédaction) / non (envoi) |
| J-<n> | | Demande des pièces administratives (récépissé, RIB, états financiers) auprès des professionnels | promoteur, expert-comptable, greffe | | non |
| J-<n> | | Demande des lettres de soutien et engagements de cofinancement | promoteur, partenaires | | partiel |
| J-<n> | | Première version de la note conceptuelle | promoteur avec /icc:note-conceptuelle | fiche-projet | oui |
| J-<n> | | Budget au format du bailleur, cofinancement bouclé | promoteur avec /icc:budget-cofinancement | devis, engagements | oui |
| J-<n> | | Réponses du bailleur intégrées ; ajustements | promoteur | questions envoyées | oui |
| J-<n> | | Relecture, réécriture humanisée, traduction si besoin | promoteur avec /icc:reecriture-humanisee | note v1 | oui |
| J-7 | | Toutes les pièces rassemblées dans projet/dossiers/<slug-bailleur>/ ; vérification des formats de fichiers | promoteur | | oui |
| J-3 | | Création du compte sur la plateforme de dépôt, test de téléversement | promoteur | connexion | non |
| J-2 | | Dépôt effectif (marge de 48 h pour les coupures de connexion) | promoteur | | non |
| J-0 | | Vérification de l'accusé de réception ; capture d'écran archivée | promoteur | | non |

Contrôle de faisabilité : somme des délais incompressibles (administration, banque, professionnels)
= <n> jours ; jours disponibles = <n> ; marge = <n>. Si la marge est négative : NO-GO ou report.
```

### Gabarit F — Questions à poser au bailleur et mail-type

```markdown
## F. Questions à poser au bailleur

| N° | Point ambigu dans l'appel (citation) | Question précise | Pourquoi c'est important pour nous | Réponse reçue (date) |
|---|---|---|---|---|
| 1 | « … » | <question> | <ce qui change selon la réponse> | |
| 2 | | | | |

### Mail-type — français

Objet : Demande de précisions — <intitulé de l'appel> — <nom du projet>

Madame, Monsieur,

Nous préparons une candidature à l'appel « <intitulé exact> » publié par <bailleur> pour le
projet « <nom du projet> », <une phrase de description : secteur, pays, objectif>, porté par
<nom de la structure ou « moi-même, en tant que … »>.

Afin de nous assurer de la conformité de notre dossier, nous vous serions reconnaissants de bien
vouloir nous préciser les points suivants :
1. <question 1, formulée à partir de la citation de l'appel> ;
2. <question 2> ;
3. <question 3>.

Nous restons à votre disposition pour tout complément et vous remercions par avance de votre
réponse avant le <date>, la date limite de dépôt étant fixée au <date limite>.

Veuillez agréer, Madame, Monsieur, l'expression de nos salutations distinguées.

<Prénom NOM>
<Fonction> — <Structure>
<Ville, Pays> — <téléphone> — <courriel>

### Mail-type — anglais

Subject: Request for clarification — <call title> — <project name>

Dear Sir or Madam,

We are preparing an application to the call "<exact title>" published by <funder> for the project
"<project name>", <one-sentence description: sector, country, objective>, led by <organisation
name or "myself, as …">.

To make sure our application complies with the guidelines, we would be grateful if you could
clarify the following points:
1. <question 1, quoting the relevant passage of the call>;
2. <question 2>;
3. <question 3>.

We remain at your disposal for any further information and thank you in advance for your reply
before <date>, as the submission deadline is <deadline>.

Yours faithfully,

<First name LAST NAME>
<Position> — <Organisation>
<City, Country> — <phone> — <email>
```

### Gabarit G — Décision

```markdown
## G. Décision

**Décision : <GO / NO-GO / GO SOUS CONDITIONS>** — score <total>/100 — critère bloquant : <aucun / lequel>

Argumentaire (3 à 5 phrases) : <éligibilité formelle ; adéquation ; pièces ; calendrier ; sélectivité>.

Conditions (si GO SOUS CONDITIONS) :
| Condition | Date limite pour la lever | Responsable | Si non levée |
|---|---|---|---|
| <ex. : convention de portage signée> | AAAA-MM-JJ | promoteur + avocat | NO-GO |

Si NO-GO : <ce qu'il faudrait changer pour la prochaine session ; autre bailleur plus adapté dans
projet/financements/cartographie.md>.

Professionnels humains indispensables pour cette candidature : <liste et pourquoi>.
```

### Exemple rempli (extrait) — scénario 2, festival de musique (association, Afrique centrale)

Hypothèse : l'association a repéré un appel à propositions d'un programme régional ACP-UE Culture
relayé par un opérateur intermédiaire (texte fourni par le promoteur ; critères ci-dessous cités
du document fourni, à titre d'illustration de la méthode).

```markdown
# Fiche de matching — Appel à propositions <programme régional ACP-UE Culture, intitulé exact du document> 
Date de l'analyse : 2026-10-30 | Rédigé avec /icc:matching-appel | Agent : icc-financements
Projet : Festival « Voix du fleuve » (3 jours, musiques urbaines et traditionnelles, 5 000 spectateurs visés)

| Élément | Valeur | Source |
|---|---|---|
| Texte de l'appel archivé dans | projet/financements/appels/acp-ue-culture-festivals-texte.md | document PDF fourni par le promoteur le 2026-10-28 |
| Date et heure limite | <date du document> 17:00 (heure de Bruxelles) [À VÉRIFIER la veille sur la page officielle] | document fourni |
| Langue du dossier | FR ou EN | document fourni |
| Montant demandé | 32 800 000 FCFA (≈ 50 000 EUR) sur un budget de 39 360 000 FCFA (≈ 60 000 EUR) | projet/budget/budget.md |

## B. Grille de conformité (extrait)
| Critère | Ce que dit l'appel | Situation | Verdict | Pourquoi / contournement | Preuve | Skill |
|---|---|---|---|---|---|---|
| Structure | « organisations à but non lucratif légalement enregistrées depuis au moins deux ans » | association déclarée depuis 2 ans et 3 mois | Éligible | ancienneté atteinte à la date limite | récépissé daté | — |
| Pays | « pays d'Afrique centrale éligibles listés en annexe 1 » | pays listé | Éligible | | annexe 1 | — |
| Cofinancement | « au moins 20 % du coût total, apports en nature non comptabilisés » | 10 % en numéraire (billetterie prévisionnelle), 15 % en nature | Contournable | il manque 10 % en numéraire : sponsors locaux ou billetterie ferme ; engagement écrit requis | lettres d'engagement | /icc:budget-cofinancement |
| États financiers | « comptes de l'exercice précédent certifiés » | comptes tenus par le trésorier, non certifiés | Contournable | expert-comptable à mandater immédiatement (délai 3 à 4 semaines) | attestation | professionnel humain requis |
| Priorités transversales | « égalité de genre et participation des jeunes évaluées » | 4 artistes femmes sur 12 ; 60 % du public visé de moins de 30 ans ; scène ouverte jeunes talents | Éligible, à renforcer | mettre en avant la programmation paritaire visée, chiffrer les jeunes bénéficiaires | fiche-projet, programmation | /icc:suivi-evaluation |

## C. Score
| Dimension | Pondération | Note | Justification |
|---|---|---|---|
| Éligibilité formelle | 40 | 30 | tout éligible sauf cofinancement numéraire et certification des comptes, contournables |
| Adéquation thématique | 20 | 17 | festival, jeunesse, genre : au cœur de l'appel ; dimension régionale faible |
| Pièces | 15 | 9 | 6 pièces sur 11 existantes ; comptes certifiés et lettres de sponsors à obtenir |
| Concurrence | 10 | 5 | appel régional, nombre de lauréats non précisé [estimation] |
| Calendrier | 15 | 10 | 52 jours disponibles ; délais professionnels 28 jours ; marge 10 jours |
| **Total** | **100** | **71** | |

## G. Décision
**Décision : GO SOUS CONDITIONS** — 71/100 — aucun critère bloquant.
Argumentaire : l'association est formellement éligible et le projet répond aux priorités de
l'appel (jeunesse, genre, musiques locales). Deux conditions doivent être levées sous 3 semaines :
sécuriser 10 % de cofinancement numéraire par lettres d'engagement de sponsors ou de la mairie, et
obtenir des comptes certifiés par un expert-comptable. La dimension régionale (échanges d'artistes
avec un pays voisin) doit être renforcée dans la note conceptuelle.
| Condition | Date limite | Responsable | Si non levée |
|---|---|---|---|
| Lettres d'engagement sponsors pour 3 936 000 FCFA (≈ 6 000 EUR) | J-21 | président + trésorier | réduire le budget ou NO-GO |
| Comptes de l'exercice précédent certifiés | J-14 | expert-comptable | NO-GO (pièce exigée) |
Professionnels indispensables : expert-comptable (certification des comptes) ; juriste pour les
contrats artistes et la déclaration à la société de gestion collective des droits d'auteur.
```

## Critères de qualité du livrable

| Critère | Vérification |
|---|---|
| Texte de l'appel archivé | `projet/financements/appels/<slug-appel>-texte.md` existe, avec URL réelle ou mention « document fourni par le promoteur » et date. |
| Citations | Chaque critère de la grille B cite le passage de l'appel ; aucun critère inventé ; les critères absents sont marqués « non précisé — à demander ». |
| Verdicts complets | Chaque ligne a un verdict parmi quatre ET une raison ; chaque « contournable » décrit l'action et le skill. |
| Score transparent | Les cinq dimensions sont notées et justifiées ; le total est exact ; un critère bloquant impose NO-GO. |
| Pièces | Chaque pièce a un responsable, une date et, si besoin, le professionnel humain requis et pourquoi. |
| Calendrier | Le rétro-planning part de la date limite réelle (fuseau indiqué) avec marge de 48 h ; la faisabilité est contrôlée. |
| Double devise | Montants en FCFA et dans la devise du bailleur, parité 1 EUR = 655,957 FCFA. |
| Inclusion | La ligne « priorités transversales » est remplie avec des faits et des preuves à produire. |
| Décision argumentée | GO / NO-GO / GO SOUS CONDITIONS avec conditions datées et responsables. |
| Honnêteté | Aucun montant, date ou URL inventé ; les estimations sont marquées [estimation] ; pas de promesse. |
| Reprenable | `projet/ETAT.md` à jour avec l'étape atteinte et les conditions en attente. |

## Erreurs fréquentes à éviter

- Analyser l'appel à partir d'un résumé ou de souvenirs d'une édition précédente : les critères
  changent ; exiger le texte de l'édition en cours.
- Confondre la date limite locale et celle du bailleur (fuseau horaire) ; ne pas prévoir de marge
  pour une coupure de connexion le jour du dépôt.
- Compter les apports en nature dans le cofinancement quand l'appel les exclut.
- Noter « éligible » un critère dont on n'a pas la preuve documentaire : c'est « à vérifier ».
- Laisser le score masquer un critère bloquant ; ou, à l'inverse, décider NO-GO sur un critère
  contournable sans avoir examiné le portage ou le partenariat.
- Sous-estimer les délais des professionnels et des administrations (certification des comptes,
  récépissé, relevé bancaire) : ce sont les postes qui font échouer les candidatures.
- Oublier les exclusions (projet déjà financé par le même bailleur, cumul interdit, candidat
  précédent non éligible).
- Imposer le gabarit du plugin alors que le bailleur impose un formulaire : le formulaire du
  bailleur prime toujours ; le gabarit sert à préparer le contenu.
- Inventer l'adresse de contact du bailleur dans le mail-type.
- Présenter l'inclusion et l'impact social comme des intentions sans chiffres ni preuves.
- Oublier de mettre à jour `projet/ETAT.md` : la décision et le rétro-planning doivent survivre à
  une coupure.

## Références et sources à vérifier

- Le texte de l'appel et ses lignes directrices (source principale) ; en cas de divergence avec ce
  skill, l'appel prime.
- `projet/financements/cartographie.md` et `skills/cartographie-bailleurs/references/bailleurs.md`
  pour la logique générale du bailleur et son domaine officiel.
- Page officielle de l'appel : à rouvrir la veille du dépôt pour vérifier toute modification
  (prolongation, rectificatif, foire aux questions).
- Si WebSearch est disponible : « "<nom du bailleur>" "<intitulé de l'appel>" <année> FAQ »,
  « lauréats <intitulé de l'appel> <année précédente> » (pour estimer la sélectivité et le profil
  des projets retenus).
- Documents nationaux : conditions d'enregistrement des associations et entreprises (OHADA pour
  les entreprises dans les pays membres), délais du greffe — via `icc-juridique`.
- Tout montant, taux, date ou critère chiffré cité dans la fiche doit porter sa source (citation
  de l'appel, document du promoteur) ou la mention [À VÉRIFIER].

## Passage de relais

Selon la décision :
- **GO ou GO SOUS CONDITIONS** : enchaîner, dans l'ordre du rétro-planning, avec
  `/icc:statut-juridique` (si portage ou pièces juridiques, agent `icc-juridique`),
  `/icc:budget-cofinancement` (agent `icc-budget`, budget au format du bailleur et cofinancement),
  `/icc:note-conceptuelle` puis `/icc:reecriture-humanisee` (agent `icc-redaction`),
  `/icc:plan-mise-en-oeuvre` si un chronogramme ou un cadre logique est exigé (agent
  `icc-mise-en-oeuvre`), `/icc:pitch-dossier-presse` pour les pièces artistiques (agent
  `icc-communication`). Les pièces sont rangées dans `projet/dossiers/<slug-bailleur>/`.
- **NO-GO** : retour à `/icc:cartographie-bailleurs` (agent `icc-financements`) pour choisir un
  autre bailleur ou préparer la prochaine session de cet appel ; noter les conditions à réunir
  d'ici là.

Mise à jour obligatoire de `projet/ETAT.md` (créer le fichier avec la structure imposée s'il
n'existe pas) :
- « Dernière mise à jour » : date et heure ; « Agent actif : icc-financements | Skill en cours :
  /icc:matching-appel » (ou le skill suivant) ;
- « Étapes terminées » : « Matching de l'appel <intitulé> — projet/financements/matching-<slug-appel>.md
  — décision : <GO / NO-GO / GO SOUS CONDITIONS>, score <n>/100 » ;
- « Étape en cours » : étape du rétro-planning en cours ;
- « Prochaines étapes » : les lignes du rétro-planning dans l'ordre, avec dates ;
- « Décisions prises / hypothèses à confirmer » : la décision, les notes marquées [estimation], les
  hypothèses de cofinancement ;
- « Questions en attente de réponse du promoteur » et questions envoyées au bailleur (gabarit F)
  avec date d'envoi ;
- « Alertes » : date limite (avec fuseau), conditions à lever et leur date, pièces manquantes,
  professionnels humains requis (expert-comptable, avocat, notaire, commissaire aux comptes).
