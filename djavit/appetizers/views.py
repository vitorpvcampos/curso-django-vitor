from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, title, vimeo_id):
        self.slug = slug
        self.title = title
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('appetizers:video', args=(self.slug,))


videos = [
    Video('test', 'Appetizer Video: Test', 431952852),
    Video('beach', 'Appetizer Video: Beach', 434093274),
]

videos_dct = {v.slug: v for v in videos}


def index(request):
    return render(request, 'appetizers/index.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'appetizers/video.html', context={'video': video})
