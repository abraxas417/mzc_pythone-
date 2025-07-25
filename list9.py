# list9.py
#리스트 함수에 대한 예제 프로그램입니다.

lst = [1, 2, 3]

# dnjsth cnrk

lst.append(4)

print(lst)

lst.extend([5,6])

print(lst)

lst.insert(1, 'b')

print(lst) #[1, 'b',2, 3, 4, 5, 6,]

lst.pop()

print(lst)

if 'b' in lst:
    lst.remove('b')

print(lst)

lst.clear()

print(lst)