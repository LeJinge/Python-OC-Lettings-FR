# Dockerfile

FROM python:3.11

# Définir les variables d'environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Définir le répertoire de travail
WORKDIR /code

# Copier les fichiers de dépendances et installer les dépendances
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copier le projet
COPY . /code/

# Exécuter collectstatic pour collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposer le port 8000
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
