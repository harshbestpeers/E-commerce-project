from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View 
from .models import Customer
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def Main(request):
    return render(request, 'home.html') 

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email') 
        print(email)
        password = request.POST.get('password')
        customer = Customer.objects.get(email=email)
        # board = Board.objects.get(id=id)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.first_name
                request.session['id'] = customer.id
                
                return redirect('home')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        return render(request, 'login.html', {'error': error_message})

class Logout(View): 
    def get(self, request):
        request.session.clear() 
        return redirect('login') 


class Signup(View):
    def get (self, request):
        return render(request, "signup.html")

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname') 
        email = request.POST.get('email') 
        password = request.POST.get('password')

        error_message = None
        customer = Customer(first_name=first_name, 
                            last_name=last_name,  
                            email=email, 
                            password=password)

        error_message = self.validateCustomer(customer)

        print(error_message)
        if not error_message: 
            customer.password = make_password(customer.password) 
            customer.save() 
            return redirect('login')

        else: 
            data = { 
                'error': error_message
            } 
            return render(request, 'signup.html', data) 

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name): 
            error_message = "Please Enter your First Name !!"
        elif len(customer.first_name) < 3: 
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name: 
            error_message = 'Please Enter your Last Name'
        elif len(customer.last_name) < 3: 
            error_message = 'Last Name must be 3 char long or more'
        elif len(customer.password) < 5: 
            error_message = 'Password must be 5 char long'
        elif len(customer.email) < 5: 
            error_message = 'Email must be 5 char long'
        elif customer.isExists(): 
            error_message = 'Email Address Already Registered..'
        # saving 
  
        return error_message

