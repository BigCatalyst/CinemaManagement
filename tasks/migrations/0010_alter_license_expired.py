# Generated by Django 3.2.9 on 2021-11-05 02:37

import datetime
from django.db import migrations
from django.utils.timezone import utc
import pgcrypto.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_alter_license_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='expired',
            field=pgcrypto.fields.EncryptedDateTimeField(charset='utf-8', check_armor=True, cipher='aes', default=datetime.datetime(2021, 12, 5, 2, 35, 44, 432766, tzinfo=utc), versioned=False),
        ),
    ]
