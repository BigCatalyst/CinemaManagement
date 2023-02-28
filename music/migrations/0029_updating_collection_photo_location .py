# Generated by Django 3.2.9 on 2021-11-05 12:16

from django.db import migrations, models
from music.models import Collection


def update_collection_path(apps, schema_editor):
    genders = Collection.objects.all()
    for gender in genders:
        gender.photo = (
            f"{str(gender.photo).replace('album', 'coleccion')}"
        )
        gender.save()


class Migration(migrations.Migration):
    dependencies = [
        ('music', '0028_auto_20211126_0829'),
    ]

    operations = [
        migrations.RunPython(update_collection_path),
    ]
