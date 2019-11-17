from django.db import models
from django.conf import settings
from cuser.models import AbstractCUser
from .coreconfig import LANGUAGE




class CustomUser(AbstractCUser):
    city = models.CharField(blank=True, max_length=40)
    location = models.CharField(blank=True, max_length=150)
    interest_lang_1 = models.CharField(
        blank=True, max_length=3, choices=LANGUAGE)
    interest_lang_2 = models.CharField(
        blank=True, max_length=3, choices=LANGUAGE)
    interest_lang_3 = models.CharField(
        blank=True, max_length=3, choices=LANGUAGE)
    is_phone_verified = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

