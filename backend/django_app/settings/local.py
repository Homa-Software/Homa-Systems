from .base import *

SECRET_KEY = "secret_key"

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
