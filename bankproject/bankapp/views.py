from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def home(request):
    return render(request,"index.html")


def signin(request):
    return render(request,"signin.html")
def signout(request):
    return render(request,"signout.html")

def forum(request):
    return render(request,"forum.html")
