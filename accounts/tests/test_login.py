import pytest
from django.contrib.auth.models import User, AnonymousUser
from django.test import Client as Browser
from django.urls import reverse

@pytest.mark.django_db
def test_login():
    client = Browser()
    url = reverse('accounts:login')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_post(user):
    client = Browser()
    url = reverse('accounts:login')
    data = {
        'username': 'testuser',
        'password': 'test'
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert response.context['user'] == user

@pytest.mark.django_db
def test_logout(user):
    client = Browser()
    client.force_login(user)
    url = reverse('accounts:logout')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['user'] == AnonymousUser()