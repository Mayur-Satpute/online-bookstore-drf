from django.urls import path
from .views import (
    CreateOrderAPIView,
    UserOrderListAPIView,
    AdminOrderListAPIView,
    UpdateOrderStatusAPIView,
    DeleteOrderAPIView
)

urlpatterns = [
    path("create/", CreateOrderAPIView.as_view()),
    path("my-orders/", UserOrderListAPIView.as_view()),
    path("admin/all/", AdminOrderListAPIView.as_view()),
    path("admin/update/<int:pk>/", UpdateOrderStatusAPIView.as_view()),
    path("admin/delete/<int:pk>/", DeleteOrderAPIView.as_view()),
]
