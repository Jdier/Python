
mpg = [18
,21
,20
,21
,16,
18
,18
,18
,16
,20
,19,
15
,17
,17
,15
,15
,17,
16
,14,
11
,14
,13,
12
,16
,15
,16,
15,
15
,14
,11
,11,
14
,19,
22]

num_items = 0
sum_items = 0
avg_num = 0
smallest_num = mpg[0]
largest_num = mpg[0]
for n in mpg:
    sum_items = sum_items + n
    num_items = num_items + 1

    if n < smallest_num:
        smallest_num = n
    
    if n > largest_num:
        largest_num = n

avg_num = sum_items / num_items

print("The number of items: ", num_items)
print("The sum of the items: ", sum_items)
print("The average of the items: ", avg_num)
print("The smallest number :", smallest_num)
print("The largest number :", largest_num)

employees = {123: 'Bob', 124: 'Susan', 128: 'Abby', 125: 'Henry', 126: 'Edward', 127: 'James'}

emp_numbers = []
emp_names = []

for key, value in employees.items():
    emp_numbers.append(key)
    emp_names.append(value)

print("List of employee numbers: ", emp_numbers)
print("List of employee names: ", emp_names)
