from django import forms
from django.db import models

class Users(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.TextField()
    address = models.TextField()
    admin = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Products(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    price = models.IntegerField()
    extras = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    valid = models.BooleanField()
    quantity = models.IntegerField(max_length=11)
    total_price = models.IntegerField(max_length=11)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id}"