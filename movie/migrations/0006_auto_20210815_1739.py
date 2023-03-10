# Generated by Django 3.1.12 on 2021-08-15 17:39

from django.db import migrations, models
from movie.models import Gender


def update_gender_image_path(apps, schema_editor):
    genders = Gender.objects.all()
    for gender in genders:
        gender.photo = "generos/" + str(gender.photo)
        gender.save()


class Migration(migrations.Migration):
    dependencies = [
        ('movie', '0005_auto_20210815_1711'),
    ]

    operations = [
        migrations.RunPython(update_gender_image_path)
    ]
