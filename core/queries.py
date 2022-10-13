from django.db.models import Avg, Count, Max, Min, Q, Sum

from authors.models import Author
from books.models import Book


def defer():
    """exclude the fields mentioned in defer()"""

    instance = Book.objects.last()
    print("Instance")
    print(vars(instance))

    defered_instance = Book.objects.defer("description").last()
    print("\nDefered instance")

    print(vars(defered_instance))
    print("\ndescription -->", defered_instance.description)


def only():
    """get the fields mentioned in only()"""

    only_instance = Book.objects.only("title").last()

    print("\nOnly instance")
    print(vars(only_instance))

    print("\nauthor -->", only_instance.author)


def intersection():
    book_price_less_than_500 = Book.objects.filter(price__lt=500)
    book_price_greater_than_300 = Book.objects.filter(price__gt=300)

    # 300 > price < 500

    print("< 500 count -->", book_price_less_than_500.count())
    print("> 300 count -->", book_price_greater_than_300.count())

    books_intersection = book_price_less_than_500.intersection(
        book_price_greater_than_300
    )

    books_intersection_method2 = book_price_less_than_500 & book_price_greater_than_300
    print("Intersection count -->", books_intersection.count())
    print("Intersection count -->", books_intersection_method2.count())


def difference():
    books_price_less_than_500 = Book.objects.filter(price__lt=500)
    books_price_less_than_300 = Book.objects.filter(price__lt=300)

    print("< 500 count -->", books_price_less_than_500.count())
    print("< 300 count -->", books_price_less_than_300.count())

    difference = books_price_less_than_500.difference(books_price_less_than_300)
    print("Difference count -->", difference.count())


def annotate():
    author = Author.objects.annotate(Avg("book__price")).last()
    print("Author -->", vars(author))

    # total = 0
    # books_of_author = Book.objects.filter(author=author)
    # total_books = books_of_author.count()
    # for i in books_of_author:
    #     total += i.price
    #     print("price -->", i.price)

    # print("average ->", total / total_books)


def alias():
    """
    annotate 'authors_count' added to instance
    alias 'authors_count' is not added to instance,instead cached. used in filtering/sorting
    """

    books_annotate = Book.objects.annotate(authors_count=Count("author"))
    print("annotate -->", vars(books_annotate[0]))

    books_alias = Book.objects.alias(avg_price=Avg("price"))

    # alias "avg_price" not added, avg_price : filtering,sorting in  the cache
    print("\n\nalias -->", vars(books_alias[0]))

    authors_alias = Author.objects.alias(books=Count("book")).filter(books__gt=2)
    print("authors -->", vars(authors_alias[0]))

    author_annotate = Author.objects.annotate(books=Count("book")).filter(books__gt=2)
    print("authors -->", vars(author_annotate[0]))


def dates():
    from datetime import date

    date = date(2020, 1, 1)
    books = Book.objects.filter(published_date__date=date)
    print("books", books)


def q_object():
    book_title_starts_with_a_or_e = Book.objects.filter(
        Q(title__startswith="a") | Q(title__startswith="e")
    )


# select_related : onetoone, foreignkey
# prefetch_related : manytomany
