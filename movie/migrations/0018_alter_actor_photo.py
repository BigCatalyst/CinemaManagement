# Generated by Django 3.2 on 2021-11-01 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0017_auto_20211031_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='photo',
            field=models.ImageField(blank=True, db_column='FotoActor', null=True, upload_to='actores/'),
        ),
    ]