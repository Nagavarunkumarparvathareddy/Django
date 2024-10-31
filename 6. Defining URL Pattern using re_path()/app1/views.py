from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    output ='''
    <html>
    <body>
    <h1>This is view page</h1>
    </body>
    </html>
    '''
    response = HttpResponse(output)
    return response
