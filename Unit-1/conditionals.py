'''
#EXERCISE 1
#truthy vs falsey
if -1:
    print('This is true')
else:
    print('This is not true')
'''
'''
#EXERCISE 2
temperature_readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 13]
count = 0
total = 0
pos_avg = 0

#count the number of negative readings
for temp in temperature_readings:
    if temp < 0:
        count += 1
        
print(count)

#find the average of positive readings
for temp in temperature_readings:
    if temp > 0:
        total += temp
        count += 1
        
pos_avg = total / count
print(pos_avg)
'''

#EXERCISE 3
titles = ['The Avengers', 'Avengers Age of Ultron', 'Captain America: The First Avenger']
count = 0

#count how many titles have 'The' in it
for title in titles:
    if 'The' in title:
        count += 1
        
print(f'List has {count} with title "The"')

#how many vowels are in a string
string = 'There is a long string that has only a few vowels'
count = 0

#a,e,i,o,u
for char in string:
    if char in 'aeiou': 
        count += 1

print(f'Number of vowels in the string is {count}')
        
        