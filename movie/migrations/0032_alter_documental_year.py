# Generated by Django 3.2.9 on 2021-12-04 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0031_alter_documental_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documental',
            name='year',
            field=models.IntegerField(blank=True, db_column='Anno', null=True, verbose_name='Año'),
        ),
    ]
