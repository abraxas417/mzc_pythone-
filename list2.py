# list2.py

#list에 대한 예제 프로그램입니다.

_list = []

print(_list)
print(type(_list))
print(len(_list))

list1 = [1, 2, 3, 4, 5]
print(_list)

#for문을 사용하여 리스트 요소를 출력하세요.

for i in list1:
    print(f'{i}', end='')

print()
print('=' * 50)

list2 = list([1, 2, 3, 4, 5])
print(list2)
print(type(list2)) 


list3 = (1, '홍길동', 100,  100 , 100)

for i in list3:
    print(i, end = '\t')