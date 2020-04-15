'''
nums = [1, 2, 3, 4, 5, 7, 11, -15, 28]
#create a list of only even numbers in nums
even_num = []

for num in nums:
    if num % 2 == 0:
        even_num.append(num)

print(even_num)
'''
'''
#use list comprehension
even_num = [num for num in nums if num % 2 == 0]

print(even_num)
'''
'''
vals = [2, 4, 6, 8]

vals_square = [val * val for val in vals]

print(vals_square)
'''
'''
#create e new list of words longer than 4 characters & print in capital letters
words = ['run', 'cat', 'hassle', 'print', 'class', 'python']

word_list = [word.upper() for word in words if len(word) > 4]

print(word_list)
'''
'''
#dictionary comprehension
person = {'name': 'Alice', 'Address': 'Toronto', 'Occupation': 'Engineer'}

new_person = {key:val for key, val in person.items()}

print(new_person)
'''
'''
#create a new dictionary with colors whose value are either warm or lively
colors = {'red': 'Bold', 'green': 'Lively', 'blue': 'Calm', 'yellow': 'Warm'}

new_colors = {key:val for key, val in colors.items() if val == 'Warm' or val == 'Lively'}

print(new_colors)
'''

#create a dictionary with the count of each letter in a string
word = "Apple"

dict_word = {letter : word.count(letter) for letter in word}

print(dict_word)
