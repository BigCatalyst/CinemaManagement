# Generated by Django 3.2.9 on 2021-11-05 01:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import pgcrypto.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20211104_1434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='license',
            options={'ordering': ('-id',), 'verbose_name': 'Licencia'},
        ),
        migrations.AlterField(
            model_name='license',
            name='expired',
            field=pgcrypto.fields.EncryptedDateTimeField(charset='utf-8', check_armor=True, cipher='aes', default=datetime.datetime(2021, 12, 5, 1, 18, 25, 555926, tzinfo=utc), versioned=False),
        ),
        migrations.AlterField(
            model_name='license',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='license',
            name='license_id',
            field=models.CharField(max_length=200, unique=True, verbose_name='Código de Activación'),
        ),
    ]
