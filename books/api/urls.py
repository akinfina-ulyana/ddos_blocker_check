from django.urls import path
from .views import BookAPIView, BookCreateView, BookDetailView, BookPriceView

urlpatterns = [
    path('books/', BookAPIView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/price/<str:name>/', BookPriceView.as_view(), name='book-price'),
]
