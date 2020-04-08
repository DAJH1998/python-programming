def dict_merge(dict1, dict2):
    dict3 = {}
    for key in dict1:
        if key in dict2:
            dict3[key] = [dict1[key], dict2[key]]
        else:
            dict3[key] = dict1[key]
            
    for key in dict2:
        if key in dict1:
            dict3[key] = [dict2[key], dict1[key]]
        else:
            dict3[key] = dict2[key]
    
    print(dict3)

    return

def list_to_dict(pairs):
    d = {}
    for k, v in pairs:
        d[k] = v        
    print(d)
    
    return d

def reverse_dict(dict1):
    new_dict = {}
    for key, count in dict1.items():
        if count in new_dict:
            new_dict[count].append(key)
        else:
            new_dict[count] = key

    print(new_dict)

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