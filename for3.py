#for3.py

# 단을 입력 받아서 구구단을 출력하는 예제 프로그램입니다.

dan = int(input("단을 입력하세요: "))

for i in range(1, 10 ,1):
    print(f'{dan} * {i} = {dan * i}')

