# Generated by Django 3.2 on 2021-10-31 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0016_auto_20210823_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='film_affinity',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='imdb',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
