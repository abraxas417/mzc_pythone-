#operator4.py

#동등 연산자에 대한 예제 프로그램입니다.

result = None

print(f'result : {result}')
print(f'result : 자료형 : {type(result)}')

flag = result is None
print(f'flag : {flag}')

flag = result is not None
print(f'flag : {flag}')

result = 'python'

flag = result == 'python'
print(f'flag : {flag}')

flag = result =='Python'
print(f'flag : {flag}')