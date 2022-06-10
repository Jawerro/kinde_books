from ast import arg
from enum import unique
from tabnanny import verbose
from django.db import models
from django.forms import CharField
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name = 'Автор')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']


class Book(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name = 'Название',
                     blank=False)
    genre = models.CharField(max_length=100, verbose_name='Жанр', blank=True)
    series = models.CharField(max_length=100, verbose_name='Серия', blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET('Автор неизвестен'))
    read = models.BooleanField(default=False)
    download = models.BooleanField(default=False)
    file = models.FileField(upload_to='books/', verbose_name='Файл', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:book_detail', args=[str(self.id)])

    class Meta:
            verbose_name = 'Книга'
            verbose_name_plural = 'Книги'
            ordering = ['name']
            
