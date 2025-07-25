#function12.py
# 인덱스에 대한 예제 프로그램입니다.

#함수정의

def print_all(a, b, c):
    print(f'a ={a}, b= {b}, c = {c}')



_list = [1, 2, 3]

print_all(*_list) # print(1, 2, 3)  : 언패킹
