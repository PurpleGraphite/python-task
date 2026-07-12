from django.urls import path

from .views import (
    BookListCreateView,
    BookSalesDashboardView,
    BookSaleListCreateView,
    BookSaleDestroyView,
    BookSaleSearchView,
    BookSaleSalesTrendView,
)

urlpatterns = [
    # Dashboard
    path(
        "",
        BookSalesDashboardView.as_view(),
        name="dashboard",
    ),

    # REST API
    path("api/books/", BookListCreateView.as_view(), name="book-list-create"),

    path(
        "api/booksales/",
        BookSaleListCreateView.as_view(),
        name="book-sale-list-create",
    ),

    path("api/booksales/sales-trends/", BookSaleSalesTrendView.as_view(), name="book-sale-trends"),

    path(
        "api/booksales/<int:pk>/",
        BookSaleDestroyView.as_view(),
        name="book-sale-delete",
    ),

     path(
        "api/booksales/search/",
        BookSaleSearchView.as_view(),
        name="book-sale-search",
    ),
]