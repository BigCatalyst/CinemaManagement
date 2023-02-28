# Generated by Django 3.2.9 on 2021-11-05 12:16

from django.db import migrations, models
from movie.models import Movie
from serial.models import Season


def update_exito_video(apps, schema_editor):
    genders = Movie.objects.all()
    for gender in genders:
        gender.definition = gender.definition.upper() if gender.definition is not None else None
        gender.save()
    genders = Season.objects.all()
    for gender in genders:
        gender.definition = gender.definition.upper() if gender.definition is not None else None
        gender.save()


class Migration(migrations.Migration):
    dependencies = [
        ('movie', '0042_auto_preparing_next_migration'),
    ]

    operations = [
        migrations.RunPython(update_exito_video),
    ]