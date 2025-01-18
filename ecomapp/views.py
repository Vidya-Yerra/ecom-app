from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from ecomapp.models import Product,Review
from ecomapp.serializers import ProductSerializer,ReviewSerializer
from rest_framework import viewsets
from django.shortcuts import redirect

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

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

