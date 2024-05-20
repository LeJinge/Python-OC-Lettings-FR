Installation du projet
======================

Prérequis
---------

- Python 3.8 ou supérieur
- pip

Instructions d'installation
---------------------------

**1. Clonez le dépôt GitHub :**

   git clone https://github.com/LeJinge/Python-OC-Lettings-FR.git

   cd Python-OC-Lettings-FR

**2. Créez un environnement virtuel et activez-le :**

   python -m venv venv

   source venv/bin/activate

**3. Installez les dépendances du projet :**

    pip install -r requirements.txt

**4. Appliquer les migrations**

   python manage.py migrate

**5. Démarrez le serveur de développement :**

   python manage.py runserver

**6. Accédez à l'application :**

    Ouvrez votre navigateur et accédez à l'adresse `http://127.0.0.1:8000/`.