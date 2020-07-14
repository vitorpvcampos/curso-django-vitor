import pytest
from django.urls import reverse
from model_bakery import baker

from djavit.django_assertions import assert_contains
from djavit.modules.models import Module


@pytest.fixture
def modules(db):
    return baker.make(Module, 2)


@pytest.fixture
def resp(client, modules):
    resp = client.get(reverse('base:home'))
    return resp


def test_modules_titles(resp, modules):
    for module in modules:
        assert_contains(resp, module.title)


def test_modules_link(resp, modules):
    for module in modules:
        assert_contains(resp, module.get_absolute_url())
