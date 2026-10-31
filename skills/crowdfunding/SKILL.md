---
name: crowdfunding
description: Utiliser quand un promoteur ICC veut lancer un financement participatif, une cagnotte, une collecte en ligne, une campagne de dons, de pré-commandes ou de pré-vente, demande quelle plateforme choisir (Ulule, KissKissBankBank, Kickstarter, Mobile Money), comment mobiliser la diaspora ou fixer contreparties et objectif.
---

# /icc:crowdfunding — Concevoir une campagne de financement participatif

## Objectif

Concevoir, pour un promoteur de projet culturel ou créatif en Afrique francophone, une campagne
de financement participatif (= collecte d'argent auprès d'un grand nombre de personnes, en
général via une plateforme en ligne) réaliste et tenable, sous l'une des trois formes :
- don avec contreparties (le contributeur donne et reçoit un remerciement ou un objet) ;
- pré-vente ou pré-commande (le contributeur achète à l'avance un produit ou un billet) ;
- prêt participatif (le contributeur prête et est remboursé ; forme rare et encadrée, qui exige
  une structure formalisée et un conseil juridique).

Le skill produit un plan complet dans `projet/communication/crowdfunding.md` : choix de
plateforme adapté aux contraintes locales (compte bancaire, vérification d'identité, frais,
devise), objectif financier calculé par la méthode des cercles, paliers et contreparties chiffrées
avec coût de revient et logistique d'envoi depuis l'Afrique, calendrier de J-30 à J+15, plan de
communication avec messages-types (WhatsApp, Facebook, Instagram, e-mail, presse locale, diaspora),
script de vidéo de 90 secondes, budget de campagne, risques et obligations.

Agent principal : `icc-communication`. Le skill ne promet jamais l'atteinte de l'objectif : il
parle de taux de conversion prudents et de promesses tenables.

## Quand l'utiliser / ne pas l'utiliser

Utiliser ce skill quand :
- la cartographie (`/icc:cartographie-bailleurs`) a identifié le crowdfunding comme source
  complémentaire ou comme preuve d'adhésion du public à montrer aux bailleurs ;
- le projet a un produit ou une expérience à pré-vendre (collection de mode, album, livre, billets
  de festival, projection) ;
- le promoteur dispose d'un réseau mobilisable (proches, communauté, diaspora, publics déjà
  acquis) et d'un contenu visuel (photos, teaser) ;
- un bailleur demande une part de cofinancement (= part du budget que vous apportez vous-même ou
  via d'autres sources) et la collecte peut en constituer une partie.

Ne pas l'utiliser quand :
- le projet n'a ni réseau mobilisable ni contenu à montrer : construire d'abord la présence en ligne
  et le pitch (`/icc:pitch-dossier-presse`) ;
- le besoin dépasse très largement ce qu'un réseau peut donner (par exemple la totalité d'un budget
  de festival) : utiliser la collecte comme complément dans un plan combiné
  (`/icc:budget-cofinancement`) ;
- il s'agit d'une levée de fonds en capital auprès d'investisseurs : relever de `icc-juridique` et
  `icc-budget`, avec un avocat et un expert-comptable ;
- aucune personne de confiance ne peut ouvrir de compte éligible à une plateforme et aucun canal
  local n'est accessible : traiter d'abord la question bancaire avec `/icc:statut-juridique`.

## Prérequis

Fichiers du dossier `projet/` à lire s'ils existent :
- `projet/ETAT.md` — à lire en premier, reprendre à l'étape indiquée ;
- `projet/fiche-projet.md` — projet, publics, équipe, réseaux existants ;
- `projet/financements/cartographie.md` — place du crowdfunding dans le plan de financement
  combiné et montant visé ;
- `projet/budget/budget.md` — coût des produits ou prestations à pré-vendre ;
- `projet/juridique/statut.md` — statut, compte bancaire, pays du compte ;
- `projet/communication/pitch.md` et `projet/communication/dossier-presse.md` — messages et
  visuels réutilisables.

Informations nécessaires (à demander si absentes) : montant visé par la collecte (FCFA et EUR,
parité fixe 1 EUR = 655,957 XAF/XOF) ; type de campagne (don, pré-vente, prêt) ; taille des
cercles de contacts ; comptes bancaires et Mobile Money disponibles (pays, titulaire) ; produits
ou contreparties possibles et leur coût ; capacité d'envoi postal ; contenu visuel existant ;
présence d'un relais dans la diaspora.

## Procédure étape par étape

Reprenable à toute étape ; noter l'étape atteinte dans `projet/ETAT.md`. Les étapes 2 à 8 sont
réalisables hors ligne ; l'étape 1 (vérification des conditions des plateformes) et le lancement
exigent la connexion.

### Étape 1 — Choisir le type de campagne et la plateforme
Déterminer le type (don avec contreparties, pré-vente, prêt) à partir de ce que le projet peut
livrer. Puis remplir le gabarit A (comparatif de plateformes) en vérifiant, pour chaque option, les
contraintes réelles (toutes marquées [À VÉRIFIER — source : site officiel de la plateforme],
car elles changent) :
- pays du compte bancaire exigé pour recevoir les fonds (les plateformes internationales exigent
  en général un compte dans un pays de leur liste, souvent en Europe ou en Amérique du Nord) ;
