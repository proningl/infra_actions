from django.http import HttpResponse


def index(request):
    return HttpResponse('У Глеба получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
