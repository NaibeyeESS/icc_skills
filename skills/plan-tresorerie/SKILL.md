---
name: plan-tresorerie
description: Utiliser quand le promoteur doit prévoir mois par mois les entrées et sorties d'argent, anticiper les retards de versement des bailleurs, calculer le préfinancement ou le BFR ; mots-clés : « trésorerie », « cash », « quand l'argent arrive », « tranches », « avance », « découvert », « payer en attendant la subvention ».
---

# /icc:plan-tresorerie — Plan de trésorerie mensuel et couverture des creux

## Objectif

Construire un plan de trésorerie mensuel sur 12 à 36 mois qui montre, mois par mois, l'argent qui
entre (encaissements), l'argent qui sort (décaissements), le solde du mois et le cumul, afin de
repérer à l'avance les mois où le projet n'aura pas de quoi payer et de préparer les solutions.

Livrables :
- `projet/budget/tresorerie.md` — tableau mensuel, tranches de versement par bailleur, besoin de
  financement maximal, stratégies de couverture, seuils d'alerte, modèle de relance ;
- `projet/budget/tresorerie.csv` — mouvements mensuels au format lu par `scripts/tresorerie.py`.

Agent principal : `icc-budget`. Prérequis logique : un budget (`/icc:budget-cofinancement`).

Définitions utilisées (le promoteur doit pouvoir les réexpliquer) :
- *Budget* = combien coûte le projet et qui paie quoi, sur toute sa durée. *Trésorerie* = quand
  l'argent est réellement sur le compte et quand il en sort. Un projet peut être parfaitement
  financé au budget et pourtant incapable de payer ses artistes en novembre.
- *Tranche* = partie d'une subvention versée à un moment donné (souvent : une part à la signature
  de la convention, une part intermédiaire sur rapport, le solde après acceptation du rapport
  final). Les pourcentages varient selon les bailleurs et les conventions [À VÉRIFIER].
- *Décalage de versement* = délai entre le moment où la dépense doit être payée et celui où le
  bailleur verse l'argent correspondant ; c'est la cause principale des crises de trésorerie.
- *Préfinancement* = argent que vous devez avancer en attendant le bailleur.
- *BFR (besoin en fonds de roulement)* = somme qu'il faut immobiliser pour faire tourner
  l'activité entre le moment où l'on paie les fournisseurs et celui où les clients paient
  (notion surtout utile pour une activité marchande : mode, édition, ventes).
- *Besoin de financement maximal* = le point le plus bas du cumul de trésorerie ; c'est le montant
  minimal d'avance, de prêt relais ou d'acompte à sécuriser.

## Quand l'utiliser / ne pas l'utiliser

Utiliser quand :
- le budget est construit et un ou plusieurs financements sont demandés ou acquis ;
- le projet a une saisonnalité marquée (festival : 80 % des dépenses sur un mois) ;
- le promoteur craint de ne pas pouvoir payer une échéance avant le versement du bailleur ;
- une banque, une microfinance ou un partenaire demande un plan de trésorerie ;
- le projet est marchand (collection de mode, édition) et il faut estimer le BFR.

