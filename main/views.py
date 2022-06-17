from django.contrib import messages
from django.urls import reverse
from django.views import generic
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail, EmailMessage
from kindle_books import settings
import os
from decouple import config


from .models import Author, Book
from .forms import BookForm, AuthorForm


# отправка файла на почту kindle
def send_email(request, pk):
        book = Book.objects.get(id=pk)
        email_recipient = []
        email_recipient.append(config('email_recipient', default=''))
        email = EmailMessage(
            book.name,
            '',
            settings.EMAIL_HOST_USER,
            email_recipient,

        )
        try:
            email.attach_file(book.file.path)
        except FileNotFoundError:
            messages.error(request, 'Файл не существует')
            return redirect('main:index')
        try:
            email.send()
            book.download = True
            book.save()
            messages.success(request, 'Файл отправлен')
            return redirect('main:index')
        except:
            messages.error(request, email)
            messages.error(request, 'Ошибка.Файл не отправлен')
            return redirect('main:book_detail', pk)
            
   

#добавление автора
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:add_book')
    else:
        form = AuthorForm()
        return render(request, 'main/add_author.html', {'form':form})


# добавление новой книги
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                            'Обьявление добавлено')
            return redirect('main:index')
    else:
        form = BookForm()
        return render(request, 'main/add_book.html', {'form': form})

# просмотр сведений об авторе
def view_author(request, author):
    author = Author.objects.get(name=author)    
    books = Book.objects.filter(author=author)
    context = {'books': books, 'author': author}
    return render(request, 'main/author_detail.html', context)

def search_author(request, author_id):
    author = Author.objects.get(id=author_id)
    return HttpResponse(author.name)

class IndexView(generic.ListView):
    model = Book
    template_name = 'main/index.html'
    context_object_name = 'books'
    queryset = Book.objects.all()


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'main/book_detail.html'


class UpdateBookView(SuccessMessageMixin, UpdateView):
    model = Book
    template_name = 'main/add_book.html'
    form_class = BookForm
    success_message = 'Информация о книге изменена'


class DeleteBook(SuccessMessageMixin, DeleteView):
    model = Book
    template_name = 'main/delete_book.html'
    success_message = 'Книга удалена'
    success_url = reverse_lazy('main:index')

class ReadedBooks(generic.ListView):
    model = Book
    template_name = 'main/readed.html'
    context_object_name = 'books'
    queryset = Book.objects.filter(read=True)






