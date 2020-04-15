#read a file
text_file = open('lines.txt', 'r') #'r' for reading

lines = text_file.read()
text_file.close()

print(lines)

#write a file
text_file = open('lines.txt', 'w') #'w' for overwriting, 'a' for appending

text_file.write('\nHere is my fourth line')
text_file.close()