---
name: fiche-projet
description: Utiliser quand un promoteur ICC veut décrire, structurer ou diagnostiquer son projet culturel (fiche projet, présentation, résumé, diagnostic, maturité, SWOT, objectifs SMART, « par où commencer », « comment présenter mon projet »). Produit projet/fiche-projet.md, pivot lu par tous les autres skills.
---

# /icc:fiche-projet — Fiche-projet standard et diagnostic de maturité

## Objectif

Produire `projet/fiche-projet.md`, la FICHE-PROJET STANDARD du promoteur : un document unique,
complet et structuré qui décrit le projet, son porteur, ses publics, son budget estimatif, son
stade de maturité et ses besoins d'accompagnement.

Cette fiche est le document pivot du plugin `icc`. Tous les autres skills (`/icc:cartographie-bailleurs`,
`/icc:matching-appel`, `/icc:budget-cofinancement`, `/icc:note-conceptuelle`, `/icc:statut-juridique`,
`/icc:pitch-dossier-presse`, etc.) la lisent en premier et NE DOIVENT PLUS reposer les questions
auxquelles elle répond. Elle doit donc être rédigée avec soin : chaque rubrique vide ou approximative
se paiera plus tard dans tous les dossiers.

Ce skill est porté par l'agent `icc-diagnostic`. Il s'adresse à un promoteur qui peut n'avoir aucune
expérience administrative : les questions sont simples, posées par blocs, avec des exemples de réponses.

## Quand l'utiliser / ne pas l'utiliser

Utiliser ce skill :
- au tout début de l'accompagnement, juste après l'accueil par `icc-orchestrateur` ;
- quand `projet/fiche-projet.md` n'existe pas, ou qu'il date de plus de six mois, ou que le projet a
  changé de nature (nouveau périmètre, nouveau budget, nouvelle structure porteuse) ;
- quand un autre skill constate que la fiche est incomplète sur une rubrique dont il a besoin
  (il renvoie alors ici plutôt que de poser ses propres questions).

Ne pas l'utiliser :
- pour rédiger un document destiné à un bailleur : c'est `/icc:note-conceptuelle` (agent
  `icc-redaction`) qui s'en charge, en partant de la fiche ;
- pour chiffrer le budget en détail : la fiche ne contient qu'un budget global estimatif ; le détail
  relève de `/icc:budget-cofinancement` (agent `icc-budget`) ;
- pour trancher le statut juridique : la fiche constate la situation ; le choix relève de
  `/icc:statut-juridique` (agent `icc-juridique`).

## Prérequis (fichiers projet/ à lire si présents, informations nécessaires)

1. Lire `projet/ETAT.md` s'il existe : il indique où en est le promoteur et les questions déjà posées.
2. Lire `projet/fiche-projet.md` s'il existe : ne pas repartir de zéro, proposer une mise à jour
   rubrique par rubrique.
3. Lire `projet/journal.md` s'il existe (échanges antérieurs, anecdotes, chiffres cités).
4. Lire toute pièce que le promoteur dépose dans `projet/pieces/` (synopsis, statuts, CV, devis, teaser
   décrit, lettres) : chaque pièce lue évite une question.
5. Créer les dossiers `projet/` et `projet/pieces/` s'ils n'existent pas.

Informations nécessaires (collectées par le questionnaire ci-dessous si absentes) : identité du
promoteur, structure porteuse ou absence de structure, secteur, titre et idée du projet, publics,
calendrier approximatif, ordre de grandeur du budget, pièces en main.

## Procédure étape par étape

Étape 0 — Reprise. Si `projet/ETAT.md` existe, lire la section « Étape en cours » et reprendre au bloc
du questionnaire indiqué. Sinon créer `projet/ETAT.md` avec la structure imposée (voir « Passage de
relais ») et noter « Skill en cours : /icc:fiche-projet — Bloc A ».

