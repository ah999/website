# Generated by Django 2.2b1 on 2019-03-07 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_album_album_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
