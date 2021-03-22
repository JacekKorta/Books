import logging
from typing import List

import requests

from books.models import Author, Book, Category

logging.basicConfig(format='%(asctime)s | %(levelname)s: %(message)s', level=logging.WARNING)


class GoogleBooksApiHandler:

    @staticmethod
    def get_json_books_data(q: str, pointer) -> dict:
        try:
            data = requests.get(
                f"https://www.googleapis.com/books/v1/volumes?q={q}"
                f"&maxResult=10&startIndex={pointer}")
            return data.json()
        except ConnectionError:
            logging.error("Connection error has occurred. "
                          "Please check your internet connection and try again ")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

    @staticmethod
    def get_authors(volume_info: dict) -> List:
        authors = volume_info.get('authors')
        authors_objects = []
        if authors:
            for author in authors:
                try:
                    authors_objects.append(Author.objects.get(name=author))
                except Author.DoesNotExist:
                    new_author = Author.objects.create(name=author)
                    authors_objects.append(new_author)
        return authors_objects

    @staticmethod
    def get_categories(volume_info: dict) -> List:
        categories = volume_info.get('categories')
        categories_objects = []
        if categories:
            for category in categories:
                try:
                    categories_objects.append(Category.objects.get(name=category))
                except Category.DoesNotExist:
                    new_category = Category.objects.create(name=category)
                    categories_objects.append(new_category)
        return categories_objects

    def add_books(self, json_data: dict) -> None:
        items = json_data.get('items')
        for item in items:
            google_api_id = item.get('id')
            volume_info = item.get('volumeInfo')
            categories = self.get_categories(volume_info)
            authors = self.get_authors(volume_info)
            book, created = Book.objects.get_or_create(
                google_api_id=google_api_id,
                defaults={
                    "title": volume_info.get("title"),
                    "published_date": volume_info.get("publishedDate"),
                    "average_rating": volume_info.get("averageRating"),
                    "ratings_count": volume_info.get("ratingsCount"),
                    "thumbnail": volume_info.get("imageLinks", {}).get("thumbnail")

                }
            )
            if created:
                if authors:
                    [book.authors.add(author) for author in authors]
                if categories:
                    [book.categories.add(category) for category in categories]
            else:
                if authors:
                    book.authors.clear()
                    [book.authors.add(author) for author in authors]
                if categories:
                    book.categories.clear()
                    [book.categories.add(category) for category in categories]

    def get_all_books(self, q: str) -> None:
        pointer = 0
        next_page = True

        while next_page:
            json_data = self.get_json_books_data(q, pointer)
            if json_data.get("items"):
                pointer += 10
                self.add_books(json_data)
            else:
                next_page = False
