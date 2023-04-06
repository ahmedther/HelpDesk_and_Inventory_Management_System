"""
Django settings for HTMS_Website project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-%mpjik#3zfe+0bdmb@24ej8f6w+v$)ko$!jb%smu0*%@g+n=#7"

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

# DEBUG = False

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "172.20.100.81",
    "http://localhost:8004",
    "http://172.20.100.81:8004",
    "http://localhost:9004",
    "http://172.20.100.81:9004",
    "172.20.200.40",
    "www.kdahlinux.com:8004",
]


CSRF_TRUSTED_ORIGINS = [
    "127.0.0.1",
    "localhost",
    "172.20.100.81",
    "http://localhost:8004",
    "http://172.20.100.81:8004",
    "http://localhost:9004",
    "http://172.20.100.81:9004",
    "172.20.200.40",
    "www.kdahlinux.com:8004",
]


# Application definition

INSTALLED_APPS = [
    "HTMS_App.apps.HtmsAppConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "HTMS_API",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "HTMS_Website.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "HTMS_Website.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "HTMS_database",
        "USER": "postgres",
        "PASSWORD": "ahmed",
        "HOST": "172.20.100.81",
        "PORT": "5432",
    }
}


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Calcutta"

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = "static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
