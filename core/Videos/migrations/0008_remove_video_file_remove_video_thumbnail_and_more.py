# Generated by Django 4.0.3 on 2022-04-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Videos', '0007_video_created_at_video_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='file',
        ),
        migrations.RemoveField(
            model_name='video',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='video',
            name='thumbnailurl',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.URLField(default='https://i.imgur.com/IpusefR.mp4', max_length=255),
            preserve_default=False,
        ),
    ]