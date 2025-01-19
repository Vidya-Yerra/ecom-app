from django.urls import path,include
from . views import authView,home,productsView, reviewView

urlpatterns = [
    path("",home,name="home"),
    path('signup/',authView, name="authView"),
    path('accounts/',include("django.contrib.auth.urls")),
    path('products/',productsView, name="productsview"),
    path('product/review/<int:product_id>',reviewView,name='reviewview')

    

]