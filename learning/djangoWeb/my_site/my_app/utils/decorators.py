from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from my_app.models.CustomerToken import CustomerToken  
from my_app.models import customer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


def classcustomer_token_required(view_func):
    @wraps(view_func)
    def _wrapped_view(self, request, *args, **kwargs):
        # token = (
        #     request.GET.get('token') or
        #     request.headers.get('X-Customer-Token')  # support both GET param and header
        # )

        token = request.headers.get('X-Customer-Token')
        print("Token received:", token)
        #token = 11

        if not token:
            return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            print(token)
            customer_token = CustomerToken.objects.get(key=token)
            print(customer_token.customer)
        except CustomerToken.DoesNotExist:
            return Response({'error': 'Invalid or expired token'}, status=status.HTTP_401_UNAUTHORIZED)

        # Attach customer to request
        request.customer = customer_token
        request.token = token
        return view_func(self, request, *args, **kwargs)
    
    return _wrapped_view


def functioncustomer_token_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # token = (
        #     request.GET.get('token') or
        #     request.headers.get('X-Customer-Token')  # support both GET param and header
        # )

        token = request.headers.get('X-Customer-Token')
        print("Token received:", token)
        #token = 11

        if not token:
            return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            print(token)
            customer_token = CustomerToken.objects.get(key=token)
            print(customer_token.customer)
        except CustomerToken.DoesNotExist:
            return Response({'error': 'Invalid or expired token'}, status=status.HTTP_401_UNAUTHORIZED)

        # Attach customer to request
        request.customer = customer_token
        request.token = token
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view


def funjwt_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        jwt_authenticator = JWTAuthentication()
        print("test")

        # Get the token from Authorization header
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            raise AuthenticationFailed("Authorization header missing or invalid")

        token = auth_header.split(' ')[1]
        print(token)

        validated_token = jwt_authenticator.get_validated_token(token)
        user_id = validated_token.get('user_id') 
        customerobj = customer.objects.get(id=user_id)
        print(customerobj)
        #user = jwt_authenticator.get_user(validated_token)

        # try:
        #     print(token)
        #     validated_token = jwt_authenticator.get_validated_token(token)
        #     user = jwt_authenticator.get_user(validated_token)
        # except Exception as e:
        #     raise AuthenticationFailed(str(e))

        # Attach user to request
        #request.user = customerobj
        customerobj.customer_id = customerobj.id
        request.customer = customerobj
        return view_func(request, *args, **kwargs)

    return _wrapped_view