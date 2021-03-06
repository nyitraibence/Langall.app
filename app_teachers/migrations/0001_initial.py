# Generated by Django 2.2.6 on 2019-10-27 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.TextField(blank=True, max_length=600)),
                ('base_price', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('teach_lang_1', models.CharField(blank=True, choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('GER', 'German'), ('FRA', 'French'), ('ITA', 'Italian'), ('RUS', 'Russian')], max_length=3)),
                ('teach_lang_2', models.CharField(blank=True, choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('GER', 'German'), ('FRA', 'French'), ('ITA', 'Italian'), ('RUS', 'Russian')], max_length=3)),
                ('teach_lang_3', models.CharField(blank=True, choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('GER', 'German'), ('FRA', 'French'), ('ITA', 'Italian'), ('RUS', 'Russian')], max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacherprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
