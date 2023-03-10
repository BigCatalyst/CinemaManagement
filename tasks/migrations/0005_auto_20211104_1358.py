# Generated by Django 3.1.12 on 2021-11-04 17:58

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20211104_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='license',
            old_name='date',
            new_name='created',
        ),
        migrations.AddField(
            model_name='license',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 4, 17, 57, 55, 928377, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='license',
            name='validated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
