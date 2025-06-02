from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.customer_list, name="customerlist"),
    path('create/', views.customer_create, name="customerCreate"),
    path('detail/<int:pk>', views.customer_detail, name="customerDetail"),
    path('update/<int:pk>', views.customer_update, name="customerUpdate"),
    path('delete/<int:pk>', views.customer_delete, name="customerdelete"),
]