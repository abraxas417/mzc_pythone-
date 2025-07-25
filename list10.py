# list10.py
#리스트함수에 대한 예제 프로그램입니다.

colors = ['yellow', 'green', 'blue', 'yellow']

print(colors.index('yellow'))

print(colors.index('yellow', 1))

#print(colors.index('red'))


num_list = [1, 3, 2]

num_list.reverse()

print(num_list)

# 오름차순 정렬

num_list.sort()

print(num_list)

#내림차순 정렬

num_list.sort(reverse=True)

print(num_list)