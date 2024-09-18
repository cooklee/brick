from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse

from shop.models import Book, Cart, BooksInCart


# Create your views here.
def index(request):
    request.session['previous'] = request.path
    books = Book.objects.order_by('?')[:10]
    return render(request, 'base.html', {'books': books})


def cart_view(request):
    return render(request, 'shop/cart.html')

def create_author_query(author):
    if author == '':
        return None
    if ' ' in author:
        author = author.split(' ')
        if len(author) != 2:
            raise ValueError('Author name must consist of first and last name')
        first_name, last_name = author
        q1 = Q(author__first_name__icontains=first_name)
        q2 = Q(author__last_name__icontains=last_name)
        return q1 & q2
    q1 = Q(author__first_name__icontains=author)
    q2 = Q(author__last_name__icontains=author)
    return q1 | q2

def book_list(request):
    request.session['previous'] = request.path
    books = Book.objects.all()
    title = request.GET.get('title', '')
    author = request.GET.get('author', '')
    try:
        query = create_author_query(author)
    except ValueError as e:
        messages.error(request, 'autor posaida jedynie nazwisko i imie')
        query = None
    books = books.filter(title__icontains=title)
    if query:
        books = books.filter(query)
    return render(request, 'shop/book_list.html', {'books': books})

def book_detail(request, book_id):
    request.session['previous'] = request.path
    book = Book.objects.get(pk=book_id)
    return render(request, 'shop/book_detail.html', {'book': book})

@login_required
def add_to_cart(request, book_id):
    path = request.session.get('previous', reverse('book_list'))
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    book = Book.objects.get(pk=book_id)
    bic, created = BooksInCart.objects.get_or_create(cart=cart, book=book)
    if not created:
        bic.quantity += 1
        bic.save()
    return redirect(path)