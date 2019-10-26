from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        print("")
        print(">>>")
        print(">>>>>> apps.py signals ready to fire")
        print(">>>")
        print("")
        from .signals import welcome_new_user, new_social_user