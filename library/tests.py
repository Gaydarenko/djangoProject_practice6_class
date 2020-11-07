from django.test import TestCase, Client


# Create your tests here.
from library.models import Book


class BooksTestCase(TestCase):
    book1 = {
        "id": 1,
        "name": "book1",
        "author_name": "author1",
        "publish_date": "2020-01-20"
    }
    book2 = {
        "id": 2,
        "name": "book2",
        "author_name": "author2",
        "publish_date": "2019-12-21"
    }

    def setUp(self):
        book1 = Book.objects.create(**self.book1)
        book2 = Book.objects.create(**self.book2)

    def test_books_list(self):
        client = Client()
        response = client.get('/books/')
        print(response)
