#while3.py

#학생들의 성적을 입력 받아 합계와 평균을 구하시오. 성적 입력을 끝내고 싶을 때는 점수에 음수를 입력한다. 평균은 소수 둘째자리까지 나타낸다.

print("입력을 종료하려면 음수를 입력하세요")
total = 0
count = 0
score = 0

while score >= 0:
   score = int(input("성적을 입력하세요"))
   if score >= 0:
      total += score
      count += 1
if count > 0:      
    aver = total / count
    print(f"합계 : {total} 평균: {aver:.2f}")
else:
    print("입력된 성적이 없습니다.")