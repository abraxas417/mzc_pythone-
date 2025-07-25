#money.py

TARGET = 2000  #목표 금액
money = 1000   #초기 자금
year = 0       #연도
rate = 0.07   #이자율

while money < TARGET:
    money = money + money * rate
    year += 1


print(year,"년")