Ne pas l'utiliser pour :
- chiffrer les coûts du projet (c'est `/icc:budget-cofinancement`) ;
- établir des états financiers passés ou un bilan (expert-comptable) ;
- négocier un prêt : ce skill prépare le document, la décision d'emprunter et les conditions
  relèvent du promoteur avec un conseiller financier ou un expert-comptable.

## Prérequis

Lire si présents :
- `projet/ETAT.md` — reprise de session ;
- `projet/budget/budget.md` et `projet/budget/budget.csv` — rubriques, montants, sources, statuts ;
- `projet/fiche-projet.md` — durée, dates clés (événement, tournage, lancement de collection) ;
- `projet/financements/matching-<slug-appel>.md` — modalités de versement si déjà lues ;
- `projet/mise-en-oeuvre/plan.md` — chronogramme, si le plan de mise en œuvre existe déjà.

Informations nécessaires si absentes : mois de démarrage, dates des grandes dépenses (acomptes
fournisseurs, cachets, achats de matières), modalités de versement de chaque bailleur (lues dans la
convention ou les lignes directrices), trésorerie disponible au départ, recettes propres et leur
calendrier (pré-ventes, billetterie, ventes), capacité d'avance des partenaires.

Outil : `python3 -I skills/plan-tresorerie/scripts/tresorerie.py projet/budget/tresorerie.csv`
(options `--solde-initial`, `--seuil-alerte`, `--eur`). Fonctionne hors ligne.

## Procédure étape par étape

1. **Cadrer la période.** Lire `projet/ETAT.md` et le budget. Fixer le mois 1 (signature probable
   ou début réel des dépenses) et le dernier mois (versement du solde, souvent 2 à 6 mois après la
   fin des activités). Un projet de 12 mois d'activités donne souvent 15 à 18 mois de trésorerie.
2. **Recenser les encaissements et leurs dates.** Pour chaque source du plan de financement :
   tranches (%), condition de déclenchement (signature, rapport intermédiaire accepté, rapport
   final accepté, facture), délai habituel entre la condition et l'arrivée des fonds (ajouter le
   délai bancaire et le délai de traitement administratif). Tout pourcentage non lu dans la
   convention ou les lignes directrices est marqué [À VÉRIFIER]. Classer chaque encaissement :
   confirmé / probable / hypothèse.
3. **Répartir les décaissements par mois.** Partir des rubriques du budget et du chronogramme :
   acomptes (souvent 30–50 % à la commande), soldes à la livraison, salaires mensuels, dépenses
   concentrées sur l'événement. Exclure les contributions en nature (elles ne passent pas par le
   compte bancaire) ; inclure en revanche les dépenses financées par l'apport propre.
4. **Écrire le CSV** (gabarit (e)) et lancer le script. Lire : mois négatifs, besoin de financement
   maximal, mois sous le seuil d'alerte, poids des encaissements « hypothèse ».
5. **Tester un scénario prudent.** Relancer en décalant chaque tranche de bailleur de 2 mois et en
   retirant les encaissements « hypothèse ». Si le projet ne tient pas, le plan de couverture est
   obligatoire, pas optionnel.
6. **Construire le plan de couverture des creux** (gabarit (c)) : pour chaque mois négatif, choisir
   une ou plusieurs mesures : échelonner les dépenses, négocier un acompte plus élevé auprès du
   bailleur, avance d'un partenaire, pré-ventes, micro-crédit relais, report d'une activité non
   critique. Chiffrer le coût de chaque mesure (intérêts, remises consenties).
7. **Fixer les seuils d'alerte** (gabarit (d)) et la règle : qui regarde le compte, à quelle
   fréquence, quelle décision à chaque seuil.
8. **Préparer la relance de bailleur** (gabarit (f)) et noter dans le calendrier les dates de dépôt
   des rapports qui déclenchent les tranches : un rapport en retard, c'est une tranche en retard.
9. **Rédiger `projet/budget/tresorerie.md`** : hypothèses, tableau produit par le script, tableau
   des tranches, plan de couverture, seuils, modèle de relance.
10. **Signaler les professionnels requis** : expert-comptable pour un plan de trésorerie destiné à
    une banque ou une microfinance, et pour le calcul du BFR d'une activité marchande ; conseiller
    juridique avant de signer un prêt ou une avance avec contrepartie.
11. **Mettre à jour `projet/ETAT.md`** (voir « Passage de relais »).

Mode faible connectivité : tout se fait hors ligne ; sauvegarder le CSV à chaque mois renseigné ;
noter dans `projet/ETAT.md` le dernier mois saisi et le scénario en cours (de base / prudent).

## Questions à poser au promoteur

1. Quel mois démarrent réellement les dépenses, et de combien disposez-vous sur le compte à ce
   moment-là ?
