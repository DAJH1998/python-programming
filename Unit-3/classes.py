'''
#defining a class
class Person:
    def __init__(self): #constructor
        print('class instantiated')

p = Person() #creates an object

class Rectangle:
    def __init__(self, l, w):
        self.length = l #property of class
        self.width = w #property of class

    def area(self):
        return self.length * self.width

    #add method to calculate the perimeter
    def perimeter(self):
        return 2 * (self.length + self.width)

r1 = Rectangle(10, 5)

print(r1.area())
print(r1.perimeter())
'''

class Playlist:
    def __init__ (self, name):
        self.songs = []
        self.name = name
    # write the add-soung method
    def add_song (self, song):
        if type(song) is dict and 'title' in song and 'artiste' in song and 'length' in song:
            self.songs.append(song)
        else:
            print('Invalid song')
    #write get_title Method
    #assume songs are dictionaries
    def get_title (self):
        titles = []
        for song in self.songs:
            titles.append(song['title'])
        return (titles)
    #write the duration method to return the total lenth of the playlist
    def duration(self):
        total_duration = 0
        for song in self.songs:
            total_duration += song['length']
        return total_duration

p = Playlist('playlist')

p.add_song({
    'title': '10 Bandz',
    'artiste': 'Joyner Lucas',
    'length': 3.34
})

p.add_song({
    'title': '10 Bandz',
    'artiste': 'Joyner Lucas'
})


p.add_song({
    'title': '44 More',
    'artiste': 'Logic',
    'length': 3.08
})

p.add_song({
    'title': 'Lucky You',
    'artiste': 'Eminem',
    'length': 4.04
})

print(p.get_title())
print(p.duration())