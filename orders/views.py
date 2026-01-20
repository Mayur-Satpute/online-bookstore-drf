from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart.models import Cart


class CreateOrderAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Response(
                {"error": "Cart is empty"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if cart.items.count() == 0:
            return Response(
                {"error": "Cart is empty"},
                status=status.HTTP_400_BAD_REQUEST
            )

        order = Order.objects.create(user=user)

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                book=item.book,
                quantity=item.quantity,
                price=item.book.price
            )

        cart.items.all().delete()  # clear cart after order

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserOrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class AdminOrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
    queryset = Order.objects.all()


class UpdateOrderStatusAPIView(UpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
    queryset = Order.objects.all()


class DeleteOrderAPIView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Order.objects.all()