Étape 1 — Cadrage (2 minutes). Expliquer au promoteur, en trois phrases, ce qu'est la fiche-projet,
pourquoi elle lui servira pour tous ses dossiers, et qu'il peut s'arrêter à tout moment : tout est
enregistré dans `projet/`. Préciser qu'aucune réponse n'est « mauvaise » et qu'un « je ne sais pas »
est une information utile (il devient un besoin d'accompagnement).

Étape 2 — Questionnaire de diagnostic progressif. Poser les blocs A à H dans l'ordre (gabarit 2),
un bloc à la fois, jamais plus de 5 questions par message. Après chaque bloc :
- reformuler les réponses en 2-3 lignes et demander confirmation ;
- écrire immédiatement les réponses dans `projet/fiche-projet.md` (rubriques correspondantes) ;
- mettre à jour `projet/ETAT.md` (« Bloc X terminé, Bloc Y en cours »).
Cette écriture incrémentale est essentielle en cas de coupure de connexion.

Étape 3 — Résumés en 3 versions. À partir des réponses, rédiger le résumé du projet en 1 phrase,
en 5 lignes et en 1 page (gabarit 1, rubrique 3). Les soumettre au promoteur ; corriger jusqu'à ce
qu'il dise « oui, c'est mon projet ». Conserver ses mots quand ils sont justes.

Étape 4 — Objectifs SMART. Transformer les intentions exprimées en un objectif général et 2 à 4
objectifs spécifiques SMART (le terme est expliqué dans le gabarit 1). Vérifier chaque objectif avec
la question : « Comment saurez-vous, à la fin, que c'est atteint ? »

Étape 5 — Publics et inclusion. Remplir la rubrique « Publics et bénéficiaires » avec les données
ventilées (femmes/hommes, jeunes, personnes handicapées, zones rurales, langues nationales). Quand
le promoteur n'a pas de chiffres, noter une estimation marquée « (estimation à confirmer) » et
proposer une méthode simple pour l'obtenir (fiche d'inscription, comptage à l'entrée, sondage).

Étape 6 — Budget global estimatif. Demander un ordre de grandeur en FCFA ; convertir en EUR au taux
fixe 1 EUR = 655,957 FCFA (XAF ou XOF selon le pays) ; afficher les deux. Noter ce qui est déjà
sécurisé (argent disponible, apport en nature valorisé, promesses écrites) et calculer le %. Ne pas
inventer de chiffres : si le promoteur n'a rien, écrire « Budget non chiffré — à construire avec
/icc:budget-cofinancement » et donner seulement la fourchette qu'il vise.

Étape 7 — Grille de maturité. Appliquer la grille d'autoévaluation notée (gabarit 3) avec le
promoteur, critère par critère, en s'appuyant sur des faits observables (pièces, dates, chiffres),
pas sur le ressenti. En déduire le niveau (1 à 5) et l'écrire dans la fiche avec la justification.

Étape 8 — SWOT. Remplir le tableau forces/faiblesses/opportunités/menaces (gabarit 1, rubrique 13)
en partant des réponses des blocs précédents. Expliquer le terme. Limiter à 3-5 points par case,
concrets.

Étape 9 — Besoins d'accompagnement et pièces. Cocher la checklist des pièces (rubrique 15), lister
les besoins d'accompagnement et, pour chacun, le skill ou l'agent `icc` compétent, ainsi que les
professionnels humains à solliciter (expert-comptable, avocat, notaire…) et pourquoi.

Étape 10 — Relecture finale. Appliquer les « Critères de qualité du livrable ». Lire la fiche à voix
haute au promoteur (ou la lui faire lire) ; corriger. Dater la fiche.

Étape 11 — Passage de relais et mise à jour de `projet/ETAT.md` (voir dernière section).

Mode faible connectivité : les blocs A à H peuvent être remplis hors ligne par le promoteur sur
papier ou dans un fichier texte à partir du gabarit 2 ; à la reconnexion, coller les réponses et
reprendre à l'étape 3.

## Questions à poser au promoteur

Le questionnaire complet est dans le gabarit 2. Règles de conduite :
- une question à la fois pour les débutants ; regrouper par bloc pour les structures expérimentées ;
- toujours donner un exemple de réponse ;
- accepter les réponses orales retranscrites, les listes, les approximations marquées comme telles ;
- ne jamais reposer une question dont la réponse figure dans `projet/` ;
- quand le promoteur hésite entre plusieurs projets, l'aider à en choisir UN pour cette fiche (les
  autres sont notés dans « Décisions prises / hypothèses à confirmer » de `projet/ETAT.md`).

Questions de relance utiles quand une réponse est trop vague :
- « Racontez-moi la dernière fois où vous avez travaillé concrètement sur ce projet. »
- « Si le projet réussit, que verra-t-on de différent dans un an ? Qui le verra ? »
- « Qui vous a déjà aidé, même un peu ? Qui vous a dit non, et pourquoi ? »
- « Qu'avez-vous déjà dépensé, en argent ou en temps ? »

## Gabarits complets

### Gabarit 1 — `projet/fiche-projet.md` (à copier tel quel)

