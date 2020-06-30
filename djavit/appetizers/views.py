from django.shortcuts import render

videos = [
    {'slug': 'test', 'title': 'Appetizer Video: Test', 'vimeo_id': 431952852},
    {'slug': 'beach', 'title': 'Appetizer Video: Beach', 'vimeo_id': 434093274},
]

videos_dct = {dct['slug']: dct for dct in videos}


def index(request):
    return render(request, 'appetizers/index.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'appetizers/video.html', context={'video': video})
