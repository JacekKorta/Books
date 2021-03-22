from django.urls import path

from books import api_views

app_name = 'books'

urlpatterns = [
    path('books/', api_views.BooksList.as_view(), name='books-list'),
    path('books/<int:pk>', api_views.BookDetail.as_view(), name='book-detail'),
    path('db/', api_views.DbImportView.as_view(), name='db-import'),
]
