def middleawre(get_response):
    def middleware_callable(request):
        print('AAAAAAAAAAAAAa')
        return get_response(request)
    return middleware_callable

# инициализация (передается get_response)
# -> вызываемый объект