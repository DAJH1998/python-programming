'''
#EXERCISE 1
#my version
grades = 25

if grades <= 100 and grades >= 80:
    print('A')
elif grades <= 79 and grades >= 60:
    print('B')
elif grades <= 59 and grades >= 50:
    print('C')
else:
    print('D')
'''
'''
#teacher's version
score = 67

if score >= 80:
    grade = 'A'
elif score >= 60:
    grade = 'B'
elif score >= 50:
    grade = 'C'
else: 
    grade = 'D'

print(grade)
'''
'''
#EXERCISE 2
#fizzbuzz
#for the first 50 integers
for num in range(1, 51):
#if the number is divisible by 15, print fizzbuzz
    if num % 15 == 0:
        print('fizzbuzz')
#if the number is divisible by 3, print fizz        
    elif num % 3 == 0:
        print('fizz')
#if the humber is divisible by 5, print buzz
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)
'''

#EXERCISE 3
#find the sum of even numbers between 1 and 10
total = 0
for num in range(1, 11):
    if num % 2 == 0:
        total += num #calculating a running sum
    
    print(total)
