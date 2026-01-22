from  django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Welcome to Project 1 Home Page")
    return render(request, 'index.html')
