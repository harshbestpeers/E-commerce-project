from django.db import models
import datetime

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self): 
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def isExists(self): 
        if Customer.objects.filter(email=self.email): 
            return True
  
        return False


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=60) 
    price = models.IntegerField(default=0) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) 
    description = models.CharField(max_length=250, default='', blank=True, null=True) 
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products") 
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customers") 
    quantity = models.IntegerField(default=1) 
    price = models.IntegerField() 
    address = models.CharField(max_length=50, default='', blank=True) 
    phone = models.CharField(max_length=50, default='', blank=True) 
    date = models.DateField(default=datetime.datetime.today) 
    status = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.product} order by {self.customer}"

    



    