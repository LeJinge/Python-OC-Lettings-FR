import logging
import os
import yaml
from pathlib import Path
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

# Load configuration from YAML file
with open(os.path.join(BASE_DIR, 'config.yaml')) as file:
    config = yaml.safe_load(file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['django']['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config['django']['debug']

ALLOWED_HOSTS = config['django']['allowed_hosts']

# Application definition

INSTALLED_APPS = [
    'oc_lettings_site.apps.OcLettingsSiteConfig',
    'lettings',
    'profiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oc_lettings_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'oc_lettings_site.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Configuration Azure Storage
AZURE_ACCOUNT_NAME = 'lettingsoc'
AZURE_ACCOUNT_KEY = '4VXqkj6YPa7JoVQo+0+tNxfqNJ44o8hTOlcZhNTC+57a78srtfiQT6diE/1HmQVKbh3M1l4VWIfN+ASt/7mqPQ=='
AZURE_CONTAINER = 'static'

# Utiliser des custom storages (optionnel mais recommandé)
DEFAULT_FILE_STORAGE = 'oc_lettings_site.custom_storages.MediaStorage'
STATICFILES_STORAGE = 'oc_lettings_site.custom_storages.StaticStorage'

# Configuration CDN
CDN_URL = 'https://cdn-endpoint-lettings.azureedge.net/static/'
STATIC_URL = CDN_URL

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = str(BASE_DIR / 'staticfiles')
STATICFILES_DIRS = [str(BASE_DIR / 'static')]

# Sentry Configuration
SENTRY_DSN = config['sentry']['dsn']

sentry_logging = LoggingIntegration(
    level=logging.INFO,  # Capture info and above as breadcrumbs
    event_level=logging.ERROR  # Send errors as events
)

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[DjangoIntegration(), sentry_logging],
    # Si vous souhaitez capturer 100 % des transactions pour le suivi des performances
    traces_sample_rate=1.0,
    # Définir cette valeur est important pour que Sentry puisse afficher les erreurs de manière plus détaillée
    send_default_pii=True
)

# Logging Configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = sentry_sdk.integrations.logging.EventHandler()
handler.setLevel(logging.WARNING)
logger.addHandler(handler)
