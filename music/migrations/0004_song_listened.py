# Generated by Django 3.2.14 on 2022-07-24 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_song_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='listened',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
