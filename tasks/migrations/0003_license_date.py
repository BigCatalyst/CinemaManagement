# Generated by Django 3.1.12 on 2021-11-04 16:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_license'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 16, 42, 20, 627613, tzinfo=utc)),
        ),
    ]
