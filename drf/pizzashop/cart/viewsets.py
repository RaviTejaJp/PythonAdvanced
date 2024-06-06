from rest_framework import viewsets
from .models import Pizza, Topping, Size
from cart.models import Cart, CartItem
from menu.serializers import (
    PizzaSerializer,
    SizeSerializer,
    ToppingSerializer,
    PizzaHyperlinkedSerializer,
    ToppingHyperlinkedSerializer,
    SizeHyperlinkedSerializer,
)
from .serializers import (
    CartSerializer,
    CartItemSerializer,
    CartHyperlinkedSerializer,
    CartItemHyperlinkedSerializer,
    CartItemCreateUpdateSerializer,
)


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaHyperlinkedSerializer


class ToppingViewSet(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingHyperlinkedSerializer


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeHyperlinkedSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartHyperlinkedSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    # serializer_class = CartItemHyperlinkedSerializer

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return CartItemCreateUpdateSerializer
        return CartItemHyperlinkedSerializer
