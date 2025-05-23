from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from my_app.models.mcustomer import mcustomer
from django.contrib import messages


class Signup(View):
    
     def get(self, request):
        return render(request, 'msignup.html')
     
     def post(self, request):
         data = request.POST
         try:
             mcustomer.create(data)
             msg = "Account Created!"
             messages.success(request, msg)
         except ValueError as e:
             msg = str(e) 
             messages.error(request, msg)
         
         return redirect("/my_app/mcustomer/signup/")
         
         