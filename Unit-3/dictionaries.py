import json
'''
#EXERCISE 1
cars = [
    {
        'make': 'Toyota',
        'model': 'Camry',
        'year': '2017',
        'color': 'black'
    },
    {
        'make': 'Toyota',
        'model': 'Prius',
        'year': '205',
        'color': 'white'
    },
    {
        'make': 'Mercedes Benz',
        'model': 'A 250',
        'year': '2019',
        'color': 'grey'
    },
    {
        'make': 'Hyundai',
        'model': 'Elantra',
        'year': '2007',
        'color': 'grey'
    },
    {
        'make': 'Lexus',
        'model': 'IS 300',
        'year': '2020',
        'color': 'blue'
    },
]
'''
'''
#my version
price = ['100', '200', '300', '400', '500']
i = 0
for car in cars:
    car['price'] = price[i]
    i += 1

print(json.dumps(cars, indent = 2))
'''
'''
#teacher's version
price = ['100', '200', '300', '400', '500']

for index, car in enumerate(cars): #returns a pair of index and item in the list
    car['price'] = price[index]

print(json.dumps(cars, indent = 2))
'''
'''
#EXERCISE 2
state_capitals = {
    
    "Alaska" : "Juneau",
    "Colorado" : "Denver",
    "Oregon" : "Salem",
    "Texas" : "Austin"

}

def reverse_lookup(my_dictionary, value):
    #return the key that matches the value
    #if no match, return: "No match for that value"
    for key in my_dictionary:
        if value == my_dictionary[key]:
            return key

    print('No match for that value')
    
    return

print(reverse_lookup(state_capitals, "Denver"))
'''
#EXERCISE 3
#write a function called frequency_counter, accepts a string
#returns a dictionary with each word, and the number of times each word
#occurs in a string

def frequency_counter(sentence):
    my_dictionary = {}
    my_sentence = sentence.split()

    for word in my_sentence:
        if word in my_dictionary:
            my_dictionary[word] += 1
        else: 
            my_dictionary[word] = 1
    
    return my_dictionary

print(json.dumps(frequency_counter('here is my sentence'), indent = 2))
print(json.dumps(frequency_counter('potato is a potato inside a potato'), indent = 2))
