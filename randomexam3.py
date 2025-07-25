#randomexam3.py
# #알파벳 소문자와 숫자를 랜덤하게 조합하여 일회용 패스워드를 생성하는
# 프로그램을 만드세요. 패스워드의 길이는 6자리로 합니다. genPass()라는
# 함수를 작성하고 이 함수가 랜덤하게 생성된 패스워드를 반환하게 합니
# 다. 모두 3개의 패스워드를 생성하여 출력하도록 합니다

import random
import string
# def genPss():  //내가 끄적인거
#     for j in range(3):
#         password = ''
#         for i in range(6):
#             ch = random.choice(['1','2','3','4','5','6','7','8','9','10','a','b','c','d','e','f','g'])
#             password += ch
#         print(password)

# genPss()

def genpass():
    str = string. ascii_lowercase + string.digits
    password = ''

    for _ in range(6):  # 변수를 사용하지 않겠다는 의미
        password += random.choice(str)
    
    return password

print(genpass())
print(genpass())
print(genpass())