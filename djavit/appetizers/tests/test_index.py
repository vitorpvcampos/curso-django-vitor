import pytest
from django.urls import reverse

from djavit.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('appetizers:index'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'title',
    [
        'Appetizer Video: Test',
        'Appetizer Video: Beach'
    ]
)
def test_title_video(resp, title):
    assert_contains(resp, title)


@pytest.mark.parametrize(
    'slug',
    [
        'test',
        'beach'
    ]
)
def test_link_video(resp, slug):
    video_link = reverse('appetizers:video', args=(slug,))
    assert_contains(resp, f'href="{video_link}"')
