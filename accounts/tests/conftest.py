from django.contrib.auth.models import User
import pytest

@pytest.fixture
def user():
    user = User.objects.create_user(username='testuser',
                                    first_name='testfirst',
                                    last_name='testlast',
                                    password='test',
                                    email='test@test.pl')
    return user
