# Generated by Django 3.2.9 on 2022-03-04 08:26

from django.db import migrations
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0029_updating_collection_photo_location '),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': (django.db.models.expressions.OrderBy(django.db.models.expressions.F('year'), descending=True, nulls_last=True), 'title'), 'verbose_name': 'Album', 'verbose_name_plural': 'Albums'},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': (django.db.models.expressions.OrderBy(django.db.models.expressions.F('success'), descending=True, nulls_last=True), 'title'), 'verbose_name': 'Canción', 'verbose_name_plural': 'Canciones'},
        ),
    ]
