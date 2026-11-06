"""Declaração mínima do app; sem modelos, views ou funcionalidades."""
from django.apps import AppConfig

class CooperadosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cooperados"
