from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'main'
urlpatterns = [
    path('book/<int:pk>/delete', views.DeleteBook.as_view(), name='delete_book'),
    path('book/<int:pk>/change', views.UpdateBookView.as_view(), name='change_book'),
    path('book/<int:pk>/', views.DetailView.as_view(), name='book_detail'),
    path('book/add_book/', views.add_book, name='add_book'),
    path('', views.IndexView.as_view(), name='index'),
    path('author/<int:author_id>', views.search_author, name='search_author'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)