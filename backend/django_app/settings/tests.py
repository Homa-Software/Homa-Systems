from .base import *

DEBUG = False
SECRET_KEY = "secret_key"

# ------------- LOGGING -------------
LOGGING = {}

# ------------- MIDDLEWARES -------------
MIDDLEWARE = list(filter(lambda x: "DebugToolbarMiddleware" not in x, MIDDLEWARE))

# ------------- PASSWORDS -------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# ------------- DATABASES -------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", "django_app"),
        "USER": env("POSTGRES_USER", "django_app"),
        "PASSWORD": env("POSTGRES_PASSWORD", "django_app"),
        "HOST": env("POSTGRES_HOST", "localhost"),
    }
}