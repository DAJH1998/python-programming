'''
#EXERCISE 1
#function takes any number of parameters
#add any number of numbers
def multiply(*args):
    product = 1
    for num in args:
        product *= num

    return product

print(multiply(1))
print(multiply(1, 10))
print(multiply(5, -3, 7))
print(multiply(1, 2, 3 ,4, 5, 6, 7, 8, 9, 10))
'''

#EXERCISE 2
#keyword arguments
def message(name, ms = 'Hello'):
    print(ms + ' ' + name)

message('Donyell')