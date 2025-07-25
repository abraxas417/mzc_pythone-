
# random1.py
# 랜덤 함수에 대한 예제 프로그램입니다.

import random     #모듈

# for i in range(100):
#     num = random.randint(1, 10)
#     print(num)
for j in range(3):
    password = ''
    for i in range(6):
        ch = random.choice(['1','2','3','4','5','6','7','8','9','10','a','b','c','d','e','f','g'])
        password += ch
    print(password)