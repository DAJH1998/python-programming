import json

class Movie:
    def __init__(self, title, genre, running_time):
        self.cast = []
        self.title = title
        self.genre = genre
        self.running_time = running_time

    def add_cast(self, casts):
        if type(casts) is dict and 'name' in casts and 'age' in casts and 'sex' in casts:
            self.cast.append(casts)
        else:
            print('Invalid input')

    def describe(self):
        print(self.cast)
    
    def compare_to(self,comparison): 
        return

    def save_to_file(self, inputfile):
        return

m = Movie('Movie', 'Horror', '3 hours')

m.add_cast({
    'name': 'Jane Doe',
    'age': 31,
    'sex': 'F'
})

m.add_cast({
    'name': 'John Doe',
    'age': 35,
})

m.describe()




