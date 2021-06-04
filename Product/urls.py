"""DemoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import RegisterLoginView,index,AddProductView,DeleteProduct,ProductListView,signout

urlpatterns = [
    path("",RegisterLoginView.as_view(),name="registerlogin"),
    path("home",index,name="home"),
    path("addproduct",AddProductView.as_view(),name="addproduct"),
    path("delete/<int:pk>",DeleteProduct.as_view(),name="delete"),
    path("list",ProductListView.as_view(),name="list"),
    path("signout",signout,name="signout")
]
