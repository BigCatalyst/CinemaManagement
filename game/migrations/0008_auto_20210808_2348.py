# Generated by Django 3.1.12 on 2021-08-09 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20210808_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='manual',
            field=models.FileField(blank=True, db_column='Manual', max_length=2500, null=True, upload_to=''),
        ),
    ]
