from django.urls import path
from . import views

urlpatterns = [
    path('gnestedaddlist/', views.GAddressList.as_view(), name="gnestedaddlist"),
    path('glist/', views.GCustomerList.as_view(), name="gccustomerlist"),
    path('mclist/', views.MCustomerList.as_view(), name="mccustomerlist"),
    path('clist/', views.CustomerList.as_view(), name="ccustomerlist"),
    path('list/', views.customer_list, name="customerlist"),
    path('create/', views.customer_create, name="customerCreate"),
    path('detail/<int:pk>', views.customer_detail, name="customerDetail"),
    path('update/<int:pk>', views.customer_update, name="customerUpdate"),
    path('delete/<int:pk>', views.customer_delete, name="customerdelete"),
]