- vérification d'identité du porteur (KYC = « know your customer », contrôle d'identité et
  d'adresse exigé par la réglementation financière) ;
- frais de plateforme et de paiement, devise de collecte et de versement, délai de versement ;
- règle « tout ou rien » (l'argent n'est versé que si l'objectif est atteint) ou « collecte
  flexible » (tout ce qui est collecté est versé) ;
- moyens de paiement acceptés par les contributeurs : carte bancaire, Mobile Money, virement.
Trois montages fréquents : (1) plateforme internationale avec un relais de confiance dans la
diaspora, titulaire du compte, lié au promoteur par une convention écrite (juriste recommandé) ;
(2) plateforme ou canal local en FCFA (Mobile Money, plateforme africaine), avec moins de
visibilité pour la diaspora ; (3) campagne hybride : plateforme internationale pour la diaspora et
numéro Mobile Money dédié pour le public local, avec un seul compteur public mis à jour
quotidiennement. Si WebSearch est disponible : « <plateforme> pays éligibles compte bancaire »,
« <plateforme> frais <année> », « crowdfunding <pays> Mobile Money plateforme ».

### Étape 2 — Fixer l'objectif financier (méthode des cercles)
Remplir le gabarit B. Dénombrer honnêtement les contacts par cercle : cercle 1 = famille, amis
proches, équipe (ils donnent presque à coup sûr) ; cercle 2 = connaissances, collègues, communauté
artistique, publics déjà acquis, diaspora connue ; cercle 3 = inconnus touchés par la presse, les
partages et la plateforme. Appliquer des taux de conversion prudents (hypothèses de travail à
ajuster au premier retour d'expérience) : cercle 1 : 30 à 50 % ; cercle 2 : 5 à 10 % ; cercle 3 :
1 à 2 %. Multiplier par un don moyen prudent par cercle. L'objectif public affiché doit être
atteignable avec les cercles 1 et 2 seuls : une campagne qui dépasse 30 % dans les 72 premières
heures a de bien meilleures chances ; si le calcul ne couvre pas le besoin, réduire l'objectif
public et prévoir des paliers de dépassement (« objectifs étendus »).

### Étape 3 — Concevoir paliers et contreparties
Remplir le gabarit C : pour chaque palier, la contrepartie, son coût de revient (fabrication,
emballage), le coût d'envoi (local, régional, international — se renseigner auprès de la poste et
des transporteurs ; les envois internationaux depuis l'Afrique sont coûteux et lents, parfois
taxés à l'arrivée), la marge nette et le nombre maximal disponible. Règles : au moins une
contrepartie immatérielle (remerciement vidéo, nom au générique, accès numérique) pour les
contributeurs lointains ; au moins un palier bas accessible au public local ; un palier
« entreprise ou mécène » ; pas de contrepartie dont le coût total dépasse 30 % du palier ; pas de
contrepartie que l'équipe ne sait pas produire dans le délai annoncé. Intégrer une contrepartie
d'inclusion (par exemple : un palier « offrir une place à un jeune ou à une personne en situation
de handicap », une version accessible du produit) et des contreparties ancrées dans les langues
nationales (dédicace, chanson, texte).

### Étape 4 — Calendrier J-30 à J+15
Remplir le gabarit D. Avant le lancement : constitution de la liste de contacts par cercle (avec
consentement, respect de la vie privée), production de la vidéo et des visuels, pré-engagement du
cercle 1 (ils donnent dans les premières 24 heures), contact presse locale, test de la page.
Pendant : lancement un jour et une heure où le réseau est disponible (éviter les coupures connues),
relances hebdomadaires avec contenu nouveau (coulisses, témoignages, portraits de l'équipe),
événement physique à mi-parcours (projection, défilé, concert, atelier ouvert), dernier sprint
sur 72 heures. Après : remerciements nominatifs, bilan public, calendrier de livraison des
contreparties, rapport aux contributeurs tous les mois jusqu'à livraison.

### Étape 5 — Plan de communication et messages-types
Remplir le gabarit E en adaptant les messages-types au ton du projet. Prévoir des versions en
français et dans la ou les langues nationales du public visé (traduction par un membre de
l'équipe), et une version anglaise courte si la diaspora est anglophone. Désigner un responsable
par canal et un rythme (WhatsApp : individuel puis statuts ; Facebook et Instagram : trois
publications par semaine ; e-mail : lancement, mi-parcours, dernier sprint, remerciement ; presse
locale : communiqué à J-7 et à mi-parcours ; radio communautaire : interview). Fixer une règle :
jamais d'ajout de personnes à un groupe sans leur accord ; privilégier les messages individuels.

### Étape 6 — Script de la vidéo de campagne (90 secondes)
Remplir le gabarit F. Tournage possible au téléphone ; sous-titres obligatoires (beaucoup regardent
sans le son, et c'est une mesure d'accessibilité) ; langue nationale avec sous-titres français,
ou l'inverse, selon le public visé ; l'équipe apparaît à l'image ; les femmes et les jeunes de
l'équipe sont visibles si c'est la réalité du projet.

### Étape 7 — Budget de campagne et objectif brut
Remplir le gabarit G : frais de plateforme et de paiement [À VÉRIFIER], coût total des
contreparties et de leur envoi (issu du gabarit C), communication (impressions, événement,
données mobiles), imprévus. Calculer l'objectif brut nécessaire pour qu'il reste le montant net
visé : objectif brut = (montant net visé + coût des contreparties + communication + imprévus) /
(1 − taux de frais). Afficher en FCFA et en EUR.

### Étape 8 — Risques, obligations et professionnels
Remplir le gabarit H. Points impératifs : la fiscalité des dons et des pré-ventes (TVA, impôt sur
les revenus ou les sociétés, émission de reçus) dépend du pays et du statut ; renvoyer à un
expert-comptable avant le lancement, et à un avocat ou juriste pour la convention avec le
titulaire du compte et pour toute campagne de prêt. Les promesses faites publiquement (dates de
livraison, contenu des contreparties, usage des fonds) engagent la réputation du promoteur ; ne
promettre que ce qui est certain. Prévoir le scénario d'échec (campagne « tout ou rien » non
atteinte) et le scénario de dépassement.

### Étape 9 — Livrable et mise à jour de l'état
Assembler les gabarits A à H dans `projet/communication/crowdfunding.md`. Relire avec la grille de
qualité. Mettre à jour `projet/ETAT.md` (voir « Passage de relais »).

## Questions à poser au promoteur

Poser uniquement celles dont la réponse ne figure pas dans les fichiers `projet/`. Regrouper en un
seul message.

1. Quel montant net voulez-vous obtenir grâce à la collecte, en FCFA ? À quoi servira-t-il
   précisément ?
2. Qu'avez-vous à proposer en échange : un produit à pré-vendre, des billets, des remerciements,
   une expérience ? Quand pourrez-vous le livrer ?
3. Combien de personnes pouvez-vous contacter personnellement (famille, amis, équipe) ? Combien de
   connaissances et de contacts professionnels ? Avez-vous une liste de diffusion, une page ou un
   compte avec des abonnés actifs (combien) ?
4. Avez-vous des proches ou des partenaires dans la diaspora prêts à relayer, voire à porter le
   compte de la campagne ? Dans quel pays ?
5. Quel compte bancaire ou Mobile Money pourrait recevoir les fonds ? À quel nom ? Dans quel pays ?
6. Avez-vous déjà des photos, un teaser, des témoignages de votre public ?
7. Pouvez-vous expédier des objets : localement, dans la sous-région, en Europe ? À quel coût et
   avec quel transporteur ?
8. Quelles langues parle votre public cible ? La campagne doit-elle exister en langue nationale ?
9. Quel événement physique pourriez-vous organiser pendant la campagne (projection, défilé,
   concert, atelier) ?
10. Votre projet implique-t-il des femmes, des jeunes, des personnes en situation de handicap, des
    zones rurales ? Comment la campagne peut-elle le montrer concrètement ?
11. Avez-vous un expert-comptable ou un juriste à qui poser les questions de fiscalité et de
    convention ?

## Gabarits complets

Copier les gabarits A à H dans `projet/communication/crowdfunding.md`, dans l'ordre.

### Gabarit A — Comparatif de plateformes et choix

```markdown
# Campagne de financement participatif — <nom du projet>
Date : AAAA-MM-JJ | Rédigé avec /icc:crowdfunding | Agent : icc-communication
Type de campagne : <don avec contreparties / pré-vente / prêt participatif>

## A. Comparatif de plateformes

| Option | Pays du compte bancaire exigé | Vérification d'identité (KYC) | Frais plateforme + paiement | Devise collecte / versement | Règle (tout ou rien / flexible) | Paiements acceptés (carte, Mobile Money) | Visibilité diaspora | Visibilité locale | Source officielle | Verdict pour nous |
|---|---|---|---|---|---|---|---|---|---|---|
| Ulule | [À VÉRIFIER — source : site officiel ulule.com] | [À VÉRIFIER] | [À VÉRIFIER] | [À VÉRIFIER] | [À VÉRIFIER] | [À VÉRIFIER] | forte en francophonie | faible | ulule.com | <éligible via relais diaspora / non éligible / à vérifier> |
| KissKissBankBank | [À VÉRIFIER — source : kisskissbankbank.com] | [À VÉRIFIER] | [À VÉRIFIER] | [À VÉRIFIER] | [À VÉRIFIER] | [À VÉRIFIER] | forte en francophonie | faible | kisskissbankbank.com | |
| Kickstarter | [À VÉRIFIER — source : kickstarter.com] | [À VÉRIFIER] | [À VÉRIFIER] | [À VÉRIFIER] | [À VÉRIFIER] | [À VÉRIFIER] | forte, anglophone | très faible | kickstarter.com | |
| GoFundMe (don simple) | [À VÉRIFIER — source : gofundme.com] | [À VÉRIFIER] | [À VÉRIFIER] | [À VÉRIFIER] | flexible | [À VÉRIFIER] | moyenne | faible | gofundme.com | |
| Plateforme africaine (Afrikwity, Fiatope, autre à identifier) | [À VÉRIFIER — source : site officiel] | [À VÉRIFIER] | [À VÉRIFIER] | FCFA [À VÉRIFIER] | [À VÉRIFIER] | Mobile Money [À VÉRIFIER] | faible | moyenne | <domaine officiel> | |
| Collecte directe Mobile Money (numéro dédié) + page web ou réseaux sociaux | compte Mobile Money au nom de <titulaire>, <pays> | selon opérateur | frais de retrait [À VÉRIFIER auprès de l'opérateur] | FCFA | flexible | Mobile Money | très faible | forte | opérateur | |

### Choix retenu
Montage : <plateforme internationale via relais diaspora / canal local / hybride>.
Titulaire du compte : <nom, lien avec le projet, pays>. Convention écrite entre le titulaire et le
promoteur : <à rédiger avec un juriste — obligatoire si le titulaire n'est pas la structure>.
Compteur unique publié : <où et à quelle fréquence>.
```

### Gabarit B — Objectif financier par la méthode des cercles

```markdown
## B. Objectif financier

| Cercle | Qui | Nombre de contacts réels | Taux de conversion prudent | Contributeurs attendus | Don moyen prudent (FCFA) | Montant attendu (FCFA) | Montant (EUR) |
|---|---|---|---|---|---|---|---|
| 1 — proches | famille, amis, équipe | <n> | 40 % (30 à 50 %) | <n> | <montant> | <montant> | <montant> |
| 2 — réseau | connaissances, collègues, communauté, publics acquis, diaspora connue | <n> | 7 % (5 à 10 %) | <n> | <montant> | <montant> | <montant> |
| 3 — inconnus | presse, partages, plateforme | <n estimé> | 1,5 % (1 à 2 %) | <n> | <montant> | <montant> | <montant> |
| **Total attendu** | | | | **<n>** | | **<montant>** | **<montant>** |

Objectif public affiché (atteignable avec cercles 1 + 2) : <montant> FCFA (≈ <montant> EUR).
Objectifs étendus : palier 2 à <montant> (<ce que cela permet>), palier 3 à <montant>.
Hypothèses à confirmer après les 72 premières heures : <taux réels observés>.
```

### Gabarit C — Paliers et contreparties

```markdown
## C. Paliers et contreparties

| Palier (FCFA / EUR) | Contrepartie | Public visé | Coût de revient unitaire (FCFA) | Coût d'envoi (local / sous-région / international) | Marge nette par contribution (FCFA) | Quantité max | Délai de livraison promis | Responsable |
|---|---|---|---|---|---|---|---|---|
| 3 000 / ≈ 4,6 | Remerciement nominatif en ligne + accès numérique (photo, extrait) | public local, jeunes | 0 | 0 | 3 000 | illimitée | J+15 | <nom> |
| 10 000 / ≈ 15 | Nom au générique ou sur le mur des contributeurs + carte postale numérique | diaspora, réseau | 0 | 0 | 10 000 | illimitée | J+30 | |
| 25 000 / ≈ 38 | <produit ou billet> | public local | <coût> | <local> | <marge> | <n> | <date> | |
| 50 000 / ≈ 76 | <produit + visite d'atelier ou rencontre> | réseau, diaspora en visite | <coût> | <coût> | <marge> | <n> | <date> | |
| 100 000 / ≈ 152 | <produit personnalisé + remerciement vidéo en langue nationale> | diaspora | <coût> | <international> | <marge> | <n> | <date> | |
| 150 000 / ≈ 229 | Palier solidaire : offrir <n> places ou <n> produits à des jeunes ou à des personnes en situation de handicap identifiés avec une association partenaire | mécènes individuels | <coût> | 0 | <marge> | <n> | <date> | |
| 500 000 / ≈ 762 | Palier entreprise ou mécène : logo, remerciement public, invitation | entreprises locales, diaspora entrepreneuriale | <coût> | 0 | <marge> | <n> | <date> | |

Contrôles : coût total (revient + envoi) ≤ 30 % du palier ; toute contrepartie physique a un
transporteur identifié et un tarif vérifié ; au moins une contrepartie immatérielle par tranche.
```

### Gabarit D — Calendrier J-30 à J+15

```markdown
## D. Calendrier de campagne

| Jour | Action | Responsable | Canal | Fait |
|---|---|---|---|---|
| J-30 | Validation du montage (plateforme, compte, convention), ouverture du compte, lancement de la vérification d'identité | promoteur, titulaire, juriste | | |
| J-28 | Liste de contacts par cercle (avec consentement), tableur de suivi | équipe | hors ligne | |
| J-25 | Tournage de la vidéo (90 s) et des photos ; rédaction des textes de la page | équipe | hors ligne | |
| J-20 | Montage vidéo, sous-titres ; devis contreparties et envois confirmés | équipe, fournisseurs | | |
| J-15 | Page de campagne rédigée et relue ; version langue nationale ; test par 3 personnes extérieures | équipe | | |
| J-10 | Pré-engagement du cercle 1 : chacun promet de contribuer dans les 24 h du lancement | promoteur | WhatsApp individuel, appels | |
| J-7 | Communiqué à la presse locale et aux radios ; prise de rendez-vous interviews | responsable com | e-mail, dépôt physique | |
| J-3 | Programmation des publications de la semaine 1 ; vérification de la connexion et du plan B (données mobiles) | responsable com | | |
| J-1 | Rappel du cercle 1 ; brouillons prêts | promoteur | WhatsApp | |
| J0 | Lancement (heure de forte disponibilité du réseau) ; messages individuels au cercle 1 ; publication | tous | tous canaux | |
| J+1 à J+3 | Objectif : 30 % de l'objectif public ; remerciement public de chaque contributeur ; messages au cercle 2 | tous | WhatsApp, réseaux | |
| J+7 | Première actualité (coulisses) ; relance cercle 2 ; article ou interview presse | responsable com | | |
| J+14 | Événement physique de mi-parcours ; actualité ; relance diaspora | équipe | événement, réseaux | |
| J+21 | Actualité : témoignage de bénéficiaires ou partenaires ; relance e-mail | | | |
| J+27 à J+30 | Dernier sprint 72 h : compte à rebours, messages individuels aux indécis, palier étendu | tous | tous | |
| J+30 | Clôture ; message de remerciement général ; bilan chiffré public | promoteur | | |
| J+31 à J+45 | Remerciements nominatifs ; collecte des adresses de livraison ; commande des contreparties ; première actualité post-campagne | équipe | | |
| mensuel jusqu'à livraison | Rapport d'avancement aux contributeurs | promoteur | e-mail, plateforme | |
```

### Gabarit E — Plan de communication et messages-types

```markdown
## E. Plan de communication

| Canal | Cible | Responsable | Rythme | Contenu principal | Langue(s) |
|---|---|---|---|---|---|
| WhatsApp (messages individuels, puis statuts) | cercles 1 et 2 | promoteur | J0, J+7, J+14, J+27 | message personnel, lien, visuel | FR + langue nationale |
| Facebook | public local, diaspora | responsable com | 3 publications / semaine | vidéo, coulisses, portraits, compteur | FR + langue nationale |
| Instagram | jeunes, diaspora, presse | responsable com | 3 publications + stories quotidiennes | visuels, making-of, témoignages | FR (+ EN court) |
| E-mail | réseau professionnel, partenaires, diaspora | promoteur | J0, J+14, J+28, J+31 | lettre de lancement, mi-parcours, dernier sprint, merci | FR / EN |
| Presse et radios locales | grand public | responsable com | J-7, J+14 | communiqué, interview, événement | FR + langue nationale |
| Relais diaspora | diaspora du pays | relais identifié | hebdomadaire | partage, soirée de soutien à distance | FR / EN |

### Message-type WhatsApp (individuel, cercle 1 et 2)
Bonjour <prénom>, c'est <votre prénom>. Je lance aujourd'hui la campagne de <projet> : <une
phrase concrète sur ce que le projet fait et pour qui>. Nous avons <n> jours pour réunir
<objectif> FCFA. Ta contribution, même de <palier bas> FCFA, compte vraiment dans les premières
heures : <lien>. Si tu préfères Mobile Money : <numéro dédié, nom du titulaire>. Merci de
partager autour de toi. <prénom>

### Message-type Facebook / Instagram (lancement)
<Nom du projet> : <phrase d'accroche concrète>. <Deux phrases sur l'histoire, les personnes,
le lieu>. Nous lançons une collecte de <n> jours pour <usage précis des fonds>. Chaque
contribution reçoit <contrepartie la plus accessible>. Lien dans la bio / ci-dessous : <lien>.
Mobile Money : <numéro>. Partagez, c'est déjà aider. #<projet> #<ville> #<secteur>

### Message-type e-mail (lancement)
Objet : <Projet> — nous avons besoin de vous pendant <n> jours
Bonjour <prénom>,
<Une phrase personnelle sur votre lien avec la personne.> Depuis <durée>, <une phrase sur le
projet et les personnes qu'il concerne>. Aujourd'hui nous lançons une campagne de financement
participatif pour <usage précis> : objectif <montant> FCFA (≈ <montant> EUR) en <n> jours.
Contribuer prend deux minutes : <lien>. Les contreparties vont de <palier bas> à <palier haut>.
Si vous ne pouvez pas contribuer, transférer ce message à trois personnes nous aide tout autant.
Merci, <prénom et nom> — <téléphone>

### Communiqué-type presse locale (extrait)
<Ville>, le <date>. <Nom du projet> lance une campagne de financement participatif du <date> au
<date> pour <usage>. <Deux phrases sur le projet, son ancrage local, les femmes, les jeunes ou les
communautés concernées, avec un chiffre vérifiable.> Le public peut contribuer sur <plateforme>
ou par Mobile Money au <numéro>. Un événement ouvert aura lieu le <date> à <lieu>.
Contact presse : <nom, téléphone, courriel>.

### Message-type diaspora (FR puis EN court)
Vous êtes loin, mais ce projet est aussi le vôtre : <une phrase sur le lien au pays, à la ville,
à la culture>. Votre contribution depuis <pays> arrive directement sur la campagne : <lien>. En
retour : <contrepartie numérique ou envoi international>. / You are far away, but this project is
yours too. Your contribution from <country> goes straight to the campaign: <link>. In return:
<digital reward>.
```

### Gabarit F — Script de vidéo de campagne (90 secondes)

```markdown
## F. Script vidéo (90 s) — sous-titres obligatoires

| Temps | Image | Texte dit (FR ou langue nationale) | Sous-titre |
|---|---|---|---|
| 0-10 s | Plan sur le lieu et les personnes du projet, en action | « Je m'appelle <prénom>. Ici, à <lieu>, nous <action concrète>. » | FR |
| 10-30 s | Images du problème ou du besoin, visages, mains au travail | « <Ce qui manque aujourd'hui et pourquoi c'est important pour notre communauté, en deux phrases factuelles>. » | FR |
| 30-55 s | Images du projet : produit, répétition, repérage, atelier | « Avec <montant> FCFA, nous allons <trois actions précises>. <Qui en bénéficie : femmes, jeunes, village, public>. » | FR |
| 55-75 s | Contreparties montrées à l'écran ; l'équipe au complet | « En échange, vous recevez <contreparties>. Chaque contribution compte, même <palier bas>. » | FR |
| 75-90 s | Plan fixe sur le promoteur ; lien et numéro Mobile Money à l'écran | « Rendez-vous sur <lien> ou au <numéro>. Partagez cette vidéo. Merci. » (formule de remerciement en langue nationale) | FR |

Règles : lumière naturelle, téléphone stable, son propre (éviter le vent) ; pas de musique dont les
droits ne sont pas acquis (utiliser la musique du projet avec accord écrit des ayants droit, voir
/icc:propriete-intellectuelle) ; durée totale inférieure à 100 s ; version 30 s pour les stories.
```

### Gabarit G — Budget de campagne

```markdown
## G. Budget de campagne

| Poste | Base de calcul | Montant (FCFA) | Montant (EUR) | Source |
|---|---|---|---|---|
| Frais de plateforme | <taux> % de l'objectif brut [À VÉRIFIER — source : site officiel] | | | plateforme |
| Frais de paiement (carte, Mobile Money, change) | <taux> % [À VÉRIFIER] | | | plateforme / opérateur |
| Contreparties (fabrication, emballage) | somme du gabarit C × quantités attendues | | | devis |
| Envois (local, sous-région, international) | somme du gabarit C | | | poste / transporteur |
| Vidéo et visuels | <prestations, données mobiles> | | | devis |
| Événement de mi-parcours | <lieu, sonorisation, boissons> | | | devis |
| Communication (impressions, données mobiles, sponsorisation éventuelle) | | | | |
| Imprévus | 10 % des postes ci-dessus | | | |
| **Total des coûts de campagne** | | | | |

Montant net visé : <montant> FCFA.
Objectif brut à afficher = (net visé + contreparties + envois + communication + imprévus) / (1 − taux de frais total)
= <calcul> = <montant> FCFA (≈ <montant> EUR).
```

### Gabarit H — Risques, obligations et professionnels

```markdown
## H. Risques, obligations, professionnels requis

| Risque ou obligation | Probabilité | Impact | Mesure | Responsable / professionnel |
|---|---|---|---|---|
| Fiscalité des dons et des pré-ventes (TVA, impôts, reçus) selon le pays et le statut | certaine | élevé | consulter un expert-comptable AVANT le lancement ; conserver toutes les preuves de collecte | expert-comptable (indispensable) |
| Fonds reçus sur le compte d'un tiers (relais diaspora) | selon montage | élevé | convention écrite (objet, reversement, délais, frais, responsabilité), relevés partagés | avocat ou juriste (indispensable) |
| Campagne de prêt participatif | si choisie | élevé | encadrement légal strict ; ne pas lancer sans avis juridique | avocat (indispensable) |
| Objectif « tout ou rien » non atteint | moyenne | élevé | objectif public prudent (cercles 1 + 2) ; plan B : collecte flexible locale | promoteur |
| Contreparties non livrées ou en retard | moyenne | réputation | marges de délai annoncées ; stock et transporteur confirmés avant lancement ; information régulière | responsable logistique |
| Coupures de connexion ou d'électricité pendant le sprint final | élevée | moyen | publications programmées, relais diaspora pour publier, données mobiles de secours | responsable com |
| Droits d'auteur sur la musique ou les images de la vidéo | moyenne | juridique | accords écrits des ayants droit ; voir /icc:propriete-intellectuelle | promoteur, juriste si contrat |
| Données personnelles des contacts et contributeurs | certaine | juridique et confiance | consentement, pas d'ajout forcé à des groupes, liste conservée en lieu sûr | promoteur |
| Taux de change et frais de transfert vers le pays | certaine si plateforme étrangère | moyen | marge dans l'objectif brut ; choisir le canal de rapatriement le moins coûteux [À VÉRIFIER] | titulaire, expert-comptable |
| Promesses publiques excessives | moyenne | réputation | ne promettre que ce qui est produit ou certain ; relecture des textes par deux personnes | équipe |
```

### Exemple rempli (extrait) — scénario 3, marque de mode en pré-commandes (Afrique de l'Ouest)

```markdown
# Campagne de financement participatif — Collection « Fil & Terre » (atelier de 3 couturières)
Type de campagne : pré-vente (pré-commandes de la première collection) + dons avec contreparties

## A. Choix retenu
Montage hybride : plateforme francophone internationale ouverte par la sœur de la créatrice,
résidente en France (titulaire du compte, convention de reversement rédigée avec un juriste de
la ville), et numéro Mobile Money dédié au nom de la créatrice pour le public local. Compteur
unique publié chaque soir sur la page Facebook de l'atelier. Frais et pays éligibles :
[À VÉRIFIER — source : site officiel de la plateforme] avant J-30.

## B. Objectif
| Cercle | Contacts réels | Taux | Contributeurs | Don moyen (FCFA) | Montant (FCFA) | EUR |
|---|---|---|---|---|---|---|
| 1 — proches (famille, amies, clientes fidèles) | 60 | 40 % | 24 | 25 000 | 600 000 | ≈ 915 |
| 2 — réseau (clientes occasionnelles, associations de femmes, diaspora connue, abonnés actifs) | 400 | 7 % | 28 | 30 000 | 840 000 | ≈ 1 281 |
| 3 — inconnus (presse, partages) | 3 000 | 1,5 % | 45 | 20 000 | 900 000 | ≈ 1 372 |
| **Total attendu** | | | **97** | | **2 340 000** | **≈ 3 567** |
Objectif public affiché (cercles 1 + 2) : 1 400 000 FCFA (≈ 2 134 EUR). Objectif étendu :
2 300 000 FCFA (≈ 3 506 EUR) = achat d'une surjeteuse professionnelle [prix à confirmer par devis].

## C. Paliers (extrait)
| Palier | Contrepartie | Coût de revient | Envoi | Marge nette | Qté max | Livraison |
|---|---|---|---|---|---|---|
| 5 000 / ≈ 7,6 | Remerciement nominatif + photo exclusive de la collection | 0 | 0 | 5 000 | illimitée | J+15 |
| 25 000 / ≈ 38 | Pochette en pagne de la collection (pré-commande) | 6 000 | local 1 500 / Europe [tarif poste à vérifier] | ≥ 12 000 (Europe à chiffrer) | 60 | J+60 |
| 45 000 / ≈ 69 | Tunique de la collection, taille au choix (pré-commande) | 14 000 | local 1 500 / Europe à vérifier | ≥ 20 000 | 40 | J+75 |
| 75 000 / ≈ 114 | Tunique + visite d'atelier et atelier d'initiation (ou remerciement vidéo en langue nationale pour la diaspora) | 14 000 | idem | ≥ 50 000 | 15 | J+75 |
| 150 000 / ≈ 229 | Palier solidaire : une tenue offerte à une jeune apprentie de l'atelier + tunique pour le contributeur | 28 000 | idem | ≥ 110 000 | 10 | J+75 |
Contrôle : coût revient + envoi local ≤ 30 % de chaque palier ; envois Europe à confirmer avant
publication (sinon proposer le retrait par un proche en visite ou la version numérique).

## G. Budget (extrait)
Frais plateforme + paiement : hypothèse de travail 8 % [À VÉRIFIER] ; contreparties attendues
≈ 520 000 FCFA ; envois ≈ 120 000 FCFA ; vidéo et visuels 60 000 FCFA ; événement « essayage
ouvert » 80 000 FCFA ; imprévus 78 000 FCFA. Objectif brut pour 1 400 000 net :
(1 400 000 + 858 000) / 0,92 ≈ 2 454 000 FCFA (≈ 3 741 EUR) : trop élevé pour les cercles 1 + 2.
Décision : réduire le net visé à 900 000 FCFA (fil, tissus, étiquettes) et viser la surjeteuse en
objectif étendu ; objectif brut affiché ≈ 1 900 000 FCFA (≈ 2 896 EUR).

## H. Professionnels
Expert-comptable : traitement fiscal des pré-ventes (TVA, impôt) et tenue des reçus — rendez-vous
avant J-30. Juriste : convention de reversement avec la titulaire du compte en France.
```

## Critères de qualité du livrable

| Critère | Vérification |
|---|---|
| Plateforme | Le comparatif A est rempli ; chaque contrainte (compte, KYC, frais, devise) porte [À VÉRIFIER] ou une source datée ; le montage retenu précise le titulaire du compte et la convention. |
| Objectif | Le gabarit B repose sur des nombres de contacts réels et des taux prudents ; l'objectif public est atteignable avec les cercles 1 et 2. |
| Contreparties | Chaque palier a un coût de revient, un coût d'envoi par zone, une marge, une quantité maximale et un délai ; contrôle des 30 % effectué ; au moins une contrepartie immatérielle et une contrepartie solidaire. |
| Calendrier | J-30 à J+15 complet avec responsables ; pré-engagement du cercle 1 ; événement de mi-parcours ; livraison et rapports post-campagne. |
| Communication | Messages-types adaptés au projet pour chaque canal, en français et en langue nationale (et anglais si diaspora anglophone) ; règle de consentement rappelée. |
| Vidéo | Script de 90 s avec sous-titres, équipe visible, lien et numéro à l'écran, droits musicaux réglés. |
| Budget | Objectif brut calculé avec la formule ; FCFA et EUR partout (parité 1 EUR = 655,957 FCFA). |
| Risques | Fiscalité renvoyée à un expert-comptable ; convention de compte renvoyée à un juriste ; scénarios d'échec et de dépassement prévus. |
| Inclusion | Genre, jeunes, handicap, zones rurales, langues nationales présents dans les contreparties, les messages et la vidéo, avec des faits. |
| Honnêteté | Aucun frais, taux ou délai de plateforme affirmé sans [À VÉRIFIER] ; pas de promesse de réussite. |
| Reprenable | `projet/ETAT.md` mis à jour avec l'étape atteinte et les vérifications restantes. |

## Erreurs fréquentes à éviter

- Fixer l'objectif sur le besoin au lieu de la capacité réelle du réseau : une campagne qui plafonne
  à 15 % décourage tout le monde ; mieux vaut un objectif prudent dépassé.
- Oublier la question du compte bancaire et du pays jusqu'au jour du lancement ; ou faire porter
  les fonds par un tiers sans convention écrite.
- Recopier des frais ou des conditions de plateforme de mémoire : ils changent ; marquer
  [À VÉRIFIER] et consulter le site officiel.
- Promettre des envois internationaux sans avoir vérifié le tarif, le délai et les taxes à
  l'arrivée depuis le pays d'expédition.
- Proposer des contreparties coûteuses qui absorbent la collecte (coût total supérieur à 30 % du
  palier).
- Lancer sans pré-engagement du cercle 1 : les 72 premières heures décident de la dynamique.
- Ajouter des contacts à des groupes WhatsApp sans consentement ; envoyer le même message
  impersonnel à tous.
- Négliger la version en langue nationale et les sous-titres : une partie du public local et les
  personnes malentendantes sont exclues.
- Utiliser une musique ou des images sans droits dans la vidéo.
- Ne pas prévoir la fiscalité des dons et des pré-ventes : renvoyer à un expert-comptable avant le
  lancement.
- Disparaître après la clôture : les rapports mensuels jusqu'à livraison sont ce qui rend possible
  une deuxième campagne.
- Oublier de mettre à jour `projet/ETAT.md`.

## Références et sources à vérifier

- Sites officiels des plateformes (domaines uniquement ; conditions, pays éligibles, frais et
  délais à lire sur place) : ulule.com, kisskissbankbank.com, kickstarter.com, gofundme.com,
  afrikwity.com, fiatope.com (existence et activité à confirmer) ; sites des opérateurs de Mobile
  Money du pays (frais de retrait, plafonds).
- `skills/cartographie-bailleurs/references/bailleurs.md`, section 6, pour la logique générale des
  plateformes.
- Si WebSearch est disponible : « <plateforme> pays éligibles compte bancaire <année> »,
  « <plateforme> frais <année> », « crowdfunding culture <pays> retour d'expérience », « tarif
  colis international poste <pays> ».
- Administration fiscale du pays et expert-comptable : traitement des dons, des pré-ventes (TVA),
  des reçus ; obligations déclaratives selon le statut (personne physique, association,
  entreprise).
- Société de gestion collective des droits d'auteur du pays et `/icc:propriete-intellectuelle`
  pour la musique et les images de la campagne.
- Documents du promoteur : devis des fournisseurs et transporteurs, relevés Mobile Money, statuts.

## Passage de relais

Après la conception de la campagne :
1. Si le montage financier (titulaire du compte, convention, fiscalité) n'est pas sécurisé :
   `/icc:statut-juridique` (agent `icc-juridique`) et rendez-vous expert-comptable et juriste.
2. Pour intégrer le montant net attendu dans le plan de financement et la trésorerie :
   `/icc:budget-cofinancement` et `/icc:plan-tresorerie` (agent `icc-budget`).
3. Pour les visuels, le pitch et la relation presse : `/icc:pitch-dossier-presse` (agent
   `icc-communication`).
4. Pour les droits sur la musique et les images de la vidéo : `/icc:propriete-intellectuelle`
   (agent `icc-juridique`).
5. Pour suivre les indicateurs de la campagne (contributeurs par cercle, part de femmes et de
   jeunes parmi les bénéficiaires des paliers solidaires) : `/icc:suivi-evaluation` (agent
   `icc-mise-en-oeuvre`).
6. Retour à `icc-orchestrateur` pour la suite du parcours.

Mise à jour obligatoire de `projet/ETAT.md` (créer le fichier avec la structure imposée s'il
n'existe pas) :
- « Dernière mise à jour » : date et heure ; « Agent actif : icc-communication | Skill en cours :
  /icc:crowdfunding » (ou le skill suivant) ;
- « Étapes terminées » : « Plan de campagne de financement participatif —
  projet/communication/crowdfunding.md (type : …, montage : …, objectif public : … FCFA) » ;
- « Étape en cours » : étape du calendrier J-30 à J+15 atteinte ou préparatif en cours ;
- « Prochaines étapes » : vérifications des plateformes, rendez-vous expert-comptable et juriste,
  tournage vidéo, date de lancement envisagée ;
- « Décisions prises / hypothèses à confirmer » : taux de conversion retenus, taux de frais
  [À VÉRIFIER], tarifs d'envoi à confirmer, titulaire du compte ;
- « Questions en attente de réponse du promoteur » : questions restées sans réponse ;
- « Alertes » : fiscalité (expert-comptable indispensable), convention de compte (juriste
  indispensable), droits musicaux, délais de livraison promis, dépendance à la connexion pendant le
  sprint final.
