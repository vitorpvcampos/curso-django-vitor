from django.shortcuts import render


def video(resquest, slug):
    videos = {
        'test': {'title': 'Appetizer Video: Test', 'vimeo_id': 431952852},
        'beach': {'title': 'Appetizer Video: Beach', 'vimeo_id': 434093274},
    }
    video = videos[slug]
    return render(resquest, 'appetizers/video.html', context={'video': video})
