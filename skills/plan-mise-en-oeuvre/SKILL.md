---
name: plan-mise-en-oeuvre
description: Utiliser quand le promoteur doit organiser l'exécution de son projet : plan d'action, activités, chronogramme, Gantt, jalons, rétro-planning, RACI (qui fait quoi), risques, achats et devis, réunions, rapports aux bailleurs ; mots-clés : « planning », « organisation », « par où commencer », « rapport d'avancement ».
---

# /icc:plan-mise-en-oeuvre — Plan opérationnel, chronogramme, risques et reporting

## Objectif

Transformer un projet (financé, ou en cours de demande quand l'appel exige un plan d'action) en
plan opérationnel exécutable : lots et activités, chronogramme avec jalons, responsabilités,
ressources, registre des risques, achats, gouvernance, calendrier de reporting aux bailleurs.

Livrable : `projet/mise-en-oeuvre/plan.md` (sections 1 à 9 du gabarit (a) à (i)). Agent principal :
`icc-mise-en-oeuvre`. Les indicateurs et la collecte de données relèvent de `/icc:suivi-evaluation`,
mais le présent plan réserve les activités et le temps nécessaires au suivi-évaluation.

Définitions (à réutiliser telles quelles avec le promoteur) :
- *Lot* (ou « work package ») = grand bloc de travail homogène (ex. : Programmation artistique).
  *Activité* = action concrète dans un lot, avec un début, une fin, un responsable, un coût.
  *WBS* (« work breakdown structure », découpage du travail) = simple arbre : projet → lots →
  activités → tâches. On s'arrête quand chaque activité peut être confiée à une personne et
  vérifiée.
- *Jalon* = date-clé qui marque un résultat vérifiable (contrats signés, programme annoncé,
  rapport déposé). Un jalon n'a pas de durée.
- *Chronogramme* (diagramme de Gantt) = tableau des activités en lignes et du temps en colonnes.
- *Rétro-planning* = chronogramme construit à rebours depuis la date de l'événement (J-365 → J).
- *RACI* = pour chaque activité : qui Réalise, qui est responsable final / Approuve (A), qui est
  Consulté, qui est Informé. Une seule personne « A » par activité.
