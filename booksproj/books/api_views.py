from rest_framework.views import APIView, Response

from .models import Book
from .serializers import BookSerializer


class BooksView(APIView):

    def get(self, request, format=None):
        books = Book.objects.prefetch_related('authors').all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
