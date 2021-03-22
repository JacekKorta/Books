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
        ordering = ['id']
        fields = [
            'title',
            'authors',
            'published_date',
            'categories',
            'average_rating',
            'ratings_count',
            'thumbnail'
        ]
