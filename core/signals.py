from django.db.models.signals import post_save
from django.dispatch import Signal
from django.dispatch import receiver
from .models import CustomUser


# NOTE: All created signals have to be imported in apps.py !



### SIGNALS ###
new_user_activation = Signal()                              # you can provide extra args -> providing_args=["example_data"]
new_social_user = Signal()


### recievers ###
@receiver([new_user_activation, new_social_user])
def welcome_new_user(sender, **kwargs):
    new_user = sender
    print('================')
    print('New user saved!')
    print(new_user.last_name, new_user.first_name)
    print(new_user.email)
    print('================')