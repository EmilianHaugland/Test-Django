# import requests module
from pickle import FALSE
import requests
import json
import urllib.parse
 
 
class Game:
    def __init__(self,obj) -> None:
        self.id=obj['id']
        self.error=False
        try:
            self.price=obj['price']
            self.name=obj['title']
            self.img=obj['img']
            self.activation_platform=obj['activation_platform']
            self.url=obj['url']
            self.store_name=obj['source']
        except:
            self.error=True
 
    def print(self):
        print("ID: " + str(self.id))
        print("Price: " + str(self.price_to_nok(self.price)))
        print("Name: " + str(self.name))
        print("Url: " + str(self.url))
        print("Image: " + str(self.img))
        print("Store Name: " + str(self.store_name))
        print("Activation Platform: " + str(self.activation_platform))
        print("")
 
    def price_to_nok(self,value):
        return float(value)*10.35 #Nov 1, 16:24 UTC · Disclaimer
 
class GamePrices:
 
    def add_games_res(self,games_out,title,page=1):
        url = "https://best-game-price-search.p.rapidapi.com/bestprice/"+title+"/"
 
        querystring = {"page":str(page),"limit":"5","currency":"USD","maxprice":"15000"}
 
        headers = {
            "X-RapidAPI-Key": "f84790c2d2msha4b8804d1a0dcc4p13782ejsn64354da2d276",
            "X-RapidAPI-Host": "best-game-price-search.p.rapidapi.com"
        }
 
        response = requests.request("GET", url, headers=headers, params=querystring)
 
        if response.status_code==200:
            for game in response.json()['results']:
                games_out.append(game)
        if response.status_code>200 or len(response.json())<=2:
            return games_out
        else:
            return self.add_games_res(games_out,title,response.json()['nextPage']['page'])
 
 
    def get_games(self,title,page=1):
       games=[]
       self.add_games_res(games,title,page)
       objects_games=[]
       for game in games:
        the_game= Game(game)
        if the_game.error==False:
            objects_games.append(the_game)
       return objects_games
