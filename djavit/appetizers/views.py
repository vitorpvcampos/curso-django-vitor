from django.shortcuts import render, get_object_or_404

from djavit.appetizers.models import Video

videos = [
    Video(slug='test', title='Appetizer Video: Test', vimeo_id='431952852'),
    Video(slug='beach', title='Appetizer Video: Beach', vimeo_id='434093274'),
]

videos_dct = {v.slug: v for v in videos}


def index(request):
    return render(request, 'appetizers/index.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'appetizers/video.html', context={'video': video})
