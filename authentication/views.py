from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from authentication.forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from django import forms

# Create your views here.

def register(request):
    context = {}

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            registered_user = authenticate(request, email=email, password=password)
            
            if registered_user:
                print("hello")
                login(request, registered_user)
                return redirect('predict_calories')
    else:
        context['form'] = RegisterForm()
       

    return render(request, "register.html", context)


def login_view(request, *args, **kwargs):
    form     = LoginForm(request.POST or None) # one of the two
    if request.POST:
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # return redirect('predict_calories')
                return redirect('home')
       
    return render(request,'login.html', context={'form': form})
   
                
def logout_view(request):
    logout(request)
    return redirect('home')



        
