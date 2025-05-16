from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    myVar = {
        "name":"abhi",
        "lname": "Path",
    }
    return render(request, 'my_app/home.html', context=myVar)

def product(request):
    return HttpResponse("Welcome product view!")

def login(request):
    return HttpResponse("Welcome login view!")

#### dynamic view #####
newsArticale = {
    'sports' : "sports page",
    'tech' : "tech page",
}

def news(request, topic):
    return HttpResponse(newsArticale[topic])