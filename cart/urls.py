from django.urls import path
from . import views

urlpatterns = [

    path('',views.showcart,name='showcart'),
    path('addtocart',views.add_to_cart),
    path('deletefromcart',views.deletefromcart),
]