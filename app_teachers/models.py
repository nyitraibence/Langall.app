from django.db import models
from core.models import CustomUser, LANGUAGE
from django.conf import settings


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