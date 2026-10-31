---
name: budget-cofinancement
description: Utiliser quand le promoteur doit chiffrer son projet : budget prévisionnel, plan de financement ou cofinancement, apport propre, valorisation en nature, frais indirects, éligibilité des dépenses, conversion FCFA/EUR ; mots-clés : « combien ça coûte », « devis », « montant à demander », « contrepartie ».
---

# /icc:budget-cofinancement — Budget prévisionnel et plan de cofinancement

## Objectif

Produire, avec le promoteur, un budget prévisionnel complet, crédible et conforme aux règles du
bailleur visé, accompagné d'un plan de cofinancement multi-sources. Livrables :

- `projet/budget/budget.md` — budget détaillé, plan de financement, grille d'éligibilité,
  hypothèses de chiffrage, pièces justificatives attendues ;
- `projet/budget/budget.csv` — les lignes budgétaires dans le format lu par le script
  `scripts/budget.py`, qui calcule sous-totaux, parts par source, taux de cofinancement,
  conversions et alertes.

Agent principal : `icc-budget`. Ce skill ne traite pas la trésorerie dans le temps (voir
`/icc:plan-tresorerie`) ni la rédaction narrative du dossier (voir `/icc:note-conceptuelle`).

Termes expliqués à leur première apparition dans ce skill ; les gabarits reprennent ces
définitions en note de bas de tableau pour que le promoteur puisse les copier tels quels.

## Quand l'utiliser / ne pas l'utiliser

Utiliser quand :
- le promoteur n'a pas de budget chiffré ou seulement un montant global (« je cherche 25 000 € ») ;
- un appel à projets exige un budget dans un format donné (tableau Excel du bailleur, rubriques
  imposées, plafonds par rubrique, devise du bailleur) ;
