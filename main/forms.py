from attr import field
from django import forms

from .views import Book, Author


class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ['name', 'genre', 'series', 'author', 'file']
