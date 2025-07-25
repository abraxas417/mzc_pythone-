# while1.py
# while 문을 이용하여 구구단을 출력하세요

dan = int(input('원하는 단은: '))

i = 1

while i <= 9:
    print(f"{dan} * {i} = {dan*i}")
    i += 1