# Generated by Django 3.1.12 on 2021-08-17 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_gendermusic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gendermusic',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='generosmusica/'),
        ),
    ]
