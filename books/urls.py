from django.urls import path
from .views import (
    BookListAPIView,
    BookDetailAPIView,
    BookCreateAPIView,
    BookUpdateAPIView,
    BookDeleteAPIView,
    CategoryCreateAPIView,
)

urlpatterns = [
    # Public
    path("", BookListAPIView.as_view()),
    path("<int:pk>/", BookDetailAPIView.as_view()),

    # Admin
    path("create/", BookCreateAPIView.as_view()),
    path("<int:pk>/update/", BookUpdateAPIView.as_view()),
    path("<int:pk>/delete/", BookDeleteAPIView.as_view()),
    path("categories/create/", CategoryCreateAPIView.as_view()),
]
