import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import time


token = spotipy.util.prompt_for_user_token(
    username="user", #* Troque aki usarname
    scope="ugc-image-upload, playlist-modify-private, playlist-read-private, user-read-private, user-read-playback-state, user-library-modify, user-read-playback-position, app-remote-control, user-read-recently-played, user-modify-playback-state, user-read-email, user-follow-modify, playlist-modify-public, user-follow-read, user-read-currently-playing, playlist-read-collaborative, user-library-read, streaming, user-top-read,", #tipo da permissão
    client_id="xxx", 
    client_secret="xxx", 
    redirect_uri="http://localhost:8800")

sp = spotipy.Spotify(auth = token)



def deviceMc(): # *coleta todos dispositivo no momento
    dev = sp.devices()
    with open( 'return/Dispositivos.json', 'w') as json_file:
         json.dump(dev, json_file, indent=4)

    return "Spotify Ok 01"


def pauseMc(): # *Pausa Musica do momento
    inf = sp.currently_playing()
    if(inf['is_playing'] == True):
        sp.pause_playback()

    return "Spotify Ok 02"


def startMc():# *inicia a musica musica
    inf = sp.currently_playing()
    if(inf['is_playing'] == False):
        sp.start_playback()

    return "Spotify Ok 03"
    

def statusMc(): #*Status do Momento Atual
    inf = sp.currently_playing()
    with open( 'return/Status.json', 'w') as json_file:
        json.dump(inf, json_file, indent=4)

    return "Spotify Ok 04"


def skipNextMc(): #*pula proxima musica
    sp.next_track()

    return "Spotify Ok 05"


def skipUndoMc(): #*volta Musica
    sp.previous_track()

    return "Spotify Ok 06"


def repetMc(state): #*Define repetição para track = reptir playlist, context = reptir musica, ou off desliga repitiçao
    sp.repeat(state)

    return "Spotify Ok 06"


def shearchMc(tipe,Psq,limit):#* pesquisa usando tipo se e artist , album, ou track depois o nome e limite de pesquisa max = 10
    pesq = sp.search(Psq, limit=limit, offset=0, type=tipe, market=None)
    
    with open( 'return/Pesquisa.json', 'w') as json_file:
        json.dump(pesq, json_file, indent=4)
    return "Spotify Ok 07"


def volumeMc(vol): #*define volume para porcentagem desejada
    sp.volume(vol)

    return "Spotify Ok 08"


def volumeUpMc(): #* almenta volume em 10%
    dev = sp.devices()
        
    for device in dev["devices"]:
        if(device["is_active"]):
            name = device["name"]
            idMc = device["id"]
            volumeMc = device["volume_percent"]
    if (volumeMc < 90):
        volumeMc = volumeMc + 10
        sp.volume(volumeMc)
    else:
        return "Vol Max"

    return "Spotify Ok 09"


def volumeDowMc(): #* diminui volume em 10%
    dev = sp.devices()
        
    for device in dev["devices"]:
        if(device["is_active"]):
            name = device["name"]
            idMc = device["id"]
            volumeMc = device["volume_percent"]
    if (volumeMc > 10):
        volumeMc = volumeMc - 10
        sp.volume(volumeMc)
    else:
        return "Vol Min"

    return "Spotify Ok 09"


def DeviceMudMc(id): #* muda dispositivo de reproduçao pre setado
    if(id == 1):
        idMc = "ba144984976c5ce6794afc4ece5c588c78782cd2"#*laptop
    elif(id == 2):
        idMc = "7e2b5ec3b2402d12208f5fcee8e55d4f01c299d9"#*Motog5

    else:
        return "Dispositivo não encontrado"

    sp.transfer_playback(idMc,True)

    return "Spotify Ok 10"


def userMc(): #* informaçoes de usuario
    usr = sp.user("lje4xcplk8eowol9u1n0gmiqo")

    with open( 'return/user.json', 'w') as json_file:
        json.dump(usr, json_file, indent=4)

    return "Spotify Ok 11 "


def shuffleMc(State): #* liga desliga reprodução aleatoria
    sp.shuffle(State)

    return "Spotify Ok 12"


def startMusicMc(idMc,toc):#* toca Algo especificado
    sp.start_playback(device_id=idMc, context_uri=toc, position_ms=0)

    return "Spotify Ok 13"


def ShearPlayMc(Psq): #* pesquisa e iniciar musica pesquisada

    shearchMc("album", Psq, 1)
    with open('return/Pesquisa.json') as f:
        data = json.load(f)

    track = data["albums"]
    item = track["items"]
    items = track["items"][0]
    uri = items["uri"]
    
    dev = sp.devices()

    for device in dev["devices"]:
        if(device["is_active"]):
            name = device["name"]
            idMc = device["id"]
            volumeMc = device["volume_percent"]
    
    print(idMc)
    sp.start_playback(

        device_id=idMc,
        context_uri=uri, 
        position_ms=0)

    return "Spotify Ok 14"


