from django.apps import AppConfig


class OurTeamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'team'

    def ready(self):
        return super().ready()
    pass
