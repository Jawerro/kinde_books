from django.contrib import messages
from django.urls import reverse
from django.views import generic
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


from .models import Author, Book
from .forms import BookForm

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



class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'books'
    queryset = Book.objects.all()


class DetailView(generic.DetailView):
    model = Book
    template_name = 'main/detail.html'


class UpdateBookView(SuccessMessageMixin, UpdateView):
    model = Book
    template_name = 'main/add_book.html'
    form_class = BookForm
    success_message = 'Информация о книге изменена'


class DeleteBook(SuccessMessageMixin, DeleteView):
    model = Book
    template_name = 'main/delete_book.html'
    success_url = reverse_lazy('main:index')


def search_author(request, author_id):
    author = Author.objects.get(id=author_id)
    return HttpResponse(author.name)



