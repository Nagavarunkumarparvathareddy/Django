from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    response = render(request,'app1/index.html')
    return response