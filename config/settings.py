"""Configuração mínima para conservar a arquitetura; não é um sistema BVapp."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "uso-academico-exclusivamente-local-nao-publicar-em-producao"
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = ["cooperados", "usinas", "cargos_corporativos"]
MIDDLEWARE = []
ROOT_URLCONF = "config.urls"
TEMPLATES = []
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
