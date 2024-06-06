from rest_framework import serializers
from .models import Cart, CartItem
from menu.serializers import ToppingSerializer


class SampleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()


class CartItemSerializer(serializers.ModelSerializer):
    toppings = ToppingSerializer(many=True, read_only=True)

    class Meta:
        model = CartItem
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = "__all__"


class CartItemHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    pizza = serializers.HyperlinkedRelatedField(
        view_name="pizza-detail", read_only=True
    )
    size = serializers.HyperlinkedRelatedField(view_name="size-detail", read_only=True)
    toppings = serializers.HyperlinkedRelatedField(
        view_name="topping-detail", many=True, read_only=True
    )

    class Meta:
        model = CartItem
        fields = ["url", "pizza", "size", "toppings", "quantity", "cart"]


class CartHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    items = CartItemHyperlinkedSerializer(many=True, read_only=True)
    user = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)

    class Meta:
        model = Cart
        fields = ["url", "user", "created_at", "updated_at", "items"]


class CartItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"

    def create(self, validated_data):
        toppings_data = validated_data.pop("toppings")
        cart_item = CartItem.objects.create(**validated_data)
        for topping_data in toppings_data:
            cart_item.toppings.add(topping_data)
        return cart_item

    def update(self, instance, validated_data):
        toppings_data = validated_data.pop("toppings")
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.save()
        instance.toppings.clear()
        for topping_data in toppings_data:
            instance.toppings.add(topping_data)
        return instance


class ReadOnlyCartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Cart
        fields = "__all__"
        read_only_fields = fields
