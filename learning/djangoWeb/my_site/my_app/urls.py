# from django.urls import path, include
# from .views import customer as views, address

from django.urls import path, include
from . import urlcustomer, urladdress

app_name = 'my_app'

urlpatterns = [
    path("address/", include(('my_app.urladdress'))),
    path("customer/", include('my_app.urlcustomer')),
]