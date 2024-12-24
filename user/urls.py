from django.urls import path
from . import views 

urlpatterns = [
   
    path('',views.Signup.as_view()),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user)
    
]