# Generated by Django 4.0.1 on 2022-01-26 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0003_like_dislike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
