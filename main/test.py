import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Book



class IndexViewTests(TestCase):

    def test_books_count(self):
        books_count = Book.objects.count()
        self.assertEqual(books_count, 4, msg='Test failed')
