"""
Definition of views.
"""


from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from array import *
from GamePrices import *






      # Do struff

class person:

    def __init__(self,firstname,lastname, mail):
        self.firstname = firstname
        self.lastname = lastname
        self.mail = mail
        self.fullname = self.lastname +', '+ self.firstname




def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    game_prices = GamePrices()
    games=[]
    gamename=request.POST.get("gamename",None)
    if  gamename:
        games=game_prices.get_games(gamename)


    return render(
        request,
        'app/index.html',
        {
            
            'games' : games,
            'title' : 'Home Page',
            'year':datetime.now().year,
        }
    )
    

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    mleh = person('Emilian', 'Haugland', 'emilian.haugland@blizzwizz.net')
    mlmk = person('Mari', 'Kallevik', 'test@gmail.com')
    persons = [mleh, mlmk]


    return render(
        request,
        'app/contact.html',
        {
             
                
             'persons' : persons,
             'title':'Personer'
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
