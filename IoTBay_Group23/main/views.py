from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.


def index(response, id):
    cust = Customer.objects.get(id=id)
    return HttpResponse(f"<h1>{cust.name}</h1>")


def v1(response):
    return HttpResponse("<h1>View 1!</h1>")
