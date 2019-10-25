from django.db import models
from django.conf import settings
from cuser.models import AbstractCUser


LANGUAGE = [
    ('ENG', 'English'),
    ('SPA', 'Spanish'),
    ('GER', 'German'),
    ('FRA', 'French'),
    ('ITA', 'Italian'),
    ('RUS', 'Russian'),
]


class CustomUser(AbstractCUser):
    city = models.CharField(blank=True, max_length=40)
    location = models.CharField(blank=True, max_length=150)
    interest_lang_1 = models.CharField(
        blank=True, max_length=3, choices=LANGUAGE)
    interest_lang_2 = models.CharField(
        blank=True, max_length=3, choices=LANGUAGE)
    interest_lang_3 = models.CharField(
        blank=True, max_length=3, choices=LANGUAGE)
    form_fill_factor = models.FloatField(blank=True, default=1, max_length=4)
    is_phone_verified = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacherprofile')
    introduction = models.TextField(blank=True, max_length=600)
    base_price = models.PositiveSmallIntegerField(blank=True, null=True)
    teach_lang_1 = models.CharField(blank=True, max_length=3, choices=LANGUAGE)
    teach_lang_2 = models.CharField(blank=True, max_length=3, choices=LANGUAGE)
    teach_lang_3 = models.CharField(blank=True, max_length=3, choices=LANGUAGE)

    def __str__(self):
        return 'Information'