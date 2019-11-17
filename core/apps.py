from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        # print(">>>>>>>>>>>>>>>>>>>>")
        # print("")
        # print("App ready() fired")
        # print("")
        # print(">>>>>>>>>>>>>>>>>>>>")

        # signals
        from .signals import welcome_new_user
        from django.db.models.signals import post_save

        # schedulers
        from scheduler import scheduler_hq
        scheduler_hq.main_schedule_controller()
        