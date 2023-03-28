from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect


def index(request):
    return HttpResponse('Страница приложения blog')


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Страница по категориям</h1><p>{catid}</p>')


def archive(request, year):
    if int(year) == 2020:
        return redirect('https://www.google.ru')

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
