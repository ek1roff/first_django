from django.http import HttpResponse
from django.shortcuts import render

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]


def index(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'blog/index.html', context=context)


def about(request):
    return render(request, 'blog/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse('Добавить страницу')


def contact(request):
    return HttpResponse('Контакты')


def login(request):
    return HttpResponse('Войти')


def show_post(request, post_id):
    return HttpResponse(f'Статья с id = {post_id}')
