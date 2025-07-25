#exam6.py
#실습문제 6번

number1,number2 = map(int,input("두 개의 정수를 입력하세요(공백) ").split())

print(f'number1 : {number1}')
print(f'number2 : {number2}')
print(f'{number1} + {number2} = {number1 + number2}')
print(f'{number1} - {number2} = {number1 - number2}')
print(f'{number1} * {number2} = {number1 * number2}')
print(f'{number1} / {number2} = {number1 / number2:.2f}')