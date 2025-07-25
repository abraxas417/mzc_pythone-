#input2.py

a,b = list(map(int,input("두 개의 정수를 입력하세요(공백) ").split(','))) # {1,5} : unpaking
print(f'a : {a}', f' b : {b}')

print(type(a))

print(type(b))

print('=' * 100)

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')