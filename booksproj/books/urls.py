from django.urls import include, path

from books import api_views


app_name = 'books'

urlpatterns = [
    path('books/', api_views.BooksView.as_view(), name='books'),
    ]