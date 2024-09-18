import pytest
from django.test import Client as Browser
from django.urls import reverse


@pytest.mark.django_db
def test_all_books_view():
    client = Browser()
    url = reverse('book_list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['books'].count() == 25


@pytest.mark.django_db
def test_search_by_author_first_name_henryk_books_view():
    client = Browser()
    titles = ['Quo Vadis', 'Krzyżacy', 'Ogniem i mieczem', 'Potop', 'Pan Wołodyjowski']
    url = reverse('book_list')
    search_params = {'author': 'Henryk'}
    response = client.get(url, search_params)
    assert response.status_code == 200
    assert response.context['books'].count() == 5
    for title in titles:
        assert title in [book.title for book in response.context['books']]

@pytest.mark.django_db
def test_search_by_author_first_name_wisława_books_view():
    client = Browser()
    titles = ['Lektury nadobowiązkowe','Chwila','Koniec i początek', 'Tutaj', 'Wielka liczba']
    url = reverse('book_list')
    search_params = {'author': 'Wisława'}
    response = client.get(url, search_params)
    assert response.status_code == 200
    assert response.context['books'].count() == 5
    for title in titles:
        assert title in [book.title for book in response.context['books']]


@pytest.mark.django_db
def test_search_by_author_last_name_Mickiewicz_books_view():
    client = Browser()
    titles = ['Pan Tadeusz', 'Dziady', 'Konrad Wallenrod', 'Sonety Krymskie', 'Grażyna']
    url = reverse('book_list')
    search_params = {'author': 'Mickiewicz'}
    response = client.get(url, search_params)
    assert response.status_code == 200
    assert response.context['books'].count() == 5
    for title in titles:
        assert title in [book.title for book in response.context['books']]

@pytest.mark.django_db
def test_search_by_author_last_name_Milosz_books_view():
    client = Browser()
    titles = ['Zniewolony umysł', 'Dolina Issy', 'Rodzinna Europa', 'Gucio zaczarowany', 'Piesek przydrożny']
    url = reverse('book_list')
    search_params = {'author': 'Miłosz'}
    response = client.get(url, search_params)
    assert response.status_code == 200
    assert response.context['books'].count() == 5
    for title in titles:
        assert title in [book.title for book in response.context['books']]

@pytest.mark.django_db
def test_search_by_author_first_last_name_stanislaw_lem_books_view():
    client = Browser()
    titles = ['Solaris', 'Cyberiada', 'Dzienniki gwiazdowe', 'Powrót z gwiazd', 'Bajki robotów']
    url = reverse('book_list')
    search_params = {'author': 'Stanisław Lem'}
    response = client.get(url, search_params)
    assert response.status_code == 200
    assert response.context['books'].count() == 5
    for title in titles:
        assert title in [book.title for book in response.context['books']]

@pytest.mark.django_db
def test_search_by_author_by_short_mi_books_view():
    client = Browser()
    titles =['Pan Tadeusz', 'Dziady', 'Konrad Wallenrod', 'Sonety Krymskie', 'Grażyna', 'Zniewolony umysł',
             'Dolina Issy', 'Rodzinna Europa', 'Gucio zaczarowany', 'Piesek przydrożny']
    url = reverse('book_list')
    search_params = {'author': 'mi'}
    response = client.get(url, search_params)
    assert response.status_code == 200
    assert response.context['books'].count() == 10
    for title in titles:
        assert title in [book.title for book in response.context['books']]



@pytest.mark.django_db
def test_detail_book_view():
    client = Browser()
    url = reverse('book_detail', args=[1])
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['book'].title == 'Quo Vadis'