# Generated by Django 3.1.12 on 2021-07-14 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='capture',
            field=models.ImageField(blank=True, db_column='Capturas', max_length=2500, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='game',
            name='photo',
            field=models.ImageField(blank=True, db_column='Foto', max_length=500, null=True, upload_to=''),
        ),
    ]
