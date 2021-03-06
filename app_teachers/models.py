from django.db import models
from core.models import CustomUser
from django.conf import settings
from core.coreconfig import LANGUAGE, DAYS
from django.utils import timezone


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacherprofile')
    introduction = models.TextField(blank=True, max_length=600)
    base_price = models.PositiveSmallIntegerField(blank=True, null=True)
    form_fill_factor = models.FloatField(blank=True, default=1, max_length=4)
    rate_avg = models.FloatField(blank=True, max_length=4)
    num_ratings = models.PositiveIntegerField(blank=True, null=True)
    teach_lang_1 = models.CharField(blank=True, max_length=3, choices=LANGUAGE)
    teach_lang_2 = models.CharField(blank=True, max_length=3, choices=LANGUAGE)
    teach_lang_3 = models.CharField(blank=True, max_length=3, choices=LANGUAGE)

    def __str__(self):
        return 'Information'


class Lesson(models.Model):
    host_teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='host_teacher')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
    created = models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    language = models.CharField(blank=True, max_length=3, choices=LANGUAGE)
    location = models.CharField(blank=True, max_length=150)
    note = models.TextField(blank=True, max_length=400)
    reject_message = models.TextField(blank=True, max_length=400)
    is_verified = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    is_over = models.BooleanField(default=False)



class TimeCell(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='time_cell')
    status = models.CharField(blank=True, max_length=10, default="available")
    s_time = models.TimeField(blank=True, null=True)
    day = models.CharField(blank=True, max_length=10, choices=DAYS)



class Rating(models.Model):
    rater = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rater_rev')
    rated_one = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rated_one_rev')
    score = models.PositiveSmallIntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, max_length=600)