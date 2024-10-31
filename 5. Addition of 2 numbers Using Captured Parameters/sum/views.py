from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request,s1,s2):
    s = int(s1)+int(s2)
    output =f'<h2>Sum of {s1} & {s2} is {s}</h2>'
    response = HttpResponse(output)
    return response
