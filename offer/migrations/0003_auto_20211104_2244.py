# Generated by Django 3.2.9 on 2021-11-05 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_auto_20210823_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='amount',
            field=models.IntegerField(blank=True, db_column='Cantidad', null=True, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.TextField(blank=True, db_column='Descripcion', null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='name',
            field=models.TextField(db_column='Oferta', verbose_name='Oferta'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='photo',
            field=models.ImageField(blank=True, db_column='Foto', null=True, upload_to='ofertas/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='price',
            field=models.TextField(blank=True, db_column='Precio', null=True, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='type',
            field=models.TextField(blank=True, db_column='TipoOferta', null=True, verbose_name='Tipo'),
        ),
    ]