- il faut démontrer un cofinancement (= part du budget que le bailleur exige que vous apportiez
  vous-même ou via d'autres sources) ou valoriser des apports en nature ;
- il faut vérifier quelles dépenses sont éligibles (= acceptées et remboursables par le bailleur)
  avant de déposer ;
- un budget existe mais paraît irréaliste, incomplet ou incohérent avec le narratif.

Ne pas l'utiliser pour :
- le plan de trésorerie mois par mois (encaissements/décaissements dans le temps) : `/icc:plan-tresorerie` ;
- le choix des bailleurs : `/icc:cartographie-bailleurs` et `/icc:matching-appel` ;
- un plan d'affaires complet sur plusieurs années avec compte de résultat prévisionnel : ce skill
  en pose la base (budget de la première année) mais un expert-comptable doit valider les états
  financiers prévisionnels destinés à une banque ou un investisseur.

## Prérequis

Lire si présents (ne pas reposer les questions auxquelles ils répondent) :
- `projet/ETAT.md` — reprendre là où la session précédente s'est arrêtée ;
- `projet/fiche-projet.md` — secteur, durée, lieu, équipe, montant visé, statut juridique ;
- `projet/financements/matching-<slug-appel>.md` — bailleur visé, plafond, taux de
  cofinancement exigé, rubriques imposées, dépenses inéligibles ;
- `projet/juridique/statut.md` — la structure porteuse (association, entreprise, portage par un
  tiers) détermine qui facture, qui encaisse et quelles charges sociales s'appliquent ;
- les lignes directrices de l'appel (PDF ou texte fourni par le promoteur) : elles priment sur les
  gabarits de ce skill.

Informations nécessaires si absentes : secteur et type de projet, durée (mois), lieux
d'exécution, taille de l'équipe, montant visé et bailleur(s) pressenti(s), ressources déjà
acquises (matériel, locaux, bénévoles, partenaires), recettes propres envisagées (billetterie,
ventes, prestations).

Outil : `python3 -I skills/budget-cofinancement/scripts/budget.py projet/budget/budget.csv`
(bibliothèque standard uniquement ; options `--eur`, `--usd`, `--plafond "Rubrique=PCT"`,
`--total-attendu`, `--cofinancement-min`, `--bailleur`). Faisable hors ligne.

## Procédure étape par étape

1. **Cadrer.** Lire `projet/ETAT.md` et `projet/fiche-projet.md`. Confirmer en une phrase le
   périmètre budgété (quelle édition, quelle phase, quelle durée) et la devise du bailleur. Noter
   le taux de change utilisé : parité fixe 1 EUR = 655,957 FCFA (XAF et XOF) ; pour l'USD ou
   la GBP, demander le taux du jour et le dater dans le document.
2. **Lire les règles du bailleur.** Demander les lignes directrices de l'appel. En extraire :
   rubriques imposées, plafond du financement, taux de cofinancement minimal, plafond des frais
   indirects, dépenses inéligibles, format attendu (tableau du bailleur, nombre de colonnes,
   arrondis), pièces justificatives exigées. Tout chiffre non lu dans un document officiel est
   marqué « [À VÉRIFIER — source : site officiel du bailleur] ». Si WebSearch est disponible,
   proposer la recherche « <nom bailleur> lignes directrices <année> budget éligibilité ».
3. **Choisir la structure budgétaire.** Partir du gabarit (a) et l'adapter au secteur via les
   sous-rubriques spécifiques ; si le bailleur impose ses rubriques, reprendre exactement les
   siennes et placer les nôtres en sous-lignes. Expliquer au promoteur pourquoi chaque rubrique
   existe.
4. **Lister les activités puis les dépenses.** Partir du plan d'activités (ou du narratif) :
   chaque activité génère des lignes de dépenses. Pour chaque ligne : unité, quantité, coût
   unitaire. Ne jamais saisir un forfait sans l'avoir décomposé au moins une fois à l'oral avec le
   promoteur (« 500 000 FCFA de communication » devient « 2 000 affiches x 150 + 10 spots radio
   x 25 000 + … »).
5. **Chiffrer avec des sources de prix** (gabarit e). Pour chaque coût unitaire, noter l'origine :
   devis reçu, barème d'usage du secteur local, prix constaté, estimation. Les lignes « estimation »
   sont à consolider par un devis avant dépôt. Inclure systématiquement : cachets et rémunérations
   déclarés (avec charges si la structure en a), frais d'accessibilité et d'inclusion (interprétation
   en langues nationales, accessibilité handicap, garde d'enfants pour les participantes si
   pertinent), suivi-évaluation, communication, frais administratifs, imprévus (5–10 % selon ce que
   le bailleur accepte — [À VÉRIFIER]).
6. **Affecter une source de financement à chaque ligne** (bailleur principal, cofinanceur,
   apport propre, valorisation en nature, recettes propres) avec un statut : acquis / demandé /
   à chercher. Respecter la logique du bailleur : certaines dépenses inéligibles pour lui doivent
   être portées par une autre source.
7. **Contrôler l'éligibilité** ligne par ligne (gabarit d) : oui / non / à vérifier, avec la raison.
8. **Écrire le CSV** (`projet/budget/budget.csv`, format gabarit f) et exécuter le script :
   `python3 -I skills/budget-cofinancement/scripts/budget.py projet/budget/budget.csv
   --total-attendu <montant> --cofinancement-min <taux exigé> --plafond "Frais administratifs=<PCT>"`.
   Lire les alertes (lignes sans source, plafonds dépassés, justificatifs manquants) et corriger.
   Coller le rapport Markdown produit dans `projet/budget/budget.md`.
9. **Construire le plan de financement** (gabarit c) et vérifier : total des sources = total des
   dépenses ; le taux de cofinancement atteint celui exigé ; la valorisation en nature n'excède pas
   ce que le bailleur accepte [À VÉRIFIER] ; les recettes propres sont prudentes (scénario bas).
10. **Rédiger les hypothèses et notes budgétaires** : une ligne d'explication par rubrique (le
    bailleur lit ces notes), la méthode de valorisation, le traitement de la TVA (récupérable ou
    non selon le statut — question pour l'expert-comptable), le taux de change daté.
11. **Relire avec le promoteur** à voix haute la cohérence narratif / budget / chronogramme :
    chaque activité du narratif a ses lignes ; chaque ligne budgétaire correspond à une activité.
12. **Signaler les professionnels requis** : expert-comptable pour états financiers certifiés,
    attestation de bonne gestion, bilan exigé par le bailleur ; commissaire aux comptes ou audit
    externe si le bailleur l'exige au-delà d'un seuil [À VÉRIFIER — fréquent pour l'UE et les
    conventions pluriannuelles] ; fiscaliste si retenues à la source sur cachets d'artistes
    étrangers.
13. **Mettre à jour `projet/ETAT.md`** (voir « Passage de relais »).

Mode faible connectivité : les étapes 3 à 10 se font entièrement hors ligne ; sauvegarder le CSV
après chaque rubrique terminée et noter dans `projet/ETAT.md` la dernière rubrique chiffrée.

## Questions à poser au promoteur

Poser uniquement celles sans réponse dans `projet/fiche-projet.md` ; une à trois questions à la
fois, en vouvoyant.

1. Quelle période exacte budgétons-nous (dates de début et de fin, nombre de mois) ?
2. Quel bailleur principal visez-vous, et avez-vous le document des lignes directrices ?
3. Avez-vous déjà des devis, des factures d'un projet précédent ou des barèmes du secteur ?
4. Qui travaille sur le projet, à quel rythme (jours), et à quel tarif local d'usage ? Ces personnes
   seront-elles payées en cachet, en salaire ou en prestation facturée ?
5. Que possédez-vous déjà (matériel, local, véhicule, bénévoles) que l'on peut valoriser ?
6. Quelles recettes propres attendez-vous (billets, ventes, prestations) et sur quelle base ?
7. Quels partenaires ont déjà promis quelque chose, par écrit ou oralement ?
8. Quelles dépenses d'inclusion prévoyez-vous (interprétation en langues nationales, accès des
   personnes handicapées, participation des femmes et des jeunes des zones rurales) ?
