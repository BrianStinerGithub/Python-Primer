# Generated by Django 4.0.4 on 2022-04-21 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Videos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='channel',
        ),
        migrations.AlterField(
            model_name='channel',
            name='playlists',
            field=models.ManyToManyField(blank=True, related_name='channel_playlists', to='Videos.playlist'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='subcriptions',
            field=models.ManyToManyField(blank=True, related_name='subscriptions', to='Videos.channel'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='subscribers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='channel',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='videos',
            field=models.ManyToManyField(blank=True, related_name='channel_videos', to='Videos.video'),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='dislikes',
        ),
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='comment_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='replies',
            field=models.ManyToManyField(blank=True, related_name='comment_replies', to='Videos.comment'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='channel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Videos.channel'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='videos',
            field=models.ManyToManyField(blank=True, related_name='playlist_videos', to='Videos.video'),
        ),
        migrations.AlterField(
            model_name='video',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='video_comments', to='Videos.comment'),
        ),
        migrations.RemoveField(
            model_name='video',
            name='dislikes',
        ),
        migrations.AddField(
            model_name='video',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='video_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='video',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='video',
            name='likes',
        ),
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='video_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbnailurl',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.URLField(max_length=255),
        ),
        migrations.AlterField(
            model_name='video',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
