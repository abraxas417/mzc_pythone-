#if4.py
#정수를 입력받아, 짝수인지 홀수인지 출력하는 코드를 작성

num = input("문자열을 입력하세요 :  ")
length = len(num)
mid = length // 2
if length % 2 == 0:
    print(f"가운데 문자: {num[mid -1]} {num[mid]}")
else:
    print(f"{num[mid]}")