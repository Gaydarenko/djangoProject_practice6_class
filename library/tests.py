import json

from django.test import TestCase, Client
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
        # print(response)
        self.assertEqual(response.status_code, 200)

        data = response.json()      # json.loads(response.body)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0], self.book1)
        self.assertEqual(data[1], self.book2)
        # print(data)

    def test_book(self):
        client = Client()
        # response1 = client.get('/books/1')
        # data1 = response1.json()
        # self.assertEqual(response1.status_code, 200)
        # self.assertIsInstance(data1, dict)
        # self.assertEqual(len(data1), 4)
        # self.assertEqual(data1['id'], self.book1['id'])
        #
        # response2 = client.get('/books/2')
        # data2 = response2.json()
        # self.assertEqual(response1.status_code, 200)
        # self.assertIsInstance(data2, dict)
        # self.assertEqual(len(data2), 4)
        # self.assertEqual(data2['id'], self.book2['id'])

        for i in range(1, 3):
            response = client.get(f'/books/{i}')
            data = response.json()
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(data, dict)
            self.assertEqual(len(data), 4)
            self.assertEqual(data['id'], i)

    def test_book_not_exist(self):
        client = Client()
        response = client.get('/books/21')
        self.assertEqual(response.status_code, 404)

        data = response.json()
        self.assertEqual(data['error'], 'not found')

    def test_book_delete(self):
        client = Client()
        response = client.delete('/books/2')
        self.assertEqual(response.status_code, 204)

        response = client.get('/books/2')
        self.assertEqual(response.status_code, 404)

    def test_book_create(self):
        client = Client()
        test_book = {
            "name": 'book3',
            "author_name": "author3",
            "publish_date": "2003-03-03"
        }
        test_book_wrong = {
            "name": 'book3',
            "author_name": "author3",
            "publish_date": "test"
        }

        response = client.post('/books/', json.dumps(test_book), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        print(response.json())

        response = client.post('/books/', 'sfhggbs/.;fklgjl', content_type="application/json")
        self.assertEqual(response.status_code, 400)
