#continue1.py

# for i in range(1,11):
#     if i%3 == 0:
#         continue
#     print(i,end = '')

#실습문제 10번
#사용자로부터 '-'이 포함된 계좌 번호를 입력 받아 '-'을 삭제한 문자열 출력
#예) 계좌번호를 입력하세요 : 321-03-235123

account_number = input("계좌 번호를 입력하세요 : ")

temp = ''
for ch in account_number:
    if ch == '-':
        continue
    temp += ch
    
print(temp)