```markdown
# FICHE-PROJET STANDARD — <Titre du projet>
Date de la fiche : AAAA-MM-JJ | Version : 1 | Rédigée avec /icc:fiche-projet
Statut des informations : [x] confirmées par le promoteur [ ] estimations à confirmer (marquées « (est.) »)

## 1. Identité du promoteur
| Champ | Réponse |
|---|---|
| Nom et prénom | |
| Rôle dans le projet (porteur, réalisateur, directeur artistique…) | |
| Ville, pays | |
| Téléphone / WhatsApp / courriel | |
| Langues de travail (français, anglais, langues nationales) | |
| Parcours en 3 lignes (formation, réalisations, années de pratique) | |
| Expérience de gestion de projet financé (oui/non ; lequel, montant, bailleur) | |

## 2. Structure porteuse
| Champ | Réponse |
|---|---|
| Existe-t-il une structure ? (oui / non / en cours) | |
| Forme (association, SARL, EI, coopérative, GIE, collectif informel) | |
| Nom, date de création, numéro de récépissé ou RCCM | |
| Compte bancaire au nom de la structure (oui/non ; banque) | |
| Nombre de membres / salariés / bénévoles (ventilé femmes/hommes) | |
| Si pas de structure : option envisagée (créer une association, portage par une structure existante — laquelle ?) | |

## 3. Secteur et titre
| Champ | Réponse |
|---|---|
| Secteur ICC principal | musique / cinéma-audiovisuel / arts visuels / mode-design / édition / jeu vidéo / arts du spectacle / artisanat d'art / patrimoine / médias-numérique |
| Sous-secteur (ex. documentaire, festival, prêt-à-porter, BD) | |
| Titre du projet (et titre provisoire si différent) | |

### 3a. Résumé en 1 phrase (30 mots max)
<Qui fait quoi, pour qui, où, avec quel résultat attendu.>

### 3b. Résumé en 5 lignes
<Contexte en 1 ligne ; projet en 2 lignes ; publics et résultat en 1 ligne ; calendrier et budget global en 1 ligne.>

### 3c. Résumé en 1 page (environ 400 mots)
<Contexte et problème — Le projet et son originalité — Publics et bénéficiaires — Résultats et impact
social — Porteur et partenaires — Calendrier et budget — Ce qui est demandé.>

## 4. Problème ou opportunité
<Quelle situation le projet veut-il changer ou saisir ? Faits observés, chiffres connus (avec source),
témoignages. Pourquoi maintenant ? Pourquoi ici ?>

## 5. Objectifs
Objectif général (le changement large auquel le projet contribue) :
<…>

Objectifs spécifiques SMART. SMART = Spécifique (un seul résultat clair), Mesurable (un chiffre ou un
fait vérifiable), Atteignable (avec vos moyens), Réaliste (dans votre contexte) et Temporel (avec une
date). Exemple : « D'ici décembre 2027, projeter le film dans 10 villages du Lac et toucher 2 000
spectateurs dont au moins 50 % de femmes. »
| N° | Objectif spécifique | Indicateur (comment on mesure) | Cible | Échéance |
|---|---|---|---|---|
| OS1 | | | | |
| OS2 | | | | |
| OS3 | | | | |

## 6. Activités principales
| N° | Activité | Lié à l'objectif | Période | Responsable | Coût estimatif (FCFA) |
|---|---|---|---|---|---|
| A1 | | | | | |
| A2 | | | | | |
| A3 | | | | | |
| A4 | | | | | |

## 7. Publics et bénéficiaires
| Catégorie | Qui précisément | Nombre estimé | dont femmes | dont jeunes (15-35 ans) | dont personnes handicapées | dont zones rurales | Langues |
|---|---|---|---|---|---|---|---|
| Bénéficiaires directs (participent, sont formés, sont filmés, vendent…) | | | | | | | |
| Bénéficiaires indirects (familles, communauté, public des diffusions) | | | | | | | |
| Partenaires / professionnels mobilisés | | | | | | | |
Comment ces chiffres seront-ils comptés ? <fiches d'inscription, billetterie, comptage, enquête>
Mesures d'inclusion prévues (accès, gratuité, sous-titres, langues nationales, horaires, garde d'enfants, accessibilité physique) :
<…>

## 8. Résultats attendus et impact social
| Résultat (ce qui existera à la fin) | Indicateur | Cible | Preuve (photo, liste, rapport, lien) |
|---|---|---|---|
| R1 | | | |
| R2 | | | |
| R3 | | | |
Impact social visé (changement durable pour les personnes et le territoire : revenus, emploi, visibilité
de groupes peu représentés, cohésion, patrimoine préservé, égalité femmes-hommes) :
<…>

## 9. Partenaires
| Partenaire | Rôle (coproduction, diffusion, hébergement, formation, financement) | Statut : acquis (lettre signée) / pressenti (discussion) / à contacter | Pièce disponible |
|---|---|---|---|
| | | | |

## 10. Calendrier indicatif
| Phase | Début | Fin | Jalons (étapes clés datées) |
|---|---|---|---|
| Préparation / développement | | | |
| Réalisation / production | | | |
| Diffusion / commercialisation | | | |
| Bilan et rapports | | | |

## 11. Budget global estimatif
| Poste (grandes masses) | FCFA | EUR (1 EUR = 655,957 FCFA) | % du total |
|---|---|---|---|
| Ressources humaines et cachets | | | |
| Équipements et location de matériel | | | |
| Production (déplacements, hébergement, consommables) | | | |
| Diffusion, communication, événements | | | |
| Fonctionnement et frais administratifs | | | |
| Imprévus (5 à 10 %) | | | |
| TOTAL | | | 100 % |

| Financement | Montant FCFA | Montant EUR | Statut (sécurisé / promis / espéré) |
|---|---|---|---|
| Apport propre en argent | | | |
| Apport en nature valorisé (matériel, local, temps bénévole) | | | |
| Partenaires acquis | | | |
| Recettes propres attendues (billetterie, ventes) | | | |
| Montant recherché auprès de bailleurs | | | |
Part déjà sécurisée : <X> % du total. Devise du bailleur visé : <EUR / USD / autre — à afficher aussi>.

## 12. Stade de maturité
Niveau retenu : <1 à 5> — <intitulé> (voir grille en annexe de la fiche). Justification en 3 lignes,
basée sur des faits observables : <…>

## 13. SWOT
SWOT = Forces (Strengths), Faiblesses (Weaknesses), Opportunités (Opportunities), Menaces (Threats).
Forces et faiblesses dépendent de vous ; opportunités et menaces viennent de l'extérieur.
| Forces (internes, à valoriser) | Faiblesses (internes, à corriger) |
|---|---|
| | |
| **Opportunités (externes, à saisir)** | **Menaces (externes, à anticiper)** |
| | |

## 14. Besoins d'accompagnement
| Besoin | Priorité (haute/moyenne/basse) | Skill ou agent icc | Professionnel humain requis ? Pourquoi ? |
|---|---|---|---|
| | | | |

## 15. Pièces disponibles (checklist)
| Pièce | Disponible | Emplacement (projet/pieces/…) | À produire / à mettre à jour |
|---|---|---|---|
| Statuts de la structure | [ ] | | |
| Récépissé / RCCM / attestation d'existence | [ ] | | |
| RIB au nom de la structure | [ ] | | |
| Pièce d'identité du représentant | [ ] | | |
| CV du porteur et de l'équipe clé | [ ] | | |
| Portfolio / dossier artistique / filmographie | [ ] | | |
| Teaser, maquette, échantillons, photos | [ ] | | |
| Synopsis / note d'intention / concept | [ ] | | |
| Devis (matériel, prestataires) | [ ] | | |
| Lettres de soutien ou de partenariat | [ ] | | |
| Rapports d'activité ou bilans des années passées | [ ] | | |
| Budget détaillé | [ ] | | |
| Autorisations (tournage, occupation d'espace, droits) | [ ] | | |

## 16. Historique des versions
| Version | Date | Modifications |
|---|---|---|
| 1 | | Création |
```

