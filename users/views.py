from django.shortcuts import render
from django.http import HttpResponse


def me(request):
    return HttpResponse("This is user profile")


def login(request):
    return HttpResponse("This is login page")
