"""Declaração mínima do app; sem modelos, views ou funcionalidades."""
from django.apps import AppConfig

class CargosCorporativosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cargos_corporativos"
