from django.shortcuts import render
from django.http import JsonResponse
from my_app.models import customer

from .api_files.serilizers import CustomerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view()
def customer_list(request):
    customerData = customer.objects.all()
    serilizedData = CustomerSerializer(customerData, many=True)
    return Response(serilizedData.data)

@api_view()
def customer_detail(request, pk):
    customerData = customer.objects.get(pk=pk)
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
