# Generated by Django 3.1.12 on 2021-08-12 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20210811_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(blank=True, db_column='Nombre', max_length=500, null=True),
        ),
    ]