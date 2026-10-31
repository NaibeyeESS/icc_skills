---
name: reecriture-humanisee
description: Utiliser quand un texte de dossier (note conceptuelle, pitch, lettre, bio) sonne générique, artificiel ou « écrit par une machine » et doit être réécrit dans la voix du promoteur (humaniser, rendre naturel, plus vivant, moins robotique, reformuler, « ça ne me ressemble pas »). Produit une version .v2.md à côté de l'original, sans changer les faits ni le format du bailleur.
---

# /icc:reecriture-humanisee — Réécriture humanisée d'un texte de dossier

## Objectif

Réécrire un texte destiné à un bailleur ou à un partenaire (note conceptuelle, pitch, lettre de
motivation, lettre de soutien, biographie, résumé de projet) pour qu'il soit naturel, incarné,
crédible et spécifique : un lecteur doit avoir l'impression d'entendre le promoteur, pas de lire un
texte interchangeable produit par un outil automatique.

Trois contraintes non négociables :
1. Les faits ne bougent pas : chiffres, dates, noms, engagements, montants, cibles restent
   strictement identiques à l'original ou aux fichiers de `projet/`.
2. Le format du bailleur est respecté : longueur (pages, mots, caractères), rubriques et leur
   ordre, langue, registre (formel pour une administration, plus libre pour une fondation).
3. L'original n'est jamais écrasé : le résultat est écrit dans `<fichier>.v2.md` à côté de
   l'original (ex. `projet/dossiers/oif-fonds-image/note-conceptuelle.v2.md`). S'il existe déjà un
   `.v2.md`, créer `.v3.md`, etc.

Ce skill est porté par l'agent `icc-redaction`. Il intervient après la mise en conformité
(`/icc:note-conceptuelle`) et avant le dépôt.

## Quand l'utiliser / ne pas l'utiliser

Utiliser ce skill :
- quand le promoteur dit « ça ne me ressemble pas », « c'est trop plat », « on dirait tous les
  dossiers », « ça fait machine » ;
- quand la grille de relecture de `/icc:note-conceptuelle` donne une note faible en « Originalité
  et point de vue » ou en « Clarté » alors que la conformité est bonne ;
- avant le dépôt de tout texte où le jury lit beaucoup de dossiers semblables (fondations,
  résidences, programmes d'accélération, festivals) ;
- pour une bio d'artiste, un pitch écrit, une lettre, dans la langue du dossier (français ou
  anglais).

Ne pas l'utiliser :
- sur un texte non encore conforme au format du bailleur : d'abord `/icc:note-conceptuelle` ;
- pour changer le fond (objectifs, budget, activités) : c'est `/icc:fiche-projet`,
  `/icc:budget-cofinancement` ou `/icc:note-conceptuelle` ;
