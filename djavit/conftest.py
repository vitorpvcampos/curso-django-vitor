import pytest
from model_bakery import baker


@pytest.fixture
def logged_user(db, django_user_model):
    user_model = baker.make(django_user_model, first_name='Fulano')
    return user_model


@pytest.fixture
def client_with_logged_user(logged_user, client):
    client.force_login(logged_user)
    return client
