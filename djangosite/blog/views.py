from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from .models import *
from .forms import *
from .utils import *


class BlogHome(DataMixin, ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


# def index(request):
#     posts = Blog.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'blog/index.html', context=context)


def about(request):
    return render(request, 'blog/about.html', {'menu': menu, 'title': 'О сайте'})


class AddPage(DataMixin, LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/addpage.html'
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'blog/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse('Контакты')


# def login(request):
#     return HttpResponse('Войти')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def show_post(request, post_slug):
#     post = get_object_or_404(Blog, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'blog/post.html', context=context)


class ShowPost(DataMixin, DeleteView):
    model = Blog
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class BlogCategory(DataMixin,ListView):

    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Blog.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


# def show_category(request, cat_slug):
#     cat = Category.objects.get(slug=cat_slug)
#     posts = Blog.objects.filter(cat_id=cat.id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat.id,
#     }
#
#     return render(request, 'blog/index.html', context=context)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')
 
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'blog/login.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))
