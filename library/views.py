from django.shortcuts import render
from django.views import View


# Create your views here.
class BookListView(View):
    def get(self, request):
        ...

    def post(self, request):
        ...


class BookView(View):
    def get(self, request, book_id):
        ...

    def post(self, request, book_id):
        ...

    def delete(self, request, book_id):
        ...