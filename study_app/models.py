from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review_text = models.TextField()

    def __str__(self):
        return self.name


class Review1(models.Model):
    email = models.EmailField()



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.quantity * self.product.price





class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Заказ #{self.id} ny {self.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product2(models.Model):
    img = models.ImageField(upload_to = 'upload',blank=True,null=True)
    img2 = models.ImageField(upload_to = 'upload',blank=True,null=True)
    img3 = models.ImageField(upload_to = 'upload',blank=True,null=True)
    img4 = models.ImageField(upload_to = 'upload',blank=True,null=True)
    img5 = models.ImageField(upload_to = 'upload',blank=True,null=True)
    price = models.IntegerField(max_length=50)
    description = models.CharField(max_length=50)
    grade = models.IntegerField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)