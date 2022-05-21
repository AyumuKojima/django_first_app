import imp
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
# Create your views here.

from django.contrib.auth.models import User

def sign_in(request):
    return render(request, 'accounts/sign_in.html')

def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('tweets:index'))

def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        print("log-in user: " + str(user))
        return HttpResponseRedirect(reverse('tweets:index'))
    else:
        print("Something went wrong.")
        return render(request, 'accounts/sign_in.html')
