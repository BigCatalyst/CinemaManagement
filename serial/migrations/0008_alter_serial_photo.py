# Generated by Django 3.2.9 on 2021-11-05 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serial', '0007_auto_20211105_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serial',
            name='photo',
            field=models.ImageField(blank=True, db_column='FotoSerie', max_length=2500, null=True, upload_to='series/', verbose_name='Foto'),
        ),
    ]
