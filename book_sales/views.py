from django.views.generic import TemplateView
from rest_framework.generics import (
    ListCreateAPIView,
    DestroyAPIView,
)
class BookSalesDashboardView(TemplateView):
    template_name = "book_sales/book_sales.html"
class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    pagination_class = None
