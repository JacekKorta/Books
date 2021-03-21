from django.core.exceptions import FieldError
from django.http import Http404
from rest_framework.views import APIView, Response

from .models import Author, Book
from .serializers import BookSerializer


class BooksList(APIView):

    def get_queryset(self):
        queryset = Book.objects.prefetch_related('authors').all()
        query_date = self.request.query_params.get('published_date', None)
        query_authors = [
            author.replace("'", "").replace('"', '')
            for author in self.request.query_params.getlist('author', None)
        ]
        sort = self.request.query_params.get('sort', None)
        if query_date is not None:
            queryset = queryset.filter(published_date=query_date)
        if query_authors:
            authors_ids = [
                author.id for author in Author.objects.filter(name__in=query_authors)
            ]
            queryset = queryset.filter(authors__in=authors_ids)
        if sort is not None:
            try:
                queryset = queryset.order_by(sort)
            except FieldError:
                return queryset
        return queryset

    def get(self, request, format=None):
        serializer = BookSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class BookDetail(APIView):

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)