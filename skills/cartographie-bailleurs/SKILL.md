---
name: cartographie-bailleurs
description: Utiliser quand un promoteur ICC demande qui peut financer son projet, cherche des bailleurs, subventions, fonds, fondations, mécènes, sponsors, bourses, résidences ou prêts, veut une liste de financeurs par secteur, pays ou montant, ou dit « où trouver de l'argent », « qui finance la culture ».
---

# /icc:cartographie-bailleurs — Cartographie des bailleurs pertinents

## Objectif

Construire, pour un promoteur de projet dans les industries culturelles et créatives (ICC), une
cartographie écrite et exploitable des bailleurs (= organismes qui apportent de l'argent : fonds
publics, coopération internationale, fondations, banques, plateformes, incubateurs) susceptibles
de financer SON projet, en croisant cinq axes :

1. le secteur ICC (musique, cinéma/audiovisuel, arts visuels, mode/design, édition, jeux vidéo,
   spectacle vivant, artisanat d'art, patrimoine, médias numériques) ;
2. le pays du promoteur et la zone géographique couverte par le bailleur ;
3. le stade de maturité du projet (idée, développement, production, diffusion, structuration
   d'entreprise, passage à l'échelle) ;
4. la fourchette de montant recherchée ;
5. le type de structure du promoteur : sans statut juridique / association / entreprise
   (ou coopérative).

Le livrable canonique est `projet/financements/cartographie.md` : un tableau par famille de
bailleurs, chaque ligne portant un verdict explicite (éligible / non éligible / à vérifier) avec
sa justification, la source officielle à consulter et l'action suivante. La cartographie est une
porte d'entrée vers `/icc:matching-appel`, qui analyse ensuite UN appel précis.

Agent principal : `icc-financements`. Ce skill ne promet jamais un financement : il parle
d'éligibilité, de probabilité et de qualité du dossier.

## Quand l'utiliser / ne pas l'utiliser

Utiliser ce skill quand :
- le promoteur ne sait pas vers quels bailleurs se tourner ou n'en connaît qu'un ou deux ;
- le projet change de nature (par exemple passage d'un atelier informel à une marque) et la liste
  des financeurs possibles doit être refaite ;
- le promoteur veut un plan de financement combinant plusieurs sources (subvention + billetterie
  + sponsors + crowdfunding) ;
- l'agent `icc-orchestrateur` ou `icc-diagnostic` a terminé la fiche-projet et oriente vers les
  financements.

Ne pas l'utiliser quand :
- le promoteur a déjà UN appel à projets en main et veut savoir s'il peut candidater : utiliser
  `/icc:matching-appel` ;
- le besoin est de rédiger le dossier de candidature : `/icc:note-conceptuelle` ;
- le besoin est de chiffrer le budget ou le cofinancement : `/icc:budget-cofinancement` ;
- le projet n'a pas encore de description minimale (objectif, secteur, pays, ordre de grandeur du
  budget) : faire d'abord `/icc:fiche-projet`.

## Prérequis

Fichiers du dossier `projet/` à lire s'ils existent (ne pas reposer les questions auxquelles ils
répondent déjà) :
- `projet/ETAT.md` — état de session ; s'il existe, le lire en premier et reprendre à l'étape
  indiquée ;
- `projet/fiche-projet.md` — secteur, pays, stade, montant visé, statut, équipe, publics ;
- `projet/juridique/statut.md` — statut juridique actuel ou visé (détermine l'éligibilité à de
  nombreux programmes) ;
- `projet/budget/budget.md` — montant total et part déjà acquise, si le budget existe ;
- `projet/financements/cartographie.md` — version antérieure à mettre à jour plutôt qu'à refaire.

