# Generated by Django 3.2 on 2021-08-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0016_auto_20210819_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.TextField(blank=True, db_column='Nombre', null=True, unique=True),
        ),
    ]
