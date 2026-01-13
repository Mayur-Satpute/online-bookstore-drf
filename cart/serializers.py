from rest_framework import serializers
from .models import Cart, CartItem
from books.models import Book
from books.serializers import BookSerializer


class AddToCartSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1)

    def create(self, validated_data):
        user = self.context["request"].user
        book_id = validated_data["book_id"]
        quantity = validated_data["quantity"]

        if quantity <= 0:
            raise serializers.ValidationError({
                "quantity": "Quantity must be greater than zero"
            })

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise serializers.ValidationError({
                "book_id": "Invalid book ID"
            })

        cart, _ = Cart.objects.get_or_create(user=user)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            book=book
        )

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()
        return cart_item


class CartItemSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "book", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "items", "total_price"]

    def get_total_price(self, obj):
        return sum(
            item.book.price * item.quantity
            for item in obj.items.all()
        )
