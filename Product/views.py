from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth import login as djangologin, logout
from django.shortcuts import render,redirect
from .forms import UserRegistrationForm, LoginForm, ProductForm
from .models import CustomUser, Products
from .decorators import login_required
from django.contrib import messages


# Create your views here.
#View for registration and login
class RegisterLoginView(TemplateView):
    model=CustomUser
    template_name = "Product/register_login.html"
    sign_in_form=LoginForm
    sign_up_form=UserRegistrationForm
    context={}
    def get(self, request, *args, **kwargs):
        self.context["form"]={'sign_in_form':self.sign_in_form,'sign_up_form':self.sign_up_form}
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        #----------login codes-------------
        if "signin" in request.POST:

            form = self.sign_in_form(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                # user=authenticate(request,username=username,password=password)
                try:
                    user = self.model.objects.get(username=username)
                    if user.username == username:
                        if user.password == password:
                            djangologin(request, user)

                            return redirect("home")
                        else:
                            messages.error(request, 'Password is incorrect')
                            self.context["form"] = {'sign_in_form': self.sign_in_form,
                                                    'sign_up_form': self.sign_up_form}
                            return render(request, self.template_name, self.context)
                    else:

                        messages.error(request, 'Incorrect username')
                        self.context["form"] = {'sign_in_form': self.sign_in_form, 'sign_up_form': self.sign_up_form}
                        return render(request, self.template_name, self.context)
                except:
                    messages.error(request, 'Invalid username and password')
                    self.context["form"] = {'sign_in_form': self.sign_in_form, 'sign_up_form': self.sign_up_form}
                    return render(request, self.template_name, self.context)
            else:
                messages.error(request, 'Invalid username and password')
                self.context["form"] = {'sign_in_form': self.sign_in_form, 'sign_up_form': self.sign_up_form}
                return render(request, self.template_name, self.context)

        #---------registration code----------
        elif "signup" in request.POST:

            form = self.sign_up_form(request.POST)
            if form.is_valid():

                form.save()

                return redirect("registerlogin")
            else:
                messages.error(request, 'Sorry! you entered invalid Information... Please Try Again')
                self.context["form"] = {'sign_in_form': self.sign_in_form, 'sign_up_form': self.sign_up_form}
                return render(request, self.template_name, self.context)
        else:

            self.context["form"] = {'sign_in_form': self.sign_in_form, 'sign_up_form': self.sign_up_form}
            return render(request, self.template_name, self.context)

#Home page
@login_required
def index(request):

    return render(request, "Product/home.html")


#View for adding products
@method_decorator(login_required,name='dispatch')
class AddProductView(TemplateView):
    model=Products
    template_name = "Product/create_product.html"
    form_class=ProductForm
    context={}
    def get(self,request, *args, **kwargs):
        self.context["form"]=self.form_class
        return render(request, self.template_name, self.context)
    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST,files=request.FILES)
        if form.is_valid():
            product_name=form.cleaned_data.get('product_name')
            description=form.cleaned_data.get('description')
            image=form.cleaned_data.get('image')
            user=CustomUser.objects.get(username=request.user)
            userid=user.id
            add_product=Products(product_name=product_name,description=description,image=image,user_id=userid)
            add_product.save()
            return redirect("list")
        else:
            self.context["form"]=form
            return render(request,self.template_name,self.context)

class ObjectMixin(object):
    model=None
    def get_object(self,id):
        return self.model.objects.get(id=id)

@method_decorator(login_required,name='dispatch')
class DeleteProduct(TemplateView,ObjectMixin):
    model=Products

    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")

        product=self.get_object(id)
        product.delete()
        return redirect("list")


#View for listing the products
@method_decorator(login_required,name='dispatch')
class ProductListView(TemplateView):
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(username=request.user)
        items = Products.objects.filter(user_id=user.id)
        if items:
            context = {}
            context['items'] = items
            return render(request, "Product/list.html", context)
        else:
            messages.error(request, 'No Products Found')
            return render(request, "Product/list.html")



def signout(request):
    logout(request)
    return redirect("registerlogin")