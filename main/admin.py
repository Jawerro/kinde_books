from django.contrib import admin

from .models import Author, Book


class BookAdmin(admin.ModelAdmin):
    fields = ['name', 'genre', 'read']


admin.site.register(Book, BookAdmin)
admin.site.register(Author)