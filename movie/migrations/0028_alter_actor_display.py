# Generated by Django 3.2.9 on 2021-12-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0027_alter_movie_origen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='display',
            field=models.BooleanField(blank=True, db_column='Mostrar', null=True, verbose_name='Mostrar'),
        ),
    ]