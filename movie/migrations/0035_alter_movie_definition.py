# Generated by Django 3.2.9 on 2021-12-06 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0034_movie_actor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='definition',
            field=models.CharField(blank=True, db_column='Definicion', max_length=500, null=True, verbose_name='Definicion'),
        ),
    ]