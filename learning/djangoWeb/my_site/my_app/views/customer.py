from django.shortcuts import render
from django.http import HttpResponse
#from my_app.models import models
#from my_app.models import customer
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
#from .classbaseform  import ClassBaseForm
#from ..models.customer import customer
from my_app.models import customer

#############################   Class Base View ##########################

class ClassBaseView(TemplateView):
    template_name = 'classbase.html'

# class ClassBaseFormView(FormView):
#     form_class = ClassBaseForm
#     template_name = 'classbaseform.html'
#     success_url = "/my_app/classbaseview"

#     def form_valid(self, form):
#         #print(form.cleaned_data)
#         return super().form_valid(form)

class ClassCreateView(CreateView):
    model = customer
    #fields = "__all__"
    fields = {'fname', 'email'}
    #success_url = "/my_app/classbaseview"
    success_url = reverse_lazy("my_app:customer/list")

    def form_valid(self, form):
        response =  super().form_valid(form)
        messages.success(self.request,"Created !")
        return response
    
class ClassListView(ListView):
    model = customer
    queryset = model.objects.all().order_by('fname')
    context_object_name = "customer_lsit"

class ClassDetailedView(DetailView):
    model = customer
    context_object_name = 'customer'

class ClassUpdateView(UpdateView):
    model = customer
    fields = {'fname', 'email'}
    context_object_name = 'customer'
    success_url = reverse_lazy("my_app:customer/list")

    def form_valid(self, form):
        response =  super().form_valid(form)
        messages.success(self.request, "Updated!")
        return response
    

class ClassDeleteView(DeleteView):
    model = customer
    success_url = reverse_lazy("my_app:customer/list")

    def form_valid(self, form):
        response =  super().form_valid(form)
        messages.success(self.request, "Deleted!")
        return response




# Create function base your views here.
def index(request):
    myVar = {
        "name":"abhi",
        "lname": "Path",
    }
    return render(request, 'home.html', context=myVar)

def product(request):
    allCustomer = customer.objects.all() 
    return render(request, 'product.html', {'allCustomer' : allCustomer})

def login(request):
    return HttpResponse("Welcome login view!")

#### dynamic view #####
newsArticale = {
    'sports' : "sports page",
    'tech' : "tech page",
}

def news(request, topic):
    return HttpResponse(newsArticale[topic])