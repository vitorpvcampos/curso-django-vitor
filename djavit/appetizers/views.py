from django.shortcuts import render, get_object_or_404

from djavit.appetizers.models import Video


def index(request):
    videos = Video.objects.order_by('creation').all()
    return render(request, 'appetizers/index.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'appetizers/video.html', context={'video': video})
