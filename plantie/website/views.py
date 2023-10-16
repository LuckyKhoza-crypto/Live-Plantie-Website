from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import models
from .import forms

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def your_plantie(request):
    form = forms.LoginForm()
    message = "Login to your Plantie account to submit a picture!"
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                message = "You have successfully logged in!"
            else:
                message ="Incorrect username or password."
    return render(request, 'your_plantie.html', context = {'form': form, 'message': message})

def logout_user(request):
    logout(request)
    return redirect('home')

def signup_user(request):
    message = ''
    form = forms.SignUpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            message = "Failed to sign you up. Please retry."
    return render(request, 'signup_user.html', {'form': form, 'message':message})


def plant_show(request):
    return render (request, 'plant_show.html', {})

def why_plant(request):
    return render (request, 'why_plant.html', {})

