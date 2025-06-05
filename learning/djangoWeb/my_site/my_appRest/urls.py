from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'customer', views.UserViewSet, basename='gccustomer')
router.register(r'address', views.AddressViewSet, basename='gccustomeraddress')

urlpatterns = [

    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('account/jwtlogin/', views.CustomerJwtLoginView.as_view(), name='jwtlogin'),

    #path('account/login/', obtain_auth_token, name="login"),
    path('account/login/', views.CustomerLoginView.as_view(), name="login"),
    path('account/logout/', views.CustomerLogOutView.as_view(), name="logout"),

    #path('gnestedaddlist/', views.GAddressList.as_view(), name="gnestedaddlist"),
    
    path('', include(router.urls)),
    #path('glist/', views.GCustomerList.as_view(), name="gccustomerlist"),
    #path('glist/<int:pk>', views.GCustomerDetail.as_view(), name="gccustomerdetail"),

    path('mclist/', views.MCustomerList.as_view(), name="mccustomerlist"),
    path('clist/', views.CustomerList.as_view(), name="ccustomerlist"),
    path('list/', views.customer_list, name="customerlist"),
    path('create/', views.customer_create, name="customerCreate"),
    path('detail/<int:pk>', views.customer_detail, name="customerDetail"),
    path('update/<int:pk>', views.customer_update, name="customerUpdate"),
    path('delete/<int:pk>', views.customer_delete, name="customerdelete"),
]

# http://127.0.0.1:8000/rest/detail/1
# http://127.0.0.1:8000/rest/account/logout
# http://127.0.0.1:8000/rest/account/jwtlogin/