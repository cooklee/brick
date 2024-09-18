import pytest
from django.contrib.auth.models import User
from django.test import Client as Browser
from django.urls import reverse


@pytest.mark.django_db
def test_delete_user_not_login():
    client = Browser()
    url = reverse('accounts:delete_account')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('accounts:login'))

@pytest.mark.django_db
def test_delete_user(user):
    client = Browser()
    client.force_login(user)
    url = reverse('accounts:delete_account')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_user_post_yes(user):
    client = Browser()
    client.force_login(user)
    url = reverse('accounts:delete_account')
    data = {
        'operation': 'Tak'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert not User.objects.filter(username='testuser').exists()
    assert response.url == reverse('index')


@pytest.mark.django_db
def test_delete_user_post_no(user):
    client = Browser()
    client.force_login(user)
    url = reverse('accounts:delete_account')
    data = {
        'operation': 'Nie'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse('accounts:profile')
