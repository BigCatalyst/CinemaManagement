# Generated by Django 3.1.12 on 2021-08-08 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20210714_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=500, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='GameCapture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.imagefile')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='captures', to='game.game')),
            ],
        ),
    ]