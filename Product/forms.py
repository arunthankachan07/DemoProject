from .models import CustomUser,Products
from django.forms import ModelForm
from django import forms


class UserRegistrationForm(ModelForm):
        class Meta:
            model=CustomUser
            # fields ="__all__"
            fields = ["username","first_name","last_name","email","password","phone","age" ]
            widgets = {
                'username': forms.TextInput(attrs={'class':'input','id':'user','placeholder':'Enter username'}),
                'first_name': forms.TextInput(attrs={'class': 'input', 'id': 'user', 'placeholder': 'Enter First Name'}),
                'last_name': forms.TextInput(attrs={'class': 'input', 'id': 'user', 'placeholder': 'Enter Last Name'}),
                'email': forms.TextInput(attrs={'class': 'input', 'id': 'user', 'placeholder': 'Enter Email Address'}),
                'password' : forms.PasswordInput(attrs={'class': 'input', 'id': 'pass', 'placeholder': 'Enter Password'}),
                'phone': forms.TextInput(attrs={'class': 'input', 'id': 'user', 'placeholder': 'Enter Your Contact No.'}),
                'age': forms.TextInput(attrs={'class': 'input', 'id': 'user', 'placeholder': 'Enter Your Age'}),


        }


class ProductForm(forms.Form):
    product_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Product Name'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Product Name'}))
    image=forms.ImageField(widget=forms.FileInput(attrs={'class': 'text_inp', 'placeholder': 'Image'}))



class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'input','id':'user','placeholder':'Enter your username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input','id':'pass','placeholder':'Enter your password'}))
