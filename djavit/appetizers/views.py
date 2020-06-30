from django.shortcuts import render


def video(resquest, slug):
    video = {'title': 'Appetizer Video: Test', 'vimeo_id': 431952852}
    return render(resquest, 'appetizers/video.html', context={'video': video})
