from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from my_app.models.mcustomer import mcustomer
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password


class Signup(View):
    
     def get(self, request):
        return render(request, 'msignup.html')
     
     def post(self, request):
         data = request.POST
         try:
             mcustomer.objects.create(
                name=data['name'],
                email=data['email'],
                password=make_password(data['password'])
            )
             msg = "Account Created!"
             messages.success(request, msg)
         except ValueError as e:
             msg = str(e) 
             messages.error(request, msg)
         
         return redirect("/my_app/mcustomer/signup/")
         
         