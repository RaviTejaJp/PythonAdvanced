from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    PizzaViewSet,
    ToppingViewSet,
    SizeViewSet,
    CartViewSet,
    CartItemViewSet,
)

router = DefaultRouter()
router.register(r"pizzas", PizzaViewSet)
router.register(r"toppings", ToppingViewSet)
router.register(r"sizes", SizeViewSet)
router.register(r"carts", CartViewSet)
router.register(r"cartitems", CartItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
