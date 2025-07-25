#exam3_3.py
#숫자를 입력 받고 , 1부터 입력 받은 수까지의 합을 계산ㅁ하여 출력하는 프로그램

a= int(input("합을 계산할 숫자를 입력하세요: "))
total = 0
for i in range(1, a+1 ,1):
    total += i
    
print(f'1 부터 {a}까지의 합은 : {total}입니다.')