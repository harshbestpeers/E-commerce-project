# models.py

from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=200)
    phone_number = models.IntegerField(default="0000000000")
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True)
    stock = models.PositiveIntegerField(null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category"
    )

    def __str__(self):
        return self.name

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    # order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.address


class Payment(models.Model):
    # order = models.OneToOneField(Order, related_name='payment', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f'Payment {self.id}'

class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    shipping_address = models.ForeignKey(ShippingAddress, related_name='shipping_address', on_delete=models.SET_NULL, null=True, blank=True, default="1")
    payment = models.ForeignKey(Payment, related_name="payment",on_delete=models.SET_NULL, null=True, blank=True, default="1")
    date_ordered = models.DateTimeField(auto_now_add=True)
    # complete = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default="pending")

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.order.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.order.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="product"
    )
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, related_name="order"
    )
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total





class Image(models.Model):
    image = models.ImageField(upload_to="static/image")
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="product_image"
    )

    def __str__(self):
        return str(self.id)
