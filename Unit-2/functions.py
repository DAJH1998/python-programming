'''
#EXERCISE 1
def add_two():
    result = 5 + 5
    print(result)

add_two()

#passing arguments
def add_two(a, b):
    result = a + b
    print(result)

add_two(10, -4)

#returning a value
def add_two(a, b):
    result = a + b
    return result

print(add_two(3, 10))
'''
'''
#EXERCISE 2
#write a function that returns the sum of the integers in a list
def sum_list(a_list):
    total = 0
    for num in a_list:
        total += num
    return total

#num_list = [23, 4, 5, 12]
print(sum_list([23, 4, 5, 12])) #44
'''
'''
#EXERCISE 3
#write a function that reverses a string
def rev_string(my_string):
    string = ''
    for i in my_string:
        string = i + string
    return string

print(rev_string('nohtyp'))
'''

#EXERCISE 3
#write a function that finds the intersection of two lists
def intersect_list(list_1, list_2):
    result = []
    for item in list_1:
        if item in list_2:
            result.append(item)

    return result

print(intersect_list([1, 2, 3, 4], [5, 4, 3, 2]))
        