- pour traduire un dossier : la traduction est un autre travail (et, si une traduction officielle est
  exigée, elle relève d'un traducteur professionnel, parfois assermenté) ; ce skill réécrit dans la
  langue du texte cible ;
- pour maquiller une faiblesse réelle (absence de budget, de partenaires, d'expérience) : un texte
  plus vivant ne remplace pas un fait manquant ; le signaler plutôt.

## Prérequis (fichiers projet/ à lire si présents, informations nécessaires)

1. `projet/ETAT.md` — lire en premier ; reprendre si une réécriture est en cours.
2. Le fichier cible (chemin donné par le promoteur ou par `ETAT.md`) — lire intégralement.
3. `projet/fiche-projet.md` — source de vérité pour les faits et la voix (résumés, anecdotes, mots
   du promoteur notés par `/icc:fiche-projet`).
4. `projet/budget/budget.md` — pour vérifier chaque chiffre financier.
5. `projet/dossiers/<slug>/plan-impose.md` et `lignes-directrices.md` — contraintes de forme
   (longueur par rubrique, langue, registre, intitulés).
6. `projet/journal.md` et `projet/communication/pitch.md` — s'ils existent, ils contiennent souvent
   la manière dont le promoteur parle réellement de son projet.
7. `projet/voix-promoteur.md` — s'il existe (créé par ce skill lors d'un premier passage), le
   réutiliser sans reposer les questions.

Informations nécessaires : la « voix » du promoteur (questionnaire ci-dessous si
`projet/voix-promoteur.md` n'existe pas), les limites de longueur, le registre attendu, la langue.

## Procédure étape par étape

Étape 0 — Reprise et sauvegarde. Lire `ETAT.md`. Vérifier que le fichier cible existe. Ne jamais
le modifier. Créer `<fichier>.v2.md` vide (ou `.v3.md` si `.v2.md` existe). Noter dans `ETAT.md` :
« Skill en cours : /icc:reecriture-humanisee — étape 1 — cible : <chemin> ».

Étape 1 — Lire et cartographier le texte cible. Numéroter les paragraphes (P1, P2…). Pour chaque
paragraphe, relever dans un tableau de travail : la rubrique du bailleur, le nombre de mots, les
faits qu'il contient (chiffres, dates, noms, engagements). Ce relevé sert à la vérification finale
(gabarit D).

Étape 2 — Collecter la voix du promoteur. Si `projet/voix-promoteur.md` n'existe pas, poser les
3 à 5 questions du gabarit C, une à la fois, et enregistrer les réponses dans ce fichier. Garder
les formulations exactes du promoteur (entre guillemets), pas une paraphrase. Si le promoteur n'est
pas joignable (faible connectivité), utiliser les résumés et anecdotes de `fiche-projet.md` et le
noter comme hypothèse dans `ETAT.md`.

Étape 3 — Diagnostiquer les tics génériques. Passer le texte au crible de la liste du gabarit A.
Pour chaque occurrence, noter le paragraphe et le type de tic. Compter. Un texte avec plus d'un
tic par paragraphe en moyenne a besoin d'une réécriture complète ; en dessous, de retouches.

Étape 4 — Réécrire paragraphe par paragraphe. Pour chaque paragraphe, produire la version
réécrite et la consigner dans le tableau avant/après (gabarit B) avec la raison du changement.
Règles d'écriture :
- commencer par le fait ou la personne, pas par le concept (« Les femmes du groupement vendent le
  poisson fumé au marché de … » plutôt que « Dans un contexte marqué par … ») ;
- un détail concret vérifiable par paragraphe (lieu, geste, objet, chiffre, nom de lieu, saison) tiré
  de la fiche, de la voix du promoteur ou de l'original — jamais inventé ;
- remplacer les superlatifs et adjectifs d'évaluation par des faits ; supprimer les triades
  automatiques quand deux termes ou un seul suffisent ;
- varier la longueur des phrases ; accepter une phrase courte ; éviter le parallélisme systématique ;
- préférer la voix active et un sujet identifiable (« nous », « la réalisatrice », « le collectif ») ;
- garder les mots du promoteur quand ils sont justes, y compris des mots de langues nationales
  expliqués entre parenthèses ;
- conserver le registre exigé : une administration attend un ton formel mais pas creux ; une
  fondation accepte la première personne ;
- garder intacts les mots-clés de l'appel que le bailleur attend (ils peuvent être critères de
  notation), mais les intégrer dans des phrases qui disent quelque chose ;
- ne rien ajouter qui ne soit pas dans l'original ou dans `projet/` : aucune nouvelle promesse,
  aucun nouveau chiffre, aucun nouveau partenaire.
Écrire chaque paragraphe réécrit dans `<fichier>.v2.md` au fur et à mesure (reprise possible).

Étape 5 — Vérification factuelle. Appliquer le protocole du gabarit D : chaque chiffre, date, nom,
montant et engagement du v2 doit exister dans l'original ou dans `projet/` ; chaque fait de
l'original doit se retrouver dans le v2 (sauf suppression volontaire validée par le promoteur). Toute
divergence est corrigée avant de continuer.

Étape 6 — Contrôle de longueur et de format. Compter les mots ou caractères par rubrique et au
total ; comparer à `plan-impose.md`. Vérifier que les intitulés et l'ordre des rubriques sont
inchangés, que la langue est homogène, que le registre correspond. Réduire si dépassement ; ne pas
combler artificiellement si le texte est plus court que la limite (plus court est permis).

Étape 7 — Liste de contrôle « texte humain ». Noter le v2 avec le gabarit E. Viser ≥ 24/30 et
aucun critère à 1. Retoucher les paragraphes responsables des notes faibles.

Étape 8 — Lecture au promoteur. Lui présenter le tableau avant/après et lui faire lire le v2
(idéalement à voix haute). Question de validation : « Est-ce que vous pourriez dire cela à un jury,
avec ces mots ? » Corriger ce qu'il refuse ou ne reconnaît pas. Noter ses refus dans
`projet/voix-promoteur.md` (section « Ce qu'il refuse de dire »).

Étape 9 — Livraison. `<fichier>.v2.md` final ; `projet/dossiers/<slug>/reecriture-<fichier>.md`
contenant le tableau avant/après, le diagnostic des tics, le protocole de vérification rempli et la
note « texte humain ». L'original reste inchangé.

Étape 10 — Mise à jour de `projet/ETAT.md` (voir « Passage de relais »).

Mode faible connectivité : tout se fait hors ligne à partir des fichiers de `projet/` ; seule la
collecte de la voix exige le promoteur ; en son absence, travailler avec la fiche et marquer les
hypothèses.

## Questions à poser au promoteur

Trois à cinq questions, une à la fois, réponses notées entre guillemets dans
`projet/voix-promoteur.md` (gabarit C). Ne pas les reposer si ce fichier existe.
1. « Racontez-moi votre projet comme vous le feriez à quelqu'un que vous rencontrez au marché ou dans
   un taxi, en une minute. » (capturer le vocabulaire, le rythme, l'ordre des idées)
2. « Quel moment précis vous a décidé à faire ce projet ? Où étiez-vous, qu'avez-vous vu ou entendu ? »
   (anecdote fondatrice, détails sensoriels)
3. « Quels chiffres connaissez-vous par cœur sur votre projet ou votre terrain ? » (les chiffres
   qu'il connaît sont ceux qu'il défendra devant un jury)
4. « Y a-t-il des mots que vous employez toujours pour en parler, y compris dans une autre langue que
   le français ? Et des mots que vous détestez ou que vous ne voulez pas voir dans votre dossier ? »
5. « Qu'est-ce que vous refusez de dire ou de promettre, même si ça ferait bien dans un dossier ? »
   (limites éthiques, prudence, sécurité des personnes)
Question de validation finale (étape 8) : « Pourriez-vous dire cela à un jury, avec ces mots ? »

## Gabarits complets

### Gabarit A — Liste de diagnostic des tics génériques

Cocher chaque tic repéré, noter le paragraphe. Les exemples en anglais servent pour les dossiers en
anglais.
| N° | Tic générique | Exemples (FR) | Exemples (EN) | Remède |
|---|---|---|---|---|
| 1 | Formule creuse d'ouverture | « Dans un monde où… », « À l'heure où… », « Depuis la nuit des temps… », « Il est important de noter que… », « Force est de constater que… » | "In today's world…", "In an increasingly…", "It is important to note that…", "It goes without saying…" | supprimer ; commencer par le fait |
| 2 | Superlatifs et adjectifs d'évaluation non prouvés | « unique », « innovant », « exceptionnel », « incontournable », « d'une importance capitale » | "unique", "innovative", "cutting-edge", "game-changing", "vibrant" | remplacer par le fait qui le prouve |
| 3 | Triades automatiques | « sensibiliser, former et accompagner » ; « local, national et international » ; « jeunes, femmes et personnes vulnérables » sans contenu | "educate, empower and inspire"; "local, national and global" | garder les termes nécessaires, préciser chacun |
| 4 | Structures trop symétriques | phrases de même longueur, parallélismes en série, listes à puces de trois mots partout | same | varier longueur et rythme ; une phrase courte |
| 5 | Absence de détails concrets | « les communautés locales », « des activités culturelles », « des partenaires clés » | "local communities", "key stakeholders", "various activities" | nommer : quel village, quelle activité, quel partenaire |
| 6 | Passif et sujets flous | « il sera procédé à », « des actions seront menées », « il est prévu que » | "activities will be carried out", "it is envisaged that" | sujet actif : « nous », « l'équipe », « la réalisatrice » |
| 7 | Nominalisations en chaîne | « la mise en place d'un processus de renforcement des capacités de structuration » | "the implementation of a capacity-building framework" | verbes : « former 12 musiciens à … » |
| 8 | Anglicismes et jargon de bailleur non expliqués | « empowerment », « mainstreaming », « stakeholders », « capacity building », « impactful » | jargon équivalent : "leverage", "synergies", "holistic", "ecosystem" | mot français précis ; expliquer le terme imposé la première fois |
| 9 | Promesses non tenables | « ce projet transformera durablement… », « garantira », « éliminera » | "will transform", "will ensure", "will eradicate" | « vise à », cible chiffrée, hypothèses |
| 10 | Connecteurs mécaniques | « De plus », « Par ailleurs », « En outre », « Ainsi » en début de chaque paragraphe ; « En conclusion » | "Moreover", "Furthermore", "Additionally", "In conclusion" | supprimer ou remplacer par un lien de sens |
| 11 | Répétition du nom du projet ou des mots-clés de l'appel | mot-clé de l'appel à chaque phrase | same | une fois par rubrique, dans une phrase qui apporte quelque chose |
| 12 | Phrases qui ne disent rien | « La culture est un vecteur de développement. » « Le projet s'inscrit dans une dynamique. » | "Culture is a powerful tool for development." | supprimer ou remplacer par un fait du projet |
| 13 | Absence de la personne | aucun « je/nous », aucun nom, aucune anecdote | same | une présence humaine par rubrique quand le registre le permet |
| 14 | Hedging excessif ou assurance excessive | « il semblerait que potentiellement », ou au contraire « indéniablement » | "arguably", "undeniably" | affirmer ce qui est su, qualifier ce qui est estimé « (est.) » |
| 15 | Fin de paragraphe en résumé | dernière phrase qui répète la première | same | finir sur un fait ou une ouverture |
Total de tics : <n> pour <p> paragraphes → ratio <n/p>. ≥ 1 : réécriture complète ; < 1 : retouches.

### Gabarit B — Tableau avant/après (`reecriture-<fichier>.md`)

```markdown
# Réécriture humanisée — <fichier cible> — AAAA-MM-JJ
Original : <chemin> (inchangé) | Version réécrite : <chemin>.v2.md
Contraintes : <langue> ; <limite mots/pages par rubrique> ; registre <formel / libre> ; rubriques inchangées.
Voix du promoteur : projet/voix-promoteur.md

| § | Rubrique | Avant (original) | Après (v2) | Tics corrigés (n° gabarit A) | Faits conservés | Mots avant → après |
|---|---|---|---|---|---|---|
| P1 | | | | | | |
| P2 | | | | | | |
```

### Gabarit C — Questionnaire de voix (`projet/voix-promoteur.md`)

```markdown
# Voix du promoteur — <nom> — recueillie le AAAA-MM-JJ par /icc:reecriture-humanisee
## 1. Le projet raconté à l'oral (transcription fidèle, 1 minute)
« … »
## 2. Anecdote fondatrice (lieu, moment, ce qui a été vu ou entendu)
« … »
## 3. Chiffres que le promoteur connaît par cœur (avec ce qu'ils désignent)
- « … » → <vérifié dans fiche-projet.md §… / budget.md §… / à vérifier>
## 4. Mots qu'il emploie (y compris en langues nationales, avec traduction)
- « … » = <sens>
## 5. Mots qu'il refuse / ce qu'il ne veut pas dire ou promettre
- « … » — raison : <…>
## 6. Registre souhaité
<formel / direct / à la première personne / au nom du collectif> ; langue(s) du dossier : <…>
## 7. Refus et corrections exprimés lors des lectures (mis à jour à chaque passage)
- AAAA-MM-JJ : « … »
```

### Gabarit D — Protocole de vérification factuelle

À remplir pour chaque texte réécrit ; aucune ligne en « non » ne peut subsister au moment de la
livraison.
| Élément du v2 | Type (chiffre / date / nom / montant / engagement / lieu) | Présent dans l'original ? | Présent dans projet/ (fichier §) ? | Conforme ? | Action |
|---|---|---|---|---|---|
| | | oui / non | oui / non | oui / non | garder / corriger / supprimer |
Contrôle inverse (faits de l'original absents du v2) :
| Fait de l'original | Paragraphe | Repris dans le v2 ? | Si non : suppression validée par le promoteur ? |
|---|---|---|---|
Règles : (1) un chiffre du v2 absent de l'original ET de `projet/` est supprimé, pas « arrondi » ;
(2) une estimation reste marquée comme telle ; (3) un engagement (« nous nous engageons à… ») ne
peut être ni ajouté ni renforcé ; (4) un nom de personne ou de lieu ne peut être ajouté sans accord
du promoteur (sécurité des personnes filmées ou citées) ; (5) les montants restent affichés dans les
deux devises de l'original.

### Gabarit E — Liste de contrôle « texte humain » (notée)

Noter chaque critère de 1 (non) à 3 (oui, nettement) ; total sur 30 ; viser ≥ 24, aucun 1.
| N° | Critère | Question | Note /3 |
|---|---|---|---|
| 1 | Entrée en matière | Le premier paragraphe commence-t-il par un fait, une personne ou un lieu plutôt que par un concept ? | |
| 2 | Détails concrets | Chaque rubrique contient-elle au moins un détail vérifiable (lieu, chiffre, objet, geste, nom) ? | |
| 3 | Présence du porteur | Sent-on qui parle (nous, je, nom de la structure) et d'où il parle ? | |
| 4 | Chiffres incarnés | Les chiffres sont-ils reliés à quelque chose de visible (« 10 projections dans les villages du lac » plutôt que « 10 activités ») ? | |
| 5 | Rythme | Les phrases ont-elles des longueurs variées ; y a-t-il au moins une phrase courte par rubrique ? | |
| 6 | Vocabulaire | Les mots sont-ils ceux du promoteur et du terrain, le jargon imposé expliqué ? | |
| 7 | Absence de superlatifs | Peut-on supprimer tous les « unique / innovant / exceptionnel » sans perte ? (oui = 3) | |
| 8 | Voix active | Les acteurs sont-ils nommés comme sujets de verbes d'action ? | |
| 9 | Honnêteté | Les estimations sont-elles marquées, les hypothèses explicites, sans promesse ? | |
| 10 | Test de la lecture à voix haute | Le promoteur pourrait-il dire ce texte à un jury avec ces mots ? | |
| **TOTAL /30** | | | |

### Gabarit F — Exemple avant/après : paragraphe de contexte, scénario 1 (documentaire, Tchad)

Contrainte : rubrique « Contexte et justification », 200 mots maximum, français, registre formel
(institut culturel). Faits issus de `projet/fiche-projet.md` (noms fictifs, estimations marquées).

| | Texte |
|---|---|
| **Avant (original, 118 mots)** | Dans un monde où les femmes jouent un rôle crucial dans le développement économique, il est important de noter que leur contribution reste largement invisible. Le lac Tchad constitue un écosystème unique et exceptionnel où les communautés locales font face à de nombreux défis. Ce projet innovant vise à sensibiliser, valoriser et autonomiser les femmes pêcheuses à travers un documentaire impactant qui transformera durablement les représentations. Par ailleurs, des activités de diffusion seront menées auprès des parties prenantes afin de garantir un impact maximal au niveau local, national et international. Ainsi, ce film s'inscrit dans une dynamique de promotion de la diversité culturelle et de l'égalité des genres. |
| **Tics repérés** | n° 1 (« Dans un monde où », « il est important de noter »), 2 (« crucial », « unique et exceptionnel », « innovant », « impactant »), 3 (« sensibiliser, valoriser et autonomiser » ; « local, national et international »), 5 (« communautés locales », « parties prenantes », « nombreux défis »), 6 (« des activités seront menées »), 9 (« transformera durablement », « garantir »), 10 (« Par ailleurs », « Ainsi »), 12 (« s'inscrit dans une dynamique »). Ratio : 8 tics pour 1 paragraphe → réécriture complète. |
| **Après (v2, 131 mots)** | Sur la rive tchadienne du lac Tchad, ce sont des femmes qui fument le poisson et le vendent sur les marchés ; leur travail fait vivre des villages entiers. Pourtant, les images du lac qui circulent parlent de sécurité ou de climat, presque jamais d'elles. En 2025, la réalisatrice Achta M. a passé trois semaines auprès d'un groupement de fumeuses de poisson et en a rapporté un teaser de 3 minutes : les femmes y racontent leur journée en arabe tchadien et en kanembou, et demandent à se voir à l'écran. « Les filets du lac », documentaire de 26 minutes, part de cette demande. Ce sont leurs voix qui structurent le film. Il sera projeté d'abord dans les villages filmés (10 projections, 2 000 spectateurs visés, dont la moitié de femmes — estimation), puis en festivals. |
| **Vérification factuelle** | « 2025 », « trois semaines », « teaser de 3 minutes », « 26 minutes », « 10 projections », « 2 000 spectateurs », « moitié de femmes (est.) », « arabe tchadien », « kanembou » : tous présents dans fiche-projet.md §3b, §4, §5, §7. Aucun fait ajouté ; les engagements (« transformera », « garantir ») de l'original, non tenables, sont remplacés par des cibles marquées comme estimations. Longueur : 131 mots ≤ 200. Registre formel conservé (pas de première personne). |
| **Note « texte humain »** | 27/30 (critère 3 « présence du porteur » à 2 : registre formel, troisième personne ; critère 5 à 2 : une phrase courte supplémentaire possible). |

### Gabarit G — Adaptation pour un dossier en anglais

Quand le texte cible est en anglais, appliquer la même procédure dans la langue du texte ; ne pas
traduire mot à mot un paragraphe français réécrit. Repères spécifiques :
- l'anglais des dossiers tolère la première personne du pluriel et des phrases plus courtes ; en
  profiter ;
- les tics anglais les plus fréquents : "In today's world", "empower", "vibrant", "leverage",
  "stakeholders", "holistic", "impactful", "showcase", "journey", "resilience" employé sans fait ;
- garder les termes exigés par l'appel ("outcomes", "outputs", "logframe") en les utilisant une fois
  correctement ;
- les montants : FCFA et devise du bailleur, séparateur de milliers anglais (16,398,925 FCFA ;
  EUR 25,000) ;
- faire relire par un locuteur compétent si le promoteur n'écrit pas en anglais ; signaler qu'une
  relecture professionnelle est souhaitable pour un dossier à fort enjeu.

Exemple court (bio, 2 phrases) :
| Avant | After |
|---|---|
| "Achta M. is a passionate and innovative Chadian filmmaker committed to empowering local communities through impactful storytelling." | "Achta M. is a filmmaker based in N'Djamena. She has made two self-produced short films (2023, 2024) and worked as assistant director on a documentary shot in Chad in 2025; her next film follows the women who smoke and sell fish on the shores of Lake Chad." |
(Faits : fiche-projet.md §1. Tics supprimés : n° 2, 5, 8.)

## Critères de qualité du livrable

- L'original est intact ; le v2 existe à côté, avec le même plan, les mêmes intitulés et le même
  ordre de rubriques.
- Protocole de vérification factuelle (gabarit D) rempli : aucun chiffre, date, nom, montant ou
  engagement ajouté, supprimé sans validation, modifié ou arrondi ; estimations toujours marquées ;
  montants dans les deux devises.
- Longueur par rubrique et totale dans les limites de `plan-impose.md` ; langue homogène ; registre
  conforme.
- Diagnostic des tics (gabarit A) et tableau avant/après (gabarit B) complets, paragraphe par
  paragraphe, avec la raison de chaque changement.
- Note « texte humain » (gabarit E) ≥ 24/30, aucun critère à 1.
- Genre, inclusion et impact social restent présents et aussi précis qu'avant (données ventilées,
  mesures concrètes) : la réécriture ne doit pas les diluer en formules.
- Les mots-clés de l'appel attendus par le bailleur sont conservés une fois par rubrique, dans des
  phrases qui portent du sens.
- Le promoteur a lu le v2 et peut le dire avec ses mots ; ses refus sont notés dans
  `projet/voix-promoteur.md`.
- Pas d'emoji, pas d'anglicisme non expliqué, termes techniques expliqués à la première apparition.
- `projet/ETAT.md` est à jour.

## Erreurs fréquentes à éviter

- Écraser l'original : toujours `.v2.md` à côté.
- « Améliorer » un chiffre, arrondir, ajouter un partenaire ou un engagement pour faire mieux.
- Inventer une anecdote ou un détail sensoriel qui n'est ni dans l'original, ni dans `projet/`, ni
  dans la bouche du promoteur.
- Remplacer les tics d'une machine par ceux d'une autre : lyrisme, métaphores filées, questions
  rhétoriques en série, phrases d'une ligne partout.
- Casser le format : dépasser la limite de mots, fusionner deux rubriques, changer un intitulé imposé.
- Passer à la première personne dans un dossier administratif qui attend la troisième personne, ou
  l'inverse dans une candidature à une fondation qui attend la voix de l'artiste.
- Supprimer les mots-clés de l'appel parce qu'ils « sonnent jargon » alors qu'ils sont critères de
  notation : les garder, les expliquer, les incarner.
- Diluer la rubrique genre/inclusion en une phrase élégante mais sans chiffres.
- Faire parler le promoteur comme il ne parle pas : un texte « vivant » qu'il ne reconnaît pas sera
  mal défendu à l'oral.
- Traduire le v2 français en anglais mot à mot pour un dossier anglais.
- Oublier que la réécriture ne corrige pas un fond faible : si le budget est incohérent, renvoyer à
  `/icc:budget-cofinancement`.

## Références et sources à vérifier

- Contraintes de forme : `projet/dossiers/<slug>/plan-impose.md` et `lignes-directrices.md`
  (produits par `/icc:note-conceptuelle`) ; en cas de doute, le texte officiel de l'appel prime.
- Faits : `projet/fiche-projet.md`, `projet/budget/budget.md`, `projet/pieces/`.
- Voix : `projet/voix-promoteur.md`, `projet/journal.md`, `projet/communication/pitch.md`.
- Principes d'écriture claire : guides de rédaction administrative et de « langage clair » (usage
  général) ; aucune règle de style ne prime sur le format du bailleur.
- Pour une relecture linguistique professionnelle (dossier en anglais à fort enjeu, traduction
  officielle exigée) : traducteur ou relecteur professionnel, parfois traducteur assermenté — à
  prévoir dans le calendrier et le budget.

## Passage de relais (quel agent/skill ensuite, et mise à jour de projet/ETAT.md)

- v2 validé → retour à `/icc:note-conceptuelle` (agent `icc-redaction`) pour l'assemblage final du
  dossier et le dépôt, ou directement au dépôt si tout est prêt.
- Faiblesse de fond révélée par la réécriture (chiffre manquant, partenaire non confirmé) →
  `/icc:fiche-projet` (agent `icc-diagnostic`), `/icc:budget-cofinancement` (agent `icc-budget`) ou
  `/icc:statut-juridique` (agent `icc-juridique`) selon le cas.
- Même travail souhaité sur le pitch ou le dossier de presse → `/icc:pitch-dossier-presse` (agent
  `icc-communication`) puis nouveau passage ici sur le fichier produit.
- Dans tous les cas, informer `icc-orchestrateur` de la version à déposer.

Mise à jour obligatoire de `projet/ETAT.md` (dernière étape) :

```markdown
# ÉTAT DU PROJET — <nom du projet>
Dernière mise à jour : AAAA-MM-JJ HH:MM
Agent actif : icc-redaction | Skill en cours : /icc:reecriture-humanisee (terminé pour <fichier>)
## Résumé du projet (5 lignes max)
<inchangé — copier depuis fiche-projet.md §3b>
## Étapes terminées (avec fichiers produits)
- Réécriture humanisée : <chemin>.v2.md (note « texte humain » <n>/30 ; vérification factuelle : conforme)
- Tableau avant/après et diagnostic : projet/dossiers/<slug>/reecriture-<fichier>.md
- Voix du promoteur : projet/voix-promoteur.md
## Étape en cours (où on en est précisément)
- <ex. : v2 validé par le promoteur ; version à déposer = .v2.md>
## Prochaines étapes (ordre recommandé)
1. Assemblage et dépôt (/icc:note-conceptuelle) — 2. <suite>
## Décisions prises / hypothèses à confirmer
- <ex. : registre formel retenu ; voix recueillie sans le promoteur à partir de la fiche (hypothèse)>
## Questions en attente de réponse du promoteur
- <ex. : accord pour citer le nom du village partenaire>
## Alertes (délais, pièces manquantes, professionnel humain requis)
- <ex. : relecture professionnelle en anglais recommandée avant le <date limite>>
```
