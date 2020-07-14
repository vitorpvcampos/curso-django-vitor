from typing import List

from djavit.modules.models import Module


def list_ordered_modules() -> List[Module]:
    """
    List of modules ordered by titles
    :return:
    """
    return list(Module.objects.order_by('order').all())


def find_module(slug: str) -> Module:
    return Module.objects.get(slug=slug)
