#exam3_3.py
#물건을 구입할 때 구입액이 10만원 이상이면 5%의 할인을 받을 수 있다
#사용자에게 물건 구입금액을 물어보고 할인금액과 최종 지불금액을 출력

price = int(input("물건을 구입한 금액은 얼마입니까? "))

if price>100000:
    discount = int(price*0.05)
else:
    print(f"지불금액: {price}")

final = price - discount
print(f"물건 구입시 할인금액 : {discount}원") 
print(f"최종 지불금액: {final}원")