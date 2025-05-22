from django.urls import path
from .views import customer as views, address

urlpatterns = [
    #path('classbaseview/', views.ClassBaseView.as_view(), name='classbaseview'),
    path('create/', views.ClassCreateView.as_view(), name='customer/create'),
    path('list/', views.ClassListView.as_view(), name='customer/list'),
    path('detail/<int:pk>', views.ClassDetailedView.as_view(), name='customer/detail'),
    path('update/<int:pk>', views.ClassUpdateView.as_view(), name='customer/update'),
    path('delete/<int:pk>', views.ClassDeleteView.as_view(), name='customer/delete'),
]