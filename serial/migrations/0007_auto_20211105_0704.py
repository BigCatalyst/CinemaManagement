# Generated by Django 3.2.9 on 2021-11-05 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serial', '0006_auto_20211105_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='serial',
            name='reviewed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='serial',
            name='photo',
            field=models.ImageField(blank=True, db_column='FotoSerie', null=True, upload_to='series/', verbose_name='Foto'),
        ),
    ]
