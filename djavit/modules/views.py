from django.shortcuts import render

from djavit.modules import facade


def detail(request, slug):
    module = facade.find_module(slug)
    classes = facade.list_ordered_module_classes(module)
    return render(request, 'modules/module_detail.html', {'module': module, 'classes': classes})


def classs(request, slug):
    classs = facade.find_classs(slug)
    return render(request, 'modules/classs_detail.html', {'classs': classs})
