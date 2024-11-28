import requests
from config import token_bs

auth = {'Authorization': f'Bearer {token_bs}'}

url = 'https://api.brawlstars.com/v1/players/%23prgg89jl'


def trophies():
    response = requests.get(url, headers=auth).json()
    return response.get('trophies')


def victories():
    response = requests.get(url, headers=auth).json()
    return response.get('soloVictories'), response.get('duoVictories'), response.get('3vs3Victories')


def sum_victories():
    response = requests.get(url, headers=auth).json()
    return response.get('soloVictories') + response.get('duoVictories') + response.get('3vs3Victories')


def nickname():
    response = requests.get(url, headers=auth).json()
    return response.get('name')
