#if3.py

# x , y , max_value  = 10 , 5, 0

# if x > y:
#     max_value = x
# else:
#     max_value = y

# print(f'max_value : {max_value}')

x,y = 10, 9

max_value = (x if x > y else y)

print(f'max_value : {max_value}')
