num_list = []

for num in range(1500, 20001):
    if num % 7 == 0 and num % 5 == 0:
        num_list.append(num)
        
print(num_list)