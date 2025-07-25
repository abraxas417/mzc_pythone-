#exam 7
#실습문제 7번

# 물건값 입력
price = int(input("물건값을 입력하세요 : "))

# 투입한 돈 입력
bill_1000 = int(input("1000원 지폐개수 : "))
coin_500 = int(input("500원 동전개수 : "))
coin_100 = int(input("100원 동전개수 : "))

# 총 투입 금액 계산
total = bill_1000 * 1000 + coin_500 * 500 + coin_100 * 100

# 거스름돈 계산
change = total - price

if change < 0:
    print("투입한 금액이 부족합니다.")
else:
    n500 = change // 500
    change %= 500
    n100 = change // 100
    change %= 100
    n10 = change // 10
    print("거스름돈")
    print(f"500원 = {n500} 100원 = {n100} 10원 = {n10}")
