# function8.py

# 일치 인수 (positional, augument), 키워드(keword) 인수

def calc(x,y,z):
    print(f'x = {x}, y = {y}, z = {z}')


#함수 호출
calc(1,2,3)

calc(y=2, z=3, x=1)