2. Pour chaque bailleur : que disent la convention ou les lignes directrices sur les tranches et
   leurs conditions ? Avez-vous le document ?
3. Quelles dépenses exigent un acompte, de quel pourcentage et combien de temps avant ?
4. Quelles recettes propres attendez-vous, à quelles dates, et sur quelle base (pré-ventes
   passées, étude, intuition) ?
5. Qui pourrait avancer de l'argent ou accepter d'être payé après l'événement (prestataires
   fidèles, partenaires, membres du collectif) et à quelles conditions ?
6. Avez-vous accès à une banque ou une microfinance et à quel coût (taux, frais, garantie) ?
7. Quelles dépenses peuvent être décalées sans mettre le projet en danger ?
8. Qui tient le compte et avec quelle fréquence pouvez-vous consulter le solde ?
9. Pour une activité marchande : vos clients paient-ils à la commande ou à la livraison ? Vos
   fournisseurs de matières exigent-ils le paiement comptant ?

## Gabarits complets

### (a) Tableau mensuel de trésorerie

| Mois | Encaissements — [Bailleur 1] | Encaissements — [Bailleur 2] | Apport propre | Recettes propres | Total encaissements | Décaissements — RH | Décaissements — Technique / production | Décaissements — Communication | Décaissements — Logistique | Décaissements — Administration | Total décaissements | Solde du mois | Cumul | Situation |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| M1 [AAAA-MM] | | | | | | | | | | | | | | ok / sous seuil / NÉGATIF |
| M2 | | | | | | | | | | | | | | |
| … | | | | | | | | | | | | | | |
| M12 | | | | | | | | | | | | | | |
| **Total** | | | | | | | | | | | | | | |

Sous le tableau : besoin de financement maximal = [montant] FCFA ([montant] EUR) atteint en
[mois] ; mois négatifs : [liste] ; encaissements « hypothèse » : [montant] ([%] des entrées).
Le script produit automatiquement une version simplifiée de ce tableau (totaux par mois) et deux
tableaux croisés (encaissements par source, décaissements par rubrique).

### (b) Tableau des tranches de versement par bailleur

| Bailleur | Montant total FCFA | Tranche | % [À VÉRIFIER] | Montant FCFA | Condition de déclenchement | Délai habituel après la condition [À VÉRIFIER] | Mois probable | Statut |
|---|---:|---|---:|---:|---|---|---|---|
| [Bailleur principal] | | 1 | [ex. 40–80] | | signature de la convention + demande de versement + RIB | [4–8 semaines] | | probable |
| | | 2 | | | rapport intermédiaire narratif et financier accepté | [6–12 semaines] | | probable |
| | | 3 (solde) | | | rapport final accepté, justificatifs vérifiés | [8–16 semaines] | | probable |
| [Cofinanceur] | | 1 | | | lettre d'octroi signée | | | |
| | | 2 (solde) | | | rapport final | | | |
| Sponsor privé | | 1 | | | contrat signé | | | hypothèse |
| | | 2 | | | visibilité réalisée (preuves) | | | hypothèse |

Règles de lecture : les délais indiqués entre crochets sont des ordres de grandeur à remplacer par
ceux de la convention ; un bailleur verse rarement le jour de la signature ; le solde (souvent
10–30 %) arrive après la fin du projet : il doit être préfinancé.

### (c) Stratégies de couverture des creux

