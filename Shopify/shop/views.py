from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("We are at about")

def contact(request):
    return HttpResponse("We are at contact")

def search(request):
    return HttpResponse("We are at search")

def tracker(request):
   return HttpResponse("We are at tracker")

def productview(request):
    return HttpResponse("We are at productview")

def cheakout(request):
    return HttpResponse("We are at cheakout")