9. Votre structure est-elle assujettie à la TVA ? Tenez-vous une comptabilité ? Avez-vous un
   compte bancaire au nom de la structure ?
10. Quel niveau d'imprévus acceptez-vous de ne pas dépenser (il est souvent plafonné) ?

## Gabarits complets

Chaque gabarit est copiable dans `projet/budget/budget.md`. Remplacer les crochets.

### (a) Structure budgétaire type ICC et sous-rubriques sectorielles

| Code | Rubrique | Contenu habituel | Repère de poids (indicatif, à adapter) |
|---|---|---|---|
| RH | Ressources humaines et cachets | salaires, cachets artistes et techniciens, honoraires, per diem liés au personnel, charges sociales le cas échéant | 30–50 % |
| EQ | Équipement et location de matériel | achat (souvent plafonné ou inéligible), location, consommables techniques | 5–20 % |
| PR | Production / création | coûts directs de l'œuvre ou de l'événement : matières, droits, décors, prestataires artistiques | 10–30 % |
| LO | Logistique et déplacements | transports, hébergement, restauration, visas, assurances voyage | 5–15 % |
| CO | Communication et diffusion | identité visuelle, impression, médias, réseaux, sous-titrage, distribution, inscriptions festivals | 5–15 % |
| IN | Inclusion et accessibilité | interprétation langues nationales, accessibilité handicap, mesures favorisant la participation des femmes et des jeunes ruraux | 2–5 % |
| SE | Suivi-évaluation | collecte de données, évaluation externe, rapport | 2–5 % |
| AD | Frais administratifs directs | comptabilité, frais bancaires, assurances, loyer au prorata, fournitures | 3–7 % |
| IM | Imprévus | réserve pour aléas, dépensée sur justificatifs | 5–10 % [À VÉRIFIER : plafond du bailleur] |
| FI | Frais indirects (overheads) | forfait en % des coûts directs pour le fonctionnement général de la structure | 0–7 % [À VÉRIFIER : taux admis par le bailleur] |

Notes de définition : *frais indirects* (ou « overheads ») = coûts de fonctionnement de la
structure qu'on ne peut pas rattacher à une seule activité (électricité du bureau, direction,
logiciels) ; les bailleurs les acceptent souvent comme un pourcentage forfaitaire des coûts
directs, sans justificatif ligne à ligne. *Frais administratifs directs* = coûts administratifs
imputables au projet et justifiés par facture. Ne pas compter les mêmes coûts dans les deux.

Sous-rubriques par secteur (à insérer sous RH/EQ/PR/CO) :

