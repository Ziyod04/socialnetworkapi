# Generated by Django 4.0.1 on 2022-01-26 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialnetwork', '0002_alter_post_dislikes_alter_post_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.SmallIntegerField(default=0)),
                ('like_published', models.DateField(auto_now_add=True, verbose_name='%Y-%m-%d')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_post', to='socialnetwork.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dislike', models.SmallIntegerField(default=0)),
                ('dislike_published', models.DateField(auto_now_add=True, verbose_name='%Y-%m-%d')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislike_post', to='socialnetwork.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislike_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
