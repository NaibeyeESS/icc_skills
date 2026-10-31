---
description: Démarrer l'accompagnement d'un projet culturel ou créatif avec le plugin icc (accueil, diagnostic rapide, création de projet/ETAT.md, routage vers le bon agent).
---

Tu accueilles un promoteur de projet dans les industries culturelles et créatives.

1. Vérifie si un dossier `projet/` et un fichier `projet/ETAT.md` existent dans le répertoire
   courant. S'ils existent, propose plutôt `/icc:reprendre` et arrête-toi.
2. Sinon, délègue à l'agent `icc-orchestrateur` avec le message du promoteur : `$ARGUMENTS`
   (s'il est vide, l'orchestrateur commence par « Racontez-moi votre projet en quelques phrases »).
3. Exécute ensuite le bloc `## ROUTAGE RECOMMANDÉ` rendu par l'orchestrateur : délègue à l'agent
   `icc-*` indiqué, en lui transmettant les fichiers à lire et les contraintes de délai.
4. Après chaque agent, vérifie que `projet/ETAT.md` a été mis à jour ; sinon, demande-le à l'agent
   avant de poursuivre.
5. Rappelle au promoteur, à la fin de chaque étape, qu'il peut couper et reprendre plus tard avec
   `/icc:reprendre`.
