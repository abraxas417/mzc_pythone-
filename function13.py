#function13.py
# 인덱스에 대한 예제 프로그램입니다.

#함수정의

def print_all(*args):
    print(args)



_list = [1, 2, 3]

print_all(*_list) # print(1, 2, 3)  : 언패킹

_list = [1, 2, 3, 4]

print_all(*_list)