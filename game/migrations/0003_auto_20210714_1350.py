# Generated by Django 3.1.12 on 2021-07-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20210713_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, db_column='FotoCategoria', null=True, upload_to=''),
        ),
    ]
