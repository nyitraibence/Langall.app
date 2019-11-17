from django.contrib import admin
from .models import TeacherProfile, Lesson


class TeacherProfileInline(admin.TabularInline):
    model = TeacherProfile
    can_delete = False
    verbose_name_plural = 'Teacher Profile'

class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'host_teacher', 'student',
                    'language', 'is_verified', 'is_rejected', 'is_over']

admin.site.register(Lesson, LessonAdmin)
