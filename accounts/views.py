from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

from django.contrib.auth.models import User

def sign_in(request):
    return HttpRequest('ログインします。')