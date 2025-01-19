from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from ecomapp.models import Product,Review
from ecomapp.serializers import ProductSerializer,ReviewSerializer
from rest_framework import viewsets
from django.shortcuts import redirect
import datetime

# Create your views here.

@login_required
def home(request):
    return render(request,"home.html",{})
def authView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect("/accounts/login/")  
    else:  
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def productsView(request):
    products = Product.objects.all()
    return render(request,"products.html",{"products":products})

def reviewView(request,product_id):
    print("In review view function")
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        user=request.user
        text=request.POST.get('review_product')
        currentdatetime=datetime.datetime.now()
        review=Review(user=user,product=product,content=text,datetime=currentdatetime)
        review.save()
        return redirect('/ecom/products/')
    else:
        return render(request,"review.html",{"product":product})



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

