# Generated by Django 3.2.9 on 2021-11-10 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0024_auto_20211105_0816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentalseason',
            old_name='doumental',
            new_name='documental',
        ),
    ]
