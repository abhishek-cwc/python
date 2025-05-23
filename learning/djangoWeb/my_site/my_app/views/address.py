from django.shortcuts import render, redirect, get_object_or_404

from my_app.models import address

from django.contrib import messages

from .addressForm import addressRegistration

from django.db.models import Q

from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage

import csv

def functionCreateView(request):
    if request.method == 'POST' :
        city = request.POST['city']
        state = request.POST['state']
        address.objects.create(city=city, state=state)
        messages.success(request, 'Address added!')
        return redirect('my_app:address/list')  
        
    return render(request, 'addresscreate.html')

def functionUpdateView(request, id):
    obj = get_object_or_404(address, pk=id)
    if request.method == 'POST':
        fm = addressRegistration(request.POST, instance=obj)
        fm.save()
        messages.success(request, "Updated")
        return redirect("my_app:address/list")

    else:
        fm = addressRegistration(instance = obj)

    return render(request, 'addressupdate.html', {'form': fm})
    


def functionListView(request):
    allAddress = address.objects.all() 
    
    if request.method == "GET":
        st = request.GET.get('query')
        if st != None:
            #allAddress = address.objects.filter(city__icontains = st) 
            allAddress = address.objects.filter(
                Q(city__icontains=st) | Q(state__icontains=st)
            )

    p = Paginator(allAddress, 5)
    page_number = request.GET.get('page', 1)
    page = p.page(page_number)
    return render(request, 'addresslist.html', {'allAddress' : page})

def functionDelete(request,id):
    obj = get_object_or_404(address, pk=id)
    obj.delete()
    messages.success(request, "deleted")
    return redirect("my_app:address/list")

def export(request):
    allAddress = address.objects.all() 
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename="address.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'CITY', 'STATE'])
    for data in allAddress:
        writer.writerow([data.id, data.city, data.state])
    return response


