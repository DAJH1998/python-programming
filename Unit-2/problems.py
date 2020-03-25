#given a string, replace every letter with its position in the alphabet
text = input('Enter a string: ')
dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
new_text = text.lower()

for i in new_text:
    if i in dict:
        new_text = new_text.replace(i, dict[i]) + " "

print(new_text) #can't print it with spaces in between the output

#given a list of numbers, find the largest number in the list
number_list = [55, 24, 469, 421, 99, 1, 24]
max = 0

for num in number_list:
    if num > max:
        max = num

print(f'Largest number in list: {max}')

#given a string of words, determine the length of the shortest word
word_list = ['potato', 'path', 'python', 'car']
result = min(len(word) for word in word_list)

print(f'Shortest word in the list: {result}')