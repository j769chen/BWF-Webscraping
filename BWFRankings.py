import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://bwfbadminton.com/rankings/2/bwf-world-rankings/6/men-s-singles/2019/46/?rows=100&page_no=1'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

playerLinks = soup.findAll('a', {"class": "tooltip"})
countries = soup.findAll('div', {"class": "country"})

class Player:
    def __init__(self, name, rank, country):
        self.name = name
        self.rank = rank
        self.country = country

children = []
players = []
ranks = []

#get player names
for i in playerLinks:
    players.append(i.getText())

#get array of ranks
for i in range(players.__len__()):
    ranks.append(i)

#clean player parameters
for i in ranks:
    players[i] = players[i].strip()

#get countries
for i in countries:
    children.append(i.findChild('span', recursive=True).getText())

#clean country parameters
for i in ranks:
    children[i] = children[i].strip()

#output
print("Rank Country Player")

for i in range(9):
    print(i+1, "  ", children[i], "   ", players[i])

for i in range(9, 99):
    print (i+1, " ",children[i], "   ", players[i])

print ("100 ", children[99], "   ", players[99])