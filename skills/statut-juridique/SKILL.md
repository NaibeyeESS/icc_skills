---
name: statut-juridique
description: Utiliser quand le promoteur demande quel statut juridique choisir ou comment se formaliser : association, entreprise (EI, entreprenant, SARL, SARLU, SAS), coopérative, GIE, portage par une structure existante, récépissé, RCCM, NIF, compte bancaire, OHADA, fiscalité ou comptabilité de base.
---

# /icc:statut-juridique — Choisir et mettre en place un statut juridique

## Objectif

Aider le promoteur d'un projet ICC (industries culturelles et créatives) à choisir, en connaissance
de cause, la forme juridique adaptée à son projet dans l'espace OHADA et selon la loi nationale sur
les associations, puis à la mettre en place concrètement (pièces, étapes, coûts à vérifier,
professionnels à solliciter). Le skill produit `projet/juridique/statut.md` : une grille de décision
notée, la forme retenue et ses raisons, la check-list de création, les documents-types à adapter
(statuts, procès-verbal d'assemblée générale constitutive, convention de portage) et le tableau des
pièces que les bailleurs exigent habituellement.

Termes à expliquer dès la première apparition :
- **OHADA** = Organisation pour l'harmonisation en Afrique du droit des affaires. Dix-sept États
  africains (dont le Tchad, le Cameroun, le Congo, la RCA, le Gabon, le Sénégal, la Côte d'Ivoire,
  le Burkina Faso, le Mali, le Bénin, le Togo, le Niger) appliquent des textes communs appelés
  « actes uniformes », directement applicables dans chaque pays. Les sociétés commerciales, les
  coopératives, le GIE et la comptabilité sont régis par ces actes uniformes. Les associations, elles,
  ne sont pas régies par l'OHADA mais par la loi nationale de chaque pays.
- **Personne morale** = entité juridique distincte des personnes qui la composent (association,
  société, coopérative). Elle peut signer des contrats, ouvrir un compte, recevoir une subvention en
  son nom propre. Une personne physique (vous-même) n'est pas une personne morale.
- **RCCM** = Registre du commerce et du crédit mobilier, registre OHADA où s'immatriculent les
  commerçants, les entreprenants et les sociétés.
- **NIF** = numéro d'identification fiscale (l'appellation varie selon le pays : NIF, IFU, NINEA,
  numéro de contribuable). Il est nécessaire pour facturer, être payé par un bailleur et payer ses
  impôts.
- **SYSCOHADA révisé** = système comptable commun de l'espace OHADA (acte uniforme relatif au
  droit comptable et à l'information financière). Il prévoit un système « normal » et un système
  « minimal de trésorerie » pour les très petites entités.

## Quand l'utiliser / ne pas l'utiliser

Utiliser quand :
- le promoteur n'a aucune structure et qu'un bailleur, un partenaire ou une banque exige une
  personne morale ;
- le promoteur hésite entre plusieurs formes (association ou entreprise, SARL ou coopérative) ;
- le promoteur veut se faire « porter » par une structure existante le temps d'un projet ;
- un dossier de financement demande des pièces juridiques qu'il ne sait pas identifier (récépissé,
  statuts, RCCM, attestation fiscale) ;
- un projet change d'échelle (atelier informel vers marque, collectif vers festival) et que la forme
  actuelle devient un frein.

Ne pas utiliser quand :
- la question porte sur les droits d'auteur, les marques, les contrats de cession ou d'artiste :
  renvoyer vers `/icc:propriete-intellectuelle` ;
- la question porte sur le budget, la trésorerie ou les dépenses éligibles : `/icc:budget-cofinancement`
  et `/icc:plan-tresorerie` ;
- le promoteur a déjà une structure adaptée et n'a besoin que de la liste des pièces : utiliser
  uniquement le gabarit G6 (tableau des pièces exigées par les bailleurs) et passer la main.

Ce skill ne remplace jamais un avocat, un notaire ou un expert-comptable. Il prépare le promoteur
à les rencontrer avec des questions précises et des documents déjà dégrossis, ce qui réduit le coût
et le délai de leur intervention.

## Prérequis

Fichiers `projet/` à lire s'ils existent (ne pas reposer les questions auxquelles ils répondent) :
- `projet/ETAT.md` : état de la session ; reprendre à l'étape indiquée.
- `projet/fiche-projet.md` : secteur, pays, nombre de porteurs, stade, objectif financier, type de
  recettes envisagées (billetterie, ventes, subventions).
- `projet/financements/cartographie.md` et `projet/financements/matching-*.md` : exigences des
  bailleurs ciblés en matière de personne morale, d'ancienneté et de pièces.
- `projet/budget/budget.md` : volume d'activité prévu (influence le régime fiscal et comptable).

Informations nécessaires si elles ne figurent pas dans ces fichiers : pays d'implantation (et
ville), nombre de personnes engagées dans le projet, existence ou non d'activités lucratives
(ventes, billetterie, prestations), horizon (projet unique ou activité durable), capacité à payer des
frais de création, existence d'une structure amie susceptible de porter le projet.

Faisable hors ligne : toute la procédure, sauf la vérification des textes nationaux, des coûts et des
délais, qui doit être marquée « À VÉRIFIER » et faite plus tard auprès du guichet compétent.

## Procédure étape par étape

1. **Lire l'état et la fiche-projet.** Si `projet/ETAT.md` existe, le lire et reprendre à l'étape en
   cours. Sinon, lire `projet/fiche-projet.md`. Si la fiche n'existe pas, proposer `/icc:fiche-projet`
   d'abord, ou recueillir le minimum (pays, secteur, porteurs, activités lucratives, bailleurs visés).
