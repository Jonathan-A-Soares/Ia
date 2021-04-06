from epicstore_api import EpicGamesStoreAPI
from datetime import datetime
import json


api = EpicGamesStoreAPI()

def freegameListEpic(): #* cria lista de jogos gratis da epicGames no momento
    free_games = api.get_free_games()['data']['Catalog']['searchStore']['elements']

    with open( 'return/FreeGames.json', 'w') as json_file:
        json.dump(free_games, json_file, indent=4)



    with open('return/FreeGames.json') as f:
        free = json.load(f)


    with open('return/FreeGame.json') as f:
        fre = json.load(f)


    o = 0
    i = 0

    for Game in free:
        o = o + 1
        freegame = Game["title"]
        print(f"{o} Name: {freegame}")

        result = {
            "Title": freegame
        }

        fre[f"Game{o}"] = result

    

    for Game in free:

        while i < 1:
            i = i + 1
            freegame = Game["title"]
            promo = Game["promotions"]
            promotion = promo["promotionalOffers"]
            promot = promotion[0]
            prom = promot["promotionalOffers"]
            pro = prom[0]
            start = pro["startDate"]
            end = pro["endDate"]

            print(f"FreeMoment: {freegame}\nFinaliza:{end}\n")
            
            result = {
                "Title": freegame,
                "endDate":end
            }

        fre[f"AtualFeeGame"] = result

    with open('return/FreeGame.json', 'w') as json_file:
        json.dump(fre, json_file, indent=4)
        json_file.close()


    return "Epic Ok 01"


def Link(lik): #* responsavel pela geração de link
    epic = "https://www.epicgames.com/store/pt-BR/p/"
    url = epic + lik
    print("Epic Ok 02")
    return url


def VeriGameEpic(title): #* verifica se tem jogo no catalogo da epicGames
    games = api.fetch_store_games(
        product_type='games/edition/base|bundles/games|editors',
        count=5,
        sort_by='releaseDate',
        sort_dir='DESC',
        release_date="startDate",
        with_price=True,
        keywords=title,
    )

    with open('return/StoreGame.json', 'w') as json_file:
        json.dump(games, json_file, indent=4)
        json_file.close()

    data = games["data"]
    catalogo = data["Catalog"]
    store = catalogo["searchStore"]
    pagin = store["paging"]
    total = pagin["total"]



    if total >= 1 :

        element = store["elements"][0]
        Title = element["title"]
        descrition = element["description"]
        lin = element["productSlug"]
        productSlug = Link(lin)

        result = {
             "Title": Title,
             "link": productSlug,
             "description": descrition


        }

    else:
         result = {
             "Title": False
        }
         return "Epic Ok False 02"
    with open('return/StoreItem.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)
        json_file.close()
        
    return "Epic Ok True 03"


ep = freegameListEpic()
print(ep)




