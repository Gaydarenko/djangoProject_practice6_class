from django.urls import path
from .views import BookListView, BookView

urlpatterns = [
    path('books/', BookListView.as_view()),
    path('books/<int:book_id>', BookView.as_view()),
]