from django.apps import AppConfig


class TuluayorkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Tuluayork'

    def ready(self):
        import Tuluayork.signals
