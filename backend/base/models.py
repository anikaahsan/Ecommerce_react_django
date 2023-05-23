from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    image=models.ImageField(upload_to='media',null=True,blank=True)
    brand=models.CharField(max_length=255,null=True,blank=True)
    category=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    rating=models.DecimalField(max_digits=7,decimal_places=1,null=True,blank=True)
    numReviews=models.IntegerField(null=True,blank=True)
    price=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    countInStock=models.IntegerField(null=True,blank=True,default=0)
    createdAt=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
         return self.name

class Review(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    rating=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    comment=models.TextField(null=True,blank=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
         return str(self.rating)


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    paymentMethod=models.CharField(max_length=255,null=True,blank=True)
    tax_price=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    shipping_price=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    total_price=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    is_paid=models.BooleanField(default=False)
    paidAt=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    is_delivered=models.BooleanField(default=False)
    deliveredAt=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
         return str(self.createdAt)


class OrderItem(models.Model):
        product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
        order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
        name=name=models.CharField(max_length=255,null=True,blank=True)
        quantity=models.IntegerField(null=True,blank=True,default=0)
        price=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
        image=models.ImageField(upload_to='images',null=True,blank=True)
        _id=models.AutoField(primary_key=True,editable=False)
        
        def __str__(self):
         return self.name

class ShippingAddress(models.Model):
     order=models.OneToOneField(Order,on_delete=models.CASCADE,null=True,blank=True)
     address=models.TextField(null=True,blank=True)
     city=models.CharField(max_length=255,null=True,blank=True)
     postalCode=models.CharField(max_length=255,null=True,blank=True)
     Country=models.CharField(max_length=255,null=True,blank=True)
     shippingPrice=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
     _id=models.AutoField(primary_key=True,editable=False)
    
     def __str__(self):
         return self.address