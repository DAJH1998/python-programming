import json

playlist = [
    {
        'title': 'Bodak Yellow',
        'genre': 'Pop',
        'artiste': 'Cardi B',
        'year': '2017',
        'length': 3.25
    },
    {
        'title': 'Gas Pedal',
        'genre': 'Hip-Hop',
        'artiste': 'Sage The Gemini',
        'year': '2012',
        'length': 3.28
    },
    {
        'title': 'Homicide',
        'genre': 'Rap',
        'artiste': 'Logic',
        'year': '2019',
        'length': 4.05
    },
    {
        'title': 'Donald Trump',
        'genre': 'Rap',
        'artiste': 'Mac Miller',
        'year': '2011',
        'length': 2.44
    },
    {
        'title': 'All Mine',
        'genre': 'Rap',
        'artiste': 'Kanye West',
        'year': '2018',
        'length': 2.25
    },
    {
        'title': '44 More',
        'genre': 'Rap',
        'artiste': 'Logic',
        'year': '2018',
        'length': 3.08
    },
    {
        'title': '10 Bandz',
        'genre': 'Rap',
        'artiste': 'Joyner Lucas',
        'year': '2020',
        'length': 3.34
    },
    {
        'title': 'Lucky You',
        'genre': 'Hip-Hop',
        'artiste': 'Eminem',
        'year': '2018',
        'length': 4.04
    },
    {
        'title': 'Wet Dreamz',
        'genre': 'Hip-Hop',
        'artiste': 'J. Cole',
        'year': '2014',
        'length': 3.59
    },
    {
        'title': 'West Coast',
        'genre': 'Hip-Hop',
        'artiste': 'G-Eazy',
        'year': '2019',
        'length': 3.25
    },
]

answer = input('Menu option: ')

while answer == '1' or answer == '2' or answer == '3':
    if answer == '1':
        print('1. Titles: ')
        for title in playlist:
            print(title['title'])
        break
    elif answer == '2':
        print('\n2. Artistes:')
        for artist in playlist:
            print(artist['artiste'])
        break
    elif answer == '3':
        total_length = 0
        for item in playlist:
            total_length += item['length']
        print(f'Playlist length: {total_length}')
        break
    



    