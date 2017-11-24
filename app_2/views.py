from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    HttpResponse("<h1>App 2</h1>")


def template_1(request):
    return render(request, "app_2/template_1.html")