2. **Qualifier la situation actuelle.** Informel, association déclarée, entreprise, coopérative,
   portage en cours. Noter les pièces déjà détenues (récépissé, statuts, RCCM, NIF, compte bancaire).
3. **Identifier les contraintes des bailleurs visés.** Pour chaque bailleur de la cartographie, noter :
   personne morale exigée (oui/non/à vérifier), ancienneté minimale (à vérifier), forme acceptée
   (association seule, entreprise acceptée, coopérative acceptée), pièces demandées. Classer en
   éligible / non éligible / à vérifier en expliquant pourquoi.
4. **Poser les questions de la section « Questions à poser au promoteur »**, en trois ou quatre
   messages courts au maximum, et consigner les réponses.
5. **Remplir la grille de décision multicritères (G1)** avec le promoteur, en notant chaque forme
   de 0 à 3 par critère, en pondérant selon ses priorités. Expliquer chaque score en une phrase.
   Lire `references/formes-juridiques-ohada.md` pour détailler les formes envisagées.
6. **Formuler une recommandation argumentée**, avec une forme principale et, le cas échéant, une
   solution transitoire (ex. portage pendant 12 mois, puis création d'une association). Indiquer
   clairement les points qui exigent un avocat, un notaire ou un expert-comptable, et pourquoi.
7. **Produire la check-list de création (G5)** pour la forme retenue, avec les pièces à rassembler,
   le guichet compétent (guichet unique ou centre de formalités, tribunal, ministère de
   l'administration territoriale ou de l'intérieur pour les associations), les coûts et délais marqués
   « À VÉRIFIER ».
8. **Générer les documents-types** nécessaires : statuts (G2) et PV d'AG constitutive (G3) pour une
   association ; convention de portage (G4) si portage ; renvoyer au notaire ou à l'avocat pour les
   statuts de société (ne pas rédiger de statuts de SARL/SAS complets : le skill fournit la liste des
   clauses à discuter, pas l'acte).
9. **Remplir le tableau des pièces exigées par les bailleurs (G6)**, croisé avec les pièces détenues
   et les pièces à obtenir, avec responsable et échéance.
10. **Écrire `projet/juridique/statut.md`** en assemblant : situation actuelle, contraintes des
    bailleurs, grille notée, recommandation, check-list, documents-types adaptés, tableau des pièces,
    professionnels à consulter, questions en suspens. Sauvegarder au fur et à mesure (mode faible
    connectivité) : écrire le fichier dès l'étape 6, puis le compléter.
11. **Vérifier les critères de qualité** (section dédiée) et corriger.
12. **Mettre à jour `projet/ETAT.md`** (voir « Passage de relais »).

## Questions à poser au promoteur

Poser uniquement celles dont la réponse n'est pas déjà dans `projet/fiche-projet.md`.

1. Dans quel pays et quelle ville le projet sera-t-il domicilié ? (La loi sur les associations et le
   guichet de création varient selon le pays.)
2. Combien de personnes portent réellement le projet et prennent les décisions ? Sont-elles prêtes
   à figurer officiellement (bureau d'association, associés) ?
3. Le projet va-t-il vendre quelque chose (billets, œuvres, vêtements, prestations) ? Quelle part des
   recettes attendez-vous des ventes par rapport aux subventions ?
4. Voulez-vous pouvoir distribuer des bénéfices aux porteurs, ou tout réinvestir dans l'activité ?
   (Une association ne distribue jamais de bénéfices.)
5. Quels bailleurs visez-vous en priorité ? Exigent-ils une association, acceptent-ils une
   entreprise ? Ont-ils une exigence d'ancienneté ?
6. Envisagez-vous un prêt bancaire, un investisseur ou un partenaire commercial à l'export ?
7. Existe-t-il une structure amie (association, société de production, coopérative) qui pourrait
   porter le projet le temps d'un financement ? Quelle relation de confiance avez-vous avec elle ?
8. Quel budget et quel délai pouvez-vous consacrer à la création (frais de greffe, notaire,
   publication, timbre) ? [montants À VÉRIFIER auprès du guichet local]
9. Qui tiendra la comptabilité ? Avez-vous accès à un expert-comptable ou à un comptable ?
10. Souhaitez-vous que la gouvernance garantisse la place des femmes, des jeunes ou des personnes
    en situation de handicap (parité au bureau, sièges réservés, langues nationales en AG) ? Comment ?

## Gabarits complets

Tous les gabarits sont à copier dans `projet/juridique/statut.md` et à adapter. Les mentions entre
crochets sont à remplir. Les mentions « À VÉRIFIER » doivent rester visibles jusqu'à vérification
auprès de la source officielle ou d'un professionnel.

### G0 — Tableau comparatif synthétique des options

| Option | Personne morale ? | Qui est responsable des dettes ? | Accès subventions | Accès prêts / investisseurs | Coût et délai de création | Comptabilité | Quand la retenir |
|---|---|---|---|---|---|---|---|
| Rester informel | Non | Le promoteur, sur tous ses biens | Très limité : la plupart des bailleurs exigent une personne morale ; certains petits fonds acceptent une personne physique [À VÉRIFIER] | Microcrédit individuel seulement | Nul | Aucune obligation, mais aucune preuve d'activité | Tests, tout premiers pas, projet unique financé sur fonds propres |
| Association (loi nationale) | Oui, après récépissé | L'association ; les dirigeants en cas de faute de gestion | Large (forme la plus attendue par les bailleurs culturels) | Prêts possibles mais difficiles ; pas d'investisseurs en capital | Faible à modéré ; délai variable (récépissé parfois long) [À VÉRIFIER] | Minimale, mais comptes annuels exigés par les bailleurs | But non lucratif, collectif, projets subventionnés |
| Entreprenant (OHADA) | Non (personne physique déclarée) | Le promoteur | Faible pour les subventions culturelles ; éligible à certains programmes d'entrepreneuriat | Microfinance oui | Faible, déclaration simplifiée au RCCM | Très allégée | Artisan ou créateur seul, petit chiffre d'affaires, étape vers la société |
| Entreprise individuelle (EI) | Non | Le promoteur, sur tous ses biens | Faible pour les subventions ; éligible programmes d'accélération | Microfinance et banques (avec garanties) | Faible à modéré | Simplifiée selon le chiffre d'affaires | Créateur seul qui vend régulièrement |
| SARL / SARLU | Oui | Limitée aux apports | Programmes d'accélération, fonds d'investissement ICC ; subventions publiques souvent fermées aux sociétés [À VÉRIFIER] | Oui : banques, investisseurs, prêts d'honneur | Modéré ; statuts parfois notariés selon le pays [À VÉRIFIER] | SYSCOHADA, souvent avec comptable | Activité marchande durable, export, un ou plusieurs associés |
| SAS | Oui | Limitée aux apports | Comme la SARL | Très adaptée aux investisseurs (statuts souples) | Modéré à élevé ; conseil juridique indispensable | SYSCOHADA | Levée de fonds, associés aux rôles différenciés |
| Société coopérative (OHADA) | Oui | Selon la forme : limitée (COOP-CA) ou plus étendue (SCOOPS) [À VÉRIFIER] | Bonne : bailleurs sensibles à l'économie sociale et solidaire | Microfinance, banques de développement | Modéré ; immatriculation au registre des coopératives | SYSCOHADA adapté | Groupe de producteurs ou d'artisans qui mutualisent |
| GIE | Oui | Les membres, de façon solidaire et indéfinie | Faible | Moyen | Faible à modéré | Allégée | Structures existantes qui mutualisent un service (diffusion, achat) |
| Portage par un tiers | Celle du porteur | Le porteur, contractuellement partagée | Celle du porteur | Celle du porteur | Nul, mais frais de gestion (5 à 15 % en pratique, à négocier) | Tenue par le porteur | Projet unique, urgence d'un appel, phase transitoire |

Lignes dédiées genre et inclusion : quelle que soit la forme, prévoir dans les statuts ou le
règlement intérieur une clause de parité ou de représentation des femmes et des jeunes dans les
organes de décision, une clause sur l'accessibilité des réunions (lieu, langue nationale, horaires
compatibles avec les responsabilités familiales), et la possibilité de membres situés en zone rurale
de participer à distance ou par représentation.

### G1 — Grille de décision multicritères (à noter avec le promoteur)

Notation : 0 = très défavorable, 1 = défavorable, 2 = favorable, 3 = très favorable.
Pondération : 1 = peu important pour vous, 2 = important, 3 = décisif. Score = note × pondération.

| Critère | Pondération (1-3) | Informel | Association | EI / Entreprenant | SARL / SARLU | SAS | Coopérative | GIE | Portage |
|---|---|---|---|---|---|---|---|---|---|
| But lucratif compatible (distribution de bénéfices) | [ ] | 3 | 0 | 3 | 3 | 3 | 2 (ristournes limitées) | 1 | selon porteur |
| Adapté au nombre de porteurs | [ ] | 1 seul | 2 et plus (souvent minimum légal, À VÉRIFIER) | 1 seul | 1 (SARLU) ou plusieurs | 1 ou plusieurs | plusieurs (minimum légal, À VÉRIFIER) | 2 et plus | indifférent |
| Protection du patrimoine personnel | [ ] | 0 | 2 | 0 | 3 | 3 | 2 | 0 | 2 |
| Accès aux subventions culturelles | [ ] | 0 | 3 | 1 | 1 | 1 | 2 | 1 | 2 à 3 |
| Accès aux prêts et investisseurs | [ ] | 0 | 1 | 2 | 3 | 3 | 2 | 1 | 0 |
| Coût et délai de création | [ ] | 3 | 2 | 3 | 1 | 1 | 1 | 2 | 3 |
| Légèreté des obligations comptables | [ ] | 3 | 2 | 2 | 1 | 1 | 1 | 2 | 3 |
| Crédibilité à l'export et avec les partenaires privés | [ ] | 0 | 1 | 1 | 3 | 3 | 2 | 1 | 1 |
| Gouvernance inclusive facile à inscrire | [ ] | 0 | 3 | 1 | 2 | 3 | 3 | 2 | 1 |
| Autonomie de décision du promoteur | [ ] | 3 | 1 | 3 | 3 | 3 | 1 | 1 | 0 |
| **Total pondéré** | | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

Mode d'emploi : remplir la pondération avec le promoteur, calculer les totaux, puis discuter les deux
premières options. La grille éclaire, elle ne décide pas : un écart de moins de 10 % entre deux formes
doit déboucher sur une consultation d'avocat ou d'expert-comptable.

### G2 — Statuts-types d'association culturelle (à adapter au droit national)

Avertissement à recopier en tête du document : « Ce modèle est générique. La loi sur les
associations de [pays] impose des mentions, un nombre minimal de membres fondateurs, une procédure
de déclaration et parfois un contrôle préalable qui lui sont propres. Faites relire ces statuts par
un juriste ou par le service des associations compétent avant toute signature. »

```
STATUTS DE L'ASSOCIATION « [NOM] »

TITRE I — CONSTITUTION, DÉNOMINATION, OBJET, SIÈGE, DURÉE

Article 1 — Constitution et dénomination
Il est fondé entre les adhérents aux présents statuts une association à but non lucratif régie par
[loi nationale sur les associations de (pays), à citer par son intitulé exact — À VÉRIFIER],
dénommée « [NOM] », ci-après « l'Association ».

Article 2 — Objet
L'Association a pour objet : [ex. la création, la production et la diffusion d'œuvres
documentaires ; la formation de jeunes et de femmes aux métiers de l'image ; la promotion du
patrimoine culturel de (région)]. Elle peut réaliser toute activité accessoire, y compris des
activités économiques, dès lors qu'elles servent cet objet et que les excédents sont réinvestis.

Article 3 — Siège social
Le siège est fixé à [adresse complète, ville, pays]. Il peut être transféré par décision du
Conseil d'administration, ratifiée par la prochaine Assemblée générale.

Article 4 — Durée
L'Association est constituée pour une durée [indéterminée / de (n) années].

TITRE II — MEMBRES

Article 5 — Catégories de membres
L'Association se compose de membres fondateurs, de membres actifs et, le cas échéant, de membres
d'honneur et de membres bienfaiteurs. [Définir chaque catégorie et ses droits de vote.]

Article 6 — Admission
Toute personne physique ou morale partageant l'objet peut demander son admission. Le Conseil
d'administration statue. L'admission ne peut être refusée pour des motifs tenant au sexe, au
handicap, à l'origine, à la langue ou aux opinions.

Article 7 — Cotisation
Le montant de la cotisation annuelle est fixé par l'Assemblée générale. [Prévoir un tarif réduit ou
une dispense pour les étudiants, les personnes sans revenu et les membres en zone rurale.]

Article 8 — Perte de la qualité de membre
Par démission, décès, radiation pour non-paiement ou exclusion pour motif grave, après que
l'intéressé a été invité à présenter ses explications.

TITRE III — ORGANES

Article 9 — Assemblée générale
L'Assemblée générale réunit tous les membres à jour de cotisation. Elle se réunit au moins une fois
par an. Elle approuve le rapport moral et le rapport financier, vote le budget, élit le Conseil
d'administration, modifie les statuts et prononce la dissolution. Convocation [n] jours à l'avance
par tout moyen (courrier, courriel, message sur téléphone). Les débats peuvent se tenir en français
et en [langue(s) nationale(s)] ; une traduction est assurée si un membre le demande. Quorum :
[fraction] des membres ; décisions à la majorité [simple / des deux tiers pour les modifications
statutaires et la dissolution]. Le vote par procuration est admis dans la limite de [n] mandats par
membre présent, afin de permettre la participation des membres éloignés.

Article 10 — Conseil d'administration
L'Association est administrée par un Conseil de [n] à [n] membres élus pour [n] ans, rééligibles
[n] fois. Le Conseil comprend au moins [40 %] de femmes et au moins [un] membre de moins de 35
ans. Il se réunit au moins [n] fois par an. Il met en œuvre les décisions de l'Assemblée, arrête
les comptes, décide des recrutements et des partenariats.

Article 11 — Bureau
Le Conseil élit en son sein un Bureau composé au minimum d'un(e) Président(e), d'un(e)
Secrétaire général(e) et d'un(e) Trésorier(ère). Le ou la Président(e) représente l'Association
en justice et dans tous les actes de la vie civile, signe les conventions de financement et ordonne
les dépenses. Le ou la Trésorier(ère) tient la comptabilité et présente le rapport financier. Deux
signatures sont requises pour tout paiement supérieur à [montant à fixer].

Article 12 — Gratuité des mandats et conflits d'intérêts
Les mandats sont bénévoles. Les frais engagés pour l'Association sont remboursés sur justificatif.
Tout administrateur en situation de conflit d'intérêts (contrat avec l'Association, rémunération
comme prestataire ou artiste) le déclare et s'abstient de voter sur le point concerné.

TITRE IV — RESSOURCES ET COMPTABILITÉ

Article 13 — Ressources
Cotisations, subventions publiques et privées, dons et legs, mécénat, recettes d'activités
(billetterie, ventes, prestations) liées à l'objet, et toute ressource autorisée par la loi.

Article 14 — Comptabilité
Il est tenu une comptabilité faisant apparaître annuellement un compte de résultat et un bilan,
selon [le système minimal de trésorerie du SYSCOHADA ou les règles nationales applicables aux
associations — À VÉRIFIER]. Les comptes sont présentés à l'Assemblée générale et tenus à disposition
des bailleurs. Au-delà d'un seuil de ressources fixé par le Conseil, un expert-comptable est
mandaté.

Article 15 — Exercice social
L'exercice commence le 1er janvier et se termine le 31 décembre.

TITRE V — RÈGLEMENT INTÉRIEUR, MODIFICATION, DISSOLUTION

Article 16 — Règlement intérieur
Un règlement intérieur, adopté par le Conseil et ratifié par l'Assemblée, précise les modalités
d'application des présents statuts (fonctionnement, protection contre le harcèlement, accessibilité
des activités, utilisation des langues).

Article 17 — Modification des statuts
Par l'Assemblée générale extraordinaire, à la majorité des [deux tiers] des membres présents ou
représentés. Toute modification est déclarée à l'autorité compétente dans le délai légal.

Article 18 — Dissolution
Prononcée par l'Assemblée générale extraordinaire à la majorité des [deux tiers]. L'actif net est
dévolu à une association poursuivant un objet similaire ; il ne peut en aucun cas être partagé
entre les membres.

Fait à [ville], le [date], en [n] exemplaires originaux.
Signatures du/de la Président(e), du/de la Secrétaire général(e) et du/de la Trésorier(ère).
```

### G3 — Procès-verbal d'assemblée générale constitutive type

```
PROCÈS-VERBAL DE L'ASSEMBLÉE GÉNÉRALE CONSTITUTIVE
DE L'ASSOCIATION « [NOM] »

Le [date], à [heure], à [lieu, adresse], se sont réunies les personnes dont les noms figurent sur
la liste de présence annexée, à l'initiative de [nom(s) des initiateurs], en vue de constituer une
association à but non lucratif.

L'assemblée désigne comme président(e) de séance [nom] et comme secrétaire de séance [nom].

Ordre du jour :
1. Exposé du projet associatif et de ses objectifs ;
2. Examen et adoption des statuts ;
3. Élection des membres du Conseil d'administration ;
4. Élection du Bureau ;
5. Fixation de la cotisation annuelle ;
6. Pouvoirs pour les formalités de déclaration.

Première résolution — Après exposé du projet par [nom], l'assemblée décide de constituer
l'association « [NOM] » ayant pour objet [reprendre l'article 2 des statuts].
Adoptée à l'unanimité / par [n] voix pour, [n] contre, [n] abstentions.

Deuxième résolution — L'assemblée adopte, article par article puis dans son ensemble, le texte des
statuts annexé au présent procès-verbal.
Adoptée à [...].

Troisième résolution — Sont élus membres du Conseil d'administration pour [n] ans :
[nom, prénom, date et lieu de naissance, profession, adresse, nationalité — pour chacun].
L'assemblée constate que le Conseil compte [n] femmes sur [n] membres et [n] membre(s) de moins
de 35 ans, conformément à l'article 10 des statuts.

Quatrième résolution — Le Conseil, réuni séance tenante, a élu le Bureau suivant :
Président(e) : [nom] — Secrétaire général(e) : [nom] — Trésorier(ère) : [nom].

Cinquième résolution — La cotisation annuelle est fixée à [montant] FCFA, réduite à [montant]
FCFA pour [catégories].

Sixième résolution — Tous pouvoirs sont donnés à [nom, fonction] pour accomplir les formalités de
déclaration auprès de [autorité compétente — À VÉRIFIER selon le pays], obtenir le récépissé,
procéder aux publications légales éventuelles et ouvrir un compte bancaire au nom de l'association.

L'ordre du jour étant épuisé, la séance est levée à [heure].

Le/la Président(e) de séance            Le/la Secrétaire de séance
[signature]                              [signature]

Annexes : liste de présence signée ; statuts adoptés ; liste des membres du bureau avec copies des
pièces d'identité ; [autres pièces exigées localement — À VÉRIFIER].
```

### G4 — Convention de portage type

Le portage = une structure existante (le « porteur ») reçoit le financement et signe la convention
avec le bailleur à la place du promoteur (le « porté »), qui conduit le projet. Le bailleur doit en
être informé et l'accepter : certains refusent le portage ou exigent que le porteur soit lui-même
impliqué artistiquement. Faire relire la convention par un avocat si le montant porté dépasse ce que
le promoteur pourrait rembourser seul, ou si le bailleur est étranger.

```
CONVENTION DE PORTAGE DE PROJET

Entre : [dénomination du porteur], [forme juridique], dont le siège est à [adresse], immatriculée
sous le n° [récépissé ou RCCM], représentée par [nom, fonction], ci-après « le Porteur »,
Et : [nom, prénom] du/de la promoteur(trice), [profession], demeurant à [adresse], ci-après
« le Porté » (ou « la Portée »).

Article 1 — Objet
Le Porteur accepte de porter juridiquement et financièrement le projet « [titre] » (ci-après « le
Projet »), décrit en annexe 1, dans le cadre du financement sollicité ou obtenu auprès de [nom du
bailleur], pour un montant prévisionnel de [montant] FCFA ([équivalent devise du bailleur]).

Article 2 — Rôles
Le Porté assure la direction artistique et la conduite opérationnelle du Projet. Le Porteur signe
la convention de financement, reçoit les fonds sur son compte, exécute les paiements sur demande
écrite du Porté, tient la comptabilité du Projet et établit les rapports financiers destinés au
bailleur, avec la contribution du Porté pour les rapports narratifs.

Article 3 — Propriété intellectuelle
Le Porté demeure seul(e) titulaire des droits d'auteur sur les œuvres créées dans le cadre du
Projet, sauf stipulation contraire du bailleur. Le Porteur est mentionné comme [structure
d'accueil / producteur délégué — préciser] aux génériques et supports. Toute cession de droits
fait l'objet d'un contrat distinct (voir /icc:propriete-intellectuelle).

Article 4 — Frais de gestion
En contrepartie, le Porteur perçoit des frais de gestion de [x] % du montant effectivement reçu du
bailleur, dans la limite de ce que le bailleur accepte comme frais indirects. Aucun autre
prélèvement n'est effectué.

Article 5 — Comptabilité et traçabilité
Les fonds du Projet sont suivis sur un compte ou un sous-compte dédié. Le Porté a accès, sur
demande et sous [n] jours, aux relevés et pièces justificatives. Un état des dépenses est partagé
chaque mois.

Article 6 — Obligations du Porté
Fournir les pièces justificatives de toute dépense dans les [n] jours, respecter le budget validé
par le bailleur, informer le Porteur de tout événement affectant le Projet, respecter les règles de
visibilité du bailleur.

Article 7 — Responsabilité
Le Porteur est responsable vis-à-vis du bailleur. En cas de dépense inéligible ou de manquement
imputable au Porté, celui-ci s'engage à rembourser au Porteur les sommes correspondantes.
[Cette clause exige l'avis d'un avocat si le montant est important.]

Article 8 — Durée et fin
La convention prend effet à sa signature et s'achève à l'acceptation du rapport final par le
bailleur. Elle peut être résiliée d'un commun accord ou pour manquement grave, après mise en
demeure restée sans effet pendant [n] jours ; le bailleur en est alors informé.

Article 9 — Transfert
Si le Porté crée sa propre structure en cours de Projet, les parties étudient avec le bailleur le
transfert de la convention de financement.

Article 10 — Litiges
Règlement amiable, puis médiation, puis tribunaux de [ville].

Fait à [ville], le [date], en deux exemplaires.
Annexes : 1. Description et budget du Projet ; 2. Convention ou appel du bailleur ; 3. Calendrier.
```

### G5 — Check-list de création par forme

Les coûts et délais sont systématiquement « À VÉRIFIER » auprès du guichet compétent ; ne jamais
les chiffrer de mémoire.

| Étape | Association | Entreprenant / EI | SARL / SARLU / SAS | Coopérative | Responsable | Fait ? |
|---|---|---|---|---|---|---|
| Choix du nom et vérification de disponibilité | Auprès de l'autorité de déclaration | Au RCCM | Au RCCM (et OAPI si marque, voir /icc:propriete-intellectuelle) | Registre des sociétés coopératives | | |
| Rédaction des statuts | Modèle G2 adapté, relu par un juriste | Sans objet | Par notaire ou avocat ; acte notarié exigé dans plusieurs pays [À VÉRIFIER] | Statuts conformes à l'acte uniforme OHADA sur les coopératives, relus par un juriste | | |
| Assemblée constitutive et PV | Modèle G3 | Sans objet | PV de constitution, nomination du gérant/président | AG constitutive avec liste des coopérateurs | | |
| Dépôt du capital | Sans objet | Sans objet | Sur compte bancaire ou chez le notaire ; montant minimal selon la forme et le pays [À VÉRIFIER] | Parts sociales libérées selon les statuts | | |
| Déclaration / immatriculation | Dépôt du dossier à [ministère de l'intérieur, préfecture ou mairie — À VÉRIFIER], obtention du récépissé | Déclaration au RCCM (guichet unique ou greffe) | Immatriculation au RCCM via le centre de formalités ou le guichet unique | Immatriculation au registre des coopératives | | |
| Publication légale | Parfois exigée (journal officiel) [À VÉRIFIER] | Généralement non | Oui, dans un journal d'annonces légales | Selon le pays [À VÉRIFIER] | | |
| Identification fiscale (NIF ou équivalent) | Oui, nécessaire pour recevoir des fonds | Oui | Oui | Oui | | |
| Choix du régime fiscal | Non-lucratif, mais déclaration des activités lucratives accessoires ; TVA selon seuil [À VÉRIFIER avec expert-comptable] | Régime simplifié ou forfaitaire selon le chiffre d'affaires | IS, TVA, régime réel ou simplifié [expert-comptable indispensable] | Régime propre aux coopératives, exonérations éventuelles [À VÉRIFIER] | | |
| Ouverture du compte bancaire | Récépissé, statuts, PV, pièces d'identité du bureau | RCCM, NIF, pièce d'identité | RCCM, statuts, PV, NIF, pièce d'identité des dirigeants | Immatriculation, statuts, PV, NIF | | |
| Affiliation sociale (si salariés) | Caisse nationale de sécurité sociale | Idem si salariés | Idem | Idem | | |
| Registres obligatoires | Registre des membres, des délibérations, de comptabilité | Livre de recettes-dépenses | Registres légaux, comptabilité SYSCOHADA | Registre des coopérateurs, des délibérations | | |
| Mise en place de la gouvernance inclusive | Clause de parité au bureau, règlement intérieur anti-harcèlement | Sans objet | Pacte d'associés, charte | Clause de représentation des femmes et des jeunes au conseil | | |

### G6 — Tableau des pièces exigées par les bailleurs

Colonne « Statut » : détenue / à obtenir / à vérifier si exigée.

| Pièce | À quoi elle sert | Qui la délivre | Durée de validité habituelle | Statut | Échéance | Responsable |
|---|---|---|---|---|---|---|
| Statuts signés et datés | Prouve l'objet et la gouvernance | L'association ou le notaire | Permanente (version à jour) | | | |
| Récépissé de déclaration (association) ou extrait RCCM (société) | Prouve l'existence légale | Autorité de déclaration / greffe | Permanente ; extrait RCCM souvent exigé de moins de 3 mois [À VÉRIFIER] | | | |
| PV d'AG constitutive et PV de la dernière AG | Prouve la régularité de la gouvernance | L'organisation | Dernier exercice | | | |
| Liste des membres du bureau ou des dirigeants, avec pièces d'identité | Identifie les signataires | L'organisation | À jour | | | |
| Attestation d'identification fiscale (NIF ou équivalent) | Permet le paiement | Administration fiscale | Permanente | | | |
| Attestation de régularité fiscale ou de non-redevance | Prouve l'absence de dettes fiscales | Administration fiscale | Souvent 3 mois [À VÉRIFIER] | | | |
| Attestation de régularité sociale (si salariés) | Prouve le paiement des cotisations | Caisse de sécurité sociale | Souvent 3 mois [À VÉRIFIER] | | | |
| Relevé d'identité bancaire au nom de la structure | Permet le virement | Banque | Permanente | | | |
| Comptes annuels des 1 à 3 derniers exercices | Prouve la capacité de gestion | Trésorier / expert-comptable | Par exercice | | | |
| Rapport d'activité du dernier exercice | Prouve l'expérience | L'organisation | Par exercice | | | |
| Pouvoir ou délégation de signature | Si le signataire n'est pas le représentant légal | L'organisation | Par dossier | | | |
| Convention de portage (si portage) | Prouve l'accord entre porteur et porté | Les deux parties | Durée du projet | | | |
| Politique interne (protection des personnes, lutte contre le harcèlement, égalité) | Exigée par un nombre croissant de bailleurs internationaux [À VÉRIFIER] | L'organisation | À jour | | | |

### G7 — Exemple rempli, scénario 1 (réalisatrice tchadienne sans structure)

Situation : réalisatrice à N'Djamena, seule, un documentaire de 26 min, 25 000 € visés (environ
16,4 M FCFA), bailleurs ciblés : Fonds Image de la Francophonie (OIF), Institut français,
Goethe-Institut, fonds de festivals. Pas de producteur. Urgence : des appels se clôturent dans les
mois à venir [dates À VÉRIFIER sur les sites officiels].

Grille G1 (pondérations choisies par la promotrice : subventions 3, délai 3, autonomie 2,
protection du patrimoine 1, lucratif 1, autres 1) — extrait des totaux : Association 44,
Portage 41, SARLU 27, Informel 20.

Recommandation : solution en deux temps.
1. Immédiatement : portage par une société de production tchadienne existante (ou une association
   audiovisuelle déclarée) pour répondre aux appels en cours. Le Fonds Image de la Francophonie
   s'adresse en règle générale à des sociétés de production [À VÉRIFIER — site officiel de l'OIF] :
   le portage par un producteur est alors la voie la plus réaliste, et le producteur devient
   producteur délégué (clause à inscrire dans la convention G4 et dans un contrat de coproduction,
   voir /icc:propriete-intellectuelle). Frais de gestion à négocier ; la réalisatrice conserve ses
   droits d'auteur.
2. Dans les 12 mois : création d'une association de promotion du cinéma documentaire (minimum de
   membres fondateurs selon la loi tchadienne sur les associations [À VÉRIFIER]), avec un bureau
   majoritairement féminin, pour accéder aux fonds d'appui des ambassades et de l'Institut français,
   et pour porter les actions d'éducation à l'image auprès des communautés du lac Tchad.

