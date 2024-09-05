from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from store.serializers import BooksSerializer
from store.models import Book


class BooksApiTestCase(APITestCase):
    def test_get(self):
        book_1 = Book.objects.create(name='Test book 1', price=10.00)
        book_2 = Book.objects.create(name='Test book 2', price=17.00)
        url = reverse('book-list')
        response = self.client.get(url)
        serial_data = BooksSerializer([book_1, book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serial_data, response.data)


