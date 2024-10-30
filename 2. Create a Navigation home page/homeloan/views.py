from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def personal(request):
    output = '''
    <html>
    <body bgcolr=red>
    <h1>This is the view for applying Personal Loan <h1>
    </body>
    <html>
    '''
    response = HttpResponse(output)
    return response

def educational(request):
    output = '''
    <html>
    <body bgcolor = green>
    <h1>This is the view for applying Educational Loan</h1>
    </body>
    </html>
    '''
    response = HttpResponse(output)
    return response

def house(request):
    output = '''
    <html>
    <body bgcolor = yellow>
    <h1>This is the view for home Educational Loan</h1>
    </body>
    </html>
    '''
    response = HttpResponse(output)
    return response


def finance(request):
    output = '''
    <html>
    <body bgcolor = blue>
    <h1>This is the view for applying Finance Loan</h1>
    </body>
    </html>
    '''
    response = HttpResponse(output)
    return response

def car(request):
    output = '''
    <html>
    <body bgcolor = orange>
    <h1>This is the view for car  Loan</h1>
    </body>
    </html>
    '''
    return HttpResponse(output)

def gold(request):
    output = '''
    <html>
    <body bgcolor = gold>
    <h1>This is the view for applying gold Loan</h1>
    </body>
    </html>
    '''
    response = HttpResponse(output)
    return response

def home(request):
    output = '''
    <html>
    <a href = /house > Home Loan</a><br><br>
    <a href = /personal>Personal Loan</a><br><br>
    <a href = /educational>Educational Loan</a><br><br>
    <a href = /finance>Finance Loan</a><br><br>
    <a href = /car>Car Loan</a><br><br>
    <a href = /gold>Gold Loan</a><br><br>
    </html>
    '''
    respone = HttpResponse(output)
    return respone