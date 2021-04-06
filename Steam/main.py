import requests
import json

Key = "4358E2CD15E421362AFA953DE781B720"
luck = "76561198355142462"
bruxo = "76561198826208472"
julio = "76561198401865562"

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
    

