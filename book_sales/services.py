from django.db.models import Q
from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from .models import BookSale

MONTHS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]



def search_book_sales(query):
    """
    Search book sales by book title or author.
    """

    queryset = (
        BookSale.objects
        .select_related("book")
        .order_by("-sale_date")
    )

    if not query:
        return queryset

    return queryset.filter(
        Q(book__title__icontains=query)
        |
        Q(book__author__icontains=query)
    )

def get_sales_trends(book_id):
    queryset = (
        BookSale.objects
        .filter(book_id=book_id)
        .annotate(month=ExtractMonth("sale_date"))
        .values("month")
        .annotate(quantity=Sum("quantity"))
        .order_by("month")
    )

    sales_by_month = {
        row["month"]: row["quantity"]
        for row in queryset
    }

    return [
        {
            "month": month_name,
            "quantity": sales_by_month.get(month_number, 0),
        }
        for month_number, month_name in enumerate(MONTHS, start=1)
    ]