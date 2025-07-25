# list3.py
# list에 대한 예제 프로그램입니다.


colors = ['red', 'green', 'blue', 'pink', 'purple']

# index

for i in range(len(colors)):
    print(f'index : {i}')


print(colors[0])
print(colors[4])


# 리스트 생성

lst = [1, 2, 3]

lst[-3] = 'b'
lst[-1] = lst[1]*2
lst[-2] = lst[0] * lst[2]

print(lst)