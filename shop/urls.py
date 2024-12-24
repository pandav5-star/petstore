from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='shop'),
    path('search',views.search),
    path('about',views.about),
    path('details',views.details,name='details')
    
]