from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group

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
    title = str(Group.title)
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context: dict[str, str] = {
        'group': group,
        'posts': posts,
        'title': title
        }
    return render(request, template, context)
