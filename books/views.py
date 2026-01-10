from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Book, Category
from .serializers import BookSerializer, BookCreateUpdateSerializer, CategorySerializer

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Book.objects.all()
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category__name__iexact=category)
        return queryset


class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateUpdateSerializer
    permission_classes = [IsAdminUser]


class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateUpdateSerializer
    permission_classes = [IsAdminUser]


class BookDeleteAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsAdminUser]



class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

