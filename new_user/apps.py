from django.apps import AppConfig


class NewUserConfig(AppConfig):
    name = 'new_user'
    verbose_name = "New User"

    def ready(self):
        from new_user import receivers
