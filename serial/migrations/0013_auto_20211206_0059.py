# Generated by Django 3.2.9 on 2021-12-06 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serial', '0012_alter_serial_origen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serial',
            name='actor',
        ),
        migrations.DeleteModel(
            name='ActorSeries',
        ),
    ]
