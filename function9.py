#function9.py

# 가변 인수 함수에 대한 예제 프로그램입니다.

#두 수의 합을 구하는 함수
#세 숫자의 합을 구하는 함수
#네 숫자의 합을 구하는 함수

def sum(*args):
    # print(f'args : {args}')
    # print(f'args type : {type(args)}')
    total = 0
    for i in args:
        total += i
    return total
# 함수 호출

print(sum(1,2))
print(sum(1, 2, 3))
print(sum(1, 2, 3, 4))

