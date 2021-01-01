import requests
import urllib.request
import time
from bs4 import BeautifulSoup


class Player:
    def __init__(self, name, rank, country):
        self.name = name
        self.rank = rank
        self.country = country


class Pair:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

ladders = {'MD': 'https://bwfbadminton.com/rankings/2/bwf-world-rankings/8/men-s-doubles/2019/46/?rows=50&page_no=1',
           'WD': 'https://bwfbadminton.com/rankings/2/bwf-world-rankings/9/women-s-doubles/2019/47/?rows=50&page_no=1',
           'XD': 'https://bwfbadminton.com/rankings/2/bwf-world-rankings/10/mixed-doubles/2019/47/?rows=50&page_no=1',
           'MS':  'https://bwfbadminton.com/rankings/2/bwf-world-rankings/6/men-s-singles/2019/46/?rows=100&page_no=1',
           'WS': 'https://bwfbadminton.com/rankings/2/bwf-world-rankings/7/women-s-singles/2019/46/?rows=100&page_no=1'
           }


def requestData(requested_ladder):
    doubles = False

    if (requested_ladder == ladders['MD'] or requested_ladder == ladders['WD']
            or requested_ladder == ladders['XD']):
        doubles = True

    response = requests.get(requested_ladder)

    soup = BeautifulSoup(response.text, "html.parser")

    playerLinks = soup.findAll('a', {"class": "tooltip"})
    countries = soup.findAll('div', {"class": "country"})

    return playerLinks, countries, doubles


def setPairs(players):
    pairs = []
    for i in range(0, len(players), 2):
        pairs.append(Pair(players[i], players[i + 1]))

    # Fix ranks
    for i in range(len(pairs)):
        pairs[i].player1.rank = i + 1
        pairs[i].player2.rank = pairs[i].player1.rank

    return pairs


def getPlayerData(playerLinks, countries, doubles): # Returns list of player objects or pair objects depending on discipline
    players = []

    # get player objects
    for i in range(len(playerLinks)):
        players.append(Player(playerLinks[i].getText().strip(), i + 1, countries[i].findChild('span', recursive=True).
                              getText().strip()))

    if doubles:
        return setPairs(players)

    return players


def main(discipline):
    requested_ladder = discipline

    playerLinks, countries, doubles = requestData(requested_ladder)

    ladder = getPlayerData(playerLinks, countries, doubles)

    return ladder


main(ladders['MD'])
# print(players)
# # get array of ranks
# for i in range(players.__len__()):
#     ranks.append(i)
#
#
# # clean player parameters
# for i in ranks:
#     players[i] = players[i].strip()
#
#
# # get countries
# for i in countries:
#     children.append(i.findChild('span', recursive=True).getText())
#
#
# # clean country parameters
# for i in ranks:
#     children[i] = children[i].strip()
#
# #output
# print("Rank Country Player")
#
# for i in range(9):
#     print(i+1, "  ", children[i], "   ", players[i])
#
# for i in range(9, 99):
#     print (i+1, " ",children[i], "   ", players[i])
#
# print ("100 ", children[99], "   ", players[99])