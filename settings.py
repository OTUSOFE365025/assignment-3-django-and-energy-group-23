from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = "assignment_3_secret"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS = ("db",)
