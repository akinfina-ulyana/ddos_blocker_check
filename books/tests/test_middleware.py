import pytest
from django.urls import reverse
from rest_framework import status
from django.conf import settings
import time

@pytest.mark.django_db
def test_middleware_blocks_ddos_anonymous(client):

    for _ in range(int(settings.REDIS_MAX_REQUESTS)-1):
        response = client.get(reverse('book-list'))
        assert response.status_code == status.HTTP_200_OK

    response = client.get(reverse('book-list'))
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_middleware_resets_after_time(client):
    for _ in range(int(settings.REDIS_MAX_REQUESTS)):
        client.get(reverse('book-list'))

    response = client.get(reverse('book-list'))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    time.sleep(int(settings.REDIS_TIMEOUT))

    response = client.get(reverse('book-list'))
    assert response.status_code == status.HTTP_200_OK