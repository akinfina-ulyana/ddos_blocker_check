from rest_framework import generics, status
from rest_framework.response import Response
from store.models import Book
from api.serializers import BooksSerializer


class BookAPIView(generics.ListAPIView):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BookPriceView(generics.GenericAPIView):
    serializer_class = BooksSerializer

    def get(self, request, name):
        try:
            book = Book.objects.get(name=name)
            return Response({'price': book.price}, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)