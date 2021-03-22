from unittest.mock import patch

from django.test import TestCase

from books.models import Author, Book, Category
from books.auxiliary.google_books_api import GoogleBooksApiHandler
from .google_api_mock import MockResponse


class TestApiGetListData(TestCase):
    gapi_auxiliary = GoogleBooksApiHandler()

    @patch("requests.post", return_value=MockResponse())
    def test_post_method_without_body_returns_400(self, mocked):
        response = self.client.post("/db/")
        self.assertEqual(response.status_code, 400)

    @patch("requests.post", return_value=MockResponse())
    def test_post_method_incorrect_body_returns_400(self, mocked):
        response = self.client.post("/db/", {"i": "war"})
        self.assertEqual(response.status_code, 400)

    @patch("requests.get", return_value=MockResponse())
    def test_get_json_books_data_returns_json_data(self, mocked):
        result = self.gapi_auxiliary.get_json_books_data("war", 0)
        self.assertEqual(isinstance(result, dict), True)

    @patch("requests.get", return_value=MockResponse())
    def test_get_json_books_data_returns_ten_results(self, mocked):
        result = self.gapi_auxiliary.get_json_books_data("war", 0)
        self.assertEqual(len(result.get("items")), 10)

    def test_get_authors_returns_list(self):
        mock = MockResponse()
        volume_info = mock.json().get("items")[0].get("volumeInfo", {})
        result = self.gapi_auxiliary.get_authors(volume_info)
        self.assertEqual(isinstance(result, list), True)

    def test_get_authors_returns_authors_instance_list(self):
        mock = MockResponse()
        volume_info = mock.json().get("items")[0].get("volumeInfo", {})
        result = self.gapi_auxiliary.get_authors(volume_info)
        self.assertEqual(all(isinstance(a, Author) for a in result), True)

    def test_get_categories_returns_list(self):
        mock = MockResponse()
        volume_info = mock.json().get("items")[0].get("volumeInfo", {})
        result = self.gapi_auxiliary.get_categories(volume_info)
        self.assertEqual(isinstance(result, list), True)

    def test_get_categories_returns_categories_instances_list(self):
        mock = MockResponse()
        volume_info = mock.json().get("items")[0].get("volumeInfo", {})
        result = self.gapi_auxiliary.get_categories(volume_info)
        self.assertEqual(all(isinstance(a, Category) for a in result), True)

    def test_add_books_creates_ten_books_in_db(self):
        mock = MockResponse()
        self.gapi_auxiliary.add_books(mock.json())
        books = Book.objects.all()
        self.assertEqual(len(books), 10)

    def test_add_books_created_books_with_title(self):
        mock = MockResponse()
        self.gapi_auxiliary.add_books(mock.json())
        books = Book.objects.all()
        self.assertEqual(all(b.title for b in books), True)

    def test_add_books_created_books_with_google_api_id(self):
        mock = MockResponse()
        self.gapi_auxiliary.add_books(mock.json())
        books = Book.objects.all()
        self.assertEqual(all(b.google_api_id for b in books), True)

    def test_add_books_created_books_with_published_date(self):
        mock = MockResponse()
        self.gapi_auxiliary.add_books(mock.json())
        books = Book.objects.all()
        self.assertEqual(all(b.published_date for b in books), True)

    def test_add_books_created_books_with_thumbnail(self):
        mock = MockResponse()
        self.gapi_auxiliary.add_books(mock.json())
        books = Book.objects.all()
        self.assertEqual(all(b.thumbnail for b in books), True)

    def test_add_books_created_books_with_authors(self):
        mock = MockResponse()
        self.gapi_auxiliary.add_books(mock.json())
        books = Book.objects.prefetch_related('authors').all()[:6]
        self.assertEqual(all(b.authors.all() for b in books), True)

    def test_add_books_created_books_with_categories(self):
        mock = MockResponse()
        self.gapi_auxiliary.add_books(mock.json())
        books = Book.objects.prefetch_related('categories').all()[:6]
        self.assertEqual(all(b.categories.all() for b in books), True)