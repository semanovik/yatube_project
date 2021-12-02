from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='main'),
    path('group/', views.group_posts, name='group'),
    path('group/<slug:pk>/', views.group_posts_detail)
]
