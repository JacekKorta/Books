from django.core.exceptions import FieldError
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Response

from books.auxiliary.google_books_api import GoogleBooksApiHandler
from .models import Author, Book
from .serializers import BookSerializer


class BookDetail(APIView):

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=200)

    @staticmethod
    def get_object(pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404


class BooksList(APIView):

    def get(self, request, format=None):
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(self.get_queryset(), request)
        serializer = BookSerializer(result_page,
                                    many=True,
                                    context={'request': request}
                                    )
        return Response(serializer.data, status=200)

    def get_queryset(self):
        queryset = Book.objects.prefetch_related('authors').all().order_by('id')
        query_date = self.request.query_params.get('published_date')
        query_authors = self.clear_authors_query_params_data()
        sort = self.request.query_params.get('sort')
        if query_date is not None:
            queryset = queryset.filter(published_date__startswith=query_date)
        if query_authors:
            queryset = self.authors_filter(queryset, query_authors)
        if sort is not None:
            try:
                queryset = queryset.order_by(sort)
            except FieldError:
                return queryset
        return queryset

    def clear_authors_query_params_data(self):
        authors = [
            author.replace("'", "").replace('"', '')
            for author in self.request.query_params.getlist('author')
        ]
        return authors

    @staticmethod
    def authors_filter(queryset, query_authors):
        authors_ids = [
            author.id for author in Author.objects.filter(name__in=query_authors)
        ]
        queryset = queryset.filter(authors__in=authors_ids)
        return queryset


class DbImportView(APIView):

    def post(self, request, format=None):
        q = request.data.get("q")
        if q:
            gapi = GoogleBooksApiHandler()
            gapi.get_all_books(q)
            return Response(status=200)
        else:
            return Response(status=400)
