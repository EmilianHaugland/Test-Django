"""
Definition of views.
"""


from datetime import datetime
import email
from django.shortcuts import render
from django.http import HttpRequest
from array import *

class maillist:

    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.mail = first + '.' + last + '@blizzwizz.net'

    def get_name(self):
       self.first
       self.last

mleh = maillist('emilian', 'haugland')
mlmk = maillist('mari', 'kallevik')

arr = [mleh.mail, mlmk.mail]


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
             
                
             'emilian' : mleh.mail,
             'mari' : mlmk.mail,
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
            'info' : 'Vi har valgt og lagge dette grunnet egen interesse men vil dele våres arbeid med folket',
            'year':datetime.now().year,
        }
    )
