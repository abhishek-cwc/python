from django.shortcuts import render, redirect, get_object_or_404
from my_app.models import mproduct, mcategory

def index(request):
    productCollection = mproduct.getAllProducts()
    categoryCollection = mcategory.getAllCategory()
    data = {
        'products' : productCollection,
        'categorys' : categoryCollection,
    }
    return render(request, 'mproducts.html', data)