def startPlayPlaylistMc(playlist): #* inicia playlist com id
    dev = sp.devices()

    for device in dev["devices"]:
        if(device["is_active"]):
            name = device["name"]
            idMc = device["id"]
            volumeMc = device["volume_percent"]
    
    sp.start_playback(

        device_id=idMc,
        context_uri=playlist,
        position_ms=0)
    return "Spotify Ok 15"


def albumListMc(): #* listas os albums retorna albums.json
    
    alb = sp.current_user_saved_albums(limit=50, offset=0)

    with open( 'return/Albuns.json', 'w') as json_file:
        json.dump(alb, json_file, indent=4)
        json_file.close()

    with open('return/Albuns.json') as f:
        albums = json.load(f)
        json_file.close()
    with open('return/Albums.json') as f:
        albus = json.load(f)
        json_file.close()

    albb = 0
 
    
    for device in albums["items"]:
        albb = albb + 1
        dataMc = device["added_at"]
        albu = device["album"]
        nameMc = albu["name"]
        musicsMc = albu["total_tracks"]
        uriMc = albu["uri"]

        result = {
            "name": nameMc,
            "date": dataMc,
            "music": musicsMc,
            "uri": uriMc,
        }

        albus[f"album{albb}"] = result
        
    with open( 'return/Albums.json', 'w') as json_file:
        json.dump(albus, json_file, indent=4)
        json_file.close()
    return "Spotify Ok 16"


def libraryMc(): #* pega todas playlist e retorna json
    library = sp.user_playlists("lje4xcplk8eowol9u1n0gmiqo", limit=50, offset=0)

    with open('return/librarys.json', 'w') as json_file:
            json.dump(library, json_file, indent=4)
            json_file.close()

    with open('return/librarys.json') as f:
        playlist = json.load(f)

    with open('return/playlists.json') as f:
        playlists = json.load(f)
        f.close()

    i = 0
    for play in playlist["items"]:

        uriMc = play["uri"]
        nameMc = play["name"]
        type = play["type"]
        publicMc = play["public"]
        collaborativeMc = play["collaborative"]
        ownerPl = play["owner"]
        namePl = ownerPl["display_name"]

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

    with open('return/playlists.json', 'w') as json_file:
        json.dump(playlists, json_file, indent=4)
        json_file.close()

    return "Spotify Ok 17"


def HistoryMc(): #* retona json com as ultima 50 musicas tocadas
    history = sp.current_user_recently_played(limit=50, after=None, before=None)

    with open('return/history.json', 'w') as json_file:
        json.dump(history, json_file, indent=4)
        json_file.close()

    with open('return/history.json') as f:
        histori = json.load(f)

    with open('return/historic.json') as f:
        historic = json.load(f)
        f.close()
    with open('return/historic.json', 'w') as json_file:
        json.dump(historic, json_file, indent=4)
        json_file.close()

    i = 0
    for histo in histori["items"]:

        track = histo["track"]
        nameMc = track["name"]
        uriMc = track["uri"]
        dateMc = histo["played_at"]
        album = track["album"]
        albumMc = album["name"]
        context = histo["context"]
        playlistMc = context["uri"]
        artist = track["artists"][0]
        artistMc = artist["name"]

        result = {
            "Nome": nameMc,
            "Uri": uriMc,
            "Data": dateMc,
            "Artista": artistMc,
            "Album": albumMc,
            "Playlist": playlistMc,
        }

        historic[f"PlayList{i}"] = result
        i = i + 1

    with open('return/historic.json', 'w') as json_file:
        json.dump(historic, json_file, indent=4)
        json_file.close()

    return "Spotify Ok 18"


def volumeMuteMc():  # * desliga som
    dev = sp.devices()

    for device in dev["devices"]:
        if(device["is_active"]):
            name = device["name"]
            idMc = device["id"]
            volumeMc = device["volume_percent"]


    vol = {
            "volumeDevice":volumeMc
    }
    with open('return/volume.json', 'w') as json_file:
        json.dump(vol, json_file, indent=4)
        json_file.close()

    sp.volume(0)
    return "Spotify Ok 19"

def volumeUnMuteMc(): #* volta som normal
    with open('return/volume.json') as f:
        vol = json.load(f)
    volume = vol["volumeDevice"]
    sp.volume(volume)
    return "Spotify Ok 20"


#*  deixe estas funçao elas sao esenciais 
devic = deviceMc()
stats = statusMc()
print(devic)
print(stats)
#-----------------------------------------------------------------------------------------------------------------------
#* chamar as funçao aki 
#* como exemplo:
#* Variavel = Função()
#* print(Variavel)
#-----------------------------------------------------------------------------------------------------------------------







#*lixos  que nao quero apagar


# with open( 'Dispositivos.json', 'w') as json_file:
#     json.dump(dev, json_file, indent=4)
# with open('Dispositivos.json') as f:    
#     is_playing = json.load(f)
# print("")
# print (is_playing['is_playing'])
    # sp.start_playback()
    # sp.pause_playback()
