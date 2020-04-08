def dict_merge(dict1, dict2):
    dict3 = {}
    for key in dict1:
        if key in dict2:
            dict3[key] = [dict1[key], dict2[key]]
        else:
            dict3[key] = dict1[key]
            
    for key in dict2:
        if key not in dict3:
            dict3[key] = dict2[key]
    
    print(dict3)

    return

def list_to_dict(pairs):
    d = {}
    for k, v in pairs:
        d[k] = v        
    
    print(d)
    
    return d

'''
def reverse_dict(dict1):
    new_dict = {}
    for key, count in dict1.items():
        if count in new_dict:
            new_dict[count].append(key)
        else:
            new_dict[count] = key

    print(new_dict)
'''

def reverse_dict(input_dict):
    new_dict = {}
    for key in input_dict:
        if type(input_dict[key]) is list or type(input_dict[key]) is dict: #keyword "type" is to see the type of the input
            new_dict[tuple(input_dict[key])] = key #
        else:
            new_dict[input_dict[key]] = key

    print(new_dict)
    
    return 

def letter_count(word):
    count = {}
    for l in word:
        count[l] = count.get(l, 0) + 1 #.get is a dictionary function, retreive a value given a specific key 
    
    return count

def possible_words(word_list, char_list):
    #which words in word_list can be formed from the 
    #charaters in char_list
    valid_words = []
    #iterate over word_list
    for word in word_list:
        is_word_valid = True
        #get a count of each character in word
        char_count = letter_count(word)
        #check each character in the word
        for letter in word:
            if letter not in char_list:
                is_word_valid = False
            else:
                if char_list.count(letter) != char_count[letter]:
                    is_word_valid = False
        #add valid word to a list
        if is_word_valid:
            valid_words.append(word)
    
    print(valid_words)

    return valid_words

legal_words = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
letters = ['e', 'o', 'b', 'a', 'm', 'g', 'l']

print('Problem 1')
dict_merge({'a': 1, 'b': 2}, {'c': 3, 'd': 4})
# should return {'a':1 , 'b': 2, 'c': 3, 'd': 4}
dict_merge({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
# should return {'a': 1, 'b': [2, 3], 'c': 4}
dict_merge({'x': 'one', 'y': 'two'}, {'x': 1.5, 'y': 3.7})
#should return {'x': ['one', 1.5], 'y': ['two', 3.7]}

print('\nProblem 2')
list_to_dict([['name', 'Alice'], ['job', 'Engineer'], ['city', 'Toronto']])
#should return {'name': 'Alice', 'job':'Engineer', 'city':'Toronto'}

print('\nProblem 3')
reverse_dict({'name': 'Alicia', 'job':'Engineer', 'city': 'Toronto'})
#should return {'Alicia': 'name', 'Engineer': 'job', 'Toronto':'city'}

print('\nProblem 5')
possible_words(legal_words, letters) # should return ['go', 'me', goal']