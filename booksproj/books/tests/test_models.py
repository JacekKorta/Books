from django.test import TestCase
from faker import Faker

from books.models import Author, Book, Category


class BasicSetupTestCase(TestCase):

    def setUp(self) -> None:
        fake = Faker(locale='en_US')

        category_1 = Category.objects.create(name='Computer science')
        category_2 = Category.objects.create(name='History')
        author_1 = Author.objects.create(name=fake.name())
        author_2 = Author.objects.create(name=fake.name())
        book_1 = Book.objects.create(
            title='The grand book about IT',
            published_date="1924",
            average_rating=4.5,
            ratings_count=1,
            thumbnail='https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg',
            google_api_id='XCVFGHERTWSA'
        )
        book_1.categories.add(category_1, category_2)
        book_1.authors.add(author_1, author_2)


class TestBasicAuthorTest(BasicSetupTestCase):

    def test_author_represented_by_name_field(self):
        author = Author.objects.get(pk=1)
        self.assertEqual(author.__str__(), author.name)


class TestBasicBookTest(BasicSetupTestCase):

    def test_book_represented_by_name_field(self):
        book = Book.objects.get(pk=1)
        self.assertEqual(
            book.__str__(),
            f"{book.title} wrote by {[author for author in book.authors.all()]}"
        )


class TestBasicCategoryTest(BasicSetupTestCase):

    def test_category_represented_by_name_field(self):
        category = Category.objects.get(pk=1)
        self.assertEqual(category.__str__(), category.name)
