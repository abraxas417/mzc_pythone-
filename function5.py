# function5.py
# 원으 ㅣ면적을 구하는 함수 출력

#원의 면적을 구하는 함수정의
def get_area(radius) :
    area = 3.14 * radius ** 2
    return area

#함수 호출
result = get_area(3)
print("반지름이 3인 원의 먼적 = ",result)

result = get_area(20)
print("반지름이 20인 원의 먼적 = ",result)