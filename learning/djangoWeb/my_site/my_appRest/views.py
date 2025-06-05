from django.shortcuts import render
from django.http import JsonResponse
from my_app.models import customer, address

from my_app.models.CustomerToken import CustomerToken

from .api_files.serilizers import CustomerSerializer, AddressSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

from rest_framework.views import APIView

from rest_framework import mixins, generics, viewsets
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken


from my_app.utils.decorators import functioncustomer_token_required, classcustomer_token_required, funjwt_required

class CustomerJwtLoginView(APIView):
    def post(self, request):
        customerEmail = request.data.get('email')
        password = request.data.get('password')
        user = customer.objects.get(email=customerEmail)
        #user = authenticate(request, username=email, password=password)
        if user is not None:
            #token, created = Token.objects.get_or_create(user=user)
            #token, created = CustomerToken.objects.get_or_create(customer=user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'token': str(refresh.access_token),
                'refresh': str(refresh),
                'customer_id': user.id,
                'email': user.email
            })
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class CustomerLoginView(APIView):
    def post(self, request):
        customerEmail = request.data.get('email')
        password = request.data.get('password')
        user = customer.objects.get(email=customerEmail)
        #user = authenticate(request, username=email, password=password)
        if user is not None:
            #token, created = Token.objects.get_or_create(user=user)
            token, created = CustomerToken.objects.get_or_create(customer=user)
            return Response({
                'token': token.key,
                'customer_id': user.id,
                'email': user.email
            })
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class CustomerLogOutView(APIView):
    @classcustomer_token_required
    def post(self, request):
        token_key = request.token
        token = CustomerToken.objects.get(key=token_key)
        # print(token)
        token.delete()
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        
        

 ## view Set in place of  GCustomerList and GCustomerDetail
 #This viewset automatically provides `list` and `retrieve` actions.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = customer.objects.all()
    serializer_class = CustomerSerializer

# class GCustomerList(generics.ListCreateAPIView):
#     queryset = customer.objects.all()
#     serializer_class = CustomerSerializer

# class GCustomerDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = customer.objects.all()
#     serializer_class = CustomerSerializer


class AddressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = address.objects.all()
    serializer_class = AddressSerializer

# class GAddressList(generics.ListCreateAPIView):
#     queryset = address.objects.all()
#     serializer_class = AddressSerializer




class MCustomerList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CustomerList(APIView):

    def get(self, request, format=None):
        customers = customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view()
def customer_list(request):
    customerData = customer.objects.all()
    serilizedData = CustomerSerializer(customerData, many=True)
    return Response(serilizedData.data)

@api_view()
@authentication_classes([])
@permission_classes([])
#@functioncustomer_token_required
@funjwt_required
def customer_detail(request, pk):
    print(request.customer.customer_id)
    #return Response({'msg': "data"})
    customerData = customer.objects.get(pk=request.customer.customer_id)
    serilizedData = CustomerSerializer(customerData)
    return Response(serilizedData.data)

@api_view(['POST'])
def customer_create(request):
    serilizer = CustomerSerializer(data = request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data)
    else:
        return Response(serilizer.error_messages) 
    
@api_view(['PUT'])
def customer_update(request, pk):
    customerData = customer.objects.get(pk=pk)
    serilizer = CustomerSerializer(customerData, data= request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data)
    else:
        return Response(serilizer.errors)
    
@api_view(['DELETE'])
def customer_delete(request, pk):
    customerData = customer.objects.get(pk=pk)
    customerData.delete()
    return Response({'message': 'customer deleted'}, status=status.HTTP_200_OK)








# Create your views here.



# def customer_list(request):
#     customerData = customer.objects.all()
#     data = {
#         'customer': list(customerData.values())
#     }
#     return JsonResponse(data)

# def customer_detail(request, pk):
#     customerData = customer.objects.get(pk=pk)
#     print(customerData.fname)
#     data = {
#         'name' : customerData.fname
#     }
#     return JsonResponse(data)
