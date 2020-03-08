from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Video

# Create your views here.

def index(request):
    all_videos = Video.objects.all()
    return render(request, 'video/index.html', {'all_videos' : all_videos})

def detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'video/detail.html', {'video' : video})

