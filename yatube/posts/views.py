from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request):
    return HttpResponse('Страница с группами')


def group_posts_detail(request, pk):
    return HttpResponse(f'Пост номер {pk}')


# Create your views here.
