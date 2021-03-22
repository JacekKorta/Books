from django.test import TestCase
from django.urls import reverse
from faker import Faker

from books.models import Author, Book, Category


class BasicSetup(TestCase):
    def setUp(self) -> None:
        fake = Faker(locale='en_US')

        category_1 = Category.objects.create(name='Computer science')
        category_2 = Category.objects.create(name='History')
        author_1 = Author.objects.create(name=fake.name())
        author_2 = Author.objects.create(name=fake.name())
        author_3 = Author.objects.create(name=fake.name())
        book_1 = Book.objects.create(
            title='The grand book about IT',
            published_date="1924",
            average_rating=4.5,
            ratings_count=2,
            thumbnail='https://wikipedia.com',
            google_api_id='XCVFGHERTWSA'
        )
        book_1.categories.add(category_1, category_2)
        book_1.authors.add(author_1, author_2)

        book_2 = Book.objects.create(
            title='The completely different book about IT',
            published_date="2004",
            average_rating=3.5,
            ratings_count=9,
            thumbnail='https://google.com',
            google_api_id='XCVxdrERTWSA'
        )
        book_2.categories.add(category_1)
        book_2.authors.add(author_3)


class TestApiGetSingle(BasicSetup):

    def test_get_method_works(self):
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_get_pk_out_of_range_return_404(self):
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 99}))
        self.assertEqual(response.status_code, 404)

    def test_book_details_contains_title_field(self):
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertContains(response, 'title')

    def test_book_details_contains_title_data(self):
        book = Book.objects.get(pk=1)
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertContains(response, book.title)

    def test_book_details_contains_authors_field(self):
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertContains(response, 'authors')

    def test_book_details_contains_authors_data(self):
        book = Book.objects.prefetch_related('authors').get(pk=1)
        authors = book.authors.all()
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        for author in authors:
            self.assertContains(response, author.name)

    def test_book_details_contains_published_date_field(self):
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertContains(response, 'published_date')

    def test_book_details_contains_published_date_data(self):
        book = Book.objects.get(pk=1)
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertContains(response, book.published_date)

    def test_book_details_contains_categories_field(self):
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertContains(response, 'categories')

    def test_book_details_contains_categories_data(self):
        book = Book.objects.prefetch_related('categories').get(pk=1)
        categories = book.categories.all()
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        for category in categories:
            self.assertContains(response, category.name)

    def test_book_details_contains_average_rating_field(self):
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertContains(response, 'average_rating')

    def test_book_details_contains_average_rating_data(self):
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertContains(response, '"average_rating":4.5')

    def test_book_details_contains_ratings_count_field(self):
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertContains(response, 'ratings_count')

    def test_book_details_contains_ratings_count_data(self):
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertContains(response, '"ratings_count":2')

    def test_book_details_contains_thumbnail_field(self):
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertContains(response, 'thumbnail')

    def test_book_details_contains_thumbnail_data(self):
        book = Book.objects.get(pk=1)
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertContains(response, book.thumbnail)

    def test_book_details_not_contains_google_api_id_field(self):
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertNotContains(response, 'google_api_id')

    def test_book_details_not_contains_google_api_id_data(self):
        book = Book.objects.get(pk=1)
        response = self.client.get(reverse('books:book-detail', kwargs={'pk': 1}))
        self.assertNotContains(response, book.google_api_id)
