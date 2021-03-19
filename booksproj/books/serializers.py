from rest_framework.views import APIView, Response
from rest_framework import serializers

from .models import Author, Book, Category


class AuthorSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):

    authors = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = (
            'title',
            'authors',
            'published_date',
            'categories',
            'average_rating',
            'ratings_count',
            'thumbnail'
        )