Professionnels indispensables : un avocat pour relire la convention de portage et le contrat de
coproduction (partage de recettes, générique) ; pas de notaire à ce stade ; un comptable pour le
suivi du budget porté.

Pièces à réunir (G6) : pièces du porteur (récépissé ou RCCM, NIF, RIB, comptes), convention de
portage signée, CV de la réalisatrice, pièce d'identité.

### G8 — Exemple rempli, scénario 3 (créatrice de mode, atelier informel, 3 couturières)

Situation : Afrique de l'Ouest, atelier informel, 3 couturières salariées de fait, objectif :
marque exportable, e-commerce, salons. Bailleurs et financeurs ciblés : Afrique Créative,
Fondation Orange, microfinance, incubateurs, pré-ventes.

Grille G1 (pondérations : lucratif 3, prêts/investisseurs 3, crédibilité export 3, coût 2,
comptabilité 1) — totaux : SARLU 52, SARL 50, Coopérative 38, EI 36, Association 19.

Recommandation : SARLU (SARL à associée unique) au nom de la créatrice, avec un capital adapté à sa
capacité [minimum légal selon le pays À VÉRIFIER], éventuellement transformée en SARL
pluripersonnelle si une associée investit. La coopérative a été écartée car la créatrice veut
garder la direction artistique et la propriété de la marque ; elle reste pertinente si les
couturières deviennent co-entrepreneuses. L'EI a été écartée pour la responsabilité illimitée et la
faible crédibilité auprès des acheteurs étrangers.

