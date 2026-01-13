from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

from .models import Cart, CartItem
from .serializers import (
    AddToCartSerializer,
    CartItemSerializer,
    CartSerializer
)

class AddToCartAPIView(CreateAPIView):
    serializer_class = AddToCartSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart_item = serializer.save()

        response_serializer = CartItemSerializer(cart_item)
        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )


class ViewCartAPIView(RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart


class UpdateCartItemAPIView(UpdateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()

    def perform_update(self, serializer):
        cart_item = self.get_object()
        if cart_item.cart.user != self.request.user:
            raise PermissionDenied("You cannot update this cart item")
        serializer.save()


class DeleteCartItemAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()

    def perform_destroy(self, instance):
        if instance.cart.user != self.request.user:
            raise PermissionDenied("You cannot delete this cart item")
        instance.delete()
