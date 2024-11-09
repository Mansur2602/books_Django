from django.shortcuts import render, redirect
from .models import Author, Book, Publishers, Publications, Sales

def book_list(request):
    sales = Sales.objects.all()
    context = {
        'sales': sales
    }
    return render(request, 'book_app/all_book.html', context)

def book(request, id):
    sales = Sales.objects.get(id = id)
    context = {
        'sales': sales
    }
    return render(request, 'book_app/book.html', context)


from django.shortcuts import render, redirect
from .models import Author, Publishers, Book, Publications, Sales

from django.shortcuts import render, redirect
from .models import Author, Publishers, Book, Publications, Sales

def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        genre = request.POST.get('genre')
        publication_year = request.POST.get('publication_year')
        publisher_id = request.POST.get('publisher')
        publication_date = request.POST.get('publication_date')
        circulation = request.POST.get('circulation')
        year = request.POST.get('year')
        price_per_book = request.POST.get('price_per_book')
        quantity_sold = request.POST.get('quantity_sold')

        # Создаем новую книгу
        author = Author.objects.get(id=author_id)
        publisher = Publishers.objects.get(id=publisher_id)

        new_book = Book(
            title=title,
            author=author,
            genre=genre,
            publication_year=publication_year
        )
        new_book.save()

        # Создаем публикацию
        new_publication = Publications(
            publisher=publisher,
            book=new_book,
            publication_date=publication_date,
            circulation=circulation
        )
        new_publication.save()

        # Вычисляем общую стоимость продаж
        total_sales_value = float(price_per_book) * int(quantity_sold)

        # Создаем запись о продаже
        new_sale = Sales(
            publication=new_publication,
            year=year,
            price_per_book=price_per_book,
            quantity_sold=quantity_sold,
            total_sales_value=total_sales_value  # Используем вычисленное значение
        )
        new_sale.save()

        return redirect('book_list')  # Перенаправляем на список книг после создания

    authors = Author.objects.all()
    publishers = Publishers.objects.all()

    context = {
        'authors': authors,
        'publishers': publishers
    }
    return render(request, 'book_app/create_book.html', context)