| Secteur | Sous-rubriques recommandées |
|---|---|
| Cinéma / audiovisuel | Développement (écriture, repérages, teaser) ; Tournage (équipe, matériel, décors, transport, régie) ; Post-production (montage, son, étalonnage, sous-titrage, DCP) ; Diffusion (festivals, projections locales, promotion) |
| Festival / spectacle vivant | Programmation artistique (cachets, droits d'auteur à la société de gestion collective, transport et accueil artistes) ; Technique (scène, son, lumière, électricité/groupe électrogène) ; Sécurité et accueil (agents, secours, sanitaires, accessibilité) ; Billetterie (système, Mobile Money, contrôle) ; Communication (médias, affichage, réseaux) |
| Mode / artisanat | Matières et fournitures ; Production (main-d'œuvre, ateliers, contrôle qualité) ; Shooting et lookbook ; Salons et déplacements commerciaux ; E-commerce (site, paiement, logistique) ; Propriété intellectuelle (dépôt de marque OAPI) |
| Musique (album, tournée) | Création (composition, arrangements, studio) ; Fabrication/distribution numérique ; Clips ; Tournée (cachets, transport, technique) ; Promotion |
| Arts visuels / exposition | Production des œuvres ; Scénographie et accrochage ; Transport et assurance des œuvres ; Médiation et publics ; Catalogue |
| Édition / jeux vidéo / médias | Création (auteurs, illustrateurs, développeurs) ; Fabrication ou développement technique ; Diffusion et distribution ; Droits et licences ; Marketing |

### (b) Tableau budget détaillé

| Code | Rubrique | Désignation | Unité | Qté | Coût unitaire FCFA | Total FCFA | Total EUR | Source de financement | Statut | Éligible [bailleur X] | Justificatif attendu |
|---|---|---|---|---:|---:|---:|---:|---|---|---|---|
| RH-01 | Ressources humaines | [fonction] | jour | [n] | [montant] | [=qté x CU] | [=FCFA/655,957] | [bailleur / apport propre / valorisation / recettes] | acquis / demandé / à chercher | oui / non / à vérifier | contrat + facture ou reçu signé |
| RH-02 | Ressources humaines | [fonction] | mois | | | | | | | | contrat + fiche de paie |
| EQ-01 | Équipement et location | [matériel] | jour | | | | | | | | facture de location |
| PR-01 | Production / création | [poste] | forfait | | | | | | | | devis puis facture |
| LO-01 | Logistique et déplacements | [trajet] | voyage | | | | | | | | billets + reçus |
| CO-01 | Communication et diffusion | [support] | unité | | | | | | | | facture + exemplaire |
| IN-01 | Inclusion et accessibilité | Interprétation [langue nationale] | séance | | | | | | | | contrat + feuille de présence |
| SE-01 | Suivi-évaluation | Collecte et rapport d'évaluation | forfait | | | | | | | | rapport + facture |
| AD-01 | Frais administratifs | Tenue de comptabilité | mois | | | | | | | | facture cabinet |
| IM-01 | Imprévus | Imprévus ([x] %) | forfait | 1 | | | | | | à vérifier | justificatifs réels |
| | **TOTAL** | | | | | **[somme]** | **[somme]** | | | | |

Légende statut : *acquis* = convention signée ou argent disponible ; *demandé* = dossier déposé ;
*à chercher* = source non identifiée ou non sollicitée. Légende éligible : *oui* = autorisé par
les lignes directrices ; *non* = exclu (à financer par une autre source) ; *à vérifier* = pas de
réponse claire dans les lignes directrices, question à poser au bailleur avant dépôt.

### (c) Plan de financement multi-sources

| Source | Type | Montant FCFA | Montant EUR | % du total | Statut | Pièce de preuve | Date probable de confirmation |
|---|---|---:|---:|---:|---|---|---|
| [Bailleur principal] | subvention | | | | demandé | convention signée | |
| [Cofinanceur 1] | subvention | | | | demandé / acquis | lettre d'engagement | |
| [Cofinanceur 2] | subvention / mécénat | | | | à chercher | lettre d'intention | |
| Apport propre en numéraire | fonds propres | | | | acquis | relevé bancaire | |
| Valorisation en nature | contribution non monétaire | | | | acquis | attestations de mise à disposition | |
| Recettes propres : billetterie | recettes | | | | prévisionnel (scénario bas) | historique ou étude | |
| Recettes propres : ventes / prestations | recettes | | | | prévisionnel | bons de commande | |
| **TOTAL** | | **[= total dépenses]** | | **100 %** | | | |

Indicateurs à afficher sous le tableau : part du bailleur principal (%), taux de cofinancement
(%), part en nature (%), part des sources acquises (%). *Valorisation en nature* (ou
« contribution en nature ») = ressources apportées sans paiement (temps bénévole, prêt de
matériel, local, services offerts) chiffrées à leur valeur de marché locale et attestées par écrit ;
tous les bailleurs ne l'acceptent pas comme cofinancement et certains la plafonnent [À VÉRIFIER].

### (d) Grille de contrôle d'éligibilité des dépenses

| Dépense ou catégorie | Règle lue dans les lignes directrices (citer la page) | Éligible | Raison / condition | Action |
|---|---|---|---|---|
| Achat d'équipement durable | [ex. : « plafonné à x % » ou « inéligible »] | oui / non / à vérifier | [ex. : accepté si indispensable et amorti sur le projet] | privilégier la location ; sinon financer sur apport propre |
| Cachets et salaires de l'équipe | | | contrats écrits, taux d'usage, pas de double financement | joindre grille tarifaire |
| Per diem | | | barème du bailleur ou barème national [À VÉRIFIER] | aligner les montants |
| Frais indirects | | | taux maximal admis [À VÉRIFIER] | ne pas dépasser |
| Imprévus | | | plafond et conditions d'utilisation [À VÉRIFIER] | justifier à l'usage |
| TVA | | | éligible seulement si non récupérable (attestation) | demander à l'expert-comptable |
| Dépenses antérieures à la signature | | généralement non | période d'éligibilité définie par la convention | reporter ou financer autrement |
| Construction, achat de terrain ou véhicule | | généralement non | | autre source |
| Dettes, intérêts, pertes de change | | généralement non | | autre source / provision |
| Dépenses en espèces sans reçu | | non | traçabilité exigée | reçus signés, Mobile Money |
| Mesures inclusion / accessibilité | | généralement oui, souvent encouragées | lien avec les objectifs du bailleur | les rendre visibles |

### (e) Méthode de chiffrage réaliste et sources de prix

| Poste | Source de prix à privilégier | Règle de prudence |
|---|---|---|
| Cachets artistes et techniciens | grilles d'usage du secteur local (syndicats, associations professionnelles, pairs) — à vérifier localement ; contrats de projets précédents | écrire le tarif journalier et le nombre de jours ; prévoir les charges si salaire |
| Location de matériel | 2 à 3 devis écrits de loueurs locaux ou de la capitale régionale | inclure transport, assurance et caution dans la ligne |
| Transport | tarifs affichés des compagnies, prix du carburant au jour J, location de véhicule avec chauffeur | +10 % si saison des pluies ou zones enclavées |
| Hébergement et restauration | prix constatés sur place, barème per diem du bailleur [À VÉRIFIER] | distinguer per diem et remboursement sur facture |
| Impression et communication | devis imprimeurs, grilles tarifaires des radios et médias | prévoir les versions en langues nationales |
| Prestations numériques (site, paiement, e-commerce) | devis prestataires, tarifs publics des plateformes | frais de transaction Mobile Money et bancaires |
| Salaires de coordination | référence du marché local, proportion du temps réellement passé | justifier par feuilles de temps |
| Tout poste sans devis | estimation argumentée (comparaison avec un projet similaire) | marquer « estimation » et obtenir un devis avant le dépôt |

Règles transversales : chiffrer en FCFA puis convertir (jamais l'inverse) ; arrondir au millier de
FCFA ; dater les prix ; signaler toute dépense en devise étrangère (variation de change à
provisionner) ; relire le total par rubrique en se demandant « quelqu'un du secteur trouverait-il
ce montant crédible ? ».

### (f) Format CSV attendu par `scripts/budget.py`

```csv
code,rubrique,designation,unite,quantite,cout_unitaire_fcfa,source,statut,eligible,justificatif
RH-01,Ressources humaines,Réalisatrice (cachet réalisation),forfait,1,1500000,OIF,demandé,oui,contrat + reçu signé
EQ-01,Équipement et location,Location caméra + optiques,jour,20,80000,OIF,demandé,oui,facture de location
```

Règles : en-tête obligatoire et identique ; séparateur « , » ou « ; » ; un libellé contenant une
virgule doit être entre guillemets (`"Imprévus (environ 4,5 %)"`) ; `source` vide = ligne non
financée (signalée) ; colonne facultative `total_fcfa` si le total ne vaut pas quantité x coût
unitaire. Commande type :

```bash
python3 -I skills/budget-cofinancement/scripts/budget.py projet/budget/budget.csv \
  --total-attendu 16400000 --cofinancement-min 20 \
  --plafond "Frais administratifs=7" --plafond "Imprévus=5" --usd <taux du jour>
```

### (g) Notes budgétaires types (à joindre au dossier)

> **Hypothèses générales.** Budget établi en FCFA (XAF) et converti en euros à la parité fixe
> 1 EUR = 655,957 FCFA. Prix relevés en [mois année] à [ville]. Les cachets suivent les tarifs
> d'usage du secteur à [ville] ; les locations de matériel reposent sur des devis joints en annexe.
> Les imprévus ([x] %) ne seront dépensés que sur justificatifs. Les contributions en nature sont
> valorisées à leur prix de marché local et attestées par écrit par chaque partenaire. La structure
> porteuse [est / n'est pas] assujettie à la TVA ; les montants sont présentés [TTC / HT].

### (h) Exemple rempli — scénario 1 : documentaire « Femmes pêcheuses du lac Tchad »

Contexte : court-métrage documentaire de 26 min, 10 mois (développement complémentaire,
tournage 20 jours à Bol, post-production, diffusion locale et festivals), porté par une association
partenaire en attendant le statut de la réalisatrice. Montant visé : 25 000 EUR = 16 400 000 FCFA.
Bailleur principal pressenti : OIF (Fonds Image de la Francophonie) [À VÉRIFIER — plafond,
taux de cofinancement et calendrier sur le site officiel de l'OIF] ; cofinancement : Institut
français (programme local) et Goethe-Institut [À VÉRIFIER].

Extrait du budget détaillé (fichier complet : 21 lignes dans `budget.csv`) :

| Code | Rubrique | Désignation | Unité | Qté | CU FCFA | Total FCFA | Total EUR | Source | Statut | Éligible OIF | Justificatif |
|---|---|---|---|---:|---:|---:|---:|---|---|---|---|
| RH-01 | Ressources humaines | Réalisatrice (cachet) | forfait | 1 | 1 500 000 | 1 500 000 | 2 286,74 | OIF | demandé | oui | contrat + reçu |
| RH-02 | Ressources humaines | Chef opérateur image | jour | 20 | 60 000 | 1 200 000 | 1 829,39 | OIF | demandé | oui | contrat + facture |
| RH-06 | Ressources humaines | Coordination production (association) | mois | 8 | 150 000 | 1 200 000 | 1 829,39 | Valorisation en nature | acquis | à vérifier | attestation + feuilles de temps |
| EQ-01 | Équipement et location | Location caméra + optiques | jour | 20 | 80 000 | 1 600 000 | 2 439,18 | OIF | demandé | oui | facture location |
| PR-02 | Production et création | Fixeuse-interprète (langues locales) | jour | 20 | 20 000 | 400 000 | 609,80 | Institut français | demandé | oui | contrat + reçus |
| LO-02 | Logistique et déplacements | Hébergement équipe à Bol | nuitée | 60 | 15 000 | 900 000 | 1 372,04 | Institut français | demandé | oui | factures |
| CO-01 | Communication et diffusion | Sous-titrage FR/EN + audiodescription | forfait | 1 | 600 000 | 600 000 | 914,69 | OIF | demandé | oui | facture |
| CO-02 | Communication et diffusion | Projections-débats dans 5 villages riverains | séance | 5 | 150 000 | 750 000 | 1 143,37 | Goethe-Institut | à chercher | à vérifier | fiches de présence + photos |
| AD-01 | Frais administratifs | Tenue de comptabilité | mois | 10 | 50 000 | 500 000 | 762,25 | Apport propre | acquis | oui | facture cabinet |
| IM-01 | Imprévus | Imprévus (environ 4,5 %) | forfait | 1 | 700 000 | 700 000 | 1 067,14 | OIF | demandé | à vérifier | justificatifs réels |

Sous-totaux calculés par le script :

| Rubrique | Total FCFA | Total EUR | % |
|---|---:|---:|---:|
| Ressources humaines | 7 200 000 | 10 976,33 | 43,9 % |
| Équipement et location | 2 450 000 | 3 735,00 | 14,9 % |
| Production et création | 1 500 000 | 2 286,74 | 9,1 % |
| Logistique et déplacements | 2 180 000 | 3 323,39 | 13,3 % |
| Communication et diffusion | 1 750 000 | 2 667,86 | 10,7 % |
| Frais administratifs | 620 000 | 945,18 | 3,8 % |
| Imprévus | 700 000 | 1 067,14 | 4,3 % |
| **TOTAL** | **16 400 000** | **25 001,64** | **100 %** |

Plan de financement :

| Source | Montant FCFA | Montant EUR | % | Statut |
|---|---:|---:|---:|---|
| OIF — Fonds Image de la Francophonie (bailleur principal) | 8 000 000 | 12 195,92 | 48,8 % | demandé |
| Institut français (programme local) | 3 600 000 | 5 488,16 | 22,0 % | demandé |
| Goethe-Institut (projections-débats, musique) | 1 250 000 | 1 905,61 | 7,6 % | à chercher |
| Valorisation en nature (coordination, prêt kit son) | 1 800 000 | 2 744,08 | 11,0 % | acquis |
| Apport propre (réalisatrice + association) | 1 750 000 | 2 667,86 | 10,7 % | acquis |
| **TOTAL** | **16 400 000** | **25 001,64** | **100 %** | |

Taux de cofinancement hors bailleur principal : 51,2 %, dont 21,7 % acquis (apport propre +
nature). Points d'attention relevés : la valorisation (11 %) doit être confirmée comme
cofinancement acceptable par l'OIF [À VÉRIFIER] ; les projections-débats n'ont pas encore de
source confirmée ; la part inclusion (interprète en langues locales, audiodescription, projections
dans les villages) est visible et chiffrée, ce qui renforce le dossier. Un expert-comptable est
indispensable si le bailleur demande les comptes certifiés de l'association porteuse.

## Critères de qualité du livrable

- Toutes les activités du narratif ont des lignes budgétaires, et inversement.
- Chaque ligne a unité, quantité, coût unitaire, source, statut, éligibilité et justificatif.
- Le total des sources égale le total des dépenses au franc près ; le script ne renvoie aucune
  alerte non expliquée.
- Les montants figurent en FCFA et dans la devise du bailleur ; le taux est daté.
- Le taux de cofinancement exigé est atteint, avec une marge ; les sources « acquises » sont
  étayées par une pièce.
- Les plafonds du bailleur (frais indirects, imprévus, équipement, per diem) sont respectés ou
  marqués « à vérifier » avec la question à poser.
- Les coûts d'inclusion, de suivi-évaluation et de communication sont présents et non symboliques.
- Les coûts unitaires sont sourcés ; aucun forfait non décomposé supérieur à 5 % du total.
- Les notes budgétaires expliquent les hypothèses en moins d'une page.
- `projet/budget/budget.csv` tourne sans erreur avec le script et `projet/ETAT.md` est à jour.

## Erreurs fréquentes à éviter

- Partir du montant du bailleur et « remplir » jusqu'au plafond au lieu de chiffrer le besoin réel.
- Oublier les coûts invisibles : charges sociales, frais bancaires et de transfert, assurances,
  droits d'auteur dus à la société de gestion collective, visas, imprévus, suivi-évaluation.
- Sous-payer l'équipe ou ne pas se rémunérer soi-même : les bailleurs y voient un manque de
  professionnalisme et un risque d'abandon.
- Mélanger budget et trésorerie : le budget dit « combien » ; la trésorerie dit « quand ».
- Double financement : imputer la même dépense à deux bailleurs.
- Valoriser des apports en nature sans attestation ni base de prix, ou au-delà de ce que le
  bailleur admet.
- Convertir avec un taux arrondi (650 ou 660) : utiliser la parité fixe 655,957.
- Ignorer les rubriques imposées par le bailleur ou dépasser la longueur de son tableau.
- Inventer un plafond ou un taux de cofinancement « habituel » : toujours lire le document de
  l'appel ou marquer [À VÉRIFIER].
- Prévoir des recettes de billetterie optimistes : présenter un scénario bas et expliquer le
  scénario haut à part.
- Omettre la TVA ou la traiter sans savoir si elle est récupérable.

## Références et sources à vérifier

- Lignes directrices et modèle budgétaire du bailleur visé : toujours le document officiel de
  l'appel en cours (OIF — Fonds Image de la Francophonie ; Institut français ; Goethe-Institut ;
  UE — programmes ACP-UE Culture et délégations ; Africalia ; UNESCO — FIDC ; AFD ; Prince
  Claus Fund ; Afrique Créative ; Fondation Orange ; fonds nationaux type FOPICA, FONSIC).
  [À VÉRIFIER — source : site officiel de chaque bailleur ; recherche « <bailleur> appel à
  projets <année> lignes directrices budget »].
- Règles de l'UE sur les coûts éligibles, frais indirects et seuils d'audit des subventions :
  [À VÉRIFIER — source : documents contractuels du programme concerné].
- Barème per diem appliqué par le bailleur ou barème national : [À VÉRIFIER].
- Grilles de cachets d'usage : associations professionnelles locales, sociétés de gestion
  collective des droits d'auteur du pays (à vérifier localement).
- Parité FCFA/EUR : 1 EUR = 655,957 XAF = 655,957 XOF (fixe). Taux USD et autres : banque
  centrale (BEAC ou BCEAO) le jour de l'établissement du budget.
- Professionnels à mobiliser : expert-comptable (états financiers, TVA, attestation de bonne
  gestion), commissaire aux comptes ou auditeur externe si exigé par la convention, fiscaliste pour
  les retenues sur cachets d'artistes étrangers.

## Passage de relais

- Ensuite, dans l'ordre recommandé : `/icc:plan-tresorerie` (agent `icc-budget`) pour échelonner
  encaissements et décaissements ; `/icc:note-conceptuelle` (agent `icc-redaction`) pour rendre
  le narratif cohérent avec le budget ; `/icc:plan-mise-en-oeuvre` (agent `icc-mise-en-oeuvre`)
  si le projet est financé ou en cours de demande avancée.
- Si une dépense pose une question de statut ou de fiscalité : `/icc:statut-juridique`
  (agent `icc-juridique`).
- Si les sources manquent : retour vers `/icc:cartographie-bailleurs` ou `/icc:matching-appel`
  (agent `icc-financements`).

Mise à jour obligatoire de `projet/ETAT.md` (structure imposée du plugin) :

```markdown
# ÉTAT DU PROJET — <nom du projet>
Dernière mise à jour : AAAA-MM-JJ HH:MM
Agent actif : icc-budget | Skill en cours : /icc:budget-cofinancement
## Résumé du projet (5 lignes max)
<inchangé ou précisé>
## Étapes terminées (avec fichiers produits)
- Budget prévisionnel et plan de cofinancement : projet/budget/budget.md, projet/budget/budget.csv
  (total <FCFA> / <EUR> ; cofinancement <x> % ; <n> lignes « à vérifier »)
## Étape en cours (où on en est précisément)
<ex. : budget validé, en attente des devis location matériel et de la confirmation du plafond de valorisation>
## Prochaines étapes (ordre recommandé)
1. /icc:plan-tresorerie  2. /icc:note-conceptuelle  3. /icc:plan-mise-en-oeuvre
## Décisions prises / hypothèses à confirmer
- Taux 1 EUR = 655,957 FCFA ; imprévus <x> % ; valorisation <x> % [À VÉRIFIER auprès du bailleur]
## Questions en attente de réponse du promoteur
- <devis manquants, confirmation des partenaires, assujettissement TVA>
## Alertes (délais, pièces manquantes, professionnel humain requis)
- Expert-comptable requis pour : <états financiers / attestation> ; date limite de l'appel : <date lue dans l'appel>
```
