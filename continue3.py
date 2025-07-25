#continue3.py

# #학생들의 성적이 리스트 자료로 있다. 성적을 체크해서 합격한 학생의 결과만
#  출력하는 프로그램. 60점 이상 합격 (continue문 사용)
#  예) scores = [ 90, 88, 34, 56, 67, 78, 88, 60, 59, 100 ]

scores = [90, 88, 34, 56, 67, 78, 88, 60, 59, 100]

for i in range(0, len(scores)):
    if scores[i] < 60:
        continue
    print(f"{i+1}번 학생 축하합니다 합격입니다.")
        