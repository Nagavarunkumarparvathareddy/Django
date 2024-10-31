from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Python(request):
    output='''
    <html>
    <body>
    <h1>Python by kvr sir<h1>
    <p>Duration : 4 months</p>
    <p>Cost : 6000</p>
    <br>
    <br>
    <h1>Python by Gupta sir<h1>
    <p>Duration : 3 months</p>
    <p>Cost : 6000</p>
    </body>
    </html>
    '''
    response = HttpResponse(output)
    return response