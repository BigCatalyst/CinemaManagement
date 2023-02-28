# Generated by Django 3.1.12 on 2021-11-04 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_auto_adding_tasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_id', models.CharField(max_length=200, unique=True, verbose_name='Licencia')),
                ('key', models.TextField(verbose_name='LLave de activación')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]