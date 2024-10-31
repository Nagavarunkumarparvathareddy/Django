from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def python(request):
    output='''
    <html>
    <body>
    <h1>Python by Mahesh sir<h1>
    <p>Duration : 4 months</p>
    <p>Cost : 6000</p>
    <br>
    <br>
    <h1>Python by kavitha mam<h1>
    <p>Duration : 3 months</p>
    <p>Cost : 6000</p>
    </body>
    </html>
    '''
    response = HttpResponse(output)
    return response

def home(request):
    output = '''
    <html>
    <a href=/Ameerpet>Python Training - Ameerpet</a><br><br>
    <a href=/KPHB>Python Training - KPHB</a><br><br>
    </html>

   '''
    response = HttpResponse(output)
    return response