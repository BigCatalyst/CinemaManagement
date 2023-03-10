# Generated by Django 3.1.12 on 2021-11-04 18:34

import datetime

from django.contrib.postgres.operations import CryptoExtension
from django.db import migrations
from django.utils.timezone import utc
import django.utils.timezone
import pgcrypto.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20211104_1358'),
    ]

    operations = [
        CryptoExtension(),
        migrations.AlterField(
            model_name='license',
            name='created',
            field=pgcrypto.fields.EncryptedDateTimeField(charset='utf-8', check_armor=True, cipher='aes', default=django.utils.timezone.now, versioned=False),
        ),
        migrations.AlterField(
            model_name='license',
            name='expired',
            field=pgcrypto.fields.EncryptedDateTimeField(charset='utf-8', check_armor=True, cipher='aes', default=datetime.datetime(2021, 12, 4, 18, 34, 12, 741665, tzinfo=utc), versioned=False),
        ),
        migrations.AlterField(
            model_name='license',
            name='validated',
            field=pgcrypto.fields.EncryptedDateTimeField(charset='utf-8', check_armor=True, cipher='aes', default=django.utils.timezone.now, versioned=False),
        ),
    ]
