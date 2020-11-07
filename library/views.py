from django.forms import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View


from.models import Book


# Create your views here.
class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return JsonResponse([model_to_dict(book) for book in books], safe=False)

    def post(self, request):
        ...


class BookView(View):
    def get(self, request, book_id):
        # try:
        #     book = Book.objects.get(pk=book_id)   # not found?
        # except Book.DoesNotExist:
        #     return JsonResponse({'error': 'not found'}, status=404)

        book = Book.objects.get(pk=book_id)   # not found?
        return JsonResponse(model_to_dict(book))

    def post(self, request, book_id):
        ...

    def delete(self, request, book_id):
        # ...
        # book = Book.objects.get(pk=book_id)
        # book.objects.delete()
        Book.objects.filter(id=book_id).delete()
        return HttpResponse(status=204)