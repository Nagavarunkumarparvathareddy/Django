from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greet1(request):
    message = '<h1>Hello Django Welcoming you</h1>'
    response = HttpResponse(message)
    return response

def greet2(request,name):
    message =f'<h1>Hello {name} Welcome .Complete your Django Course</h1>'
    response = HttpResponse(message)
    return response 