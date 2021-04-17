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


class TestApiGetListData(BasicSetup):

    def test_get_method_works(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertEqual(response.status_code, 200)

    def test_get_method_returns_books_list(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertEqual(len(response.data.get('results')), 2)

    def test_books_list_contains_title_field(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertContains(response, 'title')

    def test_books_list_contains_title_data(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertContains(response, 'The grand book about IT')
        self.assertContains(response, 'The completely different book about IT')

    def test_books_list_contains_authors_field(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertContains(response, 'authors')

    def test_books_list_contains_authors_data(self):
        authors = Author.objects.all()
        response = self.client.get(reverse('books:books-list'))
        for author in authors:
            self.assertContains(response, author.name)

    def test_books_list_contains_published_date_field(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertContains(response, 'published_date')

    def test_books_list_contains_published_date_data(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertContains(response, '2004')
        self.assertContains(response, '1924')

    def test_books_list_contains_categories_field(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertContains(response, 'categories')

    def test_books_list_contains_categories_data(self):
        categories = Category.objects.all()
        response = self.client.get(reverse('books:books-list'))
        for category in categories:
            self.assertContains(response, category.name)

    def test_books_list_contains_average_rating_field(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertContains(response, 'average_rating')

    def test_books_list_contains_average_rating_data(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertContains(response, '"average_rating":4.5')
        self.assertContains(response, '"average_rating":3.5')

    def test_books_list_contains_ratings_count_field(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertContains(response, 'ratings_count')

    def test_books_list_contains_ratings_count_data(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertContains(response, '"ratings_count":2')
        self.assertContains(response, '"ratings_count":9')

    def test_books_list_contains_thumbnail_field(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertContains(response, 'thumbnail')

    def test_books_list_contains_thumbnail_data(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertContains(response, 'https://wikipedia.com')
        self.assertContains(response, 'https://google.com')

    def test_books_list_not_contains_google_api_id_field(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertNotContains(response, 'google_api_id')

    def test_books_list_not_contains_google_api_id_data(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertNotContains(response, 'XCVFGHERTWSA')
        self.assertNotContains(response, 'XCVxdrERTWSA')


class TestApiGetListFiltered(BasicSetup):

    def test_get_year_filter_returns_book_published_in_given_year(self):
        response = self.client.get('/books/?published_date=1924')
        self.assertEqual(len(response.data.get('results')), 1)

    def test_get_year_empty_filter_returns_full_list(self):
        response = self.client.get('/books/?published_date=')
        self.assertEqual(len(response.data.get('results')), 2)

    def test_get_year_incorrect_filter_returns_empty_list(self):
        response = self.client.get('/books/?published_date="King Arthur')
        self.assertEqual(len(response.data.get('results')), 0)

    def test_get_author_filter_returns_book_given_author(self):
        author = Author.objects.get(pk=1)
        response = self.client.get(f'/books/?author={author.name}')
        self.assertEqual(len(response.data.get('results')), 1)

    def test_get_authors_filter_returns_books_given_authors(self):
        author1 = Author.objects.get(pk=1)
        author3 = Author.objects.get(pk=3)
        response = self.client.get(f'/books/?author={author1.name}&author={author3.name}')
        self.assertEqual(len(response.data.get('results')), 2)

    def test_get_author_empty_filter_returns_empty_list(self):
        response = self.client.get('/books/?author=')
        self.assertEqual(len(response.data.get('results')), 0)

    def test_get_date_sort_minus_returns_newest_first(self):
        newest_book = Book.objects.all().order_by('-published_date')[0]
        response = self.client.get('/books/?sort=-published_date')
        response_book_published_date = response.data.get('results')[0].get('published_date')
        self.assertEqual(response_book_published_date, newest_book.published_date)

    def test_get_date_sort_returns_oldest_first(self):
        oldest_book = Book.objects.all().order_by('published_date')[0]
        response = self.client.get('/books/?sort=-published_date')
        response_book_published_date = response.data.get('results')[0].get('published_date')
        self.assertNotEqual(response_book_published_date, oldest_book.published_date)

    def test_get_date_sort_empty_returns_oldest_first(self):
        oldest_book = Book.objects.all().order_by('published_date')[0]
        response = self.client.get('/books/?sort=')
        response_book_published_date = response.data.get('results')[0].get('published_date')
        self.assertEqual(response_book_published_date, oldest_book.published_date)
