from faker import Faker
from tqdm import tqdm

from authors.models import Author
from books.models import Book, Tag
from finance.models import Account, Transaction
from users.models import User

faker = Faker()


def create_authors(count):
    for _ in tqdm(range(count)):
        Author.objects.create(
            name=faker.name(), email=faker.email(), country=faker.country()
        )


def create_tags(count):
    for _ in tqdm(range(count)):
        Tag.objects.create(title=faker.word())


def create_books(count):

    for _ in tqdm(range(count)):
        tags = Tag.objects.all().order_by("?")[:2]
        author = Author.objects.all().order_by("?").first()
        book = Book.objects.create(
            title=faker.sentence(),
            description=faker.paragraph(),
            author=author,
            price=faker.random_int(min=1, max=1000),
            published_date=faker.date(),
        )
        book.tags.set(tags)
        book.save()


def destroy():
    Author.objects.all().delete()
    Book.objects.all().delete()
    Tag.objects.all().delete()


def destroy_books():
    Book.objects.all().delete()
