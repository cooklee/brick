import pytest

from shop.models import Author, Genre, Book


@pytest.fixture
def authors():
    authors = []
    for x in range(10):
        authors.append(Author(first_name=x, last_name=x))
    Author.objects.bulk_create(authors)
    return authors


@pytest.fixture
def genres():
    genres = []
    for x in range(10):
        genres.append(Genre(name=x))
    Genre.objects.bulk_create(genres)
    return genres


@pytest.fixture
def books(authors, genres):
    books = []
    for id, author in enumerate(authors):
        for x in range(4):
            books.append(
                Book(title=f'title {id} {x}', author=author, price=10 + x, description=f'description {id} {x}'))
    Book.objects.bulk_create(books)
    for id, book in enumerate(books):
        book.genres.set(genres[id % len(genres):(id + 2) % len(genres)])
    return books
