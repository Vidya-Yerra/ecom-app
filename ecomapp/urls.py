from django.urls import path,include
from . views import authView,home,productsView

urlpatterns = [
    path("",home,name="home"),
    path('signup/',authView, name="authView"),
    path('accounts/',include("django.contrib.auth.urls")),
    path('products/',productsView, name="productsview")
    

]