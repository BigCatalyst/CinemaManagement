# Generated by Django 3.2.9 on 2021-12-06 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0005_auto_20211130_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='especial',
            field=models.CharField(blank=True, db_column='Especial', max_length=1, null=True),
        ),
    ]