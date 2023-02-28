# Generated by Django 3.1.12 on 2021-07-13 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Nombre', null=True)),
                ('photo', models.TextField(blank=True, db_column='FotoCategoria', null=True)),
            ],
            options={
                'db_table': 'juegoscategorias',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Nombre', null=True)),
                ('year', models.IntegerField(blank=True, db_column='Anno', null=True)),
                ('photo', models.ImageField(blank=True, db_column='Foto', null=True, upload_to='')),
                ('manual', models.FileField(blank=True, db_column='Manual', null=True, upload_to='')),
                ('synopsis', models.TextField(blank=True, db_column='Sinopsis', null=True)),
                ('type', models.TextField(blank=True, db_column='Tipo', null=True)),
                ('size', models.TextField(blank=True, db_column='Tamano', null=True)),
                ('requirement', models.TextField(blank=True, db_column='Requisitos', null=True)),
                ('capture', models.ImageField(blank=True, db_column='Capturas', null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, db_column='IdCategoria', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='game.category')),
            ],
            options={
                'db_table': 'juegos',
            },
        ),
    ]
