from datetime import date

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    author = models.CharField(max_length=50, db_index=True)

class BookSale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    sale_date = models.DateField(default=date.today)
    quantity = models.PositiveIntegerField()
