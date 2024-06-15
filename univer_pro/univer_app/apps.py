# apps.py

from django.apps import AppConfig


class UniverAppConfig(AppConfig):
    name = 'univer_app'

    def ready(self):
        import univer_app.signals  # Импортируем сигнал
