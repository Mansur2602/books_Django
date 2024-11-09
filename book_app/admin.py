from django.contrib import admin
from .models import Author, Publishers, Publications, Book, Sales


admin.site.register(Author)
admin.site.register(Publishers)
admin.site.register(Publications)
admin.site.register(Book)
admin.site.register(Sales)
