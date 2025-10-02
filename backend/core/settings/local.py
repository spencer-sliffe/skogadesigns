from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "::1"]

# Local frontend (Next.js) at 3000
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# # SQLite by default (from base.py). If you set DATABASE_URL locally, you can switch to Postgres:
# if os.getenv("DATABASE_URL"):
#     # requires dj-database-url if you want URL parsing; or use psycopg params
#     import dj_database_url  # pip install dj-database-url
#     DATABASES["default"] = dj_database_url.parse(os.environ["DATABASE_URL"], conn_max_age=0, ssl_require=False)

# Dev email goes to console
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Relaxed security locally
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
