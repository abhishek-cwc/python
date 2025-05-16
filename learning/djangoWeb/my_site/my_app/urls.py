from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('login/', views.login, name='login'),
    path('news/<topic>', views.news, name='news'),
]