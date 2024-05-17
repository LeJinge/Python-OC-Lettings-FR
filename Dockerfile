# Utilisez une image de base avec Python 3.10
FROM python:3.10-slim

# Installez les dépendances
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --no-build-isolation -r requirements.txt && \
    rm -rf /root/.cache/pip

# Copiez l'application
COPY . .

# Définez le répertoire de travail
WORKDIR /app

# Commande par défaut pour lancer l'application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myapp.wsgi:application"]
