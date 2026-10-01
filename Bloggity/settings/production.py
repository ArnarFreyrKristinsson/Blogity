"""Production Django settings."""

import os

from .base import *  # noqa

DEBUG = False

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

INSTALLED_APPS += ["sslserver"]  # noqa

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASS"],
        "HOST": os.environ["DB_HOST"],
        "PORT": os.environ["DB_PORT"],
        "CONN_MAX_AGE": 300,
    }
}

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

STATIC_URL = "/api/static_files/"

STATIC_ROOT = "Bloggity/static_files/"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "./production-logs.log",
        }
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": True,
        },
    },
}

ALLOWED_HOSTS = [
    "staging.arnarfreyr.is",
    "arnarfreyr.is",
    "blogity.arnarfreyr.is",
    "localhost",
    "blogity.onrender.com",
    "blogity-production.onrender.com",
]

CORS_ALLOWED_ORIGINS = [
    "https://staging.arnarfreyr.is",
    "https://arnarfreyr.is",
]

CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "DELETE"]

CORS_ALLOW_HEADERS = ["authorization", "content-type"]

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_PRELOAD = True
