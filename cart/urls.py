from django.urls import path
from .views import (
    AddToCartAPIView,
    ViewCartAPIView,
    UpdateCartItemAPIView,
    DeleteCartItemAPIView
)

urlpatterns = [
    path("add/", AddToCartAPIView.as_view(), name="add-to-cart"),
    path("view/", ViewCartAPIView.as_view(), name="view-cart"),
    path("item/update/<int:pk>/", UpdateCartItemAPIView.as_view(), name="update-cart-item"),
    path("item/delete/<int:pk>/", DeleteCartItemAPIView.as_view(), name="delete-cart-item"),
]
