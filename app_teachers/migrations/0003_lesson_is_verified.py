# Generated by Django 2.2.6 on 2019-11-06 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_teachers', '0002_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