| Creux (mois, montant) | Mesure | Comment | Coût ou contrepartie | Délai de mise en place | Responsable | Décision |
|---|---|---|---|---|---|---|
| [M, montant] | Échelonner les dépenses | négocier 30 % d'acompte au lieu de 50 %, payer le solde après la tranche 2 | aucun, ou légère hausse de prix | 2 semaines | coordination | |
| | Négocier un acompte plus élevé avec le bailleur | demander une première tranche supérieure en expliquant la saisonnalité (certains bailleurs acceptent) [À VÉRIFIER] | aucun | à la signature | direction | |
| | Avance d'un partenaire | prêt sans intérêt d'un membre, d'une entreprise partenaire ou d'une collectivité, contrat écrit | reconnaissance de dette, visibilité | 3–4 semaines | direction | |
| | Pré-ventes / pré-commandes | billets « early bird » via Mobile Money, pré-commandes de la collection, souscription | remise 10–20 % | 2–3 mois avant | communication | |
| | Micro-crédit relais | prêt court terme adossé à la convention signée ; comparer 2 établissements | intérêts + frais [À VÉRIFIER localement], garantie | 4–8 semaines | direction + expert-comptable | |
| | Report d'une activité non critique | décaler une activité après la tranche suivante, avec accord du bailleur | risque sur le chronogramme | immédiat | coordination | |
| | Paiement différé négocié | fournisseurs réguliers payés à 30 ou 60 jours sur présentation de la convention | prix parfois plus élevé | 2 semaines | coordination | |
| | Réduction du périmètre | scénario bas écrit à l'avance : quelles dépenses tombent si la tranche n'arrive pas | perte de qualité ou d'audience | immédiat | direction | |

Toute avance ou prêt doit faire l'objet d'un écrit (montant, date, remboursement, intérêts) ; faire
relire par un conseiller juridique ou un expert-comptable avant signature.

### (d) Seuils d'alerte et règles de décision

