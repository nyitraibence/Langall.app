from django.contrib import admin
from .models import TeacherProfile


class TeacherProfileInline(admin.TabularInline):
    model = TeacherProfile
    can_delete = False
    verbose_name_plural = 'Teacher Profile'

