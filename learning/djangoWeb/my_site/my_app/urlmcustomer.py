from django.urls import path
from .views import customer as views, address, login, Signup, order, acount

urlpatterns = [
    path('signup/', Signup.as_view(), name='mcustomer/signup'),
    path('login/', login.index, name='mcustomer/login'),
    
    path('order/', order.index, name='mcustomer/order'),
    path('account/', acount.index, name='mcustomer/acount'),
]