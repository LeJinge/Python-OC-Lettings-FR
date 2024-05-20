Fonctionnement de la pipeline
=============================

Le projet utilise CircleCI pour la mise en place de la pipeline CI/CD. La pipeline inclut les étapes suivantes :

1. **Vérification du code avec Flake8** :

   Assure que le code respecte les normes de style Python.

2. **Tests unitaires avec couverture** :

   Exécute les tests unitaires et génère un rapport de couverture.

3. **Construction et déploiement de l'image Docker** :

   Construit une image Docker et la déploie sur Docker Hub.

4. **Déploiement de l'application** :

    Déploie l'application sur Microsoft Azure sur une App Service. A l'aide d'un webhook, le déploiement
    est automatiquement déclenché en venant pull la dernière image Docker présente sur DockerHub.

**Configuration de CircleCI :**

Le fichier de configuration de CircleCI (`.circleci/config.yml`) contient les détails de chaque étape de la pipeline.
