import json

with open('return/FreeGames.json') as f:
    free = json.load(f)

o = 0
i = 0
for Game in free:
    o = o + 1
    freegame = Game["title"]
    print(f"{o} Name: {freegame}")

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