### Gabarit 2 — Questionnaire de diagnostic progressif (blocs A à H)

À poser dans l'ordre. Entre parenthèses : exemple de réponse à proposer au promoteur s'il bloque.

**Bloc A — Vous et votre structure** (alimente rubriques 1 et 2)
1. Comment vous appelez-vous et quel est votre rôle dans le projet ? (« Je suis réalisatrice, c'est
   mon film. »)
2. Où êtes-vous basé(e) ? (ville, pays)
3. Depuis combien de temps pratiquez-vous votre activité ? Qu'avez-vous déjà réalisé ? (« Deux
   courts-métrages auto-produits, un atelier de montage. »)
4. Avez-vous une structure déclarée (association, entreprise, coopérative) ? Si oui, laquelle, depuis
   quand, avec un compte bancaire ? Si non, connaissez-vous une structure qui pourrait vous porter ?
5. Avez-vous déjà géré un financement reçu d'un partenaire ? Lequel, quel montant ?

**Bloc B — Le projet en quelques mots** (alimente rubriques 3 et 4)
6. Dans quel domaine se situe votre projet ? (musique, cinéma, mode, édition…)
7. Racontez-moi votre projet comme à un ami, en quelques phrases.
8. Quel problème voulez-vous régler, ou quelle occasion voulez-vous saisir ? (« Personne ne montre le
   travail des femmes pêcheuses ; elles-mêmes ne se voient jamais à l'écran. »)
9. Pourquoi ce projet maintenant ? Qu'est-ce qui a déclenché l'idée ?
10. Qu'est-ce qui le rend différent de ce qui existe déjà ?

**Bloc C — Ce que vous voulez atteindre** (alimente rubriques 5 et 8)
11. Si tout réussit, que verra-t-on de différent dans un an ? Dans trois ans ?
12. Donnez-moi un, deux ou trois résultats concrets avec un chiffre. (« Un film de 26 minutes terminé ;
    10 projections ; 2 000 spectateurs. »)
13. Comment saurez-vous que c'est atteint ? Que pourrez-vous montrer ?

**Bloc D — Ce que vous allez faire** (alimente rubriques 6 et 10)
14. Quelles sont les grandes étapes, de maintenant à la fin ? (« Repérages, tournage, montage,
    diffusion. »)
15. Pour chaque étape : quand, combien de temps, qui s'en occupe ?
16. Qu'avez-vous déjà fait ? Qu'est-ce qui est prêt aujourd'hui ?

**Bloc E — Pour qui** (alimente rubrique 7)
17. Qui profite directement du projet ? Combien de personnes environ ?
18. Parmi elles, combien de femmes ? de jeunes (15-35 ans) ? de personnes handicapées ? de
    personnes vivant en zone rurale ? Si vous ne savez pas, dites-le : on notera une estimation.
19. Dans quelles langues le projet s'adresse-t-il à ses publics ?
20. Qu'est-ce qui pourrait empêcher certaines personnes d'y accéder (prix, distance, horaires,
    handicap) et que prévoyez-vous pour y remédier ?

**Bloc F — Avec qui et avec quoi** (alimente rubriques 9 et 11)
21. Qui vous accompagne déjà (personnes, structures, lieux) ? Avez-vous un écrit de leur part ?
22. Qui aimeriez-vous avoir comme partenaire et pourquoi ?
23. Quel budget total imaginez-vous, en FCFA ? Même approximatif. (« Entre 15 et 20 millions. »)
24. Qu'avez-vous déjà : argent, matériel, local, temps bénévole, promesses écrites ?
25. Avez-vous déjà des devis ou des prix connus pour les gros postes ?

**Bloc G — Vos forces et vos difficultés** (alimente rubriques 12, 13 et 14)
26. De quoi êtes-vous le plus fier dans ce projet ou votre parcours ?
27. Qu'est-ce qui vous manque le plus aujourd'hui ? (argent, structure, producteur, compétence,
    matériel, réseau)
28. Qu'est-ce qui, à l'extérieur, pourrait aider le projet ? (un appel à projets, un festival, un
    événement national, une demande du marché)
29. Qu'est-ce qui, à l'extérieur, pourrait le mettre en danger ? (saison des pluies, insécurité,
    hausse des prix, départ d'un partenaire, délai administratif)
30. Sur quoi voulez-vous être accompagné(e) en priorité ?

**Bloc H — Vos papiers** (alimente rubrique 15)
31. Parcourons la liste des pièces : pour chacune, l'avez-vous ? Où est-elle ? Est-elle à jour ?
32. Pouvez-vous déposer celles que vous avez dans `projet/pieces/` (ou m'en dicter le contenu) ?

### Gabarit 3 — Grille d'autoévaluation de maturité (notée)

Noter chaque critère de 0 à 2 selon des faits observables ; total sur 20.
| Critère | 0 point | 1 point | 2 points | Note |
|---|---|---|---|---|
| Formulation du projet | idée orale seulement | texte d'une page | dossier écrit (synopsis, concept, note) | |
| Preuve de concept artistique | rien à montrer | esquisses, maquette, démo | teaser, pilote, prototype, édition test réalisée | |
| Équipe | porteur seul | 1-2 personnes identifiées | équipe clé engagée par écrit | |
| Structure porteuse | aucune | en cours ou portage envisagé | structure déclarée avec compte bancaire | |
| Publics | non définis | décrits qualitativement | chiffrés et ventilés (genre, jeunes, rural) | |
| Budget | aucun chiffre | ordre de grandeur | budget par postes avec devis | |
| Financement | 0 % sécurisé | apport en nature ou promesses | au moins 10 % sécurisé par écrit | |
| Partenaires | aucun | pressentis | au moins une lettre signée | |
| Calendrier | aucun | grandes phases | jalons datés | |
| Expérience de gestion | aucune | un petit projet géré | un financement externe géré et rapporté | |
| **TOTAL /20** | | | | |

Correspondance notée → niveau de maturité (grille à 5 niveaux) :
| Niveau | Intitulé | Score indicatif | Critères observables | Ce qu'il est réaliste de viser |
|---|---|---|---|---|
| 1 | Idée | 0-4 | intention orale, pas d'écrit, pas d'équipe, pas de chiffre | bourses de développement, résidences d'écriture, formations, petits fonds locaux |
| 2 | Concept | 5-8 | texte écrit, premiers contacts, ordre de grandeur budgétaire | aides au développement, appels pour premiers projets, incubateurs |
| 3 | Prototype / pilote | 9-12 | preuve de concept réalisée (teaser, édition test, collection capsule), équipe partielle, budget par postes | aides à la production, fonds thématiques, cofinancements modestes |
| 4 | En cours | 13-16 | structure déclarée, financement partiel sécurisé, activités démarrées, partenaires signés | appels structurants, financements pluriannuels, coproductions |
| 5 | Consolidation | 17-20 | plusieurs éditions ou œuvres livrées, rapports financiers passés, équipe stable | partenariats long terme, investisseurs, programmes d'accélération |

Le niveau n'est pas un jugement de valeur : il sert à orienter vers les financements réellement
accessibles (éligibles) plutôt que vers ceux qui seront refusés (non éligibles) ou incertains
(à vérifier). Un bailleur qui exige deux ans d'existence juridique écartera mécaniquement un projet
de niveau 1-2 sans structure, quelle que soit sa qualité artistique.

### Gabarit 4 — Exemple rempli complet : scénario 1 (documentaire, Tchad)

Les noms sont fictifs ; les chiffres marqués « (est.) » sont des estimations du promoteur à confirmer.

```markdown
# FICHE-PROJET STANDARD — « Les filets du lac » (titre provisoire)
Date de la fiche : 2026-10-30 | Version : 1 | Rédigée avec /icc:fiche-projet
Statut des informations : [x] confirmées par le promoteur [x] estimations à confirmer (marquées « (est.) »)

## 1. Identité du promoteur
| Champ | Réponse |
|---|---|
| Nom et prénom | Achta M. (nom fictif) |
| Rôle | Réalisatrice et porteuse du projet |
| Ville, pays | N'Djamena, Tchad |
| Contact | WhatsApp et courriel fournis (non reproduits ici) |
| Langues | français, arabe tchadien, notions de kanembou |
| Parcours | Formation en audiovisuel à N'Djamena ; deux courts-métrages auto-produits (fiction 12 min, 2023 ; portrait 8 min, 2024) ; assistante réalisation sur un documentaire étranger tourné au Tchad en 2025 |
| Expérience de gestion de financement | Non. A géré ses propres fonds (environ 400 000 FCFA sur le portrait de 2024). |

## 2. Structure porteuse
| Champ | Réponse |
|---|---|
| Structure ? | Non |
| Option envisagée | (a) créer une association culturelle à N'Djamena, ou (b) portage par une société de production tchadienne existante avec laquelle un premier contact a eu lieu (pas d'écrit). Décision à prendre avec /icc:statut-juridique. |
| Compte bancaire | Compte personnel uniquement. |

## 3. Secteur et titre
| Champ | Réponse |
|---|---|
| Secteur | cinéma-audiovisuel |
| Sous-secteur | court-métrage documentaire (26 min) |
| Titre | « Les filets du lac » (provisoire) |

### 3a. Résumé en 1 phrase
Un documentaire de 26 minutes réalisé par une réalisatrice tchadienne donne la parole aux femmes
pêcheuses du lac Tchad, dont le travail nourrit des villages entiers mais reste invisible.

### 3b. Résumé en 5 lignes
Sur les rives tchadiennes du lac Tchad, des femmes pêchent, fument et vendent le poisson, mais ne
sont jamais représentées ni dans les médias ni dans les décisions. « Les filets du lac » les suit
pendant une saison de pêche et laisse leurs voix structurer le récit, en arabe tchadien et en
kanembou sous-titrés. Le film sera projeté dans les villages filmés puis en festivals. Tournage
prévu sur 2027 ; budget global visé 25 000 EUR (16 398 925 FCFA), 0 % sécurisé à ce jour.

### 3c. Résumé en 1 page
<Rédigé à partir des blocs B, C, E, F — environ 400 mots. Non reproduit dans cet exemple pour la
place ; suit le plan : contexte et problème / le film et son point de vue / publics / résultats et
impact / porteuse et partenaires / calendrier et budget / ce qui est demandé.>

## 4. Problème ou opportunité
Les femmes assurent une part importante de la transformation et de la vente du poisson sur les
rives du lac, mais les images du lac Tchad qui circulent parlent de sécurité ou de climat, jamais
d'elles. Elles ne se voient pas à l'écran et ne sont pas consultées. La réalisatrice a passé trois
semaines en repérage en 2025 auprès d'un groupement de fumeuses de poisson et dispose d'un teaser
de 3 min tourné à cette occasion. Chiffres de contexte : à documenter avec sources (FAO, ministère
de la Pêche) — [À VÉRIFIER].

## 5. Objectifs
Objectif général : contribuer à la visibilité et à la reconnaissance du rôle économique et social des
femmes du lac Tchad par le cinéma documentaire.
| N° | Objectif spécifique | Indicateur | Cible | Échéance |
|---|---|---|---|---|
| OS1 | Réaliser un documentaire de 26 min sous-titré FR/EN | film livré (fichier master) | 1 film | déc. 2027 (est.) |
| OS2 | Projeter le film auprès des communautés filmées | nombre de projections et de spectateurs | 10 projections, 2 000 spectateurs dont 50 % de femmes (est.) | juin 2028 (est.) |
| OS3 | Diffuser en festivals et à la télévision | sélections, diffusions | 3 sélections, 1 diffusion TV (est.) | déc. 2028 (est.) |

## 6. Activités principales
| N° | Activité | Objectif | Période | Responsable | Coût est. (FCFA) |
|---|---|---|---|---|---|
| A1 | Écriture et repérages complémentaires | OS1 | T1 2027 | réalisatrice | à chiffrer |
| A2 | Tournage (3 semaines, 2 sessions) | OS1 | T2-T3 2027 | réalisatrice + chef opérateur | à chiffrer |
| A3 | Montage, étalonnage, mixage, sous-titrage | OS1 | T4 2027 | monteur (à recruter) | à chiffrer |
| A4 | Projections villageoises avec écran gonflable et débats | OS2 | S1 2028 | réalisatrice + partenaire local | à chiffrer |
| A5 | Inscriptions festivals, dossier de presse | OS3 | 2028 | réalisatrice | à chiffrer |

## 7. Publics et bénéficiaires
| Catégorie | Qui | Nombre | dont femmes | dont jeunes | dont pers. handicapées | dont rural | Langues |
|---|---|---|---|---|---|---|---|
| Directs | femmes du groupement filmées et leurs familles | 40 (est.) | 30 | 15 (est.) | non connu | 40 | arabe tchadien, kanembou |
| Indirects | spectateurs des projections villageoises et urbaines | 2 000 (est.) | 1 000 visé | 800 (est.) | à prévoir (accès) | 1 500 (est.) | idem + FR |
| Professionnels | équipe technique tchadienne, stagiaires | 6 (est.) | 3 visé | 4 | — | 0 | FR |
Comptage : feuilles de présence aux projections, estimation visuelle validée par deux personnes.
Inclusion : projections gratuites, en plein air, en langues nationales ; horaires après la vente du
poisson ; place réservée aux personnes à mobilité réduite ; au moins une femme dans l'équipe technique.

## 8. Résultats attendus et impact social
| Résultat | Indicateur | Cible | Preuve |
|---|---|---|---|
| R1 Film 26 min terminé | master livré | 1 | fichier, visa de censure si requis |
| R2 Communautés voient le film | spectateurs | 2 000 (est.) | feuilles de présence, photos |
| R3 Visibilité nationale/internationale | sélections | 3 (est.) | courriels de sélection |
Impact social : reconnaissance du travail des femmes pêcheuses ; archives filmées d'un savoir-faire ;
formation de jeunes techniciens tchadiens ; matière pour le plaidoyer du groupement.

## 9. Partenaires
| Partenaire | Rôle | Statut | Pièce |
|---|---|---|---|
| Groupement de fumeuses de poisson (village A) | participation, accès, logistique | acquis oralement | lettre à rédiger (/icc:note-conceptuelle, gabarit lettre de soutien) |
| Société de production tchadienne | portage administratif, coproduction | pressenti | aucune |
| Institut français du Tchad | projection à N'Djamena | à contacter | aucune |

## 10. Calendrier indicatif
| Phase | Début | Fin | Jalons |
|---|---|---|---|
| Développement | nov. 2026 | mars 2027 | fiche, statut, budget, 2 dossiers déposés |
| Production | avr. 2027 | déc. 2027 | tournage sessions 1 et 2 ; montage terminé |
| Diffusion | janv. 2028 | déc. 2028 | 10 projections ; 3 inscriptions festivals |
| Bilan | déc. 2028 | fév. 2029 | rapport narratif et financier |

## 11. Budget global estimatif
Total visé : 25 000 EUR = 16 398 925 FCFA (XAF). Répartition par postes : non chiffrée — à construire
avec /icc:budget-cofinancement à partir de devis. Financement : apport en nature (caméra personnelle,
temps de la réalisatrice) à valoriser ; 0 % sécurisé en argent. Montant recherché : la totalité, à
répartir entre 2-3 bailleurs (cofinancement = part du budget que le bailleur exige que vous apportiez
vous-même ou via d'autres sources).

## 12. Stade de maturité
Niveau 2 — Concept (score 7/20 : formulation 1, preuve de concept 2 grâce au teaser, équipe 0,
structure 0, publics 1, budget 0, financement 0, partenaires 1, calendrier 1, expérience 1).
Le teaser est un atout de niveau 3 ; l'absence de structure et de budget maintient le projet au
niveau 2. Priorité : statut puis budget.

## 13. SWOT
| Forces | Faiblesses |
|---|---|
| Teaser de 3 min existant ; accès de confiance au groupement ; maîtrise des langues du terrain ; réalisatrice tchadienne, femme, sur un sujet de femmes | Pas de structure ni de compte ; pas de producteur ; budget non chiffré ; pas d'expérience de reporting |
| **Opportunités** | **Menaces** |
| Intérêt des fonds francophones et des festivals documentaires pour les voix d'Afrique centrale ; thématiques genre et climat ; portage possible par une production locale | Accès au lac soumis à la situation sécuritaire et à la saison ; hausse des coûts de transport ; délais de création d'association ; calendrier des appels à vérifier |

## 14. Besoins d'accompagnement
| Besoin | Priorité | Skill / agent | Professionnel humain |
|---|---|---|---|
| Choisir entre association et portage | haute | /icc:statut-juridique (icc-juridique) | notaire ou juriste pour les statuts si association ; avocat pour le contrat de portage |
| Chiffrer le budget | haute | /icc:budget-cofinancement (icc-budget) | expert-comptable si le bailleur exige des états certifiés |
| Identifier les appels (OIF/Fonds Image, Institut français, Goethe, festivals) | haute | /icc:cartographie-bailleurs puis /icc:matching-appel | — |
| Rédiger la note conceptuelle | moyenne | /icc:note-conceptuelle puis /icc:reecriture-humanisee | — |
| Pitch | basse | /icc:pitch-dossier-presse | — |

## 15. Pièces disponibles
| Pièce | Disponible | Emplacement | À produire |
|---|---|---|---|
| Synopsis | [x] | projet/pieces/synopsis.md | mettre à jour après repérages |
| Teaser 3 min | [x] | lien privé noté dans projet/pieces/teaser.md | sous-titrer en FR/EN |
| CV | [ ] | | /icc:note-conceptuelle (gabarit CV) |
| Statuts, récépissé, RIB | [ ] | | après /icc:statut-juridique |
| Devis | [ ] | | location matériel, post-production |
| Lettres de soutien | [ ] | | groupement, société de production |
| Budget détaillé | [ ] | | /icc:budget-cofinancement |
```

## Critères de qualité du livrable

- Les 16 rubriques existent ; aucune n'est vide : au minimum « non renseigné — raison — qui/quand ».
- Les trois résumés sont cohérents entre eux et avec les objectifs ; le promoteur les reconnaît comme
  « son » projet.
- Chaque objectif spécifique a un indicateur, une cible et une échéance ; les activités renvoient à
  un objectif ; les résultats renvoient à une preuve.
- Les publics sont chiffrés et ventilés (femmes, jeunes, handicap, rural, langues) ; les estimations
  sont marquées « (est.) » ; les mesures d'inclusion sont concrètes (pas « ouvert à tous »).
- Le budget est affiché en FCFA et en EUR (ou devise du bailleur) avec le taux fixe ; le % sécurisé
  est calculé ou explicitement « 0 % ». Aucun chiffre inventé.
- Le niveau de maturité est justifié par le score et des faits observables.
- Le SWOT contient 3 à 5 points concrets par case, sans généralités.
- Les besoins d'accompagnement renvoient à un skill `icc` précis et signalent les professionnels
  humains indispensables (statuts : notaire/juriste ; comptes certifiés : expert-comptable ;
  contrats : avocat).
- La fiche est datée, versionnée, écrite au vouvoiement quand elle s'adresse au promoteur, sans
  emoji, sans anglicisme inutile, chaque terme technique expliqué à sa première apparition.
- `projet/ETAT.md` est à jour.

## Erreurs fréquentes à éviter

- Poser les 32 questions d'un coup : le promoteur débutant abandonne. Un bloc à la fois.
- Écrire la fiche à la fin seulement : en cas de coupure, tout est perdu. Écrire après chaque bloc.
- Remplacer les mots du promoteur par du jargon de bailleur : la fiche doit rester lisible par lui.
- Inventer des chiffres de contexte (« 70 % des femmes… ») sans source : marquer « [À VÉRIFIER] ».
- Confondre activités (ce qu'on fait) et résultats (ce qui existe à la fin) ou objectifs (le changement).
- Noter la maturité « au ressenti » : s'appuyer sur la grille et des pièces.
- Oublier la ventilation genre/jeunes/handicap/rural, puis devoir réinterroger pour chaque dossier.
- Omettre la structure porteuse ou le compte bancaire : c'est le premier critère d'éligibilité de la
  plupart des bailleurs.
- Promettre un financement : parler d'éligibilité et de probabilité.
- Laisser la fiche sans date ni version : les autres skills ne sauront pas si elle est à jour.

## Références et sources à vérifier

- Grille de maturité : inspirée des grilles courantes d'incubateurs ICC et de la logique des appels
  (développement / production / diffusion) ; adapter aux critères de l'appel visé — « usage général,
  vérifier dans les lignes directrices de l'appel en cours ».
- Définition SMART : usage général en gestion de projet.
- Taux de change : parité fixe 1 EUR = 655,957 XAF/XOF (Banque de France / BEAC / BCEAO — site
  officiel).
- Données de contexte sectoriel (pêche, culture, emploi) : institut national de statistique du pays,
  ministère de tutelle, UNESCO, FAO — toujours citer la source et l'année ; si WebSearch est
  disponible, lancer « <pays> statistiques <secteur> <année> » et noter « [À VÉRIFIER — source : …] ».
- Pour les exigences juridiques (récépissé d'association, RCCM, OHADA) : `/icc:statut-juridique`.

## Passage de relais (quel agent/skill ensuite, et mise à jour de projet/ETAT.md)

Ordre recommandé après la fiche, à adapter au niveau de maturité :
- Pas de structure ou structure fragile → `/icc:statut-juridique` (agent `icc-juridique`).
- Budget non chiffré → `/icc:budget-cofinancement` puis `/icc:plan-tresorerie` (agent `icc-budget`).
- Structure et budget en place → `/icc:cartographie-bailleurs` puis `/icc:matching-appel`
  (agent `icc-financements`).
- Appel identifié → `/icc:note-conceptuelle` puis `/icc:reecriture-humanisee` (agent `icc-redaction`).
- Projet en cours ou en consolidation → `/icc:plan-mise-en-oeuvre`, `/icc:suivi-evaluation`
  (agent `icc-mise-en-oeuvre`), `/icc:pitch-dossier-presse`, `/icc:crowdfunding` (agent
  `icc-communication`).
- Dans tous les cas, rendre la main à `icc-orchestrateur` qui confirme l'ordre.

Mise à jour obligatoire de `projet/ETAT.md` (dernière étape) :

```markdown
# ÉTAT DU PROJET — <nom du projet>
Dernière mise à jour : AAAA-MM-JJ HH:MM
Agent actif : icc-diagnostic | Skill en cours : /icc:fiche-projet (terminé)
## Résumé du projet (5 lignes max)
<copier le résumé 3b de la fiche>
## Étapes terminées (avec fichiers produits)
- Fiche-projet standard v1 : projet/fiche-projet.md (niveau de maturité : <n>)
## Étape en cours (où on en est précisément)
- Fiche terminée ; passage de relais à <agent/skill>.
## Prochaines étapes (ordre recommandé)
1. <skill 1> — 2. <skill 2> — 3. <skill 3>
## Décisions prises / hypothèses à confirmer
- <ex. : option de portage par une société de production à confirmer>
## Questions en attente de réponse du promoteur
- <ex. : nombre exact de membres du groupement partenaire>
## Alertes (délais, pièces manquantes, professionnel humain requis)
- <ex. : statuts à faire relire par un juriste ; aucune pièce administrative disponible>
```
