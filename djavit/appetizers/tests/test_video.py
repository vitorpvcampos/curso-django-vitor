import pytest
from django.urls import reverse
from model_bakery import baker

from djavit.appetizers.models import Video
from djavit.django_assertions import assert_contains


@pytest.fixture
def video(db):
    return baker.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse('appetizers:video', args=(video.slug,)))


@pytest.fixture
def resp_video_not_found(client, video):
    return client.get(reverse('appetizers:video', args=(video.slug + 'video_not_found',)))


def test_status_code_video_not_found(resp_video_not_found):
    assert resp_video_not_found.status_code == 404


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp, video):
    assert_contains(resp, video.title)


def test_content_video(resp, video):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}"')
