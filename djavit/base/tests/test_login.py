import pytest
from django.urls import reverse
from model_bakery import baker

from djavit.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


def test_login_form_page(resp):
    assert resp.status_code == 200


@pytest.fixture
def user(db, django_user_model):
    user_model = baker.make(django_user_model)
    password = 'password'
    user_model.set_password(password)
    user_model.save()
    user_model.plane_password = password
    return user_model


@pytest.fixture
def resp_post(client, user):
    return client.post(reverse('login'), {'username': user.email, 'password': user.plane_password})


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('modules:index')


@pytest.fixture
def resp_home(client, db):
    return client.get(reverse('base:home'))


def test_login_button_available(resp_home):
    assert_contains(resp_home, 'Enter')


def test_login_link_available(resp_home):
    assert_contains(resp_home, reverse('login'))


@pytest.fixture
def resp_home_with_logged_user(client_with_logged_user, db):
    return client_with_logged_user.get(reverse('base:home'))


def test_login_button_unavailable(resp_home_with_logged_user):
    assert_not_contains(resp_home_with_logged_user, 'Enter')


def test_login_link_unavailable(resp_home_with_logged_user):
    assert_not_contains(resp_home_with_logged_user, reverse('login'))


def test_logout_button_available(resp_home_with_logged_user):
    assert_contains(resp_home_with_logged_user, 'Logout')


def test_name_logged_user_available(resp_home_with_logged_user, logged_user):
    assert_contains(resp_home_with_logged_user, logged_user.first_name)


def test_logout_link_unavailable(resp_home_with_logged_user):
    assert_contains(resp_home_with_logged_user, reverse('logout'))
