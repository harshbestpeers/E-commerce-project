from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import (
    Customer,
    Product,
    Category,
    Order,
    OrderItem,
    ShippingAddress,
    Image,
)
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def Main(request):

    categories = Category.objects.all()
    print(categories)
    context = {"categories": categories}
    return render(request, "home.html", context)


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get("email")
        print(email)
        password = request.POST.get("password")
        customer = Customer.objects.get(email=email)
        # board = Board.objects.get(id=id)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session["customer"] = customer.first_name
                request.session["id"] = customer.id

                return redirect("home")
            else:
                error_message = "Invalid !!"
        else:
            error_message = "Invalid !!"

        return render(request, "login.html", {"error": error_message})


class Logout(View):
    def get(self, request):
        request.session.clear()
        return redirect("login")


class Signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        error_message = None
        customer = Customer(
            first_name=first_name, last_name=last_name, email=email, password=password
        )

        error_message = self.validateCustomer(customer)

        print(error_message)
        if not error_message:
            customer.password = make_password(customer.password)
            customer.save()
            return redirect("login")

        else:
            data = {"error": error_message}
            return render(request, "signup.html", data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "Please Enter your First Name !!"
        elif len(customer.first_name) < 3:
            error_message = "First Name must be 3 char long or more"
        elif not customer.last_name:
            error_message = "Please Enter your Last Name"
        elif len(customer.last_name) < 3:
            error_message = "Last Name must be 3 char long or more"
        elif len(customer.password) < 5:
            error_message = "Password must be 5 char long"
        elif len(customer.email) < 5:
            error_message = "Email must be 5 char long"
        elif customer.isExists():
            error_message = "Email Address Already Registered.."
        # saving

        return error_message


class Categorys(View):
    def get(self, request, id):
        product = Product.objects.filter(category=id)
        context = {"product": product}
        return render(request, "category.html", context)


class Card(View):
    def get(self, request, id):
        return render(request, "category.html")


def cart_detail(request):
    cart = request.session.get("cart", {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []

    for product in products:

        cart_items.append(
            {
                "product": product,
                "quantity": cart[str(product.id)],
                "total_price": product.price * cart[str(product.id)],
            }
        )

    context = {
        "cart_items": cart_items,
        "total_price": sum(item["total_price"] for item in cart_items),
    }
    return render(request, "cart_detail.html", context)


class AddToCart(View):
    def Post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart = request.session.get("cart", {})
        cart[str(product.id)] = cart.get(str(product.id), 0) + 1
        request.session["cart"] = cart
        return redirect("cart_detail")

class UpdateCart(View):
    def post(self, request, product_id):
        cart = request.session.get('cart', {})
        if str(product_id) in cart:
            quantity = request.POST.get('quantity')
            if quantity:
                cart[str(product_id)] = int(quantity)
                request.session['cart'] = cart
        return redirect('cart_detail')
