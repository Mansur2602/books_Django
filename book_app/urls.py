from django.contrib import admin
from django.urls import path
from book_app.views import book_list, book,  create_book

urlpatterns = [
    path('', book_list, name = 'book_list'),
    path('book/<id>', book, name='book'),
    path('create_book', create_book, name = 'create_book')
]