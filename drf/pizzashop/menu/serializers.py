from rest_framework import serializers
from .models import Pizza, Topping, Size


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = "__all__"


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = "__all__"


class PizzaHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = ["url", "name", "description", "base_price"]


class ToppingHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topping
        fields = ["url", "name", "price"]


class SizeHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = ["url", "name", "price_multiplier"]
