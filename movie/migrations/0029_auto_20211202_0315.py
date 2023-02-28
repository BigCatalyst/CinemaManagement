# Generated by Django 3.2.9 on 2021-12-02 08:15

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0028_alter_actor_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documental',
            name='origen',
            field=django_countries.fields.CountryField(blank=True, db_column='Origen', max_length=500, null=True, verbose_name='País de origen'),
        ),
        migrations.AlterField(
            model_name='humor',
            name='origen',
            field=django_countries.fields.CountryField(blank=True, db_column='Origen', max_length=500, null=True, verbose_name='País de origen'),
        ),
    ]
