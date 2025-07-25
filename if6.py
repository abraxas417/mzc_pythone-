#if6.py

# 정수를 입력 받아서 양수, 음수, 0 인지를 출력하는 예제 프로그램입니다.

num = int(input("정수를 입력하세요 "))

if num > 0:
    print("정수")
elif num<0:
    print("음수")
else:
    print("0")