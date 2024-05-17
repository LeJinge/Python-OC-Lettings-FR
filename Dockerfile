# Utilisez une image de base avec Python 3.10
FROM python:3.8-slim

# Définez le répertoire de travail
WORKDIR /app

# Copiez le fichier de dépendances
COPY requirements.txt .

# Installez les dépendances
# Mettre à jour pip à une version spécifique et installer les dépendances sans isolation et en mode silencieux
RUN pip install --no-cache-dir --upgrade pip==23.0.1 && \
    pip install --no-cache-dir --progress-bar off --no-build-isolation -r requirements.txt

# Copiez l'application
COPY . .

# Exposez le port 8000
EXPOSE 8000

# Commande par défaut pour lancer l'application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