| Niveau | Seuil (cumul prévisionnel du mois) | Signal | Décision | Qui | Quand |
|---|---|---|---|---|---|
| Vert | cumul > 1 mois de dépenses fixes | aucun | suivi mensuel | trésorier ou coordination | fin de mois |
| Orange | cumul entre 0 et 1 mois de dépenses fixes | fragile | geler les dépenses non engagées, relancer les bailleurs, activer une mesure de couverture | coordination + direction | sous 7 jours |
| Rouge | cumul prévisionnel négatif dans les 2 mois | danger | activer le plan de couverture, informer les partenaires, renégocier les échéances | direction | immédiat |
| Noir | impossibilité de payer une échéance due | crise | prioriser les paiements (salaires et obligations légales d'abord), informer le bailleur par écrit, réduire le périmètre | direction | immédiat |

Rituel : actualiser `tresorerie.csv` avec les montants réels chaque fin de mois ; comparer prévu /
réalisé ; faire glisser les tranches non reçues ; relancer le script.

### (e) Format CSV attendu par `scripts/tresorerie.py`

```csv
mois,type,libelle,montant_fcfa,source_ou_rubrique,statut
2027-01,E,Apport propre du collectif,1500000,Apport propre,confirmé
2027-03,E,Bailleur principal - tranche 1 (40 % à la signature),8000000,Bailleur principal,probable
2027-06,D,Acomptes artistes (30 %),3600000,Cachets artistes,
2027-11,D,Solde cachets artistes (70 %),8400000,Cachets artistes,
```

Règles : `type` = E (encaissement) ou D (décaissement) ; `mois` au format AAAA-MM ; `statut` des
encaissements = confirmé / probable / hypothèse ; un libellé contenant une virgule est entre
guillemets. Commande type :

```bash
python3 -I skills/plan-tresorerie/scripts/tresorerie.py projet/budget/tresorerie.csv \
  --solde-initial 0 --seuil-alerte 1000000
```

### (f) Modèle de relance d'un bailleur pour un versement en retard

Version française :

> Objet : Convention n° [référence] — demande de versement de la tranche [n°]
>
> Madame, Monsieur [nom du gestionnaire],
>
> Dans le cadre de la convention n° [référence] signée le [date] entre [bailleur] et [structure],
> la tranche [n°] d'un montant de [montant en devise du bailleur] ([montant FCFA]) devait être
> versée à la suite de [condition : signature / acceptation du rapport intermédiaire transmis le
> (date)]. À ce jour, notre compte [banque, référence RIB joint] n'a pas été crédité.
>
> Ce versement conditionne le paiement de [cachets des artistes / acompte technique] prévu le
> [date]. Afin de respecter le calendrier approuvé, nous vous serions reconnaissants de bien
> vouloir nous indiquer la date prévisionnelle du virement ou, le cas échéant, les pièces
> complémentaires attendues.
>
> Nous restons à votre disposition pour tout échange et vous remercions de votre appui.
>
> [Nom, fonction, structure, téléphone, courriel] — Pièces jointes : convention, demande de
> versement initiale, accusé de réception du rapport, RIB.

English version:

> Subject: Grant agreement no. [reference] — request for payment of instalment [no.]
>
> Dear [name],
>
> Under grant agreement no. [reference] signed on [date] between [funder] and [organisation],
> instalment [no.] of [amount in funder's currency] ([amount in FCFA]) was due following
> [condition: signature / approval of the interim report submitted on (date)]. As of today, our
> account [bank, bank details attached] has not been credited.
>
> This payment is required to meet [artists' fees / technical supplier deposit] due on [date]. In
> order to keep to the approved schedule, we would be grateful if you could indicate the expected
> transfer date or let us know of any additional documents required.
>
> We remain available for any further information and thank you for your continued support.
>
> [Name, position, organisation, phone, email] — Attachments: agreement, initial payment request,
> acknowledgement of report, bank details.

Rythme conseillé : première relance courtoise 2 semaines après la date attendue, seconde à 4
semaines avec copie au responsable de programme, puis appel téléphonique ; garder la trace de
chaque échange dans `projet/journal.md`.

### (g) Mini-gabarit BFR (activité marchande : mode, édition, artisanat)

| Élément | Hypothèse | Montant FCFA | Montant EUR |
|---|---|---:|---:|
| Stock de matières et produits finis moyen | [n] mois de ventes | | |
| Créances clients (ventes non encore payées) | [n] jours de délai de paiement | | |
| Dettes fournisseurs (achats non encore payés) | [n] jours de délai obtenu | | |
| **BFR = stock + créances − dettes fournisseurs** | | | |

Le BFR est à financer en permanence (fonds propres, prêt, acomptes clients, pré-commandes).
Un expert-comptable doit valider le calcul avant de le présenter à une banque ou un investisseur.

### (h) Exemple rempli — scénario 2 : festival de musiques urbaines et traditionnelles (1re édition)

Contexte : association de 12 musiciens (Afrique centrale), festival de 3 jours fin novembre 2027,
5 000 spectateurs visés, budget 1re édition environ 60 000 EUR dont 37 900 000 FCFA
(57 778 EUR) de dépenses monétaires (les contributions en nature sont exclues de la trésorerie).
Période : 15 mois (janvier 2027 → mars 2028, solde du bailleur principal après rapport final).

Tranches retenues comme hypothèses de travail (à remplacer par les termes des conventions) :

| Source | Total FCFA | Tranches et mois probables | Statut |
|---|---:|---|---|
| Bailleur principal (appel culture international) | 20 000 000 | 40 % mars 2027 (signature) ; 40 % octobre 2027 (rapport intermédiaire) ; 20 % mars 2028 (rapport final) [À VÉRIFIER] | probable |
| Ambassade — fonds d'appui culturel | 5 000 000 | 80 % mai 2027 ; 20 % février 2028 [À VÉRIFIER] | probable |
| Sponsors privés | 6 000 000 | 50 % septembre 2027 (contrats) ; 50 % décembre 2027 (après visibilité) | hypothèse |
| Billetterie | 5 400 000 | pré-ventes Mobile Money 1 400 000 en octobre ; 4 000 000 sur place en novembre | probable (scénario bas) |
| Apport propre du collectif | 1 500 000 | janvier 2027 | confirmé |

Sortie du script (extrait) :

| Mois | Encaissements | Décaissements | Solde du mois | Cumul | Situation |
|---|---:|---:|---:|---:|---|
| 2027-01 | 1 500 000 | 450 000 | 1 050 000 | 1 050 000 | ok |
| 2027-02 | 0 | 450 000 | -450 000 | 600 000 | sous seuil |
| 2027-03 | 8 000 000 | 450 000 | 7 550 000 | 8 150 000 | ok |
| 2027-05 | 4 000 000 | 950 000 | 3 050 000 | 10 750 000 | ok |
| 2027-06 | 0 | 4 050 000 | -4 050 000 | 6 700 000 | ok |
| 2027-09 | 3 000 000 | 3 950 000 | -950 000 | 4 850 000 | ok |
| 2027-10 | 9 400 000 | 2 950 000 | 6 450 000 | 11 300 000 | ok |
| 2027-11 | 4 000 000 | 20 700 000 | -16 700 000 | -5 400 000 | NÉGATIF |
| 2027-12 | 3 000 000 | 450 000 | 2 550 000 | -2 850 000 | NÉGATIF |
| 2028-01 | 0 | 1 250 000 | -1 250 000 | -4 100 000 | NÉGATIF |
| 2028-02 | 1 000 000 | 450 000 | 550 000 | -3 550 000 | NÉGATIF |
| 2028-03 | 4 000 000 | 450 000 | 3 550 000 | 0 | sous seuil |
| **Total** | **37 900 000** | **37 900 000** | **0** | **0** | |

Lecture : besoin de financement maximal de 5 400 000 FCFA (8 232 EUR) en novembre 2027, le mois
du festival, parce que le solde des cachets (8 400 000) et de la technique (4 000 000) tombe avant
le solde du bailleur et le second versement des sponsors. Quatre mois négatifs consécutifs. Les
encaissements « hypothèse » (sponsors, 6 000 000) représentent 16 % des entrées : sans eux, le
creux atteint environ 11 400 000 FCFA.

Plan de couverture retenu :

| Creux | Mesure | Effet | Coût |
|---|---|---|---|
| nov. 2027, 5 400 000 | Négocier le paiement de 30 % du solde technique à 30 jours (décembre) | -1 200 000 sur novembre | aucun |
| nov. 2027 | Pré-ventes renforcées (objectif 2 500 000 au lieu de 1 400 000, tarif réduit jusqu'au 31 octobre) | +1 100 000 en octobre | remise 15 % |
| nov. 2027 | Avance remboursable d'une entreprise partenaire (3 000 000, remboursée en mars 2028 au versement du solde) | couvre le reste | reconnaissance de dette, logo sur scène |
| déc. 2027 → févr. 2028 | Déposer le rapport final avant le 15 janvier pour avancer le solde ; relance à J+15 | solde en février plutôt qu'en mars | aucun |
| scénario sans sponsors | Scénario bas écrit : 2 scènes au lieu de 3 le premier soir, réduction de 2 000 000 de communication | creux ramené sous 6 000 000 | audience réduite |

Alertes consignées : seuil orange à 1 000 000 FCFA ; revue du compte chaque fin de mois ;
expert-comptable à consulter avant la signature de l'avance partenaire et pour le rapport
financier intermédiaire qui déclenche la tranche 2.

## Critères de qualité du livrable

- La période couvre jusqu'au dernier versement attendu, pas seulement la durée des activités.
- Chaque encaissement a une date probable, une condition de déclenchement et un statut
  (confirmé / probable / hypothèse) ; les pourcentages de tranches non lus dans une convention
  sont marqués [À VÉRIFIER].
- Les décaissements sont cohérents avec le budget (même total hors contributions en nature) et
  avec le chronogramme.
- Le besoin de financement maximal est identifié et chaque mois négatif a au moins une mesure de
  couverture chiffrée et datée.
- Un scénario prudent (tranches décalées de 2 mois, sans encaissements « hypothèse ») est présenté.
- Montants en FCFA et en devise du bailleur ; taux daté.
- Les seuils d'alerte et le responsable du suivi sont nommés.
- Le modèle de relance est prêt à envoyer (références de convention à compléter).
- Le CSV tourne sans alerte inexpliquée ; `projet/ETAT.md` est à jour.

## Erreurs fréquentes à éviter

- Supposer que le bailleur verse 100 % à la signature : lire la convention, prévoir le solde
  après le rapport final.
- Oublier le délai bancaire et administratif (semaines, parfois mois) entre « rapport accepté » et
  « argent sur le compte ».
- Compter la valorisation en nature comme de l'argent disponible.
- Inscrire les sponsors et la billetterie comme « confirmés » alors qu'aucun contrat n'est signé.
- Faire glisser une tranche dans le tableau sans faire glisser aussi la dépense qu'elle finance, ou
  l'inverse.
- Ne pas provisionner les frais de transfert international et les pertes de change sur les
  versements en devises.
- Déposer les rapports en retard : c'est le retard le plus fréquent et le plus évitable.
- Signer une avance ou un prêt sans écrit ni relecture par un professionnel.
- Payer en espèces sans reçu pour « aller plus vite » : la dépense deviendra inéligible et le
  bailleur retiendra le montant sur le solde.
- Confondre solde du mois et cumul : un mois positif peut laisser un cumul négatif.

## Références et sources à vérifier

- Conventions et lignes directrices des bailleurs visés : modalités de versement, délais,
  conditions des rapports [À VÉRIFIER — source : site officiel ou convention signée ; recherche
  « <bailleur> modalités de versement subvention <année> »].
- Conditions et taux des établissements de microfinance et banques locales : [À VÉRIFIER
  localement ; comparer au moins deux offres].
- Frais des plateformes de billetterie et de Mobile Money : grilles tarifaires des opérateurs
  [À VÉRIFIER].
- Parité 1 EUR = 655,957 FCFA (fixe) ; autres devises : BEAC ou BCEAO le jour du calcul.
- Professionnels : expert-comptable (plan de trésorerie pour banque, BFR, rapport financier
  intermédiaire), conseiller juridique (contrat d'avance ou de prêt), établissement financier.

## Passage de relais

- Ensuite : `/icc:plan-mise-en-oeuvre` (agent `icc-mise-en-oeuvre`) pour aligner le chronogramme
  sur les tranches et planifier les rapports qui les déclenchent ; `/icc:crowdfunding` (agent
  `icc-communication`) si une pré-vente ou une collecte doit combler un creux ; `/icc:statut-juridique`
  (agent `icc-juridique`) avant de contracter une avance ou un prêt.
- Retour vers `/icc:budget-cofinancement` si la trésorerie révèle un besoin de source
  supplémentaire ou un rééchelonnement des dépenses.

Mise à jour obligatoire de `projet/ETAT.md` :

```markdown
# ÉTAT DU PROJET — <nom du projet>
Dernière mise à jour : AAAA-MM-JJ HH:MM
Agent actif : icc-budget | Skill en cours : /icc:plan-tresorerie
## Résumé du projet (5 lignes max)
<inchangé>
## Étapes terminées (avec fichiers produits)
- Plan de trésorerie <n> mois : projet/budget/tresorerie.md, projet/budget/tresorerie.csv
  (besoin de financement maximal <FCFA> / <EUR> en <mois> ; <n> mois négatifs ; plan de couverture rédigé)
## Étape en cours (où on en est précisément)
<ex. : scénario prudent calculé ; en attente des modalités de versement officielles du bailleur principal>
## Prochaines étapes (ordre recommandé)
1. /icc:plan-mise-en-oeuvre  2. /icc:crowdfunding (si pré-ventes)  3. /icc:suivi-evaluation
## Décisions prises / hypothèses à confirmer
- Tranches <bailleur> : <x/y/z %> [À VÉRIFIER] ; billetterie scénario bas <montant> ; avance partenaire <montant> à formaliser
## Questions en attente de réponse du promoteur
- <convention à fournir, accord du partenaire pour l'avance, taux microfinance>
## Alertes (délais, pièces manquantes, professionnel humain requis)
- Rapport intermédiaire à déposer avant <date> pour déclencher la tranche 2 ; expert-comptable requis pour <rapport financier / contrat d'avance>
```