Informations minimales nécessaires (à demander si absentes) : secteur ICC précis, pays de résidence
et pays de réalisation, stade du projet, montant total recherché (en FCFA et en euros, parité fixe
1 EUR = 655,957 XAF/XOF), type de structure, calendrier souhaité, langue(s) de travail possibles,
capacité de cofinancement (= part du budget que le bailleur exige que vous apportiez vous-même ou
via d'autres sources).

Annexe à lire : `references/bailleurs.md` (annuaire structuré des bailleurs, avec leur domaine web
officiel et la logique de leurs programmes ; aucun montant ni date n'y figure, tout est à vérifier).

## Procédure étape par étape

La procédure est reprenable à n'importe quelle étape : après chaque étape, noter dans
`projet/ETAT.md` l'étape atteinte. Les étapes 1 à 4 et 6 à 8 sont réalisables hors ligne (à
partir de `references/bailleurs.md`) ; seule l'étape 5 (veille) nécessite la connexion.

### Étape 1 — Lire le contexte
Lire `projet/ETAT.md`, `projet/fiche-projet.md`, `projet/juridique/statut.md` si présents.
Extraire les cinq axes (secteur, pays, stade, montant, structure). Si une information manque,
poser uniquement les questions de la section « Questions à poser au promoteur » qui restent sans
réponse.

### Étape 2 — Établir le profil de financement
Remplir le gabarit A (« Profil de financement »). Déterminer notamment :
- si le promoteur peut recevoir des fonds en son nom (compte bancaire, statut) ou s'il doit passer
  par une structure porteuse (= association ou société déjà constituée qui reçoit et gère la
  subvention pour le compte du promoteur, moyennant une convention) ;
- la fourchette de montant par projet qui est cohérente avec le stade (un premier film ne cherche
  pas la même chose qu'une troisième édition de festival) ;
- la ou les langues de dossier possibles (français seul, ou anglais aussi) ;
- la capacité de cofinancement réelle (apport en nature compris : temps de travail, matériel,
  locaux — vérifier si le bailleur l'accepte).

### Étape 3 — Passer en revue les familles de bailleurs
Pour chacune des neuf familles ci-dessous, parcourir `references/bailleurs.md`, retenir les
bailleurs dont la zone géographique et les secteurs couvrent le projet, et rédiger une ligne par
bailleur dans le tableau correspondant du gabarit B :
1. coopération internationale et multilatérale ;
2. coopération bilatérale et instituts culturels (ambassades, Institut français, Goethe-Institut,
   British Council, Wallonie-Bruxelles International) ;
3. fondations privées ;
4. fonds nationaux et régionaux ;
5. banques, microfinance et investisseurs ;
6. crowdfunding (= financement participatif, collecte auprès du public) ;
7. incubateurs et programmes d'accélération ;
8. coproductions, diffuseurs et acheteurs (pour l'audiovisuel, le spectacle, l'édition) ;
9. résidences, bourses et prix.

Pour chaque ligne, attribuer le verdict :
- **Éligible** : le type de structure, le pays et le secteur correspondent explicitement à ce que
  le bailleur finance habituellement. Écrire pourquoi en une phrase.
- **Non éligible** : au moins un critère bloquant connu (par exemple, le bailleur ne finance que
  des personnes morales et le promoteur n'a pas de statut ; ou le pays n'est pas couvert). Écrire
  lequel, et indiquer si le blocage est contournable (structure porteuse, partenariat, changement
  de statut via `/icc:statut-juridique`).
- **À vérifier** : critère incertain ou information manquante. Écrire quelle information manque et
  où la chercher.

Ne jamais inscrire de montant, de date limite, de taux de cofinancement ou de critère chiffré sans
la mention « [À VÉRIFIER — source : site officiel du bailleur] ». Si le promoteur fournit un
document officiel (lignes directrices, appel), on peut citer ses chiffres en indiquant « source :
document fourni par le promoteur, daté du … ».

### Étape 4 — Classer et prioriser
Classer les lignes « éligible » et « à vérifier » selon trois critères simples : adéquation
(secteur + stade), accessibilité (langue, complexité du dossier, pièces exigées), calendrier
(prochain appel attendu dans le délai du promoteur). Remplir le gabarit C (« Top 5 prioritaire »).
Vérifier que le top 5 comporte au moins une source non concurrentielle (billetterie, pré-vente,
prestations, crowdfunding) pour ne pas dépendre uniquement des subventions.

### Étape 5 — Veille (si WebSearch ou WebFetch est disponible)
Pour chaque bailleur du top 5 puis, si le temps le permet, pour les autres lignes « à vérifier » :
- requêtes recommandées (remplacer l'année par l'année en cours et la suivante) :
  - `"<nom du bailleur>" appel à projets <année> culture`
  - `"<nom du bailleur>" "<secteur>" Afrique <année>`
  - `"<nom du programme>" lignes directrices` ou `guidelines`
  - `appel à candidatures <secteur> <pays> <année>`
  - `résidence artistique <secteur> Afrique <année>` ; `bourse <secteur> <pays> <année>`
- consulter en priorité les pages officielles (domaine indiqué dans `references/bailleurs.md`),
  puis les annuaires et newsletters spécialisés : la lettre d'information de l'Institut français
  local, les pages « appels » des délégations de l'Union européenne, les agendas des réseaux
  professionnels du secteur (réseaux de festivals, marchés du film africains, salons de design),
  les groupes professionnels locaux sur les réseaux sociaux et WhatsApp où circulent les appels ;
- pour chaque résultat, noter : date de publication de la page, date limite si indiquée (avec la
  mention [À VÉRIFIER]), URL de la page officielle consultée, et reporter dans la colonne
  « source officielle à consulter ». Ne jamais recopier une URL que l'on n'a pas effectivement
  ouverte ; sinon n'indiquer que le domaine officiel.
Sans connexion : remplir les colonnes à partir de `references/bailleurs.md`, marquer « veille à
faire » dans la colonne action suivante et lister dans le gabarit D les requêtes à lancer dès le
retour de la connexion (le promoteur peut les lancer lui-même depuis un téléphone).

### Étape 6 — Intégrer genre, inclusion et impact social
Pour chaque bailleur du top 5, noter dans la colonne « ce qu'il finance » si le programme accorde
une attention particulière aux femmes, aux jeunes, aux personnes en situation de handicap, aux
zones rurales, aux langues nationales ou à l'impact social. Remplir la rubrique « Atouts
d'inclusion du projet » du gabarit A : ce que le projet apporte réellement sur ces plans (sans
inventer), car c'est souvent un critère de sélection et toujours un argument de dossier.

### Étape 7 — Signaler les professionnels humains et les blocages
Lister dans le gabarit E les points qui exigent une personne qualifiée : création d'une structure
(notaire, greffe, avocat selon le pays), ouverture d'un compte bancaire dédié, attestation
comptable ou états financiers certifiés (expert-comptable ; commissaire aux comptes si le bailleur
exige des comptes audités), convention de portage (avocat ou juriste). Le skill n'écrit jamais
ces actes à la place du professionnel.

### Étape 8 — Rédiger le livrable et mettre à jour l'état
Écrire `projet/financements/cartographie.md` en assemblant les gabarits A à E remplis, dans
l'ordre. Créer le dossier `projet/financements/` s'il n'existe pas. Relire avec la grille de
« Critères de qualité du livrable ». Puis mettre à jour `projet/ETAT.md` (voir « Passage de
relais »).

## Questions à poser au promoteur

Poser uniquement celles qui ne trouvent pas de réponse dans `projet/fiche-projet.md`. Regrouper les
questions en un seul message pour économiser la connexion.

1. Dans quel pays résidez-vous, et dans quel(s) pays le projet se déroule-t-il ?
2. Dans quel secteur précis se situe le projet (par exemple : documentaire, festival de musique,
   marque de mode) et à quel stade en êtes-vous (idée, développement, production, diffusion,
   structuration, passage à l'échelle) ?
3. Quel montant total cherchez-vous, en FCFA ? Quelle part est déjà acquise ou apportée par vous ?
4. Avez-vous une structure juridique (association déclarée, entreprise, coopérative) ? Si non,
   connaissez-vous une structure qui pourrait porter le projet pour vous ?
5. Avez-vous un compte bancaire au nom de la structure ou à votre nom ? Dans quel pays ?
6. Pouvez-vous rédiger ou faire traduire un dossier en anglais si nécessaire ?
7. Quels bailleurs avez-vous déjà sollicités, avec quel résultat et quand ?
8. Quelle est votre échéance : à quelle date devez-vous disposer des fonds ?
9. Quelle part du budget pouvez-vous couvrir vous-même, en argent ou en nature (matériel, temps,
   locaux) ?
10. Votre projet implique-t-il particulièrement des femmes, des jeunes, des personnes en situation
    de handicap, des zones rurales ou des langues nationales ? De quelle manière concrète ?
11. Disposez-vous de documents déjà prêts : CV, portfolio, teaser, lettres de soutien, statuts,
    rapports d'activité, états financiers ?

## Gabarits complets

Copier les gabarits A à E dans `projet/financements/cartographie.md`, dans l'ordre, et les remplir.

### Gabarit A — Profil de financement

```markdown
# Cartographie des bailleurs — <nom du projet>
Date : AAAA-MM-JJ | Rédigé avec /icc:cartographie-bailleurs | Agent : icc-financements

## A. Profil de financement

| Axe | Valeur |
|---|---|
| Secteur ICC | <secteur précis> |
| Pays de résidence / pays du projet | <pays> / <pays> |
| Stade de maturité | <idée / développement / production / diffusion / structuration / passage à l'échelle> |
| Montant total recherché | <montant> FCFA (≈ <montant> EUR, parité 1 EUR = 655,957 FCFA) |
| Part déjà acquise ou apportée | <montant> FCFA (<pourcentage> %) |
| Type de structure | <sans statut / association / entreprise / coopérative> |
| Structure porteuse possible | <oui : nom / non / à chercher> |
| Compte bancaire | <au nom de la structure / personnel / aucun> — pays : <pays> |
| Langues de dossier possibles | <français / anglais / autre> |
| Capacité de cofinancement | <montant ou %> en numéraire ; <description> en nature |
| Échéance de financement | <date à laquelle les fonds sont nécessaires> |
| Bailleurs déjà sollicités | <liste, date, résultat> |

### Atouts d'inclusion et d'impact social du projet
| Dimension | Ce que le projet fait concrètement | Preuve disponible |
|---|---|---|
| Genre (femmes dans l'équipe, publics, sujet) | <texte> | <document, chiffre> |
| Jeunes | <texte> | <preuve> |
| Handicap / accessibilité | <texte> | <preuve> |
| Zones rurales / décentralisation | <texte> | <preuve> |
| Langues nationales | <texte> | <preuve> |
| Impact social ou économique (emplois, revenus, cohésion) | <texte> | <preuve> |
```

### Gabarit B — Tableaux par famille de bailleurs

Reproduire ce tableau pour chacune des neuf familles (titre « ## B.1 Coopération internationale et
multilatérale », « ## B.2 Coopération bilatérale et instituts culturels », « ## B.3 Fondations »,
« ## B.4 Fonds nationaux et régionaux », « ## B.5 Banques, microfinance, investisseurs »,
« ## B.6 Crowdfunding », « ## B.7 Incubateurs et accélérateurs », « ## B.8 Coproductions,
diffuseurs, acheteurs », « ## B.9 Résidences, bourses, prix »). Une ligne par bailleur.

```markdown
## B.<n> <Famille>

| Bailleur | Programme | Ce qu'il finance (et attention genre/inclusion) | Type de bénéficiaire exigé | Fourchette indicative | Cofinancement exigé | Calendrier type | Langue du dossier | Verdict + pourquoi | Source officielle à consulter | Action suivante |
|---|---|---|---|---|---|---|---|---|---|---|
| <nom> | <nom du programme ou « programme général »> | <objets financés ; priorités genre/jeunes/inclusion si connues> | <personne physique / association / entreprise / consortium> | [À VÉRIFIER — source : site officiel] | [À VÉRIFIER — source : site officiel] | [À VÉRIFIER — source : site officiel] | <FR / EN / FR ou EN> | <Éligible / Non éligible / À vérifier> — <raison en une phrase> | site officiel : <domaine> ; page consultée le AAAA-MM-JJ : <URL réellement ouverte ou « non consultée »> | <lancer veille / préparer matching / chercher structure porteuse / écarter> |
```

### Gabarit C — Top 5 prioritaire et plan de financement combiné

```markdown
## C. Top 5 prioritaire

| Rang | Bailleur / source | Pourquoi en priorité (adéquation, accessibilité, calendrier) | Montant visé auprès de cette source | Conditions à remplir avant de candidater | Skill /icc: suivant |
|---|---|---|---|---|---|
| 1 | <nom> | <raison> | <montant> FCFA (≈ <montant> EUR) | <statut, pièces, cofinancement> | /icc:matching-appel |
| 2 | <nom> | <raison> | <montant> | <conditions> | <skill> |
| 3 | <nom> | <raison> | <montant> | <conditions> | <skill> |
| 4 | <nom> | <raison> | <montant> | <conditions> | <skill> |
| 5 | <source propre : billetterie, pré-vente, crowdfunding, prestations> | <raison> | <montant> | <conditions> | /icc:crowdfunding ou /icc:budget-cofinancement |

### Plan de financement combiné (hypothèse de travail)
| Source | Montant visé (FCFA) | Montant visé (EUR) | % du budget | Statut (acquis / demandé / à solliciter / hypothèse) |
|---|---|---|---|---|
| <source 1> | | | | |
| <source 2> | | | | |
| Apport propre (numéraire + nature) | | | | |
| **Total** | | | 100 % | |
```

### Gabarit D — Procédure de veille

```markdown
## D. Veille à mener

| Bailleur | Requête à lancer (WebSearch ou moteur de recherche du téléphone) | Page officielle à ouvrir | Fréquence | Dernière vérification | Résultat |
|---|---|---|---|---|---|
| <nom> | "<nom>" appel à projets <année> culture | site officiel : <domaine> | mensuelle | AAAA-MM-JJ ou « jamais » | <appel ouvert / fermé / rien trouvé> |

Autres canaux à suivre : newsletter de l'Institut français du pays ; page « appels à propositions »
de la délégation de l'Union européenne ; groupes professionnels locaux (WhatsApp, Facebook) du
secteur ; réseaux et marchés professionnels du secteur ; ministère de la culture (fonds nationaux).
Hors ligne : relire cette liste, préparer les pièces génériques (CV, portfolio, statuts), noter les
questions à poser aux bailleurs.
```

### Gabarit E — Professionnels requis et alertes

```markdown
## E. Professionnels humains requis et alertes

| Besoin | Professionnel | Pourquoi indispensable | Urgence |
|---|---|---|---|
| <ex. : créer une association / une SARL> | <notaire, greffe, avocat selon le pays> | <la plupart des bailleurs exigent une personne morale et un compte bancaire dédié> | <avant toute candidature> |
| <ex. : états financiers certifiés> | expert-comptable (commissaire aux comptes si comptes audités exigés) | <pièce exigée par les bailleurs institutionnels> | <selon appel> |
| <ex. : convention de portage> | avocat ou juriste | <sécurise les flux financiers et la propriété du projet> | <avant signature> |

### Alertes
- <délais serrés, pièces manquantes, incohérences entre montant et stade, dépendance à une seule source>
```

### Exemple rempli (extrait) — scénario 1, documentaire au Tchad

```markdown
# Cartographie des bailleurs — « Les pêcheuses du lac » (documentaire 26 min)
Date : 2026-10-30 | Rédigé avec /icc:cartographie-bailleurs | Agent : icc-financements

## A. Profil de financement
| Axe | Valeur |
|---|---|
| Secteur ICC | Cinéma / audiovisuel — court-métrage documentaire (26 min) |
| Pays de résidence / pays du projet | Tchad / Tchad (lac Tchad) |
| Stade de maturité | Développement (synopsis et teaser 3 min disponibles ; pas de budget ; pas de producteur) |
| Montant total recherché | 16 400 000 FCFA (≈ 25 000 EUR) |
| Part déjà acquise ou apportée | 0 FCFA (apport en nature : matériel de tournage personnel, à chiffrer) |
| Type de structure | Sans statut — portage par une société de production existante à l'étude (/icc:statut-juridique) |
| Compte bancaire | Personnel — Tchad |
| Langues de dossier possibles | Français ; anglais avec aide à la traduction |
| Échéance de financement | Tournage souhaité en saison sèche, dans 10 à 14 mois |

### Atouts d'inclusion et d'impact social du projet
| Dimension | Ce que le projet fait concrètement | Preuve disponible |
|---|---|---|
| Genre | Réalisatrice ; sujet centré sur l'activité économique des femmes pêcheuses | Synopsis, teaser |
| Zones rurales | Tournage sur les rives du lac Tchad, hors capitale | Repérages (photos) |
| Langues nationales | Entretiens en langues locales, sous-titrés en français | Teaser |

## B.1 Coopération internationale et multilatérale (extrait)
| Bailleur | Programme | Ce qu'il finance | Type de bénéficiaire exigé | Fourchette indicative | Cofinancement exigé | Calendrier type | Langue | Verdict + pourquoi | Source officielle | Action suivante |
|---|---|---|---|---|---|---|---|---|---|---|
| OIF | Fonds Image de la Francophonie | Développement, production et finition d'œuvres cinématographiques et audiovisuelles de pays francophones du Sud ; documentaire inclus | Société de production (personne morale) établie dans un pays membre, en général | [À VÉRIFIER — source : site officiel] | [À VÉRIFIER — source : site officiel] | [À VÉRIFIER — source : site officiel ; sessions périodiques] | FR | À vérifier — le programme correspond au secteur et au pays, mais exige habituellement une société de production : nécessite le portage par un producteur | site officiel : francophonie.org ; page non consultée (hors ligne) | Trouver un producteur porteur, puis /icc:matching-appel dès l'appel ouvert |
| UNESCO | Fonds international pour la diversité culturelle (FIDC) | Projets structurants pour les politiques et industries culturelles ; rarement une œuvre isolée | ONG, institutions publiques, parfois micro-entreprises | [À VÉRIFIER — source : site officiel] | [À VÉRIFIER] | [À VÉRIFIER] | FR ou EN | Non éligible en l'état — finance des projets de structuration du secteur, pas un film unique ; contournable si le film s'inscrit dans un projet collectif de formation | site officiel : unesco.org | Écarter pour ce film ; noter pour un futur projet de formation |

## B.2 Coopération bilatérale et instituts culturels (extrait)
| Institut français (réseau au Tchad) | Dispositifs de soutien aux acteurs culturels locaux et à la mobilité | Événements, mobilité, parfois production locale | Artistes et structures du pays | [À VÉRIFIER] | [À VÉRIFIER] | [À VÉRIFIER] | FR | Éligible en principe — soutien aux artistes du pays, personnes physiques parfois acceptées ; montant probablement partiel | site officiel : institutfrancais.com et site de l'Institut français du Tchad | Prendre rendez-vous avec le chargé de mission culture ; /icc:matching-appel |
| Goethe-Institut (région Afrique centrale / de l'Ouest) | Programmes culture et coproduction | Projets culturels avec dimension de coopération, parfois cinéma | Variable | [À VÉRIFIER] | [À VÉRIFIER] | [À VÉRIFIER] | FR, EN ou DE | À vérifier — couverture du Tchad depuis quel institut régional à confirmer | site officiel : goethe.de | Veille : "Goethe-Institut appel à projets cinéma Afrique <année>" |

## C. Top 5 prioritaire
| Rang | Bailleur / source | Pourquoi | Montant visé | Conditions | Skill suivant |
|---|---|---|---|---|---|
| 1 | OIF — Fonds Image de la Francophonie | Cœur de cible secteur/pays ; référence pour un premier documentaire | 50 à 60 % du budget [hypothèse de travail] | Producteur porteur ; budget chiffré ; dossier artistique | /icc:statut-juridique puis /icc:matching-appel |
| 2 | Institut français (local) | Accessible, interlocuteur sur place, aide au développement | 10 à 15 % [hypothèse] | Dossier court, rendez-vous | /icc:matching-appel |
| 3 | Fonds d'appui culturel d'une ambassade (France, Allemagne, UE) | Petits montants, procédure légère | 10 % [hypothèse] | Statut ou portage | veille puis matching |
| 4 | Fonds documentaires et festivals (marchés de coproduction africains) | Visibilité, coproduction, pré-achat | variable | Teaser, dossier EN | veille |
| 5 | Apport propre + pré-vente de diffusion locale + crowdfunding diaspora | Réduit la dépendance aux subventions | 10 à 15 % | Plan de campagne | /icc:crowdfunding |

## E. Professionnels requis
| Besoin | Professionnel | Pourquoi | Urgence |
|---|---|---|---|
| Convention de portage avec une société de production | Avocat ou juriste | Fixer la répartition des droits, la gestion des fonds et la rémunération de la réalisatrice | Avant toute candidature au nom du producteur |
| Budget prévisionnel au format du bailleur | Expert-comptable (relecture) ou directeur de production expérimenté | Les fonds cinéma exigent un devis détaillé normé | Avant dépôt |
```

## Critères de qualité du livrable

Avant d'enregistrer `projet/financements/cartographie.md`, vérifier chaque point :

| Critère | Vérification |
|---|---|
| Couverture | Les neuf familles ont été examinées ; les familles sans bailleur pertinent portent la mention « aucune source pertinente identifiée — pourquoi ». |
| Verdicts explicites | Chaque ligne a un verdict (éligible / non éligible / à vérifier) ET une raison en une phrase. Aucun verdict sans raison. |
| Aucun chiffre inventé | Tout montant, date, taux ou critère chiffré porte « [À VÉRIFIER — source : …] » ou cite un document fourni par le promoteur. |
| URL honnêtes | Seuls figurent des domaines officiels, ou des URL effectivement ouvertes pendant la session (avec date de consultation). |
| Double devise | Tous les montants sont en FCFA et en euros (ou devise du bailleur), parité 1 EUR = 655,957 FCFA. |
| Diversification | Le top 5 contient au moins une source non concurrentielle (recettes propres, pré-vente, crowdfunding). |
| Inclusion | Le gabarit A comporte la rubrique genre/inclusion/impact remplie avec des faits, pas des intentions vagues. |
| Professionnels | Le gabarit E nomme les professionnels requis et pourquoi. |
| Actions | Chaque ligne du top 5 renvoie à un skill `/icc:` ou à une action concrète datée. |
| Reprenable | `projet/ETAT.md` est à jour, avec l'étape atteinte et les requêtes de veille restantes. |
| Lisibilité | Termes techniques expliqués à la première occurrence ; vouvoiement ; pas d'emoji ; pas de promesse de résultat. |

## Erreurs fréquentes à éviter

- Recopier des montants ou des dates limites de mémoire : les programmes changent chaque année ;
  toujours marquer [À VÉRIFIER] et renvoyer au site officiel.
- Inventer une URL profonde (page précise d'un appel) : n'indiquer que le domaine officiel tant
  que la page n'a pas été ouverte.
- Déclarer « éligible » un promoteur sans statut auprès d'un bailleur qui finance des personnes
  morales : c'est « non éligible en l'état, contournable par portage ». Le dire clairement.
- Proposer un bailleur dont le programme concerne la structuration du secteur (politiques
  culturelles, formation) pour financer une œuvre unique, ou l'inverse.
- Oublier les sources propres (billetterie, ventes, prestations, pré-commandes) et construire un
  plan reposant à 100 % sur des subventions.
- Oublier la question du compte bancaire et du pays du compte : de nombreux bailleurs et toutes les
  plateformes de crowdfunding en dépendent.
- Mélanger la fourchette du bailleur et le besoin du projet : un fonds qui accorde de petites aides
  ne couvrira pas un budget de festival de 60 000 EUR ; l'indiquer et prévoir un montage combiné.
- Présenter l'inclusion comme un slogan : le bailleur lit des faits (qui, combien, où, comment).
- Faire la cartographie avant la fiche-projet : sans secteur, pays, stade et montant, le tableau
  est inutilisable.
- Oublier de mettre à jour `projet/ETAT.md` : en cas de coupure, tout le travail de tri est perdu.

## Références et sources à vérifier

- `references/bailleurs.md` (ce skill) : annuaire structuré des bailleurs avec domaine officiel,
  zone, secteurs, bénéficiaires habituels, logique de programme. Aucun montant ni date : tout est
  à vérifier sur le site officiel.
- Sites officiels (domaines seulement ; pages précises à ouvrir pendant la veille) : OIF
  (francophonie.org), Union européenne (europa.eu et site de la délégation locale), AFD (afd.fr),
  GIZ (giz.de), UNESCO (unesco.org), Africalia (africalia.be), Institut français
  (institutfrancais.com), British Council (britishcouncil.org), Goethe-Institut (goethe.de),
  Wallonie-Bruxelles International (wbi.be), Prince Claus Fund (princeclausfund.org), Ford
  Foundation (fordfoundation.org), Fondation Doen (doen.nl), Afrique Créative (afriquecreative.fr),
  Fondation Orange (fondationorange.com), Open Society Foundations (opensocietyfoundations.org),
  BAD (afdb.org), Banque mondiale (worldbank.org), CEDEAO (ecowas.int), Union africaine (au.int).
- Fonds nationaux : ministère de la culture du pays du promoteur ; FOPICA (Sénégal), FONSIC
  (Côte d'Ivoire) — existence, statut et modalités à vérifier auprès des sites officiels.
- Si WebSearch est disponible : lancer la recherche « <nom du bailleur> appel à projets <année> »
  et consulter la page officielle avant toute inscription de chiffre.
- Documents fournis par le promoteur : lignes directrices d'appels, courriers de bailleurs,
  conventions antérieures — ils priment sur toute connaissance générale.

## Passage de relais

Après la cartographie, l'ordre recommandé est :
1. Si le verdict d'un bailleur prioritaire dépend du statut : `/icc:statut-juridique` (agent
   `icc-juridique`) pour choisir entre création d'une structure et portage.
2. Dès qu'un appel précis est identifié ou ouvert : `/icc:matching-appel` (agent
   `icc-financements`) pour la grille d'éligibilité, le score et la décision GO / NO-GO.
3. Pour chiffrer le plan de financement combiné et le cofinancement : `/icc:budget-cofinancement`
   (agent `icc-budget`).
4. Pour la source participative du top 5 : `/icc:crowdfunding` (agent `icc-communication`).
5. Pour le dossier de candidature : `/icc:note-conceptuelle` (agent `icc-redaction`).

Mise à jour obligatoire de `projet/ETAT.md` (créer le fichier avec la structure imposée s'il
n'existe pas) :
- « Dernière mise à jour » : date et heure ; « Agent actif : icc-financements | Skill en cours :
  /icc:cartographie-bailleurs » (ou le skill suivant si le relais est immédiat) ;
- « Étapes terminées » : ajouter « Cartographie des bailleurs — projet/financements/cartographie.md
  (familles examinées : …, top 5 : …) » ;
- « Étape en cours » : si la veille (étape 5) n'est pas terminée, indiquer précisément les
  bailleurs restant à vérifier ;
- « Prochaines étapes » : la liste numérotée ci-dessus adaptée au projet ;
- « Décisions prises / hypothèses à confirmer » : hypothèses de répartition du plan de financement,
  choix de portage ;
- « Questions en attente de réponse du promoteur » : questions des sections ci-dessus restées sans
  réponse ;
- « Alertes » : contenu du gabarit E (professionnels requis), délais courts, pièces manquantes,
  dépendance à une seule source.
