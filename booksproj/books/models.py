from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    authors = models.ManyToManyField(Author, blank=True)
    published_date = models.PositiveSmallIntegerField(null=True, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    average_rating = models.FloatField(null=True, blank=True)
    ratings_count = models.PositiveIntegerField(null=True, blank=True)
    thumbnail = models.URLField(null=True, blank=True)
    google_api_id = models.CharField(max_length=12, unique=True)




