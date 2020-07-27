from typing import List

import pytest
from django.urls import reverse
from model_bakery import baker

from djavit.django_assertions import assert_contains
from djavit.modules.models import Module, Classs


@pytest.fixture
def modules(db):
    return baker.make(Module, 2)


@pytest.fixture
def classes(modules):
    classes = []
    for module in modules:
        classes.extend(baker.make(Classs, 3, module=module))
    return classes


@pytest.fixture
def resp(client, modules, classes):
    resp = client.get(reverse('modules:index'))
    return resp


def test_available_index(resp):
    assert resp.status_code == 200


def test_title(resp, modules: List[Module]):
    for module in modules:
        assert_contains(resp, module.title)


def test_description(resp, modules: List[Module]):
    for module in modules:
        assert_contains(resp, module.description)


def test_public(resp, modules: List[Module]):
    for module in modules:
        assert_contains(resp, module.public)


def test_classes_titles(resp, classes: List[Classs]):
    for classs in classes:
        assert_contains(resp, classs.title)


def test_classes_urls(resp, classes: List[Classs]):
    for classs in classes:
        assert_contains(resp, classs.get_absolute_url())
