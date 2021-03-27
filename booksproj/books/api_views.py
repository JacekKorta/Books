import django_filters

from django.core.exceptions import FieldError
from django.http import Http404
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Response

from books.auxiliary.google_books_api import GoogleBooksApiHandler
from .models import Author, Book
from .serializers import BookSerializer


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BooksList(generics.ListAPIView):
    queryset = Book.objects.prefetch_related('authors').all()
    serializer_class = BookSerializer
    filterset_fields = ['published_date']
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['published_date']

    def get_queryset(self):
        queryset = Book.objects.prefetch_related('authors').all().order_by('id')
        query_authors = self.clear_authors_query_params_data()
        query_date = self.request.query_params.get('published_date')
        if query_authors:
            authors_ids = [
                author.id for author in Author.objects.filter(name__in=query_authors)
            ]
            queryset = queryset.filter(authors__in=authors_ids)
        if query_date is not None:
            queryset = queryset.filter(published_date__startswith=query_date)
        return queryset

    def clear_authors_query_params_data(self):
        authors = [
            author.replace("'", "").replace('"', '')
            for author in self.request.query_params.getlist('author')
        ]
        return authors


class DbImportView(APIView):

    def post(self, request, format=None):
        q = request.data.get("q")
        if q:
            gapi = GoogleBooksApiHandler()
            gapi.get_all_books(q)
            return Response(status=200)
        else:
            return Response(status=400)
