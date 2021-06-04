from django.contrib import admin

# Register your models here.
from Product.models import CustomUser, Products

admin.site.register(Products)