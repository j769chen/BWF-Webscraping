import requests
import urllib.request
import time
from bs4 import BeautifulSoup

ladders = ['https://bwfbadminton.com/rankings/2/bwf-world-rankings/8/men-s-doubles/2019/46/?rows=50&page_no=1',
           'https://bwfbadminton.com/rankings/2/bwf-world-rankings/9/women-s-doubles/2019/47/?rows=50&page_no=1',
           'https://bwfbadminton.com/rankings/2/bwf-world-rankings/10/mixed-doubles/2019/47/?rows=50&page_no=1']

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


ranks = []
players = []

for i in range(1, 51):  # since doubles pairs, need to have index twice
    ranks.append(i)
    ranks.append(i)

for i in range(100):  # doubles
    players.append(Player(playerLinks[i].getText().strip(), ranks[i],
                          countries[i].findChild('span', recursive=True).getText().strip()))

print("Rank Country Pair")

for i in range(18):
    print(players[i].rank, "  ", players[i].country, "   ", players[i].name)
    if i % 2 != 0:
        print("")  # newline to differentiate pairs

for i in range(18, 100):
    print(players[i].rank, " ", players[i].country, "   ", players[i].name)
    if i % 2 != 0:
        print("")
