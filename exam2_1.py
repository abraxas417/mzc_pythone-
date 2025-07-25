# exam2_1.py

#사용자로부터 두 수를 입력 받아 둘 중에서 큰 수를 출력하는 프로그램

a,b = map(int,input("두 개의 정수를 입력하세요(공백) ").split())

max_value= (a if a>b else b)

print(f'큰 값: {max_value}')

