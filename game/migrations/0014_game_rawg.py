# Generated by Django 3.2 on 2021-11-02 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0013_alter_gamecapture_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='rawg',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
