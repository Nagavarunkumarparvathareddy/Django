from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def deposit(amount):
    output ='''<HTML>
    <BODY bgcolor =cyan>
    <H2>This is deposit view </H2>
    </BODY>
    </HTML>'''
    displayoutput = HttpResponse(output)
    return  displayoutput

def withdraw(amount):
    output = '''<html>
    <body bgcolor = yellow>
    <h2>This is withdraw view</h2>
    </body>
    </html>'''
    displayoutput  = HttpResponse(output)
    return displayoutput