Étapes : notaire ou avocat pour les statuts (acte notarié selon le pays [À VÉRIFIER]), dépôt du
capital, immatriculation RCCM au guichet unique, NIF, choix du régime fiscal avec un
expert-comptable (TVA à l'export, régime simplifié), ouverture de compte, contrats de travail des
trois couturières (régularisation sociale progressive, à budgéter), puis dépôt de marque OAPI (voir
/icc:propriete-intellectuelle).

Inclusion : la SARLU prévoit dans son règlement intérieur un plan de formation et de montée en
responsabilité des couturières (cheffe d'atelier), horaires compatibles avec la garde d'enfants,
et une part des achats de tissus réservée à des tisserandes rurales.

## Critères de qualité du livrable

- Chaque forme envisagée est notée dans la grille G1 avec une phrase d'explication par score.
- La recommandation est argumentée, propose une forme principale et, si nécessaire, une solution
  transitoire datée.
- Toute affirmation sur un minimum légal, un coût, un délai, un taux d'imposition ou une exonération
  porte la mention « À VÉRIFIER » et la source à consulter (guichet unique, administration fiscale,
  texte national cité par son intitulé).
- Les professionnels indispensables sont nommés avec la raison précise (ex. « notaire : acte notarié
  exigé pour les statuts de SARL dans ce pays », « expert-comptable : choix du régime de TVA »).
- Les contraintes des bailleurs ciblés sont classées éligible / non éligible / à vérifier.
- Les documents-types sont adaptés (nom, objet, pays, organes) et non laissés à l'état brut.
- Une rubrique genre et inclusion figure dans les statuts, le PV et la check-list.
- Le fichier `projet/juridique/statut.md` est autonome : un lecteur qui ne connaît pas le projet
  comprend la situation, la décision et les étapes suivantes.
- `projet/ETAT.md` est mis à jour avec les alertes (pièces manquantes, rendez-vous professionnel).

## Erreurs fréquentes à éviter

- Créer une association uniquement pour « avoir un statut » alors que le projet vend des produits et
  veut distribuer des revenus aux porteurs : risque de requalification fiscale et de blocage avec
  les banques.
- Créer une société pour un projet qui vivra uniquement de subventions culturelles : la plupart des
  fonds publics et des fondations ne financent pas de sociétés commerciales [À VÉRIFIER par
  bailleur].
- Oublier que l'association n'est pas régie par l'OHADA et que chaque pays a sa propre loi et son
  propre délai de récépissé ; déposer un dossier de financement avant d'avoir le récépissé.
- Signer un portage sans convention écrite, sans clause de propriété intellectuelle ni accès aux
  relevés ; ne pas informer le bailleur du portage.
- Inventer ou recopier des montants de capital minimum, de frais de greffe ou de taux d'impôt
  d'un autre pays ; les régimes varient à l'intérieur même de l'espace OHADA.
- Rédiger soi-même des statuts de SARL ou de SAS « pour économiser le notaire » là où l'acte notarié
  est obligatoire : l'immatriculation sera refusée.
- Négliger le NIF et l'attestation de régularité fiscale : sans eux, le bailleur ne peut pas virer
  les fonds.
- Choisir un bureau d'association composé des seuls proches sans compétence de gestion, ou sans
  aucune femme alors que le projet s'adresse aux femmes.
- Confondre entreprenant (statut OHADA simplifié, plafonds de chiffre d'affaires) et entreprise
  individuelle classique.
- Oublier d'annoncer dès le départ la question des cotisations sociales des personnes qui
  travaillent déjà (couturières, techniciens) : c'est un coût à budgéter, pas un détail.

## Références et sources à vérifier

- Actes uniformes OHADA, à consulter sur le site officiel de l'OHADA et les textes publiés au
  Journal officiel de l'OHADA : acte uniforme révisé relatif au droit des sociétés commerciales et
  du groupement d'intérêt économique ; acte uniforme relatif au droit des sociétés coopératives ;
  acte uniforme portant sur le droit commercial général (statut de l'entreprenant, RCCM) ; acte
  uniforme relatif au droit comptable et à l'information financière (SYSCOHADA révisé). Ne pas citer
  de numéro d'article sans l'avoir vérifié dans le texte.
- Loi nationale sur les associations du pays concerné (intitulé et autorité de déclaration À
  VÉRIFIER auprès du ministère de l'administration du territoire ou de l'intérieur).
- Code général des impôts du pays concerné (régimes simplifiés, TVA, exonérations culturelles
  éventuelles) : à vérifier avec un expert-comptable ; si WebSearch est disponible, rechercher
  « code général des impôts <pays> associations » et « guichet unique création entreprise <pays> ».
- Guichets uniques ou centres de formalités des entreprises du pays (coûts et délais).
- Lignes directrices des bailleurs ciblés pour les exigences de personne morale et d'ancienneté :
  vérifier sur le site officiel de chaque bailleur ; si WebSearch est disponible, lancer
  « <nom bailleur> appel à projets <année> éligibilité ».
- Fichier annexe de ce skill : `references/formes-juridiques-ohada.md` (détail de chaque forme).

## Passage de relais

- Si la forme retenue implique des contrats, une marque ou des droits d'auteur : `/icc:propriete-intellectuelle`
  (agent `icc-juridique`).
- Si les pièces juridiques sont réunies et que le promoteur doit candidater : `/icc:matching-appel`
  puis `/icc:note-conceptuelle` (agents `icc-financements`, `icc-redaction`).
- Si le choix dépend du volume d'activité ou du régime fiscal : `/icc:budget-cofinancement`
  (agent `icc-budget`) avant de trancher.
- Si le portage est retenu : prévenir `icc-redaction` que le porteur sera le demandeur officiel
  dans les dossiers.
- Retour à `icc-orchestrateur` pour la suite du parcours.

Mise à jour obligatoire de `projet/ETAT.md` en fin de procédure, en respectant sa structure :
- « Agent actif : icc-juridique | Skill en cours : /icc:statut-juridique » puis, une fois terminé,
  le skill suivant recommandé ;
- « Étapes terminées » : ajouter « Statut juridique : `projet/juridique/statut.md` (forme retenue :
  …) » ;
- « Décisions prises / hypothèses à confirmer » : forme retenue, solution transitoire, hypothèses
  sur les exigences des bailleurs ;
- « Questions en attente » : réponses manquantes du promoteur ;
- « Alertes » : pièces manquantes avec échéances, rendez-vous avocat / notaire / expert-comptable
  requis et pourquoi, délai d'obtention du récépissé ou du RCCM par rapport aux dates limites des
  appels [À VÉRIFIER].
