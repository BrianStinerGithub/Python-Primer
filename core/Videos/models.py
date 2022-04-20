import uuid
import logging
from unicodedata import category, decimal
from django.db import models
from core.settings import LANGUAGE_CODE
from uuid import uuid4

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_h = logging.FileHandler('importing_errors.log')
file_h.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
file_h.setFormatter(formatter)


Editable = True
# TODO: Make this editable=False before deployment.

class Channel(models.Model):

    try:
        uuid =          models.UUIDField(default=uuid4, editable=Editable, unique=True)
        name =          models.CharField(max_length=255)
        about =         models.TextField(blank=True)
        views =         models.IntegerField(default=0)
        location =      models.CharField(max_length=255, blank=True)
        category =      models.CharField(max_length=255, blank=True)
        owner =         models.ForeignKey('auth.User',on_delete=models.SET_DEFAULT, default=1)
        icon =          models.ImageField(upload_to='Videos/Channels/icons/',blank=True)
        banner =        models.ImageField(upload_to='Videos/Channels/banners/',blank=True)
        subscribers =   models.ManyToManyField('auth.User', related_name='subscribers', blank=True)
        videos =        models.ManyToManyField('Video', related_name='channel_videos', blank=True)
        subcriptions =  models.ManyToManyField('Channel', related_name='subscriptions', blank=True)
        playlists =     models.ManyToManyField('Playlist', related_name='channel_playlists', blank=True)
        created_at =    models.DateTimeField(auto_now_add=True)
        updated_at =    models.DateTimeField(auto_now=True)
    except TypeError:
        logger.exception('A field was not correctly filled out when attempting to add a channel')



class Playlist(models.Model):
    try:
        uuid =          models.UUIDField(default=uuid4, editable=Editable, unique=True)
        name =          models.CharField(max_length=255)
        about =         models.TextField(blank=True)
        duration =      models.IntegerField(default=0)
        views =         models.IntegerField(default=0)
        videos =        models.ManyToManyField('Video', related_name='playlist_videos', blank=True)
        channel =       models.ForeignKey('Channel',on_delete=models.SET_DEFAULT, default=1)
        created_at =    models.DateTimeField(auto_now_add=True)
        updated_at =    models.DateTimeField(auto_now=True)
    except TypeError:
        logger.exception('A field was not correctly filled out when attempting to add a playlist')


class Video(models.Model):

    try:
        uuid =          models.UUIDField(default=uuid4, editable=Editable, unique=True)
        name =          models.CharField(max_length=255)
        url =           models.URLField(max_length=255)
        thumbnailurl =  models.URLField(max_length=255, blank=True)
        description =   models.TextField(blank=True)
        duration =      models.IntegerField(default=0)
        comments =      models.ManyToManyField('Comment', related_name='video_comments', blank=True)
        channel =       models.ForeignKey('Channel',on_delete=models.CASCADE, related_name='video_channel')
        # likes =         models.ManyToManyField('auth.User', related_name='video_likes', blank=True)
        # dislikes =      models.ManyToManyField('auth.User', related_name='video_dislikes', blank=True)
        likes =         models.IntegerField(default=0)
        dislikes =      models.IntegerField(default=0)
        views =         models.IntegerField(default=0)
        created_at =    models.DateTimeField(auto_now_add=True)
        updated_at =    models.DateTimeField(auto_now=True)
    except TypeError:
        logger.exception('A field was not correctly filled out when attempting to add a video')

class Comment(models.Model):
    try:
        video =         models.ForeignKey('Video',on_delete=models.CASCADE)
        content =       models.TextField(max_length=1024)
        author =        models.ForeignKey('auth.User',on_delete=models.CASCADE)
        likes =         models.ManyToManyField('auth.User', related_name='comment_likes', blank=True)
        dislikes =      models.ManyToManyField('auth.User', related_name='comment_dislikes', blank=True)
        replies =       models.ManyToManyField('Comment', related_name='comment_replies', blank=True)
        created_at =    models.DateTimeField(auto_now_add=True)
        updated_at =    models.DateTimeField(auto_now=True)
    except TypeError:
        logger.exception('A field was not correctly filled out when attempting to add a comment')
