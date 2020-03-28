def letter_count(my_string, letter):
    count = 0
    for i in my_string:
        if i == letter:
            count = count + 1 

    return count

print(letter_count('abcde', 'a'))