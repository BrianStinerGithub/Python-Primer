from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from . import models

def home(request):
    homepage_videos = models.Video.objects.all()
    return render(request, 'home.html', {'videos': homepage_videos})

# def main_list(request):
   # return render(request, '.html', {'videos': recommended_videos})

def upload(request):
    return render(request, 'upload.html')

def profile(request):
    return render(request, 'profile.html')

@require_http_methods(["GET"])
def watch(request, video_id):
    video = models.Video.objects.get(uuid=video_id)
    return render(request, 'watch.html', {'video': video})

@require_http_methods(["POST"])
def likeVideo(request, pk): 
    video = get_object_or_404(models.Video, id=request.POST.get('video_id'))
    video.likes += 1
    video.save()
    # return HttpResponseRedirect(reverse('article_detail'), args=[str(pk)])
    return render(request, 'watch.html', {'video': video})

@require_http_methods(["POST"])
def dislikeVideo(request, pk):
    video = get_object_or_404(models.Video, id=request.POST.get('video_id'))
    video.dislikes += 1
    video.save()
    # return HttpResponseRedirect(reverse('article_detail'), args=[str(pk)])
    return render(request, 'watch.html', {'video': video})

@require_http_methods(["GET"])
def view_channel(request, channel_id):
    channel = models.Channel.objects.get(uuid=channel_id)
    return render(request, 'view_channel.html', {'channel': channel})

@require_http_methods(["POST"])
def upload_video(request, video: models.Video):
    models.Video.objects.create(video)
    return redirect('home')

@require_http_methods(["POST, PUT"])
def update_video(request, video: models.Video):
    models.Video.objects.update(video)
    return redirect("home")

@require_http_methods(["POST, DELETE"])
def delete_video(request, video_id):
    video = models.Video.objects.get(uuid=video_id)
    models.Video.objects.delete(video)
    return redirect("home")

@require_http_methods(["POST"])
def create_channel(request, channel: models.Channel):
    models.Channel.objects.create(channel)
    return redirect('view_channel', channel.uuid)

@require_http_methods(["POST, PUT"])
def update_channel(request, channel: models.Channel):
    models.Channel.objects.update(channel)
    return redirect('view_channel', channel.uuid)

@require_http_methods(["POST, DELETE"])
def delete_channel(request, channel_id):
    channel = models.Channel.objects.get(uuid=channel_id)
    models.Channel.objects.delete(channel)
    return redirect("home")





