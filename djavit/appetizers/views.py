from django.shortcuts import render

from djavit.appetizers.models import Video

videos = [
    Video(slug='test', title='Appetizer Video: Test', vimeo_id='431952852'),
    Video(slug='beach', title='Appetizer Video: Beach', vimeo_id='434093274'),
]

videos_dct = {v.slug: v for v in videos}


def index(request):
    return render(request, 'appetizers/index.html', context={'videos': videos})


def video(request, slug):
    video = Video.objects.get(slug=slug)
    return render(request, 'appetizers/video.html', context={'video': video})
