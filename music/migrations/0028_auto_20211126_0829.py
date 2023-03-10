# Generated by Django 3.2.9 on 2021-11-26 13:29

from django.db import migrations
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0027_auto_20211113_0932 '),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('name',), 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ('name',), 'verbose_name': 'Colección', 'verbose_name_plural': 'Colecciones'},
        ),
        migrations.AlterModelOptions(
            name='concert',
            options={'ordering': ('interpreter',), 'verbose_name': 'Concierto', 'verbose_name_plural': 'Conciertos'},
        ),
        migrations.AlterModelOptions(
            name='dvd',
            options={'ordering': ('title',), 'verbose_name': 'DVD', 'verbose_name_plural': 'DVDs'},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': (django.db.models.expressions.OrderBy(django.db.models.expressions.F('success'), descending=True, nulls_last=True), django.db.models.expressions.OrderBy(django.db.models.expressions.F('video'), descending=True, nulls_last=True), 'title'), 'verbose_name': 'Canción', 'verbose_name_plural': 'Canciones'},
        ),
    ]
