import pytest
from django.contrib.auth.models import User
from django.test import Client as Browser
from django.urls import reverse


@pytest.mark.django_db
def test_change_password_user_not_login():
    client = Browser()
    url = reverse('accounts:change_password')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('accounts:login'))



@pytest.mark.django_db
def test_change_password(user):
    client = Browser()
    client.force_login(user)
    url = reverse('accounts:change_password')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_change_password_post(user):
    client = Browser()
    client.force_login(user)
    url = reverse('accounts:change_password')
    data = {
        'old_password': 'test',
        'password': 'newpassword',
        'confirm_password': 'newpassword'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    user = User.objects.get(username='testuser')
    assert user.check_password('newpassword')
    assert response.url == reverse('index')