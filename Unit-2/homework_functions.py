#Problem 1
def letter_count(my_string, letter):
    count = 0
    for i in my_string:
        if i == letter:
            count = count + 1 
    print(count)
    return count

#Problem 2
def count_words(my_string):
    res = len(my_string.split())
    print(res)
    return res

#Problem 3
def reverse_list(string_list):
    string_list.reverse()
    print(string_list)
    return string_list

#Problem 4
def split_list(num_list, val):
    count = 0
    list1 = []
    list2 = []
    for value in num_list:
        if value > val:
            count += 1
            list2.append(value)
        elif value < val:
            count += 1
            list1.append(value)
    print(f'{list1}, {list2}')
    return val
    

print('Problem 1 results:')
letter_count('abcde', 'a') #should return 1
letter_count('this is going to be easy', 'i') #should return 3
letter_count('how about that?', 'z') #should return 0

print('Problem 2 results:')
count_words('hey there!!') #should return 2
count_words('I\'m staying home because of the epidemic') # shoud return 7
count_words('how-about-a-hypenated-string?') #shoud return 1

print('Problem 3 results:')
reverse_list([]) # should return []
reverse_list([1, 2, 3]) # should return [3, 2, 1]
reverse_list(['this', 'is', 'cool!']) #should return ['cool!', 'is' , 'this']

print('Problem 4 results:')
split_list([1, 2, 3], 0) # should return [[], [1, 2, 3]]
split_list([4, 5, 11, 8, 19], 10) #should return [[4, 5, 8], [11, 19]]
split_list([5, 6, 20, -4, -12, 0], -1) # should return [[-4, -12], [5, 6, 20, 0]]

