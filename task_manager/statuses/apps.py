from django.apps import AppConfig


class StatusesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task_manager.statuses'

    def ready(self):
        pass
