from django.db.models.signals import post_save
from django.dispatch import Signal
from django.dispatch import receiver
from .models import CustomUser
# for reciever functions:
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


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
    subject = '🎉 Köszönjük, hogy regisztráltál!'
    message = render_to_string('email/welcome_new_user.html', {
        'new_user': new_user,
    })
    to_email = new_user.email
    email = EmailMessage(
                subject, message, to=[to_email]
    )
    email.content_subtype = "html"          # important addition for html email to render !
    email.send()
    print('greeting email: sent >>>')
    print('================')