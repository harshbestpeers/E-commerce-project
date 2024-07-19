from django.urls import path
from .views import *

urlpatterns = [
    path("", Main, name="home"),
    path("Signup/", Signup.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("categorys/<int:id>", Categorys.as_view(), name="category"),
    path("cart_detail/", cart_detail, name="cart_detail"),
    path("add_to_cart/<int:product_id>", AddToCart.as_view(), name="add_to_cart"),
    path("update_cart/<int:product_id>", UpdateCart.as_view(), name="update_cart"),
    path(
        "remove_from_cart/<int:product_id>",
        RemoveFromCart.as_view(),
        name="remove_from_cart",
    ),
    path("shipping/", Shipping.as_view(), name="shipping"),
    path("shipping/", Shipping.as_view(), name="shipping"),
    path("product/", ProductAndImage.as_view(), name="product_and_image"),
]
