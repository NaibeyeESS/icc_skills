# Plugin `icc` — Industries Culturelles et Créatives

Agents et skills Claude Code, en français, pour accompagner les promoteurs de projets culturels
et créatifs (musique, cinéma et audiovisuel, arts visuels, mode et design, édition, jeux vidéo,
arts du spectacle, artisanat d'art, patrimoine, médias et contenus numériques) sur deux fronts :

1. **Trouver et obtenir des financements** — subventions, appels à projets, prêts, mécénat,
   crowdfunding, investisseurs, coproductions, résidences, bourses.
2. **Mettre en œuvre le projet** — structuration juridique, planification, budget et trésorerie,
   suivi-évaluation, communication, reporting aux bailleurs.

Conçu d'abord pour l'Afrique francophone (Tchad, Afrique centrale et de l'Ouest), adaptable à
d'autres zones. Pensé pour des promoteurs de tous niveaux, y compris sans expérience
administrative, et pour une connectivité irrégulière : chaque étape écrit ses livrables dans des
fichiers et résume son état dans `projet/ETAT.md` pour permettre la reprise.

## Installation

Le plugin est un dossier contenant `.claude-plugin/plugin.json`, `agents/`, `commands/` et
`skills/`.

```bash
# Depuis le répertoire de travail du promoteur, à chaque nouvelle séance
claude --plugin-dir /chemin/vers/icc
```

`--plugin-dir` charge le plugin pour la session en cours uniquement. Ensuite, dans la session :

```
/icc:demarrer
```

Pour vérifier le plugin après une modification : `claude plugin validate /chemin/vers/icc`.

Un guide pour débutantes, destiné aux participantes du Labo Ngousso, se trouve dans
[docs/guide-labo-ngousso.html](docs/guide-labo-ngousso.html).

Le promoteur travaille dans le répertoire courant ; tous les livrables sont écrits dans un
sous-dossier `projet/` (créé à la demande).

Aucune dépendance externe : les deux scripts de calcul (`budget.py`, `tresorerie.py`) n'utilisent
que la bibliothèque standard Python 3 et se lancent avec `python3 -I`.

## Parcours type

```
/icc:demarrer
   │
   ▼
icc-orchestrateur ── accueil, 10 questions max, crée projet/ETAT.md, rend un ROUTAGE RECOMMANDÉ
   │
   ▼
icc-diagnostic ───── /icc:fiche-projet → projet/fiche-projet.md (document pivot)
   │
   ├─ pas de personne morale ? ──► icc-juridique ── /icc:statut-juridique, /icc:propriete-intellectuelle
   │
   ▼
icc-financements ─── /icc:cartographie-bailleurs → projet/financements/cartographie.md
                     /icc:matching-appel        → projet/financements/matching-<appel>.md  (GO / NO-GO)
   │
   ▼
icc-budget ───────── /icc:budget-cofinancement → projet/budget/budget.md + budget.csv
                     /icc:plan-tresorerie      → projet/budget/tresorerie.md + tresorerie.csv
   │
   ▼
icc-redaction ────── /icc:note-conceptuelle    → projet/dossiers/<bailleur>/…
                     /icc:reecriture-humanisee → …/note-conceptuelle.v2.md
   │
   ├─► icc-communication ── /icc:pitch-dossier-presse, /icc:crowdfunding → projet/communication/…
   │
   ▼  (financement obtenu)
icc-mise-en-oeuvre ─ /icc:plan-mise-en-oeuvre → projet/mise-en-oeuvre/plan.md
                     /icc:suivi-evaluation    → projet/mise-en-oeuvre/suivi-evaluation.md

À tout moment :  /icc:reprendre  (relit projet/ETAT.md et repart de l'étape en cours)
```

L'ordre n'est pas rigide : l'orchestrateur adapte le parcours (urgence d'une date limite, statut
déjà existant, budget déjà fait…). Un promoteur peut aussi appeler directement un skill
(`/icc:budget-cofinancement`) ou demander un agent par son nom.

## Commandes

| Commande | Rôle |
|---|---|
| `/icc:demarrer [message]` | Démarre l'accompagnement : délègue à `icc-orchestrateur`, puis exécute son routage |
| `/icc:reprendre [nouveautés]` | Reprend à partir de `projet/ETAT.md` sans refaire le diagnostic |

## Agents (`agents/icc-<nom>.md`)

| Agent | Rôle | Skills principaux |
|---|---|---|
| `icc-orchestrateur` | accueil, diagnostic rapide, routage, suivi global, reprise de session | (lit `projet/ETAT.md`) |
| `icc-diagnostic` | maturité du projet, profil du promoteur, forces/faiblesses, fiche-projet standard | `/icc:fiche-projet` |
| `icc-financements` | veille, matching secteur/pays/stade/montant, classement par éligibilité et probabilité | `/icc:cartographie-bailleurs`, `/icc:matching-appel`, `/icc:crowdfunding` |
| `icc-redaction` | dossiers conformes à chaque bailleur (note conceptuelle, formulaires, lettres, CV, portfolio) | `/icc:note-conceptuelle`, `/icc:reecriture-humanisee` |
| `icc-budget` | budget, trésorerie, cofinancement, éligibilité des dépenses | `/icc:budget-cofinancement`, `/icc:plan-tresorerie` |
| `icc-mise-en-oeuvre` | plan d'action, chronogramme, indicateurs, risques, reporting bailleurs | `/icc:plan-mise-en-oeuvre`, `/icc:suivi-evaluation` |
| `icc-juridique` | statut (association/entreprise/coopérative), PI, contrats types, fiscalité de base | `/icc:statut-juridique`, `/icc:propriete-intellectuelle` |
| `icc-communication` | pitch, dossier de presse, présence en ligne, sponsors, crowdfunding | `/icc:pitch-dossier-presse`, `/icc:crowdfunding`, `/icc:reecriture-humanisee` |

Chaque agent sait résumer son état dans `projet/ETAT.md`, signale quand un professionnel humain
est indispensable (expert-comptable, avocat, notaire) et n'invente jamais un bailleur, un montant
ou une date limite : toute information non vérifiée est marquée `[À VÉRIFIER — source : …]`.

## Skills (`skills/<nom>/SKILL.md`, invoqués par `/icc:<nom>`)

| Skill | Objet | Livrable dans `projet/` |
|---|---|---|
| `cartographie-bailleurs` | panorama des bailleurs pertinents (secteur × pays × stade × montant × structure), procédure de veille ; annuaire `references/bailleurs.md` | `financements/cartographie.md` |
| `matching-appel` | analyse d'un appel précis : éligibilité point par point, score /100, pièces, rétro-planning, GO / NO-GO | `financements/matching-<appel>.md` |
| `fiche-projet` | fiche-projet standard, questionnaire progressif, grille de maturité | `fiche-projet.md` |
| `note-conceptuelle` | note conceptuelle au format du bailleur, cadre logique, lettres de soutien et de motivation, CV, portfolio ; annexe `references/rubriques-bailleurs.md` | `dossiers/<bailleur>/…` |
| `budget-cofinancement` | budget par rubriques, plan de financement, éligibilité des dépenses ; script `scripts/budget.py` | `budget/budget.md`, `budget/budget.csv` |
| `plan-tresorerie` | trésorerie mensuelle, tranches de versement, couverture des creux ; script `scripts/tresorerie.py` | `budget/tresorerie.md`, `budget/tresorerie.csv` |
| `plan-mise-en-oeuvre` | activités, chronogramme, RACI, risques, achats, reporting | `mise-en-oeuvre/plan.md` |
| `suivi-evaluation` | théorie du changement, indicateurs désagrégés, outils de collecte, rapport d'évaluation | `mise-en-oeuvre/suivi-evaluation.md` |
| `statut-juridique` | choix et création du statut (OHADA, associations), portage, fiscalité de base ; annexe `references/formes-juridiques-ohada.md` | `juridique/statut.md` |
| `propriete-intellectuelle` | droits d'auteur, marque et dessins/modèles (OAPI), gestion collective, contrats types, droit à l'image | `juridique/propriete-intellectuelle.md` |
| `pitch-dossier-presse` | pitch 30 s / 2 min / 7 min, one-pager, deck, dossier de presse, présence en ligne, sponsors | `communication/pitch.md`, `communication/dossier-presse.md` |
| `crowdfunding` | campagne de financement participatif adaptée au contexte (plateformes, Mobile Money, diaspora) | `communication/crowdfunding.md` |
| `reecriture-humanisee` | rendre un texte naturel et incarné sans changer les faits ni le format imposé | `<fichier>.v2.md` à côté de l'original |

## Arborescence produite chez le promoteur

```
projet/
├── ETAT.md                      ← état de session (reprise)
├── fiche-projet.md              ← document pivot
├── diagnostic.md
├── financements/
│   ├── cartographie.md
│   ├── matching-<appel>.md
│   └── veille.md
├── budget/
│   ├── budget.md  budget.csv
│   ├── tresorerie.md  tresorerie.csv
│   └── justificatifs.md
├── dossiers/<bailleur>/
│   ├── note-conceptuelle.md  note-conceptuelle.v2.md
│   ├── cadre-logique.md  lettre-motivation.md  cv-<nom>.md  portfolio.md
│   ├── lettres-soutien/
│   └── conformite.md
├── juridique/
│   ├── statut.md  statuts-association.md  pv-ag-constitutive.md  convention-portage.md
│   ├── propriete-intellectuelle.md
│   ├── contrats/
│   └── autorisations/
├── mise-en-oeuvre/
│   ├── plan.md  suivi-evaluation.md  tableau-de-bord.md
│   ├── rapports/
│   └── reunions/
└── communication/
    ├── pitch.md  dossier-presse.md  presence-en-ligne.md
    ├── partenaires-sponsors.md  crowdfunding.md  kit-visuels.md
```

## Règles transversales (appliquées par tous les agents et skills)

- Jamais de bailleur, d'appel, de montant ou de date limite inventés ; information non vérifiée
  marquée et accompagnée de l'endroit où la vérifier (WebSearch quand disponible).
- Toujours distinguer éligible / non éligible / à vérifier, et expliquer pourquoi.
- Niveau de langage adapté ; chaque terme technique expliqué à sa première apparition.
- Livrables directement utilisables (tableaux chiffrés, textes rédigés, calendriers datés),
  écrits dans `projet/`.
- Formats des bailleurs respectés (pages, rubriques, devises, langue) ; montants en FCFA et dans
  la devise du bailleur (parité fixe 1 EUR = 655,957 FCFA).
- Genre, inclusion et impact social intégrés dans chaque gabarit pertinent, sans plaquage.
- Mode faible connectivité : `projet/ETAT.md` mis à jour à chaque étape.
- Signalement explicite des cas où un professionnel humain est indispensable.

## Scénarios de validation

### Scénario 1 — Réalisatrice tchadienne, documentaire, 25 000 €, sans structure

**Situation.** Réalisatrice à N'Djamena, synopsis et teaser de 3 min prêts, pas de budget, pas de
producteur, pas de structure juridique. Cherche 25 000 € (≈ 16,4 M FCFA) pour un documentaire de
26 min sur les femmes pêcheuses du lac Tchad.

| Étape | Agent | Skills chargés | Fichiers produits |
|---|---|---|---|
| 1 | `icc-orchestrateur` | — | `projet/ETAT.md` (mode faible connectivité activé), routage → diagnostic |
| 2 | `icc-diagnostic` | `/icc:fiche-projet` | `projet/fiche-projet.md` (maturité : 3 — prototype, grâce au teaser), `projet/diagnostic.md` (faiblesse n° 1 : pas de personne morale) |
| 3 | `icc-juridique` | `/icc:statut-juridique` | `projet/juridique/statut.md` : comparaison association vs portage par une société de production existante ; recommandation : portage immédiat pour les appels proches + création d'association en parallèle ; `convention-portage.md` ; alerte « avocat pour le contrat de coproduction » |
| 4 | `icc-financements` | `/icc:cartographie-bailleurs`, `/icc:matching-appel` | `cartographie.md` (OIF/Fonds Image de la Francophonie, Institut français local, Goethe-Institut, fonds documentaire des festivals, ambassades — tout marqué à vérifier), `matching-<appel>.md` pour l'appel le plus proche, GO SOUS CONDITIONS (portage signé, budget bouclé) |
| 5 | `icc-budget` | `/icc:budget-cofinancement`, `/icc:plan-tresorerie` | `budget.md`/`budget.csv` (développement / tournage / post-production / diffusion ; 16,4 M FCFA ; cofinancement : apport en nature + partenaire TV locale), `tresorerie.md` (creux au tournage → acompte négocié) |
| 6 | `icc-redaction` | `/icc:note-conceptuelle`, `/icc:reecriture-humanisee` | `dossiers/<bailleur>/note-conceptuelle.md` + `.v2.md`, `lettre-motivation.md`, `lettres-soutien/structure-porteuse.md`, `cv-realisatrice.md`, `conformite.md` |
| 7 | `icc-juridique` (retour) | `/icc:propriete-intellectuelle` | `autorisations/droit-image-*.md` (femmes filmées, communauté), `contrats/coproduction-*.md` (projet, à faire valider par un avocat) |
| 8 | `icc-communication` | `/icc:pitch-dossier-presse` | `communication/pitch.md` (pitch 2 min pour un forum de coproduction) |

**Critères de réussite.** Aucun montant de bailleur affirmé sans « à vérifier » ; budget bouclé
en FCFA et EUR ; note conceptuelle conforme au nombre de pages de l'appel ; `ETAT.md` permet de
reprendre après coupure à n'importe quelle étape ; besoin d'avocat signalé pour la coproduction.

### Scénario 2 — Collectif de musiciens, festival annuel, financement pluriannuel

**Situation.** Association déclarée depuis deux ans (Afrique centrale), 12 musiciens. Festival de
3 jours, 5 000 spectateurs visés, trois éditions à financer (~60 000 € la première).

| Étape | Agent | Skills chargés | Fichiers produits |
|---|---|---|---|
| 1 | `icc-orchestrateur` | — | `ETAT.md`, routage → diagnostic (structure OK, donc pas de détour juridique initial) |
| 2 | `icc-diagnostic` | `/icc:fiche-projet` | `fiche-projet.md` (maturité : 4 — en cours), `diagnostic.md` (force : association existante avec comptes ; faiblesse : aucun rapport bailleur déjà rendu) |
| 3 | `icc-financements` | `/icc:cartographie-bailleurs`, `/icc:matching-appel` | `cartographie.md` multi-sources pluriannuel (UE/ACP Culture, Africalia, ambassades, Institut français, sponsors privés télécoms/brasseries, billetterie), `matching-acp-ue.md` (score 71/100, GO SOUS CONDITIONS : partenaire co-demandeur, audit) |
| 4 | `icc-budget` | `/icc:budget-cofinancement`, `/icc:plan-tresorerie` | `budget.md` pluriannuel 3 éditions (programmation / technique / sécurité / billetterie / communication), plan de financement avec % par source, `tresorerie.md` saisonnière (pic J-60 à J+15, tranches bailleur décalées → relais sponsors et pré-ventes) |
| 5 | `icc-mise-en-oeuvre` | `/icc:plan-mise-en-oeuvre`, `/icc:suivi-evaluation` | `plan.md` (rétro-planning J-365 → J+30, RACI, registre des risques : pluies, sécurité, désistement d'artiste), `suivi-evaluation.md` (indicateurs : spectateurs ventilés F/H/jeunes, artistes femmes programmées, revenus des artistes, emplois temporaires) |
| 6 | `icc-juridique` | `/icc:propriete-intellectuelle` | `contrats/engagement-artiste.md`, captation et droit à l'image, note sur la société de gestion collective nationale et les assurances (à vérifier localement) |
| 7 | `icc-redaction` | `/icc:note-conceptuelle`, `/icc:reecriture-humanisee` | `dossiers/acp-ue/note-conceptuelle.md` + `.v2.md`, `cadre-logique.md`, `lettres-soutien/` (mairie, partenaire européen) |
| 8 | `icc-communication` | `/icc:pitch-dossier-presse`, `/icc:crowdfunding` | `dossier-presse.md`, `partenaires-sponsors.md` (paliers de sponsoring chiffrés depuis le budget), `crowdfunding.md` (pré-vente de pass, diaspora) |

**Critères de réussite.** Cohérence montant fiche-projet = budget = note ; chronogramme compatible
avec la trésorerie ; 5 à 10 indicateurs maximum, tous désagrégés ; expert-comptable signalé pour
l'audit exigé par le bailleur.

### Scénario 3 — Créatrice de mode, de l'atelier informel à une marque exportable

**Situation.** Atelier informel, 3 couturières (Afrique de l'Ouest). Objectif : collection,
e-commerce, salons internationaux.

| Étape | Agent | Skills chargés | Fichiers produits |
|---|---|---|---|
| 1 | `icc-orchestrateur` | — | `ETAT.md`, routage → diagnostic puis juridique en priorité (export impossible sans structure ni marque) |
| 2 | `icc-diagnostic` | `/icc:fiche-projet` | `fiche-projet.md` (maturité : 3 — pilote ; chiffre d'affaires informel estimé), `diagnostic.md` (atout : production existante ; faiblesses : pas de statut, pas de marque déposée, pas de comptabilité) |
| 3 | `icc-juridique` | `/icc:statut-juridique`, `/icc:propriete-intellectuelle` | `statut.md` (grille : EI/entreprenant vs SARLU vs coopérative ; recommandation argumentée selon l'objectif d'investisseurs), `propriete-intellectuelle.md` (dépôt de marque OAPI, classes de Nice concernées, dessins et modèles, registre des créations), alertes notaire/expert-comptable |
| 4 | `icc-financements` | `/icc:cartographie-bailleurs`, `/icc:matching-appel` | `cartographie.md` (Afrique Créative, Fondation Orange, incubateurs, microfinance, prêts d'honneur, crowdfunding pré-vente — tout à vérifier), `matching-<programme>.md` |
| 5 | `icc-budget` | `/icc:budget-cofinancement`, `/icc:plan-tresorerie` | `budget.md` (matières / production / shooting / salons / e-commerce), `tresorerie.md` 12 mois avec besoin en fonds de roulement expliqué |
| 6 | `icc-mise-en-oeuvre` | `/icc:plan-mise-en-oeuvre`, `/icc:suivi-evaluation` | `plan.md` (collection → shooting → boutique en ligne → premier salon), `suivi-evaluation.md` (ventes, pays touchés, emplois féminins créés, revenus des couturières) |
| 7 | `icc-communication` | `/icc:pitch-dossier-presse`, `/icc:crowdfunding`, `/icc:reecriture-humanisee` | `pitch.md` (pitch investisseur 7 min + deck 10 diapos), `dossier-presse.md` (communiqué de lancement, lookbook), `crowdfunding.md` (pré-commandes, contreparties chiffrées avec coût d'envoi) |
| 8 | `icc-redaction` | `/icc:note-conceptuelle` | `dossiers/<programme>/formulaire-reponses.md` (réponses au formulaire en ligne avec compteur de caractères) |

**Critères de réussite.** Statut recommandé avec justification et professionnels à consulter ;
marque et créations inscrites dans un registre avec démarches datées ; objectif de crowdfunding
fixé par la méthode des cercles et non par le besoin ; trésorerie sans mois négatif non couvert.

## Limites et avertissements

- Les agents fournissent une information juridique, financière et administrative générale et
  des gabarits de travail ; ils ne remplacent ni un avocat, ni un notaire, ni un expert-comptable,
  et le disent.
- Les annuaires de bailleurs (`skills/cartographie-bailleurs/references/bailleurs.md`,
  `skills/note-conceptuelle/references/rubriques-bailleurs.md`) décrivent des logiques générales :
  montants, dates et critères doivent être vérifiés sur les sites officiels avant tout dépôt.
- Les gabarits de statuts et de contrats sont des projets à adapter au droit national et à faire
  valider.

## Adapter le plugin

Les skills sont rédigés en Markdown et modifiables : pour adapter le plugin à un autre pays ou
secteur, commencez par `skills/cartographie-bailleurs/references/bailleurs.md` et
`skills/statut-juridique/references/formes-juridiques-ohada.md`.
