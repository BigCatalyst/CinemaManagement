# Generated by Django 3.2.9 on 2021-12-05 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0033_auto_20211205_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(blank=True, to='movie.Actor', verbose_name='Elenco de la película'),
        ),
    ]
