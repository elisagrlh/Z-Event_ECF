from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    f = open("C:/xampp/htdocs/ECF/SiteWeb/ZEvent/ZEvent/business/index.html", "r")
    resp = f.read()
    return HttpResponse(f"{resp}")