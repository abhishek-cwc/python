from django.urls import path, include
from . import urlcustomer, urladdress, urlmproducts, urlmcustomer

app_name = 'my_app'

urlpatterns = [
    path("address/", include(('my_app.urladdress'))),
    path("customer/", include('my_app.urlcustomer')),
    path("mproducts/", include('my_app.urlmproducts')),
    path("mcustomer/", include('my_app.urlmcustomer')),
]