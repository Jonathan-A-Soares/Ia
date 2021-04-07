import requests
import json

Key = "xx"


def librarySteam(key,Sid):
    r = requests.get(
        f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&steamid={Sid}&format=json&include_appinfo=True')
    with open('return/LibraryGames.json', 'w') as json_file:
        json.dump(r.json(), json_file, indent=4)
    return "Steam Ok 01"


def gamesRecentSteam(key, Sid, cout):
    r = requests.get(
        f'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1?key={key}&steamid={Sid}&format=json&&cout={cout}&include_appinfo=True')
    with open('return/GamesRecent.json', 'w') as json_file:
        json.dump(r.json(), json_file, indent=4)

    return "Steam Ok 02"
    

