import imp
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
# Create your views here.

from django.contrib.auth.models import User

def sign_in(request):
    return HttpResponse('ログインします。')

def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('tweets:index'))