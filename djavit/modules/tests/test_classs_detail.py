import pytest
from django.urls import reverse
from model_bakery import baker

from djavit.django_assertions import assert_contains
from djavit.modules.models import Module, Classs


@pytest.fixture
def module(db):
    return baker.make(Module)


@pytest.fixture
def classs(module):
    return baker.make(Classs, module=module)


@pytest.fixture
def resp(client, classs):
    resp = client.get(reverse('modules:classs', kwargs={'slug': classs.slug}))
    return resp


def test_title(resp, classs: Classs):
    assert_contains(resp, classs.title)


def test_vimeo(resp, classs: Classs):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{classs.vimeo_id}"')
