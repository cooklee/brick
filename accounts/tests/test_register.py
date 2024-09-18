from django.contrib.auth.models import User
from django.test import Client as Browser
from django.urls import reverse
import pytest

def test_register():
    client = Browser()
    url = reverse('accounts:register')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_register_post():
    client = Browser()
    url = reverse('accounts:register')
    data = {
        'username': 'testuser',
        'password': 'testpassword',
        'first_name': 'testfirst',
        'last_name': 'testlast',
        'email': 'test@test.pl'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert User.objects.get(username='testuser')
    assert response.url == reverse('index')