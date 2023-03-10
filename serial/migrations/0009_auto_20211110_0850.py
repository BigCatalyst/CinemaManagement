# Generated by Django 3.2.9 on 2021-11-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serial', '0008_alter_serial_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serial',
            name='title',
            field=models.CharField(blank=True, db_column='Titulo', max_length=1000, null=True, verbose_name='Título en Español'),
        ),
        migrations.AlterField(
            model_name='serial',
            name='title_eng',
            field=models.CharField(db_column='TituloIng', max_length=1000, verbose_name='Título en Inglés'),
        ),
    ]
