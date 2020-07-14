from django.shortcuts import render

from djavit.modules import facade


def detail(request, slug):
    module = facade.find_module(slug)
    return render(request, 'modules/module_detail.html', {'module': module})
