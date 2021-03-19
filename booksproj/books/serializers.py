from rest_framework.views import APIView, Response
from rest_framework import serializers

from .models import Author, Book, Category


class AuthorSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('name',)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class BookSerializer(serializers.ModelSerializer):

    authors = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = [
            'title',
            'authors',
            'published_date',
            'categories',
            'average_rating',
            'ratings_count',
            'thumbnail'
        ]

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.authors = validated_data.get('authors', instance.authors)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.average_rating = validated_data.get('average_rating', instance.average_rating)
        instance.ratings_count = validated_data.get('ratings_count', instance.ratings_count)
        instance.thumbnail = validated_data.get('thumbnail', instance.thumbnail)
        instance.google_api_id = validated_data.get('google_api_id', instance.google_api_id)
        instance.save()
        return instance
