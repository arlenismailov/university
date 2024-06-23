from django.apps import AppConfig

class UniverAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'univer_app'

    def ready(self):
        import univer_app.signals  # Импорт сигналов
