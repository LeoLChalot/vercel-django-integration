"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

import dj_database_url

from mysite.config import AppSettings

# Charger les paramètres
config = AppSettings()
# DEBUG = config.debug
# print(config.database_url)

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/


ALLOWED_HOSTS: list[str] = ["localhost", "127.0.0.1", "[::1]", "now.sh", ".vercel.app"]

print(ALLOWED_HOSTS)
# Application definition

INSTALLED_APPS: list[str] = [
    # This project
    "website",
    "custom_user",
    # Wagtail CRX (CodeRed Extensions)
    "coderedcms",
    "django_bootstrap5",
    "modelcluster",
    "taggit",
    "wagtailcache",
    "wagtailseo",
    # Wagtail
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail",
    "wagtail.contrib.settings",
    "wagtail.contrib.table_block",
    "wagtail.admin",
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
]

MIDDLEWARE: list[str] = [
    # Save pages to cache. Must be FIRST.
    "wagtailcache.cache.UpdateCacheMiddleware",
    # Common functionality
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.CommonMiddleware",
    # Security
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # CMS functionality
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    # Fetch from cache. Must be LAST.
    "wagtailcache.cache.FetchFromCacheMiddleware",
]

ROOT_URLCONF = "mysite.urls"
AUTH_USER_MODEL = "custom_user.User"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


# Database configuration
# database_url = os.getenv("DATABASE_URL_OPTION")
database_url = config.database_url

print(f"[SETTINGS] DATABASE_URL : {os.getenv("DATABASE_URL_OPTION")}")
DATABASES = {
    "default": dj_database_url.parse(
        database_url,
        conn_max_age=600,
        ssl_require=True,
    )
}

# Backend configuration

# STATIC_URL = STATIC_HOST + "/static/"
STATIC_URL = '/static/'


STATIC_ROOT = BASE_DIR / "static"

DEFAULT_FILE_STORAGE = "mysite.storage_backend.blob_storage.VercelBlobStore"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


STORAGES: dict[str, dict[str, str]] = {
    "default": {
        "BACKEND": DEFAULT_FILE_STORAGE,
    },
    "media": {
        "BACKEND": DEFAULT_FILE_STORAGE,
    },
    "staticfiles": {
        "BACKEND": STATICFILES_STORAGE,
    },
}


# print("ENVIRONMENT:", os.getenv("ENVIRONMENT"))

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS: list[dict[str, str]] = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]




# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "fr-FR"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATICFILES_FINDERS: list[str] = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# STATIC_HOST = "vercel-django-integration-jonz9ypl8-leolchalots-projects.vercel.app" if not DEBUG else ""


# Répertoire temporaire pour les fichiers
TEMP_DIR = "/tmp"

# Fichiers médias
# MEDIA_ROOT = TEMP_DIR
MEDIA_URL = "https://gqb3dhg6ajkwelj6.public.blob.vercel-storage.com/original_images/"
DOCUMENT_URL = "https://gqb3dhg6ajkwelj6.public.blob.vercel-storage.com/documents/"


# Login

LOGIN_URL = "wagtailadmin_login"
LOGIN_REDIRECT_URL = "wagtailadmin_home"

# Wagtail settings

WAGTAIL_SITE_NAME = "SafeBear"

WAGTAIL_ENABLE_UPDATE_CHECK = False

WAGTAILIMAGES_EXTENSIONS: list[str] = [
    "gif",
    "jpg",
    "jpeg",
    "png",
    "webp",
    "svg",
]

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
# WAGTAILADMIN_BASE_URL = "http://localhost"
WAGTAILADMIN_BASE_URL = "https://vercel-django-integration.vercel.app"

# Tags
TAGGIT_CASE_INSENSITIVE = True

# Sets default for primary key IDs
# See https://docs.djangoproject.com/en/5.1/ref/models/fields/#bigautofield
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Disable built-in CRX Navbar and Footer since this project has a
# custom implementation.
CRX_DISABLE_NAVBAR = True
CRX_DISABLE_FOOTER = True

