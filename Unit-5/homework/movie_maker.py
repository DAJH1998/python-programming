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
    
    def compare_to(self, other_movie): 
        common_count = 0
        for item in self.cast:
            for other_item in other_movie.cast:
                if item['name'] == other_item['name']:
                    common_count += 1
            
            if common_count > 1:
                return 1
        
        return -1

    def save_to_file(self, input_file):
        dump_dict = {}
        dump_dict['title'] = self.title
        dump_dict['genre'] = self.genre
        dump_dict['running_time'] = self.running_time
        dump_dict['cast'] = self.cast

        with open(input_file, 'w') as dump_file:
            json.dump(dump_dict, dump_file)

m = Movie('Movie', 'Horror', '3 hours')
m2 = Movie('Movie2', 'Comedy', '2 hours')

m.add_cast({
    'name': 'Jane Doe',
    'age': 31,
    'sex': 'F'
})

m.add_cast({
    'name': 'John Doe',
    'age': 35,
    'sex': 'M'
})

m2.add_cast({
    'name': 'Janey Doe',
    'age': 31,
    'sex': 'F'
})

m2.add_cast({
    'name': 'Johnny Doe',
    'age': 35,
    'sex': 'M'
})

m.describe()
m2.describe()

print(m.compare_to(m2))

m.save_to_file('movie_date.json')




