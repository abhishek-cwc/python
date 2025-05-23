from django.urls import path
from .views import customer as views, address

#app_name = 'my_app_address'

urlpatterns = [
    path('create/', address.functionCreateView, name='address/create'),
    path('list/', address.functionListView, name='address/list'),
    path('update/<int:id>', address.functionUpdateView, name='address/update'),
    path('delete/<int:id>', address.functionDelete, name='address/delete'),
    path('export/', address.export, name='address/export'),
]