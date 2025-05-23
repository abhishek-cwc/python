from django.urls import path
from .views import customer as views, address, mproducts

urlpatterns = [
    path('', mproducts.index, name='mproducts/'),
]