from django.urls import path
from .views import BookListView, BookView

urlpatterns = [
    path(r'books/', BookListView.as_view()),
    path(r'books/<int:book_id>', BookView.as_view()),
]
