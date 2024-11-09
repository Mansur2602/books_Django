from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.DateField(null=False)

    def __str__(self):
        return self.name


class Publishers(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Publications(models.Model):
    publisher = models.ForeignKey(Publishers, related_name='publications', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='publications', on_delete=models.CASCADE)
    publication_date = models.DateField()
    circulation = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.book.title} - {self.publisher.name}"


class Sales(models.Model):
    publication = models.ForeignKey(Publications, related_name='sales', on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    price_per_book = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_sold = models.PositiveIntegerField()
    total_sales_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.publication.book.title} {self.year}"

    

 
