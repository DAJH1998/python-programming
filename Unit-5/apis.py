import requests

url = "https://deezerdevs-deezer.p.rapidapi.com/search"
album_url = "https://deezerdevs-deezer.p.rapidapi.com/album/"

querystring_eminem = {"q":"eminem"}
querystring_ed = {"q":"ed sheeran"}
querystring_cardi = {"q":"cardi B"}

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "2ab7c9815dmshc54ce3e5affb5a7p117757jsn67407177f01b"
    }

response_eminem = requests.request("GET", url, headers=headers, params=querystring_eminem).json()
response_ed = requests.request("GET", url, headers=headers, params=querystring_ed).json()
response_cardi = requests.request("GET", url, headers=headers, params=querystring_cardi).json()

em = response_eminem["data"]
ed = response_ed["data"]
cardi = response_cardi["data"]

def track_count(artist):
    count = 0
    for track in artist:
        count += 1

    return print(f'Amount of tracks: {count}')

def album_count(artist):
    albums = []
    for item in artist:
        albums.append(item["album"]["title"])
    
    return len(set(albums))

def explicit(artist):
    explicit_count = 0
    for song in artist:
        if song["explicit_lyrics"] == True:
            explicit_count += 1

    return print(f'Explicit songs: {explicit_count}')

def album_data (artist):
    album_id = []
    
    for item in artist:
        album_id.append(item["album"]["id"])
    set(album_id)
    for item in album_id:
        album_url = album_id + item
        album_data = requests.request("GET", album_url, headers=headers).json()

    return album_data

track_count(em)
track_count(ed)
track_count(cardi)

print(album_count(em))
print(album_count(ed))
print(album_count(cardi))

explicit(em)
explicit(ed)
explicit(cardi)

print(album_data(em))
