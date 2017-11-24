from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>App 1</h1>")


def template_1(request):
    return render(request, "app_1/template_1.html")


def template_2(request):
    return render(request, "app_1/template_2.html")

