import json

with open('librarys.json') as f:
    playlist = json.load(f)

with open('playlists.json') as f:
    playlists = json.load(f)
    f.close()
  
i= 0
for play in playlist["items"]:
    
    uriMc = play["uri"]
    nameMc = play["name"]
    type = play["type"]
    publicMc = play["public"]
    collaborativeMc = play["collaborative"]
    ownerPl = play["owner"]
    namePl = ownerPl["display_name"]

    print(
        f" Nome:{nameMc}\n Uri:{uriMc}\n tipo:{type}\n Publica:{publicMc}\n coloborativa:{collaborativeMc}\n Dono:{namePl}"
        )
    print("")

    result = {
        "Nome": nameMc,
        "Uri": uriMc,
        "tipo": type,
        "Publica": publicMc,
        "coloborativa": collaborativeMc,
        "Dono": namePl,
    }

    playlists[f"PlayList{i}"] = result
    i = i + 1

with open('playlists.json', 'w') as json_file:
    json.dump(playlists, json_file, indent=4)
    json_file.close()

