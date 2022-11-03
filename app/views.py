"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Personer',
            'message':'Kontaktpersoner',
            'mailMK' : 'marikallevik@gmail.com',
            'mailEH' : 'emilian.haugland05@gmail.com',
            'telEH' : '400 52 933',
            'telMK' : '944 35 459', 
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Om oss',
            'message':'Your application description page.',
            'omoss' : 'Vi er et lag på to personer som jobber for at folk med interesse for spill skal ha en lettere mulighet for å finne spill på tilbud.',
            'info' : 'Vi har valgt og lagge dette grunnet egen interesse men vil dele våres arbeid med folket'
            'year':datetime.now().year,
        }
    )
