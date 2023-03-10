# Generated by Django 3.2 on 2021-08-23 07:27

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0020_rename_name_dvdsong_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('title',), 'verbose_name': 'Album', 'verbose_name_plural': 'Albums'},
        ),
        migrations.AlterModelOptions(
            name='albumsong',
            options={'verbose_name': 'Canción del Album', 'verbose_name_plural': 'Canciones del Album'},
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'verbose_name': 'Colección', 'verbose_name_plural': 'Colecciones'},
        ),
        migrations.AlterModelOptions(
            name='concert',
            options={'verbose_name': 'Concierto', 'verbose_name_plural': 'Conciertos'},
        ),
        migrations.AlterModelOptions(
            name='dvd',
            options={'verbose_name': 'DVD', 'verbose_name_plural': 'DVDs'},
        ),
        migrations.AlterModelOptions(
            name='dvdsong',
            options={'verbose_name': 'Canción del DVD', 'verbose_name_plural': 'Canciones del DVD'},
        ),
        migrations.AlterModelOptions(
            name='gendermusic',
            options={'ordering': ('name',), 'verbose_name': 'Género Musical', 'verbose_name_plural': 'Géneros Musicales'},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': (django.db.models.expressions.OrderBy(django.db.models.expressions.F('success'), descending=True, nulls_last=True), 'title'), 'verbose_name': 'Canción', 'verbose_name_plural': 'Canciones'},
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(blank=True, db_column='Titulo', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='albumsong',
            name='title',
            field=models.CharField(blank=True, db_column='Titulo', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, db_column='Nombre', max_length=500, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(blank=True, db_column='Nombre', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='definition',
            field=models.CharField(blank=True, db_column='Definicion', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='interpreter',
            field=models.CharField(blank=True, db_column='Interprete', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='place',
            field=models.CharField(blank=True, db_column='Lugar', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='title',
            field=models.CharField(blank=True, db_column='Titulo', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='dvdsong',
            name='title',
            field=models.CharField(blank=True, db_column='Nombre', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(blank=True, db_column='TituloCancion', max_length=500, null=True),
        ),
    ]
