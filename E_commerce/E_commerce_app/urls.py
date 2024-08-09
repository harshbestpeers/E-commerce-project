from django.urls import path
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
    path("", Main, name="home"),
    path("Signup/", Signup.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("categorys/<int:id>", Categorys.as_view(), name="category"),
    path("cart_detail/", cart_detail, name="cart_detail"),
    path("add_to_cart/<int:product_id>", AddToCart.as_view(), name="add_to_cart"),
    path("update_cart/<int:product_id>", UpdateCart.as_view(), name="update_cart"),
    # path("PlaceOrder/", PlaceOrder.as_view(), name="place_order"),
    path("product/", ProductAndImage.as_view(), name="product_and_image"),
    path("OrderHistory/", OrderHistory.as_view(), name="order_history"),
    path(
        "OrderHistoryItem/<int:order_id>",
        OrderHistoryItem.as_view(),
        name="order_history_item",
    ),
    path("search/", Search.as_view(), name="search"),
    path("wishlist/", DetailWishlist.as_view(), name="wishlist"),
    path(
        "add_to_wishlist/<int:product_id>",
        AddToWishList.as_view(),
        name="add_to_wishlist",
    ),
    path(
        "delete_to_wishlist/<int:product_id>",
        RemoveFromWishList.as_view(),
        name="delete_to_wishlist",
    ),
    path("dummy/", Dummy.as_view(), name="dummy"),
    path("account/", Account.as_view(), name="account"),
    # api
    path("Customer/", CustomerListCreate.as_view(), name="Customer-list-create"),
    path(
        "Customer/<int:pk>/",
        CustomerRetrieveUpdateDestroy.as_view(),
        name="Customer-detail",
    ),
    path("Order/", OrderListCreate.as_view(), name="Order-list-create"),
    path("Order/<int:pk>/", OrderRetrieveUpdateDestroy.as_view(), name="Order-detail"),
    # path('payment/', PaymentView.as_view(), name='payment'),
    path(
        "create-checkout-session/",
        CreateCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
    path("payment-success/", PaymentSuccess, name="payment-success"),
    path("payment-cancel/", PaymentCancel, name="payment-cancel"),


    path('create-payment-intent/', create_payment_intent, name='create_payment_intent'),
    path('payment-success/', PaymentSuccess, name='payment_success'),
]
