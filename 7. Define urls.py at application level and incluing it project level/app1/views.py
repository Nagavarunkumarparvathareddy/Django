from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def applicatioview(request):
    output ='''
    <html>
    <body>
    <h1>Defining urls.py at application level and the including urls.py at project level</h1>
    </body>
    </html>
    '''
    response = HttpResponse(output)
    return response