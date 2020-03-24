'''
#EXERCISE 1
num = 5

while num < 10:
    print('YEAH!')
    num += 1
'''
'''
#EXERCISE 2
answer = 5
guess = int(input("Guess the number: "))

while guess != answer:
    
    guess = int(input("Wrong guess XD, Try Again: "))

print("Nice Job")
'''

#EXERCISE 3
#Check if string is a palindrome
my_string = input("Enter a string: ")
rev_string = ''
index = len(my_string) - 1

while index >= 0:
    rev_string += my_string[index]
    index -= 1

if my_string == rev_string:
    print('Palindrome')
else:
    print('Not a palindrome')