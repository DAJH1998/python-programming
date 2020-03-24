odd_strings = ['abba', '111', 'canal', 'level', 'abc', 'racecar',
'123451' , '0.0', 'papa', '-pq-']
count = 0

for word in odd_strings:
    if len(word) > 3 and word[0] == word[len(word) - 1]:
        count += 1
        print(word)

print(count)
        