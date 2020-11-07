import time

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

def middleawre(get_response):
    def middleware_callable(request):
        start = time.time()
        rs = get_response(request)
        print('Request ', time.time() - start)
        return rs
    return middleware_callable

# инициализация (передается get_response)
# -> вызываемый объект


class Middleware:
    def __init__(self, get_response):   # def middleawre(get_response):
        self.get_response = get_response
        # возвращает созданный обьект, он вызываемый, потому что __call__

    def __call__(self, request):    # def middleware_callable(request):
        start = time.time()
        # return JsonResponse({})
        rs = self.get_response(request)
        print('Request in class ', time.time() - start)
        return rs

    def process_exception(self, request, exception):
        if isinstance(exception, ObjectDoesNotExist):
            print("response from middleware")
            return JsonResponse({'error': 'not found'}, status=404)

        # if isinstance(exception, ValueError):
        #     return JsonResponse({'error': 'not valid data'}, status=400)

class MiddlewareValidation:
    def __init__(self, get_response):   # def middleawre(get_response):
        self.get_response = get_response
        # возвращает созданный обьект, он вызываемый, потому что __call__

    def __call__(self, request):    # def middleware_callable(request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if isinstance(exception, ValueError):
            return JsonResponse({'error': 'not valid data'}, status=400)