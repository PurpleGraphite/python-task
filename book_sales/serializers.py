from .models import Book, BookSale
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class BookSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSale
        fields = "__all__"