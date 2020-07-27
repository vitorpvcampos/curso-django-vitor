from typing import List

from django.db.models import Prefetch

from djavit.modules.models import Module, Classs


def list_ordered_modules() -> List[Module]:
    """
    List of modules ordered by titles
    :return:
    """
    return list(Module.objects.order_by('order').all())


def find_module(slug: str) -> Module:
    return Module.objects.get(slug=slug)


def list_ordered_module_classes(module: Module):
    return list(module.classs_set.order_by('order').all())


def find_classs(slug):
    return Classs.objects.select_related('module').get(slug=slug)


def list_modules_with_classes():
    ordered_classes = Classs.objects.order_by('order')
    return Module.objects.order_by('order').prefetch_related(
        Prefetch('classs_set', queryset=ordered_classes, to_attr='classes')
    ).all()