- *Registre des risques* = liste des événements qui pourraient nuire au projet, avec leur
  probabilité, leur impact, les mesures de prévention (éviter qu'ils arrivent) et d'atténuation
  (limiter les dégâts s'ils arrivent).
- *Passation / achats* = façon de choisir les fournisseurs ; les bailleurs exigent souvent plusieurs
  devis au-delà de certains montants [À VÉRIFIER dans la convention].
- *Reporting* = rapports narratifs (ce qui a été fait) et financiers (ce qui a été dépensé) dus au
  bailleur à des dates fixées par la convention ; ils déclenchent les tranches de paiement.

## Quand l'utiliser / ne pas l'utiliser

Utiliser quand :
- la convention est signée ou le financement très probable, et il faut démarrer ;
- l'appel demande un plan d'action, un chronogramme ou une analyse des risques dans le dossier ;
- le projet implique plusieurs partenaires, lieux ou prestataires ;
- le promoteur se sent dépassé par le nombre de choses à faire ;
- un rapport intermédiaire ou final est dû et il n'existe pas de modèle.

Ne pas l'utiliser pour : chiffrer (budget), prévoir la trésorerie, définir les indicateurs
détaillés (suivi-évaluation), rédiger les contrats (juridique). Ce skill les cite et les ordonne.

## Prérequis

Lire si présents : `projet/ETAT.md` ; `projet/fiche-projet.md` ; `projet/budget/budget.md` (les
rubriques deviennent des lots et des ressources) ; `projet/budget/tresorerie.md` (dates des tranches
et des rapports) ; `projet/dossiers/<slug-bailleur>/note-conceptuelle.md` (objectifs et résultats
promis) ; la convention de financement ou les lignes directrices (format et calendrier des rapports,
règles d'achats, visibilité du bailleur, modifications autorisées).

Informations nécessaires si absentes : date de début et de fin, date de l'événement ou de la
livraison, équipe disponible (noms, rôles, temps), partenaires et leur rôle, contraintes de
calendrier (saison des pluies, fêtes, examens, élections, calendrier des festivals), règles du
bailleur en matière de rapports et d'achats.

Tout se fait hors ligne, en Markdown ; pas de script nécessaire.

## Procédure étape par étape

1. **Cadrer.** Lire `projet/ETAT.md` et les fichiers présents. Reformuler en 5 lignes : objectif,
   résultats attendus, dates, budget, bailleurs et leurs échéances de rapport.
2. **Découper en lots** (gabarit (a)). Partir des rubriques budgétaires et du narratif : 5 à 9 lots,
   dont obligatoirement « Gestion, administration et reporting », « Communication et visibilité »,
   « Suivi-évaluation » et une ligne ou un lot « Inclusion et accessibilité ».
3. **Détailler les activités** : pour chacune, un verbe d'action, un livrable vérifiable, un
   responsable, une durée, un coût (référence à la ligne budgétaire), une dépendance éventuelle.
4. **Construire le chronogramme** (gabarit (b)). Choisir la maille : mois pour un projet de 12 à 36
   mois, semaine pour les 3 derniers mois avant un événement. Placer les jalons et les échéances
   de rapport. Pour un événement, construire en rétro-planning depuis J. Tenir compte des saisons
   (pluies, chaleur extrême, fêtes religieuses, rentrée scolaire, période électorale).
5. **Attribuer les responsabilités** (RACI, gabarit (c)) ; vérifier qu'aucune personne ne cumule
   plus de 3 « A » simultanés et que chaque partenaire sait ce qu'il doit livrer et quand.
6. **Lister les ressources** par activité : personnes, matériel, lieux, autorisations, argent (lien
   avec la trésorerie : une activité ne peut pas démarrer avant la tranche qui la finance).
7. **Analyser les risques** (gabarit (d)) : lister au moins 10 risques, dont les risques typiques
   ICC en Afrique (retard de versement, saison des pluies, coupures d'électricité ou de connexion,
   autorisations administratives, sécurité, défaillance d'un partenaire, variation de change,
   santé, désistement d'artiste). Noter probabilité x impact, prévention, atténuation,
   responsable, signal d'alerte.
8. **Fixer la procédure d'achats** (gabarit (e)) : seuils de la convention [À VÉRIFIER],
   nombre de devis, grille de comparaison, archivage des pièces.
9. **Définir la gouvernance** (gabarit (f)) : instances, fréquence, ordre du jour type, prise de
   décision, modèle de compte rendu.
10. **Établir le calendrier de reporting** (gabarit (g)) à partir de la convention : dates, type de
    rapport, pièces à joindre, tranche déclenchée, qui rédige, qui valide (expert-comptable pour le
    volet financier si exigé).
11. **Préparer le modèle de rapport d'avancement** (gabarit (h)) et le compte rendu type (gabarit (i)).
12. **Relire la cohérence** : chaque résultat promis dans la note conceptuelle a ses activités ; chaque
    activité a un coût budgété et une date compatible avec la trésorerie ; chaque rapport est
    planifié avant la tranche qu'il déclenche.
13. **Écrire `projet/mise-en-oeuvre/plan.md`**, signaler les professionnels requis (expert-comptable
    pour les rapports financiers certifiés ; juriste pour les contrats artistes et prestataires ;
    assureur ; huissier pour constats si la convention l'exige), puis **mettre à jour
    `projet/ETAT.md`**.

Mode faible connectivité : écrire le plan lot par lot et sauvegarder ; noter dans `projet/ETAT.md`
le dernier lot complété et le gabarit en cours.

## Questions à poser au promoteur

1. Quelle est la date de fin non négociable (événement, livraison, fin de convention) ?
2. Qui compose l'équipe, avec quel temps disponible par semaine, et qui décide en dernier ressort ?
3. Quels partenaires sont engagés par écrit et pour quoi ?
4. Quelles contraintes de calendrier connaissez-vous (pluies, fêtes, examens, élections, autres
   événements concurrents) ?
5. Quelles autorisations faut-il obtenir (occupation de l'espace public, tournage, sécurité,
   droits d'auteur auprès de la société de gestion collective, visas d'artistes) et quel délai ?
6. Que dit la convention sur les rapports (dates, format, langue, pièces) et sur les achats
   (nombre de devis, seuils) ?
7. Qu'est-ce qui vous a mis en difficulté lors d'un projet précédent ?
8. Comment comptez-vous assurer la participation des femmes, des jeunes, des personnes handicapées
   et des publics ruraux ou non francophones, et qui en est responsable ?
9. Quelle fréquence de réunion l'équipe peut-elle tenir réellement, et par quel canal (présentiel,
   téléphone, messagerie) ?

## Gabarits complets

### (a) Tableau des lots et activités

| Code | Lot / activité | Livrable vérifiable | Responsable | Début | Fin | Durée | Dépend de | Ligne budgétaire | Coût FCFA | Coût EUR |
|---|---|---|---|---|---|---|---|---|---:|---:|
| L1 | Gestion, administration et reporting | | | | | | | AD, SE | | |
| L1.1 | Signer la convention, ouvrir le dossier comptable | convention signée, plan comptable | | | | | — | AD-01 | | |
| L1.2 | Rapport intermédiaire narratif et financier | rapport accepté | | | | | L2–L5 | AD-01 | | |
| L1.3 | Rapport final et clôture | rapport accepté, solde reçu | | | | | tous | AD-01, SE-01 | | |
| L2 | [Lot cœur de métier 1 : programmation, tournage, collection…] | | | | | | | | | |
| L2.1 | | | | | | | | | | |
| L3 | [Lot cœur de métier 2 : technique, post-production, e-commerce…] | | | | | | | | | |
| L4 | Communication et visibilité (dont visibilité du bailleur) | plan de communication, supports, revue de presse | | | | | L2 | CO | | |
| L5 | Inclusion et accessibilité | mesures mises en œuvre et documentées | | | | | L2, L3 | IN | | |
| L6 | Suivi-évaluation | ligne de base, collecte, rapport d'évaluation | | | | | tous | SE | | |
| L7 | Partenariats et mobilisation | conventions de partenariat signées | | | | | — | | | |
| | **Total** | | | | | | | | | |

### (b) Chronogramme (Gantt en tableau) et jalons

Maille mensuelle (projet de 12 mois) — mettre « X » dans les mois d'activité, « J » pour un jalon,
« R » pour une échéance de rapport :

| Code | Activité | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 | M13 | M14 | M15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1.1 | Signature, mise en place administrative | X | J | | | | | | | | | | | | | |
| L2.1 | [activité] | | X | X | X | | | | | | | | | | | |
| L2.2 | [activité] | | | | X | X | X | | | | | | | | | |
| L1.2 | Rapport intermédiaire | | | | | | R | | | | | | | | | |
| L3.1 | [activité] | | | | | | | X | X | X | | | | | | |
| L4.1 | Communication | | | X | | X | | X | X | X | X | | | | | |
| L5.1 | Inclusion et accessibilité | | X | | | X | | | X | | X | | | | | |
| L6.1 | Suivi-évaluation | X | | | | | X | | | | X | X | | | | |
| — | Événement / livraison | | | | | | | | | | J | | | | | |
| L1.3 | Rapport final | | | | | | | | | | | | R | | | |
| — | Solde du bailleur | | | | | | | | | | | | | | | J |

Tableau des jalons :

| Jalon | Date | Preuve | Conséquence si manqué |
|---|---|---|---|
| Convention signée | | copie signée | pas de démarrage éligible |
| Partenaires et prestataires contractualisés | | contrats | retard en cascade |
| Programme / scénario / collection validé | | document validé | communication impossible |
| Autorisations obtenues | | arrêtés, récépissés | annulation possible |
| Rapport intermédiaire déposé | | accusé de réception | tranche 2 retardée |
| Événement / livraison | | photos, fiches de présence, œuvre livrée | — |
| Rapport final déposé | | accusé de réception | solde retardé |

### (c) Matrice RACI

| Activité | [Promoteur / direction] | [Coordination] | [Responsable technique] | [Responsable communication] | [Trésorier / comptable] | [Partenaire 1] | [Bailleur] |
|---|---|---|---|---|---|---|---|
| Signature et administration | A | R | I | I | C | I | C |
| Programmation / création | A | R | C | I | I | C | I |
| Achats et contrats prestataires | A | R | C | I | C | I | I |
| Communication et visibilité | I | A | I | R | I | C | C |
| Inclusion et accessibilité | A | R | C | C | I | C | I |
| Suivi-évaluation | A | C | I | I | I | C | I |
| Rapport intermédiaire / final | A | R | C | C | R (volet financier) | C | I |

R = réalise ; A = approuve / responsable final (un seul par ligne) ; C = consulté avant ; I = informé après.

### (d) Registre des risques (probabilité x impact)

Échelle : probabilité 1 (rare) à 3 (probable) ; impact 1 (faible) à 3 (grave) ; score = P x I ;
traiter en priorité les scores 6 et 9.

| N° | Risque | P | I | Score | Prévention | Atténuation si le risque survient | Signal d'alerte | Responsable |
|---|---|---|---|---|---|---|---|---|
| 1 | Retard de versement d'une tranche | 3 | 3 | 9 | déposer les rapports en avance ; plan de couverture de trésorerie ; relance planifiée | activer avance partenaire ; échelonner les paiements ; informer les prestataires | tranche non reçue 2 semaines après la date attendue | direction |
| 2 | Saison des pluies (routes coupées, plein air impossible) | 2 | 3 | 6 | caler les activités extérieures en saison sèche ; lieu de repli couvert ; transport anticipé | reporter de quelques jours ; bâcher ; déplacer en salle | prévisions météo à J-7 | coordination |
| 3 | Coupures d'électricité ou de connexion | 3 | 2 | 6 | groupe électrogène et carburant ; onduleurs ; sauvegardes hors ligne ; fichiers de travail locaux | basculer sur groupe ; reporter les envois ; travailler hors ligne | coupures répétées la semaine précédente | technique |
| 4 | Autorisations administratives tardives ou refusées | 2 | 3 | 6 | déposer les demandes 3 mois avant ; relations suivies avec les autorités ; dossier complet | lieu ou date alternatifs ; médiation par un partenaire institutionnel | pas de récépissé à J-45 | direction |
| 5 | Sécurité (foule, incidents, contexte) | 2 | 3 | 6 | plan de sécurité, agents formés, secours, assurance, coordination avec les autorités | protocole d'évacuation ; annulation partielle | alerte des autorités, incidents locaux | coordination |
| 6 | Désistement d'un partenaire ou d'un artiste | 2 | 2 | 4 | contrats écrits avec clauses ; plan B par poste clé | remplaçant identifié à l'avance ; réaffectation du cachet | absence de réponse 2 semaines | programmation |
| 7 | Variation de change sur un financement en devise étrangère hors euro | 2 | 2 | 4 | convertir dès réception ; provision ; budget en FCFA | réduire des dépenses non critiques | variation > 5 % | trésorier |
| 8 | Dépassement de budget sur une rubrique | 2 | 2 | 4 | 3 devis ; suivi mensuel prévu/réalisé ; imprévus | réallocation autorisée par le bailleur [À VÉRIFIER : plafond de flexibilité entre rubriques] | écart > 10 % sur une rubrique | trésorier |
| 9 | Problème de santé d'une personne clé | 1 | 3 | 3 | binômes sur chaque fonction ; documentation partagée | redistribution des rôles | — | direction |
| 10 | Faible participation des femmes ou des publics ciblés | 2 | 2 | 4 | horaires et lieux adaptés, garde d'enfants, communication en langues nationales, transport | ajuster la mobilisation en cours de projet | inscriptions ventilées à J-30 sous la cible | inclusion |
| 11 | Perte de données ou de justificatifs | 2 | 3 | 6 | classeur physique + copie numérique hebdomadaire ; photos des reçus le jour même | reconstitution avec fournisseurs ; déclaration au bailleur | justificatifs manquants au point mensuel | comptable |
| 12 | Conflit interne ou de gouvernance | 2 | 2 | 4 | RACI écrit ; règles de décision ; réunions régulières | médiation par un tiers de confiance | réunions annulées, décisions bloquées | direction |

### (e) Plan de passation / achats simplifié

| Tranche de montant (à aligner sur la convention [À VÉRIFIER]) | Procédure minimale | Pièces à conserver |
|---|---|---|
| Petits achats (en dessous du premier seuil du bailleur) | achat direct sur facture ou reçu signé | facture/reçu, preuve de paiement |
| Achats intermédiaires | 3 devis écrits comparés sur une grille (prix, délai, qualité, références) ; décision motivée | devis, grille de comparaison signée, bon de commande, facture, preuve de paiement, PV de réception |
| Achats importants | consultation écrite élargie ou appel d'offres simplifié ; comité de 3 personnes ; contrat écrit | dossier de consultation, offres, PV d'ouverture et d'analyse, contrat, factures, PV de réception |
| Tout achat | pas de paiement en espèces sans reçu ; privilégier virement ou Mobile Money ; pas de conflit d'intérêts (déclaration) | registre des achats |

Grille de comparaison de devis :

| Critère | Pondération | Fournisseur A | Fournisseur B | Fournisseur C |
|---|---:|---|---|---|
| Prix TTC FCFA | 40 % | | | |
| Délai et disponibilité aux dates | 20 % | | | |
| Qualité / conformité technique | 25 % | | | |
| Références et fiabilité | 15 % | | | |
| **Note pondérée / 100** | | | | |
| Décision motivée et signatures | | | | |

### (f) Gouvernance et réunions

| Instance | Participants | Fréquence | Objet | Décisions | Compte rendu |
|---|---|---|---|---|---|
| Point d'équipe | équipe opérationnelle | hebdomadaire (30 min, messagerie ou présentiel) | avancement, blocages, semaine à venir | opérationnelles | 10 lignes dans `projet/journal.md` |
| Comité de pilotage | direction, coordination, trésorier, partenaires clés | mensuel, puis bimensuel à J-60 | chronogramme, budget prévu/réalisé, risques, reporting | stratégiques, réallocations | gabarit (i) |
| Point bailleur | direction + gestionnaire du bailleur | selon convention ou trimestriel | avancement, difficultés, modifications à faire approuver | validation des changements | courriel récapitulatif |
| Réunion de lancement / de clôture | tous + partenaires | une fois chacune | partage du plan ; bilan et leçons apprises | — | compte rendu + liste de présence |

Règles : ordre du jour envoyé 48 h avant ; chaque décision a un responsable et une date ; les
décisions qui modifient le budget ou le chronogramme approuvé sont soumises au bailleur selon la
convention [À VÉRIFIER : seuil de modification sans avenant].

### (g) Calendrier de reporting aux bailleurs

| Bailleur | Rapport | Période couverte | Date limite (convention) | Format / langue / pages | Pièces jointes | Tranche déclenchée | Rédige | Valide | Date interne de bouclage (J-15) |
|---|---|---|---|---|---|---|---|---|---|
| [Bailleur principal] | Intermédiaire narratif + financier | M1–M6 | [À VÉRIFIER] | [modèle du bailleur] | état des dépenses, copies de justificatifs, photos, fiches de présence, revue de presse | tranche 2 | coordination + comptable | direction (+ expert-comptable si exigé) | |
| [Bailleur principal] | Final narratif + financier | M1–M12 | [À VÉRIFIER] | | idem + rapport d'évaluation, inventaire, preuves de visibilité | solde | | | |
| [Cofinanceur] | Final | | [À VÉRIFIER] | | | solde | | | |
| Partenaires / sponsors | Bilan de visibilité | post-événement | contrat | dossier photos, audience, retombées | solde sponsor | communication | direction | |

### (h) Modèle de rapport d'avancement (intermédiaire) — prêt à remplir

> **Rapport intermédiaire — [Nom du projet]**
> Convention n° [réf.] — Bailleur : [nom] — Structure : [nom] — Période : du [date] au [date]
> Rédigé par : [nom, fonction] — Date : [date]
>
> **1. Résumé exécutif (10 lignes).** Avancement global : [x] % des activités réalisées, [x] % du
> budget consommé. Principaux résultats : [3 points]. Principales difficultés : [2 points].
> Demandes au bailleur : [modification, prolongation, réallocation — ou « aucune »].
>
> **2. Activités réalisées par lot.**
>
> | Lot / activité | Prévu (période) | Réalisé | Écart et explication | Preuves disponibles |
> |---|---|---|---|---|
> | L2.1 [ ] | | | | photos, listes de présence, contrats |
>
> **3. Résultats et indicateurs (extrait du cadre de suivi-évaluation).**
>
> | Indicateur | Ligne de base | Cible | Valeur atteinte à ce jour | dont femmes / jeunes / personnes handicapées / zone rurale | Source de vérification |
> |---|---|---|---|---|---|
> | | | | | | |
>
> **4. Inclusion, genre et impact social.** Mesures mises en œuvre : [ ]. Participation ventilée :
> [chiffres]. Difficultés et ajustements : [ ].
>
> **5. Partenariats, communication et visibilité du bailleur.** [Partenaires actifs, supports
> produits, mentions du bailleur — joindre les preuves.]
>
> **6. Difficultés rencontrées et mesures prises.** [Lien avec le registre des risques.]
>
> **7. Rapport financier (synthèse).**
>
> | Rubrique | Budget approuvé FCFA | Dépensé sur la période FCFA | Cumul dépensé FCFA | % consommé | Budget approuvé EUR | Cumul dépensé EUR | Écart et explication |
> |---|---:|---:|---:|---:|---:|---:|---|
> | Ressources humaines | | | | | | | |
> | … | | | | | | | |
> | **Total** | | | | | | | |
>
> Encaissements reçus : [tranche 1, date, montant]. Trésorerie au [date] : [montant]. Cofinancements
> mobilisés : [liste et montants]. Justificatifs : [n] pièces archivées, liste en annexe. Taux de
> change appliqué : 1 EUR = 655,957 FCFA [autre devise : taux daté].
>
> **8. Programme de la période suivante.** [Activités, jalons, besoins de décision du bailleur.]
>
> **9. Annexes.** Liste de présence ventilée, photos avec consentement, revue de presse, copies de
> justificatifs, contrats, devis comparés, rapport de suivi-évaluation.

### (i) Compte rendu de réunion type

> **Compte rendu — [Comité de pilotage / point d'équipe] n° [ ]** — Date : [ ] — Lieu / canal : [ ]
> Présents : [ ] — Excusés : [ ] — Rédacteur : [ ]
>
> | Point à l'ordre du jour | Discussion (3 lignes max) | Décision | Responsable | Échéance |
> |---|---|---|---|---|
> | 1. Avancement du chronogramme | | | | |
> | 2. Budget prévu / réalisé et trésorerie | | | | |
> | 3. Risques et alertes | | | | |
> | 4. Inclusion et participation | | | | |
> | 5. Reporting et bailleurs | | | | |
> | 6. Divers | | | | |
>
> Prochaine réunion : [date, heure, canal]. Compte rendu diffusé à : [ ] le [ ].

### (j) Exemple rempli — scénario 2 : festival de musiques, rétro-planning J-365 → J+30

Contexte : 1re édition, 3 jours fin novembre 2027 (J = jour d'ouverture), 5 000 spectateurs visés,
association de 12 musiciens, budget d'environ 60 000 EUR (39 400 000 FCFA), bailleur principal
international + ambassade + sponsors + billetterie. Saison des pluies locale supposée de mai à
octobre [à adapter au pays].

Lots : L1 Gestion et reporting ; L2 Programmation artistique ; L3 Technique et site ; L4 Sécurité,
accueil et billetterie ; L5 Communication et visibilité ; L6 Inclusion et accessibilité ; L7
Suivi-évaluation ; L8 Partenariats et sponsors.

Rétro-planning (extrait, maille mensuelle puis hebdomadaire) :

| Échéance | Lot | Activité | Livrable | Responsable (A/R) |
|---|---|---|---|---|
| J-365 (déc. 2026) | L1 | Dépôt des dossiers de financement, constitution du comité de pilotage | dossiers déposés, RACI signé | présidente (A) / coordinateur (R) |
| J-300 (févr. 2027) | L8 | Prospection sponsors (dossier de partenariat, 20 entreprises ciblées) | 20 rendez-vous | chargé partenariats |
| J-270 (mars 2027) | L1 | Signature convention bailleur principal, tranche 1 | convention, virement reçu | présidente |
| J-240 (avril) | L2 | Appel à candidatures artistes (objectif : 40 % de groupes avec au moins une femme leader, 30 % d'artistes de moins de 30 ans, 2 groupes de musique traditionnelle rurale) | 60 candidatures | directrice artistique |
| J-210 (mai) | L3 | Choix du site, autorisation d'occupation, pré-réservation technique (saison des pluies : site avec repli couvert) | arrêté municipal demandé, devis x3 | régisseur |
| J-180 (juin) | L2 | Programmation validée, contrats et acomptes artistes (30 %) ; déclaration à la société de gestion collective des droits d'auteur | 24 contrats signés | directrice artistique / juriste |
| J-150 (juillet) | L6 | Plan inclusion : accès personnes à mobilité réduite, interprétation en langue des signes sur la scène principale, navettes depuis 3 quartiers périphériques, tarif réduit étudiants, garde d'enfants | plan validé, devis | référente inclusion |
| J-120 (août) | L5 | Identité visuelle, site, réseaux ; plan média en français et en 2 langues nationales | charte, calendrier de publication | chargée communication |
| J-90 (sept.) | L8, L3 | Contrats sponsors signés (50 % encaissés) ; acompte technique scène-son-lumière | contrats, bon de commande | présidente / régisseur |
| J-60 (début oct.) | L1 | Rapport intermédiaire déposé (déclenche tranche 2) ; ouverture des pré-ventes Mobile Money | accusé de réception, billetterie ouverte | coordinateur / trésorière |
| J-45 | L4 | Plan de sécurité validé avec les autorités, recrutement et formation de 30 agents et bénévoles (parité visée), convention secours | plan signé, liste formée | responsable sécurité |
| J-30 | L5, L7 | Lancement de la campagne médias ; ligne de base de l'évaluation (questionnaire pré-festival en ligne et dans 3 quartiers) | spots diffusés, 200 réponses | communication / référent S&E |
| J-14 | L3 | Montage planifié, test électrique, groupe électrogène et carburant pour 3 jours | check-list signée | régisseur |
| J-7 | L2, L4 | Arrivée des artistes hors ville, répétitions, briefing sécurité et accueil, fiches de présence ventilées prêtes | planning répétitions | directrice artistique |
| J-2 → J-1 | L3 | Montage scène, balances, répétition générale accessibilité (parcours fauteuil, interprètes) | PV de réception technique | régisseur |
| J, J+1, J+2 | tous | Festival : comptage des entrées par tranche horaire, questionnaires de satisfaction (cible 400), photos/vidéos avec consentement | données brutes | coordinateur |
| J+3 → J+7 | L3, L1 | Démontage, paiement des soldes artistes et technique, inventaire | PV, reçus | régisseur / trésorière |
| J+15 | L5, L8 | Bilan de visibilité aux sponsors (solde 50 %), revue de presse | dossier envoyé | communication |
| J+30 (fin déc.) | L7, L1 | Réunion de clôture et leçons apprises ; lancement de la rédaction du rapport final (dépôt visé mi-janvier) | compte rendu, plan du rapport | présidente |

Trois risques prioritaires retenus (score 9 ou 6) : retard de la tranche 2 (prévention : rapport
intermédiaire déposé à J-60 ; atténuation : avance partenaire 3 000 000 FCFA négociée à J-90),
pluies tardives en novembre (site avec repli couvert, bâches, J+1 réservé comme jour tampon pour la
scène extérieure), coupures électriques (groupe électrogène dimensionné, carburant 3 jours, test à
J-14). Gouvernance : point d'équipe hebdomadaire par messagerie, comité de pilotage mensuel puis
toutes les deux semaines à partir de J-60. Reporting : intermédiaire à J-60, final mi-janvier avec
rapport financier revu par un expert-comptable (exigence probable du bailleur [À VÉRIFIER]).

## Critères de qualité du livrable

- Chaque résultat promis dans le dossier de financement est couvert par au moins une activité ;
  chaque activité a un livrable vérifiable, un responsable unique « A », des dates et un coût relié
  au budget.
- Le chronogramme place les rapports avant les tranches qu'ils déclenchent et tient compte des
  saisons et contraintes locales.
- Les lots Gestion/reporting, Communication, Inclusion et Suivi-évaluation existent et ont du temps
  et de l'argent.
- Le registre contient au moins 10 risques notés, avec prévention, atténuation, signal et
  responsable ; les 3 risques prioritaires sont repris dans le chronogramme (dates tampons, plan B).
- La procédure d'achats respecte les seuils de la convention ou les marque [À VÉRIFIER].
- Le calendrier de reporting reprend les dates exactes de la convention et fixe une date interne de
  bouclage à J-15.
- Les modèles de rapport et de compte rendu sont remplis au moins une fois à titre d'exemple.
- Le plan tient en un fichier lisible par un partenaire qui découvre le projet ; `projet/ETAT.md`
  est à jour.

## Erreurs fréquentes à éviter

- Planifier les activités sans regarder la trésorerie : une activité démarrée avant la tranche qui
  la finance crée un découvert.
- Oublier les délais administratifs (autorisations, visas, déclarations de droits d'auteur) et
  les saisons.
- Un chronogramme sans jour tampon : tout retard devient une crise.
- Deux « A » pour la même activité, ou aucun.
- Registre des risques décoratif : sans signal d'alerte ni responsable, il ne sert à rien.
- Payer des prestataires sans devis comparés ni contrat : dépenses contestées par le bailleur.
- Déposer les rapports à la date limite plutôt qu'en avance.
- Modifier le budget ou le calendrier approuvés sans accord écrit du bailleur.
- Traiter l'inclusion comme une phrase du dossier plutôt que comme des activités datées, chiffrées
  et mesurées.
- Reporter le suivi-évaluation à la fin : sans ligne de base, rien ne pourra être démontré.

## Références et sources à vérifier

- Convention de financement et lignes directrices : calendrier et format des rapports, seuils
  d'achats et de modification, règles de visibilité [À VÉRIFIER — source : convention signée ou
  site officiel du bailleur ; recherche « <bailleur> guide de gestion des subventions <année> »].
- Règles de passation applicables aux subventions de l'UE, de l'AFD, de la GIZ ou d'autres
  bailleurs institutionnels : [À VÉRIFIER — documents contractuels du programme].
- Autorités locales : procédure et délais pour l'occupation de l'espace public, la sécurité, le
  tournage [à vérifier auprès de la mairie, de la préfecture ou du ministère compétent].
- Société de gestion collective des droits d'auteur du pays : déclaration des programmes et
  redevances [à vérifier localement].
- Calendriers saisonniers (pluies, fêtes, scolaire, électoral) du pays d'exécution.
- Professionnels : expert-comptable (rapports financiers, certification), juriste (contrats
  artistes et prestataires, assurances), assureur (responsabilité civile, annulation), huissier si
  constat exigé, médecin ou service de secours pour les événements.

## Passage de relais

- Ensuite : `/icc:suivi-evaluation` (agent `icc-mise-en-oeuvre`) pour détailler indicateurs et
  collecte ; `/icc:propriete-intellectuelle` et `/icc:statut-juridique` (agent `icc-juridique`)
  pour les contrats artistes, prestataires et droits ; `/icc:pitch-dossier-presse` (agent
  `icc-communication`) pour le lot communication.
- Retour vers `/icc:plan-tresorerie` si le chronogramme déplace des dépenses ; vers
  `/icc:budget-cofinancement` si une activité n'a pas de ligne budgétaire.

Mise à jour obligatoire de `projet/ETAT.md` :

```markdown
# ÉTAT DU PROJET — <nom du projet>
Dernière mise à jour : AAAA-MM-JJ HH:MM
Agent actif : icc-mise-en-oeuvre | Skill en cours : /icc:plan-mise-en-oeuvre
## Résumé du projet (5 lignes max)
<inchangé>
## Étapes terminées (avec fichiers produits)
- Plan de mise en œuvre : projet/mise-en-oeuvre/plan.md (<n> lots, <n> activités, <n> risques, calendrier de reporting)
## Étape en cours (où on en est précisément)
<ex. : chronogramme validé ; procédure d'achats en attente des seuils de la convention>
## Prochaines étapes (ordre recommandé)
1. /icc:suivi-evaluation  2. /icc:propriete-intellectuelle (contrats)  3. /icc:pitch-dossier-presse
## Décisions prises / hypothèses à confirmer
- Date de l'événement <date> ; saison des pluies <mois> ; seuils d'achats [À VÉRIFIER]
## Questions en attente de réponse du promoteur
- <convention, noms des responsables, autorisations>
## Alertes (délais, pièces manquantes, professionnel humain requis)
- Rapport intermédiaire dû le <date> ; expert-comptable pour le volet financier ; juriste pour <n> contrats artistes
```
