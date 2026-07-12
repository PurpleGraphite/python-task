from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import (
    ListCreateAPIView,
    DestroyAPIView,
)

from .models import BookSale, Book
from .serializers import BookSaleSerializer, BookSerializer
from .services import search_book_sales, get_sales_trends


class BookSalesDashboardView(TemplateView):
    template_name = "book_sales/book_sales.html"


class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    pagination_class = None

class BookSaleListCreateView(ListCreateAPIView):
    queryset = (
        BookSale.objects
        .select_related("book")
        .order_by("-sale_date")
    )

    serializer_class = BookSaleSerializer
    

class BookSaleSalesTrendView(APIView):

    def get(self, request):

        book_id = request.query_params.get("book_id")

        if not book_id:
            return Response(
                {"detail": "book_id query parameter is required."},
                status=400,
            )

        trends = get_sales_trends(book_id)

        data = []

        for row in trends:

            data.append(
                {
                    "month": row["month"],
                    "quantity": row["quantity"],
                }
            )

        return Response(data)



class BookSaleDestroyView(DestroyAPIView):
    queryset = BookSale.objects.all()

    serializer_class = BookSaleSerializer

class BookSaleSearchView(APIView):

    def get(self, request):

        query = request.query_params.get("q", "").strip()

        queryset = search_book_sales(query)

        serializer = BookSaleSerializer(
            queryset,
            many=True,
        )

        return Response(serializer.data)

