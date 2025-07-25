#연속 if 문

score= int(input("성적을 입력하세요: "))

if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60:
    print("D학점")
elif score <60:
    print("F학점")
else:
    print("성적을 올바르게 입력해주세요")