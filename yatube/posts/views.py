from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    description = "Это главная страница проекта Yatube"
    posts = Post.objects.order_by('-pub_date')[:10]
    context: dict[str, str] = {
        'title': title,
        'description': description,
        'posts': posts
        }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Лев Толстой – зеркало русской революции.'
    description = "Здесь будет информация о группах проекта Yatube"
    context: dict[str, str] = {
        'title': title,
        'description': description
        }
    return render(request, template, context)
