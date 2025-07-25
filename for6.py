#for6.py
#구구단을 출력하는 프로그램 예제입니다.


for k in range(1,10):
    for j in range(2,10):
        print(f'{j}*{k}={j*k}',end='\t')
    print()