# Generated by Django 4.0.3 on 2022-04-15 19:39

from django.db import migrations, models
import django.utils.timezone
import uuid
import random as rnd


class Migration(migrations.Migration):

    dependencies = [
        ('Videos', '0011_remove_comment_uuid_comment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='id',
            field=models.BigAutoField(auto_created=True, default=rnd.randint(1,199), primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playlist',
            name='id',
            field=models.BigAutoField(auto_created=True, default=rnd.randint(1,100), primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='id',
            field=models.BigAutoField(auto_created=True, default=rnd.randint(1,100), primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='channel',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
