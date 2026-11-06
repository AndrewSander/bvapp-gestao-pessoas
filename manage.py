#!/usr/bin/env python3
"""Ponto de entrada padrão do Django; não há aplicação funcional nesta entrega."""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
