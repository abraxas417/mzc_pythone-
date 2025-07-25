#while2.py
# 사용자가 입력한 숫자를 더해서 합을 계산하는 프로그램. 입력을 계속할 건지 물어서 yes 를 입력하면 다음숫자 입력, no를 입력하면 합을 출력

answer= 'yes'
total = 0

while answer == 'yes':
    a = int(input("숫자를 입력하세요: "))
    total += a
    answer = input("계속(yes/no) ?")

print(f"입력한 숫자들의 합: {total}")