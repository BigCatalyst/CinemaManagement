# Generated by Django 3.2 on 2021-11-02 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0014_game_rawg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='photo',
            field=models.ImageField(blank=True, db_column='Foto', max_length=500, null=True, upload_to='juegos/'),
        ),
    ]
