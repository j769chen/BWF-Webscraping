import requests
import urllib.request
import time
from bs4 import BeautifulSoup

ladders = ['https://bwfbadminton.com/rankings/2/bwf-world-rankings/6/men-s-singles/2019/46/?rows=100&page_no=1',
           'https://bwfbadminton.com/rankings/2/bwf-world-rankings/7/women-s-singles/2019/47/?rows=100&page_no=1']

url = ladders[0]

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

playerLinks = soup.findAll('a', {"class": "tooltip"})
countries = soup.findAll('div', {"class": "country"})


class Player:
    def __init__(self, name, rank, country):
        self.name = name
        self.rank = rank
        self.country = country


players = []
for i in range(100):  # get top 100 singles player data
    players.append(Player(playerLinks[i].getText().strip(), i + 1,
                          countries[i].findChild('span', recursive=True).getText().strip()))

print("Rank Country Player")

for i in range(9):
    print(players[i].rank, "  ", players[i].country, "   ", players[i].name)

for i in range(9, 99):
    print(players[i].rank, " ", players[i].country, "   ", players[i].name)

print(players[99].rank, "", players[99].country, "   ", players[99].name)
