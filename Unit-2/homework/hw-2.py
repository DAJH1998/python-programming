worker_type = input('Enter worker type: ')
hours_worked = int(input('Enter hours worked: '))
weekly_wage = 0

if worker_type == 'full_time':
    if hours_worked <= 40:
        weekly_wage = hours_worked * 50
    elif hours_worked > 40:
        weekly_wage = hours_worked * 70
elif worker_type == 'part_time':
    if hours_worked <= 20:
        weekly_wage = hours_worked * 65
    elif hours_worked > 20:
        weekly_wage = hours_worked * 70
elif worker_type == 'contract':
    weekly_wage = hours_worked * 120
    weekly_wage = weekly_wage - (weekly_wage / 4) 

print(f'Weekly wage is ${weekly_wage}')



