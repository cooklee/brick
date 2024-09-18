# Generated by Django 5.1.1 on 2024-09-08 21:53

from django.db import migrations
from shop.data_file import authors


def add_default_genres(apps, schema_editor):
    Genre = apps.get_model('shop', 'Genre')
    default_genres = [
        "Fantasy",
        "Science Fiction",
        "Romance",
        "Mystery",
        "Horror",
        "Thriller",
        "Non-fiction",
        "Biography"
    ]
    lst = []
    for genre in default_genres:
        Genre.objects.create(name=genre)
        lst.append(Genre(name=genre))
    Genre.objects.bulk_create(lst)


def add_authors_with_books(apps, schema_editor):
    Author = apps.get_model('shop', 'Author')
    Book = apps.get_model('shop', 'Book')
    Genre = apps.get_model('shop', 'Genre')
    for author in authors:
        author_instance = Author.objects.create(first_name=author['first_name'], last_name=author['last_name'])
        for book in author['books']:
            genres = book['genres']
            obj_genres = []
            for genre_name in genres:
                genre_instance, created = Genre.objects.get_or_create(name=genre_name)
                obj_genres.append(genre_instance)
            price = book['price']
            book_instance = Book.objects.create(title=book['title'], author=author_instance, description=book['description'], price=price)
            book_instance.genres.set(obj_genres)


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        # migrations.RunPython(add_default_genres),
        migrations.RunPython(add_authors_with_books),
    ]
