from django.contrib import admin
from cuser.admin import UserAdmin
from .models import CustomUser
from app_teachers.admin import TeacherProfileInline


class CustomUserAdmin(admin.ModelAdmin):
    inlines = [TeacherProfileInline]

    list_display = ['email', 'first_name',
                    'last_name', 'is_teacher', 'is_active', ]
    fieldsets = (
        ('Users auth. details', {
            'classes': ('collapse',),
            'fields': ('is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login'),
        }),
        ('Authentication', {
            'fields': ('email', 'password')
        }),
        ('Profile', {
            'fields': ('first_name', 'last_name', 'city', 'location', 'interest_lang_1', 'interest_lang_2', 'interest_lang_3', 'is_phone_verified', 'is_teacher', 'is_premium','favourites'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)

