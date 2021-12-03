from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Post(models.Model):
    # Содержание поста, текстовое поле
    text = models.TextField()

    # Дата публикации, хранит дату и время
    # Параметр auto_now_add определяет, что в поле будет автоматически подставлено
    # время и дата создания новой записи
    pub_date = models.DateTimeField(auto_now_add=True)

    # Ссылка на модель User, ForeignKey
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
        )
        




# Create your models here.
