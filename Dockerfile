# Utilisez une image de base avec Python 3.10
FROM python:3.8-slim

# Définez le répertoire de travail
WORKDIR /app

# Copiez le fichier de dépendances
COPY requirements.txt .

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copiez l'application
COPY . .

# Exposez le port 8000
EXPOSE 8000

# Commande par défaut pour lancer l'application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myapp.wsgi:application"]
