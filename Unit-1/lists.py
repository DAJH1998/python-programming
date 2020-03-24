'''
#EXERCISE 1
numbers = [8, 5, 17]

#insert number -5 at the front of the list
numbers.insert(0, -5)
print(numbers)

#find the numbers of elements in the list
print(len(numbers))

#remove the last element in the lis
last_el = numbers.pop()
print(last_el) 
print(numbers)

#print the second element in the list
print(numbers[1])
'''
'''
#EXERCISE 2
grades = [70, 85, 91, 23, 60, 45, 90, 56, 77, 88]

#add 5 to each grade in the list
#we have to access each element(position) in the list, change the element
#we need access to the index
for grade in range(len(grades)):
    grades[grade] += 5

print(grades)
'''

#EXERCISE 3
#make each word past tense in this list

verbs = ['like', 'hate', 'fake', 'rake']

for verb in range(len(verbs)):
    verbs[verb] += 'd'

print(verbs)

